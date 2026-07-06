# Corpus Coverage Index — *A Map for Mortals*

**The master tracker.** Updated by Claude Code after every wave (Runbook P2, and again each wave in P5). This is the source of coordination truth — it lives in the repo, not in any chat. *(Template below; replace the example rows as real data lands.)*

- **Last updated:** 2026-07-06 (P1 landing validated; P2 synthesis pending)
- **Current wave:** 1
- **Saturation status:** not yet assessed
- **Reports held:** 7 (of nominal 8 — `04-eastern` never landed) · **Canonical claims (deduped):** 0 (pre-ingestion) · **Dilemmas:** ~30 named across reports (pre-merge)

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

Flag thin cells — the book is ordered by life-stage (SPEC §8), so each stage needs forks.

| | child | youth | young-adult | adult | midlife | elder |
|---|---|---|---|---|---|---|
| **forks held** | _0_ | _0_ | _0_ | _0_ | _0_ | _0_ |

| Domain | Coverage | Notes |
|---|---|---|
| love / commitment | thin | |
| work / vocation | thin | |
| money / enough | thin | |
| grief / loss | thin | |
| death / mortality | thin | |
| friendship | thin | |
| meaning | thin | |

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

> Candidates, **not** verdicts (CLAUDE.md §2.7). Confirmed only by human review.

| Cluster (canonical claim) | Appears in | # independent traditions | Note |
|---|---|---|---|
| _"Direct your energy to what is within your control."_ | 02, 04, 05 | 3 | Stoic · Gita · Serenity — classic convergence |
| _(add as found)_ | | | |

## 5 · Contradiction / tension candidates

| Tension (fork) | Sides & sources | Note |
|---|---|---|
| _Seize the day ⟷ play the long game_ | 02 (Horace) ⟷ 02/04 (Stoic/Buddhist) | first-class dilemma |
| _(add as found)_ | | |

---

## 6 · Wave log & saturation metrics

| Wave | Reports added | New canonical claims | New dilemmas | New traditions | Notes |
|---|---|---|---|---|---|
| 1 | 8 | _n_ | _n_ | _n_ | baseline |
| 2 | | | | | |

> **Saturation watch:** when "new canonical claims / new dilemmas / new traditions" trend toward zero across waves, the corpus is approaching broad-enough. (Runbook P5 — Claude proposes, Jason decides.)

---

## 7 · Backlog — next-wave queries (ranked, de-duplicated)

Each item: scope (one tradition/thinker/text/thread) + the do-not-duplicate note to paste into the Wave-N template.

1. **[P1] African wisdom** — Ubuntu + Yoruba/Akan/Zulu proverbs; Mbiti, Wiredu, Gyekye. *Do-not-duplicate:* none yet.
2. **[P1] Women's voices corrective** — across eras/traditions. *Do-not-duplicate:* George Eliot/Weil/Arendt if already in 06/07.
3. **[P1] Indigenous & First Nations oral wisdom** — with provenance/appropriation care.
4. **[P2] Persian/Zoroastrian & Mid-East** — Gathas, Khayyam, Ferdowsi. *Do-not-duplicate:* Sufi material in 05.
5. **[P2] Practical/strategic** — Sun Tzu, Musashi, Kautilya, Gracián. *Do-not-duplicate:* Machiavelli in 03/06.
6. **[P2] World folk & proverbial** — proverbs as units; cross-cultural proverb convergence.
7. **[depth] …** — pull from reports' §C/§E/§G (e.g. Epictetus *Discourses* book-by-book).

*(Claude Code re-ranks this list each synthesis pass.)*
