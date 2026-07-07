# A Map for Mortals — Methodology & Data-Science Spec

> **TRANSITION NOTICE (2026-07-07):** a v0.4 methodology reset was adopted after external adversarial review — `docs/methodology-v0.4-transition.md` **binds where it conflicts with this document** (pending Jason's E-0003 confirmation, after which this document is revised in full). Key changes: Model C research identity; corpus-bounded language; robustness profiles superseded by claim-type dossiers; `publish-ready` suspended; publication-driven (not corpus-wide) verification.

**Version:** 0.3 · **Status:** production · **Implements** the Wave-1 methodology report (`corpus/reports/wave-1/01-methodology.md`), adapted for autonomous execution in the Claude Code harness.

> **The governing principle of v0.3 — harness-native by default.** The *epistemics* are non-negotiable: provenance on everything, adjudicated judgments, disaggregated robustness, independence as argued evidence. The *tools* are replaceable. Always prefer the simplest tool that preserves the epistemics in this environment; the research-grade stack (§6) is an optional upgrade, never a blocker. An instruction that can't run here has a documented fallback — stalling and simulating are both forbidden.

---

## 1 · The store

- **Canonical store = YAML files in git.** `graph/units/u-####.yaml`, `graph/claims/c-####.yaml`, `graph/edges/e-####.yaml`. Git history is the versioning; everything diff-able and auditable. The example files in `graph/` are **normative for format**.
- **Two levels, never conflated:** a **unit** is one sourced expression (a quote/passage with its source); a **claim** is the canonical, merged idea that units express. Units are minted at ingestion; claims are minted at clustering; `unit.claim_id` links them.
- **Graph queries via NetworkX** (pure pip): a small loader in `tools/` builds the graph from YAML on demand. **Neo4j is optional** (§6) — a projection, never the canonical store.
- **Editions:** a book cites a frozen graph. Cut editions as git tags + a manifest in `graph/editions/` listing included claim/unit IDs and their verification states.
- **Provenance (PROV-shaped, lightweight):** every unit/claim/edge carries `prov` (source report or source text, extracting agent+pass, date) and every edge `origin` (`inferred` | `curated` | `inferred-then-curated`), `confidence`, `method`.

## 2 · Verification — the truth budget

Deep-research reports are **claims about sources, not verified data**. Every quotation enters as unverified and climbs:

| Tier | Meaning |
|---|---|
| `verified-primary` | wording confirmed against a primary/public-domain edition (Perseus, Gutenberg, SuttaCentral, ctext.org, sacred-texts…), with URL + date + matched text recorded in `verification` |
| `verified-secondary` | attribution confirmed by a reliable authority (SEP, Quote Investigator, scholarly edition) but wording not yet checked against the primary text |
| `attested` | asserted by a report; plausible; unchecked |
| `dubious` / `apocryphal` | flagged or known-false attribution |
| `communal` | proverbs/folk units — attributed to a people/language, not a person |

**The print gate (hard):** verbatim quotes in the book require `verified-primary` **and** `copyright_flag: public-domain` (or explicit licence). Otherwise: paraphrase with honest framing ("a saying attributed to…"), or omit.
**The budget (what keeps this finite):** verification effort follows publish priority — book-candidate units get full primary verification; the long tail may remain `attested` in the graph, honestly labelled. Website/game inherit the same labels visibly.

## 3 · Schema (canonical)

**Unit** (`graph/units/`): `id`, `claim_id` (null until clustered), `type` [Insight|Dilemma|Virtue|Danger|Practice|Consequence], `paraphrase` (neutral one line; a normative act — adjudicated), `quotation` (original language, if held), `quotation_translation`, `source` {author, work, passage, translator, edition_year, language, url, urn}, `tradition`, `era`, `register`, `claim_type` (**mandatory**), `polarity`, `conditionality`, `life_domains[]`, `life_stages[]`, `endorsement` (literary: endorsed|complicated|undercut|ambiguous|n/a), `attribution_confidence` (tiers above), `verification` {status, method, checked_against, date}, `copyright_flag`, `prov`, `notes`.

**Claim** (`graph/claims/`): `id`, `canonical_claim`, `claim_type`, `polarity`, `conditionality`, `member_units[]`, `robustness_profile` (below), `status` [candidate|adjudicated|publish-ready], `prov`, `notes`.

**Edge** (`graph/edges/`): `id`, `type`, `from`, `to`, `origin`, `confidence`, `method`, `prov`, `notes`; `independence_basis` (graded: strong|partial|weak|none + one-line evidence) on `CONVERGES_WITH`. Types: EXPRESSED_BY, FROM_WORK, IN_TRADITION, INFLUENCED, CONVERGES_WITH, REFINES, QUALIFIES, **CONTRADICTS** (logical) split from **IN_TENSION_WITH** (prudential/conditional — the book's actual subject), **FUNCTIONAL_ANALOGY** *(added 2026-07-07: similar action/function without proposition-level equivalence — never counted as convergence)*, ADDRESSES, CULTIVATES, GUARDS_AGAINST, LEADS_TO, APPLIES_IN, SUPPORTED_BY, UNDERMINED_BY.

**Robustness profile** — a disaggregated vector; **never one score**. Eight dimensions, each `{rating: high|moderate|low|very-low, certainty, basis}`: (1) recurrence, independence-weighted; (2) source diversity; (3) temporal spread; (4) claim type; (5) empirical support (GRADE-style); (6) contestation; (7) attribution integrity; (8) survives-scrutiny. Orderings only as **partial order** (dominance on every dimension); incomparables stay incomparable; note sensitivity of any ordering to defensible re-weightings.

## 4 · The pipeline (stages, gates, targets)

Targets are **tunable defaults** — a landing zone, not dogma. Adjust via `ops/DECISIONS.md`.

- **S1 · Ingestion & normalisation.** Parse reports; mint units; re-derive labels rather than trusting a report's labels blindly (spot-check ≥10% per report against the report's own quoted evidence); everything enters `attested` at best. *Gate:* all landed reports ingested; validator clean. *Target:* 1,500–3,000 units, ≥25 traditions across all waves.
- **S2 · Verification (rolling).** Climb the tiers per §2, prioritised by publish-candidacy. *Gate at ship:* 100% of book verbatim quotes `verified-primary` + public-domain.
- **S3 · Clustering → claims.** At this corpus scale Claude adjudication is the **primary** method: group units by candidate shared claim (within domains, then across), adversarially second-passed. Cross-check, where the environment allows, with small CPU embeddings (`sentence-transformers`, e.g. bge-small/all-MiniLM; record model+version) + cosine near-duplicate mining; disagreement between methods → escalate or keep split (splitting is reversible; bad merges poison). *Gate:* every unit has `claim_id` or a recorded singleton status. *Target:* 400–800 claims.
- **S4 · Edges.** Candidates from: report §E sections, within-cluster adjacency, high-similarity cross-cluster pairs, and directed Claude passes per dilemma. Adjudicate type (esp. CONTRADICTS vs IN_TENSION_WITH). **Independence:** a judgment, never a computation — build `graph/intellectual-history.md` (known transmission: who read whom, translation events, chronology) and grade `independence_basis` against it; positive transmission evidence → INFLUENCED edges. NLI models optional (§6), candidate-generation only. *Gate:* all semantic edges adjudicated with origin/confidence; major convergences have argued independence.
- **S5 · Robustness profiles** per §3 for every claim headed to the book. *Gate:* no publish-ready claim without a complete, honest profile.
- **S6 · Curation → page-specs.** Select and order along the life-phase spine (SPEC §8); choose diagram forms per the form-selection logic (SPEC §7); write `book/page-specs/` (SPEC §12). Curation edits page-specs, not generator code. *Target:* 8 stage chapters, 6–10 forks each, ~150–250 pages, backed by 250–450 publishable units.
- **S7 · Render & QA.** Generator (evolved from the archived prototype) renders page-specs → PDF; **mandatory** per-page raster inspection; fix; re-render. *Gate:* every page viewed; SPEC composition rules hold.

**Walking skeleton first (de-risk):** before scaling S1–S7 corpus-wide, run **one life-stage chapter end-to-end** (~30 units → verify → claims → edges → profiles → page-specs → rendered chapter) and deliver it as the first publish package. Proves the whole pipeline while everything is still cheap to change.

## 5 · Corpus waves (unchanged in spirit)

Waves of deep research (Jason, in Claude chat) → land in `corpus/reports/wave-N/` → synthesis updates `corpus/COVERAGE-INDEX.md` (coverage map incl. life-stage × domain, gap register, merge candidates, backlog, wave metrics) → next wave's prompts prepared with do-not-duplicate lists (`prompts/deep-research/`). **Saturation heuristic:** a wave adding <20% new canonical claims signals approaching saturation; Claude proposes, Jason decides. Wave-2 gap prompts (African, Indigenous, Persian, practical/strategic, women's voices, world proverbs) are ready to run.

## 6 · Optional upgrades (adopt only when earned)

Adopt when the default hits a real limit, and record the decision: **Neo4j** (if NetworkX queries become unwieldy at scale), **larger embedding models / seeded UMAP + HDBSCAN** (if small-model clustering visibly underfits), **NLI models (DeBERTa-MNLI)** as extra edge-candidate generation (candidate-only, blocked by similarity to avoid O(n²)), **text-reuse tooling** (Passim/Tesserae — only if installable; the intellectual-history layer is the primary transmission method regardless). Never let an optional tool block a gate.

## 7 · Adjudication & anti-bias

The full protocol lives in `CLAUDE.md §4` (steer → adversarial second pass with the cross-model fallback ladder → external gold standards → confidence + escalation → skew monitoring). Task bias checklists: **paraphrase** (strip your slant; preserve conditionality; don't smooth hard claims; don't Westernise; keep claim type honest) · **clustering** (word-overlap ≠ agreement; translation divergence ≠ disagreement; when unsure, keep split) · **independence** (absence of evidence of transmission ≠ evidence of absence; grade honestly) · **robustness** (corpus frequency ≠ global frequency; digitisation bias inflates recurrence) · **curation** (the map must reflect the corpus, not the curator; disclose the editorial hand in the book itself).

## 8 · Ship gate (book v1)

Ship when **all** hold: corpus saturated (§5) · every printed claim publish-ready (verified attribution, mandatory claim_type, full robustness profile, provenance) · **print gate 100%** (§2) · escalation queue worked to Jason's sign-off (target <30 open at any package) · corpus-composition caveat written honestly into the book · a frozen edition tagged. Then render. Website and game follow as projections of the same graph. **Depth serves the book; the book does not wait on infinite depth.**

## 9 · Open questions (carried honestly)

Independence is arguable, never provable · corpus skew is structural even with effort · paraphrase is itself a normative act · edition/release discipline across three products · curation vs systematicity — disclosed to readers in the book.

*The one fixed star: **truth above all else.***
