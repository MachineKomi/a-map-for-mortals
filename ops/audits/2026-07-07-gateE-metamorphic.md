# Gate E metamorphic proof — all pages traced (executed against the live build)

**Date:** 2026-07-07 · **Edition:** building-years-v0.2.0 · **Scope:** the migrated pages
(mutations target by-020, by-030, by-050 — pages other than the Gate B pilot)
**Method:** each failure mode injected into the real store/specs, `build_book.py`
executed, exit code + refusal message captured verbatim, state restored, positive
control re-run. Runner: scratchpad gateE_metamorphic.py (session artefact; this file is
the persisted record).

| # | Mutation | Observed |
|---|---|---|
| M1 | a-0026 `status` → `draft` (by-020's convergence claim) | exit 1 — `ASSERTION GATE: a-0026 status 'draft' is not approved` |
| M2 | a-0028 loses mandatory caveat "not its twin" | exit 1 — `ASSERTION GATE: a-0028 text no longer carries mandatory caveat 'not its twin'` |
| M3 | "independently arrived" added to by-020 editorial | exit 1 — `ASSERTION GATE: prohibited phrasing 'independently arrived' (per a-0026) appears in unapproved page text on by-020-carrying` |
| M4 | bare (untraced) string restored into by-050's caption | exit 1 — `UNTRACED COPY: bare string under 'caption' on traced page by-050-money` |
| M5 | u-0002 attribution downgraded to `attested` | exit 1 — `PRINT GATE REFUSAL: u-0002 (for c-0002) is attested/public-domain - verbatim quotation forbidden` |
| M6 | restored state (positive control) | exit 0 — 9 traces emitted, render succeeds |

**Result: 6/6.** The Gate B guarantees now hold for every page of the proof chapter:
no page renders with a revoked assertion, a stripped caveat, a prohibited phrasing in
unapproved text, an unverified verbatim quote, or an unadjudicated bare string.

**Honest scope:** still scripted-and-captured rather than a persistent automated suite
over the live store (the fixture suite covers the static rules); wiring these six cases
into tools/tests is queued as post-Gate-E hardening. M4's gate (UNTRACED COPY) exists
only for pages marked `traced: true` — all 9 pages of this chapter are, and new pages
default to traced under the Gate E convention recorded in the plan file.
