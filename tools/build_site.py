#!/usr/bin/env python3
"""Build the static HTML site from docs/ and templates/.

Standard library only. Run:
    python3 tools/build_site.py

Reads docs/*.md and templates/*.md, converts them to printable HTML pages,
writes site/index.html, site/style.css, and one page per source file.
Re-running overwrites site/ output for these files (idempotent).
"""
from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATES = ROOT / "templates"
TOOLS = ROOT / "tools"
SITE = ROOT / "site"

SITE_TITLE = "The AI Manual for Clinical Nurse Educators"
FOOTER_NOTE = (
    "Education only. Never clinical advice. Fictional examples only — "
    "no patient data. Published by Asdale Dynamics, LLC. MIT licensed; "
    "see the repository's LICENSE."
)


# --------------------------------------------------------------------------
# Markdown -> HTML (supported: headings, paragraphs, fenced code, tables,
# blockquotes, ordered/unordered lists with checkboxes, hr, inline styles)
# --------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Convert inline markdown to HTML, escaping everything else."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", out)
    out = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: _link(m.group(1), m.group(2)),
        out,
    )
    return out


def _link(label: str, target: str) -> str:
    """Resolve a markdown link target to a site-local or external href."""
    schemes = ("http://", "https://")
    if not target.startswith(schemes):
        if target.endswith(".md"):
            target = target[: -len(".md")] + ".html"
            if not target.startswith(("docs/", "templates/")):
                # bare chapter name, e.g. templates/lesson-plan-template.md
                if target.startswith("templates/"):
                    pass  # already site-relative
                else:
                    target = "docs/" + target
            target = target.replace("docs/", "").replace(
                "templates/", "templates/", 1
            )
        elif target.endswith(".txt"):
            if not target.startswith("templates/"):
                target = "templates/" + Path(target).name
    closed = html.escape(target, quote=True)
    return f'<a href="{closed}">{label}</a>'


def _md_to_html(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    para: list[str] = []

    def flush() -> None:
        if para:
            out.append(f"<p>{_inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            flush()
            block: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1  # move past closing fence
            out.append("<pre><code>" + html.escape("\n".join(block)) + "</code></pre>")
            continue

        if (
            line.startswith("|")
            and i + 1 < len(lines)
            and re.match(r"^\|(\s*:?-+:?\s*\|)+\s*$", lines[i + 1])
        ):
            # simple table with a separator row on the next line
            flush()
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows: list[list[str]] = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = "".join(f"<th>{_inline(c)}</th>" for c in header)
            body = "".join(
                "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
                for r in rows
            )
            out.append(
                f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
            )
            continue

        if line.startswith(">"):
            flush()
            content: list[str] = []
            while i < len(lines) and lines[i].startswith(">"):
                content.append(lines[i].lstrip(">").strip())
                i += 1
            # wrap-wrapped quotes become one paragraph; blank ">" lines split them
            paragraphs: list[str] = []
            buf: list[str] = []
            for c in content:
                if c == "":
                    if buf:
                        paragraphs.append(" ".join(buf))
                        buf = []
                else:
                    buf.append(c)
            if buf:
                paragraphs.append(" ".join(buf))
            inside = "".join(f"<p>{_inline(c)}</p>" for c in paragraphs if c.strip())
            out.append(f"<blockquote>{inside}</blockquote>")
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            text_ = m.group(2).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", text_.lower()).strip("-")
            out.append(f'<h{level} id="{slug}">{_inline(text_)}</h{level}>')
            i += 1
            continue

        if re.match(r"^-{3,}\s*$", line) or re.match(r"^\*{3,}\s*$", line):
            flush()
            out.append("<hr>")
            i += 1
            continue

        m_ul = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        m_ol = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m_ul or m_ol:
            flush()
            is_ol = bool(m_ol)
            first = (m_ol or m_ul).group(1)
            base_indent = len(first.replace("\t", "    "))
            items: list[str] = []
            pattern = r"^(\s*)\d+\.\s+(.*)$" if is_ol else r"^(\s*)[-*]\s+(.*)$"
            while i < len(lines):
                m2 = re.match(pattern, lines[i])
                if not m2:
                    # allow a wrapped continuation line (indented, non-blank)
                    if (
                        lines[i].strip()
                        and not lines[i].lstrip().startswith(("#", ">", "```", "|"))
                        and (len(lines[i]) - len(lines[i].lstrip())) > base_indent
                        and items
                    ):
                        items[-1] = items[-1] + " " + lines[i].strip()
                        i += 1
                        continue
                    break
                indent = len(m2.group(1).replace("\t", "    "))
                if indent <= base_indent:
                    items.append(m2.group(2).strip())
                else:
                    # flatten deeper nesting with an arrow marker
                    items.append("\u21b3 " + m2.group(2).strip())
                i += 1
            rendered: list[str] = []
            for item in items:
                m_check = re.match(r"^\[( |x|X)\]\s+(.*)$", item)
                if m_check:
                    box = "\u2610" if m_check.group(1) == " " else "\u2611"
                    rendered.append(
                        f'<li class="check">{box} {_inline(m_check.group(2))}</li>'
                    )
                else:
                    rendered.append(f"<li>{_inline(item)}</li>")
            tag = "ol" if is_ol else "ul"
            out.append(f"<{tag}>\n" + "\n".join(rendered) + f"\n</{tag}>")
            continue

        if not line.strip():
            flush()
            i += 1
            continue

        para.append(line.strip())
        i += 1

    flush()
    return "\n".join(out)


# --------------------------------------------------------------------------
# Page generation
# --------------------------------------------------------------------------

def _title_of(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


CSS = """:root{--ink:#1d2733;--soft:#5a6b7d;--line:#d8e0e8;--bg:#fbfcfd;--accent:#0b6b6b;--mark:#faf3d1}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 Georgia,'Times New Roman',serif}
.wrap{max-width:52rem;margin:0 auto;padding:1.4rem 1.2rem 3rem}
header.site{border-bottom:3px solid var(--accent);padding:.9rem 0 .6rem}
header.site h1{font-size:1.05rem;margin:0;font-family:system-ui,Segoe UI,Helvetica,sans-serif;letter-spacing:.02em}
header.site p{margin:.15rem 0 0;color:var(--soft);font-size:.85rem;font-family:system-ui,Segoe UI,Helvetica,sans-serif}
nav.top,nav.bottom{font-family:system-ui,Segoe UI,Helvetica,sans-serif;font-size:.9rem;margin:.6rem 0}
nav.top a,nav.bottom a,article a{color:var(--accent)}
nav.bottom{display:flex;gap:1rem;justify-content:space-between;border-top:1px solid var(--line);padding-top:.8rem;margin-top:2rem}
article h1{font-size:1.75rem;line-height:1.25;margin:.4rem 0 1rem}
article h2{font-size:1.3rem;margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.25rem}
article h3{font-size:1.08rem;margin-top:1.6rem}
blockquote{margin:1.2rem 0;padding:.7rem 1rem;border-left:4px solid var(--accent);background:var(--mark)}
blockquote p{margin:.3rem 0}
code{font-family:ui-monospace,Consolas,monospace;font-size:.86em;background:#eef2f6;padding:.08em .35em;border-radius:3px}
pre{background:#eef2f6;border:1px solid var(--line);border-radius:6px;padding:.8rem .9rem;overflow-x:auto}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1.1rem 0;font-size:.92rem;text-align:left}
th,td{border:1px solid var(--line);padding:.45rem .6rem;vertical-align:top}
th{background:#eef2f6;font-family:system-ui,Segoe UI,Helvetica,sans-serif;font-size:.85rem}
ul.check{list-style:none;padding-left:.2rem}
ul.check li{margin:.45rem 0}
hr{border:none;border-top:1px solid var(--line);margin:2rem 0}
footer.site{border-top:1px solid var(--line);margin-top:2.4rem;padding-top:.9rem;color:var(--soft);font-size:.82rem;font-family:system-ui,Segoe UI,Helvetica,sans-serif}
ul.toc{font-size:1.02rem}
ul.toc li{margin:.55rem 0}
@media print{body{background:#fff;font-size:11.5pt}
header.site,nav.top,nav.bottom{display:none}
.wrap{max-width:none;padding:0}
article h1{page-break-before:always}
article h1:first-of-type{page-break-before:auto}
blockquote,pre,table{page-break-inside:avoid}}
"""


def _page(title: str, body_html: str, top_nav: str, bottom_nav: str, base: str = "") -> str:
    html_title = title if title == SITE_TITLE else f"{title} — {SITE_TITLE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(html_title)}</title>
<link rel="stylesheet" href="{base}style.css">
</head>
<body>
<div class="wrap">
<header class="site">
<h1>{SITE_TITLE}</h1>
<p>Education only. Never clinical advice.</p>
</header>
<nav class="top">{top_nav}</nav>
<article>
{body_html}
</article>
<nav class="bottom">{bottom_nav}</nav>
<footer class="site">
<p>{FOOTER_NOTE}</p>
<p>Copyright (c) 2026 Asdale Dynamics, LLC.</p>
</footer>
</div>
</body>
</html>
"""


def _chapter_nav(chapters: list[tuple[str, str]], idx: int) -> tuple[str, str]:
    top = '<a href="index.html">&larr; Contents</a>'
    if idx > 0:
        prev_title, prev_file = chapters[idx - 1]
        prev_html = f'<a href="{prev_file}">&larr; {html.escape(prev_title)}</a>'
    else:
        prev_html = "<span></span>"
    if idx + 1 < len(chapters):
        next_title, next_file = chapters[idx + 1]
        next_html = f'<a href="{next_file}">{html.escape(next_title)} &rarr;</a>'
    else:
        next_html = '<a href="index.html">Contents &uarr;</a>'
    return top, prev_html + next_html


def _readme_of_templates(printable: list[Path]) -> str:
    lines = "".join(
        f'<li><a href="templates/{p.name}">{p.name}</a> (print-ready)</li>'
        for p in printable
    )
    return (
        "<p>Also included as print-ready plain-text files:</p><ul>" + lines + "</ul>"
    )


def main() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "templates").mkdir(parents=True)
    (SITE / "style.css").write_text(CSS, encoding="utf-8")

    chapters: list[tuple[str, str]] = []   # (title, site-relative filename)
    templates: list[tuple[str, str]] = []

    for md in sorted(DOCS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        title = _title_of(text)
        body = _md_to_html(text)
        filename = md.stem + ".html"
        chapters.append((title, filename))
        top, bottom = _chapter_nav(chapters, len(chapters) - 1)
        (SITE / filename).write_text(_page(title, body, top, bottom), encoding="utf-8")

    for md in sorted(TEMPLATES.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        title = _title_of(text).replace(" (fill in the brackets)", "")
        title = title.replace(" (criteria × levels, fill in the brackets)", "")
        body = _md_to_html(text)
        filename = "templates/" + md.stem + ".html"
        templates.append((title + " (template)", filename))
        (SITE / filename).write_text(
            _page(
                title,
                body,
                '<a href="../index.html">&larr; Contents</a>',
                '<a href="../index.html">Contents &uarr;</a>',
                base="../",
            ),
            encoding="utf-8",
        )

    printable = sorted(TEMPLATES.glob("*.txt"))
    for p in printable:
        shutil.copyfile(p, SITE / "templates" / p.name)

    toc = "".join(f'<li><a href="{f}">{html.escape(t)}</a></li>' for t, f in chapters)
    tpl_toc = "".join(
        f'<li><a href="{f}">{html.escape(t)}</a></li>' for t, f in templates
    )
    txt_items = "".join(
        f"<li><code>templates/{p.name}</code></li>" for p in printable
    )
    tools_item = (
        '<li><code>tools/check_no_patient_data.py</code> — scans for patient-data'
        " patterns before you share or commit</li>"
    )
    index_body = f"""<h1>{SITE_TITLE}</h1>
<p>A plain-English guide for clinical nurse educators using AI to draft
lesson plans, fictional teaching cases, simulation scenarios, and rubrics —
safely, accessibly, and with zero patient data, ever.</p>
<blockquote><p><strong>Education only. Never clinical advice.</strong></p></blockquote>
<h2>Chapters</h2>
<ul class="toc">
{toc}
</ul>
<h2>Fill-in templates</h2>
<ul class="toc">
{tpl_toc}
</ul>
<h2>Print-ready plain-text templates</h2>
<ul>
{txt_items}
</ul>
<h2>Tools</h2>
<ul>
{tools_item}
</ul>
<p>Before sharing anything you drafted with AI, run the checker:</p>
<pre><code>python3 tools/check_no_patient_data.py docs/ templates/</code></pre>
{_readme_of_templates(printable) if printable else ""}
"""
    (SITE / "index.html").write_text(
        _page(SITE_TITLE, index_body, "", ""), encoding="utf-8"
    )
    (SITE / "GENERATED.txt").write_text(
        "All files in this directory are generated by tools/build_site.py.\n"
        "Edit docs/ or templates/ instead, then rebuild:\n"
        "    python3 tools/build_site.py\n"
        "Verify with:\n"
        "    python3 tools/check_all.py\n",
        encoding="utf-8",
    )
    print(
        f"Built {len(chapters)} chapters, {len(templates)} template pages, "
        f"{len(printable)} print-ready files -> {SITE}/"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
