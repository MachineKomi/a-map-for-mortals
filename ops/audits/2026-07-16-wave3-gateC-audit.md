# Gate-C-style audit — wave-3 minting (u-0347..u-0487)

**Date:** 2026-07-16
**Scope:** S1 spot-check of the 141 wave-3 "modern thinkers" units minted this session.
**Method:** fresh-context adversarial auditor (subagent), charged to find defects, NOT to
rubber-stamp. 28 units audited (~20% of batch, double the 10% floor) across all 5 reports,
each checked against its source report block. Plus batch-wide automated scans on every unit
for `copyright_flag`, `attribution_confidence`, `verification.status`, misattribution-watchlist
phrases, and claim-type laundering.

**Disclosure (§4 anti-bias):** the auditor shares model weights with the minting agents
(`claude-code:s1-wave3-v1`). It cannot rule out shared blind spots (a consistent error both
would make identically). Mitigation: every check was mechanical where possible — verbatim-quote
comparison against the report's `original_quote` strings and literal field-by-field claim_type/
conditionality comparison against the report's enumerated values. Disclosure recorded in the
audit and carried into this file.

## Result

**Zero material defects.** No honesty-contract field is wrong in a way that launders a
normative claim as empirical, drops a load-bearing qualifier, fabricates a quote,
misattributes, or breaks copyright discipline.

**Batch-wide discipline (141/141 each):**
- `copyright_flag: in-copyright` — compliant
- `attribution_confidence: attested` — compliant
- `verification.status: pending-primary` — compliant
- No verbatim-print candidates (all 45 non-null `quotation_translation` values are coined
  terms / single short famous formulations whitelisted by the reports)
- `prov.source_report` paths correct; per-report counts 28/16/39/32/26 = 141 exact

**Sensitive-target spot checks (all PASS):**
- u-0350 (Harari "biggest fraud") — observational/contested, NOT empirical ✓
- u-0365 (Chira/Botero/Gray) — genuinely empirical ✓
- u-0382 (Ord 1-in-6) — empirical estimate, heavily caveated ✓ (post-audit: added the
  business-as-usual ~1-in-3 "two bullets" clarification to notes)
- u-0416 (Haidt great-rewiring) — empirical/contested, "do NOT present as established" ✓
- u-0421 (Odgers critique) — dissent preserved first-class ✓
- u-0460 (Singer disability) — normative, "argued and widely rejected, not fact", dissent central ✓
- u-0469 (social priming retraction) — empirical, retraction carried ✓
- u-0484 (positivity ratio retraction) — empirical, retraction carried ✓

**Dissent preservation (all first-class, none blended):**
Torres longtermism critique (u-0389); Odgers/Orben-Przybylski/Ferguson/reporting-artifact
(u-0421/0422/0423/0424) modeling the teen-mental-health debate as live two-sided; Singer
disability-rights dissent (u-0460); EA critique cluster (u-0459).

## Minor issues (enum-flattening, not honesty breaches)

1. **`conditionality` enum lacks `speculative`/`robust`** → those report grades collapse to
   `conditional` (the only honest fit in the 3-value enum). Affected ~12 units. In every case
   the richer wording is preserved in `notes`. The two retraction units (u-0469, u-0484) are
   the clearest loss: the report said `robust` (the *retraction* is robust), unit says
   `conditional`. No information lost, but the structured field is flatter than the report.
   *Deferred to a methodology decision:* consider adding `robust`/`speculative` to the enum.
2. **Batch-level `attested` overrides finer report grades** (u-0372 medium, u-0424 medium-high,
   u-0480 medium) — finer grade preserved in `notes`. Internally consistent with the batch rule.
3. **u-0451 (Appiah fallibilism)** — report's longer attributed gloss trimmed to bare term in
   `quotation_translation`. Conservative; gloss carried in paraphrase.

## Verdict

**PASS — fit to merge subject to primary-source verification at the print gate**, exactly as
the `pending-primary` flags promise. The honesty contract held; no S1 rework required. The
single post-audit fix (u-0382 notes) is applied. Enum-flattening debt is recorded for a
methodology decision, not a blocker.
