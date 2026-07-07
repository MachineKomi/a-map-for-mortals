# Wave-3 — Modern life & contemporary thinkers

Ready-to-run deep-research queries filling the corpus's largest remaining skew: **modern life,
modern insight, and living / recently-living thinkers.** The store is currently rich in ancient
and pre-20th-century wisdom and thin on the questions that define a contemporary life — technology,
attention, the long future, meaning in a secular age, the modern science of judgement.

**To run:** each block below is a fresh deep-research chat (Claude chat). Prepend the **Shared
research contract** *and* the **Wave-3 copyright discipline** (both below) to the block's FOCUS /
ALREADY-COVERED, then paste. **Save outputs to `corpus/reports/wave-3/NN-shortname.md`** (create the
folder). Then Claude Code ingests them through the same pipeline as every other report (S1 extract →
validate → adjudicate → the wisdom-graph engine) — see the "How these flow" note at the bottom.

> These authors are **alive or recently living and their books are in copyright.** That changes what
> a report may contain (the copyright discipline below), but **not** how it's structured: same
> schema, same claim-type honesty, same misattribution care as every tradition report.

---

## Shared research contract (hold to all — same as `wave-N-template.md`)

1. Truth above all; never start from a desired conclusion.
2. Tendencies, never destinies — wisdom is conditional and probabilistic.
3. Recurrence ≠ proof; convergence is robustness, not truth.
4. Keep claim types distinct: empirical / normative / prudential / metaphysical / observational.
5. Verify every quote against a primary edition and section/page; FLAG dubious/apocryphal; never
   fabricate a quote, citation, or source — mark "unknown" if unsure.
6. Preserve dissent and minority wisdom; don't prune to a tidy consensus.
7. Credit author/work/section/edition/year; **flag copyright status** (all of wave-3 is in-copyright
   unless noted); ground positions in reputable scholarship and the serious critiques.
8. Distinguish a writer's argued position from an established fact.

## Wave-3 copyright discipline (MANDATORY — read before running any block)

This wave is **transformative research**: we study these writers to draw on their **ideas and
insights and express them in our own words.** We are *not* reproducing their books.

1. **Paraphrase and synthesis are the deliverable.** For each wisdom unit, the `canonical_claim` — a
   neutral one-line paraphrase *in your own words* — carries the wisdom. That is what we ingest.
2. **`original_quote`: leave it `null` by default.** Include a verbatim quotation ONLY when the exact
   wording is itself the object of interest (a term the author coined, a single famous formulation),
   and then keep it to **one short sentence or phrase**, properly attributed (author · work ·
   chapter/page). **Never** string multiple quotations together; **never** reproduce a paragraph or a
   passage; **never** produce a close running summary that tracks a chapter's structure page by page.
3. **Set `copyright_flag: in-copyright`** and `attribution_confidence` honestly. These units are
   *not* print-gate candidates for verbatim reproduction — and that's correct: the book will express
   their insights in its own voice (per `A-Map-for-Mortals-VOICE.md`), never by quoting them at
   length.
4. **Minimal, attributed, transformative** is the whole rule: extract the load-bearing *idea* as a
   discrete unit; attribute it clearly; move on. If in doubt, paraphrase.
5. **Extra claim-type vigilance for this wave** (these writers mix registers fast):
   - Sweeping historical narratives (e.g. Harari) are **interpretive/observational and often
     contested** — never tag them empirical or present them as consensus history.
   - Existential-risk and AI arguments (e.g. Bostrom) are **prudential/normative and speculative** —
     a scenario is never a prediction; flag it as an argument, with its serious critiques.
   - Causal claims about technology and wellbeing (e.g. phones and mental health) are **genuinely
     contested** — cite the empirical layer honestly, tag `conditionality: contested`, and never let
     a normative worry borrow empirical authority.

## Per-unit schema & output sections

Use exactly the schema and the A–G output sections from `wave-N-template.md` (id · type ·
canonical_claim · original_quote *(usually null here)* · citation · tradition · era · register ·
claim_type · polarity · conditionality · life_domains[] · life_stages[] · addresses_dilemmas[] ·
cultivates_virtues[] · guards_against[] · attribution_confidence · speaker_context · notes; then
sections A source-inventory / B units / C forks / D virtues-&-dangers / E convergences-to-test /
F misattribution-watchlist / G leads). For `tradition`, use a modern-facet label (e.g.
`contemporary/big-history`, `contemporary/existential-risk`, `contemporary/attention-economy`,
`contemporary/secular-meaning`, `contemporary/judgement-science`).

---

### 3a · The human story — big history & where we're heading — **P0**

```
ROLE: an intellectual historian and critical reader of "big history" and popular macro-history,
alert to where a sweeping narrative outruns its evidence.

FOCUS (ideas in your own words; quotes null-by-default):
- Yuval Noah Harari — Sapiens (shared fictions / intersubjective realities — money, religion,
  nations, law — as the thing that lets large numbers of strangers cooperate; the Agricultural
  Revolution as a mixed or "luxury trap" bargain rather than pure progress); Homo Deus (the pivot
  from famine/plague/war toward bids for health, happiness, and control; "dataism" as an emerging
  value system); 21 Lessons for the 21st Century (meaning, work, attention, and story in a world of
  information overload).
- Jared Diamond — Guns, Germs and Steel (geography and luck vs innate destiny — treat the thesis
  critically, note the historians' pushback); Collapse (societies as making choices that help or
  doom them).
- David Christian / big-history "thresholds" (complexity, energy, and the long view) — lightly.
- Great forks to capture: the useful story we live by vs the literal truth; progress vs its hidden
  costs; the individual vs the shared fiction that binds the group; adapting to change vs anchoring
  in what lasts.
- CARE: Harari is enormously read and enormously contested by working historians — FLAG the
  contested big claims as interpretive, not settled; keep `conditionality: contested` where the
  scholarship divides.

ALREADY COVERED — DO NOT DUPLICATE: the empirical report (08) for any specific study; ancient
"myths that bind" material — cross-reference, don't re-extract.
```

### 3b · The long future — existential risk, AI, and our obligations forward — **P0**

```
ROLE: a philosopher of technology and risk, rigorous about the difference between an argument, a
scenario, and a prediction.

FOCUS (ideas in your own words; quotes null-by-default — a coined term like "orthogonality thesis"
may be named, not block-quoted):
- Nick Bostrom — Superintelligence (the control / alignment problem; the orthogonality thesis —
  intelligence and goals are independent; instrumental convergence — most goals imply self-
  preservation and resource-seeking; the first-mover risk of a decisive strategic advantage); the
  Vulnerable World Hypothesis.
- Toby Ord — The Precipice (existential risk as this century's defining moral problem; the moral
  weight of an enormous possible future).
- William MacAskill — What We Owe the Future (longtermism — future people matter morally now) —
  paired with its serious critics (the "fanaticism" worry; near-term-harm advocates who say
  longtermism distracts from present suffering).
- Stuart Russell — Human Compatible (build machines that are uncertain about our goals and defer to
  us — "provably beneficial AI").
- Great forks: push technological progress vs hold back for safety; the present vs future
  generations; hope/optimism vs vigilance/precaution; act on a small probability of vast harm vs
  refuse to be "mugged" by tiny probabilities.
- CARE: these are PRUDENTIAL/NORMATIVE and SPECULATIVE — a scenario is never a forecast; tag
  `claim_type` and `conditionality` accordingly and carry the critiques as first-class dissent.

ALREADY COVERED — DO NOT DUPLICATE: none held. Cross-reference the Stoic "control what is yours"
material (report 02) only as a convergence-to-test, not a re-extraction.
```

### 3c · The examined life online — attention, technology, and finitude — **P1**

```
ROLE: a critic of the attention economy and of digital life, even-handed about contested causal
claims.

FOCUS (ideas in your own words):
- Cal Newport — Deep Work (attention as the scarce, trainable resource that produces value and
  meaning); Digital Minimalism (choosing tools on your own terms).
- Jenny Odell — How to Do Nothing (resisting the attention economy; attention as an act of care and
  a form of resistance, not idleness).
- Oliver Burkeman — Four Thousand Weeks (finitude as the point, not the problem; a secular memento
  mori against the fantasy of "getting on top of everything").
- Sherry Turkle — Alone Together (connected yet alone; the substitution of connection for
  conversation).
- Jonathan Haidt (The Anxious Generation / The Coddling of the American Mind) and the Tristan-Harris
  "time well spent" critique of persuasive design — HANDLE THE CAUSAL CLAIMS CRITICALLY: the
  phones-cause-teen-mental-illness thesis is genuinely contested (e.g. Candice Odgers, Amy Orben) —
  represent it as a live debate, tag contested, cite the empirical layer honestly.
- Great forks: connection vs solitude; presence vs productivity; using the tool vs being used by it;
  more information vs better attention.

ALREADY COVERED — DO NOT DUPLICATE: mortality/finitude wisdom from the ancients (carpe diem cluster)
and the elder-stage material (wave-2/05) — cross-reference as convergence-to-test.
```

### 3d · Meaning and morality in a secular age — **P1**

```
ROLE: a scholar of modern moral philosophy and the search for meaning, careful to keep a normative
position distinct from a settled fact.

FOCUS (ideas in your own words):
- Viktor Frankl — Man's Search for Meaning (meaning available even in suffering, through work, love,
  and the stance we take toward what we can't change) — separate the philosophy from the clinical
  claims of logotherapy.
- Ernest Becker — The Denial of Death (mortality-denial as a hidden engine of human behaviour) as a
  framework, plus terror-management research as its empirical echo (tag the empirical part honestly).
- Charles Taylor — A Secular Age (the shift to the "buffered self" and the "immanent frame"; why
  belief became one option among many).
- Susan Wolf (meaning as active engagement with things worth engaging); Kwame Anthony Appiah
  (Cosmopolitanism; identity and "the lies that bind"); Peter Singer (the widening moral circle;
  effective altruism) as a live normative position WITH its critiques.
- Great forks: meaning made vs meaning found; the wide moral circle vs local loyalty and love; a
  disenchanted world vs re-enchantment; the examined stance vs simply living.
- CARE: these are argued positions, not consensus — keep the dissent; don't launder normative claims
  into empirical ones.

ALREADY COVERED — DO NOT DUPLICATE: existentialism already in the corpus (Camus/Sartre in report 06)
— cross-reference; take Frankl and Becker from the meaning-and-mortality angle, not the literary one.
```

### 3e · The modern science of judgement and the good life (critically) — **P2**

```
ROLE: a behavioural scientist who is candid about the replication crisis and about effect sizes.

FOCUS (ideas in your own words; this wave overlaps report 08 — cross-reference and FLAG for merge):
- Daniel Kahneman — Thinking, Fast and Slow (fast System-1 vs slow System-2; the biases) — NOTE the
  priming/behavioural chapters hit hard by the replication crisis, and Kahneman's own later caution.
- Daniel Gilbert — Stumbling on Happiness (affective forecasting — we're bad at predicting what will
  make us happy).
- Barry Schwartz — The Paradox of Choice (maximisers vs satisficers; more options, less satisfaction
  — note the effect is itself contested).
- Angela Duckworth — Grit — treat CRITICALLY (contested effect sizes, incremental-over-conscientious-
  ness debate); positive psychology (Seligman) with the same candour.
- Great forks: intuition vs deliberation; more choice vs less; grit/effort vs acceptance-and-fit;
  optimise vs "good enough".
- CARE: separate robust findings from contested or failed ones; carry the WEIRD-sample and
  replication caveats forward; never present a shaky finding as established.

ALREADY COVERED — DO NOT DUPLICATE: the graded findings in report 08 (money↔wellbeing,
post-traumatic growth, resilience trajectories, habit formation, ego-depletion/marshmallow as
failed/contested) — cross-reference and merge, do not re-grade from scratch.
```

---

## How these flow through the existing engine (no new pipeline)

1. **Jason** runs each block as a fresh deep-research chat and drops the outputs in
   `corpus/reports/wave-3/` (Claude Code renames to `NN-shortname.md`).
2. **Claude Code** ingests them exactly like every other report: S1 extraction to `graph/units/`
   (with `copyright_flag: in-copyright` and `original_quote` null-by-default per the discipline
   above), then `tools/validate_graph.py` / `validate_units.py`, then the Gate-C-style audit and the
   adjudication protocol, then S3/S4 clustering and edge-building — the same "wisdom analytics engine"
   the tradition corpus already runs through.
3. **The print gate does the copyright enforcement automatically:** in-copyright units cannot be
   quoted verbatim in the book; their *insights* reach the page only as our own paraphrase/synthesis
   in the house voice. So the corpus can hold modern wisdom safely, and the book expresses it
   transformatively.
4. **Coverage:** these become a new `contemporary/*` facet block in `COVERAGE-INDEX.md`; the
   life-stage spine gains its thin "modern adult life" cells; convergences between ancient forks and
   modern framings (Stoic control ↔ Bostrom-era risk; carpe diem ↔ Four Thousand Weeks) get tested at
   S4, never asserted.

**Roadmap note:** wave-3 is queued behind the round-3 recovery (Gate C/D/E reconciliation) so it
enters a store whose enforcement is sound — but the prompts are ready now, and running the research
(Jason's step) can proceed in parallel since it produces reports, not graph writes.
