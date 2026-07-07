# Review feedback index

Read in this order:

1. **`2026-07-07-adversarial-review.md`** — evidence-backed findings on the methodology and delivered work, including page-level issues and P0/P1/P2 priorities.
2. **`2026-07-07-methodology-v0.4-proposal.md`** — recommended hybrid research model, epistemic layers, claim-specific confirmation dossiers, adversarial roles, and migration strategy.
3. **`2026-07-07-implementation-blueprint.md`** — concrete repository structure, object contracts, phase gates, validators, requirement mapping, page-spec contract, first commits, and stop conditions.
4. **`2026-07-07-response-to-claude-adjudication.md`** — second-model review of Claude's response and implementation: concessions, residual pushbacks, revised-page audit, and the exact reconciliation needed before Gate B.

## Recommended immediate sequence

1. Jason decides whether to adopt the hybrid discovery-corpus + confirmation-dossier model.
2. Claude records that decision and writes the v0.4 schema/transition contract.
3. Claude builds validators and negative fixtures before migrating content.
4. Claude migrates and rebuilds page 8 as the methodological stress test.
5. External review checks the page trace, dossier, render, and failure tests.
6. Only then does Claude migrate the rest of the skeleton or resume large-scale verification.

The central recommendation is to scale **after enforcement**, not after adding caveat prose.
