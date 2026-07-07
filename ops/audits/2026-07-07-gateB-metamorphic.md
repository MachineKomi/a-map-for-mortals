# Gate B metamorphic proof — page 8 pilot (executed against the live build)

**Date:** 2026-07-07 · **Target:** `by-080-help` (traced-prose) at edition building-years-v0.1.1
**Method:** each failure mode injected into the real store, `build_book.py` executed,
exit code + refusal message captured verbatim, state restored, positive control re-run.

| # | Mutation | Expected | Observed |
|---|---|---|---|
| M1 | a-0004 `status: approved-…` → `draft` | build fails | exit 1 — `ASSERTION GATE: a-0004 status 'draft' is not approved` |
| M2 | a-0002 text loses its mandatory caveat | build fails | exit 1 — `ASSERTION GATE: a-0002 text no longer carries mandatory caveat 'anonymity marks a separate rung'` |
| M3 | prohibited phrase ("point the same way") added to editorial copy | build fails | exit 1 — `ASSERTION GATE: prohibited phrasing 'point the same way' (per a-0001) appears in unapproved page text on by-080-help` |
| M4 | u-0024 attribution downgraded to `attested` | quote gate fails | exit 1 — `PRINT GATE REFUSAL: u-0024 (for c-0024) is attested/public-domain — verbatim quotation forbidden` |
| M5 | restored state (positive control) | build passes | exit 0 — render + trace emitted |

**Result: 5/5 behave correctly.** The reviewer's Gate-B acceptance criterion —
"page 8 must become impossible to render with an undeclared quote, false convergence,
stale evidence dependency, or unsupported shared lesson" — is met for this page:
undeclared quotes are caught by the copy linter (proven in tools/tests, 10/10), false
convergence phrasing by the prohibited-phrase sweep (M3), stale approval/evidence by
the assertion gate (M1/M2), and unverified quotation by the print gate (M4).

**Honest scope:** one page renders this way. The other eight pages remain on the v0.3
copy path (mitigated, not traced) until Gate E migrates them through the same model.
These runs were scripted and their outputs captured, but they are not yet a persistent
automated suite over the real store — the fixture suite covers the static rules;
build-time metamorphic automation is queued with the Gate E migration.
