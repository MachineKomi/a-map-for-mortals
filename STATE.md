# STATE — the living ledger

**Read me at the start of every session. Update me before every commit that changes status.** The repo is your memory; the context window is not.

## Current phase
**P1 → P2** — P0 complete on the laptop (2026-07-06). Wave-1 reports landed, renamed, validated. Synthesis (P2) next.

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
1. P2: synthesise → rebuild `corpus/COVERAGE-INDEX.md` from real data (coverage map incl. life-stage × domain, gap register, merge candidates, tension candidates, next-wave backlog with do-not-duplicate notes, wave metrics). Commit `index: synthesise wave-1`.
2. P3: walking-skeleton chapter (~30 units end-to-end: ingest → verify → claims → edges → profiles → page-specs → rendered chapter) → **publish package #1** for Jason.
3. Prepare wave-2 prompts (Eastern traditions is the headline gap; also women's voices, non-Western literature, childhood/elder life-stages — see COVERAGE-INDEX gap register).

## Blockers / waiting on Jason
- None currently.

## Publish packages
| # | Contents | Proposed | Status |
|---|---|---|---|
| 1 | Walking-skeleton chapter (P3) | — | not yet |

## Session log (newest first)
- 2026-07-06 (later) · laptop: remote `github.com/MachineKomi/a-map-for-mortals` connected & pushed. Corrected machine labels (this machine is the laptop, not the PC; tower = optional compute). Licence decided under delegation after adversarial review (E-0001 → closed; `LICENSE.md`; reasoning in `ops/DECISIONS.md`). P1 done: reports renamed to convention (04 kept vacant — eastern report missing), 7 parallel fresh-context reviews ran shape/citation/red-flag checks; all usable; findings logged in COVERAGE-INDEX.
- 2026-07-06 · laptop (Claude Code): P0 complete. Probed environment (see capabilities); pip weasyprint unrenderable on Windows → adopted official standalone exe + wrote `tools/fetch_weasyprint.py`; pdftoppm absent → wrote `tools/pdf_to_png.py` (pypdfium2); full render→rasterise→view loop verified with evidence (test page viewed; charset mojibake caught and documented). Validator clean on examples. Git initialised; first commit. Found wave-1 reports already landed (7). Flagged missing GitHub remote to Jason.
- 2026-07-03 · Claude chat: v0.3 scaffold built; critical review applied (harness-native stack, verification tiers + print gate, STATE ledger, cross-model fallback ladder, numeric targets, walking-skeleton phase). Handed off to Claude Code.
