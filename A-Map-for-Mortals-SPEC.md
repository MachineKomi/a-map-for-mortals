# A Map for Mortals — Design & Build Spec

**Document:** Design & Build Specification · **Version:** 0.3 · **Status:** production
*(v0.3 adds §12: the production generator and page-spec bridge. v0.2 content unchanged.)*
**Supersedes:** §6 of `the-map-of-a-life-BOOTSTRAP.md` (design system & build playbook).
**Implements:** `A-Map-for-Mortals-REQUIREMENTS.md`. **Background:** `wisdom-project-architecture.md`. **Canonical values:** `founding-principles.md`.

> **New in v0.2:** §6 the **diagram form library** (a wide pool of forms, replacing reliance on a single decision-tree template), §7 the **form-selection & configuration logic**, §8 the **life-phase architecture** (the book's new spine), and §9 the **"same fork at different altitudes"** device. The visual system (§1–5) and build pipeline (§10) carry forward from the validated prototype.

---

## 1 · Visual direction (validated — carry forward)

Primarily **light mode**; warm off-white background; **dark navy as the main ink**; **orange + pink accents**; restrained extra tints only where useful. Editorial / literary / philosophical; clean modern layout with human warmth; elegant, generous spacing. Prose is **concise — "poetic clarity, not essay"** — tight enough to live inside diagrams.

The distinctiveness of the look (so it never reads as generic AI cream-and-terracotta) comes from: **pink as a disciplined second accent**, **strict semantic colour**, **bespoke hand-authored diagrams**, and the **forking-path-in-a-north-star** signature motif.

## 2 · Palette (exact hex — validated, on-brand)

| Token | Hex | Use |
|---|---|---|
| Paper (bg) | `#FBF7F0` | warm ivory page background |
| Panel | `#FFFDF9` | figure/card panels (slightly brighter) |
| Ink (navy) | `#16223B` | primary text + structure |
| Ink-2 | `#4A546B` | secondary text |
| Ink-3 | `#717A8C` | tertiary / fine captions |
| Orange | `#DD6A3B` | **caution / decision points / eyebrows / the harder road** |
| Orange tint | `#F6E2D4` | orange fills |
| Pink (rose) | `#CF6A86` | **insight / warmth / the wiser path** |
| Pink tint | `#F7DDE6` | pink fills |
| Navy tint | `#E6EAF1` | neutral node fills / robustness pill |
| Line | `#E3D6C2` | warm hairlines / borders |
| Warm | `#EFB58A` | sparing warm accent on dark panels |

**Semantic discipline (amended 2026-07-07 — R-V5 outranks palette semantics; see ops/DECISIONS.md):** navy = structure/ink; orange and pink are **evaluative colours applied ONLY where the project has adjudicated an evidence-backed asymmetry** (orange = the adjudicated harder/cautioned side, pink = the adjudicated wiser/insight side). **Unresolved poles and genuine open tensions receive equal-status neutral colour** — colour must never answer a question the evidence has not. **No green** (one dark `#2e7d56` is permitted only for a positive "yes" branch chip), **no purple**. Colour *energy* may rise in early-life chapters and fall toward the close (see §8); the grammar above is fixed.

## 3 · Typography (present in the environment)

- **Lora** (variable serif, incl. italic) — body, headings, display. `/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf` (+ `Lora-Italic-Variable.ttf`).
- **Poppins** (geometric sans: Light/Regular/Medium/Bold + italics) — eyebrows, diagram labels, captions, page furniture. Same directory.
- Serif-display + geometric-sans is the premium editorial pairing. Put SVG diagram labels in Poppins. Use proper unicode (— " ' · → ↔) via Python escapes.

## 4 · Page setup (validated)

- Trim **178 mm × 254 mm** (7″×10″) → `504.567 × 720 pt`.
- Margins ~19–22 mm; discreet running header (`A MAP FOR MORTALS · v 0.0.x`) + centred page numbers in Poppins; **full-bleed cover** (named `@page`, no margins/header); a `bare` named page (no header/number) for the colophon.
- The **forking-path motif** (a stem splitting into two branches with small accent nodes, inside a faint north-star ring) anchors cover and colophon.

## 5 · Technical approach (what works here)

- **HTML/CSS → PDF via WeasyPrint** (v69 installed via `pip install weasyprint --break-system-packages`).
- **WeasyPrint runs no JavaScript → Mermaid will NOT render.** Build **every diagram as hand-authored inline SVG (or HTML/CSS for card-like forms).** This also gives far better design control.
- A **Python generator** assembles SVG/HTML helpers → one function per diagram form → prose → CSS → `book.html`, then `WeasyPrint(...).write_pdf(...)`.
- **QA loop is mandatory:** `pdftoppm -png -r 96..130 book.pdf pg` and **view every page**, then fix and re-render. Never ship without eyeballing every page.

---

## 6 · The diagram form library *(new — the visual heart)*

The book draws on a **wide pool of diagram forms**. Each is a **parameterised template**, not a fixed picture: it accepts content (claim, voices, branches, poles, stages, conditions, lesson) and a **register** (reading level, density, colour energy) so the same form serves a six-year-old's fork and an adult's. **Form follows content** (R-V3): the form is chosen to fit the node, never defaulted.

The catalogue below is the starting library and is expected to grow. Forms are grouped into families.

### A · Choice forms — *how to decide*
| Form | Best for | Configured by |
|---|---|---|
| **Decision tree (interrogation)** | a single hard choice resolved by asking yourself the right questions in order | gates & their questions, off-ramps, action, lesson |
| **Branching-outcome map (two roads)** | showing where each path *tends* to lead over time, rather than how to pick | branches, depth, time horizon, tendency labels |
| **Flowchart with feedback** | behaviours that cycle (the apology loop, the procrastination spiral) | nodes, decision diamonds, loop-backs, exit condition |

### B · Tension forms — *good against good*
| Form | Best for | Configured by |
|---|---|---|
| **Trade-off spectrum** | a virtue-vs-virtue tension where the answer is a *position*, not a pole | the two poles, cost-notes, where each curdles |
| **2×2 matrix (quadrants)** | two independent dimensions crossing into four stances (candour × care) | axis labels, four cell labels, the "aim here" cell |
| **Balance scale** | weighing competing duties or costs vs benefits; the fulcrum is the condition | the two pans, weights, the deciding fulcrum |
| **Pendulum / over-correction** | how a virtue swings to a vice, and the corrective over-swings too | the swing poles, the centre of gravity |

### C · Process & time forms
| Form | Best for | Configured by |
|---|---|---|
| **Cycle / loop (the engine)** | self-reinforcing processes (choice→consequence→interpretation→character) | the stages, the highlighted "hinge" |
| **Cascade / consequence timeline** | delayed payoffs; the long game; near vs far consequences | events along time, near/far emphasis |
| **Ladder / staircase** | progressions of mastery or maturity; escalation; stages within a phase | rungs & labels, the "you are here" |
| **Threshold / dose-response curve** | "the virtue is in the dose" — a good that becomes harm past a tipping point | curve shape, the optimum band, the cliff |

### D · Convergence & evidence forms
| Form | Best for | Configured by |
|---|---|---|
| **Convergence map** | independent voices across distance/time meeting at one claim (robustness) | the voices, their distances, the shared claim, where it frays |
| **Wisdom-node card** | one idea with its converging voices, its bend, and an honest trust label | claim, voices grid, "where it bends", robustness pill |
| **Comparison columns** | contrasting two stances, two schools, or *the same fork at two ages* | the columns, the rows compared |

### E · Scope & relational forms
| Form | Best for | Configured by |
|---|---|---|
| **Radial constellation (north star)** | one fixed centre with orbiting satellites (a value and its guardians) | centre, satellites, ring |
| **Concentric rings (circles of control)** | spheres of control / influence / concern; self → family → world | the rings, their contents, the "act here" ring |
| **Venn / overlap** | where two goods overlap (the sweet spot) or two roles collide | the sets, the overlap label |
| **Journey map / terrain** | orienting overviews; the **life-stage opener**; a road with landmarks & forks | landmarks, the road, the forks along it |
| **Attention-flow (river / Sankey-ish)** | where time, money, attention, or love *actually* go | the flows, their widths, the sinks |

### F · Reframe forms
| Form | Best for | Configured by |
|---|---|---|
| **Then / now · before / after** | a perspective shift; a cognitive reframe | the before panel, the after panel, the hinge insight |

**Library rules.**
- Every form must be able to express **conditionality and tension** (R-V5); a form that can only say "do this" is unfit.
- A page or spread should **vary its form from its neighbours** unless a deliberate motif (e.g. a recurring fork, §9) calls for repetition.
- New forms are welcome; each new form is added here with its "best for" and its config parameters so selection stays principled.

---

## 7 · Form selection & configuration logic *(new)*

The graph already codes every unit with attributes (`type`, `register`, `claim_type`, `polarity`, `conditionality`, `life_domains`, `life_stages`; see architecture §3). **Those attributes choose the form.** Indicative mapping (defaults, not laws — an editor may override for variety or fit):

| If the node is… | Prefer form(s) |
|---|---|
| a **Dilemma** with high conditionality | trade-off spectrum · 2×2 matrix · branching-outcome map |
| an **Insight** that is a sequential personal choice | decision tree (interrogation) |
| about a **process / cycle** | cycle/loop · flowchart with feedback |
| about **consequences over time** | cascade/timeline |
| a **strong convergence** across traditions | convergence map · wisdom-node card |
| a **"virtue in the dose"** caution | threshold curve · pendulum |
| about **scope of control / spheres** | concentric rings · radial constellation |
| about **allocation** of a finite resource | attention-flow |
| a **developmental progression** | ladder/staircase |
| a **contrast** (two schools, or one fork at two ages) | comparison columns |
| a **reframe / perspective shift** | then-now |

**Configuration knobs** every form accepts:
1. **Content** — the specific claim/branches/poles/voices/stages/lesson.
2. **Life-domain** — colours the framing language and examples (love, work, money, grief…).
3. **Life-stage register** — reading level, word budget, visual density, colour energy (see §8).
4. **Insight weight** — how much caveat/conditionality apparatus to show (a light fork for a child vs a fully-caveated node for an adult).

The goal (R-V4): a finished page never looks like "the same mould, reused" — it looks like *this form was chosen and tuned for this idea, at this age.*

---

## 8 · The life-phase architecture *(new — the book's spine)*

The body is a **journey through the stages of a life, in order**, from the earliest stage a child can follow it read aloud, to the final stage of life (R-S1). Life-domains run *through* the stages; they are not the top level.

### Front matter — *the operating system* (before the journey)
Cover · Foreword (honest version/thin-slice framing) · **The North Star** (truth above all) · **How to read the maps** (a legend for the visual language) · **The engine of a life** (choice → consequence → interpretation → character).

### The stages
Indicative scheme (names and bands are tunable; the *ordering and the adapting register are the requirement*). Each stage = a chapter: an orienting **journey-map** opener + a central felt question + a curated handful of defining forks + a quiet close.

| # | Stage (working name) | Indicative band | The felt question | Sample forks | Register |
|---|---|---|---|---|---|
| 1 | **The Listening Years** | read-aloud, ~3–6 | *Is the world safe, and am I good?* | share or keep · the easy lie or the true thing · try again after falling · be brave about the dark · be kind to the small | read-aloud; very few words; warm pictic forms (simple two-road forks, journey maps, big friendly shapes); highest colour energy; lowest density |
| 2 | **The Naming Years** | ~7–11 | *What's fair, and where do I fit?* | fairness vs winning · loyalty vs doing right · effort vs talent · owning a mistake · the first cruelty witnessed | simple ladders, comparison columns, two-road maps; concrete |
| 3 | **The Becoming Years** | ~12–17 | *Who am I, and whose opinion rules me?* | belonging vs authenticity · risk vs caution · the courage of first love · rebellion vs conscience · who to trust · the crowd vs the self | tension becomes first-class: 2×2 matrices, spectra begin, pendulum, branching outcomes |
| 4 | **The Threshold Years** | ~18–25 | *How do I build a self that's mine?* | the safe wage vs the calling · freedom and its costs · love vs independence · leaving home · *enough* begins · who to become | full vocabulary: decision trees, trade-off maps, attention-flow, node cards |
| 5 | **The Building Years** | ~26–45 | *How do I carry what I've taken on?* | ambition vs peace · partnership through change · the help that frees (raising others) · the long game vs the quick win · time as the scarce thing · integrity under pressure | densest: cascades, cycles, threshold curves, convergence maps |
| 6 | **The Reckoning Years** | ~45–60 | *Was it the right life — and can it still change?* | regret vs reinvention · meaning vs achievement · caring for ageing parents · mortality entering view · forgiveness (self and others) · what to keep, what to lay down | reframes (then/now), balance scales, node cards on meaning |
| 7 | **The Gathering Years** | ~60–75 | *What do I pass on, and how do I let go?* | legacy vs letting go · wisdom offered vs imposed · changing roles · gratitude vs grievance · teaching without controlling | constellations, comparison columns (*the same fork now vs at 20*), gentle descending ladders |
| 8 | **The Closing Years** | the final stage | *What matters at the last, and what remains?* | truth vs denial at the end · peace vs unfinished business · farewell and forgiveness · what to hand on · the meaning made, not found | spare, quiet, weighty; mostly node cards and a final map-of-a-life; lowest density; the forking-path motif returns |

### Back matter
Methodology appendix (honest, plain-language) · Limits appendix (*what this is not*) · Colophon + credo (*convergence is robustness, not truth; recurrence is resonance, not proof*).

**Register gradient (R-S3).** Word budget, vocabulary, visual density, and colour energy rise from stage 1 to a peak around stages 4–5, then fall toward a spare, weighty close. The earliest pages must *genuinely work* read aloud to a small child; the latest must hold an adult at the end of life.

---

## 9 · The same fork at different altitudes *(new)*

Some forks recur across life — **truth, courage, enough, letting go, forgiveness, belonging**. When a fork recurs, it is **rendered freshly each time** to show how the choice changes shape with age (R-S4). For example:

- **Truth** — *Listening Years:* a simple two-road fork ("say what happened, or hide it?"). *Becoming Years:* a 2×2 of candour × kindness. *Reckoning Years:* a node card on honesty with oneself; *Closing Years:* a quiet reframe on truth at the end.
- **Enough** — appears as "share or keep" (child), "the safe wage or the calling" (threshold), "ambition vs peace" (building), "what to lay down" (reckoning).

This recurrence is a designed throughline, not repetition — and it is one of the few places the library *intentionally* reuses a theme across forms (each in a **different** form, per §6 library rules).

---

## 10 · Build pipeline, QA, and bugs to avoid (validated — carry forward)

**Generator architecture.** Token constants → SVG/HTML helpers (`esc`, `lines`, `rnode`, `diamond`, `pill`, `varrow`, `harrow`, `arrow`, `star`, `svg`) → **one function per diagram form** (the library in §6) → HTML section per page → CSS string → `build_html()` assembles the body → write `.html` then `.pdf`. Keep each form a **shared, parameterised builder** (as `build_tree` already is) so it can be configured by content and register (§7) and extended without copy-paste.

**QA loop (mandatory):** render → `pdftoppm` every page → **view each PNG** → fix → re-render. Fewer, well-chosen elements per page is more reliable than crowding.

**Bugs to pre-empt (from prior renders):**
1. **Don't stack two display elements** on one page (e.g. a giant decorative numeral colliding with a drop cap). One flourish per page.
2. **Size cards/figures to fit one page — no stranded sliver.** Use `break-inside: avoid`; verify a figure *and its caption* fit together.
3. **Watch SVG label collisions.** Draw branch/region labels **last**, on solid chips; widen gaps; make off-ramp geometry adaptive to each node's real edges (as the tree builder now does).
4. **`break-inside: avoid` on every callout/box** so navy boxes never split across a page.
5. **Don't split a short prose intro from a tall figure** across two half-empty pages. Keep intros to ~2 tight paragraphs and **size the figure so prose + figure share one well-filled page**; reserve a full page only for a genuinely tall centrepiece.

**General bar:** every page well-composed; every diagram honest (conditionality/tension visible, never destinies); premium editorial feel throughout.

---

## 11 · Prototype status & next-slice roadmap

**Current:** *A Map for Mortals* v0.0.2 — a 16-page vertical slice. It samples *across* the book (north star, engine, cascade, node, convergence, trade-offs, several decision trees, scope grid, humour, limits). Its honest weakness, now addressed in this spec: it **over-uses the decision-tree form** (R-V1).

**Next slice should demonstrate the v0.2 direction by:**
1. **Widening the visual vocabulary** — implement 4–6 new forms from §6 (suggested first set: branching-outcome map, 2×2 matrix, threshold curve, concentric rings, journey-map opener, comparison columns) as shared parameterised builders.
2. **Showing the spine** — reshape part of the slice around **2–3 contiguous life-stages** (e.g. Listening → Becoming → Building) so the register gradient (§8) and the "same fork at different altitudes" device (§9) are visible.
3. **Proving form-selection** — pick forks whose *content* obviously calls for different forms, so the slice reads as "form follows content," not "one template repeated."
4. Keeping the per-page QA discipline (§10) and the honest framing (foreword, colophon).

## 12 · The production generator & the page-spec bridge *(new in v0.3)*

The production book is built in `book/`, decoupled into three layers so curation never means editing code:

1. **The graph** (`graph/`) holds the truth: claims, units, edges, robustness profiles, verification states.
2. **Page-specs** (`book/page-specs/`, one YAML per page/spread) hold the curation: `{id, stage, sequence, form (from the §6 library), refs: [claim/unit IDs], register: {reading_level, density, colour_energy}, copy: {eyebrow, title, captions, lesson}, notes}`. Curation, reordering, re-forming, and Jason's feedback are all edits to page-specs. Every `ref` must be `publish-ready`, and every verbatim quote drawn through a ref must satisfy the print gate (REQUIREMENTS R-T1) — the build refuses otherwise.
3. **The generator** (`book/generator/build_book.py`, seeded from the proven prototype) holds the rendering: one parameterised builder per diagram form, the design system (§1–5), and the assembly. It reads page-specs; it contains no book content of its own. Locked creative copy (title, subtitle, Principle 16, "On laughing") is carried forward verbatim from the archived prototype.

Renders land in `book/renders/` and pass the mandatory per-page raster QA (§10) before any publish package. A rendered book cites a frozen graph edition (`graph/editions/`).

---

*The one fixed star, in the work and in this spec: **truth above all else.***
