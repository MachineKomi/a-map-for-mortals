# STATE — the living ledger

**Read me at the start of every session. Update me before every commit that changes status.** The repo is your memory; the context window is not.

## Current phase
**P1** — P0 complete on the PC (2026-07-06). Wave-1 reports landed (7 files); validate them next.

## Status snapshot
- Repo scaffold v0.3 (2026-07-03): harness-native methodology, unified runbook, two-level graph store, ops files, validator. Prototype archived in `prototype/` (do not edit).
- Corpus: Wave-1 reports present in `corpus/reports/wave-1/` — 7 report files + README (methodology, Greco-Roman, Near-Eastern/Abrahamic, literature, moralists/modern philosophy, Nietzsche, empirical flourishing). Not yet renamed to `NN-tradition-shortname.md` convention or validated (P1). Wave-2 gap prompts ready.
- Graph: empty except normative example files (`example: true`). Validator clean on examples (2 files, 0 errors).
- Git: initialised locally on the PC 2026-07-06. **No GitHub remote yet — waiting on Jason** (see blockers).

## Environment capabilities — PC (probed 2026-07-06)
- python: **3.14.3** — invoke as `python`, NOT `python3` (Store alias). pip 25.3 works without `--break-system-packages`.
- pyyaml: **6.0.3 installed**; validator runs clean.
- weasyprint: pip package installs but **cannot render** (missing GTK/Pango DLLs; sandbox blocked the GTK runtime installer). **Working renderer: official standalone `tools/bin/weasyprint.exe` v69.0** (gitignored; re-fetch per machine with `python tools/fetch_weasyprint.py`). Verified: rendered a test PDF.
- pdftoppm: **absent**. Replacement: `tools/pdf_to_png.py` (pypdfium2, pure pip). Verified: rasterised the test PDF; page viewed. Same QA discipline, different binary.
- QA-loop lesson (real defect caught): generated HTML must declare `<meta charset="utf-8">` or non-ASCII (em-dashes etc.) renders as mojibake.
- sentence-transformers: **deliberately deferred** (heavy torch install on a low/mid-spec machine; optional per METHODOLOGY §4/§6). Primary S3 method is Claude adjudication; attempt install only if cross-check is needed at S3 and record the outcome here.
- external second-model CLI: **none found** (no codex/gemini/ollama/gh). Adversarial ladder fallback (b) is active: fresh-context subagent with adversarial charter, shared-weights disclosed in `method`.
- Chrome + Edge present (backup HTML→PDF path if WeasyPrint ever breaks; not currently used).

## Environment capabilities — laptop
- **Unprobed. Run P0 probe on first laptop session and record here.** (`python tools/fetch_weasyprint.py` + `pip install pyyaml pypdfium2` should be the whole setup.)

## Next actions (ordered)
1. **Jason: create/share the GitHub remote** → `git remote add origin … && git push -u origin main`.
2. P1: validate the 7 wave-1 reports (expected shape: source inventory, unit blocks, dilemmas, convergences, misattribution list, leads); rename to `NN-tradition-shortname.md`; log gaps in `COVERAGE-INDEX.md`. Commit `corpus: land wave-1 reports`.
3. P2: synthesise → rebuild `corpus/COVERAGE-INDEX.md` from real data (coverage map, gap register, merge candidates, tension candidates, next-wave backlog, wave metrics). Commit `index: synthesise wave-1`.
4. P3: walking-skeleton chapter (~30 units end-to-end) → **publish package #1** for Jason.

## Blockers / waiting on Jason
- **GitHub remote**: repo arrived on the PC without `.git`. Local git initialised; need the remote URL (or Jason creates an empty repo and shares it). Until then, single-machine only — do not start work on the laptop.
- Licence decision — `ops/ESCALATIONS.md` E-0001 (recommend MIT code / CC-BY 4.0 content; needed before wide sharing, not before P1–P3).

## Publish packages
| # | Contents | Proposed | Status |
|---|---|---|---|
| 1 | Walking-skeleton chapter (P3) | — | not yet |

## Session log (newest first)
- 2026-07-06 · PC (Claude Code): P0 complete. Probed environment (see capabilities); pip weasyprint unrenderable on Windows → adopted official standalone exe + wrote `tools/fetch_weasyprint.py`; pdftoppm absent → wrote `tools/pdf_to_png.py` (pypdfium2); full render→rasterise→view loop verified with evidence (test page viewed; charset mojibake caught and documented). Validator clean on examples. Git initialised; first commit. Found wave-1 reports already landed (7). Flagged missing GitHub remote to Jason.
- 2026-07-03 · Claude chat: v0.3 scaffold built; critical review applied (harness-native stack, verification tiers + print gate, STATE ledger, cross-model fallback ladder, numeric targets, walking-skeleton phase). Handed off to Claude Code.
