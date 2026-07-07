# Implementation blueprint: turning the review into a stronger project

**Audience:** Claude

**Status:** recommended execution plan, subject to Jason's decisions

**Depends on:** `2026-07-07-adversarial-review.md` and `2026-07-07-methodology-v0.4-proposal.md`

## Desired outcome

The project should be able to make—and mechanically enforce—this promise:

> Every visible quotation, factual statement, interpretation, convergence, condition, empirical summary, and editorial synthesis can be traced to its sources and adjudication; its scope and uncertainty are explicit; the chosen visual form does not imply more than the evidence supports.

That is the operational meaning of “truth above all else”. The immediate objective is not more units, more edges, or more pages. It is to make one complete path from source to page trustworthy and repeatable, then scale it.

## Five decisions to make before implementation

Claude should present these to Jason as one concise decision package. My recommendations are included.

| Decision | Options | Recommendation |
|---|---|---|
| Research identity | curated anthology; systematic research map; hybrid | **Hybrid discovery corpus + claim confirmation dossiers** |
| Public language | global recurrence; corpus-bounded recurrence | **Always corpus/source-frame bounded** |
| Editorial voice | blended with graph claims; visibly separate | **Visibly separate and traceable** |
| External scrutiny | one-off review; risk-tiered recurring review | **Risk-tiered recurring review** |
| v1 scope | breadth first; fewer deeply supported forks | **Fewer, deeply supported forks** |

If Jason rejects the hybrid model, stop and revise the methodology explicitly. Do not retain systematic-sounding claims while operating an anthology method.

## The minimum viable methodological reset

Avoid a large platform rewrite. The reset can remain Python + YAML + git.

### Keep

- existing stable unit IDs;
- existing reports and synthesis extracts;
- YAML canonical storage;
- the design system and generator approach;
- current units as discovery records;
- the principle that computation proposes and adjudication decides;
- publish packages and escalation/decision logs.

### Change

- split source text from interpretation;
- make forks and publication assertions first-class;
- replace free-text taxonomy values with controlled IDs and display aliases;
- separate textual verification, interpretation review, empirical appraisal, rights, and community authority;
- make page-specs reference approved assertions instead of restating substance;
- generate status and audit counts from data;
- use claim-specific confirmation dossiers rather than verifying all units in numerical order.

### Defer

- Neo4j;
- large embedding models;
- corpus-wide clustering;
- more broad research waves;
- expansion of the diagram library;
- website/game implementation;
- migrating all 346 units before the new model is proven.

## Proposed repository structure

Do not move the existing store immediately. Add v0.4 stores alongside it and migrate incrementally.

```text
graph/
  units/                    # existing discovery units; stable IDs
  sources/                  # src-####: person/community/source authority
  works/                    # w-####: abstract works
  editions/                 # edn-####: concrete editions/translations
  interpretations/          # i-####: adjudicated readings of units
  claims/                   # c-####: consolidated propositions
  forks/                    # f-####: first-class conditional tensions
  relations/                # r-####: reified semantic/genealogical relations
  dossiers/                 # d-####: claim/fork evidence dossiers
  assertions/               # a-####: exact publication-approved statements
  registries/
    traditions.yaml
    domains.yaml
    life-tasks.yaml
    languages.yaml
    relation-types.yaml
  releases/                 # frozen graph/page manifests; avoid overloading editions/

book/
  page-specs/               # arrangement + editorial framing + assertion refs
  page-traces/              # generated visible assertion/source manifests
  renders/

ops/
  adjudications/            # exact independent verdict records
  protocols/                # registered confirmation dossier protocols
  audits/                   # stratified audit manifests/results
  publish-packages/

tools/
  validate_schema.py
  validate_graph.py
  validate_publication.py
  generate_status.py
  create_audit_sample.py
  freeze_release.py
  build_trace.py
```

The names are suggestions. The layer boundaries matter more than the directories.

## Object contracts

### 1. Unit: sourced expression, not canonical meaning

Keep `u-####`, but progressively narrow its responsibility.

```yaml
id: u-0023
edition_ref: edn-0048
passage: "Agamemnon 176–183"
held_text:
  original: "..."
  translation: "..."
  extent: complete-passage
speaker: chorus
context: "early choral ode following the account of Iphigenia"
textual_status:
  source_identity: verified
  wording_match: verified
  original_language: held
  attribution: secure
  checked_by: act-0123
access:
  copyright_basis_ref: rights-0048
  community_protocol_ref: null
prov:
  acquisition_ref: act-0007
```

Existing paraphrase and coding fields can remain during migration but should be marked `legacy_interpretation` and cease driving publication.

### 2. Interpretation: a contestable reading

```yaml
id: i-0023a
unit_ref: u-0023
proposition: "The chorus presents suffering as a divinely fixed path to understanding."
claim_type: metaphysical
polarity: descriptive
scope:
  speaker_scope: "chorus in this ode"
  asserted_generality: universal
  project_scope: contested
endorsement:
  value: ambiguous
  basis: "the trilogy complicates but does not simply negate the ode"
alternative_readings:
  - summary: "learning through experience, without redemptive-suffering implication"
    source_refs: [...]
adjudication_refs: [adj-0102]
status: adjudicated
```

One unit can have multiple live interpretations. Do not force disputed material into one paraphrase.

### 3. Claim: a proposition with explicit merge criteria

```yaml
id: c-0048
proposition: "Some people report or exhibit beneficial change after adversity."
claim_type: empirical
scope:
  population: "people exposed to potentially traumatic events"
  outcome: "specified domains of functioning"
  temporality: post-event
member_interpretations: [i-0102a, i-0103b]
merge_rule: "same outcome proposition; excludes claims that suffering necessarily causes growth"
non_members:
  - ref: i-0023a
    reason: "metaphysical universal law, not empirical prevalence claim"
status: adjudicated
```

This prevents the current move from Aeschylus/Nietzsche to a composite empirical sentence without recording the transformation.

### 4. Relation: an asserted relationship with evidence

```yaml
id: r-0019
type: FUNCTIONAL_ANALOGY
from: c-maimonides-help
to: c-zosima-active-love
shared_feature: "both reject easy or self-flattering giving"
non_equivalence:
  - "Maimonides explicitly targets recipient independence"
  - "Zosima explicitly targets endurance and fantasy, not independence"
genealogy:
  status: shared-scriptural-background-possible
  evidence_refs: [...]
confidence:
  conclusion: moderate
  basis: "analogy is real; proposition-level convergence is not established"
adjudication_refs: [...]
```

The `non_equivalence` field is as important as the similarity field.

### 5. Fork: question, poles, costs, conditions, unknowns

A fork is not merely an `IN_TENSION_WITH` edge.

```yaml
id: f-0004
question: "When does adversity become a source of growth, and when does it merely wound?"
claim_type_mix: [prudential, empirical, metaphysical]
poles:
  - claim_ref: c-growth-possible
    protects: [meaning-making, agency]
    costs: [pressure-to-grow, retrospective-distortion]
  - claim_ref: c-harm-common
    protects: [recognition-of-injury, permission-not-to-grow]
    costs: [under-recognition-of-resilience]
conditions:
  supported: [...]
  hypothesised: [...]
unresolved:
  - "which mechanisms distinguish perceived from measured growth"
mandatory_dissent_refs: [...]
dossier_ref: d-0004
status: dossier-complete
```

Mixed claim types must remain visibly mixed. An empirical study cannot refute a metaphysical claim without a bridging argument.

### 6. Dossier: evidence, objections, and permitted inference

```yaml
id: d-0004
target_ref: f-0004
protocol_ref: protocol-0004
search_completed: 2026-07-xx
source_frame:
  included: [...]
  excluded: [...]
findings:
  textual: [...]
  empirical: [...]
  dissent: [...]
transmission_bounds:
  lower_source_families: 1
  upper_source_families: 2
  unknown_cases: [...]
strongest_objection: "..."
response: "..."
what_would_change_assessment: "..."
permitted_inferences: [...]
prohibited_inferences: [...]
adjudication_refs: [...]
status: complete
```

### 7. Publication assertion: exact approved wording

```yaml
id: a-0082
text: "Across these studies, resilience was the most common observed trajectory; growth was neither universal nor required."
kind: evidence-summary
supports: [d-0004]
claim_type: empirical
scope_labels: [study-populations, heterogeneous-stressors]
mandatory_caveats:
  - "trajectory definitions varied"
  - "resilience is not the same as being strengthened"
prohibited_transformations:
  - causal
  - universal
  - prescriptive
status: approved-for-package-02
```

The page may shorten or style this only through declared transformation rules.

## Revised page-spec contract

Page-specs should curate, not recreate evidence.

```yaml
id: by-070-suffering
stage: building-years
sequence: 70
form: contested-node-card
fork_ref: f-0004
assertion_refs:
  title: a-0079
  central: a-0080
  voices: [a-0081, a-0082]
  evidence: [a-0083, a-0084]
  caution: a-0085
editorial:
  eyebrow: "FORK FOUR · THE WEIGHT THAT STRENGTHENS?"
  transition: "This consolation is old. Its limits matter."
  adjudication_ref: adj-editorial-0070
register:
  reading_level: adult
  density: high
  colour_energy: low
form_decision:
  reason: "one historically recurrent claim under direct empirical contestation"
  rejected:
    - form: threshold-curve
      reason: "no common quantitative dose-response model"
```

Allowed free editorial text should be narrow: transitions, questions, rhythm, and orientation. Any sentence making a source, historical, empirical, interpretive, or prescriptive claim must be an assertion ref.

## Form-selection rules that deliver the visual specification honestly

Visual variety remains a requirement, but truth fit outranks variety.

### Eligibility rules

| Form | Required evidence structure | Forbidden use |
|---|---|---|
| Convergence map | ≥2 bounded source families; relation/genealogy records | unresolved semantic analogy presented as same claim |
| Trade-off spectrum | poles vary on one defensible dimension | unrelated mechanisms forced onto one axis |
| 2×2 | two genuinely independent dimensions | axes invented to create a preferred quadrant |
| Threshold curve | structured dose/threshold evidence or clearly labelled schematic | arbitrary curve presented as measured data |
| Node card | one approved assertion plus dissent/scope | generic trust pill without a dossier |
| Comparison columns | common comparison schema and conditions | curator-invented “take it when” rules without support |
| Journey map | editorial chapter orientation | implying one universal chronological life route |
| Attention flow | measured or explicitly elicited allocation values | decorative widths implying quantities |

### Form decision record

Every page should record:

- the semantic job;
- forms considered;
- why the chosen form fits;
- what the geometry/colour encodes;
- what it deliberately does not encode;
- any reader-misinterpretation risk.

### Neutrality

- unresolved poles receive equal visual status;
- colour never means “wiser” by default;
- line width, position, area, and curve shape cannot imply evidence strength unless data-backed;
- conceptual diagrams say “schematic”; evidence charts identify source data.

### Variety gate

Check variety only after every page passes form eligibility. It is better to repeat an honest form than use a misleading novel one.

## Revised pipeline and gates

### M0 — method decision

**Output:** Jason-approved methodology identity and permitted public claims.

**Gate:** governing docs agree on discovery versus confirmation, bounded recurrence language, and `publish-ready` meaning.

### M1 — schema and enforcement pilot

**Output:** v0.4 schemas, validators, negative fixtures, controlled registries.

**Gate:** intentionally broken objects fail for the correct reason.

### M2 — one-page vertical proof

Use page 8 first because it contains licensing, interpretation, convergence, empirical directness, and editorial synthesis problems.

**Gate:** 100% visible assertion trace; no raw quote/copy bypass; external adjudication complete; changing a source object changes or blocks render.

### M3 — skeleton migration

Migrate only units/claims required by the nine-page chapter.

**Gate:** all current page-level review findings resolved or explicitly escalated; frozen mini-release; trace and QA manifests.

### M4 — P4 calibration audit

Generate a reproducible stratified sample:

- ≥10% per report;
- all dubious/apocryphal units;
- all record-only/consent-gated units;
- all in-copyright book candidates;
- oversample literary speech, metaphysical/normative boundaries, strategic advice, translations, and empirical claims.

**Gate:** material error rate below a predeclared threshold by category. If exceeded, quarantine and re-audit the affected batch/report.

### M5 — chapter dossier loop

For each stage:

1. define the felt question and cultural assumptions;
2. nominate forks from the discovery corpus;
3. register claim/fork protocols;
4. confirm only nominated candidates;
5. reject weak candidates without needing replacements;
6. approve assertions;
7. curate pages;
8. run content, visual, rights, and reader-comprehension QA.

**Gate:** stage package meets requirements and traceability before the next stage scales.

### M6 — book freeze and ship

**Output:** edition manifest, rights/community manifest, page traces, audit summary, final PDF, QA record, known limits.

**Gate:** every dependency is frozen and every visible assertion resolves inside the release closure.

## Work prioritisation: pull from the book, do not push the whole corpus

The current plan proposes rolling S2 over 313 units. That is inefficient and may verify material never used.

Use a publication-driven queue:

1. stage/fork candidate selected;
2. source and risk triage;
3. verify the smallest set capable of testing the candidate;
4. build dossier;
5. either approve, narrow, or reject;
6. verify additional voices only if they materially change the dossier or page.

Operational priority may use a workflow score, provided it is never presented as truth:

- intended package proximity;
- source accessibility;
- rights feasibility;
- interpretive risk;
- empirical/high-stakes risk;
- likely information gain;
- representation/gap value.

The highest priority is not always the easiest quote. It is the check most likely to change whether a proposed page should exist.

## Adjudication workflow

### Proposal record

Each gate records the exact proposed value and evidence.

### Blind independent review

Where possible, hide:

- desired chapter;
- preferred diagram;
- source prestige/name for pure semantic classification;
- prior model confidence;
- proposer rationale until the reviewer commits a first reading.

### Role-specific review

Use the roles defined in the methodology proposal rather than generic disagreement. One reviewer may cover multiple low-risk roles, but the record states which hat was worn.

### Resolution

- concur: retain both reasons;
- diverge with decisive evidence: deciding adjudicator selects and explains;
- both partly valid: create separate interpretation objects or narrow the assertion;
- genuine stalemate affecting publication: escalate;
- uncertainty without publication impact: retain as unresolved, do not manufacture closure.

### Calibration

Maintain a small gold/calibration set. It need not claim absolute truth; it should contain cases with strong external anchors:

- known fake quotations;
- clear literary undercutting;
- verified translation mismatches;
- empirical association/causation traps;
- known transmission chains;
- claim-type boundary examples.

Measure gate-specific error, not one global agreement statistic.

## Validation implementation

### `validate_schema.py`

- local required fields/enums/types;
- strict date format;
- controlled registry IDs;
- status transitions;
- structured rights/verification objects.

### `validate_graph.py`

- ID/filename match;
- referential integrity;
- endpoint type constraints;
- reciprocal membership;
- duplicate/symmetric relation handling;
- release closure;
- no source aliases counted as distinct entities.

### `validate_publication.py`

- assertion approval;
- mandatory caveats present;
- prohibited transformations absent;
- all quote text sourced through unit refs;
- no raw quote overlap in editorial fields;
- form eligibility;
- genealogy review for convergence;
- rights/community authority;
- page trace completeness.

### `generate_status.py`

Generate into a checked-in report or delimited section of `STATE.md`:

- counts by object/status;
- warnings/errors;
- verification and rights distributions;
- consent/record-only counts;
- controlled tradition/language/era/stage coverage;
- package readiness;
- open escalations;
- current release hash.

Humans/agents should not manually maintain volatile counts.

### CI and local gate

Run all validators and tests on every commit affecting graph, page-spec, generator, or release data. Keep local execution simple; CI is a second enforcement point, not a replacement.

## Requirement-to-evidence matrix

Claude should maintain this matrix as the real definition of done.

| Requirement family | Implementation evidence |
|---|---|
| Truth/uncertainty R-0 | assertion trace; claim-type dossiers; prohibited inference tests |
| Dilemmas R-C2 | first-class fork objects with poles, costs, conditions, dissent |
| Conditionality R-C3 | scoped assertions + mandatory caveats + form eligibility |
| Sources R-C4 | edition/unit refs and generated credits/bibliography |
| Dissent R-C5 | mandatory counterposition in dossier and page trace |
| Breadth R-C6 | normalised dashboard separating discovery and publishable coverage |
| Life spine R-S | structured stage applicability + reader tests + alternative-life caveat |
| Same fork/altitudes R-S4 | shared fork ID, distinct stage assertions/forms, comparison audit |
| Visual variety R-V1/2 | form distribution report after eligibility passes |
| Form follows content R-V3/4 | form decision record and builder inputs from graph objects |
| Honest diagrams R-V5 | semantic encoding declaration + reader comprehension test |
| Premium execution R-V6/D1 | visual QA manifest and final-page inspection |
| Single source R-D2 | mutation/metamorphic tests + 100% trace coverage |
| Print gate R-T1 | unit-level quote refs + structured rights + build refusal tests |
| Auditability R-T2 | acquisition/activity/adjudication records + release closure |
| Autonomous process R-P1 | generated queues/status and explicit escalation thresholds |
| Harness-native R-P3 | Python/YAML implementation; optional tools never gate correctness |

This makes “done” evidential rather than rhetorical.

## Reader testing that serves the vision

The specification is unusually reader-specific, but current QA is only visual.

### Epistemic comprehension test

For a small sample of pages, ask readers:

- Which parts are quotations, project interpretations, evidence, and editorial advice?
- Is one pole endorsed?
- What changes the recommendation?
- What is uncertain?
- Is a chart measured data or schematic?

If readers infer certainty or endorsement the page does not claim, redesign it.

### Stage-fit test

- Listening Years: actual read-aloud comprehension and emotional effect.
- Becoming/Threshold Years: avoid patronising register; test relevance.
- Building/Reckoning: test recognition across different family/work/class paths.
- Gathering/Closing: involve older readers and relevant care/practice expertise.

### Usefulness test

Ask readers to apply the map to a concrete scenario and explain why one pole fits. The objective is not agreement with the book; it is whether conditions and trade-offs improve reasoning without pretending to decide for them.

## Publish package v2

Every publish package should contain:

1. rendered deliverable;
2. frozen release manifest and git commit;
3. page assertion trace;
4. source/rights/community-authority manifest;
5. dossier summary for each fork;
6. adjudication summary with divergences retained;
7. coverage and exclusion statement;
8. validator/test output including warnings;
9. visual QA record tied to PDF hash;
10. reader-test summary where applicable;
11. known limits and open escalations.

Keep the package concise by linking to detailed graph records. Jason reviews the finished work and the decisions that materially affect it, not raw pipeline noise.

## Suggested first implementation commits

This sequence is intentionally small and reversible.

1. `ops: decide hybrid discovery+dossier methodology`
2. `method: define v0.4 object contracts and status transitions`
3. `tools: add controlled registries and schema validator`
4. `tools: add cross-file graph validator with negative fixtures`
5. `graph: migrate page-08 source and interpretation objects`
6. `graph: adjudicate page-08 relations and evidence dossier`
7. `book: render page-08 from publication assertions`
8. `tools: add page trace and publication-policy validator`
9. `book: freeze page-08 mini-release and QA package`
10. `ops: review pilot, amend method, authorise skeleton migration`

Do not commit a 346-unit migration before commit 10 proves the model.

## Stop conditions

Claude should stop and escalate when:

- Jason has not chosen the research identity;
- a page requires an unsupported editorial synthesis to work;
- a convergence has no defensible shared proposition;
- empirical evidence is too indirect for the intended advice;
- community authority is unresolved;
- rights are incompatible with commercial publication;
- external adjudicators materially diverge on a keystone interpretation;
- a batch audit exceeds its material-error threshold;
- reader tests consistently misunderstand uncertainty or visual semantics;
- a required assertion cannot be traced.

Stopping is not failure. Shipping a beautiful unsupported page is failure.

## What “more effective” means here

Effectiveness is not processing all available material. It is reducing the distance between work performed and book quality.

The improved method is more effective because it:

- verifies only material that can change a publication decision;
- rejects weak pages early;
- reuses dossiers and assertions across book, website, and game;
- makes external review targeted rather than asking for another global audit;
- prevents duplicate copy/source maintenance;
- turns the founding principles into executable tests;
- keeps editorial creativity free where it is genuinely editorial;
- gives Jason finished choices instead of intermediate data work;
- preserves the current corpus without allowing it to overclaim.

## Final instruction to Claude

Treat the existing implementation as valuable evidence about where the method breaks, not as sunk cost that must be defended. The visual prototype has already done its job: it exposed the exact places where source, interpretation, synthesis, evidence, and rhetoric blur.

Use page 8 to prove the replacement architecture. If the new system can prevent the anonymous-Maimonides error, refuse the indirect purpose-mortality inference, distinguish analogy from convergence, enforce the CC-BY terms structurally, and still produce a beautiful useful page, the project will have a foundation worth scaling.
