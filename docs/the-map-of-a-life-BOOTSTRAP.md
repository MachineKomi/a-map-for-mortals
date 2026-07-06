# The Map of a Life — Project Bootstrap & Prototype Brief

*A handoff document to resume this project in a fresh chat. Working title: **The Map of a Life** (not yet locked).*

---

## 0 · How to use this document

This is a self-contained brief that re-establishes the project, its spirit, where things stand, and — most importantly — the **complete spec and design system for the v0.0.1 prototype**, which is the immediate task.

**Already in this project's knowledge library (don't recreate — read for depth):**
- `wisdom-project-architecture.md` — the deep architecture & research-direction doc (vision, methodology, ontology, corpus of thinkers, computational methods, the one-graph-three-formats plan, title options, next steps).
- `founding-principles.md` — the enshrined north star and 15 principles. **This is canonical. Truth above all else is fixed and never changes.**
- `life-wisdom-decision-trees.md` — an earlier set of age-based Mermaid decision trees (an early sketch of the "wisdom as forks" idea).

**Not in the library (captured here, because earlier work on it never shipped):** the prototype's design system, page structure, diagram inventory, the HTML/CSS→PDF technical approach, and the lessons from prior build attempts. **Sections 6–8 below are the operative part.**

**Immediate next action:** plan and build the **v0.0.1 prototype book** — an honest, thin, but representative vertical slice — as a beautiful PDF. See §6 for the full spec and §7 for the suggested working method. Recommend confirming the principles wording and a one-screen build plan with me before generating, then building, rasterizing every page to QA, and iterating to a premium result.

---

## 1 · The project in one page (the vision)

A multi-format **"wisdom through choices"** project. The throughline: **wisdom is not a list of answers but a map of recurring forks** — the choices humans face again and again, the tensions with no clean resolution, and the consequences that *tend*, on balance and over time, to follow.

Three linked formats, all **projections of one underlying "wisdom graph" (single source of truth):**
1. **The illustrated book** — a beautiful print-on-demand book (Amazon KDP) of rendered diagrams: decision trees, flowcharts, node maps, trade-off maps, wisdom nodes. *(The prototype is the first slice of this.)*
2. **The website** — a free, navigable, living map of the whole graph (explore by theme, thinker, tradition, dilemma, consequence, life-stage).
3. **The game** — a simple text-based life-simulation: you live an ordinary human life (childhood → love → work → failure → ageing → death); each fork is a node from the graph; choices traverse edges and shape character, relationships, outcomes, and how the story ends. The ending draws *the map of the life you lived*.

**What makes it distinct** from the ocean of quote books: (a) it is **honest about contradiction and conditionality** (dilemmas are first-class; it shows where the wise disagree); (b) it is **evidence-informed without being pseudo-scientific** (independent cross-tradition convergence is treated as a *robustness signal*, never as proof); (c) it is **beautiful and experiential**.

*(Full detail in `wisdom-project-architecture.md`: methodology, ontology, the thinker corpus across Greco-Roman / Nietzsche's web / Eastern / Hebrew wisdom / literary authors, the data-science methods, and worked node examples.)*

---

## 2 · The non-negotiable spirit (intent & nuance — read carefully)

This matters more than any feature. The whole project must embody it.

- **Truth above all else.** Supreme and permanent. Truth-seeking before ideology, aesthetics, comfort, morality, virtue-signalling, sentiment, preference, marketability, and before what we wish were true. **Let the data drive. Never bias.** Never begin with a conclusion and reach back for wisdom to support it. If honest/disciplined/just/compassionate lives *do* tend to go better, *show it with evidence* — never assume it.
- **Honest about uncertainty, and still useful.** Few choices have certain consequences. Most wisdom is **conditional and probabilistic**, dependent on person, time, place, temperament, culture, class, luck, biology, trauma, opportunity, and history. We must **generalise to be useful — but never let a generalisation pretend to be a law.** Diagrams show tendencies and risks, *never destinies*. Useful without ever becoming dishonest.
- **Recurrence ≠ proof.** Convergence across independent traditions is evidence of *robustness*, not truth. Age and popularity show that an idea *resonated*, not that it is *correct*.
- **Three kinds of truth kept distinct:** what *is*, what we *ought* to do, what *tends to work*. Never dress one as another.
- **Respect sources; flag dubious attributions.** Misattribution is rampant; check quotes; add nothing to a wise person's mouth.
- **Refuse to flatten a life.** No diagram holds a whole human being; keep saying so.

**Tone DO-NOTs (hard rules):** not preachy, not moralising, not a self-help gimmick, no overclaiming, no fake scientific certainty. **Tone DO:** beautiful, serious, practical, honest, emotionally resonant — the first glimpse of a real book about how people choose, suffer, trade off, endure, love, lose, grow, deceive themselves, and try to live well.

*(Canonical wording lives in `founding-principles.md` — 15 principles, with Truth above all else as #1 and fixed. Everything else is revisable.)*

---

## 3 · Working style (how to collaborate with me on this)

- I work **spec-driven** with AI agents and value a clear plan before execution. For big tasks, **break it down** — propose a short plan, get a nod, then build. (We explicitly split this into: enshrine principles → plan prototype → build.)
- I care about **intellectual honesty over flattery** — push back, show trade-offs, don't just agree.
- I have a strong eye for **premium, editorial, intentional design**. "Looks templated" or "looks under-finished" is a fail.
- Be honest and up front about limitations (e.g. that v0.0.1 is a thin slice). Don't pretend completeness.

---

## 4 · Where we are

- ✅ **Vision & architecture** defined (`wisdom-project-architecture.md`).
- ✅ **Principles enshrined** (`founding-principles.md`) — *pending my final sign-off on wording; flag this at the start of the next chat.*
- ⏳ **v0.0.1 prototype**: fully designed and substantially prototyped, but **not yet finalised or delivered.** Earlier attempts to build the whole thing in one pass rendered a genuinely beautiful ~20-page PDF but hit specific page-composition bugs (see §6.6). Per my request we're now doing it **stepwise and carefully**.

---

## 5 · The immediate task — build the v0.0.1 prototype

A beautiful, **honest, thin-but-representative vertical slice** of the book, as a PDF (HTML/CSS → PDF). It should feel like the first glimpse of the finished work, while being explicitly and visibly an early prototype.

### 5.1 Purpose & honest framing
Its purpose is to **share the vision** with people I care about, help them understand what I'm building, and help me get excited. It must be **honest at the front**: a foreword stating this is **version 0.0.1 — an early conceptual vertical slice, not the finished corpus, not the completed analysis, and not a final claim about human wisdom.** Keep the slice **thin** (a handful of sources/diagrams), but make that thin slice **as representative of the full vision and final product as possible.**

### 5.2 Structure (sections)
1. Cover
2. Foreword: Version 0.0.1 (the honest framing)
3. The North Star: Truth Above All Else
4. The Principles of the Project
5. What This Book Is Trying to Do
6. A First Map of Human Choice
7. A few sample wisdom diagrams / node graphs
8. A few sample "wisdom nodes"
9. A sample decision tree about an ordinary life choice
10. A sample trade-off map
11. A sample cross-tradition convergence page
12. Appendix A: Methodology
13. Appendix B: Limits, Uncertainty, and What This Prototype Is Not

### 5.3 Required example diagrams (the visual heart)
- **"Truth Above All Else" principle map** — a radial map with TRUTH at the centre and the supporting principles around it.
- **The engine of a life** — `choice → consequence → interpretation → character → future choice` as a loop; highlight *interpretation* as "the hinge of freedom" (the one place freedom reliably lives).
- **A trade-off map** — spectra such as comfort↔growth, harmony↔honesty, peace↔ambition, belonging↔freedom; with the message that there is **no fixed correct point** — the skill is the leaning, and noticing when you've drifted too far.
- **A wisdom node** — e.g. *"Control what you can; consent, honestly, to what you cannot."* Show: the claim, independent voices across traditions (Epictetus / Bhagavad Gita / Shantideva / the Serenity Prayer), the tension ("where it bends" — the quietism risk), and an honest robustness label ("recurrent · cross-traditionally convergent · conditional at the margins").
- **A decision tree for an ordinary, difficult choice** — recommended: *"There's a hard truth I could speak — should I?"* It must be **honest and conditional**: truth-telling is unconditional in *value* but conditional in *delivery* (is it true? is it mine to say? will it help or only wound? right moment/manner?), resolving to: *"Truth above all is never truth without skill. We do not soften what is true — only choose when, how, and whether it is ours to say."* (This elegantly reconciles the decision tree with the north star.) Other viable choices: forgive/not, ambition vs security, endure hardship.
- **A cross-tradition convergence map** — several thinkers across great distance/time converging on one insight; caption it as **evidence of robustness, not proof** ("four traditions, little or no contact, two thousand years").

### 5.4 Methodology appendix (digestible, honest)
Cover, in plain terms: build a broad corpus (philosophical/literary/religious/ethical/practical) crediting sources → tag claims, metaphors, choices, virtues, warnings, conditions, consequences → identify recurring insights across eras/traditions → map contradictions and conditional advice → use semantic clustering, network analysis, frequency analysis, source diversity, and human review → **convergence = robustness, not proof; recurrence ≠ truth** → preserve minority/dissenting wisdom → keep the whole project revisable. ("Computation proposes; humans verify.")

### 5.5 Limits appendix
Honest: not the finished corpus; not the completed analysis (diagrams composed by hand to show *form*, not generated from a finished dataset); not a final claim; correlation ≠ causation; recurrence ≠ truth; a choice doesn't guarantee its outcome; the written record skews literate/powerful/recent/Western (we'll widen it and keep naming the gap); no diagram contains a whole life. End on what it *is*: an honest first glimpse.

---

## 6 · Prototype design system & build playbook (the reusable spec)

This is what was figured out and validated in prior build runs. **Reuse it.**

### 6.1 Visual direction
Primarily **light mode**; warm off-white background; **dark navy as the main ink**; **orange + pink accents**; a few restrained extra tints only where useful. Editorial / literary / philosophical; clean modern layout with human warmth; elegant, generous spacing. Writing must be **concise — "poetic clarity, not essay"** — tight enough to live inside diagrams.

### 6.2 Palette (exact hex — validated and on-brand)
| Token | Hex | Use |
|---|---|---|
| Paper (bg) | `#FBF7F0` | warm ivory page background |
| Panel | `#FFFDF9` | figure/card panels (slightly brighter) |
| Ink (navy) | `#16223B` | primary text + structure |
| Ink-2 | `#4A546B` | secondary text |
| Ink-3 | `#717A8C` | tertiary / fine captions |
| Orange | `#DD6A3B` | **caution / decisions / eyebrows / the harder road** |
| Orange tint | `#F6E2D4` | orange fills |
| Pink (rose) | `#CF6A86` | **insight / warmth / the wiser path** |
| Pink tint | `#F7DDE6` | pink fills |
| Navy tint | `#E6EAF1` | neutral node fills / robustness pill |
| Line | `#E3D6C2` | warm hairlines / borders |
| Warm | `#EFB58A` | sparing warm accent on dark panels |

**Semantic discipline:** navy = structure/ink; orange = caution/decision points; pink = insight/warmth/wiser path. **No green** (stay on the stated palette — it reads cohesive and premium).

### 6.3 Typography (both fonts are present in the environment)
- **Lora** (variable serif, incl. italic) — body + headings + display. Literary, warm. At `/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf`.
- **Poppins** (geometric sans, Light/Regular/Medium/Bold + italics) — eyebrows, diagram labels, captions, page furniture. Clean, modern. Same fonts dir.
- This serif-display + geometric-sans pairing is the premium editorial look. (DejaVu, Liberation, Noto Serif CJK also available; `apt-get` works via the Ubuntu archives if more are ever needed — but these two are sufficient.)

### 6.4 Page setup
- Trim **178mm × 254mm** (7"×10") — a designed book feel.
- Generous margins (~20–22mm); discreet running header (e.g. "THE MAP OF A LIFE · v 0.0.1") and centred page numbers in Poppins; **full-bleed cover** (named page, no margins).
- A delicate **forking-path motif** (a stem splitting into two branches with small accent-coloured nodes, inside a faint "north-star" ring) works beautifully on the cover and colophon.

### 6.5 Technical approach (what works here)
- **HTML/CSS → PDF via WeasyPrint** (v69 is installed). 
- **WeasyPrint runs no JavaScript → Mermaid will NOT render.** Build **every diagram as hand-authored inline SVG.** This also gives far better design control.
- A **Python generator** is the clean way to do it: small SVG helper functions (rounded-rect node, pill, arrow-with-triangle-head, diamond marker, "?" badge, multi-line centred text) + one function per diagram + the prose + the CSS, assembled into `book.html`, then `WeasyPrint('book.html').write_pdf('book.pdf')`.
- **QA loop is essential for "visually stunning":** rasterize every page with **`pdftoppm -png -r 130 book.pdf pg`** and *view each PNG*, then fix and re-render. Do not ship without eyeballing every page.
- Put SVG text in Poppins for labels; use proper unicode (—, ", ', ·, →) via Python `\u…` escapes (they decode correctly into the HTML).

### 6.6 ⚠️ Lessons learned — bugs to avoid (from prior renders)
The earlier one-pass build produced a genuinely beautiful 20-page PDF, but rasterizing revealed these defects. **Pre-empt all of them:**

1. **Don't stack two display elements.** A giant decorative "0.0.1" numeral collided with the foreword's drop cap. Pick one flourish per page; drop redundant decorative numerals (the page title already says "Version 0.0.1").
2. **Size cards/figures to fit one page — leave no stranded sliver.** The wisdom-node card was a hair too tall and pushed its robustness label + caption onto an otherwise-empty next page. Tighten internal spacing; use `break-inside: avoid`; verify it + its caption fit together.
3. **Watch SVG label collisions.** Decision-tree branch labels ("if unsure", etc.) were painted over by the caution boxes (the gap was too small and boxes were drawn last). Widen gaps, shorten labels, and/or draw labels after the boxes. Confirm by rasterizing and zooming.
4. **`break-inside: avoid` on every callout/box.** The methodology "one discipline" navy box split across a page break, leaving a near-empty page. Keep boxes intact and size content to fit.
5. **Biggest one — don't split a short prose intro from its tall figure across two half-empty pages.** Pages that paired a few lines of prose with a tall SVG looked top-heavy and under-filled. **Fix:** keep prose intros tight (≈2 short paragraphs) and **size/compact the figure so prose + figure share ONE well-filled page.** The trade-off-map page and the wisdom-node page did exactly this and were the best-composed pages — use them as the model. Reserve a full dedicated page only for the genuinely tall centrepiece (the decision tree), and even then keep it well-filled and balanced.

**General bar:** every page well-composed (no top-heavy/empty pages, no split boxes, no stranded captions); diagrams honest (conditionality/tensions visible, never destinies); premium editorial feel throughout. The approach is proven — it just needs disciplined per-page QA.

---

## 7 · Suggested working method for the new chat
1. **Re-ground** from this doc + the three library artefacts. Note that the prototype design system is in §6 here (not in the library).
2. **Confirm** the principles wording is approved (ask me), and propose a **one-screen build plan** (section list, diagram inventory, page plan) for a quick nod.
3. **Build** the generator → render → **rasterize and inspect every page** → fix the known pitfalls (§6.6) → iterate to premium.
4. **Deliver** `book.pdf` (primary) + `book.html` (editable source) to outputs and present. Keep the foreword/appendices honest about the v0.0.1, thin-slice nature.

---

## 8 · Open questions / decisions pending
- **Final title.** Recommendation: **The Map of a Life** + a descriptive subtitle (poetic title + searchable subtitle is the right pattern for KDP), e.g. *"The choices, tensions, and gathered wisdom of being human — drawn as decision trees."* Confirm or choose an alternative. *(Other options are in `wisdom-project-architecture.md`; check trademark before committing.)*
- **Any edits to the principles** wording before they're rendered into the prototype.
- **Slice scope** — keep it thin: roughly the 13 sections above with ~6 hero diagrams and 1 fully-worked wisdom node is enough to be representative without overclaiming completeness.

---

*Prepared as a bootstrap so a fresh chat (with the three artefacts in its project knowledge) can resume immediately and build the v0.0.1 prototype. The one fixed star, in the work and in this document: **truth above all else.***
