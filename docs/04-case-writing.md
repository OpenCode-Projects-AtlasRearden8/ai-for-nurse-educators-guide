# Chapter 4 — Case Writing: Fictional, De-Identified, Usable

Teaching cases are the highest-value documents you can draft with AI — because
the *pattern* of a good case is formulaic, and formulaic is where AI shines.
The danger is equally real: cases written carelessly can smuggle in real
patient details or clinical-decision content. This chapter shows the pipeline
that keeps cases fictional, useful, and safe.

## The three hard rules for AI-generated cases

1. **Fictional composites only.** Built from textbook patterns and plausible
   human factors, never from a real encounter. If it feels like "that Tuesday
   patient," stop — that's Rule 2 of Chapter 1.
2. **Education only.** The case's learning point is a concept (communication,
   ethics, teamwork, documentation *habits*, safety culture), not clinical
   decision-making, not dosing, not diagnosis.
3. **Label it.** Every case opens with: *"Fictional teaching case — characters
   and settings are invented composites with no connection to any real
   person."*

## Choose the learning point before the plot

Beginners write "a case about a person"; educators write "a case about a
concept wearing a person costume." Decide the concept first:

- Communication breakdown (handoff, escalation, clarification)
- Documentation habits (timeliness, precision, correction)
- Ethics of privacy and disclosure (great for education-only settings)
- Team dynamics across roles
- Safety culture: reporting, follow-up, learning-from-near-miss
- Fatigue, workload, and cognitive load in shift work

Then ask the AI for a **situation** that exercises exactly that concept.

## The fictional detail bank

To help the AI generate nothing identifiable, give it a closed cast list.
Prompt pattern:

```text
We will use ONLY these fictional composite characters and settings. Do not
invent names, locations, dates of birth, medical record numbers, or any
identifying details beyond this list.

CAST (all fictional):
- R. Okafor, an experienced evening-shift coordinator at a fictional
  community education center (never a named facility)
- J. Lindgren, a new volunteer coordinator, first week on the job
- Setting: an after-school program that runs medication-adjacent paperwork
  only in the abstract — no real student records
- The concept under study: a rushed verbal handoff that loses one document
  and leads to duplicated work, discovered the next morning
```

A closed cast lets AI write richly *charactered* cases (which is the value)
while bounding it away from anything real. Swap the cast to your discipline:
for nurse-educator sessions, "fictional training sim center staff member R.O."
brings clinical texture without clinical stakes.

## Structure that keeps cases teachable

Aim for 250–400 words in four layers:

1. **Setting** (one sentence, fictional): where, when (weekday/shift), roles.
2. **Friction** (two or three sentences): what went wrong or got tangled —
   build from *human and process* failure, not diagnosis.
3. **Human response** (the size of an iceberg): two to four plausible actions
   someone took, some right, some questionable. Don't fix it; *leave the case
   unresolved*.
4. **Discussion questions** (three to five): use verbs from Bloom's levels —
   *identify, contrast, prioritize, justify, propose*.

### Example skeleton (fictional, non-clinical)

```text
Fictional teaching case — invented composite, not a real person.

Friday evening shift at City Library Annex (fictional). R. Okafor, the
evening coordinator, hands the closing duties to trainee J. Lindgren with
three lines in a text message instead of the standard checklist. Two of the
three are misread because of the abbreviation "ctd" — J. assumes "carts to
desk"; R. means "count the returned-date stamp." The next morning, surveillance
footage review discovers a cart left in the overflow area and one returned-date
stamp unaccounted for until noon.

Discussion questions:
1. Identify every point where the message could have been clarified.
2. Contrast verbal-only handoff with checklist-based handoff in this situation.
3. Propose a two-line checklist text that would have survived abbreviation.
4. Justify why "mark the abbreviation" is or is not enough on its own.
```

Note deliberately *non-nursing props* (date stamp, cart) — enough texture to
feel real, nothing that walks into clinical-decision territory. For a purely
educator-skills session, this is the sweet spot.

## Case-writing prompt pattern (the workhorse)

```text
Role: Chair of a fictional committee drafting teaching cases for professional
volunteer coordinators.

Task: Write a 350-word fictional teaching case about [a concept], using only
the cast and setting listed below. Leave the situation unresolved and write 4
discussion questions using Bloom's verbs (two at lower levels, two at higher).

Audience: [students level].

Format:
- First line: "Fictional teaching case — invented composite."
- Paragraph 1: setting (one sentence).
- Paragraph 2: the friction.
- Paragraph 3: human actions taken (2–4).
- Then: "Discussion questions:" list.

Constraints: No names beyond the cast, no real institutions, no dates with
more than day-of-week precision, absolutely no real patient or student data of
any kind, no medication decisions or doses of any kind. Education-focused; the
teach point is [concept]. Mark any factual claim [VERIFY].
```

Generate three versions, pick the best, merge what's good from the other two.
Generation is cheap; judgment is not — so spend judgment at exactly the step
where it buys the most.

## De-identification pass with human eyes

Even after AI, run the eyeball test:

- **Specifics creep.** "a 36-year-old with a Tuesday med-surg admission" —
  that's a fingerprint a colleague could recognize; cut or genericize it.
  Weekday and role textures ("Friday evening shift") are fine — they're
  atmosphere, not identity.
- **Tool-test creep.** If any line of your case implies a specific real
  facility, system, form, or company, genericize it ("the center's intake
  form").
- **Reality test.** Ask one colleague to read it cold: "Could this be an
  actual event at us?" If yes, fictionalize something visible.

Then run the automated pass:

```bash
python3 tools/check_no_patient_data.py docs/ templates/
```

## What to do when the AI drifts clinical

Written mostly as-is above, cases tend to stay put. But if a correction or a
line slides into dosing, diagnostics, or clinical guidance — the manual stops
being educational and starts being something it must never be — take the low
road: cut the line, not a rewrite. Restate the same *educational mechanism*
(clarification, escalation, documentation, teamwork) in non-clinical terms and
have the AI re-draft just that line. This keeps you commercially and
ethically clean: education-only, always.

## The case revision loop that actually saves time

1. **Draft** with the workhorse prompt (3 versions).
2. **Fact-pass:** everything tagged [VERIFY] checked against current, reputable
   sources; anything fragile gets rewritten as a *principle*, not a stat.
3. **De-identification pass** by eyeball + the provided checker.
4. **Read-aloud pass:** any sentence you stumble on, rewrite shorter.
5. **Usability pass:** can your least-experienced student finish it in 6
   minutes? If not, cut one character or one sentence of friction.

Ten minutes total, and your case is classroom-ready.

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
