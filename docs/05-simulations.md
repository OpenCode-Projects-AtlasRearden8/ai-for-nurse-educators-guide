# Chapter 5 — Simulation Scenarios with AI

Simulation paperwork is the soul-crushing part of sim education: objectives,
scenario script, props list, facilitator notes, debrief questions. AI drafts
all of it in one pass — *if* you keep it fictional, education-only, and
unlocked enough for learners to really perform. This chapter gives you the
shape and the prompts.

## What a good scenario document contains (and what AI drafts well)

| Section | Contents | AI draft quality |
| --- | --- | --- |
| Cover line | Title, fiction disclaimer, intended audience | Very good |
| Learning objectives | 2–4, observable, sim-suited | Good — you must level them |
| Setup | Room, props, roles, timing blocks | Very good for checklists |
| Scenario flow | Brief, action, "escalation" beats | Good for structure |
| Roles & role cards | What each role knows, says, does | Excellent — very gen-AI friendly |
| Facilitator notes | Watch-fors, intervention triggers | Good; needs your pedagogy |
| Debrief frame | Questions, not answers | Good |
| Reset checklist | What to reset between runs | Very good |

## Step 1: Pick (or write) the learning objectives for sim

Sim scenarios shine at objectives like:

- **Demonstrate** a skill or behavior under time pressure
- **Prioritize** among competing demands
- **Communicate** a handoff, clarification, or escalation
- **Recognize** a pattern signal (e.g., "when the room is dropping cues, stop
  and count")
- **Participate constructively** in debrief (a real, teachable skill)

Prompt the AI to pressure-test your objectives the same way you did for lesson
plans (Chapter 3): observable? Right level? Would a sim actually let a learner
demonstrate it?

## Step 2: Generate the scenario with a closed cast

Build a cast list the same way as Chapter 4, then:

```text
Role: Simulation scenario writer for a nurse-educator training program.

Task: Draft a scenario document for a 12-minute simulation about
[communication under interruption] using ONLY the cast and setting below.

CAST (all fictional):
- Sim-1: "Drill Room Lead" (a role label, not a person)
- Sim-2: "Trainee Volunteer"
- Sim-3: "Background Voice" (offstage, delivers the interruption line)
- Setting: a fictional community-education center simulation lab; props are
  a clipboard, a paper checklist, two chairs, a mobile phone prop.

Format (keep exactly):
1. Title + "Fictional simulation — all roles and props are invented."
2. Learning objectives (2–4, observable).
3. Setup (what is in the room at start, who is where).
4. Phase 1 — Baseline (2 min): what happens before the interruption.
5. Phase 2 — Interruption event (4 min): what Sim-3 does, what could go wrong.
6. Phase 3 — Recovery (4 min): what the Trainee does, right or not.
7. Phase 4 — Reset (2 min).
8. Role cards: one short card per role — each card includes only what THAT
   role knows and needs to say.
9. Facilitator notes: three "watch-fors" and one trigger to pause.
10. Debrief questions (5, escalating: what happened → why → transfer).

Constraints: Education only. No medication decisions, no clinical care, no
patient data of any kind. No real names, no real institutions, no real
phone numbers (use the literal string "555-SIM" or "setup desk, extension 0").
All facts tagged [VERIFY].
```

## Step 3: The four things you will need to fix

1. **Over-scripted dialogue.** AI writes full sentences for learners to say.
   Sim is about learners *finding words*. Replace scripted lines with role
   cards describing **goals and constraints** ("You believe the checklist was
   skipped for one item; get the Trainee to confirm without accusing").
2. **Under-specified failure.** Scenarios in which nothing can go wrong are
   just theater. For each phase ask: what are the three ways a learner could
   respond — good, average, struggling — and does the role card support all
   three?
3. **Debrief with answers hiding inside.** If a debrief question presupposes
   the right answer, it's a lecture. Rewrite as a genuine open question.
4. **Prop realism gaps.** AI doesn't know your sim lab budget. Read the props
   list and ask: "Could I stage this with what's actually in that drawer?"

## Step 4: The role cards — the most valuable 10 minutes you'll spend

AI's best trick in sims is role cards: one card per role, private knowledge
included, no character in the card knows the whole plan. Prompt:

```text
From the scenario above, extract a role card for Sim-2 (Trainee Volunteer) only:
- What they know at the start
- What they must do
- What they must NOT do
- Lines they may use if stuck (maximum 3, optional, replaceable)
- One private note (something they believe that isn't stated aloud)
Keep card under 120 words, plain language, education-only.
```

Then cut. The goal: a card a nervous learner can scan in 15 seconds.

## Step 5: Facilitator notes and debrief frame

The facilitator notes you write yourself are:

- **Watch-fors** — three behaviors that tell you the scenario is working
  or stalling (e.g., "Trainee reads the checklist aloud but doesn't act on
  it")
- **Intervention trigger** — one condition where you'd pause (e.g., "if the
  Trainee physically leaves the room, or stalls more than 90 seconds without
  a question")

Debrief frame — escalate from *what* to *so what* to *now what*:

1. What happened, in your words?
2. Where did the message get fuzzy?
3. Why did the fuzzy moment survive two people?
4. What's the smallest change that would have helped?
5. What does this look like in your real work next week?

Add the fiction reminder again in the debrief slide — learners sometimes treat
sim as real, with real anxiety. Say it in exactly this order:

> "This was fictional. The *frustration* was real, and that's what makes it
> safe — here, missing a step is the point, not a failure."

That single reframe turns defensive silence into genuine discussion, reliably.

## Accessibility in sims (quick pass)

- Timing flexibility — offer a no-timer variant for learners who panic on
  clocks (Chapter 9).
- Reading load — role cards under 120 words; offer to read them aloud.
- Sensory load — one prop person at a time; no strobing lights or siren chaos.
- Physical access — never require a learner's body type, accent, speech rate,
  or any identity characteristic to *be* the scenario's failure. Failure
  belongs to the *task*, not the person.

## Quality gate before run day

- [ ] Fiction disclaimer on the title line *and* in the debrief slide
- [ ] Closed cast only; no names invented beyond the cast list
- [ ] Objectives demonstrable in this room, in this time
- [ ] Role cards ≤ 120 words with private notes
- [ ] Facilitator notes contain triggers to pause, not just to prod
- [ ] Debrief questions are genuinely open (no answers hidden inside)
- [ ] Reset checklist: what is reset *literally* between runs
- [ ] No patient data, no clinical guidance — re-run the checker and re-read

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
