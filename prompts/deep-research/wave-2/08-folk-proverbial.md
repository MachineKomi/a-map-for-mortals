# Wave-2 · 08 · World folk & proverbial wisdom — **P2**

**Run as a fresh deep-research query in Claude chat. Save the report to `corpus/reports/wave-2/08-folk-proverbial.md`.**

```
ROLE: a paremiologist (proverb scholar) and folklorist attentive to provenance.

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
- Proverbs as a wisdom-unit type, gathered across many cultures (European, Asian,
  Middle-Eastern, Latin American), plus fable traditions (Panchatantra; Jataka tales;
  La Fontaine; Aesop only for the comparative layer — his fables belong to another
  query).
- The phenomenon of CROSS-CULTURAL PROVERB CONVERGENCE — the same practical insight
  independently proverbialised in many languages — flagged explicitly as a robustness
  signal, WITH the caveat that trade routes and colonial transmission fake independence
  (grade each convergence: plausibly independent vs likely transmitted).
- CONTRADICTING PROVERB PAIRS as first-class dilemmas ("look before you leap" vs "he
  who hesitates is lost"; "many hands make light work" vs "too many cooks") — one
  exemplar pair is already held; build the set.
- Great forks proverbs encode: haste vs care; thrift vs generosity; honesty vs tact;
  courage vs prudence.
- CARE: proverbs are communal and often unattributable — record provenance as a people/
  language/region with attribution_confidence: communal; note variant forms; never
  present one culture's proverb as universal; beware invented "ancient proverbs"
  (the "may you live in interesting times" is NOT Chinese — document such cases in
  the watchlist).

ALREADY COVERED — DO NOT DUPLICATE: African proverb traditions belong to the African
query (running in parallel) — cross-reference, don't overlap; Aesop is touched by the
Greco-Roman and childhood queries; one contradicting-proverb-pair exemplar and a folk
unit are held from a literary report. Focus here on the COMPARATIVE cross-cultural
layer no other query covers.

FOR EACH WISDOM UNIT capture (this schema):
  id · type [Insight|Dilemma|Virtue|Danger|Practice|Consequence] · canonical_claim
  (neutral one-line paraphrase — the merge key) · original_quote · citation (author ·
  work · section/verse · translator · edition/year · language) · tradition · era ·
  register [aphorism|principle|argument|parable|metaphor|poem|proverb] · claim_type ·
  polarity [prescriptive|cautionary|descriptive] · conditionality [universal-ish|
  conditional|contested] · life_domains[] · life_stages[] (child|youth|young-adult|
  adult|midlife|elder) · addresses_dilemmas[] · cultivates_virtues[] ·
  guards_against[] · attribution_confidence [verified|probable|dubious|apocryphal|
  communal] · speaker_context (for literary units) · notes.

OUTPUT — end the report in these sections, in order:
  A) Source inventory table (source · tradition · era · best edition/translation ·
     public-domain vs copyright status).
  B) Wisdom units as YAML-like blocks, grouped by culture/theme.
  C) Central dilemmas / forks identified (contradicting pairs prominent).
  D) Virtues cultivated and dangers guarded against.
  E) Candidate cross-cultural convergences with independence grading.
  F) Misattribution watchlist (invented "ancient proverbs", false attributions).
  G) Leads — the highest-value follow-up queries and sources you surfaced (ranked).

Make the report graph-ingestible and skimmable. Depth over breadth — go deep on the
scoped target rather than wandering.
```
