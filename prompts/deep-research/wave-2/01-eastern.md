# Wave-2 · 01 · Eastern traditions — **P0, run first**

**Run as a fresh deep-research query in Claude chat. Save the report to `corpus/reports/wave-2/01-eastern.md`.**
*(Replaces the never-run wave-1 `04-eastern` — the corpus currently holds no Confucian, Daoist, Buddhist, Hindu, or Japanese material. Several wave-1 convergence clusters have named Eastern members waiting to be sourced.)*

```
ROLE: a source-critical scholar of Chinese, Indian, Buddhist, and Japanese philosophy,
rigorous about editions, translations, and misattribution.

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
- Chinese: Analects (Confucius); Mencius; Daodejing & Zhuangzi (Daoist); Xunzi; the
  Confucian-Daoist fork (cultivation/duty vs wu-wei/naturalness) as a first-class
  dilemma; Han Feizi / Legalism as the hard-nosed counter-voice (descriptive care).
- Indian: Bhagavad Gita (action without attachment; dharma vs desire); Upanishads
  (selected); Dhammapada and core Pali suttas (Four Noble Truths, impermanence,
  non-attachment); Patanjali's Yoga Sutras (practice units); Kural (Tiruvalluvar).
- Buddhist beyond India: Nagarjuna (selectively); Zen/Chan (Dogen, koan tradition —
  flag interpretive difficulty honestly); Shantideva (Bodhicaryavatara).
- Japanese: mono no aware, wabi-sabi as observational/aesthetic wisdom; Yoshida Kenko
  (Essays in Idleness); Hagakure treated critically (romanticised-bushido caveat).
- Great forks: engagement vs withdrawal; effort vs acceptance; desire vs non-attachment;
  self-cultivation vs spontaneity; duty to family vs to truth.
- Public-domain translations to anchor on: Legge (Chinese classics), Müller (Sacred Books
  of the East), Edgerton/Besant (Gita), Buddharakkhita/Müller (Dhammapada) — flag where
  Victorian translations distort (e.g. Legge's Christianising register) and name the
  in-copyright modern standard for comparison (e.g. Watson, Ivanhoe, Bodhi).
- MISATTRIBUTION WATCHLIST (mandatory): fake Buddha quotes are the single worst
  attribution swamp on the internet — check against Fake Buddha Quotes
  (fakebuddhaquotes.com); likewise spurious Laozi ("journey of a thousand miles" is
  genuine — Ch. 64 — but verify wording; "When the student is ready..." is not Laozi)
  and Confucius fortune-cookie quotes.
- Claim types: karma/rebirth/moksha claims are metaphysical, never empirical; meditation
  benefit claims may cite empirical studies but must not borrow their authority for
  metaphysics.

ALREADY COVERED — DO NOT DUPLICATE: Stoicism and the Greco-Roman schools (a prior report)
— where Eastern material converges (dichotomy of control ↔ Gita karma yoga / Buddhist
non-attachment; tranquility-as-byproduct ↔ ataraxia), flag the convergence candidate
explicitly rather than re-extracting the Western side. Also held: Schopenhauer's
Upanishad/Buddhist reception; a Buddhist-papañca parallel to Seneca on imagined
suffering; Confucian relational-ethics and Confucian-li parallels named but unsourced —
these are HOOKS your units should land on: extract the Eastern primary sources that
substantiate or complicate them, and FLAG each for merge.

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
