# Adversarial review of *A Map for Mortals*

**Audience:** Claude, as the implementing agent

**Review baseline:** commit `1feb9fbc246e09876139c86a86f2211b54d1c0c0` on 2026-07-07

**Scope:** project intent, requirements, specification, methodology, runbook, prompts, corpus synthesis, committed graph, validator/tooling, operations records, page-spec bridge, generator, and all nine rendered pages of publish package 1

**Review posture:** constructive but deliberately hostile to unsupported confidence

**Companion proposal:** `2026-07-07-methodology-v0.4-proposal.md` develops the recommended hybrid research model, six-layer graph architecture, adjudication roles, validation tests, and migration sequence.

## Executive verdict

The project has a strong and unusually explicit ethical centre. Its best decisions are worth preserving: units are separated from canonical claims; source uncertainty is represented rather than hidden; translation mistakes have actually been caught; literary endorsement is modelled; dissent and transmission are treated as data; the CARE instinct is correct; and the rendered chapter is visually assured.

The present system is not yet capable of delivering the project's strongest promise, however. It can produce a beautiful, carefully caveated anthology. It cannot yet justify presenting itself as a graph-derived map whose recurrence, convergence, robustness, and curation are disciplined by the corpus. Four foundational problems prevent that:

1. The rendered book is not substantively generated from the graph. Most claims, voices, conditions, evidence statements, and interpretations live as manually written copy in page-specs. Only explicitly declared quote blocks reliably pass through the graph and print gate.
2. The corpus is a purposive, model-generated discovery anthology, not a sample from which frequency, recurrence, saturation, or “master fork” claims can be inferred. The current language sometimes exceeds that limitation.
3. The robustness profile has no coherent measurement semantics. Dimensions point in different directions, `high` does not consistently mean the same thing, inapplicable dimensions are forced to `low`, and formulaic absence-of-evidence language is being promoted to `publish-ready`.
4. The approved walking skeleton contains several substantive interpretive and empirical overreaches. They are exactly the kind of aesthetically persuasive errors that “truth above all else” is meant to stop.

My recommendation is to treat P3 as a successful **visual and production prototype**, not as proof of the epistemic pipeline. Do not begin large-scale S2 or corpus-wide merging until the P0 items below are addressed. Continuing now would make incorrect structure expensive to unwind.

## What should be kept

- The founding principles are clear, memorable, and operationally useful.
- The S2 translation checks have demonstrated real value. Correcting Carter/Higginson, P&V/Garnett, Touger/Meszler, and other mismatches is stronger evidence of seriousness than any methodology prose.
- The two-level unit/claim distinction is correct, even though it has not yet been proven at merge scale.
- `CONTRADICTS` versus `IN_TENSION_WITH`, and recurrence versus transmission, are important distinctions.
- The decision to show the weakness of “suffering strengthens” is directionally right.
- The visual form library and page composition are strong. I viewed every page of `building-years-v0.1.0.pdf`; the pages are clean, legible, and varied.
- Unknown fields are generally left unknown in the P4 ingestion rather than supplied from memory.
- The Indigenous record-only and consent-gate concepts should remain, with a stronger governance process.

These strengths make the problems below worth fixing. They are not cosmetic criticisms.

## Priority summary

| Priority | Finding | Why it matters |
|---|---|---|
| **P0** | The page-spec bridge bypasses the graph and print gate | The “single source of truth” claim is currently false in the render layer |
| **P0** | Corpus design cannot support frequency, saturation, or global recurrence inferences | The project risks turning prompted selection into apparent discovery |
| **P0** | Robustness profiles are not valid measurement objects | Attractive trust labels can communicate confidence that was not earned |
| **P0** | Publish package 1 contains material content errors and forced syntheses | The first public proof already demonstrates the central failure mode |
| **P0** | Adjudication is insufficiently independent and insufficiently persisted | A fresh context with shared weights is not a reliable adversary for the same model pipeline |
| **P1** | Validation checks shape, not truth-system integrity | “0 errors” currently permits broken refs, bypasses, stale ledgers, and false dates |
| **P1** | Provenance, textual verification, interpretation, evidence quality, and licence are conflated | A checked string is being allowed to look like a checked claim |
| **P1** | The implemented ontology is too thin for the promised graph and downstream products | The website/game would need a second content model |
| **P1** | Life-stage and taxonomy coding are uncontrolled and culturally over-generalised | Coverage counts and stage curation are not dependable |
| **P1** | Operational records are contradictory and non-reproducible | The repo is not yet a trustworthy memory system |
| **P2** | Reproducible builds, QA evidence, and dependency integrity are incomplete | The PDF cannot yet be tied to a frozen, inspectable edition |

---

## P0 findings

### 1. The graph is not the book's substantive source of truth

The architecture promises three layers: graph truth, page-spec curation, and content-free rendering. The implementation does not enforce that separation.

`book/generator/build_book.py` loads claims and units, but almost every form renders `spec["copy"]` directly. Apart from `verbatim_quotes` and `quote_ref` in comparison columns, the graph is not consulted for claim wording, voices, source metadata, independence, robustness, evidence, edge meaning, conditions, or caveats. `refs` are not read or validated by the generator. A page can cite four claims and print unrelated content without failing.

This creates a second, unaudited wisdom store in `book/page-specs/`:

- `voices[].name`, `meta`, and `gloss` manually duplicate source and interpretive data.
- `claim_label`, `bend`, `evidence`, `frays`, spectra, conditions, and lessons are manually asserted.
- Independence styles are manually assigned in page copy rather than derived from edges.
- Composite claims are written in page copy without becoming adjudicated graph objects.
- There is no trace from a visible sentence to a unit, claim, edge, empirical source, or editorial judgment.

The hard print gate is therefore narrower than the package says. I found at least three verbatim passages manually embedded in copy fields and bypassing `Graph.printable_quote()`:

- `by-020-carrying.yaml` embeds Rabbi Tarfon's verified wording in `copy.outro`; only `c-0001` is declared in `verbatim_quotes`.
- `by-030-judgment.yaml` embeds sixteen contiguous words from Marcus Aurelius in a voice gloss, with no `verbatim_quotes` entry.
- `by-070-suffering.yaml` embeds Nietzsche's famous wording in a voice gloss, with no quote declaration.

The Faust phrase in page prose and other quote-like fragments expose the same design weakness even where wording is shortened. The build's claim that it “pulls quotations and sources FROM THE GRAPH (never hand-copied into specs)” is contradicted by the page-specs.

There are additional enforcement gaps:

- The build does not require `refs` to exist or be `publish-ready`.
- It does not require claims used by prose or forms to be listed in `refs`.
- It chooses the first member unit of a claim for a quote. This will become arbitrary after real merges.
- It infers a CC-BY licence by searching for the substring `cc-by` in free-text notes.
- It does not validate the visible copy against the referenced edge direction, confidence, or independence grade.

**Required repair**

1. Make visible assertions addressable. Each page object should use structured references such as `claim_ref`, `unit_ref`, `edge_ref`, `evidence_ref`, and `editorial_assertion_ref`, not copied names and conclusions.
2. Quote by **unit ID**, never by claim ID. Store an exact excerpt or character/line range plus the displayed translation/version.
3. Move composite statements into graph claims or a first-class `editorial_assertions/` store with claim type, provenance, method, confidence, and adjudication record.
4. Make builders derive voices, credits, independence styles, robustness labels, and empirical evidence from refs.
5. Add a page-spec validator and a quote linter over **all string fields**. Any sufficiently long overlap with held quotation text should fail unless declared through a quote object.
6. Emit a page trace manifest listing every visible assertion, its source object, transform, adjudication, and licence.

**Acceptance test:** change the canonical claim or an independence edge and rebuild. The visible page must change without editing page copy. Introduce an undeclared quotation into any copy field; the build must fail.

### 2. The corpus is a discovery anthology, not a frequency-bearing sample

The research prompts are thoughtful, but they are purposive and strongly seeded. They name target thinkers, desired themes, “great internal forks”, known convergences, life-stage needs, and output quotas/shape. They require the researcher to end with dilemmas and convergence candidates. That is appropriate for discovery. It is not an unbiased way to discover how frequently human wisdom contains particular structures.

Consequences:

- “Effort versus acceptance appears in five of six reports” says more about six prompt modules and the shared schema than about human wisdom.
- Calling it “the corpus's master fork” overstates what the acquisition design establishes.
- Recurrence counts are conditioned on which texts the project asked the model to search, which passages the model selected, and how many units it chose to return.
- Report size is not exposure. A tradition represented by one survey and a tradition represented by fifty selected units do not supply comparable votes.
- “New claims per wave” is not a saturation measure when each wave deliberately opens preselected new regions and each model response has an arbitrary length budget.
- Absence from a report cannot be treated as absence from a tradition because the reports are not exhaustive text searches.

The original Wave-1 prompts are missing. `prompts/deep-research/wave-1/README.md` explicitly says the archive is empty. This breaks reproducibility for nearly half the corpus.

The current data also show that the coding vocabulary is not stable enough for quantitative summaries:

- 346 units use **153 distinct tradition strings** and **154 distinct domain strings**.
- Obvious synonyms coexist: `German philosophy`/`german-philosophy`, `French moralists`/`french-moralist`/`french-moralists`, `Russian literature`/`russian-literature`, `Pre-Socratic`/`presocratic`, and `aging`/`ageing`.
- `adult` is attached to 306 of 346 units, while `child` is attached to 21. Broad “could apply” tags make apparent coverage much larger than direct life-stage evidence.
- Twelve units have no life stage despite the validator allowing this.

**Required repair**

Define the inferential target before doing more research. A practical two-corpus design would work:

1. **Discovery corpus:** purposive, broad, gap-filling, explicitly non-frequency-bearing. Its job is to find candidate forks, dissent, and sources.
2. **Validation corpus:** a declared sampling frame of texts/passages with reproducible inclusion and unitisation rules. Its job is to test whether nominated claims recur, fail to recur, or change meaning within that bounded frame.

For the validation corpus, record:

- why each source/text entered the frame;
- the searchable textual extent and edition;
- extraction coverage, including negative results;
- source-family and transmission clusters;
- units per fixed amount of source text where possible;
- the exact prompt/model/tool and report hash;
- a bounded claim: “recurs in X of Y sampled source families”, never “human wisdom agrees”.

Use saturation only within a declared frame, and report discovery saturation separately from validation recurrence. Recover the Wave-1 prompts if possible; otherwise permanently label Wave-1 acquisition as non-reproducible.

### 3. The robustness profile is not a coherent measurement model

The profile looks rigorous, but its dimensions and ratings cannot support the promised partial ordering.

Problems:

- Direction is inconsistent. `high` recurrence seems favourable; `high` contestation appears to mean more dispute, which is unfavourable; `high` claim type means “empirical”, which is not intrinsically better than normative or prudential; `high` attribution integrity is favourable.
- Inapplicable dimensions are forced to `low`. Empirical claims receive low recurrence and temporal spread even when those axes are irrelevant. A dominance comparison would therefore penalise empirical claims for category mismatch.
- `claim_type_dim` improperly turns a type distinction into a quality hierarchy. A metaphysical claim receives `low` because it is not empirically testable, despite the project promising to keep claim types distinct rather than rank one truth type above another.
- “No recorded contestation in the skeleton set” is treated as low contestation, and “no known refutation” becomes moderate survival. In a 33-unit curated set, those are absence-of-search statements, not evidence.
- Several empirical profiles give `high` “survives scrutiny” because a failure flag was not recorded. That is circular and vulnerable to literature-search gaps.
- Most profile basis lines are formulaic outputs of graph degree and the 33-unit skeleton, not adjudicated evidence reviews.
- The claimed partial-order and sensitivity analysis are not implemented anywhere.

All 33 current claims are single-member claims. The walking skeleton therefore did not exercise canonical merging at all. It proved unit passthrough plus manually curated edges, not S3 clustering. Calling the “full pipeline proven” is inaccurate.

**Required repair**

Replace the universal high/moderate/low vector with claim-type-specific evidence dossiers:

- **Textual/attribution:** edition match, original-language availability, translation comparison, speaker/context, attribution dispute.
- **Empirical:** design, estimand, sample, causal status, effect size/uncertainty, directness, risk of bias, replication/synthesis, external validity, date of literature search.
- **Prudential:** mechanism, conditions, counterexamples, harms of application and non-application, evidence directness.
- **Normative:** tradition fidelity, explicit premises, internal dissent, rival frameworks; no pretence that recurrence settles the norm.
- **Metaphysical:** source fidelity, coherence, scope, rival positions; empirical support marked `not-applicable`, not `low`.

Every field needs an orientation and an `unknown`/`not-applicable` state. “Survives scrutiny” should record the strongest named objection and the reasoned result, not the absence of a failure flag. Do not implement dominance until the dimensions are commensurable and monotonic; it may be better to abandon ranking entirely.

Define `publish-ready` as a representation contract: safe to publish **in a specified wording with specified caveats**, not “robust” in the abstract. Store those mandatory presentation constraints so the generator can enforce them.

### 4. Publish package 1 contains substantive overreach

The visual result is good. The epistemic result needs re-adjudication. These are not copy-editing points; they expose structural weaknesses.

#### Page 2 — carrying and releasing

The page says “Voices that never met” while Edgar/Lear is explicitly displayed as lineage and `e-0003` says transmission is likely. More importantly, Rabbi Tarfon's unfinished-work injunction is not the same “division of labour” as Epictetus's dichotomy of control. It may refine or complement it, but calling it convergence requires a more exact shared proposition. The page's central synthesis is stronger than the edges warrant.

#### Page 4 — ambition and peace

The spectrum is built backwards from an attractive fork. Thoreau's “quiet desperation” and Pascal's perpetual preparation both diagnose unlived life; neither is straightforward evidence for a contentment pole. Faust's wager is a dramatic pact spoken by a complicated character who is ultimately saved, not a clean endorsement of striving. Qoheleth supplies present joy, but the page's “two hells” and single striving/contentment axis flatten at least three distinct mechanisms: compulsive striving, conformity/resignation, and deferred living.

This is precisely the failure mode the project rejects: sources recruited to fill a predetermined diagram.

#### Page 5 — money

The plotted curves are generated from arbitrary mathematical functions in `form_threshold_curve`; they are not data from Killingsworth, Kahneman, and Mellers. The title says “measured”, the chart has quantitative labels, and the caption names a study, so a reader will reasonably infer a data visualisation. It is a conceptual illustration.

The prose then crosses its own causal caveat. “Money moves the curve”, “buys least where the pain is deepest”, and “less than temperament” are not established by the displayed observational analysis. The 2024 PNAS critique specifically argues that inappropriate causal assumptions underlie the original conclusions: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11572929/>. If the graph records “causal direction remains open”, the prose cannot quietly restore a causal story.

Create separate form types for `conceptual-curve` and `evidence-plot`. An evidence plot must be generated from structured values or digitised source data, carry axes/units/uncertainty, and identify the exact figure/table. Otherwise label it prominently “schematic, not data”.

#### Page 7 — suffering

“The oldest consolation on record” is unsupported; at most it is the oldest source in this selected set. More seriously, the claim that the *Oresteia*'s vengeance cycle “learns nothing” ignores the third play's establishment of a court and transformation/pacification of the Furies. The ending is contested, but it cannot be summarised as no learning without argument. The primary text establishes the continuing court at *Eumenides* 674–710: <https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0006%3Acard%3D674>. Current scholarship treats the legal transition as pivotal even while disputing triumphalist readings: <https://www.journal.edizioniets.eu/index.php/dioniso/article/view/199>.

The empirical asterisk is useful, but Frazier 2009 studied 122 undergraduates reporting a trauma over two months; it challenges retrospective PTG measurement, not all survivor reports in all settings. The source abstract is here: <https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2009.02381.x/>. The Galatzer-Levy review's 65.7% modal resilience estimate is real, but it concerns heterogeneous post-stressor trajectories, not a universal “return to baseline” for every adversity: <https://www.sciencedirect.com/science/article/pii/S0272735818300539>.

#### Page 8 — helping

The sentence “Maimonides ranks the anonymous, strengthening gift above every warmer-feeling kind” combines two different ranks. Strengthening a person to self-sufficiency is the highest level; mutual anonymity is the next level. The page's own quotation does not say anonymous. See the source hierarchy: <https://www.sefaria.org/Mishneh_Torah%2C_Gifts_to_the_Poor.10.7-14/>.

Zosima's active-love passage concerns labour, endurance, applause, and fantasy. It does not itself say that help should make the recipient independent. `e-0019` forces a convergence by importing “the other's strength” into Dostoevsky's claim.

The life-purpose mortality result does not support “help that frees”. The graph itself links it only indirectly and at low confidence to Russell's outward interest, and `c-0019` is not even among the page refs. “The arrow points outward” turns an observational hazard association into directional counsel after admitting it is an association. The paper reports HR 2.43 for lowest versus highest purpose, not “two-and-a-half times the mortality” in the ordinary risk-ratio sense: <https://pmc.ncbi.nlm.nih.gov/articles/PMC6632139/>. A 2026 reanalysis also argues that baseline health substantially weakens purpose–longevity estimates, which should enter the current evidence review: <https://pmc.ncbi.nlm.nih.gov/articles/PMC13193554/>.

#### Page 9 and chapter framing

“The Building Years' truest sentence” is editorial rhetoric, not a finding. That can be acceptable if the editorial voice is openly distinguished from mapped evidence. At present the system does not distinguish them.

The opener also assumes a culturally and economically specific life course: choosing largely complete by 26, then mortgage, marriage, child, dependants, and a twenty-year holding pattern. This is recognisable to one audience but not a universal life stage. The book needs a visible reminder that stages are lenses, not a normative timetable.

**Required repair:** reclassify package 1 as “design/production proof; content under re-adjudication”. Rebuild it only after the traceable page model exists, using the same pages as acceptance tests.

### 5. Adjudication is not independent enough, and its evidence is not retained

The same model family performs report generation, report validation, extraction, paraphrase, classification, clustering, edge proposal, robustness construction, curation, and the “fresh-context” adversarial pass. Fresh context reduces anchoring but does not address correlated knowledge gaps, cultural priors, or shared stylistic convergence.

The current record is not sufficient for audit:

- `ops/adjudications/2026-07-07-s3s4-skeleton.md` says the full verdict table existed in pass output, but that output is not in the repo.
- Proposals, exact adversarial objections, and final rationales are summarised, not preserved object by object.
- Independence claims contain no citations to intellectual-history evidence.
- The required `graph/intellectual-history.md` does not exist.
- All nine divergences were adopted and none escalated. That may be correct, but without the complete record it also looks like “the adversary always wins”.
- The architecture originally promised human sample adjudication and inter-rater agreement. Methodology v0.3 quietly replaces that with Claude as primary adjudicator and does not report calibration.

“Never blend verdicts” is also too rigid. It correctly prevents laundering disagreement into false consensus, but two readings can each identify different valid constraints. Preserve both verdicts, then use a named deciding pass or human/domain expert to select or synthesise with explicit reasons. Do not average confidence.

**Required repair**

- Persist exact gate inputs, independent verdicts, model/tool versions, prompts, and final decisions.
- Use blind IDs where possible so adjudicators do not see the desired chapter or diagram.
- Add a third, deciding process for divergences.
- Establish calibrated external samples per gate. Domain-expert review is necessary for Indigenous/community material, original-language keystone claims, empirical synthesis, and difficult literary endorsement. Jason need not perform it personally.
- Report agreement and error categories by gate, not one global percentage.
- Build the intellectual-history layer with cited evidence and explicit “not searched” versus “searched, no evidence found”.

This external review should not be treated as a one-off absolution. It demonstrates why recurring independent checks are needed.

---

## P1 findings

### 6. The validator validates local shape, not graph integrity

At the baseline commit, `python tools/validate_units.py` reports:

> Validated 404 file(s): 0 error(s), 17 warning(s).

That is useful but far short of the implied gate. It does not check:

- filename equals object ID;
- referenced claim/unit/edge endpoints exist;
- unit↔claim membership is reciprocal;
- symmetric edges are duplicated or contradictory;
- edge endpoint types are legal for the edge type;
- edge confidence is an enum;
- claim polarity and conditionality are present;
- provenance source reports and source locators exist;
- page-spec refs exist and are publish-ready;
- every visible quote passes the print gate;
- future or impossible dates;
- licence evidence;
- edition manifests;
- taxonomy vocabulary;
- source/report hashes;
- required adversarial records;
- `publish-ready` presentation constraints.

It also treats missing source work/author as warnings while the ledger calls the result “clean”. Either warnings are accepted debt and should be counted in the gate, or they are failures. Do not use “clean” to mean “exit code zero”.

Add schema validation plus cross-file semantic validation and run it in CI/pre-commit. Include negative tests for every honesty rule. A gate without a test is a convention.

### 7. Verification fields conflate different questions

`verified-primary` currently means roughly “the displayed string was matched to an edition”. That does not establish:

- correct original-language meaning;
- translation quality;
- attribution of the underlying work;
- speaker/endorsement interpretation;
- accuracy of the canonical paraphrase;
- truth or practical reliability of the claim;
- copyright status in the relevant market.

The word “verified” on reader-facing pills can therefore mislead. Prefer “text checked to [edition]” for wording.

Empirical units use `verified-secondary` even where the full paper was read, because the tier system was designed for quotations rather than evidence. A DOI match is source identity, not evidence appraisal.

Copyright has the same problem. `copyright_flag` is one of `public-domain`, `in-copyright`, or `unknown`, while licences are inferred from notes. Public-domain status is jurisdiction-dependent. The graph contains 68 in-copyright units; 64 retain held text totalling about 7,782 characters. Publishing a repository with upstream copyrighted extracts is a separate permission question; labelling the repository “audit only” does not itself grant permission.

Use structured, separate records:

- `source_identity_status`
- `text_match_status` and matched edition
- `original_language_status`
- `translation_status` and comparison/reviewer
- `interpretation_status`
- `evidence_appraisal_status`
- `copyright_basis`, jurisdiction, term, checked date
- `licence_spdx`, version, URL, attribution text, commercial/derivative permissions

The print gate should consume those fields, not notes.

There is also a governing-document contradiction to resolve: Requirements R-0.5 says unverified quotations start at `dubious`; Methodology §2 and actual ingestion use `attested`. The latter is more useful, but the requirement must be corrected so the gate has one meaning.

### 8. The implemented graph is too thin for the promised ontology

The architecture promises typed nodes for insights, dilemmas, virtues, dangers, domains, life stages, practices, consequences, thinkers, traditions, and works. The implemented canonical store has only units, claims, and edges. Thinkers, works, traditions, domains, and stages are uncontrolled strings embedded in units.

This is why there are 153 tradition strings and 154 domain strings for 346 units, and why the graph cannot yet answer the queries envisioned for the website/game. Edge types such as `FROM_WORK`, `IN_TRADITION`, `APPLIES_IN`, `CULTIVATES`, and `GUARDS_AGAINST` have no canonical target stores or endpoint constraints.

Decide now whether to:

- implement small controlled entity stores with stable IDs and aliases; or
- explicitly narrow the v1 promise and remove unsupported graph relation types.

Do not leave free-text values while planning recurrence and coverage metrics. At minimum create canonical registries for source family, tradition/lineage, work/edition, domain, life stage, and geography/language, with aliases separated from display labels.

### 9. Life-stage coding and the spine need a scope model

The life-stage spine is a strong editorial device, but the current schema turns broad relevance guesses into data. A unit being usable by an adult is not evidence that it arises from, defines, or is distinctive to the Building Years.

Replace `life_stages[]` with structured applicability:

- stage/life-task;
- `direct` / `adaptable` / `incidental`;
- evidence or rationale;
- cultural/class/family assumptions;
- confidence;
- contraindications or excluded paths.

Keep ages explicitly indicative. Include non-linear lives, disability, precarity, migration, childlessness, early bereavement, late starts, and deaths outside the “Closing Years”. “Refuse to flatten a life” must change the spine's data model, not only appear as a disclaimer.

The skew dashboard is also incomplete. The methodology requires monitoring tradition, language, gender, and era. The index gives broad tradition prose and stage/domain counts, but no normalised language, era, gender/unknown, geography, oral/written, elite/non-elite, living-community, or publication-readiness distributions. Separate raw research coverage from **publishable** coverage; Indigenous material behind a consent gate does not yet close a publishable coverage gap.

### 10. Operational records currently contradict the repository

At baseline:

- `STATE.md` begins by saying P3 is paused for Jason's review and Wave-2 is unprocessed, although package 1 is approved and P4 ingestion is complete.
- Its status snapshot says the graph has 33 units and 35 validated files.
- Its next actions contain duplicate numbering and obsolete P4 work after the pause item.
- `corpus/COVERAGE-INDEX.md` says the graph has 33 units although 346 are committed.
- `README.md` says graph construction is beginning.
- 313 P4 units have provenance date `2026-07-08`, but the actual commits are dated 2026-07-07. The current project date is 2026-07-07. This is false provenance, even if caused by a mistaken session date.
- `STATE.md` claims 16 consent gates; only 11 unit notes begin `CONSENT GATE`. It also says 11 in an earlier session entry.
- `STATE.md` says the whole graph validates clean; the validator emits 17 warnings.
- The P4 coordinator records a 15/15 spot-check. That is about 4.8% of 313 units and does not meet Methodology §4's “≥10% per report” spot-check rule. No itemised check record is committed.

The repository cannot be the agent's memory while these surfaces disagree.

Create one generated status report from the store and manifests. Keep narrative decisions in `STATE.md`, but derive counts, verification distributions, warnings, CARE gates, and phase completion mechanically. Validate dates against commit/session time and reject future provenance. Persist spot-check sample IDs, criteria, results, and required per-report coverage.

### 11. CARE is a good start, not yet a consent process

The record-only and consent-gate choices are appropriately cautious. The remaining process is underspecified:

- Who can grant or advise on consent for each community/source?
- Is permission needed for quotation, paraphrase, commercial publication, graph publication, or all four?
- How are community protocols different from Western copyright handled?
- What happens if no representative authority exists?
- How can permission be withdrawn or scope-limited in a frozen edition?
- Are community reviewers compensated and credited?

Do not call the Indigenous gap closed until this is operational. Keep `research_coverage` and `publishable_coverage` separate, and default unresolved community material to non-publication rather than merely “low confidence”.

### 12. Empirical evidence needs a real review protocol

The empirical report is replication-aware, which is a strong start. It is still a selected set of individual findings mapped onto existing wisdom claims. That design invites “science confirms the ancients” cherry-picking even when caveats are present.

For every empirical bridge, require:

- a preregistered or at least predeclared question/estimand;
- a search date and search strategy;
- evidence hierarchy and inclusion criteria;
- directness to the actual wisdom claim;
- effect size and uncertainty;
- causal versus associational language template;
- population/context boundaries;
- contradictory and null evidence;
- living update status.

Do not let `SUPPORTED_BY` connect constructs merely because they are adjacent. The purpose-mortality → outward interest → helping others chain is the warning example. Encode construct distance and never display a low-directness bridge as “the studies add their vote”.

---

## P2 findings

### 13. Editioning, build reproducibility, and QA evidence are incomplete

`graph/editions/` is empty, yet SPEC §12 says a rendered book cites a frozen graph edition. The generator hard-codes `building-years-v0.1.0` and reads every YAML page-spec in the directory. Adding future pages would rebuild the same named edition with different content. The committed PDF is not accompanied by a manifest of graph object hashes, page-spec hashes, generator commit, renderer hash, or font hashes.

The dependency story is also incomplete:

- no requirements/lock file;
- fonts are fetched from the mutable `google/fonts` main branch;
- downloaded binaries/fonts have no checksum verification;
- WeasyPrint is version-pinned but the archive is not hash-pinned;
- no automated tests or CI are present.

The visual QA assertion is not independently auditable. The package says every page was viewed and lists defects fixed, but there is no committed QA manifest identifying render hash, page images, reviewer, result, and defect resolution. Screenshots need not bloat git; a small signed manifest and contact sheet in the publish package would suffice.

Add an edition configuration selecting page-specs explicitly. Freeze a manifest before render. Make the output embed edition/tag/commit identifiers. Hash dependencies. Record QA against the final PDF hash.

### 14. The visual language itself biases the answer

The mandatory palette assigns pink to “insight/warmth/the wiser path” and orange to “caution/decision/the harder road”. That is incompatible with genuine unresolved tensions. On the ambition spectrum, contentment sits at the pink end and striving at the orange end before evidence has decided anything. A reader receives a moral answer through colour while the prose says both poles are goods.

Use neutral, equal-status colours for unresolved poles. Reserve evaluative colour for claims where the project has explicitly adjudicated evidence and state what the colour means. Remove “aim here” defaults from forms unless the target position is itself a sourced, contested claim.

### 15. Governing-document drift needs correction

- Requirements and SPEC refer to a locked “Principle 16” on humour, but the canonical founding-principles file contains only 15 principles.
- SPEC §3/§5 describes Linux font paths and a pip WeasyPrint environment that STATE says does not work on the actual Windows machine.
- The operating manual prescribes `python3`; STATE says only `python` works here.
- Requirements says unverified starts `dubious`; Methodology and ingestion use `attested`.
- Architecture promises human coding agreement; current methodology does not.

These are not all equally serious, but governing documents cannot govern if contradictory. Add an explicit precedence map and update superseded sections rather than relying on readers to infer which sentence won.

---

## Specific P4 ingestion observations

P4 successfully minted all IDs `u-0034` through `u-0346`, and the manifest mapping is complete. Unknown source fields are usually preserved honestly. That is good raw-material work.

It should not yet be considered a passed S1 interpretive gate:

- 282 of 346 units are `attested`; 24 are `verified-primary`, 8 `verified-secondary`, 24 `communal`, 6 `dubious`, and 2 `apocryphal`.
- 313 new units are unclustered, as expected.
- 285 units have no source URL; 101 have no passage locator; 16 have no work; 2 have no author.
- 12 have no life stage.
- The required per-report ≥10% spot-check is not evidenced.
- Provenance dates for all 313 new units are wrong by one day.

Sample label concerns show why a larger independent audit is necessary:

- `u-0183` is typed `Virtue`, but its sourced expression is an injunction/principle; the virtue would be *shu*, not the sentence itself.
- `u-0205` says personhood is constituted relationally, yet is coded normative/prescriptive rather than metaphysical or observational. Its own note warns that Ubuntu's ontological claims are not empirical but does not resolve the normative/metaphysical distinction.
- `u-0215` uses `communal` for a precise modern Parker rendering. Communal provenance and textual verification are different axes and should not share one confidence field.
- `u-0260` is `universal-ish` while its note says “within tradition”; the current enum cannot represent scope.
- `u-0280` is typed as a `Dilemma` although the stored expression is one normative instruction to choose truth over the lie. A dilemma should model both poles and the standing question.
- `u-0305` extends an armed-conflict doctrine into `career` and `negotiation`. That editorial generalisation is not in the source and risks normalising deception outside warfare.

Do a stratified independent audit before S3: at least 10% **per report**, oversampling metaphysical/normative boundary cases, literary speech, communal material, realpolitik, modern translations, in-copyright text, and high-stage-relevance units. Preserve the full results.

## Recommended implementation sequence

### Gate A — repair the truth model

1. Declare P3 a design proof with content pending re-adjudication.
2. Reconcile governing documents and terminology.
3. Define schema v0.4: controlled entity IDs, structured verification/licensing, claim-type evidence dossiers, scope/applicability, editorial assertions, and presentation constraints.
4. Write migration and validators before migrating content.

**DoD:** cross-file validator, page-spec validator, quote linter, no future dates, no uncontrolled new vocabulary, and negative tests proving each rule fails correctly.

### Gate B — make one page genuinely graph-derived

Rebuild page 2 or page 7 with no substantive hard-coded copy beyond declared editorial framing. Produce a trace manifest and deliberately mutate source objects to prove the render responds.

**DoD:** every visible quote, source, evidence statement, independence mark, caveat, and trust label traces to an object and adjudication.

### Gate C — calibrate adjudication

Run a stratified external review over the P4 sample. Save full independent verdicts and final resolutions. Compute agreement/error categories separately for paraphrase, claim type, polarity, conditionality, stage applicability, and source context.

**DoD:** ≥10% per report, high-risk oversample, itemised record, explicit remediation threshold.

### Gate D — define the corpus claim

Label the existing 346 units as the discovery corpus. Define the validation frame and what recurrence/saturation statements are allowed. Normalise entities and source families.

**DoD:** a reader can tell exactly what population each count describes and what it does not describe.

### Gate E — re-adjudicate the walking skeleton

Correct the page-level issues above, add source notes/bibliography, and regenerate from a frozen mini-edition.

**DoD:** final PDF hash + edition manifest + page trace + QA manifest + external content review. Only then call the epistemic pipeline proven.

### Gate F — resume S2/P6

Prioritise verification by intended use and risk, not merely visual candidacy. Then perform real merging on a bounded pilot with reversible split/merge records before scaling to all 346 units.

## Questions the project must answer explicitly

1. Is this primarily a curated work of practical philosophy informed by a corpus, or an empirical map of recurrence in human wisdom? It can contain both, but the claims and methods must not blur them.
2. What would falsify a proposed convergence or fork? Current prompts are much better at finding examples than disconfirming the frame.
3. What does “truth” mean for normative and metaphysical claims? Attribution and robustness are not truth conditions.
4. What minimum independent scrutiny is required before a claim can influence book copy?
5. Which parts of the graph are intended to drive the website/game automatically? The current free-text model will not support that promise.
6. Is the life-stage spine a universal developmental model, a Western editorial itinerary, or a set of optional life tasks? Name it honestly.

## Bottom line to Claude

Do not respond by adding more caveat prose around the existing system. The core problem is enforcement. The project already knows the right principles; the code and schemas do not yet make violations difficult.

The correct next move is smaller and stricter: make one page genuinely traceable, make one claim profile genuinely defensible, make one adjudication genuinely independent, and make one recurrence statement genuinely bounded. Then scale.

Truth above all else requires the project to be willing to discover that its most elegant diagram is the wrong diagram.
