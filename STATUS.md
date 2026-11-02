# STATUS.md

**Project:** The AI Manual for Clinical Nurse Educators
**Owner:** Asdale Dynamics, LLC (Copyright (c) 2026 Asdale Dynamics, LLC)
**Scope rule:** Education only. Never clinical advice. No patient data anywhere.
**Status:** Complete and verified — all checks pass (exit 0).

## What was built

- **`docs/` — 11 chapters** of the manual (Markdown, printable):
  0. Introduction — who this is for and what it teaches
  1. Safety-first rules — no patient data, education-only, verification, human grading
  2. Prompting basics — five-part prompt pattern, five habits, local-tool note
  3. Lesson plans — objective fixing, template-driven drafts, four classic AI defects
  4. Case writing — fictional composites, closed cast, de-identification pass
  5. Simulations — scenario documents, role cards, facilitator notes, debrief frames
  6. Rubrics — shapes, level language, fairness bugs, feedback-only grade split
  7. Citation & hallucination checks — three hallucination types, five verification checks, worked fabricated-citation example, AI-use disclosure line
  8. Review workflow — PASS-QC ten-minute quality gate
  9. Accessibility notes — heading order, alt text, color, plain language, timing flexibility, grayscale printing
  10. Glossary — plain-language definitions
- **`templates/` — 8 files**: four fill-in templates (lesson plan, teaching case, simulation scenario, rubric) each in Markdown and print-ready plain text, all carrying fiction + education-only disclaimers and safety checklists.
- **`site/` — static HTML site** (generated, no JS): index with table of contents, one page per chapter and template, single readable stylesheet, print stylesheet (nav hidden, page-break control), mobile viewport, full keyboard navigation.
- **`tools/` — 2 scripts, standard library only:**
  - `build_site.py` — Markdown→HTML converter (headings, tables, fenced code, blockquotes, checkbox lists) and index/nav generator; re-runnable.
  - `check_no_patient_data.py` — tripwire scanner for MRN/DOB/SSN-like patterns, long digit runs, slash-dates, room/bed pairs, named-patient lines, phone numbers; includes `--selftest`.
  - `check_all.py` — runs every check: patient-data scan, docs lint (H1 first, disclaimers), template lint (fiction + education-only + credit lines), internal-link resolution, full site build, generated-HTML tag-balance and link-target validation.
- **`LICENSE`** — MIT, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`.
- **`README.md`** — overview, run instructions, credit to Asdale Dynamics, LLC.

## How to run it

Requires Python 3.9+ (standard library only; no packages to install).

```bash
# Build the static site from docs/ and templates/ into site/
python3 tools/build_site.py

# Run ALL checks (build included); exit 0 = everything passes
python3 tools/check_all.py

# Verify the patient-data scanner itself catches planted patterns
python3 tools/check_no_patient_data.py --selftest
```

Read the manual by opening `site/index.html` in any browser; every page prints cleanly (print stylesheet included) for offline classroom use.

## Verification results (final run, exit code 0)

- Patient-data scan clean over `docs/`, `templates/`, `README.md` — PASS
- Docs lint passed (11 chapters; each starts with H1 and carries both disclaimers) — PASS
- Template lint passed (8/8 files have fiction + education-only + credit lines) — PASS
- Internal-link check passed — PASS
- Site build succeeded (11 chapter pages + 4 template pages + 4 print-ready text files + stylesheet + index) — PASS
- Generated-HTML sanity: 16 pages parse with balanced tags; all index links resolve — PASS
- Negative test: planted MRN/DOB/SSN/phone/patient-name patterns in a scratch file were all detected (10 findings across 9 pattern types), and clean files pass — PASS
- No secrets, API keys, or personal data in any file; all examples are labeled fictional composites — verified by manual review plus the scanner

## Known gaps

- The Markdown converter covers the constructs used in this repo (headings, tables, fenced code, blockquotes, lists with checkboxes, inline styles) — it is not a full CommonMark implementation and may render arbitrary third-party Markdown imperfectly.
- The patient-data scanner is a heuristic tripwire, not a de-identification guarantee; the human eyeball pass in Chapter 1 is always still required.
- No PDF generation — printing is browser "print to PDF" via the included print stylesheet.
- No search function, dark mode, or multi-language output in `site/`.
- AI prompting examples are tool-agnostic by design; specific product click-paths change too fast to teach, so they are intentionally omitted.
- Automation coverage for other formats (DOCX/EPUB export) is not included.

## Git

Repository initialized locally with a single plain-message commit (no Co-authored-by trailers, no remote, nothing pushed or published).
