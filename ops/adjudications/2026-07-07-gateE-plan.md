# Gate E — skeleton migration plan (resumable)

**Goal:** all 9 pages of the Building Years proof render through the traced model —
every claim-bearing string resolves from an approved assertion or is declared editorial;
every page emits a trace; the prohibited-phrase sweep and assertion/print gates guard all
of them. Then: frozen mini-release (edition bump, full QA view, metamorphic sample),
proposed to Jason as publish package #2.

**Mechanism (built first, commit 1):** `render_page` now supports `traced: true` pages —
`resolve_copy` walks the whole copy tree; `{assert: a-xxxx}` resolves through
`approved_assertion` (status + mandatory caveats), `{editorial: ...}` is declared voice,
bare strings outside FURNITURE_KEYS (eyebrow/title) fail the build. Quotes anywhere
(incl. inside form builders, e.g. comparison-columns `quote_ref`) land in the page trace
via `Graph.trace_sink`. Prohibited-phrase sweep runs over all non-assertion page text.

**Per-page procedure (the page-8 pilot pattern, ops/adjudications/2026-07-07-page08-pilot.md):**
1. Read the spec + its refs; classify each sentence: editorial voice / source-summary /
   relation-summary / historical-interpretive / quote.
2. For claim-bearing sentences: mint `a-####` assertions (kind, refs, mandatory_caveats,
   prohibited_phrasings, adjudication record in ops/adjudications/), or repair/weaken to
   honest editorial voice.
3. Rewrite the spec with wrappers + `traced: true`. Build; fix; commit per page or pair.
4. QA loop on the final render: rasterise + view every page.

**Page order (simple → hard) and status:**
- [x] by-080-help — traced-prose (Gate B pilot, done)
- [ ] by-090-close — prose, 2 refs
- [ ] by-010-opener — journey-map, editorial landmarks
- [ ] by-030-judgment — node-card, 2 refs
- [ ] by-070-suffering — node-card, 4 refs (PTG evidence strip — empirical caveats)
- [ ] by-060-time — comparison-columns, 4 refs (quote_refs inside figure)
- [ ] by-040-ambition — trade-off-spectrum, 4 refs (curdle notes are interpretive)
- [ ] by-050-money — threshold-curve, 3 refs (band label = evidence claim)
- [ ] by-020-carrying — convergence-map, 4 refs (independence labels = the hardest
      relation claims; needs dossiers like d-0001 per argued convergence)

**Assertion ID allocation:** a-0006 onward, sequential. Adjudication records:
ops/adjudications/2026-07-07-gateE-<page>.md (one per page or pair).

**Done means:** build fails on any revoked assertion / stripped caveat / prohibited
phrase / unverified quote on ANY page; 9/9 traces in book/page-traces/; edition bumped;
every rendered page viewed; metamorphic sample re-run; STATE + package #2 proposal.
