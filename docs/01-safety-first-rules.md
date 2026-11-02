# Chapter 1 — Safety First: The Non-Negotiable Rules

Read this chapter once, slowly. Everything else in the manual builds on it.

## Rule 1: Education only, never clinical advice

This manual — and everything you create with it — is about *teaching
materials*. It is never:

- Guidance for treating an actual patient
- A substitute for institutional policy, protocols, or order sets
- A source for drug dosing, calculations, or clinical decision-making
- A replacement for your board of nursing, accreditation, or curriculum
  committee

If a learner's clinical question could affect real patient care, the answer
comes from your policy manual, your preceptor, and your faculty — not from an
AI chat, and not from this book.

## Rule 2: No real patient data, ever

This is the biggest one. **Never paste real patient information into any AI
tool.** Not "just this once," not "the AI is private," not "I removed the
name." Real patient details belong in the medical record, not in a chat box.

Banned from any prompt, ever, even partially:

- Names, initials, nicknames
- Dates of birth, ages paired with admission dates, admission/discharge dates
- Medical record numbers, account numbers, room and bed numbers
- Employers, addresses, phone numbers, email addresses
- Any story specific enough that a colleague could recognize the person
  ("the 36-year-old post-op from Tuesday night shift" — that's identifying)
- Photographs, screenshots, wound images, scan images

**Say it in categories instead:** a middle-aged adult with new shortness of
breath is fine. A 54-year-old named patient from Tuesday is not.

Everything in this manual's examples uses clearly fictional composites built
from textbook patterns, and every template in `templates/` includes a
"Fictional — not a real person" line. The included tool
`tools/check_no_patient_data.py` scans your files for common real-data
patterns (MRN-like numbers, DOB-style dates, URL-safe identifiers) before you
share or commit anything.

If you *have* already pasted patient data into a chat tool: follow your
organization's privacy-incident procedure immediately. Tell your privacy
officer. Do that first; recover later.

## Rule 3: The AI is a draft generator, not an authority

Language models predict plausible text. That means they can produce content
that is:

- Fluent and completely wrong (a made-up normal value)
- Half right (a real guideline cited from the wrong year)
- Confidently invented (a journal article that does not exist)

Treat every AI draft like a nursing student's strong first attempt: promising,
never signed off without review.

## Rule 4: Verify before a learner sees it

Before anything leaves your desk:

1. Facts and numbers → check against a current, reputable source.
2. Guidelines → confirm the **year and organization**.
3. Citations → confirm the article actually exists (Chapter 7).
4. Tone → read it once out loud; AI writing has a tells-and-hedges rhythm.
5. Clinical accuracy → your professional judgment; you are the safeguard.

## Rule 5: Keep grading and progress decisions human

AI can *draft* rubric wording and *suggest* feedback phrasing. The decision
about a real learner's progress — grades, remediation, readiness — stays with
qualified humans, following your institution's process. Never feed a real
learner's identifiable work to an AI tool without checking your institution's
policy on student data, intellectual property, and accessibility.

## Rule 6: Check your tool's terms — once, carefully

Before using any AI service with course material, skim:

- Does the vendor train on your inputs? (Many can be toggled off.)
- Is there an education or privacy tier?
- If learners will use it, is there a minimum age and what data is collected?

When in doubt, prefer **local tools** (running on your own machine) for
drafting sensitive-adjacent content — see Chapter 2 — or simply keep identities
and records out of the tool entirely, which is what this manual teaches.

## Quick audit: the 30-second safety checklist

Before you hit Enter on any prompt, ask:

- [ ] Am I typing **only** fictional/category-level details?
- [ ] Would this still work if I replaced every specific with "a sample"?
- [ ] Is my goal here teaching material, not clinical guidance?
- [ ] Am I prepared to verify whatever comes back?

Yes × 4 → proceed. This habit is the whole chapter in one breath.

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
