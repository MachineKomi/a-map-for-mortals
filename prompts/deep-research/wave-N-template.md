# Wave-N Deep-Research Template

**Where to run:** Claude chat, as a **fresh** deep-research query — one scoped target per chat (not a continuation of an old thread).
**How it's used:** Claude Code fills the four `«FILL»` slots from the current `COVERAGE-INDEX.md` and hands the finished prompt to the human. Save the result to `corpus/reports/wave-N/NN-tradition-shortname.md`.

> Keep each query **scoped to one** tradition / thinker / text / thread. Breadth gaps already have ready-made prompts in `wave-2-gap-traditions.md`; use this template for depth passes and newly-surfaced threads.

```
ROLE: «FILL: the right kind of scholar for this target — e.g. "a classicist and
historian of ancient philosophy with rigorous source-criticism".»

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

FOCUS — «FILL: the precise target and what to extract. Name the works, the themes, the
great internal forks to capture, and any special source-critical cautions.»

ALREADY COVERED — DO NOT DUPLICATE: «FILL from COVERAGE-INDEX.md: the thinkers/works/
claims already held, so this query opens NEW ground. Where a figure overlaps a prior
report, treat them only from this query's distinct angle and FLAG the overlap so units
can be merged rather than duplicated.»

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
  F) Misattribution watchlist (commonly faked/misrendered quotes for this target).
  G) Leads — the highest-value follow-up queries and sources you surfaced (ranked).

Make the report graph-ingestible and skimmable. Depth over breadth — go deep on the
scoped target rather than wandering.
```
