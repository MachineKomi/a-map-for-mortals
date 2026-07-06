# graph/ — the wisdom graph (canonical store)

YAML in git; schema in `A-Map-for-Mortals-METHODOLOGY.md §3`; the `example: true` files here are **normative for format** — replace with real data as it lands (keep or delete the examples then).

- `units/u-####.yaml` — one sourced expression each (quote/passage + source + labels + verification).
- `claims/c-####.yaml` — canonical merged ideas; `member_units` links; robustness profiles live here.
- `edges/e-####.yaml` — typed, provenance-carrying relations (CONTRADICTS ≠ IN_TENSION_WITH; independence graded on CONVERGES_WITH).
- `editions/` — frozen-edition manifests (with git tags) that the book cites.
- `intellectual-history.md` — the transmission layer (who read whom) that independence judgments argue against. Created at S4.

Validate with `python3 tools/validate_units.py` before committing. IDs are stable; soft-delete, never re-use.
