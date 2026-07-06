# Wave-2 · 02 · African wisdom (Ubuntu & the proverb traditions) — **P1**

**Run as a fresh deep-research query in Claude chat. Save the report to `corpus/reports/wave-2/02-african.md`.**

```
ROLE: a scholar of African philosophy and oral tradition, attentive to provenance and
to living, plural traditions (not a monolithic "African wisdom").

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
- Ubuntu / communitarian personhood ("I am because we are"); the individual-vs-community
  debate in modern African philosophy: John Mbiti, Kwasi Wiredu, Kwame Gyekye, Ifeanyi
  Menkiti, Sophie Oluwole (Yoruba thought); Placide Tempels treated critically.
- The great proverb traditions AS wisdom units: Yoruba, Akan/Ashanti (incl. proverbs
  encoded in Adinkra symbols), Zulu, Igbo, Ethiopian, Swahili (incl. classical utendi
  poetry). Anansi and other folktale wisdom; the elder and oral transmission.
- Great forks: individual vs community/personhood; destiny vs effort; deference to
  elders vs questioning; hospitality, reciprocity, justice.
- CARE: name specific peoples/languages; do not essentialise; flag colonial-era
  distortions; attribute proverbs to a people/language, not a person (use
  attribution_confidence: communal where apt); note that "Ubuntu" popularisations
  (corporate/leadership books) often distort — anchor in the scholarly literature.

ALREADY COVERED — DO NOT DUPLICATE: Egyptian instruction texts (Ptahhotep, Amenemope)
are already held from a Near-Eastern report — cross-reference and flag for merge, don't
repeat. A prior report holds a "Golden Rule / one-body solidarity" convergence cluster
(Hillel · Sermon on the Mount · Saadi) and an "individual vs community" fork is expected
to resonate with the engagement-vs-withdrawal fork held from Western material — flag
convergences/tensions with these rather than re-extracting them.

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
     e.g. proverbs falsely attributed to a single sage, invented "African proverbs").
  G) Leads — the highest-value follow-up queries and sources you surfaced (ranked).

Make the report graph-ingestible and skimmable. Depth over breadth — go deep on the
scoped target rather than wandering.
```
