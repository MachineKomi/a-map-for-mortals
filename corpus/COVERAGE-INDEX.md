# Corpus Coverage Index — *A Map for Mortals*

**The master tracker.** Updated by Claude Code after every wave (Runbook P2, and again each wave in P5). This is the source of coordination truth — it lives in the repo, not in any chat. *(Template below; replace the example rows as real data lands.)*

- **Last updated:** 2026-07-06 (P2 synthesis complete from wave-1 extracts)
- **Current wave:** 1 (wave-2 prompts ready to run)
- **Saturation status:** baseline set; not yet assessable
- **Reports held:** 7 (of nominal 8 — `04-eastern` never landed) · **Report-level units:** 182 (extracts in `corpus/synthesis/wave-1/`) · **Canonical claims (deduped):** 0 (minting begins at S1/S3) · **Named dilemmas:** 38 (~10 distinct cross-report forks)

---

## 1 · Coverage map (traditions & sources)

Depth: `none` · `survey` (breadth pass) · `deep` (focused extraction).

| Tradition / source area | Depth | Report(s) | Notes |
|---|---|---|---|
| Methodology / data science | — | `01-methodology.md` | not a corpus area; validated: prescribes git+YAML-compatible pipeline, no contradictions with METHODOLOGY v0.3 |
| Greco-Roman & classical | survey | `02-greco-roman.md` | validated: ~39 units, all 6 sections, excellent locators (Stephanus/Bekker/DK); 13-quote misattribution watchlist; depth queries queued for Epictetus, Aristotle |
| Nietzsche & approved precursors | survey | `03-nietzsche.md` | validated: ~18 units; Förster-Nietzsche/*Will to Power* forgery quarantined; Kaufmann translations in-copyright — PD alternatives (Common/Ludovici) flagged; overlap w/ 06 — merge downstream |
| **Eastern (Chinese/Indian/Buddhist/Japanese)** | **none** | **— MISSING** | **expected as `04-eastern.md`, never landed — top wave-2 priority** |
| Abrahamic & Near-Eastern wisdom | survey | `05-near-eastern-abrahamic.md` | validated: ~34 units (14 Hebrew, 7 ANE, 7 Christian, 6 Islamic/Sufi); claim types kept honest; Rumi/Hafiz fake-quote hazard walled off; thin: Qur'anic doctrinal wisdom, Talmudic reasoning |
| Moralists / Enlightenment / modern West | survey | `06-modern-west.md` | validated: ~50 units; exemplary copyright tracking (incl. Russell US-PD Jan 2026 note); thin: German Idealism, Rousseau; parenthood/elder stages light |
| Literary wisdom | survey | `07-literary.md` | validated: ~20 units with `endorsement` + `dramatic_context` fields properly used (irony not flattened); Hugo/Kretzmer 1985 lyric caught; zero non-Western literature, zero 20th-century — named gaps |
| Empirical evidence base | survey | `08-empirical.md` | validated: 26 graded findings (A–E rubric) + mapping table; replication-crisis-aware (ego depletion, marshmallow, positivity ratio foregrounded as failed/contested); causal honesty good; WEIRD skew flagged not quantified |
| _African (Ubuntu, proverbs)_ | none | — | **P1 gap** |
| _Indigenous / First Nations oral_ | none | — | **P1 gap (epistemic care)** |
| _Persian / Zoroastrian / Mid-East_ | none | — | **P2 gap** |
| _Practical / strategic_ | none | — | **P2 gap** |
| _Women's voices (corrective)_ | none | — | **P1 gap** |
| _World folk & proverbial_ | none | — | **P2 gap** |

## 2 · Coverage by life-stage & domain (the book's spine)

Flag thin cells — the book is ordered by life-stage (SPEC §8), so each stage needs forks. Unit-stage tags below are report-level (pre-adjudication), tallied from `corpus/synthesis/wave-1/*-extract.yaml` (tooling: see extract files; tally script inline in session, reproducible from the YAML).

| | child | youth | young-adult | adult | midlife | elder |
|---|---|---|---|---|---|---|
| **units bearing on stage** | **3 ⚠** | **23 ⚠** | 44 | 157 | 58 | 59 |

**The spine's two ends are starving.** The book must open at read-aloud childhood and close at end-of-life; wave-1 gives the first chapter almost nothing and feeds the elder chapter mostly death/adversity material (little on late friendship, usefulness, handing-over). Corrective block added to the wave-2 prompt pack.

| Domain | Units (approx) | Coverage | Notes |
|---|---|---|---|
| self / character | 85 | strong | largest domain by far |
| adversity / suffering | 42 | strong | incl. empirical qualifiers (PTG contested) |
| work / vocation | 34 | good | |
| death / mortality | 29 | good | concentrated in adult/elder |
| money / enough | 25 | good | strong empirical layer (thresholds contested) |
| anxiety / fear | 23 | good | |
| love / commitment | 15 | adequate | thin on marriage/parenthood as lived stages |
| friendship | 16 | adequate | |
| grief / loss | 13 | adequate | mostly literary |
| meaning | 12 | adequate | empirical + existentialist |
| family / parenthood | 8 | **thin** | one Bacon unit + empirical; a stage-defining domain barely fed |
| aging | 7 | **thin** | see spine note above |

---

## 3 · Gap register (prioritised)

| Priority | Gap | Why it matters | Status |
|---|---|---|---|
| **P0** | **Eastern traditions (Confucian, Daoist, Buddhist, Hindu, Japanese)** | **expected wave-1 report never landed; without it the corpus is Western + Near-Eastern only — the single largest skew** | **queued (wave 2, first)** |
| P1 | African & Indigenous wisdom | corpus must not skew literate/recent/Western (a stated honesty commitment) | queued (wave 2) |
| P1 | Women's voices across eras | corrects the male/literate skew (wave-1 women: Austen, Eliot, Dickinson, Weil, Arendt only) | queued (wave 2) |
| P1 | Child + elder life-stages | every content report leans adult/midlife; the book's spine needs its first and last chapters fed (read-aloud childhood material; facing-the-end material) | queued (wave 2) |
| P2 | Persian/Zoroastrian; practical/strategic; world proverbs | breadth | queued |
| P2 | Non-Western + 20th-century literature | 07-literary is canon-Western, pre-1900 | queued |
| P2 | Islamic doctrinal & Talmudic reasoning depth | 05 leans Sufi-poetic; jurisprudential ethics and disputational wisdom absent | queued |
| P2 | Depth passes (Epictetus, Analects, Gita, Shakespeare…) | surveys aren't the digging | from reports' §C/§G |

### P1 validation log (2026-07-06)
All 7 landed reports passed shape validation (independent fresh-context review per report; method disclosed: reviewer shares model weights with pipeline). Common findings: all six expected sections present in every content report; misattribution watchlists uniformly strong (13 Greco-Roman, 10 Nietzsche, 7 Abrahamic, 10 modern-West, 8 literary cases); no fabricated citations detected on sampling (empirical report's 5 most-load-bearing citations verified against originals); locator quality high (standard scholarly numbering throughout). Recurring caveats to carry into ingestion (S1/S2): (1) reports' own "verified" labels are **claims, not verifications** — everything enters `attested` per METHODOLOGY §2 regardless of report labels; (2) several units flagged by the reports themselves as needing primary-text confirmation (e.g. 4 Ludovici-translation Nietzsche quotes, Wordsworth + Grand Inquisitor units in 07); (3) translation copyright must be tracked at unit level (Kaufmann, P&V, Fagles, Nicholson etc. in copyright; PD alternatives named per report); (4) all content reports lean adult/midlife — child/elder chapters underfed.

---

## 4 · Convergence candidates (cross-report canonical-claim clusters)

> Candidates, **not** verdicts (CLAUDE.md §2.7). First-pass merge candidates from the wave-1 extracts; independence is a judgment made at S4, never assumed here. Lineage flags from report 05 are preserved — several apparent convergences are **transmission, not independence**.

| Cluster (candidate canonical claim) | Appears in | Traditions (raw) | Note |
|---|---|---|---|
| Suffering can teach / strengthen (*pathei mathos*) | 02, 03, 07, **08** | Greek tragedy · Nietzsche · literary · empirical | **book gold**: the empirical layer *contests* it (post-traumatic growth may be retrospective bias) — a convergence with an honest asterisk |
| Act on what is yours; release the rest | 02, 03, 05, 07 | Stoic · Nietzschean amor fati (partial) · tawakkul · tragic acceptance | 03 flags Stoic↔Heraclitus inheritance; not all independent |
| Happiness comes from within, not possessions | 02, 06, **08** | Cynic/Stoic/Epicurean · Schopenhauer/Emerson · empirical | 08 *qualifies*: money genuinely matters up to contested thresholds — keep the qualifier attached |
| Memento mori / prepared equanimity before death | 02, 05, 06, 07 | Epicurean+Stoic · Ecclesiastes/Gilgamesh · Montaigne/Spinoza (inverted) · Lear | Spinoza's inversion (meditate on life) is a REFINES, not a member |
| Intellectual humility; cleverness ≠ wisdom | 02, 05, 07 | Socratic · Ptahhotep/Proverbs/à Kempis · Euripides | 05 warns: shared didactic genre inflates apparent convergence |
| Honest psychology of motives; self-deception as central danger | 02, 03, 06, 07 | know-thyself · Montaigne/moralists/Nietzsche · La Rochefoucauld · Oedipus/Emma | strong; watch claim-type (observational vs normative) |
| Golden Rule / one-body solidarity | 05, 07 | Hillel · Sermon on Mount · Saadi · Zosima | 05 grades Hillel↔Saadi among the most genuinely independent in the corpus |
| Moderation / the mean / optimal middle distance | 02, 06 | Aristotle/Horace/Hesiod · Schopenhauer's porcupines/Confucian li | |
| Outward-directed interest cures self-absorption | 06, **08** | Russell/Smith · empirical (purpose, meaning) | empirical SUPPORTS with grade caveats |
| Seize ordinary joy in the face of mortality | 02, 05 | Horace · Ecclesiastes/Siduri | 05 lineage flag: Qoheleth↔Mesopotamia partly NOT independent |
| Imagined suffering exceeds real suffering | 06 (Seneca via pseudo-Montaigne), Buddhist parallel named | Stoic · Buddhist *papañca* | Buddhist side unsourced until Eastern report lands |
| Becoming / self-overcoming / restless striving | 03, 06, 07 | Heraclitus/Nietzsche · Emerson · Faust/Whitman | 07 warns: don't collapse Faust and Whitman into one claim |

## 5 · Contradiction / tension candidates

> The forks are the book's subject. Cross-report recurrences below are the strongest chapter candidates; per-report forks live in the extracts.

| Tension (fork) | Sides & sources | Note |
|---|---|---|
| **Effort ⟷ acceptance** | fate/agency (02) · amor fati vs revolt (03) · tawakkul vs tie-your-camel (05) · freedom vs determinism (06) · freedom vs fate (07) | **in 5 of 6 reports — the corpus's master fork**; renders at every life-stage altitude |
| Engagement ⟷ withdrawal | civic vs lathe biosas (02) · solitude vs herd (03) · solitude vs society (06) · renounce vs seize joy (05) | second-strongest recurrence |
| Reason ⟷ passion | extirpate vs moderate (02) · reason vs passion primacy (06) · passion vs duty (07) | 06 notes it's partly terminological |
| Suffering teaches ⟷ suffering just harms | pathei mathos (02/07) + made-stronger (03) vs Oresteia counter-reading (07) + PTG contested (08) | the shadow side of the top convergence — keep both |
| Self-interest ⟷ genuine benevolence | La Rochefoucauld (06) vs Smith/Kant (06) · love/charity (05) · prosocial-spending replication FAILURE (08) | claim-type slippage warning from 06 |
| Virtue/duty ⟷ happiness as criterion | virtue vs pleasure (02) · duty vs happiness (06) · happiness ≠ meaning (08) | |
| Pessimism ⟷ affirmation | denial vs Dionysian yes (03) · Schopenhauer vs Spinoza/Emerson (06) · Macbeth's nihilism as *undercut* (07) | |
| Justice ⟷ mercy | measure-for-measure vs mercy (05) · Oresteia vengeance cycle vs forgiveness (07) | |
| Fear ⟷ love as motive | Proverbs vs Sufis/Sermon on Mount (05) | single-report but cross-tradition; strong |
| Theodicy: trust restored ⟷ protest unanswered | Job/Psalm 73/Ludlul vs Babylonian Theodicy (05) · Zosima vs Ivan (07) | across four ancient cultures + the novel; "the question outlives every answer" |

---

## 6 · Wave log & saturation metrics

| Wave | Reports added | Units (report-level) | Named dilemmas | Convergence cands | Tension cands | Traditions (raw tags) | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 7 (of 8; 04-eastern missing) | **182** | 38 (≈10 distinct cross-report forks after first-pass dedup) | 29 (12 cross-report clusters) | 35 | ~25 (normalise at S1) | baseline; unit `verified` labels are the **reports' claims** — everything enters the graph `attested` (METHODOLOGY §2) |
| 2 | | | | | | | |

> **Saturation watch:** when "new canonical claims / new dilemmas / new traditions" trend toward zero across waves, the corpus is approaching broad-enough. (Runbook P5 — Claude proposes, Jason decides.)

---

## 7 · Backlog — next-wave queries (ranked, de-duplicated)

Each item: scope (one tradition/thinker/text/thread) + the do-not-duplicate note to paste into the Wave-N template. Blocks 1–4 + 6–8 are ready to run in `prompts/deep-research/wave-2-gap-traditions.md`.

1. **[P0] Eastern traditions** (block 2·0 — replaces the never-landed 04) — Confucian/Daoist/Buddhist/Hindu/Japanese. *Do-not-duplicate:* Stoic parallels (02), Schopenhauer's Buddhist reception (06); flag convergences instead. **Several §4 clusters have named-but-unsourced Eastern members waiting on this.**
2. **[P1] African wisdom** (block 2a) — Ubuntu + Yoruba/Akan/Zulu proverbs; Mbiti, Wiredu, Gyekye. *Do-not-duplicate:* Egyptian instruction texts (05).
3. **[P1] Women's voices corrective** (block 2e) — across eras/traditions. *Do-not-duplicate:* Austen/Eliot/Dickinson (07), Weil/Arendt (06).
4. **[P1] Indigenous & First Nations oral wisdom** (block 2b) — with provenance/appropriation care.
5. **[P1] Childhood & old age corrective** (block 2g — NEW) — the spine's starving ends: read-aloud wisdom, coming-of-age thresholds; late-life friendship/usefulness/handing-over beyond death-preparation. *Do-not-duplicate:* memento-mori cluster (02/05/06), Cicero De Senectute if in 02.
6. **[P2] Persian/Zoroastrian & Mid-East** (block 2c) — Gathas, Khayyam, Ferdowsi. *Do-not-duplicate:* Sufi material (05), Saadi (05).
7. **[P2] Practical/strategic** (block 2d) — Sun Tzu, Musashi, Kautilya, Gracián. *Do-not-duplicate:* Machiavelli if in 06.
8. **[P2] World folk & proverbial** (block 2f) — proverbs as units; contradicting proverb pairs (07 has one exemplar unit).
9. **[P2] Non-Western + 20th-century literature** — 07 is canon-Western pre-1900 by its own admission.
10. **[depth] Primary-text confirmations queued by the reports themselves** — 02: Democritus B191, Cicero Tusc. I.30.74, Sophocles OT lines; 03: four Ludovici quotes vs Gutenberg; 07: Wordsworth, Grand Inquisitor. (These are S2 verification tasks, not new research.)
11. **[depth] Epictetus Discourses, Montaigne essay-by-essay, Analects & Gita book-by-book (post-Eastern)** — from reports' recommendations.

*(Claude Code re-ranks this list each synthesis pass.)*
