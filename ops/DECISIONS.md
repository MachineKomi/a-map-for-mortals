# Decision Log

Significant decisions, newest first. Institutional memory for future sessions — check here before re-litigating anything.

| Date | Decision | Rationale / source |
|---|---|---|
| 2026-07-06 | **Licence (closes E-0001):** MIT for code; graph/book/docs **all rights reserved for now**, revisit at edition 1 with presumption toward opening the graph (CC-BY 4.0 + per-field exclusions); corpus reports **no licence granted, audit only**. See `LICENSE.md`. | Delegated by Jason 2026-07-06. Initial proposal (MIT + CC-BY content + ARR book) was put through an adversarial fresh-context pass (method: subagent, shared weights disclosed). Adversary's decisive objections, accepted: (1) the book is generated from the graph, so CC-BY graph = irrevocable licence to commercially republish the book's substance — the ARR book layer would be self-defeating; (2) CC-BY is a one-way door taken at minimum information — ARR→open is one commit, open→ARR is impossible; (3) corpus reports are AI outputs with mixed/unclear copyright — "original portions CC-BY" is un-administrable and may licence an empty set; honest label is "no licence, audit only"; (4) real anti-knock-off levers at ship time are trademark/first-mover/versioning, not licence choice — queue for edition 1. Verdicts did not diverge (adversary: "concur with modifications"); modifications adopted wholesale. Revisit trigger: edition-1 freeze (P8). |
| 2026-07-06 | Repo managed by Claude Code (Jason hands-off on GitHub); laptop is the primary machine, GPU tower/cloud only on documented need | Jason 2026-07-06 |
| 2026-07-03 | Harness-native stack by default; heavy tools (Neo4j, big embedders, NLI, text-reuse) optional upgrades only | Execution realism in Claude Code (METHODOLOGY v0.3 §6) |
| 2026-07-03 | Print gate: verbatim book quotes require verified-primary + public-domain | Truth above all, operationalised (METHODOLOGY §2) |
| 2026-07-03 | Two-level store: units (sourced expressions) vs claims (canonical, merged) | Schema clarity; clean dedup |
| 2026-07-03 | Walking-skeleton chapter before corpus-wide scaling | De-risk the full pipeline early; cheap course-correction |
| 2026-07-03 | Cross-model adversarial pass with fallback ladder (external CLI → fresh-context subagent → escalate); never blend verdicts | Jason's GPT-5.5 suggestion, made harness-realistic |
| 2026-06 | Claude Code exclusively (no Cowork); autonomous runs; Jason reviews publish packages only | Jason |
| 2026-06 | Life-phase spine (8 stages, read-aloud → end of life); diagram form library, form follows content | Jason feedback on prototype (SPEC v0.2) |
| 2026-06 | Title locked: *A Map for Mortals* + subtitle; Principle 16 (humour) locked; truth above all fixed forever | Jason (prototype phase; copy archived in prototype/) |
