# Wave-2 · 04 · Women's voices — a deliberate corrective — **P1**

**Run as a fresh deep-research query in Claude chat. Save the report to `corpus/reports/wave-2/04-womens-voices.md`.**

```
ROLE: an intellectual historian recovering women's wisdom across eras and traditions,
explicitly to counter the male/literate skew this project commits to naming.

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

FOCUS (real wisdom units, not tokens):
- Ancient/medieval: Enheduanna; Sappho; Hypatia (as transmitted — flag that her own
  writings are lost); Ban Zhao (critically); Murasaki Shikibu & Sei Shōnagon; Hildegard
  of Bingen; Julian of Norwich; Teresa of Ávila; Christine de Pizan.
- Early-modern/modern: Mary Astell; Mary Wollstonecraft; Margaret Fuller; Simone de
  Beauvoir; Edith Stein; Iris Murdoch; Mary Midgley; (FLAG copyright: Audre Lorde,
  bell hooks, Maya Angelou — paraphrase-only candidates).
- Across traditions: women mystics/poets — Rabia al-Adawiyya (Sufi); Mirabai & Akka
  Mahadevi (Bhakti); Zen nuns and teachers; note where Indigenous women's wisdom is
  better handled by the Indigenous query (running in parallel) and cross-reference.
- Themes/forks: care vs justice (the ethics-of-care debate — Gilligan, Noddings, and
  their critics, kept honest); voice vs silence; autonomy vs relation; the examined
  life under constraint.
- CARE: note where a woman's thought was transmitted or distorted by men (Hypatia,
  Rabia, Diotima-as-Plato's-construct); flag copyright for 20th-century figures.

ALREADY COVERED — DO NOT DUPLICATE: George Eliot, Jane Austen, Emily Dickinson (a
literary report holds them: Middlemarch "unhistoric acts", Austen's undercut irony,
"Hope is the thing with feathers"); Simone Weil (attention as generosity) and Hannah
Arendt (action/natality) are held from a modern-philosophy report — take Weil/Arendt
only for what those units omit, and flag for merge. Simone de Beauvoir is NOT yet held
(one existentialist stub aside) — treat her fully here.

FOR EACH WISDOM UNIT capture (this schema):
  id · type [Insight|Dilemma|Virtue|Danger|Practice|Consequence] · canonical_claim
  (neutral one-line paraphrase — the merge key) · original_quote · citation (author ·
  work · section/verse · translator · edition/year · language) · tradition · era ·
  register [aphorism|principle|argument|parable|metaphor|poem] · claim_type · polarity
  [prescriptive|cautionary|descriptive] · conditionality [universal-ish|conditional|
  contested] · life_domains[] · life_stages[] (child|youth|young-adult|adult|midlife|
  elder) · addresses_dilemmas[] · cultivates_virtues[] · guards_against[] ·
  attribution_confidence [verified|probable|dubious|apocryphal] · speaker_context (for
  literary units) · notes.

OUTPUT — end the report in these sections, in order:
  A) Source inventory table (source · tradition · era · best edition/translation ·
     public-domain vs copyright status).
  B) Wisdom units as YAML-like blocks, grouped by thinker/text/theme.
  C) Central dilemmas / forks identified.
  D) Virtues cultivated and dangers guarded against.
  E) Candidate cross-tradition convergences and contradictions to test later.
  F) Misattribution watchlist (commonly faked/misrendered quotes for this target —
     women's quotes are heavily meme-corrupted, e.g. "well-behaved women" is Laurel
     Thatcher Ulrich, routinely misattributed).
  G) Leads — the highest-value follow-up queries and sources you surfaced (ranked).

Make the report graph-ingestible and skimmable. Depth over breadth — go deep on the
scoped target rather than wandering.
```
