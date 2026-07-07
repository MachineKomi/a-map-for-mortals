# tools/

Pipeline scripts. Grow the toolkit here; document each script's purpose at the top of the file; prefer stdlib + pyyaml; graceful failure messages over stack traces.

- `validate_units.py` — schema validator for graph/ YAML (units, claims, edges). Run before every graph commit; CI-style exit codes.
- `fetch_weasyprint.py` — one-time per machine: downloads the official WeasyPrint standalone Windows exe (pinned v69.0) into `tools/bin/` (gitignored). The pip package lacks GTK/Pango DLLs on Windows; the official exe is self-contained.
- `fetch_fonts.py` — one-time per machine: downloads Lora + Poppins (OFL) from the official google/fonts repo into `book/generator/fonts/` (gitignored). WeasyPrint v69 ignores variable-font weight ranges — the generator declares discrete weights.
- `validate_graph.py` — cross-file integrity + future-date rejection + the QUOTE LINTER (any ≥8-word overlap between page-spec copy and held quotation text fails unless gate-declared). Run with validate_units.py before every commit.
- `generate_status.py` — regenerates STATE.md's STATUS block from the store. Hand-maintained counts are forbidden (external review P1-10).
- `pdf_to_png.py` — pdftoppm replacement (pypdfium2, pure pip). Rasterises a PDF to per-page PNGs for the mandatory view-every-page QA loop.
- `apply_canonical_ids.py` — Gate A registry canonicalisation: fills `canonical_id` in graph/registries/ from an adjudicated mapping YAML. All-or-nothing (refuses on any coverage gap); the mapping file with its contested flags is the audit record — commit it alongside the registries.
- `tests/run_fixture_tests.py` — negative fixtures: 12 minimal stores, each with exactly one honesty-rule violation, asserting validate_graph.py fails with the expected message (plus a positive control). Run after any validator change.

**Machine notes (PC, 2026-07-06):** invoke Python as `python` (not `python3` — that's a Windows Store alias here). Render with `tools/bin/weasyprint.exe IN.html OUT.pdf`. Generated HTML **must** declare `<meta charset="utf-8">` — caught real mojibake in the P0 probe without it.

Expected to grow: report ingestion helpers, a NetworkX loader/query helper, verification fetch helpers, skew dashboard, edition freezer, page-spec renderer glue.
