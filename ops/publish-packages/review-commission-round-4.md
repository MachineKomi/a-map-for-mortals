# External review commission — round 4 (against `building-years-v0.3.0`)

**Prepared:** 2026-07-18 · **Tag:** `building-years-v0.3.0` · **Reviewer:** Jason to commission
(external model / human auditor). This package is what the reviewer is pointed at.

## What changed since round 3 (the reviewer's baseline)

Round 3 (`review-feedback/2026-07-07-adversarial-review-round-3.md`) was adjudicated
substantially-conceded (`ops/adjudications/2026-07-07-external-review-round-3-response.md`).
Since then the recovery sequence (#2–#6) is **complete**:

1. **Confirmed bugs hardened + fixtures** (typed-ref resolution, structured rights gate,
   raw-claim/furniture ban, hash-bound approval; 20 fixtures + 14 gate tests).
2. **Gate C honestly re-run** (`ops/audits/2026-07-07-gateC-rerun.md`); translation attribution
   confirmed as the systemic weak layer.
3. **Gate D framed** (`docs/gate-D-corpus-claim.md`) — corpus-bounded language, no recurrence
   metric without a named frame + denominator.
4. **Stress-page rebuilds (#4) complete:** first-class fork objects (f-0001 time, f-0002 ambition);
   empirical dossier d-0002 backing the money page; page-5 competing-model chart (the one-curve
   defect fixed); page-4 fork redesign; fresh adversarial passes on pages 2/7/8
   (`ops/adjudications/2026-07-17-adversarial-passes-by020-by070-by080.md`).
5. **Hash-closed editions cut:** `building-years-v0.2.0` (chapter) and now `v0.3.0` (chapter +
   corpus-wide graph). Reproducibility verified (HTML byte-identical on re-render).
6. **Corpus-wide graph build (#6) complete:** S3 + S4 done.
   - **487 units → 484 claims** (481 singletons + 3 genuine merges). Every batch adversarially
     second-passed; one bad merge caught and split (Singer rescue principle).
   - **49 edges** (23 skeleton + 15 contest + 11 convergence). Intellectual-history layer built
     (`graph/intellectual-history.md`) as the transmission-evidence base. Convergence edges graded
     conservatively: no edge `strong`; transmission booked INFLUENCED not CONVERGES_WITH.

## What is under review

- **The graph build itself** — are the S3 clusters and S4 edges honest? Especially:
  - The 3 merges (c-0034 MacAskill longtermism, c-0310 Saadi Bani Adam, c-0313 Attar Simorgh) —
    genuinely the same proposition, or forced?
  - The convergence independence grades (all `partial`, none `strong`) — is the conservatism
    honest, or are Seneca↔impact-bias (e-0045) and Ubuntu↔Saadi (e-0047) under-graded?
  - The INFLUENCED bookings (e-0039 Harari←Vipassana, e-0042 Burkeman←Seneca, e-0044 Frankl←Stoic)
    — is the transmission evidence sound, or is any a real convergence mis-typed as transmission?
- **The chapter (unchanged since v0.2.0)** — re-confirm the round-3 repairs held; the chapter is
  byte-identical so any round-3 finding that's still open is still live.
- **The intellectual-history layer** (first cut) — are the transmission channels documented or
  asserted? (One channel — Thoreau↔French moralists — is flagged unattested-in-corpus.)

## Known-weak / honest limits (not hidden)

- **Wave-3 claims are `attested` / `pending-primary`** — insights reach a page only as paraphrase,
  never verbatim (in-copyright discipline held). None are print-gate candidates.
- **Robustness profiles are provisional** ("corpus-wide S3 in progress" bases) — the corpus-wide
  recurrence/diversity/temporal ratings need a refresh now that S3 is done. This is debt, not a
  claim of completion.
- **6 S4 candidates were rejected as NO-EDGE** because the ancient endpoint claims don't exist yet
  (memento-mori, phronesis, ancient cosmopolitanism, etc.) — deferred to a depth pass.
- **The chapter draws only on the 33 skeleton claims** (c-0001..c-0033); the 451 new claims
  (c-0034..c-0492) are in the graph but not yet rendered in any page. Curation (P6/P7) is the
  next phase.
- **e-0040 was re-routed** (Schopenhauer/modern → Epicurean/ancient) and **e-0048's notes** had
  an inverted comparison — both fixed, but flagging that the convergence edges are fresh and
  adversarially-reviewed once, not repeatedly stress-tested.

## Focused questions for the reviewer

1. **S3 honesty:** is the singleton-heavy clustering (481/484 singletons) defensible, or is it
   under-merging distinct attestations of the same claim? Where would you force a merge?
2. **S4 independence grading:** is "no edge `strong`, transmission→INFLUENCED" the right default,
   or is it systematically under-claiming robust convergence? Specifically e-0045 / e-0047.
3. **Wave-3 claim-type discipline:** spot-check that interpretive/observational claims were not
   laundered as empirical (the reports were disciplined; verify it held through clustering).
4. **Anything from round 3 still live** in the (unchanged) chapter that the recovery didn't reach.

## How to run it

```bash
git checkout building-years-v0.3.0
python tools/validate_graph.py      # 0 err/0 warn expected
python tools/validate_units.py graph/units/ graph/claims/   # 0 err, 17 counted warnings
python tools/tests/run_fixture_tests.py  # 20/20
python tools/tests/run_gate_tests.py     # 14/14
cd book/generator && python build_book.py  # renders 9 pages; HTML hash in the manifest
```

The edition manifest (`graph/editions/building-years-v0.3.0.yaml`) records every ingredient's
sha256 — any drift since the tag is detectable.
