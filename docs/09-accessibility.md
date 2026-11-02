# Chapter 9 — Accessibility Notes

Accessible materials aren't a compliance chore — they're better for *every*
learner, and they cost minutes when built in early. AI tools make accessibility
easier: they can draft alt text, simplify language, and produce consistent
heading structure, if you ask. This chapter is the checklist.

## Why "just print it" isn't the bar

Materials you hand out will be read:

- by learners using screen readers or text-to-speech
- on a phone, in grayscale, with tired eyes
- by learners with ADHD, dyslexia, low vision, or processing
  differences
- at 9pm, in a hallway, after a shift

Each habit below serves all of those readers — and it makes your documents
clearer for you, too.

## Heading discipline (the single highest-value habit)

- Every document has exactly one top-level heading (the title).
- Section headings nest in order (H1 → H2 → H3), never skipping levels.
- Headings describe content ("What to bring to lab"), not decoration ("More!").

Screen readers navigate by heading structure. Broken heading order makes a
document un-navigable no matter how good the content is. AI drafts frequently
"decorate" heads — spot-check structure, not just wording.

**Prompt pattern:**

```text
Reformat this document with correct heading hierarchy: one H1, then H2s in
order, H3s only under their parent H2. No heading may be used for emphasis
instead of structure. Keep my words otherwise unchanged.
```

## Alt text that actually describes

Every image (even a screenshot, even a decorative sketch) gets alt text that
answers: *what would a reader miss without it?* AI drafts this well when you
give it context:

```text
Write alt text for this image, for a page about [your lesson]. Keep under
80 words. Describe function, not appearance. If the image is purely
decorative, say so and I'll mark it as such.
```

Complex diagrams need both alt text **and** a long description in body text.
Never make a diagram the *only* carrier of an instruction.

## Color: a tool, never a signal

- If "the red row" means something, the same meaning must survive in plain
  text (label, icon-with-text, or bold + text).
- Print test in grayscale before class. Most AI-proposed color schemes fail
  this in a way that matters.

AI designs with color constantly — it's pattern-beautiful. Strip color-only
meaning out at review time (PASS-QC step C).

## Plain language (with a worked AI prompt)

Aim for common words, short sentences, concrete examples, and front-loaded
meaning. AI simplification prompt:

```text
Simplify this text for a first-semester student reading after a shift, in
plain language. Keep my meaning exactly — do not add or remove any teaching
point. Keep technical terms, but define each one in the same sentence. No
exclamation points. Under [word count] words.
```

The "keep my meaning exactly" is the crucial line — without it, simplification
drifts into a different lesson.

## Timing and flexibility

- Never make a timed activity the *only* way to demonstrate an objective.
- Offer an alternative demonstration for any timed task.
- State time limits in advance, not as a surprise.

This is an ADHD-friendly practice and also a best practice generally: people
perform better when the clock's role is known.

## Structure for focus (ADHD-friendly, everyone-friendly)

- One action per list item; state the action first.
- Put the deadline/deliverable at the top of any handout, not the bottom.
- Use white space by default; AI will fill it — tell it not to.
- Chunk work into steps that each have a visible "done" state.

## Printability

- Test the draft in **grayscale print** before finalizing.
- Serif or humanist sans body font, 11–12pt minimum for print.
- Line length and margins: leave room for handwritten notes (most learners
  will use them).
- Avoid fancy boxes that eat toner or clip in duplex printing.

AI produces beautiful complex layouts readily; simple ones it must be told to
do. Prompt: *"One column, generous margins, no decorative elements, printable
in black and white."*

## Screen-reader spot checks (no special tools needed)

Read your web or exported-PDF documents with the keyboard only:

- Tab through; can you reach every link and control?
- Does the heading structure tell the story on its own?
- Are link labels descriptive ("Chapter 7: Citation checks" rather than
  "click here")?

Ten minutes with the Tab key catches most issues library accessibility
workshops spend hours teaching.

## The accessibility quick checklist (PASS-QC step C)

- [ ] One H1; heading levels nested correctly
- [ ] Alt text on every image; long text equivalents for complex figures
- [ ] No meaning carried by color alone
- [ ] Sentences short; jargon defined inline
- [ ] Time-flexible alternatives for any timed activity
- [ ] Grayscale print test passed
- [ ] Links have descriptive labels
- [ ] Deliverable stated at the top of every handout
- [ ] Fiction/education-only disclaimers present (and screen-readably placed —
      near the top, not buried at the end)

---

*Copyright (c) 2026 Asdale Dynamics, LLC. Education only, never clinical advice.*
