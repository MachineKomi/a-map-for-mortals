# Production Runbook — *A Map for Mortals*

One runbook, corpus to shipped book. **Claude Code executes autonomously**; Jason runs deep-research queries and reviews publish packages. Every phase: do the work in batches → validate → commit → **update `STATE.md`**. Supersedes the old CORPUS-BUILD-RUNBOOK.

> **The whole flow:** P0 env → P1 land reports → P2 synthesise → **P3 walking skeleton (first publish package)** → P4 scale ingestion+verification → P5 wave loop until saturation → P6 graph completion → P7 curation → P8 render → P9 ship gate.

---

## P0 · Environment & repo check *(first session)*
1. Read `CLAUDE.md`, `STATE.md`, the three governing docs.
2. Probe capabilities and **record results in `STATE.md`**: `python3 -V`; `pip install pyyaml --break-system-packages`; can `weasyprint` install and render a one-page test PDF; is `pdftoppm` present; can `sentence-transformers` install (optional — note if not, S3 falls back to Claude-judgment clustering per METHODOLOGY §4); is any external-model CLI configured (for the adversarial ladder).
3. `git init` if needed; confirm `.gitignore`; first commit.
4. Flag open items to Jason in `ops/ESCALATIONS.md` (licence is already queued there).
**DoD:** capabilities recorded; validator runs clean on the example graph files; committed.

## P1 · Land & validate reports
1. Jason drops reports into `corpus/reports/wave-1/` (`NN-tradition-shortname.md`).
2. For each report: check the expected shape (source inventory, unit blocks, dilemmas, convergences, misattribution list, leads); log gaps in `COVERAGE-INDEX.md` — never fabricate missing sections. Note report count may differ from the nominal 8; tolerate whatever landed.
**DoD:** every present report validated & logged. Commit: `corpus: land wave-1 reports`.

## P2 · Synthesise → coverage index
Reading **all** reports (report-by-report; use scripts for aggregates — context discipline):
1. Coverage map (tradition × depth; life-stage × domain — the book's spine needs every stage fed).
2. Gap register (P1–P3 priorities; the Western/literate skew is a named commitment).
3. First-pass canonical-claim merge candidates across reports (candidates, not verdicts).
4. Contradiction/tension candidates.
5. Ranked, de-duplicated backlog for the next wave, each item with its do-not-duplicate note.
6. Wave metrics (new claims / dilemmas / traditions) for the saturation trend.
**DoD:** `corpus/COVERAGE-INDEX.md` rebuilt from real data. Commit: `index: synthesise wave-1`.

## P3 · Walking skeleton *(the de-risk phase — do not skip)*
Run **one life-stage chapter end-to-end** before scaling anything:
1. Pick a stage with rich Wave-1 coverage (likely The Building or Threshold Years).
2. ~30 units: ingest (S1) → verify book-candidates to `verified-primary` (S2) → cluster to claims (S3) → edges incl. one argued convergence and one genuine tension (S4) → robustness profiles (S5) → page-specs in ≥4 distinct diagram forms (S6) → render the chapter with full per-page QA (S7).
3. Assemble **publish package #1**: the chapter PDF + provenance/coverage summary + escalation queue + known limits. Propose in `STATE.md`; pause for Jason.
**DoD:** a reviewable rendered chapter proving the entire pipeline. Commit: `book: walking-skeleton chapter (publish package 1)`.
*Incorporate Jason's feedback before P4 — this is where course-correction is cheap.*

## P4 · Scale ingestion & verification
S1 across all landed reports, in committed batches (~25 units); S2 rolling, publish-priority first; skew dashboard updated in the index.
**DoD:** all reports ingested; validator clean; verification tiers tracked. Commits per batch: `graph: ingest 04-eastern batch 3/5`.

## P5 · Wave loop *(until saturation)*
1. Assemble next-wave prompts from the backlog (template + do-not-duplicate from the index) → hand to Jason → reports land in `corpus/reports/wave-N/` → P1+P2+P4 for the new wave.
2. Watch the saturation heuristic (<20% new claims). Claude proposes stop/continue; **Jason decides**. Wave-2 gap prompts are ready in `prompts/deep-research/wave-2-gap-traditions.md`.
**DoD:** Jason declares corpus complete for book v1.

## P6 · Graph completion
S3 corpus-wide (reconcile with index merge candidates) → S4 edges + `graph/intellectual-history.md` → S5 profiles for all book-candidate claims. Escalations flow throughout.
**DoD:** METHODOLOGY gates S3–S5 met; queue worked down. Commit: `graph: claims+edges+profiles complete for edition-1 candidates`.

## P7 · Curation → page-specs
Full traversal along the life-phase spine: stage openers, fork selection (6–10/stage), the same-fork-at-different-altitudes device, form selection per node, register gradient. Page-specs only — no generator hacking. Includes front matter (north star, how-to-read, engine) and honest back matter (methodology summary, limits, corpus-composition caveat, colophon).
**DoD:** complete page-spec set; every referenced claim publish-ready. Commit: `book: edition-1 page-specs`.

## P8 · Render & QA
Freeze **edition 1** (git tag + `graph/editions/` manifest) → generator renders all page-specs → **view every page** → fix → re-render until clean.
**DoD:** full book PDF, every page inspected. Commit: `book: edition-1 full render`.

## P9 · Ship gate → publish package
Check METHODOLOGY §8 line by line, with evidence. Assemble the final publish package (book PDF, print-gate audit, provenance summary, remaining escalations, limits). Jason reviews → iterate → sign-off → done. Website and game are subsequent projections of the tagged edition.

---

| Phase | Owner | Output |
|---|---|---|
| P0 env check | Claude Code | capabilities in STATE |
| P1 land reports | Jason → Claude Code | validated wave-1 |
| P2 synthesis | Claude Code | COVERAGE-INDEX |
| **P3 walking skeleton** | Claude Code → Jason | **publish package #1** |
| P4 scale ingest+verify | Claude Code | populated graph/ |
| P5 wave loop | Claude Code prompts · Jason runs · Jason decides stop | saturated corpus |
| P6 graph completion | Claude Code | claims/edges/profiles |
| P7 curation | Claude Code | page-specs |
| P8 render | Claude Code | edition-1 PDF |
| P9 ship gate | Claude Code → Jason | signed-off book v1 |
