# A stronger methodology for *A Map for Mortals*

**Companion to:** `2026-07-07-adversarial-review.md`

**Audience:** Claude, as the implementing agent

**Purpose:** propose a better end-to-end method and data architecture, not merely identify defects

## Recommendation in one sentence

Use a **hybrid evidence-synthesis model**: keep the present corpus as a purposive discovery corpus, but require a bounded, adversarial, claim-specific confirmation dossier before any convergence, fork, consequence, robustness statement, or editorial synthesis becomes publishable.

This preserves what makes the project feasible and beautiful while removing the false implication that prompted anthology-building is itself empirical discovery.

## Why the project needs a methodological reset, not a patch

The present method tries to make one pipeline do five different jobs:

1. discover interesting wisdom;
2. establish what a source actually says;
3. decide whether different sources mean the same thing;
4. evaluate whether the advice tends to work;
5. write a useful, beautiful book.

Those jobs require different evidence, different reviewers, and different stopping rules. Combining them in a single `unit → claim → edge → robustness → page` progression makes an early editorial interpretation appear to acquire epistemic strength merely by moving downstream.

The reset should preserve YAML, git, the generator, stable IDs, and the existing raw corpus. The required change is conceptual: introduce explicit layers and prevent later layers from laundering judgments made in earlier ones.

## Three viable models

### Model A — honest curated anthology

The project could openly be a beautifully sourced work of practical philosophy. Claude and Jason select important voices and tensions, verify quotations, preserve dissent, and write editorial syntheses.

**Advantages**

- Fastest route to an excellent book.
- No pretence that corpus frequency measures humanity.
- Editorial judgment can be acknowledged instead of hidden behind scores.
- The graph remains useful for source management and downstream products.

**Limits**

- “Recurrence”, “convergence”, “saturation”, and robustness must be modest, corpus-bounded descriptions.
- The empirical or data-science distinctiveness of the project becomes smaller.
- Selection bias is disclosed rather than methodologically controlled.

This model would still be worthwhile. It is substantially more honest than a pseudo-quantitative map.

### Model B — research-grade systematic map

The project could define source populations, reproducible searches, formal inclusion criteria, dual screening, calibrated coding, exhaustive source windows, and systematic synthesis.

**Advantages**

- Recurrence and absence statements become defensible within declared frames.
- The research output could stand separately from the book.
- Selection and extraction decisions become reproducible.

**Limits**

- “Human wisdom” is not a searchable literature with a stable denominator.
- Oral traditions, lost works, translation histories, and unequal digitisation defeat a single global sampling frame.
- A fully systematic treatment across eras, languages, and traditions requires expert teams, not one autonomous model pipeline.
- The method could consume the project and prevent the book from shipping.

Do not choose this model implicitly. If chosen, resource and describe it as a genuine research programme.

### Model C — discovery corpus plus confirmation dossiers

This is the recommended model.

The broad corpus remains explicitly purposive. Its purpose is to surface candidate claims, forks, source families, dissent, and gaps. A candidate selected for publication then enters a separate confirmation workflow that tests a precise proposition against relevant sources, transmission history, counterexamples, and—where applicable—empirical evidence.

**Advantages**

- Preserves momentum and the existing 346-unit investment.
- Concentrates expensive scrutiny on the 250–450 units likely to matter to the book.
- Makes recurrence claims bounded without requiring an impossible universal corpus.
- Matches the project's actual unit of value: a carefully rendered fork, not a corpus statistic.
- Supports the website/game because the underlying claims and conditions become more explicit.

**Limits**

- It cannot estimate global prevalence.
- Confirmation dossiers involve judgment and must remain auditable.
- Different chapters will have different evidence depths.

That limitation is acceptable. “We tested this candidate against a declared source frame and the strongest objections we found” is a stronger and more useful claim than “it appeared often in our prompted corpus”.

## Borrow methods selectively; do not cargo-cult them

Several established approaches provide useful components:

- [PRISMA-ScR](https://www.prisma-statement.org/scoping) provides reporting discipline for bounded scoping searches: questions, inclusion decisions, source flow, and transparent limits. It should inform claim dossiers, not be claimed for the whole wisdom corpus.
- [JBI evidence-synthesis guidance](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/overview?homepageId=4685837) reinforces that different questions and evidence types require different synthesis methods.
- [RAMESES realist synthesis standards](https://pmc.ncbi.nlm.nih.gov/articles/PMC3558331/) are unusually well matched to “tendencies, never destinies”: ask what works, for whom, under what circumstances, through what mechanism. Use the context–mechanism–outcome idea for prudential claims without pretending every aphorism is an intervention study.
- [GRADE-CERQual](https://www.cerqual.org/what-is-the-grade-cerqual-approach2/) offers a better shape for confidence in qualitative synthesis: methodological limitations, coherence, adequacy, and relevance. Adapt the logic; do not copy health-review ratings onto philosophy.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) supplies a minimal provenance grammar of entities, activities, and agents. The repo needs this conceptual discipline, not an RDF/OWL stack.
- [CARE Principles](https://www.gida-global.org/careprinciples) correctly centre collective benefit, authority to control, responsibility, and ethics for Indigenous data.
- [Local Contexts labels](https://localcontexts.org/labels/about-the-labels/) show how communities can express specific access and reuse rules. The project must not assign those labels on a community's behalf; it can build space to carry community-applied labels and protocols.
- [RO-Crate](https://www.researchobject.org/ro-crate/about_ro_crate) could later package a frozen publish edition with inputs, methods, outputs, and provenance. It is optional; a YAML manifest can implement the same discipline now.

The principle is to borrow mature controls where they solve a real failure mode, while retaining the lightweight local stack.

---

## Proposed epistemic architecture

The graph should separate six layers. Each layer may refer backwards, but no layer may silently rewrite the one before it.

### L0 — acquisition record

An immutable record of what entered the project and how:

- report ID and hash;
- original prompt and model/tool version;
- acquisition date;
- target scope and inclusion instructions;
- source report block/line locator;
- extraction activity and agent;
- known omissions or failed searches.

This is where the current Wave-1 provenance gap belongs. If a prompt is unavailable, record `unknown`; do not imply reproducibility.

### L1 — source and edition

Canonical entities for:

- person/community/attributed author;
- work;
- passage locator;
- edition;
- translator/editor;
- language;
- licence/copyright basis;
- source URL/DOI/URN/archive;
- living-community authority or protocol where relevant.

Works and editions must be distinct. “Maimonides, *Mishneh Torah*” and “Meszler 2003 English on Sefaria” are not one source object. A translation is an edition-level expression with its own rights and interpretive risks.

### L2 — sourced expression

The present unit belongs here, but with less interpretation:

- exact held text;
- text type and speaker;
- immediate context;
- edition ref;
- textual verification state;
- whether the expression is complete, excerpted, translated, paraphrased, or report-only;
- CARE/access rules;
- provenance activity.

`attribution_confidence` should be decomposed. `communal`, `text-verified`, and `authorship-disputed` can all be true at once; one enum cannot represent them.

### L3 — interpretation

Every paraphrase is an interpretation object, not a neutral property of the expression:

- neutral proposition attempted;
- claim type;
- polarity;
- scope and implied subject;
- conditions;
- speaker/author endorsement;
- alternative readings;
- interpretive evidence and scholarship;
- adjudicators and verdicts;
- confidence in source fidelity.

One expression may support multiple interpretations. This matters for Aeschylus, Faust, Qoheleth, literary narrators, contested translations, and communal sayings. The current schema forces one canonical reading too early.

### L4 — synthesis objects

Claims, forks, mechanisms, outcomes, and relations live here.

#### Claims

A claim consolidates compatible interpretation objects. It must define equivalence criteria: what counts as the same proposition and what would make two members only analogous.

#### Forks

Forks need first-class objects rather than being inferred from a pair of claims:

```yaml
id: f-0001
question: "When should a person persist, and when should they release control?"
scope:
  actor: person
  contexts: [long-horizon responsibility, uncertain outcomes]
poles:
  - claim_ref: c-persist
    gains: [...]
    costs: [...]
    failure_modes: [...]
  - claim_ref: c-release
    gains: [...]
    costs: [...]
    failure_modes: [...]
conditions:
  - condition: "meaningful influence remains"
    shifts_toward: c-persist
    support_refs: [...]
  - condition: "outcome is no longer materially influenceable"
    shifts_toward: c-release
    support_refs: [...]
unresolved:
  - "how partial influence should be judged"
adjudication_refs: [...]
```

This prevents the diagram from inventing the conditions after claim selection.

#### Reified relations

An edge is an evidence-bearing assertion and should be treated as a node-like record:

- precise relation proposition;
- semantic similarity type;
- direction;
- mechanism;
- context;
- counter-reading;
- transmission evidence;
- supporting citations;
- adjudication history;
- confidence and basis.

“Converges with” should be split at least into:

- `SEMANTIC_EQUIVALENCE`
- `FUNCTIONAL_ANALOGY`
- `SHARED_MOTIF`
- `GENEALOGICAL_TRANSMISSION`
- `POSSIBLE_SHARED_MILIEU`

Maimonides and Zosima may share a broad motif around demanding help; that does not make their propositions equivalent.

### L5 — evidence dossier

Every publication candidate gets a dossier specific to its claim type. The dossier is not the claim and does not overwrite it.

For a prudential claim:

- intended outcome;
- hypothesised mechanism;
- context/mechanism/outcome configurations;
- counterexamples;
- dangers of action and inaction;
- empirical directness;
- source diversity and transmission bounds;
- strongest dissent;
- what evidence would change the assessment.

For empirical claims:

- explicit estimand;
- study design;
- population;
- exposure/intervention and comparator;
- outcome definition;
- effect estimate and uncertainty;
- causal status;
- directness to the wisdom claim;
- bias/limitations;
- replication/synthesis;
- date and strategy of evidence search.

For normative/metaphysical claims, do not manufacture an empirical robustness grade. Record source fidelity, premises, scope, internal dissent, rival frameworks, and practical implications.

### L6 — publication assertion and render

The book should not render raw claims directly. It should render approved **publication assertions**: exact sentences or structured diagram statements that declare their support and mandatory caveats.

```yaml
id: a-0042
kind: empirical-summary
text: "In this US sample, lower purpose was associated with a higher mortality hazard."
claim_refs: [c-0033]
evidence_refs: [d-0033]
transformation: conservative-summary
mandatory_caveats:
  - observational
  - older-US-sample
  - baseline-health-sensitivity
prohibited_phrasings:
  - "purpose makes people live longer"
  - "the arrow points outward"
status: approved-for-edition
adjudication_refs: [...]
```

Page-specs then arrange assertion IDs and editorial framing. A page trace can prove what was rendered.

---

## A better research workflow

### Stage 1 — discover broadly

Keep deep-research waves, but change their epistemic label:

- outputs are candidate-source reports;
- no report may mark a quotation or claim “verified” for graph purposes;
- prompts explicitly request failed searches, dissent, and material that resists the target ontology;
- prompts do not require a minimum number of convergences;
- prompts ask which proposed “great forks” are alien, misleading, or absent in the target tradition;
- reports separate direct textual evidence from researcher synthesis.

This stage maximises recall and diversity. It does not assign robustness.

### Stage 2 — register a candidate before confirming it

For each possible book claim/fork, write a short protocol **before** targeted verification:

- exact question;
- provisional proposition;
- claim type;
- source frame to search;
- equivalence criteria;
- known transmission risks;
- expected counterpositions;
- disconfirming outcomes;
- intended book use.

This stops the confirmation process from changing its target every time contrary evidence appears.

Example: do not ask “Which traditions teach the dichotomy of control?” Ask:

> Within these specified source families, which expressions distinguish owned action from unowned outcome; do they prescribe acceptance, continued effort, divine trust, or something else; and which are textually or genealogically related?

### Stage 3 — build a bounded confirmation dossier

Search the declared source frame. A lightweight claim-level flow record should include:

- sources considered;
- sources excluded and why;
- exact expressions found;
- plausible negative cases;
- translations compared;
- scholarly interpretations consulted;
- transmission evidence;
- empirical evidence search where relevant;
- unresolved questions.

Use PRISMA-like reporting where it helps transparency, but call it a project dossier, not a systematic review unless it genuinely meets that method.

### Stage 4 — adversarially test equivalence

Before merging expressions, run distinct tests:

1. **Substitution test:** could one proposition replace the other without changing advice?
2. **Reason test:** do they recommend similar action for the same reason?
3. **Scope test:** do they apply to the same actor, context, and outcome?
4. **Failure-mode test:** do they break in the same way?
5. **Counterfactual test:** would the sources disagree in a plausible case?
6. **Genealogy test:** is recurrence independent, inherited, or unknown?

If only action resembles, classify functional analogy. If wording resembles but mechanism differs, do not merge. If the source traditions would reject the shared canonical wording, the merge fails.

### Stage 5 — search against the preferred reading

Every publication candidate must receive a hostile search:

- strongest textual counter-reading;
- strongest dissent within each represented tradition;
- strongest empirical complication;
- likely harm if applied by the wrong person;
- likely harm if ignored;
- population or culture excluded by the framing;
- prestige/authority bias check;
- survivorship and translation bias check.

The adversary should not see the desired diagram or chapter title. Otherwise it is still editing toward the answer.

### Stage 6 — approve a bounded publication assertion

The output of adjudication is not “claim true”. It is:

> This exact assertion may be used in this context, with these caveats, supported by these objects, as of this evidence-search date.

That contract is enforceable by the generator.

### Stage 7 — test reader understanding

The project aims to be useful, so epistemic UX is part of truthfulness.

Test whether readers can correctly answer:

- Is this claim empirical, normative, prudential, or metaphysical?
- Is the diagram showing observed data or a conceptual model?
- Does convergence mean truth?
- Which pole is preferred, if any?
- What conditions change the advice?
- What is uncertain?

Test the Listening Years with actual read-aloud adults and children. Test the Closing Years with older and seriously ill readers or appropriate practitioners. Test colour semantics for unintended moral steering. A page can be factually careful and still mislead through design.

---

## A better adversarial-review system

Generic “try to disagree” passes are too weak. Assign failure-specific roles.

### Source critic

Checks edition, wording, attribution, passage context, translation, speaker, and reception.

### Conceptual analyst

Checks claim type, equivalence, scope, hidden premises, and whether a fork is genuine or constructed.

### Genealogy reviewer

Checks chronology, transmission, shared milieu, source-family independence, and uncertainty.

### Empirical methodologist

Checks estimand, study design, effect language, directness, replication, causal inference, and current literature.

### Context/cultural reviewer

Checks decontextualisation, Westernisation, intra-tradition dissent, authority, and applicability.

### Publication adversary

Checks whether prose, form, colour, labels, and omissions cause readers to infer more than the evidence says.

### Rights/community reviewer

Checks copyright/licence and, separately, community authority, benefit, consent, access, and reuse.

Not every unit needs all seven. Risk-tier them.

| Tier | Example | Minimum review |
|---|---|---|
| A | Short PD classical quotation, uncontroversial context | source critic + sampled conceptual review |
| B | Literary speech or disputed translation | source critic + conceptual analyst |
| C | Claimed independent convergence | conceptual + genealogy reviewers |
| D | Empirical consequence used as life advice | empirical + conceptual + publication reviewers |
| E | Living Indigenous/community knowledge | community-authorised process; model review is not sufficient |
| F | Medical, legal, self-harm, abuse, or other high-stakes advice | relevant professional review or exclusion |

Persist all verdicts. When reviewers diverge, a deciding adjudicator should state which argument controls and why. “Never blend” should mean no averaging or concealed compromise, not a ban on explicit synthesis.

## Rework independence as bounds, not grades

`strong|partial|weak|none` is too compressed. Independence is rarely a property of two ideas; it is a hypothesis about their histories.

Record evidence categories:

- direct documented influence;
- common textual ancestor;
- shared institutional or linguistic milieu;
- plausible contact route;
- chronology permits influence but route unknown;
- chronology/contact makes direct influence unlikely;
- not investigated.

Build source-family components from positive transmission evidence. Then report recurrence as a range:

- **lower bound:** number of clearly distinct source families;
- **upper bound:** number if all unresolved contacts were independent;
- **unknown:** cases too poorly sourced to count.

This is more honest than turning absence of a documented link into “partial independence”. It also makes the book's lineage-versus-rediscovery diagrams materially better.

## Replace “robustness” with a reader-use contract

The word robustness currently bundles too much. A claim can be textually secure, widely recurrent, empirically unsupported, normatively contested, and still useful in a narrow context.

Use a compact public summary with independent axes:

- **Text:** secure / disputed / indirect
- **Meaning:** clear / multiple live readings / heavily contested
- **Recurrence:** bounded source-family count or unknown
- **Effects:** supported / mixed / indirect / untested / not applicable
- **Scope:** named contexts and exclusions
- **Dissent:** strongest live counterposition
- **Use:** safe wording and mandatory caution

Avoid one visual shape that readers will interpret as an overall score. Do not colour one claim “high robustness” merely because it has many old sources.

## Better book architecture

The life-stage spine can remain, but pages should have a repeatable epistemic grammar even when their visual forms vary.

Every substantive fork should answer:

1. What is the real question?
2. What are the strongest poles?
3. What does each pole protect?
4. What does each pole cost?
5. Under what conditions does each become more apt?
6. Where does each curdle?
7. Who dissents, and on what grounds?
8. What is source wisdom versus modern evidence versus editorial synthesis?
9. What remains unknown?

This is not a requirement to print nine headings. It is a content contract the chosen form must carry.

Distinguish voices visually:

- sourced expression;
- project paraphrase;
- evidence summary;
- editorial synthesis;
- reader question.

The current design lets editorial sentences inherit the authority of adjacent quotations. That must stop.

For unresolved poles, use equal-status colour. “Wiser path” cannot be a global semantic colour token in a book committed to genuine tensions.

## Better game architecture

The current graph is not sufficient to model consequences. A game needs scoped tendencies, not aphorism adjacency.

A consequence relation should specify:

- choice/action;
- actor and affected parties;
- context/preconditions;
- time horizon;
- outcome distribution or qualitative tendency;
- mediating mechanism;
- trade-off/cost;
- evidence type and confidence;
- reversibility;
- exceptions;
- whether it is descriptive, prudential, or authored fiction.

Do not let ancient recurrence determine game outcome probabilities. Where empirical estimates do not exist, the game must label outcomes as authored scenario logic rather than evidence-derived simulation. Otherwise the downstream product will amplify the current robustness problem.

## Validation and testing that enforce the method

Add tests in layers.

### Schema tests

- controlled IDs and registries;
- required scope and claim type;
- structured rights and verification;
- no future dates;
- source/report locator exists;
- aliases do not become distinct traditions/domains.

### Referential tests

- interpretation points to an expression;
- claim members point to interpretations;
- fork poles and conditions point to claims/assertions;
- relation endpoints are type-compatible;
- publication assertion refs exist and are approved;
- edition manifest closes over every dependency.

### Epistemic policy tests

- convergence cannot publish without genealogy review;
- empirical causal wording cannot publish from associational evidence;
- conceptual chart cannot present itself as measured data;
- disputed literary speech cannot publish as authorial endorsement;
- community-gated content cannot enter an edition without authority record;
- `unknown` cannot silently default to favourable.

### Metamorphic tests

These are especially valuable:

- change a unit from verified to unverified: every dependent quote build fails;
- change an edge from convergence to transmission: recurrence count and diagram change;
- remove an evidence ref: the empirical sentence disappears or build fails;
- mark a mandatory caveat: any page omitting it fails;
- merge two claims: quote selection remains explicit by unit, never first-member arbitrary;
- change a controlled alias: counts remain stable.

### Golden-page tests

For two pilot pages, store the expected page trace, not only pixel output. Visual snapshots catch layout regressions; trace snapshots catch epistemic regressions.

## Metrics worth tracking

Avoid vanity metrics such as total units, raw tradition strings, model agreement without a gold sample, or validator exit code alone.

Track:

- percentage of visible factual/interpretive assertions with trace refs — target 100%;
- undeclared quote count — target 0;
- material error rate in independent stratified audit;
- per-gate adjudicator agreement and error type;
- unresolved high-risk items;
- verification/rights/community-authority completeness by intended edition;
- source-family lower/upper recurrence bounds;
- proportion of publication claims with a named counterposition;
- empirical statements with explicit causal status, population, and search date;
- reader comprehension of uncertainty and claim type;
- warnings as well as errors;
- reproducibility: edition rebuild yields the same trace and materially identical PDF.

Suggested quarantine rule: if a stratified batch audit finds more than a small predeclared material-error threshold, stop and audit the entire batch rather than extrapolating “15/15 clean” from an undersized convenience sample.

## Migration path from the current repository

Do not rewrite all 346 units immediately.

### Step 0 — freeze and relabel

- Tag the current graph as discovery corpus v0.3.
- Correct false dates and generated status counts.
- Mark package 1 as visual/production proof with content pending re-adjudication.
- Stop using `publish-ready` until its new contract exists.

### Step 1 — write schema v0.4 and tests

- Add controlled registries and the six-layer object model.
- Keep old fields readable during migration.
- Implement validators and failure fixtures before content migration.

### Step 2 — migrate one problematic page

Page 8 is the best stress test because it contains:

- licensed translation;
- two traditions;
- a forced convergence;
- an indirect empirical bridge;
- editorial counsel;
- a factual ranking error.

If the new model can make page 8 honest and traceable, it can handle easier pages.

### Step 3 — migrate the 33-unit skeleton

- Create interpretation objects;
- re-adjudicate claims and edges;
- create fork and dossier objects;
- approve publication assertions;
- regenerate the nine pages from a frozen mini-edition.

### Step 4 — calibrate on a stratified P4 sample

Audit at least 10% per report plus all high-risk units. Use the results to refine schema and prompts. Do not migrate the remaining units until error modes stabilise.

### Step 5 — migrate by publication priority

Only transform units needed for the next chapter/dossier. Long-tail discovery units can remain v0.3 `attested` until used.

### Step 6 — resume waves only for identified dossier gaps

Future research prompts should answer registered questions, seek disconfirmation, and record negative results. Broad gap waves remain useful occasionally, but unit volume is no longer a progress target.

## Proposed immediate decisions for Claude

1. Recommend Model C formally in `ops/DECISIONS.md`; Jason decides.
2. Do not begin rolling verification of 313 units merely because they exist. Verify by dossier and intended publication use.
3. Treat the current review's page-level errors as a test suite for schema v0.4.
4. Produce an architecture decision record before code changes: layer boundaries, object IDs, migration compatibility, and what remains free text.
5. Build the page trace and assertion contract before expanding the form library.
6. Use this external review as one adjudicator, not as authority. Where Claude diverges, preserve the strongest evidence on both sides and escalate genuine methodological choices to Jason.

## Final view

The project's central insight remains sound: wisdom is often better represented as conditional forks than as isolated quotations. The mistake would be to infer that a graph representation automatically makes the work empirical, or that repeated prompted retrieval makes a claim robust.

The better project is both humbler and stronger:

- discovery is openly curated;
- source text remains distinct from interpretation;
- similarity remains distinct from equivalence;
- recurrence remains distinct from independence;
- oldness remains distinct from truth;
- evidence remains distinct from editorial usefulness;
- the page says only what its trace can support.

That architecture will produce a better book, a safer website, and a more honest game. It also gives Claude and future external reviewers precise surfaces on which to disagree productively.
