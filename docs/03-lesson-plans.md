# Chapter 3 — Lesson Plans with AI

A lesson plan is just a promise you make to yourself: *by the end of this
session, learners will be able to do X, and here's how we'll get there.* AI is
excellent at the connective tissue — timing, transitions, activity shapes —
and bad at deciding what matters in your course. You decide the destination;
the AI paves the road.

## Anatomy of a lesson plan (the parts AI can help draft)

| Part | What it is | AI draft quality |
| --- | --- | --- |
| Learning objective(s) | Observable, measurable, learner-level | Good per draft; needs verb-leveling |
| Hook / anticipatory set | Opens the session, grabs attention | Good — expects editing |
| Content outline | Talking points, key concepts | Good — needs fact check |
| Active learning activity | Practice, discussion, simulation | Mostly human-critical; AI can frame |
| Materials & prep list | What you need in the room | Very good |
| Assessment / exit ticket | How you'll know objective was hit | Good, one exit ticket per objective |
| Timing map | Minutes per segment | Very good |
| Access & inclusion notes | How the plan works for all learners | Good starting notes |

## Step 1: Fix the objective first

Garbage objectives in, garbage plans out. A usable objective:

- Names an **observable learner behavior** (list, demonstrate, compare,
  prioritize, teach-back) — not "understand" or "appreciate"
- Has a condition ("given a fictional case," "in the skills lab") and often a
  standard ("in fewer than 5 steps," "per the rubric in this packet")

Then have the AI *pressure-test* it:

```text
Here is my objective: "Students will be able to prioritize the first three
actions for a workstation interruption during a skills check-off." Is this
observable? Which Bloom's level is it? Suggest a rewording if it is not
measurable, and list three activities that would fit it. Fictional teaching
material only; mark facts [VERIFY].
```

Level your objectives across a unit too: a good block mixes lower-level
(Objective 1: list the steps) and higher-level (Objective 2: prioritize among
competing tasks) verbs. Ask the AI to tag each of your objectives with its
Bloom's level; most do this reliably.

## Step 2: Generate the plan against your template

Open `templates/lesson-plan-template.md`, copy it, and prompt:

```text
Role: nurse educator drafting teaching materials.
Task: Fill in the attached lesson-plan template for a 50-minute class session
on professional communication in a simulated handoff.
Audience: second-year associate-degree nursing students; they have seen one
simulation day.
Format: keep my template's exact section order; fill every [bracket].
Constraints: Education only. No drug names, doses, or clinical-decision
guidance. All details fictional and generic; no patient data of any kind.
Mark every factual statement [VERIFY]. Bias toward low-prep, low-cost
activities using only paper, whiteboard, and chairs.
```

You'll get a draft in under a minute that's maybe 70% right. Your job: fix the
segments that don't fit your room, replace generic activities with your
favorites, and clear every `[VERIFY]`.

## Step 3: Fix the four classic AI lesson-plan defects

1. **Time collapse.** AI happily assigns 4 minutes to an activity needing 15.
   Redo the timing map yourself against the real clock.
2. **Activity inflation.** Proposes "think-pair-share plus gallery walk plus
   Kahoot" for a 50-minute room. Keep *one* active-learning segment and make
   it good.
3. **Objective drift.** Activities that don't map to any objective. For each
   segment, ask: which objective does this serve? If the answer is silence,
   cut it.
4. **Comma-spice inspiration.** Overwritten hooks ("Imagine a world where…").
   Strip to one clean question or scenario line.

## Step 4: Build the assessment last

One exit-brief-check per objective beats one big quiz. Prompt pattern:

```text
For each objective below, write ONE exit-ticket item: either a 2-sentence
constructed response or a 3-option multiple choice with plausible distractors.
Audience: [yours]. Fictional only, no clinical decision guidance, tag factual
claims [VERIFY].
Objectives:
1. …
2. …
```

Check the distractors — AI distractors are either absurd or barely different.
Good distractors are *plausible misconceptions your students actually hold.*
Edit until you recognize your students in them.

## Step 5: Accessibility pass (early, not at the end)

Now — not the night before — run the Chapter 9 checklist:

- Objective written in plain language? Read it aloud; if you stumble, rewrite.
- Any image-only instructions? Add text equivalents.
- Timed activity with no flexibility? Add a no-timing alternative.
- Print copy legible in grayscale? Re-run `tools/check_no_patient_data.py`
  and your own eyeballs.

## Worked micro-example (fictional)

Objective: *Given a fictional scenario card, the learner will teach back three
priority handoff elements in under two minutes.*

- **Hook (5 min):** "What gets lost when a verbal handoff is rushed?" Chart on
  board, no answers corrected yet.
- **Mini-lecture (10 min):** Three talking points — what a handoff carries
  [VERIFY], what breaks first under time pressure (human factors, fictional
  composite) [VERIFY], and the teach-back move.
- **Activity (25 min):** Pair role-play with two fictional scenario cards
  (Scenario A: new head of a school soccer club needing paperwork handoff;
  Scenario B: fictional clinic reception desk shift change — deliberately
  *everyday* transfer practices, no clinical decisions).
- **Debrief (5 min):** Two prompts: what did your partner do that helped? What
  felt rushed?
- **Exit ticket (5 min):** Teach-back of the three priority elements.

Deliberately **non-clinical props** keep the discussion on communication
skill, not on clinical urgency — safer, and it generalizes.

## Checklist before you teach it

- [ ] Objectives observable and leveled
- [ ] Every segment serves an objective
- [ ] Timing map survives a real clock
- [ ] Facts marked [VERIFY] are actually verified
- [ ] No patient data anywhere (run the checker)
- [ ] Accessibility pass done
- [ ] You would be happy if a colleague observed this plan exactly as written

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
