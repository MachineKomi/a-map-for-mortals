# Wave-2 · 06 · Persian, Zoroastrian & broader Middle-Eastern wisdom — **P2**

**Run as a fresh deep-research query in Claude chat. Save the report to `corpus/reports/wave-2/06-persian.md`.**

```
ROLE: a scholar of Persian literature and pre-Islamic Iranian religion.

CONTEXT: This feeds "A Map for Mortals," which maps human wisdom as a MAP OF RECURRING
FORKS — choices under tension with consequences that tend (on balance, over time) to
follow — inside ONE versioned wisdom graph that becomes a book, a website, and a text-
first life-sim game. Your report will be merged with others, so follow the shared rules
and the output schema exactly.

SHARED RESEARCH CONTRACT (hold to all of these):
1. Truth above all; never start from a desired conclusion.
2. Tendencies, never destinies — wisdom is conditional and probabilistic.
3. Recurrence != proof; independent cross-tradition convergence is robustness, not truth.
4. Keep claim types distinct: empirical / normative / prudential / metaphysical /
   observational. Tag religious/theological claims normative or metaphysical, never
   empirical.
5. Verify every quote against a primary edition and section/verse; FLAG dubious or
   apocryphal ones. NEVER fabricate a quote, citation, or source — mark "unknown" if
   unsure. Online misattribution is rampant.
6. Preserve dissent and minority wisdom; don't prune to a tidy consensus.
7. Prefer public-domain primary sources; credit author/work/section/translator/edition/
   year; flag in-copyright translations; ground positions in reputable scholarship (e.g.
   the Stanford Encyclopedia of Philosophy).
8. For literary material, distinguish a character's view from the author's endorsement.

FOCUS:
- Zoroastrianism: the Gathas of Zarathustra; "good thoughts, good words, good deeds";
  the ethical opposition of truth (asha) and the lie (druj) — note the resonance with
  this project's own "truth above all" (flag as convergence candidate, don't force it).
- Persian wisdom poetry: Omar Khayyam (Rubaiyat — note FitzGerald is interpretive, not
  literal; treat FitzGerald-vs-literal as an attribution issue per quatrain); Ferdowsi
  (Shahnameh); Nizami; Attar (beyond what a prior report holds).
- Pre-Islamic Arabian wisdom (hikma); the muʿallaqāt.
- Great forks: fate vs will; carpe diem vs piety (the Khayyam tension); truth vs the lie.

ALREADY COVERED — DO NOT DUPLICATE: Rumi, Hafiz, Al-Ghazali, Attar (one unit), and
Saadi are held from a Near-Eastern/Abrahamic report — with a misattribution quarantine
already in place for Coleman Barks' Rumi and Ladinsky's Hafiz "translations" (extend it,
don't repeat it). Take Saadi here only from the practical-ethics/adab angle; flag all
overlaps for merge. A carpe-diem cluster (Horace, Ecclesiastes/Siduri) exists — Khayyam
material should flag convergence with it, noting FitzGerald's Victorian filter.

FOR EACH WISDOM UNIT capture (this schema):
  id · type [Insight|Dilemma|Virtue|Danger|Practice|Consequence] · canonical_claim
  (neutral one-line paraphrase — the merge key) · original_quote · citation (author ·
  work · section/verse · translator · edition/year · language) · tradition · era ·
  register [aphorism|principle|argument|parable|metaphor|poem] · claim_type · polarity
  [prescriptive|cautionary|descriptive] · conditionality [universal-ish|conditional|
  contested] · life_domains[] · life_stages[] (child|youth|young-adult|adult|midlife|
  elder) · addresses_dilemmas[] · cultivates_virtues[] · guards_against[] ·
  attribution_confidence [verified|probable|dubious|apocryphal|communal] ·
  speaker_context (for literary units) · notes.

OUTPUT — end the report in these sections, in order:
  A) Source inventory table (source · tradition · era · best edition/translation ·
     public-domain vs copyright status).
  B) Wisdom units as YAML-like blocks, grouped by thinker/text/theme.
  C) Central dilemmas / forks identified.
  D) Virtues cultivated and dangers guarded against.
  E) Candidate cross-tradition convergences and contradictions to test later.
  F) Misattribution watchlist (commonly faked/misrendered quotes for this target —
     FitzGerald's Khayyam liberties; fake Rumi already quarantined elsewhere).
  G) Leads — the highest-value follow-up queries and sources you surfaced (ranked).

Make the report graph-ingestible and skimmable. Depth over breadth — go deep on the
scoped target rather than wandering.
```
