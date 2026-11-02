# Chapter 7 — Citation and Hallucination Checks

AI invents citations the way a confident stranger gives directions: smoothly,
plausibly, and wrong. This chapter gives you a repeatable process for catching
fabricated references, invented numbers, and "realistic" guideline names
before they end up in front of students.

## Why AI hallucinates (the 30-second explanation)

Language models generate *plausible text*, not *verified text*. When asked for
a citation, it assembles a pattern that looks like a citation — real-sounding
author, real-sounding journal, real-looking year — without looking anything
up. The output can be 90% pattern and 10% reality. Citations, statistics, and
guideline names are exactly the content types where pattern beats reality.

## The three hallucination types to hunt

1. **Fabricated citation.** Author + journal + year all plausible; article
   doesn't exist. Sometimes it's a mash-up of two real papers.
2. **Real source, wrong content.** A real guideline exists — cited for a claim
   it doesn't make, or from the wrong year/edition.
3. **Plausible number.** A specific percentage or incidence figure with no
   verifiable origin. Numbers fabricated by AI almost never trace to a real
   source, and *"40% of students report…"* is the classic case.

## The prevention prompts (use before generation)

Add to any prompt that could touch facts:

```text
Verify before stating: if you are not certain a fact, guideline name, or
citation is real and current, either omit it or mark it [VERIFY]. Do NOT
generate citations from memory. If I need references, list search terms I
can use to find them myself instead of inventing sources.
```

That last line is the trick: **ask for search terms, not sources.** AI is
honest (and useful) at generating search strategy; it is unreliable at
generating bibliography.

## The verification pass (use after generation)

Five checks, in order, 30–60 seconds each:

1. **Existence check.** Paste the title into a real search engine, a library
   database, or a citation database. If you can't find the exact article in
   2 minutes, treat it as fabricated. (Tip: search the *title in quotes* plus
   the first author's surname.)
2. **Content check.** Open the real source. Does it actually support the
   sentence in your draft? Wrong-content hallucination is sneakier than
   fabrication.
3. **Freshness check.** For any guideline, standard, or statistic, check the
   publication year against today. Guidelines change; a 2012 edition handed
   to students is a teaching error.
4. **Attribution check.** Does the AI attribute the claim to the source's
   *actual author or organization*? A real article cited to a made-up
   organization is still a hallucination.
5. **Number check.** Trace every statistic to a named, current, reputable
   source — or delete the number. A principle stated in plain words is more
   teachable than a suspect percentage.

## Worked example: catching a fabricated citation

Suppose an AI draft includes this line:

> "Studies show that 68% of learners prefer visual case formats (Morales &
> Chen, 2019, *Journal of Applied Health Pedagogy*)."

Verification walkthrough:

- Existence: search the exact title/author pair → not found; the journal
  name sounds plausible but doesn't appear in a library catalog. **Fabricated.**
- Even if *"Journal of Applied Health Pedagogy"* existed, the number 68% is
  untraceable. **Delete.**
- Rescue the sentence by restating it as a principle not a stat:

> "Many learners report preferring visual case formats; consider offering a
> visual version alongside the text version."

Same pedagogical utility, zero fabrication risk.

## Rendering uncertainty honestly in your teaching materials

When you can't verify something but it's pedagogically useful:

- **Generalize:** "commonly reported," "widely taught," "varies by setting."
- **Attribute to yourself as the educator:** "In my experience in the
  simulation lab…"
- **Name the uncertainty for learners:** "Numbers vary by source and year;
  your clinical agency's policy is the source of truth for practice."

Students respect uncertainty stated plainly. They lose respect fast for
authority that gets the details wrong.

## Citing AI use itself (transparency default)

 Whenever an AI tool contributed to material students will see — even just as
a first-drafter — a short disclosure line protects everyone:

> "Drafted with the assistance of an AI writing tool; reviewed and edited by
> the instructor. Fictional teaching material — not clinical guidance."

For student-facing AI *assignments*, mirror the standard you set: require
students to disclose AI use the same way. One sentence of transparency prevents
a semester of ambiguity.

## A note about this manual's own citations

You'll notice this manual cites almost nothing numerically. That's deliberate.
Where a claim depends on a specific number, guideline name, or study, we've
_stated it as a principle_ instead — because a manual that round-trips through
AI generation itself must model the restraint it teaches.

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
