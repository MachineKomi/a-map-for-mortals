# book/ — the production book build

- `generator/build_book.py` — the production generator, seeded from the proven prototype (WeasyPrint; no JS; hand-authored SVG/HTML diagrams). Extend per SPEC: one parameterised builder per diagram form; content comes from page-specs, not hardcoding.
- `page-specs/` — one YAML per page/spread (SPEC §12): stage, form, referenced claim/unit IDs, register knobs, copy. **Curation edits page-specs, not generator code.**
- `renders/` — output PDFs + page rasters. Mandatory QA: `pdftoppm -png`, view every page.

Locked creative copy (title, subtitle, Principle 16, "On laughing", design tokens) lives in the archived `prototype/build_book.py` — carry it forward verbatim.
