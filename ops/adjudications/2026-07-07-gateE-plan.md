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
- [x] by-090-close — done (a-0006/a-0007 + i-0025a; intent claim repaired)
- [x] by-010-opener — done (corpus-bounded the 'wise disagree' claim)
- [x] by-030-judgment — done (a-0008..a-0010; card labels store-derived; camp detail removed)
- [x] by-070-suffering — done (a-0011..a-0016; Frazier design error repaired)
- [x] by-060-time — done (a-0017..a-0019)
- [x] by-040-ambition — done (a-0020..a-0022; ungrounded flourish dropped)
- [x] by-050-money — done (a-0023..a-0025; causal/threshold conflation repaired)
- [ ] by-020-carrying — IN PROGRESS: drafts a-0026..a-0028 under fresh-context
      adversarial review (the argued-convergence page — round-1's faulted claim class)

**Assertion ID allocation:** a-0006 onward, sequential. Adjudication records:
ops/adjudications/2026-07-07-gateE-<page>.md (one per page or pair).

**Done means:** build fails on any revoked assertion / stripped caveat / prohibited
phrase / unverified quote on ANY page; 9/9 traces in book/page-traces/; edition bumped;
every rendered page viewed; metamorphic sample re-run; STATE + package #2 proposal.
