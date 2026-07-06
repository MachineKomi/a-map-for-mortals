# A Map for Mortals — Requirements

**Document:** Product Requirements · **Version:** 0.3 · **Status:** production
*(v0.3 adds §8: truth-verification and autonomous-process requirements. v0.2 content unchanged.)*
**Supersedes:** the requirements implied across `the-map-of-a-life-BOOTSTRAP.md` (the design spec in §6 of that file is superseded by `A-Map-for-Mortals-SPEC.md`).
**Reads alongside:** `wisdom-project-architecture.md` (deep architecture, ontology, methodology — still current) and `founding-principles.md` (**canonical; truth above all else is fixed**).

> **What changed in v0.2.** Two pieces of direction are now captured as first-class requirements:
> 1. **Visual variety — form follows content.** The book must *not* lean on one repeated diagram template. It draws on a wide library of diagram forms, each chosen and configured to suit the specific lesson, life-domain, life-stage, and kind of insight. (See R-V1…R-V6 and the form library in the spec.)
> 2. **A life-phase spine.** The book is structured by the stages of a life, in order — from the earliest stage at which a child can understand it read aloud, through to the final stage of life. (See R-S1…R-S5 and the life-phase architecture in the spec.)

---

## 0 · Title & identity

- **Title:** *A Map for Mortals* (locked).
- **Subtitle:** *or, how to be a human — the forks, the trade-offs, and the gathered wisdom of those who walked ahead.* (locked)
- The working title *The Map of a Life* used in older docs is retired in favour of the above. The *graph* may still be referred to internally as "the map of a life."

---

## 1 · The fixed star and the spirit (non-negotiable)

The canonical wording lives in `founding-principles.md`. In brief, every requirement below is subordinate to these:

- **R-0.1 — Truth above all else.** Supreme and permanent. Truth-seeking before ideology, aesthetics, comfort, virtue-signalling, sentiment, or marketability. Never start from a conclusion and reach back for wisdom to support it. *Let the data drive.*
- **R-0.2 — Honest about uncertainty, still useful.** Diagrams show *tendencies and risks, never destinies*. Generalise to be useful; never let a generalisation pretend to be a law.
- **R-0.3 — Recurrence ≠ proof; convergence = robustness, not truth.** Independent cross-tradition agreement is a signal to be tested, not a verdict.
- **R-0.4 — Keep the three truths distinct:** what *is* (empirical), what we *ought* to do (normative), what *tends to work* (prudential). Never dress one as another.
- **R-0.5 — Respect sources; flag dubious attributions.** Add nothing to a wise person's mouth. Unverified quotes start at `dubious`.
- **R-0.6 — Refuse to flatten a life.** No diagram holds a whole human being; the book keeps saying so.
- **R-0.7 — Tone.** Beautiful, serious, practical, honest, emotionally resonant; dry, humane humour welcome (Principle 16). **Never** preachy, moralising, self-help-gimmicky, or falsely certain.

---

## 2 · Content requirements

- **R-C1.** The atomic unit is the **node**, not the quote: a claim, the independent voices that reached it, the place it bends, and an honest label for how far it can be trusted.
- **R-C2.** **Dilemmas (forks) are first-class.** Where the wise disagree, the book shows the fork and the conditions under which each side applies — it does not resolve tensions into platitudes.
- **R-C3.** Every claim carries its **conditionality** visibly (universal-ish / conditional / contested) and, where relevant, the danger it guards against and the danger of taking it too far.
- **R-C4.** **Sources are credited** throughout; attribution confidence is tracked; the methodology is summarised in front matter and given in full in an appendix.
- **R-C5.** **Minority and dissenting wisdom is preserved**, not pruned to fit a tidy consensus.
- **R-C6.** The corpus is **broad and deliberately widened** beyond the literate/powerful/recent/Western default, and the remaining gap is named rather than hidden.

---

## 3 · Structure requirements — the life-phase spine *(new in v0.2)*

- **R-S1 — Life-phase ordering.** The body of the book is organised as a **journey through the stages of a life, in chronological order**, beginning at the **earliest stage at which a child can understand it being read aloud** and continuing **through to the final stage of life**. Stages are the primary spine; life-domains (love, work, money…) are threaded *through* the stages rather than forming the top-level structure.
- **R-S2 — Each stage is a chapter** with: an orienting opener (the terrain of that stage and its central felt question), a curated handful of the forks that *define* that stage, and a quiet close. The indicative stage scheme and per-stage register are specified in the spec.
- **R-S3 — Register adapts to the stage.** Reading level, word count, vocabulary, visual density, and colour energy **scale with the life-stage**: spare and warm and read-aloud at the start; fuller and denser through the building and reckoning years; spare again, and weightier, at the close. The earliest pages must genuinely work read aloud to a young child; the latest must hold an adult facing the end.
- **R-S4 — The same fork at different altitudes.** Certain forks recur across stages (e.g. *truth, courage, enough, letting go*). When a fork recurs, it is **rendered differently each time** to show how the same choice changes shape across a life. This is a feature, not redundancy.
- **R-S5 — An operating-system front section** precedes the journey: the north star (truth above all), how to read the maps (a legend for the visual language), and the engine of a life (choice → consequence → interpretation → character). The journey assumes these.

---

## 4 · Visual & diagram requirements — variety, form follows content *(new in v0.2)*

- **R-V1 — No monotony.** The book **must not** rely on one repeated diagram template. Visual sameness across many pages is a defect, even when each individual diagram is good. (This directly retires the prototype's reliance on a single decision-tree shape.)
- **R-V2 — A wide form library.** The book draws on a **broad, named library of diagram forms** — decision trees, branching-outcome maps, trade-off spectra, 2×2 matrices, balance scales, cycles, cascades, ladders, threshold curves, convergence maps, node cards, comparison columns, constellations, concentric rings, overlaps, journey maps, attention-flow diagrams, and reframes, among others. The full catalogue lives in the spec and is expected to grow.
- **R-V3 — Form follows content.** The form for any node is **selected to fit the content**, not defaulted. A node's attributes (its type, claim type, polarity, conditionality, whether it concerns a process, a tension, a consequence over time, a convergence, a scope) drive which form is appropriate. The spec defines the selection logic.
- **R-V4 — Forms are configurable.** Each form is a **parameterised template, not a fixed picture** — configurable around the lesson, the life-domain, the life-stage, and the specific insight, so the same form can carry different content at different weights and reading levels. "Templated" in the pejorative sense (visibly the same mould reused without thought) remains a fail; a rich, well-chosen, well-configured set of templates is the goal.
- **R-V5 — Diagrams stay honest.** Every form must be able to show **conditionality and tension** and must never imply a destiny. A form that can only express certainty is unfit for this book.
- **R-V6 — Premium, intentional execution.** Each diagram reads as deliberately composed for its page: no stranded slivers, no orphaned captions, no label collisions, no top-heavy/under-filled pages. The design system (palette, type, semantic colour) in the spec is mandatory and applied consistently.

---

## 5 · Design & production requirements

- **R-D1 — Editorial bar.** Premium, literary, intentional design throughout. "Looks templated" or "looks under-finished" is a fail.
- **R-D2 — Single source of truth.** The book is a **curated traversal of one versioned wisdom graph**. The website and game are sibling projections of the same graph; the book must not diverge into a separate content store.
- **R-D3 — Print-on-demand first.** The primary deliverable is a print-ready book (Amazon KDP), trim **178 mm × 254 mm**, produced via the HTML/CSS → PDF pipeline in the spec.
- **R-D4 — Honest framing while in prototype.** Until the corpus and analysis are real, the book states plainly that diagrams are composed by hand to show *form*, and labels its version and thin-slice status at the front and in the colophon.
- **R-D5 — Downstream formats (roadmap, not in current scope).** The graph is built so it can also yield: a **free interactive website**, an **app**, and a **text-first "choose your own adventure" game** (heavy on text, light on visuals) with **text-to-speech**, so the work is usable by people who cannot or prefer not to read on a page. Requirements here are recorded so nothing in the book or graph forecloses them; building them is future work.

---

## 6 · Definition of done (for a finished book; the prototype meets a subset)

A chapter/stage is "done" when:
- it opens with an orienting spread and a clear central question for that life-stage;
- its forks are rendered in **at least three distinct diagram forms**, each chosen to fit its content (R-V1–V4);
- every diagram is honest about conditionality (R-V5) and every page is well-composed (R-V6);
- sources are credited and attribution confidence is shown where claims are attributed;
- the register matches the stage (R-S3);
- where a recurring fork appears, it is rendered freshly for this altitude (R-S4).

---

## 7 · Out of scope / non-goals (for the book)

- Not a quote wall; not a self-help programme; not a moral lecture.
- Not a claim to completeness or to final truth.
- The website, app, and game are **siblings**, not part of the book deliverable — but the graph and book must not block them (R-D5).

---

## 8 · Truth-verification & process requirements *(new in v0.3)*

- **R-T1 — The print gate.** No quotation appears verbatim in the book unless its wording is verified against a primary edition (`verified-primary`) **and** it is public-domain or licensed. Otherwise: honest paraphrase ("a saying attributed to…") or omission. Verification effort is budgeted by publish priority, so this stays finite.
- **R-T2 — Auditability.** Every unit, claim, and edge carries provenance, method, and confidence; any judgment is re-examinable after the fact.
- **R-P1 — Autonomous operation.** Claude Code runs the pipeline end-to-end; contestable calls route to an escalation queue; Jason reviews **publish packages** (finished deliverables + escalations + provenance summary + known limits), not intermediate steps.
- **R-P2 — Convergence, not perfection.** Numeric ship targets (METHODOLOGY §4/§8) are tunable defaults that force the build to land; depth serves the book, the book does not wait on infinite depth.
- **R-P3 — Harness-native tooling.** Prefer the simplest tool that preserves the epistemics in the execution environment; no gate may be blocked by an optional heavy dependency.

---

*The one fixed star, in the work and in this document: **truth above all else.***
