# Publish Package #1 — The Building Years (walking-skeleton chapter)

**Proposed:** 2026-07-07 · **Status: APPROVED 2026-07-08** — Jason: "Looks great so far, please proceed." Register, honesty apparatus, and fork selection stand as rendered; P4 unlocked.
**The deliverable:** `book/renders/building-years-v0.1.0.pdf` (9 pages; HTML beside it).
Regenerate any time with `python book/generator/build_book.py`; QA rasters with
`python tools/pdf_to_png.py book/renders/building-years-v0.1.0.pdf book/renders/qa --dpi 110`.

## What this package proves (the point of P3)

The full pipeline ran end-to-end on one chapter before anything scales: report →
S1 ingestion (33 units) → S2 primary verification (32/33, with matched text recorded
per unit) → S3 claims (33, adversarially adjudicated) → S4 edges (23, typed and
independence-graded, adversarially adjudicated) → S5 robustness profiles (25
publish-ready claims) → S6 page-specs (9) → S7 render with per-page visual QA
(12 pages viewed in round 1, 3 defects found and fixed, 9 pages re-viewed clean).

## Provenance & coverage summary

- **Content:** 5 forks of The Building Years; 7 diagram forms; 12 verbatim quotations,
  every one pulled from the graph through the print gate (verified-primary AND
  public-domain-or-licensed — the build refuses otherwise; it refused twice during
  production, correctly both times).
- **Verification:** every printed quote traces to a unit whose `verification.checked_against`
  holds URL + edition + the matched text. Seven wave-1 report errors (all translation
  attributions) were caught and corrected at S2 — the full list is in STATE.md.
- **Adjudication:** clustering and edges went through a fresh-context adversarial pass
  (shared weights disclosed); 9 divergences adopted, incl. retyping three "convergences"
  as lineage (INFLUENCED) — visible on the fork-one map as dashed lines. Record:
  `ops/adjudications/2026-07-07-s3s4-skeleton.md`.
- **Honest-asterisk showpiece:** page 7 prints "suffering strengthens" WITH its empirical
  contestation (PTG measurement critique; resilience-is-modal) and a `survives scrutiny:
  LOW` trust label. This is the book's honesty contract made visible.

## Escalations attached (2 open — target <30 ✓)

- **E-0002 (new):** Maimonides translation for print — Meszler CC-BY (recommended,
  needs an attribution line in credits — draft: "Maimonides translation by Rabbi
  Joseph B. Meszler, CC-BY, via Sefaria") vs CC0-with-typos. Decide by P7.
- **E-0001 (closed, review welcome):** licence scheme decided under delegation —
  veto window still open since nothing irrevocable was granted.

## Known limits (read before judging the chapter)

1. **Register is a first draft.** The prose aims at "poetic clarity, not essay" — your
   taste call on whether it lands is exactly what this review is for.
2. **Robustness profiles are provisional by design** — recurrence/diversity/spread are
   computed over a 33-unit corpus and say so on every claim. They harden at P4/P6.
3. **Russell's "outward interest" was cut** from the help page rather than printed
   unverified (no fetchable PD text yet despite US-PD status). The page leans on
   verified voices instead.
4. **The Qoheleth, tie-your-camel, and Faust voices appear as paraphrase/gloss**, not
   verbatim (copyright or verification state) — honest framing per R-T1.
5. **One chapter ≠ the book:** no front matter, no same-fork-at-altitudes device (needs
   other chapters), no cover. Those are P7 scope.
6. **Wave-2 landed but is unprocessed** — nothing in this chapter draws on it yet.

## Questions for Jason (the review)

1. Does the register land — serious, warm, not preachy? Where does it wobble?
2. Is the honesty apparatus (trust pills, asterisk card, lineage-vs-independence
   legend) illuminating or heavy? It can be tuned per page.
3. Fork selection: are these five the Building Years you'd map? What's missing?
4. The escalations above.
5. Any verdict on the visual system beyond the prototype's validation (the new forms:
   convergence map, threshold curve, columns, spectrum).
