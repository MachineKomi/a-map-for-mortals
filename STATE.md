# STATE — the living ledger

**Read me at the start of every session. Update me before every commit that changes status.** The repo is your memory; the context window is not.

## Current phase
**P3 in progress — S2 mostly done (23/33 verified)** — walking-skeleton chapter is **The Building Years** (SPEC stage 5). Wave-2 landed in parallel (8/8 reports, renamed, shape-checked — deep validation deferred until P3 ships).

### S2 status (2026-07-07)
- **verified-primary (14):** u-0009–u-0012, u-0013–u-0018, u-0021–u-0025 — all with matched text + URL in `verification.checked_against`. Real corrections made: Avot wording fixed to Taylor 1897's actual text (report mis-credit); Dostoevsky fixed to Garnett's real wording ("love in action is a harsh and dreadful thing", Book II ch. 4); Maimonides translation swapped Touger(NC)→Meszler(CC-BY) (curation choice queued, E-0002).
- **verified-secondary (8):** u-0026–u-0033 (empirical; DOI-confirmed; one title + one HR figure corrected).
- **REMAINING QUEUE (10): u-0001–u-0008 (Greco-Roman, Nietzsche), u-0019, u-0020.** Three verifier agents died on the monthly spend limit mid-run; u-0001's partial upgrade was reverted (no verification trail). Sources known-good: Gutenberg (#2680 Long Marcus, #52263 Ludovici Twilight, #52190 Ludovici Ecce Homo, #10741 Saunders), Wikisource Seneca Letter 13/Gummere, Perseus Horace. Gutenberg was timing out at session end — retry.

### P3 walking-skeleton design (fixed for this phase)
- **Stage:** The Building Years (~26–45; "How do I carry what I've taken on?").
- **Five forks:** (1) carrying vs releasing [effort⟷acceptance master fork: u-0001,02,07,09,10,21]; (2) ambition vs peace [u-0013,14,15,16,22 + money findings u-0026,27]; (3) time, the scarce thing [u-0003,04,11,17,18 + habit findings u-0028,29]; (4) the weight that strengthens? [u-0005,06,08,23 + PTG/resilience u-0030,31]; (5) the help that frees [u-0012,19,20,24,25 + u-0032,33].
- **Planned edges:** argued convergence on fork 1 (Stoic·Nietzsche·tawakkul·Lear — independence graded per lineage notes); genuine tension on fork 2 (striving ⟷ contentment). More as adjudicated at S4.
- **S2 verification queue (book candidates first):** u-0001 (Carter wording mismatch flagged), u-0008 (Gutenberg #52263), u-0021 (fix edition), u-0024 (**P&V-wording landmine — must substitute real Garnett text**), u-0013 (capture the 'what one is' sentence itself), empirical DOI checks (titles supplied beyond report: confirm all 8).
- **Render pipeline ready:** fonts fetched+verified (`tools/fetch_fonts.py`); WeasyPrint exe + pdf_to_png QA loop proven. Generator note: declare discrete font weights (variable-range syntax ignored by WeasyPrint v69).

## Status snapshot
- Repo scaffold v0.3 (2026-07-03): harness-native methodology, unified runbook, two-level graph store, ops files, validator. Prototype archived in `prototype/` (do not edit).
- Corpus: Wave-1 landed — 7 of the nominal 8 reports. **04-eastern never landed** (no Eastern-traditions report: Confucian, Daoist, Buddhist, Hindu all missing from wave-1) — top gap for wave-2. All 7 present reports validated (see `corpus/COVERAGE-INDEX.md`): shape complete, misattribution watchlists strong, no fabricated citations detected by review; per-report gaps logged.
- Graph: empty except normative example files (`example: true`). Validator clean on examples (2 files, 0 errors).
- Git: remote connected and pushed 2026-07-06 — `https://github.com/MachineKomi/a-map-for-mortals` (public). Claude Code manages the repo.
- Licence: **decided 2026-07-06** (delegated by Jason; adversarially reviewed) — MIT for code; graph/book/docs all rights reserved **for now**, revisit at edition 1 with presumption toward opening the graph; corpus reports unlicensed, audit-only. See `LICENSE.md` + `ops/DECISIONS.md`.

## Machines & compute strategy
- **Laptop (this machine) is primary** — Jason expects most or all of the project to run here. Low/mid-spec; prefer light tooling.
- **GPU tower** (128GB RAM, 12GB VRAM) available if genuinely needed (e.g. heavy embedding/clustering at S3 scale); Jason can also spin up cloud compute. Escalate a request only when a documented limit is hit — don't design for hardware we don't need.

## Environment capabilities — laptop (probed 2026-07-06)
- python: **3.14.3** — invoke as `python`, NOT `python3` (Store alias). pip 25.3 works without `--break-system-packages`.
- pyyaml: **6.0.3 installed**; validator runs clean.
- weasyprint: pip package installs but **cannot render** (missing GTK/Pango DLLs; sandbox blocked the GTK runtime installer). **Working renderer: official standalone `tools/bin/weasyprint.exe` v69.0** (gitignored; re-fetch per machine with `python tools/fetch_weasyprint.py`). Verified: rendered a test PDF.
- pdftoppm: **absent**. Replacement: `tools/pdf_to_png.py` (pypdfium2, pure pip). Verified: rasterised the test PDF; page viewed. Same QA discipline, different binary.
- QA-loop lesson (real defect caught): generated HTML must declare `<meta charset="utf-8">` or non-ASCII (em-dashes etc.) renders as mojibake.
- sentence-transformers: **deliberately deferred** (heavy torch install on a low/mid-spec machine; optional per METHODOLOGY §4/§6). Primary S3 method is Claude adjudication; attempt install only if cross-check is needed at S3 and record the outcome here. If it underfits, the GPU tower is the documented upgrade path.
- external second-model CLI: **none found** (no codex/gemini/ollama/gh). Adversarial ladder fallback (b) is active: fresh-context subagent with adversarial charter, shared-weights disclosed in `method`.
- Chrome + Edge present (backup HTML→PDF path if WeasyPrint ever breaks; not currently used).

## Environment capabilities — GPU tower
- **Unprobed; probe only if/when heavy compute is actually needed.** (`python tools/fetch_weasyprint.py` + `pip install pyyaml pypdfium2` should be the whole base setup on any new machine.)

## Next actions (ordered)
1. P3·S2 finish: verify the remaining 10 units (u-0001–u-0008, u-0019, u-0020; sources listed above). Do directly (curl + python match), not via heavy agents — spend-limit economy.
2. P3·S3: cluster the 33 units to claims (Claude adjudication + adversarial second pass; c-#### files). S4 edges (argued convergence on fork 1 with independence_basis; genuine tension on fork 2). S5 robustness profiles.
3. P3·S6/S7: page-specs for The Building Years (journey-map opener + ≥4 distinct forms) → production generator from prototype (discrete font weights; charset meta) → render → view every page → **publish package #1** for Jason.
4. After P3 ships: wave-2 P1/P2 (deep-validate the 8 landed reports, extract, rebuild COVERAGE-INDEX, wave metrics vs saturation heuristic).
5. Then P4 scale ingestion (remaining ~150 wave-1 units + wave-2, batches of ~25).

## Blockers / waiting on Jason
- None currently.

## Publish packages
| # | Contents | Proposed | Status |
|---|---|---|---|
| 1 | Walking-skeleton chapter (P3) | — | not yet |

## Session log (newest first)
- 2026-07-07 (P3·S2 + wave-2 landing) · laptop: six S2 verifier agents dispatched; three completed (14 verified-primary incl. three real corrections — Avot/Taylor, Garnett wording, Touger→Meszler licence swap; 8 empirical verified-secondary with a title and an HR figure corrected against the journals). Three agents killed by the monthly spend limit mid-run — their orphaned edits audited: u-0013–u-0018 verifications independently re-matched against source texts and accepted; u-0001 partial edit reverted (no trail). 10 units still queued. Wave-2 arrived complete (8/8): renamed to convention, section shape checked; deep validation deferred until P3 ships. Escalation E-0002 added (Maimonides translation choice).
- 2026-07-06 (P3·S1) · laptop: wave-2 prompts assembled ready-to-paste (Jason running them). SPEC read; skeleton chapter fixed = The Building Years, 5 forks, 33 units selected across all 6 reports. Six minting agents produced u-0001..u-0033 (validator clean; everything attested + pending-primary regardless of report labels; labels re-derived; honest flags: P&V-not-Garnett wording on u-0024, Darussalam translation in-copyright on u-0009, supplied paper titles marked for DOI check on empirical units). 15% spot-check passed. Fonts fetched + render-verified (`tools/fetch_fonts.py`; discrete weights needed under WeasyPrint v69).
- 2026-07-06 (P2) · laptop: six parallel extraction agents produced faithful per-report YAML extracts (`corpus/synthesis/wave-1/`, 182 units; missing fields left empty, never invented; compound labels preserved verbatim). COVERAGE-INDEX rebuilt from real data: life-stage×domain tallies (child=3, youth=23 — spine's ends starving), 12 cross-report convergence clusters (lineage flags preserved; PTG/money empirical qualifiers attached), 10 cross-report forks (effort⟷acceptance in 5/6 reports = master fork), wave-1 baseline metrics, re-ranked backlog. Wave-2 prompt pack extended: block 2·0 Eastern (P0, replaces never-run 04) + block 2g childhood/old-age corrective (P1).
- 2026-07-06 (later) · laptop: remote `github.com/MachineKomi/a-map-for-mortals` connected & pushed. Corrected machine labels (this machine is the laptop, not the PC; tower = optional compute). Licence decided under delegation after adversarial review (E-0001 → closed; `LICENSE.md`; reasoning in `ops/DECISIONS.md`). P1 done: reports renamed to convention (04 kept vacant — eastern report missing), 7 parallel fresh-context reviews ran shape/citation/red-flag checks; all usable; findings logged in COVERAGE-INDEX.
- 2026-07-06 · laptop (Claude Code): P0 complete. Probed environment (see capabilities); pip weasyprint unrenderable on Windows → adopted official standalone exe + wrote `tools/fetch_weasyprint.py`; pdftoppm absent → wrote `tools/pdf_to_png.py` (pypdfium2); full render→rasterise→view loop verified with evidence (test page viewed; charset mojibake caught and documented). Validator clean on examples. Git initialised; first commit. Found wave-1 reports already landed (7). Flagged missing GitHub remote to Jason.
- 2026-07-03 · Claude chat: v0.3 scaffold built; critical review applied (harness-native stack, verification tiers + print gate, STATE ledger, cross-model fallback ladder, numeric targets, walking-skeleton phase). Handed off to Claude Code.
