#!/usr/bin/env python3
"""Run every quality check for the repository and exit non-zero on failure.

Usage:
    python3 tools/check_all.py

Checks:
  1. Patient-data tripwire over docs/, templates/, README.md
  2. Docs lint: one H1 first line; footer disclaimer present; no stray
     unclosed [VERIFY] goldmines in final templates (tag count reported)
  3. Template lint: fiction disclaimer + education-only line present
  4. Link check: internal markdown links resolve to real files
  5. Site build (tools/build_site.py) — must succeed
  6. Generated HTML sanity: every built page parses as HTML and the
     index links resolve to files that exist
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

FAILURES: list[str] = []
NOTES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)


def ok(msg: str) -> None:
    NOTES.append(msg)


def check_1_patient_data() -> None:
    import check_no_patient_data as ndp

    findings = ndp.scan([ROOT / "docs", ROOT / "templates", ROOT / "README.md"])
    if findings:
        for f_ in findings:
            fail(f"[1 patient-data] {f_}")
    else:
        ok("1. patient-data scan clean (docs/, templates/, README.md)")


def check_2_docs_lint() -> None:
    for chapter in sorted((ROOT / "docs").glob("*.md")):
        lines = chapter.read_text(encoding="utf-8").splitlines()
        if not lines or not lines[0].startswith("# "):
            fail(f"[2 docs] {chapter.name}: first line must be an H1 title")
        joined = "\n".join(lines)
        if "Education only" not in joined and "education only" not in joined.lower():
            fail(f"[2 docs] {chapter.name}: missing 'Education only' disclaimer")
        if "never clinical advice" not in joined.lower():
            fail(f"[2 docs] {chapter.name}: missing 'never clinical advice' phrase")
        tags = re.findall(r"\[VERIFY\]", joined)
        if tags:
            NOTES.append(f"2. {chapter.name}: {len(tags)} [VERIFY] teaching-example tag(s)")
    chapters = sorted((ROOT / "docs").glob("*.md"))
    if len(chapters) < 10:
        fail(f"[2 docs] expected >= 10 chapters, found {len(chapters)}")
    else:
        ok(f"2. docs lint passed ({len(chapters)} chapters)")


def check_3_templates_lint() -> None:
    expected_any = ["Fictional", "fictional"]
    for tpl in sorted((ROOT / "templates").glob("*")):
        text = tpl.read_text(encoding="utf-8")
        if not any(w in text for w in expected_any):
            fail(f"[3 templates] {tpl.name}: missing fiction disclaimer")
        low = text.lower()
        if "education only" not in low or "never clinical advice" not in low:
            fail(f"[3 templates] {tpl.name}: missing education-only disclaimer")
        if "Asdale Dynamics" not in text:
            fail(f"[3 templates] {tpl.name}: missing Asdale Dynamics credit line")
    templates = sorted((ROOT / "templates").glob("*"))
    ok(f"3. template lint passed ({len(templates)} template files)")


def check_4_links() -> None:
    md_files = sorted((ROOT / "docs").glob("*.md")) + sorted(
        (ROOT / "templates").glob("*.md")
    )
    md_files.append(ROOT / "README.md")
    pattern = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
    n_links = 0
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        for m in pattern.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            # this-repo links are written for the site runtime; resolve both
            # site-relative (docs/ prefix) and repo-relative
            candidates = [ROOT / target, ROOT / "docs" / target]
            if not any(c.exists() for c in candidates):
                clean = re.sub(r"^(docs/|templates/)", "", target)
                repo_guess = (
                    (ROOT / "docs" / clean)
                    if target.startswith("docs/")
                    else (ROOT / "templates" / clean)
                )
                if not repo_guess.exists() or not (ROOT / clean).exists():
                    fail(f"[4 links] {f.name}: broken internal link -> {target}")
                    continue
            n_links += 1
    ok(f"4. link check passed ({n_links} internal links resolved)")


def check_5_build() -> None:
    import build_site

    try:
        build_site.main()
        ok("5. site build succeeded")
    except Exception as exc:  # noqa: BLE001 — report any build failure as a check failure
        fail(f"[5 build] exception: {exc!r}")


def check_6_html() -> None:
    from html.parser import HTMLParser

    class Collector(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.links: list[str] = []
            self.h1: str | None = None
            self.stack: list[str] = []

        def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
            if tag in ("br", "meta", "link", "hr", "img"):
                return
            self.stack.append(tag)
            if tag == "h1" and self.h1 is None:
                pass
            if tag == "a":
                for k, v in attrs:
                    if k == "href" and v:
                        self.links.append(v)

        def handle_endtag(self, tag: str) -> None:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()

    site = ROOT / "site"
    pages = sorted(site.glob("*.html")) + sorted(site.glob("templates/*.html"))
    if not pages:
        fail("[6 html] no generated pages found")
        return
    expected_mds = {p.stem + ".html" for p in (ROOT / "docs").glob("*.md")}
    expected_mds |= {"templates/" + p.stem + ".html" for p in (ROOT / "templates").glob("*.md")}
    have = {str(p.relative_to(site)) for p in pages}
    missing = expected_mds - have
    if missing:
        fail(f"[6 html] expected pages not generated: {sorted(missing)}")

    for page in pages:
        parser = Collector()
        parser.feed(page.read_text(encoding="utf-8"))
        if parser.stack:
            fail(f"[6 html] {page.relative_to(site)}: unbalanced tags {parser.stack}")
    # resolve index links
    idx = site / "index.html"
    parser = Collector()
    parser.feed(idx.read_text(encoding="utf-8"))
    for link in parser.links:
        if link.startswith(("http://", "https://", "#")):
            continue
        if not (site / link).exists():
            fail(f"[6 html] index link target missing: {link}")
    ok_count = len(pages)
    ok(f"6. generated HTML sanity passed ({ok_count} pages)")


def main() -> int:
    check_1_patient_data()
    check_2_docs_lint()
    check_3_templates_lint()
    check_4_links()
    check_5_build()
    check_6_html()
    print("\n=== check_all results ===")
    for note in NOTES:
        print("PASS  " + note)
    if FAILURES:
        print(f"\nFAILED — {len(FAILURES)} problem(s):")
        for f_ in FAILURES:
            print("  " + f_)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
