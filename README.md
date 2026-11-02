# The AI Manual for Clinical Nurse Educators

**Education only. Never clinical advice.**

A plain-English, beginner-friendly guide for clinical educators and nurse
educators who want to use AI tools to draft lesson plans, write fictional
teaching cases, build simulation scenarios, and grade with rubrics — safely,
accessibly, and without ever putting patient data at risk.

Built the way Dylan Asdale explains AI: like a friend would. Step by step,
never condescending.

Published by **Asdale Dynamics, LLC**.

## What's inside

| Path | What it is |
| --- | --- |
| `docs/` | The manual, chapter by chapter (Markdown) |
| `site/` | A static, printable HTML version of the manual (generated) |
| `templates/` | Fill-in lesson plans, case outlines, sim scenarios, rubrics |
| `tools/` | Helpers: a no-patient-data scanner, a link/claim checker, and the site builder |

## Quick safety rules (from Chapter 1)

1. This manual is for **teaching materials only**. It is never clinical advice.
2. **Never paste real patient data** into an AI chat — no names, MRNs, dates of
   birth, room numbers, or "this one patient I had last week" stories.
3. Treat every AI draft as a **rough draft**. You are the content expert; the
   AI is the fast typist.
4. **Verify every citation** before you hand something to a learner. AI can
   invent references that look perfectly real.
5. Keep decisions about curriculum, grading, and learner progress **human**.

## How to run it

Requirements: Python 3.9+ (standard library only — no installs needed).

```bash
# Build the static site from docs/ into site/
python3 tools/build_site.py

# Run all checks (no patient data patterns, broken internal links, template sanity, build, HTML)
python3 tools/check_all.py

# Optional: verify the patient-data scanner itself
python3 tools/check_no_patient_data.py --selftest
```

Open `site/index.html` in any browser to read the manual. Every page is
ready to print for offline use in a classroom or skills lab.

## Templates

Copy any file in `templates/` (Markdown or the plain-text `.txt` variants)
and fill in the bracketed placeholders. They are deliberately generic so they
work for fundamentals, med-surg, psych, community, or any other course.

## Accessibility notes

See `docs/09-accessibility.md`. Highlights: heading-order discipline, alt text,
color-independent cues, no timing traps, and printable layouts that work in
grayscale. The generated site uses a single stylesheet with readable default
font sizes and full keyboard navigation.

## Known limits

AI outputs vary by tool and week. The manual teaches **transferable habits**
(prompting patterns, verification steps, review workflows) rather than
click-paths that expire. Verify anything factual against current, reputable
sources before teaching from it.

## License

MIT — see `LICENSE`. Copyright (c) 2026 Asdale Dynamics, LLC.

This project is education material. It contains no patient data, no secrets,
and no personal information. Fictional cases are labeled as fictional.
