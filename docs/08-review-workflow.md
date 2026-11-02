# Chapter 8 — The Review Workflow: Your Quality Gate

Every previous chapter ends with "you check it before learners see it." This
chapter makes that check **systematic** — one workflow you run on every AI
draft, in under ten minutes, so quality is a habit rather than a heroics.

## The PASS-QC workflow

**P — Purpose.** Does this draft serve the stated learning objective? One
sentence answer. If you can't say it, cut or refocus the draft before editing
words.

**A — Accuracy.** All `[VERIFY]` tags cleared or rewritten as principles.
Guideline/spec years confirmed. Numbers traced or deleted (Chapter 7).

**S — Safety.**
- No patient data of any kind — automated check plus eyeball check (Chapter 1).
- No clinical decision guidance slipped in (education only, always).
- Fiction labeled on every teaching case and sim scenario.

**S — Suitability.** Right level for your actual learners? Activities doable
in your actual room, with your actual prep budget? Timing survives a real
clock (cut timing by half for any activity the AI proposed)?

**Q — Quality of language.** Read-aloud pass. Sentence you stumble on = rewrite
shorter. Watch for AI tells: hedges stacked on hedges, empty adjectives
("crucial," "vital"), and the comma-splice flourish.

**C — Care (fairness & accessibility).** The Chapter 9 checklist: headings in
order, alt text, no color-only cues, no timing traps, plain language,
printable in grayscale.

## Standing in ten minutes

| Step | Time | What you actually do |
| --- | --- | --- |
| P | 1 min | Say the objective out loud; compare to draft |
| A | 3 min | Clear every [VERIFY]; own-eyes guideline/year check |
| S | 2 min | Run the checker script; skim for any real-data pattern |
| S | 2 min | Timing/room/level sanity pass |
| Q | 1 min | Read the first paragraph and every heading aloud |
| C | 1 min | Accessibility quick-list |

Ninety seconds per step is deliberate — this workflow only survives if it's
cheap. Twenty minutes and you won't run it; ten minutes and you will.

## What to do when the draft fails a step

Fail **A** → try fixing in the same chat: "Rewrite without any statistics or
guideline names; state each as a principle." This conversion is almost always
possible and usually improves teachability.

Fail **S (safety)** → never salvage. Cut the offending line entirely, no
rewrite. Safety failures aren't editing problems; they're scope problems.

Fail **S (suitability)** → tell the AI the constraint you discovered ("my room
has 6 tables and no tech") and regenerate only the activity section.

Fail **Q** → usually a signal the draft was too long. Cut 30% and the Q
problems mostly vanish on their own.

Fail **C** → do the fix now, not the night before class. Accessibility fixes
are fast when early, painful when late.

## The "regenerate vs. edit" decision

The instinct is to keep editing a flawed draft. But AI regeneration is cheap:

- **Edit** when the structure is right and the wording is close.
- **Regenerate** when the structure is wrong (wrong activity shape, wrong
  scenario for your room), because wording-level fixes on a wrong structure
  eat hours.

Rule of thumb: if your third edit is targeting the same paragraph, stop and
regenerate the section instead.

## Version habits (lightweight, not bureaucratic)

Save every accepted draft with a suffix you can grep: `_v2_final`.

Write one line in a running note file per artifact:

```text
2026-03-05  case_handoff_v2  — PASS-QC: A ✓ (2 numbers deleted), S ✓, 
              timing cut 25→10 min. Debuted with Tuesday cohort.
```

Three seconds to write; priceless when you teach the same material next
semester and can't remember why v2 lost the statistics. (It was because of
Chapter 7. You'll thank you.)

## Team use: the peer-review ask

When a colleague reviews your AI-assisted material, ask exactly two questions:

1. "Would you have caught the same [VERIFY] flags I did — did any slip?"
2. "Is the fiction label visible enough that a tired you, at 9pm, won't read
   this as real?"

That's it. Two questions, not fifteen. Peer review of AI material fails when
it becomes full-document line editing — which is your job, not theirs — or
when it's skipped entirely.

## Your standing reminder

Every AI draft is a **gift of time-gained for review time spent**. The workflow
exists to spend that gained time on the parts only a human educator can
judge: fit, tone, fairness, and truth. Run PASS-QC every time, and you'll
rarely be caught out by the one draft that deserved it.

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
