# STATE — the living ledger

**Read me at the start of every session. Update me before every commit that changes status.** The repo is your memory; the context window is not.

## Current phase
**P3 COMPLETE — publish package #1 proposed; PAUSED for Jason's review.** The Building Years chapter is rendered and page-QA'd (`book/renders/building-years-v0.1.0.pdf`, 9 pages). Full pipeline proven: S1 33 units → S2 32/33 verified → S3 33 claims adjudicated → S4 23 edges adjudicated → S5 25 profiles → S6 9 page-specs → S7 render, every page viewed. **Review: `ops/publish-packages/package-01.md`.** Wave-2 landed (8/8, unprocessed) — processing it is the next non-blocked work.

### S2 status — COMPLETE for the skeleton (2026-07-07)
- **verified-primary (24):** u-0001–u-0018 (except u-0019 n/a here), u-0021–u-0025 — precisely: u-0001–u-0008, u-0009–u-0018, u-0021–u-0025. Every one carries matched text + URL in `verification.checked_against`.
- **verified-secondary (8):** u-0026–u-0033 (empirical; DOI-confirmed).
- **attested (1):** u-0019 (Russell) — US-PD since Jan 2026 but no fetchable transcription yet; attempts logged in the unit; `copyright_flag: in-copyright` anyway (life+70 non-US to 2041), so it was never a verbatim-print candidate.
- **Six wave-1 report errors caught and corrected at S2** (log for the honesty appendix): Carter→Higginson (u-0001), spliced Marcus wording (u-0002), "short time to live"→"short space of time" (u-0003), non-Conington crib (u-0004), Basore→Stewart (u-0006), Taylor mis-credit (u-0010), P&V-as-Garnett (u-0024). Pattern: report attributions of *translations* are the weak layer — S2 checks are non-negotiable for every print candidate at P4 scale.

### P3 walking-skeleton design (fixed for this phase)
- **Stage:** The Building Years (~26–45; "How do I carry what I've taken on?").
- **Five forks:** (1) carrying vs releasing [effort⟷acceptance master fork: u-0001,02,07,09,10,21]; (2) ambition vs peace [u-0013,14,15,16,22 + money findings u-0026,27]; (3) time, the scarce thing [u-0003,04,11,17,18 + habit findings u-0028,29]; (4) the weight that strengthens? [u-0005,06,08,23 + PTG/resilience u-0030,31]; (5) the help that frees [u-0012,19,20,24,25 + u-0032,33].
- **Planned edges:** argued convergence on fork 1 (Stoic·Nietzsche·tawakkul·Lear — independence graded per lineage notes); genuine tension on fork 2 (striving ⟷ contentment). More as adjudicated at S4.
- **Render pipeline ready:** fonts fetched+verified (`tools/fetch_fonts.py`); WeasyPrint exe + pdf_to_png QA loop proven. Generator note: declare discrete font weights (variable-range syntax ignored by WeasyPrint v69).

## Status snapshot
- Repo scaffold v0.3 (2026-07-03): harness-native methodology, unified runbook, two-level graph store, ops files, validator. Prototype archived in `prototype/` (do not edit).
- Corpus: Wave-1 landed — 7 of the nominal 8 reports. **04-eastern never landed** (no Eastern-traditions report: Confucian, Daoist, Buddhist, Hindu all missing from wave-1) — top gap for wave-2. All 7 present reports validated (see `corpus/COVERAGE-INDEX.md`): shape complete, misattribution watchlists strong, no fabricated citations detected by review; per-report gaps logged.
- Graph: 33 skeleton units (u-0001–u-0033), 32 verified (24 primary, 8 secondary), 1 attested. Validator clean (35 files).
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
1. **PAUSED — awaiting external adversarial review.** Jason is running a GPT-5.5 review of methodology, approach, and output. Process its verdicts per CLAUDE.md §4 (concur/diverge, never blend; record in ops/adjudications/; stalemates back to Jason). This is ladder option (a) — a genuinely external second model.
2. After the review lands: S2 rolling verification of the 313 new units (publish-priority first; translation attributions are the known weak layer — 8+ more suspected mislabels already flagged unknown at mint); then corpus-wide S3 merging (P6) with the recorded FOR-MERGE candidates.
2. ~~Wave-2 P1/P2~~ **DONE 2026-07-08** (all validated, extracted, index rebuilt; spine ends fed — child 19, elder 132 combined).
3. After sign-off: P4 scale ingestion (remaining ~150 wave-1 units + wave-2, batches of ~25; S2 checks mandatory on every print candidate — the translation-attribution lesson).
4. Backlog: u-0019 Russell PD text retry; u-0008 German vs Nietzsche Source; original-language capture where still null (u-0001 Greek, u-0023 Greek).

## Blockers / waiting on Jason
- None currently. (Package #1 approved 2026-07-08.)

## Publish packages
| # | Contents | Proposed | Status |
|---|---|---|---|
| 1 | The Building Years chapter + provenance + escalations + limits (`ops/publish-packages/package-01.md`) | 2026-07-07 | **APPROVED by Jason 2026-07-08** ("Looks great so far, please proceed") |

## Session log (newest first)
- 2026-07-08 (P4 complete → pause) · laptop: ingestion finished — 25 minting agents total produced u-0034..u-0346; graph now holds all 346 report-level units (404 files validate clean). S1 gate spot-check passed 15/15. CARE discipline held (2 record-only stubs, 16 consent-gates). Jason requested an external GPT-5.5 adversarial review of methodology/approach/output — in-flight work landed and committed, then paused. No S2/S3/curation work until feedback arrives.
- 2026-07-08 (wave-2 P2) · laptop: eight extraction agents → 164 units in corpus/synthesis/wave-2/ (44 dilemmas, 36 convergences with FOR-MERGE flags, 34 tensions; CARE flags carried on all 24 Indigenous units — 11 consent-gate, 2 record-only). Index rebuilt: combined 346 report-level units; spine ends transformed (child 3→19, youth 23→65, elder 59→132 incl. living-the-end material); wave-2 saturation row added (novelty very high, no signal, by design). Cross-wave merge candidates recorded for P6 — Gita/Buddhist↔Stoic control cluster feeds skeleton claim c-0001 directly. Overnight run ends here: P4 scaling deliberately waits for Jason's package-01 review per the runbook (course-correction is cheap before scale).
- 2026-07-08 (wave-2 P1, overnight continued) · laptop: eight parallel validators — ALL PASS (~170 report-level units). Standouts: Eastern report gates every Buddha/Laozi quote against external checkers; Indigenous report documents Chief Seattle to the 1972 screenwriter and imposes a consent/CARE gate; Persian report marks every FitzGerald quatrain dubious; strategic report traces 'ends justify the means' to Ovid. Gap register updated: Eastern/African/Indigenous/Women's/P2-breadth gaps CLOSED; child+elder reduced. Next: wave-2 extraction to corpus/synthesis/wave-2/ + full index rebuild (P2), then P4 scale ingestion after Jason's package-01 review.
- 2026-07-07 (P3 S3–S7, overnight run) · laptop: S3 33 claims (1:1, merges deferred); S4 23 edges; adversarial pass on both (24 concur / 9 diverge, all adopted — 3 convergences retyped as lineage, Faust endorsement discipline enforced, field drift batch-aligned; record in ops/adjudications/). S5 25 profiles, provisional-by-design. Production generator built; print gate refused a copyright-unknown Seneca quote and validated ellipsis excerpts verbatim. First render 12 pages → per-page QA found 3 overflow defects → fixed → 9 pages, every page viewed clean. Publish package #1 proposed; P3 paused for Jason.
- 2026-07-07 (P3·S2 finish) · laptop: completed the 10 queued verifications directly (curl + char-matching, no subagents — spend economy). Five more report errors caught (Carter→Higginson, spliced Marcus, Basore wording, non-Conington crib, Basore→Stewart) and Kaufmann replaced with verified Ludovici PD text. u-0019 Russell honestly left attested (no fetchable text yet). S2 pattern logged: translation attributions are the reports' weak layer.
- 2026-07-07 (P3·S2 + wave-2 landing) · laptop: six S2 verifier agents dispatched; three completed (14 verified-primary incl. three real corrections — Avot/Taylor, Garnett wording, Touger→Meszler licence swap; 8 empirical verified-secondary with a title and an HR figure corrected against the journals). Three agents killed by the monthly spend limit mid-run — their orphaned edits audited: u-0013–u-0018 verifications independently re-matched against source texts and accepted; u-0001 partial edit reverted (no trail). 10 units still queued. Wave-2 arrived complete (8/8): renamed to convention, section shape checked; deep validation deferred until P3 ships. Escalation E-0002 added (Maimonides translation choice).
- 2026-07-06 (P3·S1) · laptop: wave-2 prompts assembled ready-to-paste (Jason running them). SPEC read; skeleton chapter fixed = The Building Years, 5 forks, 33 units selected across all 6 reports. Six minting agents produced u-0001..u-0033 (validator clean; everything attested + pending-primary regardless of report labels; labels re-derived; honest flags: P&V-not-Garnett wording on u-0024, Darussalam translation in-copyright on u-0009, supplied paper titles marked for DOI check on empirical units). 15% spot-check passed. Fonts fetched + render-verified (`tools/fetch_fonts.py`; discrete weights needed under WeasyPrint v69).
- 2026-07-06 (P2) · laptop: six parallel extraction agents produced faithful per-report YAML extracts (`corpus/synthesis/wave-1/`, 182 units; missing fields left empty, never invented; compound labels preserved verbatim). COVERAGE-INDEX rebuilt from real data: life-stage×domain tallies (child=3, youth=23 — spine's ends starving), 12 cross-report convergence clusters (lineage flags preserved; PTG/money empirical qualifiers attached), 10 cross-report forks (effort⟷acceptance in 5/6 reports = master fork), wave-1 baseline metrics, re-ranked backlog. Wave-2 prompt pack extended: block 2·0 Eastern (P0, replaces never-run 04) + block 2g childhood/old-age corrective (P1).
- 2026-07-06 (later) · laptop: remote `github.com/MachineKomi/a-map-for-mortals` connected & pushed. Corrected machine labels (this machine is the laptop, not the PC; tower = optional compute). Licence decided under delegation after adversarial review (E-0001 → closed; `LICENSE.md`; reasoning in `ops/DECISIONS.md`). P1 done: reports renamed to convention (04 kept vacant — eastern report missing), 7 parallel fresh-context reviews ran shape/citation/red-flag checks; all usable; findings logged in COVERAGE-INDEX.
- 2026-07-06 · laptop (Claude Code): P0 complete. Probed environment (see capabilities); pip weasyprint unrenderable on Windows → adopted official standalone exe + wrote `tools/fetch_weasyprint.py`; pdftoppm absent → wrote `tools/pdf_to_png.py` (pypdfium2); full render→rasterise→view loop verified with evidence (test page viewed; charset mojibake caught and documented). Validator clean on examples. Git initialised; first commit. Found wave-1 reports already landed (7). Flagged missing GitHub remote to Jason.
- 2026-07-03 · Claude chat: v0.3 scaffold built; critical review applied (harness-native stack, verification tiers + print gate, STATE ledger, cross-model fallback ladder, numeric targets, walking-skeleton phase). Handed off to Claude Code.
