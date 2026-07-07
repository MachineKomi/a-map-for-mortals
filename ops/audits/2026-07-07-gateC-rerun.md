# Gate C — honest rerun (round-3 P0-1)

**Supersedes** `2026-07-07-gateC-results.md`, whose "no quarantines" conclusion is **withdrawn**.
The original applied the predeclared 5%/report material-error threshold to the *post-repair,
post-lead-adjudication* state — which converts an independent stop-rule into a discretionary
score and lets defects be zeroed by fixing or relabelling them. Per the review's repair, this
rerun (a) preserves the auditors' first-pass verdicts immutably, (b) reports **observed
pre-repair** and **residual post-repair** rates, (c) applies quarantine to the **pre-repair**
rate, and (d) treats a false structured field (e.g. a wrong `source.translator`) as MATERIAL
even where the unit is not print-ready and even where uncertainty is noted elsewhere.

## The two rates, per report (auditors' first-pass materiality = "observed")

| Report | Sampled | Observed material (auditor first pass) | Pre-repair rate | Lead overturn | Residual (post-adjudication) | Threshold (>5%) |
|---|---|---|---|---|---|---|
| w1 02-greco-roman | 3 | 0 | 0% | — | 0 | pass |
| **w1 03-nietzsche** | 2 | 2 (u-0057, u-0065 — translator credited ≠ held wording) | **100%** | none | 0 (both fixed to the PD translator's verbatim) | **QUARANTINE** |
| w1 05-near-eastern | 4 | 0 | 0% | — | 0 | pass |
| **w1 06-modern-west** | 7 | 1 (u-0120 — held French may be a back-translation; Pascal-misattribution risk) | **14%** | none | 1 still open (Gate F primary check owed) | **QUARANTINE** |
| w1 07-literary | 3 | 0 (Kretzmer is the intentional apocryphal exhibit) | 0% | — | 0 | pass |
| w1 08-empirical | 3 | 0 | 0% | — | 0 | pass |
| **w2 01-eastern** | 3 | 1 (u-0200 — attributed `attested` while report said quarantine; paraphrase-as-synthesis) | **33%** | **yes** (tie-break: NON-MATERIAL — quotation is null so nothing publishable; `attested` is *weaker* than the report's `probable`) | 0 | **QUARANTINE on observed rate** (overturn disclosed) |
| w2 02-african | 1 | 0 | 0% | — | 0 | pass |
| w2 03-indigenous | 5 | 0 (stub discipline verified) | 0% | — | 0 | pass |
| w2 04-womens-voices | 4 | 0 | 0% | — | 0 | pass |
| w2 05-childhood | 2 | 0 | 0% | — | 0 | pass |
| **w2 06-persian** | 7 | 2 (u-0285 edition unpinned; u-0287 fork-structure at field level) | **29%** | partial (u-0287 argued an S3 clustering matter, not minted-data) | u-0285 fixed → verified-primary; u-0287 open | **QUARANTINE** |
| w2 07-practical-strategic | 5 | 0 (2 conditional flags, since discharged: u-0319 verified) | 0% | — | 0 | pass |
| **w2 08-folk-proverbial** | 2 | 1 (u-0345 — `endorsement: n/a` where the source *undercuts* the proverb) | **50%** | **yes** (tie-break: NON-MATERIAL narrow — first-attestation is conventional; posture was declared in notes) | 0 (endorsement re-derived `undercut`, attribution `communal`) | **QUARANTINE on observed rate** (overturn disclosed) |

## Result (the honest one)

**Five reports breach the predeclared threshold on the observed pre-repair rate**, not zero.
- **Three quarantine on findings the lead did NOT overturn** — w1 03-nietzsche, w1 06-modern-west,
  w2 06-persian — all in or adjacent to the translation-attribution weak layer the review named.
  These get **full-batch re-audits** (03-nietzsche = 19 units, 06-persian = 25 units dispatched
  2026-07-07; 06-modern-west = queued).
- **Two more trigger on the observed rate but the lead overturned the single finding** (w2
  01-eastern u-0200; w2 08-folk-proverbial u-0345). Both overturns are defensible and their full
  reasoning is preserved verbatim in `2026-07-07-gateC-results.md` and the by020 tie-break record —
  but per the review's rule they are disclosed as **lead overturns**, not silently zeroed, so a
  reader can judge whether the calibration is being gamed. A lead-overturn rate this high on a
  small sample is itself a signal: the materiality definition needs the sharper form below.

## Materiality definition, corrected (was a loophole)

Old: "declared uncertainty is non-material." That let a note neutralise a contradictory structured
field. New, in force:
- A **false or misleading structured field** (wrong `source.translator`, `endorsement`, edition,
  attribution tier presented as stronger than the evidence) is **MATERIAL**, regardless of notes.
- **Correctly-structured** uncertainty (e.g. `quotation: null`, `verification.status:
  pending-primary` with an honest method) **mitigates severity** but does not itself create a defect.
Under this definition u-0200's overturn stands (its fields were honest; quotation null), while
u-0057/u-0065 were correctly MATERIAL (the translator field was false).

## Immutable first-pass verdicts

The seven original auditors' per-unit verdicts are session artefacts (subagent transcripts). This
rerun records their materiality calls in the table above as the immutable observed layer; going
forward, per-unit first-pass verdicts (category, severity, field, rationale, auditor, timestamp)
must be **committed** at audit time, not only summarised — that process gap is itself a Gate C
finding and is fixed for the triggered-batch re-audits now running (their full per-unit tables
will be committed).

## Triggered full-batch re-audits (the quarantine paying off)

Fresh-context full re-audits of the triggered batches. **They found real defects the 10%
sample missed — which is exactly the point of the quarantine rule the original run bypassed.**

### w1 03-nietzsche (19 units) — 2 NEW material defects found, both remediated
- **u-0058** (eternal recurrence, GS §341): `translator: Thomas Common` was FALSE — held wording
  is a Kaufmann-style rendering (modern "you", not Common's "thou/thee"). The unit's own notes
  already conceded "does not read like Common" yet left the field standing. **Fixed:** translator
  → null, copyright_flag → in-copyright, Gate F line-match owed.
- **u-0060** (perspectivism, GM III §12): `translator: Horace B. Samuel` was FALSE — held wording
  is Kaufmann-style, not Samuel's 1913 diction. **Fixed:** same remediation.
- Minor/print-blocking (no false field, honestly null — Gate F flagged, not "fixed"): u-0068,
  u-0073 hold likely-Hollingdale (in-copyright) *Untimely Meditations* wording with translator null.
- Needs-primary (Gate F): u-0058/59/60/61/67/68/70/72/73 (9). CARE/endorsement clean across the batch.

### w2 06-persian (25 units) — 1 material-borderline + 1 escalated-minor, both remediated
- **u-0303** (Saadi, Gulistan): `translator: James Ross 1900` was an unverified field carrying a
  **public-domain determination** — the report only nominated Ross; the held wording is the
  Gladwin/Rehatsek-lineage phrasing shared across several PD translations. **Fixed:** translator →
  null; copyright_flag KEPT public-domain (all candidate translators are PD, so PD-in-outcome is
  safe) with the identity unresolved until Gate F.
- **u-0302** (Saadi, Bani Adam): `translator: Dick Davis 2002` does not match the held English.
  **Fixed:** translator → null; copyright_flag kept in-copyright (conservative → no print consequence).
- The FitzGerald–Khayyam units (u-0285–0288) were handled correctly (FitzGerald credited as author
  not Khayyam; `dubious`; edition numbers pinned; mandatory display tag). Zoroastrian eschatology
  tagged metaphysical/normative, never empirical. The batch was **stronger** than the weak-layer
  prior predicted.

### w1 06-modern-west (53 units) — full re-audit DISPATCHED (in progress)
Triggered by u-0120. Focus: the u-0104–u-0148 discovery-corpus subset (u-0013–u-0025 already
S2-verified). Results and remediation to be appended.

## What the quarantine mechanism proved
The 10% sample found u-0057/u-0065 in Nietzsche; the full re-audit found **u-0058 and u-0060 too** —
a 2× undercount in that batch. This is direct evidence that the original "apply threshold
post-repair, no quarantines" method was not just procedurally invalid but **materially
under-counted** the defect rate. The corrected rule (quarantine on observed pre-repair rate, then
full re-audit) is doing what it exists to do.

## Consequence for the ledger

STATE.md already carries Gate C as **invalid / rerun required**; this file is that rerun's spine.
The rerun is not itself complete until the triggered full-batch re-audits return and their material
units are repaired or dropped. **Gate C stays open** until then. No recurrence/coverage metric may
be reported off this corpus in the meantime (also gated by Gate D being undone).
