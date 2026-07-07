# Publish package #2 — The Building Years, traced proof v0.2.0

> **RECLASSIFIED 2026-07-07 (external review round 3, adjudication accepted):** this is a
> **trace-system proof with content still under re-adjudication**, NOT a completed Gate E
> epistemic proof. Do not read the claims below as "content verified." Round 3 confirmed a
> dangling adjudication file behind pages 4–5, a fail-open rights gate, a false Frazier
> correction (below, item 3 — now retracted), and that most pages received lead-only review.
> Gate C and Gate E statuses are reset in STATE.md. This package is on hold pending the
> recovery sequence in `ops/adjudications/2026-07-07-external-review-round-3-response.md`.

**Proposed:** 2026-07-07 · **Deliverable:** `book/renders/building-years-v0.2.0.pdf` (9 pages, all viewed) + `book/page-traces/` (9 trace manifests)

## What this is
The same proof chapter as package #1, rebuilt so that **every claim-bearing sentence on
every page resolves from the graph or is declared editorial** — nothing in between. 28
publication assertions (a-0001..a-0028) now carry the pages' source-summaries,
relation-summaries, interpretive claims and syntheses, each with mandatory caveats and
prohibited phrasings enforced at build time. Machine-looking labels (the node-card
kicker, claim label and trust pill) are derived from the store and cannot drift from it.
6/6 metamorphic proofs (`ops/audits/2026-07-07-gateE-metamorphic.md`): the build refuses
a revoked assertion, a stripped caveat, a prohibited phrasing, an unverified quote, or
an untraced bare string — on any page, not just the pilot.

## What re-adjudication caught (the honest changelog)
Migrating the eight v0.3 pages surfaced **four** genuine defects (originally reported as
five — item 3 below was a self-inflicted regression, not a catch), repaired in the store:
1. **by-090:** "She meant it as consolation" — authorial-intent claim beyond the
   evidence → re-grounded in the documented double reading (a-0007 + i-0025a).
2. **by-030:** "writing to himself *in an army camp*" — factual garnish with no store
   basis → removed.
3. ~~**by-070:** Frazier study design misstated~~ **RETRACTED — this was NOT a defect in
   the v0.3 copy; my "repair" introduced one.** The v0.3 line ("one two-month study of 122
   US students") was compressed but correct: the Frazier 2009 abstract confirms a two-month
   interval and n=122 trauma-exposed analytic group. My revised a-0015 wrongly dropped the
   two-month interval and added an unverified "~1,500". Now corrected to the primary-checked
   design (round-3 P0-6). Galatzer-Levy's co-authors were still genuinely restored in a-0016.
4. **by-050:** the 2024 reanalysis was credited with the causal critique; it contests
   the threshold — the causal caution comes from the observational design → both
   cautions kept, correctly attributed (a-0024). *(Round 3 P0-7 shows this page needs a
   deeper rebuild — quantile≠subgroup, one-sided chart, construct overreach; queued.)*
5. **by-020:** the convergence page passed a mandatory fresh-context adversarial pass,
   which tightened "openly inheriting"→"likely inheriting", "keep arriving"→"arrive",
   "graded inconsistently"→"chain grading is contested" (verdicts verbatim in
   `ops/adjudications/2026-07-07-gateE-by020.md`). Also dropped as ungrounded: the
   Qoheleth "because nothing lasts, not despite it" flourish (by-040).

## Provenance / coverage summary
- 9/9 pages `traced: true`; 9 trace manifests map every visible block to its objects
  and adjudication records (`ops/adjudications/2026-07-07-gateE-*.md`, one per page/pair).
- Verbatim quotes: 8, all verified-primary + public-domain (or CC-BY: Meszler), each
  trace carrying the checked_against evidence.
- Assertions: 28 approved; interpretations: 3; dossiers: 1; every relation rendered on a
  page rests on an adjudicated edge (the two argued convergences remain graded
  moderate/partial; the two lineages remain lineage).

## Known limits
- This is still a **proof of the production system**, not a book chapter release:
  Model C confirmation (E-0003) and the Maimonides translation choice (E-0002) are open
  with Jason; corpus coverage behind these five forks is skeleton-scale (33 claims).
- The metamorphic run is scripted-and-captured, not yet a persistent CI suite.
- Editorial voice is marked in traces and by register on the page, but a reader-facing
  editorial-marker convention (SPEC-level) still needs a design pass at Gate F/next render.

## Escalation queue attached
E-0003 (Model C confirmation — decides when "proof" can become "release candidate");
E-0002 (Maimonides translation). Nothing new added by this package.
