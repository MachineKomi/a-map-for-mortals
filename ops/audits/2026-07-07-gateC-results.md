# Gate C stratified audit — results and adjudication

**Date:** 2026-07-07 · **Manifest:** `ops/audits/2026-07-07-gateC-sample.yaml` (51 units, deterministic sha256 seed `gateC-2026-07-07`, ceil(10%)/report + all dubious/apocryphal/record-only oversampled)
**Predeclared threshold:** material error rate > 5% of a report's sampled units in any category → quarantine and full re-audit of that report's batch.
**Definition in force:** MATERIAL = a defect in the minted unit that would mislead a reader or corrupt counts — *excluding* uncertainty already declared inside the unit itself.

## Who judged what (per CLAUDE.md §4)

- **First pass:** seven fresh-context subagent auditors (shared weights with the lead — disclosed), each covering one stratum, six-category charter (wording-fidelity, paraphrase-fidelity, label-defensibility, attribution-posture, locator-accuracy, care/endorsement-discipline).
- **Adjudication:** lead agent, verifying every flagged finding against the unit files and reports before accepting it.
- **Tie-break:** where lead and auditor diverged on materiality (u-0200, u-0345), a fresh-context subagent with an adversarial charter — instructed to *uphold the auditors' MATERIAL verdicts against the lead* — gave the deciding pass (shared weights disclosed). No verdicts were blended; diverging readings are preserved below.

## Results by report

| Report | Sampled | Auditor-proposed material | Adjudicated material | Rate | Action |
|---|---|---|---|---|---|
| w1 02-greco-roman | 3 | 0 | 0 | 0% | pass |
| w1 03-nietzsche | 2 | 2 caveats (u-0057, u-0065) | 0 — declared verification debt, **now discharged** (both verified-primary this session) | 0% | pass |
| w1 05-near-eastern | 4 | 0 | 0 | 0% | pass |
| w1 06-modern-west | 7 | 1 (u-0120) | 0 — risk was already declared in-unit; flag moved into the verification block; Gate F priority | 0% | pass |
| w1 07-literary | 3 | 0 (intentional Kretzmer apocryphal exhibit only) | 0 | 0% | pass |
| w1 08-empirical | 3 | 0 | 0 | 0% | pass |
| w2 01-eastern | 3 | 3 issues on u-0200 | 0 — tie-break: NON-MATERIAL (clear) | 0% | pass |
| w2 02-african | 1 | 0 | 0 | 0% | pass |
| w2 03-indigenous | 5 | 0 (stub discipline verified) | 0 | 0% | pass |
| w2 04-womens-voices | 4 | 0 | 0 | 0% | pass |
| w2 05-childhood-old-age | 2 | 0 | 0 | 0% | pass |
| w2 06-persian | 7 | 2 (u-0285, u-0287) + 1 minor (u-0298) | 0 — u-0285 declared and **now discharged** (verified-primary); u-0287 schema misread; u-0298 unrepairable without fabrication | 0% | pass |
| w2 07-practical-strategic | 5 | 0 (2 conditional flags, already declared) | 0 | 0% | pass |
| w2 08-folk-proverbial | 2 | 1 (u-0345) | 0 — tie-break: NON-MATERIAL (narrow), mandatory repairs executed | 0% | pass |

**No batch exceeds the predeclared threshold. No quarantines.** Auditors proposed material findings on 5 units; each was adjudicated against the files before the threshold was applied, and the two genuinely contested calls went to the adversarial tie-break rather than being settled by the lead alone.

## Diverging verdicts, preserved (never blended)

### u-0200 (Nagarjuna, MMK) — auditor: MATERIAL ×3; tie-break: **NON-MATERIAL (clear)**
Auditor: "attribution_confidence = 'attested' is inconsistent with report's 'QUARANTINE' label… Would mislead a reader into treating an unverified claim as attested."
Tie-break: "every charged defect is an *in-band declared uncertainty*, which the definition in force expressly excludes. `quotation: null` — there is literally no wording that could mislead or reach print… `attested` *means* 'asserted by a report; plausible; unchecked' — it is weaker than the report's 'probable', not stronger… The auditor's 'not publication-ready' charge applies a print-gate standard to an S1 discovery record."
Repair executed regardless: editorial meta-commentary ("deliberately apophatic and heavily contested") stripped from `paraphrase` (already carried in notes and `conditionality: contested`).

### u-0345 (Sandys / "honesty is the best policy") — auditor: MATERIAL; tie-break: **NON-MATERIAL (narrow)**
Auditor: "Type = Virtue implies endorsement; report context shows Sandys is reporting/critiquing the proverb, not endorsing it… may mislead a reader about the unit's epistemic status."
Tie-break: "the auditor identified a genuine field-discipline defect, but it is declared in-unit and conventional in form; it demands repair, not batch quarantine… Had the caveat not been in the unit, I would have upheld MATERIAL."
Mandatory repairs executed: paraphrase re-subjected to the proverb; `endorsement: n/a` → `undercut` (machine-readable source posture); `attribution_confidence: attested` → `communal` (matches the sibling proverb units; Sandys retained as first-attestation locator).

### u-0287 (FitzGerald determinism) — auditor: MATERIAL; lead: **NON-MATERIAL** (adjudicated directly)
The auditor asked unit fields to encode the two-pole fate-vs-will fork. Forks are modelled at claim/edge level (METHODOLOGY §3); wave-2 units have `claim_id: null` because S3 clustering has not run. The unit already carries `conditionality: contested`, `endorsement: ambiguous`, `attribution_confidence: dubious`, and the ZO-01 opposition in notes. Follow-up queued: mint the IN_TENSION_WITH edges for the ZO-01 ↔ FE-02 ↔ KH-03 ↔ MU-02 cluster at S3.

## Verifications performed as audit follow-ups (evidence in the unit files)

1. **u-0285** (FitzGerald quatrain XII): held wording matched verbatim against the Fifth Edition text in Gutenberg #246; 1st-ed. variant confirmed (and corrected: it is quatrain **XI** there, not XII). → `verified-primary`.
2. **u-0057** (Nietzsche, amor fati): the report's English was confirmed as Kaufmann-like, **not** the credited Common — replaced with Common's verbatim from Gutenberg #52124 (dropped wording preserved in `verification.method`). → `verified-primary`.
3. **u-0065** (Nietzsche on Goethe): the report's English matched no PD edition — replaced with Ludovici's verbatim from Gutenberg #52263 (OCR artefacts retained as-transcribed and flagged). The report's "last German before whom I feel reverence" is a Kaufmann-style rendering absent from Ludovici (§51 reads "whom I respect") — noted in-unit. → `verified-primary`.

## Systemic findings

1. **Translation attribution is confirmed as the corpus's weak layer.** Three of three flagged quotation_translations turned out to be a *different translator's* rendering than the one credited (u-0057, u-0065, and previously the wave-1 S2 batch). **Binding consequence for Gate F:** every `quotation_translation` must be line-matched against the *named* translator's text before any status above `pending-primary`; a mismatch is repaired by substituting the named PD translator's verbatim, never by re-crediting to match the held wording.
2. **The S1 'probable'→'attested' normalisation confused two independent auditors**, who read `attested` as stronger than the report's label. The rule is documented and uniform, and `attested` is the *weaker* tier, so no repair mid-audit — but the recurring misreading is recorded as a schema-usability debt for the next schema pass (candidate: carry `report_label` as a structured field rather than notes-only).
3. **Source posture must be machine-readable.** u-0345 showed that a fields-only consumer can misread a unit whose posture lives in notes. Adopted as a rule (see DECISIONS 2026-07-07): where a source attests wisdom it does not endorse, the `endorsement` enum (`undercut`/`complicated`) must say so; notes are context, not the record of posture.

## Follow-up queue

- **Gate F priority:** u-0120 (locate Joubert's French in a primary Pensées edition — drop the quotation if unlocatable; Pascal-misattribution watchlist), u-0319 (capture Jacobs 1892 Maxim 130 verbatim), u-0200 (pin MMK verse against Garfield print — drop, don't downgrade, if it fails, per report), u-0298 (verse anchor for Zuhayr's muʿallaqa).
- **S3:** mint the fate-vs-will tension edges (ZO-01 ↔ KH-03 cluster); consider the honesty-vs-tact fork with u-0345 as the honesty pole.
- **Minor, no action:** u-0118 claim_type divergence (documented re-derivation), u-0339 popular-variant order reversal (original order held; variant noted in report).

## Honest scope

This audits 51 of 346 units (14.7%), stratified with risk-tier oversampling. A clean result bounds, not eliminates, the mint-error rate; the oversampled dubious/apocryphal/record-only tiers all passed, which is the strongest signal in the sample. Auditor raw outputs are session artefacts (subagent transcripts), not repo files; their verdicts are quoted verbatim above where they diverged from the adjudication.
