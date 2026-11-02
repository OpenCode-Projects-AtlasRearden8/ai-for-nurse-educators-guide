# Chapter 2 — Prompting Basics, in Plain English

An AI writing tool is like a very fast new graduate: enthusiastic, tireless,
and in need of clear instructions. This chapter teaches five habits that make
almost any AI tool output better.

## The five-part prompt pattern

You do not need magic words. You need five parts:

1. **Role** — who the AI should write as.
2. **Task** — the one thing you want produced.
3. **Audience** — who it's for and what they already know.
4. **Format** — the shape of the output (sections, word count, headings).
5. **Constraints** — the rules: fictional only, no citations unless verified,
   plain language, education only.

### Example prompt (good)

```text
Role: You are a nurse educator writing teaching materials.

Task: Draft a 20-minute lesson plan on hand hygiene as an infection-prevention
behavior.

Audience: First-year pre-nursing community-college students. No clinical
experience. Assume they know what a hospital is and nothing else.

Format: Give me — (1) one learning objective written in "learner will be able
to" form, (2) a 5-minute hook question, (3) a 10-minute mini-lecture outline
with three talking points, (4) a 5-minute active-learning activity, (5) an
exit-ticket question.

Constraints: Content is fictional teaching material. Include NO drug names,
NO doses, NO clinical decision guidance. Keep language plain (short sentences,
no jargon without a definition). If you state any factual claim, mark it with
[VERIFY] so I can check it.
```

### Example prompt (weak — and why)

```text
Write a lesson plan about hand hygiene.
```

What's missing: audience level, length, format, and the fiction/safety
constraints. You'll get something generic that doesn't fit your room, and
nothing marked for verification. The five-part pattern fixes all of it.

## Habit 1: Iterate, don't restart

Treat the first answer as draft one. Follow up in the same chat:

- "Make the activity doable with only paper and chairs."
- "Rewrite the objectives at Bloom's *analyze* level instead of *remember*."
- "Cut this to 150 words. Keep the same structure."

Same conversation, small adjustments — that's where the quality lives.

## Habit 2: Ask for structure before prose

Two-step beats one-step for long documents:

1. "Give me an outline only: section headings for a rubric for a written
   case-analysis assignment. No prose."
2. Approve or fix the outline, *then*: "Good. Now write section 2 only."

This prevents 900 words you have to throw away.

## Habit 3: Put the constraints where they can't slip

The phrase that pays: *"If you are not certain, say so instead of guessing."*
Add *"Do not invent citations, numbers, or guideline names. Mark uncertain
claims with [VERIFY]."* These single lines prevent most hallucination damage
at the source (see Chapter 7).

## Habit 4: Neutralize the "polite guessing" trap

AI tools rarely say "I don't know." If a prompt implies an answer exists,
it will invent a plausible one. Use the error bar honestly:

```text
List the five most common reasons first-semester students report feeling
overwhelmed, based on general patterns you know about. For each, write
[CONFIDENCE: high/medium/low] so I know which of these is solid teaching
material versus something I should double-check.
```

Confidence markers turn an invisible risk into a visible checklist.

## Habit 5: Give the AI your format, not the reverse

Paste in an empty template (like the ones in `templates/`) and say:

```text
Fill in this template using fictional, category-level details only. Leave
[VERIFY] markers on every factual claim. Do not use medication names or doses.
```

This is the single most reliable move in the whole manual. The template carries
your standards; the AI just fills the boxes.

## Working without an internet connection (local tools)

Some educators prefer tools that run entirely on their own laptop — nothing
typed leaves the machine. The prompting skills in this chapter are identical
for local tools; the only differences are setup and speed. If privacy from a
cloud vendor is your worry, remember: the bigger protection is Rule 2 (no real
data in the tool at all), not which tool you pick.

## Do / Don't quick card

| Do | Don't |
| --- | --- |
| Say who the audience is | Assume "default" level works |
| Ask for outlines first | Ask for a 5-page document cold |
| Mark uncertainty with [VERIFY] | Ship unverified specifics |
| Fill in your own template | Let the AI choose your format |
| Iterate in the same chat | Start a fresh chat for every tweak |
| Keep details fictional and category-level | Paste anything real, ever |

## Practice: your first five prompts

Try these today (all safe, all fictional):

1. Rewrite this confusing paragraph in plain language for first-semester
   students. Keep my meaning exactly.
2. Generate 10 multiple-choice distractor rationales for a question about
   stereoscopic vision; mark each [CONFIDENCE] level.
3. Turn this bulleted list into a two-column table: observable behavior |
   why it matters in the learning lab.
4. Draft three role-play lines for a fictional "anxious first-day student."
5. Suggest five titles for a handout, each under 8 words, no exclamation
   points.

Each one is small, low-stakes, and builds the muscle. That's the whole skill.

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
