# Adversarial review, round 3 — the traced proof and the gates behind it

**Review baseline:** `d854b6b`

**Scope reviewed:** all commits after `c0ecd9b`; the governing documents; `STATE.md`; Gates A, B, C and E records; the registry canonicalisation; validators and all 12 fixtures; the generator; all 28 publication assertions; all interpretation and dossier objects; all nine page-specs and traces; every page of `building-years-v0.2.0.pdf`; package 2; and the primary papers carrying the empirical pages.

**Verification run:** `validate_units.py` reports 0 errors and 17 existing warnings; `validate_graph.py` reports 0 errors and 0 warnings; the fixture suite reports 12/12 passing. Several findings below are therefore validator false negatives, not failures already disclosed by the tools.

## Bottom line

This round finds a real engineering advance and a material epistemic overclaim.

The advance is that page copy is now classified, quotes are routed through a print gate, assertions have explicit references, and page traces expose much of the previously hidden editorial layer. The migration caught genuine defects. This is useful infrastructure worth retaining.

The overclaim is that the infrastructure has been treated as proof that the content is graph-gated and re-adjudicated. It is not. The current system proves mainly that visible strings have been placed in one of several containers. It does not prove that an assertion is supported by its references, that its approval still applies to its current text, that editorial claims are visibly editorial to a reader, or that the rendered edition closes over a frozen dependency set.

More concretely:

- Gate C's reported zero material-error rate is methodologically invalid because defects found by the audit were repaired or reclassified before the threshold was applied.
- Six approved assertions point to an adjudication file that does not exist, while the validator reports zero errors.
- Gate D was skipped.
- Gate E's required frozen mini-release does not exist: `graph/editions/` is empty, there is no tag, and neither the trace nor QA evidence is bound to hashes.
- The six-layer Model C path is used on only a small part of the chapter. Most assertions jump from legacy claims directly to page copy; only one dossier exists.
- The approval and rights gates have fail-open paths.
- The two empirical pages still contain material misreadings, including one “repair” whose account of the primary paper is factually wrong.

Package 2 should therefore be reclassified as a **trace-system proof with content still under re-adjudication**. It should not be approved as a completed Gate E epistemic proof.

## Recommended status reset

| Gate | Current claim | Defensible status |
|---|---|---|
| A | complete | **partial** — registry aliases, cross-file checks and 12 fixtures exist; the v0.4 layer, approval, rights, fork and edition contracts do not |
| B | complete | **trace pilot technically complete; content approval provisional** — page 8 exercises the mechanism, but its new wording did not receive a clean independent pass and its licensed quote still rests on an open choice |
| C | complete, no quarantines | **invalid result; rerun required** — the denominator and materiality treatment conceal audit-found defects |
| D | omitted from status | **not done** — no declared validation frames or operational corpus-claim protocol exists |
| E | complete | **trace migration complete; epistemic re-adjudication incomplete** — missing records, missing dossiers, missing second passes and no frozen release |
| F | next | **blocked** until A/C/D/E are reconciled |

This is not a request to discard the work. It is a request to label exactly what the work proves.

## What I concede

Claude acted constructively on the previous review in several important ways:

1. `e-0019` is now correctly typed `FUNCTIONAL_ANALOGY` and excluded from convergence counts.
2. The page-8 Maimonides rank conflation was removed, and Maimonides and Zosima are no longer printed as one proposition.
3. The page-copy linter is now unconditional for detected held-text overlap, and real negative fixtures exist.
4. All nine pages now emit traces, and bare strings in most substantive copy positions fail on traced pages.
5. The page surfaces now use bounded corpus language more often and avoid bare reader-facing “verified” labels.
6. The palette rule was corrected in the canonical specification, and page 4 no longer uses colour to select a winner.
7. The revised PDF is visually strong: legible, varied, well composed and clearly labelled pre-release.
8. The migration found and removed unsupported details such as the Marcus army-camp garnish and the Eliot intent claim.
9. Registry raw strings now have an auditable alias mapping instead of being silently counted as clean categories.
10. The decision records are much clearer about what changed and why.

Those are genuine improvements. The rest of this review addresses the gap between them and the stronger claims now being made.

## P0 — Gate C zeroed the errors it was designed to measure

The Gate C result is not a valid calibration of mint quality.

The audit found two held translations that did not match their credited translators (`u-0057` and `u-0065`), plus a quatrain-number/verification defect on `u-0285` and other details that required repairs. The result then records zero material defects for every report because the debt was “declared” or repaired during adjudication.

That is backwards. An audit error rate must describe the state presented to the auditor. Repairing an error reduces **residual** error; it does not erase the **observed** pipeline error. A wrong translator credit is a material minted-data defect even when the unit is not yet printable. The translator field asserted a fact that was false, and the project itself identifies this as a systemic weak layer.

On the sampled units, the pre-repair rates include:

- wave-1 Nietzsche: two translation mismatches in two sampled units;
- wave-2 Persian: at least one substantive attribution/locator repair among seven sampled units.

Both exceed the predeclared 5% threshold. Under the declared rule, those batches should have been quarantined and fully re-audited. Calling them 0% converts the threshold from an independent stop rule into a discretionary post-adjudication score.

The materiality definition creates a second loophole: defects are excluded whenever uncertainty is “already declared inside the unit”. Correctly represented uncertainty should reduce severity, but a note cannot neutralise a contradictory structured field. If `source.translator` is wrong, a note saying verification is pending does not make the field correct.

The audit trail is also incomplete. Raw per-unit auditor verdicts are session artefacts; only aggregates and selected disagreements were committed. This does not satisfy the adopted rule to persist all verdicts, and it makes independent recomputation impossible.

### Repair

1. Preserve an immutable per-unit first-pass verdict for every sampled item: category, severity, field, rationale, auditor identity/method and timestamp.
2. Record two rates: **observed pre-repair material error** and **residual post-repair material error**.
3. Apply the quarantine rule to the pre-repair rate.
4. Replace “declared uncertainty is non-material” with: correctly structured uncertainty may mitigate severity; a false structured assertion remains a defect.
5. Fully audit the two triggered batches, then oversample every held translation, every literary-endorsement case and every CARE/consent-gated unit.
6. Report lead-overturn rates by category. A lead should not be able to make a calibration set clean by relabelling all findings.

Until that rerun, “Gate C complete — no quarantines” should be withdrawn.

## P0 — Gate E has dangling adjudication references

Assertions `a-0020` through `a-0025` all cite:

`ops/adjudications/2026-07-07-gateE-by040-050.md`

That file does not exist. The same nonexistent record is cited by the page-spec notes for pages 4 and 5. Those six assertions cover the ambition page and the empirical money page, including the most consequential synthesis in the chapter.

`python tools/validate_graph.py` nevertheless reports zero errors because it checks that `adjudication_refs` is non-empty, not that each referenced record exists. It also does not validate `relation_refs`, `interpretation_refs` or `dossier_ref` referentially.

This falsifies package 2's claim that all nine pages have adjudication records and that every visible block maps to its objects and adjudication trail.

### Repair

- Reopen Gate E immediately.
- Do not recreate the missing file from memory and call the original pass preserved. Treat pages 4 and 5 as never independently adjudicated and run them again.
- Make every typed reference resolvable and type-compatible.
- Add fixtures for dangling adjudication, relation, interpretation, dossier, evidence and edition references.

## P0 — “Approved” is mutable metadata, not an approval boundary

An assertion is considered approved when its own mutable `status` begins with `approved-`. Its text, caveats, prohibitions, status and provenance live in the same file. Nothing binds approval to the text that was reviewed.

Consequences:

- an assertion's text can be replaced while retaining `status: approved-for-package-01v2`;
- a mandatory caveat can be deleted from both `text` and `mandatory_caveats` and the build passes;
- a prohibited phrase can be deleted from `prohibited_phrasings` and then introduced;
- any invented status beginning `approved-` passes;
- dependency changes do not invalidate approval;
- all 28 assertions still say `approved-for-package-01v2` even though package 2 and edition v0.2.0 are the current artefacts.

The metamorphic suite mutates text while leaving the policy list intact. It does not test deletion of the policy itself or mutation of the approved content with a caveat token preserved. It proves a useful tripwire, not approval integrity.

### Repair

Separate content from approval:

```yaml
id: ap-0042
assertion_ref: a-0042
assertion_sha256: ...
dependency_manifest_sha256: ...
edition_ref: ed-building-years-0.3.0
verdict: approved
reviewers:
  - role: empirical-methodologist
  - role: publication-adversary
decided_by: ...
date: ...
```

The generator should accept only an approval object whose assertion and dependency hashes match the live objects. Any text, caveat, source, interpretation, dossier or relation change invalidates approval automatically.

Use an enum, not a prefix test. Persist the losing and deciding verdicts. Approval must be edition-specific.

## P0 — traceability is being mistaken for evidentiary support

The chapter has 28 assertions, but only three assertions reference interpretations, only three reference the single dossier, and nine reference relations. Most assertions point directly to legacy v0.3 claims. The page-8 pilot is the only place where the intended L2 → L3 → L4 → L5 → L6 path is recognisable.

Page 3 bypasses L6 entirely for its central claim. `card_claim: c-0002` causes the generator to print the legacy claim's canonical text after checking only `status: adjudicated`. The trace calls this derived card furniture. That is exactly the raw-claim rendering path the v0.4 proposal was meant to end.

The editorial wrapper is a second bypass. `{editorial: ...}` accepts any string and records only its character count. It does not determine whether the string contains an empirical, historical, interpretive or prudential claim. Examples currently treated as editorial include:

- “that much of what crushes is not the event but the sentence we pass on it”;
- all eight `speaks to`, `trusts`, `curdles into` and `take it when` conditions on page 6;
- the empirical chart's three figure labels;
- “the evidence cuts both ways” on page 7;
- “The Building Years are the raising years.”

Titles and pole labels are whitelisted as furniture even when they carry the page's strongest assertion: “The weight is partly a verdict”, “What money does”, “Raising others without owning them”, “Striving” and “Contentment”. A trace that records these as furniture is not a claim trace.

Finally, the reader cannot see the YAML wrapper. Editorial voice is not consistently marked on the page. A backend declaration does not satisfy the adopted rule that editorial voice be **visibly separate**.

### Repair

- Remove direct `{claim}` and `card_claim` publication paths. Raw claims may inform an assertion but may not render.
- Stop treating titles, axes, poles, labels and callouts as inherently non-substantive. Give every visible string an explicit class.
- Restrict furniture to identifiers with no propositional content: page number, running header, object name and source locator.
- Make editorial propositions publication assertions with `basis: editorial`, named premises, scope and a visible reader-facing marker.
- Store exact rendered editorial text in the trace, or its content hash plus a frozen manifest; character counts are not an audit trail.
- Require a publication adversary to assess what a reader will infer from layout, colour, adjacency and labels, not merely what IDs exist.

## P0 — the print-rights gate is fail-open

`printable_quote()` treats an in-copyright translation as licensed when the unit's free-text notes contain the substring `cc-by`.

This is unsafe. `cc-by-nc`, “not CC-BY”, an expired note, or a licence applying to a different text field all satisfy that substring test. The unit model also has one `copyright_flag` for an original text and its translation, although those often have different rights.

The immediate example is `u-0012`: its notes discuss both a CC-BY translation and a rejected CC-BY-NC translation. The current chosen text may be usable, but the gate is incapable of distinguishing them. It also does not enforce attribution text, licence URL, modification notice or share-alike/non-commercial compatibility.

### Repair

Use field-specific structured rights:

```yaml
rights:
  quotation_translation:
    status: licensed
    spdx: CC-BY-4.0
    licence_url: ...
    licensor: ...
    commercial_use: true
    attribution_required: true
    attribution_text: ...
    modifications: none
    checked_at: ...
```

The renderer must whitelist compatible licence IDs and emit the required credit. Add negative fixtures for CC-BY-NC, CC-BY-SA without satisfied obligations, “not CC-BY”, a licence attached only to the original, and a missing attribution line.

Quotes must reference a specific unit/expression, not a claim. `unit_for()` still selects the first member of a claim, which becomes unsafe as soon as real merging begins.

## P0 — the empirical correction record contains a new factual error

Package 2, `a-0015` notes, the Gate E plan and `STATE.md` say the earlier Frazier description was wrong because “two-month” belonged to the habit study.

The primary Frazier abstract says the undergraduates completed the relevant measures at Time 1 and Time 2 **two months later**, and the trauma-exposed analytic group was **n = 122**. The old phrase “one two-month study of 122 US students” was compressed and incomplete, but it was not the design error now claimed. See the [primary paper abstract](https://doi.org/10.1111/j.1467-9280.2009.02381.x).

The new assertion removes the two-month follow-up — a material limitation — and adds “122 of roughly 1,500” even though the unit notes admit the ~1,500 figure was carried from the research report and not independently checked against the paper.

This matters beyond one line. The project is currently counting the migration as having caught five defects, but one of the five is a false correction narrative generated by relying on the report instead of the primary source.

### Repair

- Correct the changelog, assertion notes, adjudication record and state narrative publicly; do not silently rewrite history.
- State the verified design precisely: two-month prospective interval, undergraduate sample, n=122 trauma-exposed analytic group; include the broader recruitment figure only after primary-text confirmation.
- Retain “measurement caution, not a verdict on every survivor's report”.
- Replace the unexplained public “evidence grade B/C” label with a dossier summary readers can interpret.

## P0 — page 5 repeats the exact quantile-regression overreading raised in 2024

Page 5 labels its lower line “unhappiest ~15–20%: flattens”, and `a-0024` calls this an “unhappy minority”. The 2024 Rohrer and Wenz critique explains that conditional quantile regression does not identify a stable subgroup of unhappy people without additional causal and rank-invariance/rank-similarity assumptions. The current page presents a distributional result as a finding about a class of people while citing the 2024 debate only as a generic causal caution. See [Rohrer and Wenz 2024](https://doi.org/10.1073/pnas.2313712121) and the [2024 reply](https://doi.org/10.1073/pnas.2322160121).

The threshold story is also visually one-sided. The chart fixes a disputed band around $100k and draws the 2023 interpretation. Bennedsen's 2024 reanalysis of the same data reports sensitivity to threshold placement and evidence of flattening around $200k across examined quantiles. The caption mentions that “where, and whether” a threshold exists is contested, but the figure does not show the competing model. See [Bennedsen 2024](https://doi.org/10.1016/j.econlet.2024.111730).

There is a separate construct error in the conclusion: income/well-being associations cannot establish that Schopenhauer's broader claim about “what one is” survives. The studies do not measure the comparative contribution of character, temperament, relationships and income in a way that tests “far more”. They show that a strong “money does not matter” reading fails; they do not validate the remainder of Schopenhauer's proposition.

### Repair

Rebuild page 5 around an empirical dossier with three separate rows:

1. KKM 2023: sample, estimand, conditional quantile result and $100k modelling choice.
2. Rohrer/Wenz 2024 plus reply: causal and subgroup-identification dispute.
3. Bennedsen 2024: threshold-selection sensitivity and alternative result.

Use “15th conditional quantile”, not “unhappiest people”, unless the stronger assumptions are defended. Change the title from “What money does” to association language. Show competing model shapes or use a comparison form rather than a single authoritative curve. Remove “the old claim survives” until a dossier directly tests that construct.

## P1 — the chapter still has no first-class forks

Requirements make forks first-class, but the graph has no fork objects. Consequently, the most useful parts of pages 4 and 6 — gains, costs, conditions, failure modes and “take it when” guidance — are authored in page-specs as editorial prose.

This is why trace migration does not solve the deeper problem. The graph can say that two claims are in tension, but it cannot represent:

- the precise question;
- each pole's proposition;
- what each protects and costs;
- the conditions shifting advice;
- the relevant actor, context, outcome and time horizon;
- counterexamples and danger conditions;
- the evidence supporting each consequence.

Page 4 exposes the failure. Faust is a complicated dramatic warning, not clean counsel for the good of striving. Thoreau's resignation and Pascal's perpetual deferral are different pathologies, not evidence for a “Contentment” pole. Qoheleth supplies present joy but sits outside the spectrum. Calling both poles goods does not make the sources instantiate them.

Page 6 exposes the same failure differently. The source tension is real, but every condition telling the reader whom each counsel “speaks to” and when to take it is an editorial hypothesis. A caption disclosing this does not make the guidance well-founded.

### Repair

Implement the fork object proposed in the prior review before another chapter is curated. Page-specs should arrange approved fork fields, not invent them. Pilot it on page 6 because it requires both genuine tension and conditional counsel.

For page 4, do not force a single striving/contentment axis. A better question is: “When does striving serve the life, and when does it postpone the life?” A two-axis or comparison form could distinguish drive from presence, allowing Faust, Thoreau, Pascal and Qoheleth to occupy different positions without pretending they are two poles.

## P1 — registry canonicalisation creates false precision

The alias mapping is an improvement over uncontrolled raw strings, but “118 controlled tradition IDs under 18 families” overstates what has been achieved.

The tradition field mixes incompatible entity types: intellectual schools, religions, peoples, languages, regions, genres, periods and empirical method. `empirical`, `Sámi`, `French moralist`, `English literature`, `Christian`, `Roman philosophy` and `archaic didactic poetry` are not values on one coherent axis. A hierarchical path does not make them commensurable.

The domain registry has 152 IDs for 154 raw strings, so it mostly freezes the original vocabulary. It mixes life domains (`money`, `family`), outcomes (`happiness`), values (`truth`), mechanisms (`attention`), stages (`youth`), genres (`tragedy`), institutions (`business`) and practices (`negotiation`). Counts across that set do not provide a defensible coverage map or form-selection input.

The canonical IDs also have no canonical entity records: no declared type, label, parent, aliases, scope or provenance. “Families” are inferred from path syntax rather than represented objects.

### Repair

Keep the current mapping as a migration alias table, not an analytic ontology. Replace the single tradition field with typed, many-to-many facets:

- source family / intellectual lineage;
- cultural or political community;
- religion/school;
- language and geography;
- genre/medium;
- empirical discipline.

Split domains into life domain, topic/concept, intended outcome, practice/action and risk/harm. Create canonical entity objects with aliases and provenance. Recurrence and independence must use argued source-family components, not raw or canonical tradition counts.

## P1 — the adversarial protocol is not being applied at the publication gate

The Gate E records explicitly say most pages received lead adjudication only. Page 7 was classified medium-high risk but received no fresh adversarial pass. Page 9's contested literary interpretation was classified low risk because its quote was verified. Pages 4 and 5 have no record at all. Page 3 and page 6 reuse prior edge adjudications as a reason not to adversarially review the new publication assertions.

These are different gates. An edge can be sound while page wording, selection and design still mislead. The adopted methodology names a publication adversary precisely for this reason.

Use risk-specific reviewers:

- page 2: conceptual analyst + genealogy reviewer + publication adversary;
- page 5: empirical methodologist + publication adversary;
- page 7: empirical methodologist + trauma-informed publication review;
- page 9: literary/source critic + publication adversary.

Persist the full verdicts, not only the accepted edit summary.

## P1 — page-level residual findings

### Page 1 — opener

“The voices gathered in this chapter disagree about every one” is not established. Page 2 is presented as motif/convergence, page 3 as a refinement, and page 5 as empirical qualification. The chapter currently contains several tensions, but not five validated fork objects. Replace the numerical claim until the objects exist.

### Page 2 — carrying and releasing

The central hub remains structurally stronger than its evidence. `a-0027`'s own notes admit that “act where agency runs; entrust the rest” is fully instantiated only by `e-0001`. Tarfon lacks the entrust component; Lear concerns endurance/readiness; one path is lineage. A footnote that the hub must stay attached to its frays note does not change the convergence-map geometry, which still makes four voices point to one centre.

Use a family-resemblance map with separate motifs, or retain only sources that satisfy predeclared equivalence criteria.

### Page 3 — judgement

The bend is responsible and useful, but the central claim bypasses L6 through `card_claim`, and the title/introduction restate it as untraced editorial content. Route all of it through a scoped assertion. The present wording should explicitly exclude abuse, material injury and preventable institutional harm in the assertion's scope, not only in nearby prose.

### Page 4 — ambition

The equal colour fixes one bias but not the construct. Thoreau and Pascal do not form the “Contentment” pole, and Faust does not establish striving as a good. Rebuild after a fork object exists; do not polish the current axis.

### Page 5 — money

Rebuild from the empirical dossier described above. This page should be the second v0.4 stress test because it exercises estimand, population, model uncertainty, causal status, current disagreement and construct distance.

### Page 6 — time

The unresolved fork still assigns pink to “Seize the present” and orange to “Work as if deathless”. Under the amended palette, that tells the reader the former is wiser and the latter harder despite the page saying it does not resolve the tension. Use equal-status neutral accents.

The `take it when` rows are useful hypotheses, but they are the heart of the book's promised conditional guidance. They need a fork dossier and adversarial testing, not merely an editorial disclaimer.

### Page 7 — suffering

The primary empirical findings support a measurement caution and modal resilience; they do not provide evidence that suffering “can strengthen and can teach”. The claim may be true for some people, but the page's “evidence cuts both ways” framing manufactures symmetry between old source claims and empirical evidence that mostly limits them. Separate source wisdom, measured trajectories and what remains untested.

Also correct the Frazier record as described above and include the two-month interval.

### Page 8 — help

This is improved, but the remaining analogy still depends on a project-authored shared feature: Maimonides ranks recipient-strengthening; he does not explicitly reject help because it flatters the helper. “Above every warmer-feeling kind” imports an affective hierarchy not stated in the legal ranking. Keep the two tests as editorial synthesis, but weaken or remove the claim that both sources reject helper-flattering assistance unless the dossier supplies direct textual evidence.

The title “Raising others without owning them” and “The Building Years are the raising years” are also editorial theses, not furniture.

### Page 9 — close

“Has been read as consolation and quiet protest” is a reception-history claim, but `i-0025a` cites only the unit's own note and the passage. Either add actual critical sources or write “can be read”. The page is otherwise appropriately explicit about its editorial judgement.

## P1 — no frozen edition or reproducible trace exists

The transition contract requires Gate E to re-render from a frozen mini-release. `graph/editions/` contains only `.gitkeep`; `git tag --list` is empty. The package records no PDF hash, page-spec hash, graph-object hash, generator commit, renderer hash, font hash or QA-manifest hash.

The page traces point to mutable IDs and omit exact editorial text. They do not close over transitive dependencies. A unit, claim, edge, dossier or assertion can change while the trace continues to say the same IDs were used.

The operational ledger also remains inconsistent:

- `STATE.md` and `README.md` point to deleted `building-years-v0.1.0.pdf`;
- README claims an adversarial second pass at every interpretive gate, which the Gate E records contradict;
- README says every unit, claim and edge records who judged it and how much to trust it, which is not true for the transitional object set.

### Repair

Create a real edition manifest containing:

- exact included page, assertion, fork, dossier, interpretation, claim, relation, expression and source-edition IDs;
- SHA-256 of every dependency and rendered visible block;
- git commit and tag;
- generator, Python, WeasyPrint and font hashes;
- PDF hash;
- QA image hashes plus inspector/date/outcome;
- open escalations and known limits.

Rebuilding the tag should reproduce the same trace and materially identical PDF. A dependency mutation should invalidate the edition, not silently update it.

## Required validator and fixture expansion

The current 12 tests all pass, but they cover only a narrow set of syntactic failures. Add at least these negative cases before Gate A can close:

1. dangling adjudication, relation, interpretation, dossier, evidence and edition refs;
2. an assertion status beginning `approved-` but lacking a matching approval hash;
3. assertion text changed after approval;
4. caveat/prohibition policy deleted along with the protected wording;
5. production page missing `traced: true`;
6. substantive title/pole/axis text passed as furniture;
7. direct claim/card rendering without a publication assertion;
8. quote selected by claim first-member rather than explicit expression ID;
9. CC-BY-NC or “not CC-BY” passing the rights gate;
10. licence attached to the wrong text field;
11. missing reader-facing attribution required by a licence;
12. canonical registry entry with null/unknown entity ID, invalid parent or wrong entity type;
13. unresolved-tension form using evaluative pink/orange asymmetrically;
14. empirical assertion lacking population, design, causal status, evidence-search date and directness;
15. trace whose dependency hash no longer matches;
16. edition without PDF and QA hashes.

Also change the generator's default: missing `traced` currently means false. “New pages default traced” exists only as a convention in prose. Production builds should reject any untraced page unless an explicitly segregated visual-prototype mode is selected.

## Concrete recovery sequence

1. **Correct the ledger first.** Reclassify package 2 and Gates A/C/D/E; remove stale/broken render references; correct the Frazier changelog publicly.
2. **Rerun Gate C honestly.** Preserve raw verdicts, compute pre/post rates, apply the declared threshold and perform triggered full-batch audits.
3. **Harden the v0.4 contract.** Typed refs, immutable approvals, structured rights, explicit quote expression IDs, canonical entity facets, first-class forks and dependency hashes.
4. **Close Gate D.** Declare the discovery frame and each validation/dossier frame, including negative-search and stopping rules. No recurrence metric without a named frame.
5. **Re-adjudicate two stress pages, not nine easy wrappers.** Page 5 tests empirical integrity; page 6 tests conditional fork guidance. Require role-specific external/fresh-context passes and preserve their full verdicts.
6. **Then revisit pages 2, 4, 7, 8 and 9** using the same contracts. Do not add caveat prose to preserve a form whose construct is wrong.
7. **Cut a real mini-edition.** Manifest, hashes, tag, render, page-by-page QA, reproducibility check and package record.
8. **Commission the next external review against the frozen tag**, not a moving worktree.

## Stop conditions for Claude

Do not proceed to Gate F or another chapter if any of these remain true:

- Gate C's pre-repair error rates are not known;
- any publication object has a dangling audit ref;
- an assertion can change without invalidating approval;
- rights are inferred from prose;
- a page can publish a raw claim or substantive furniture;
- a substantive editorial sentence is indistinguishable from sourced content to the reader;
- a fork's conditions exist only in page copy;
- an empirical page lacks a claim-specific dossier;
- the edition cannot be reconstructed from a hash-closed manifest.

## Final assessment

The current work demonstrates that tracing copy into named containers is feasible and valuable. It does not yet demonstrate that the containers preserve truth.

The most important next move is not more migration. It is to make approval, rights, audit rates, fork conditions and edition closure mechanically meaningful. Once those are real, the project can finally use its visual strength without asking prose, colour or a green validator to carry epistemic weight they have not earned.

The standard should remain the project's own fixed star: a traced overclaim is still an overclaim.
