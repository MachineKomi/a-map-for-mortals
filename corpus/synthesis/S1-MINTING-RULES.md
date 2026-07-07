# S1 Minting Rules (P4 scale ingestion) — binding for every minting agent

Read first: `graph/units/u-0000-EXAMPLE.yaml` (normative format — match field-for-field;
do NOT include `example: true`; set `claim_id: null`). Your assignment (report, rid→uid
mapping) is in `corpus/synthesis/ingest-manifest-p4.yaml`. The rid identifies the unit
in the SOURCE REPORT — mint from the report's full unit block, not from the extract
(the extract is only the index).

## The honesty contract (non-negotiable)

1. **`attribution_confidence: attested` for everything** regardless of the report's
   label (reports are claims about sources; S2 climbs). Exceptions: keep the report's
   own `dubious`/`apocryphal` where given; use `communal` for proverbs/oral units
   attributed to a people or language. Record the report's original label in `notes`.
   `verification: {status: pending-primary, method: "attested by wave-N report; wording
   not yet checked against a primary edition", checked_against: null, date: null}`.
2. **Re-derive labels** (type, register, claim_type, polarity, conditionality,
   life_domains, life_stages) from the report's own quoted evidence — never copy its
   labels blindly. Where your judgment differs, keep yours and note the difference.
   Claim-type discipline: religious/metaphysical claims are never `empirical`;
   observational generalisations are not `prudential` advice; realpolitik counsel from
   the strategic stream keeps the report's cautionary/descriptive framing.
3. **`paraphrase` is a normative act:** neutral, one line, preserve conditionality,
   don't smooth hard claims, don't Westernise, add nothing to anyone's mouth.
4. **`quotation` / `quotation_translation`: copy the report's wording EXACTLY** —
   never improve, complete, or invent. Original language into `quotation` when held;
   English into `quotation_translation`. If the report holds no wording, null with an
   inline comment. If the report itself flags a wording as paraphrase-pending, keep the
   flag in `notes`.
5. **`source`**: author (or people/language for communal units), work, passage (the
   precise locator), translator, edition_year, language, url (only if the report gives
   one), urn: null. Unknown stays null — never supplied from memory.
6. **`copyright_flag`**: public-domain only where the report establishes the quoted
   wording's edition is PD; in-copyright where it says so (incl. CC-BY-NC); unknown
   otherwise. CC-BY material: in-copyright + licence note in `notes`.
7. **`endorsement`** for literary/character speech: carry the report's label
   (endorsed|complicated|undercut|ambiguous) and put speaker + dramatic context in
   `notes`. Non-literary: `n/a`.
8. **Empirical/evidence units**: type per function (Consequence/Practice/Danger),
   claim_type: empirical, polarity: descriptive, no quotation (nulls), source = lead
   citation, copyright_flag: unknown + "no verbatim quotation held", and `notes` MUST
   carry evidence grade, replication status, and effect sizes exactly as the report
   gives them.
9. **CARE flags (Indigenous units — check the extract's `care` field):**
   - `care-flag` (sacred/restricted): mint a RECORD-ONLY STUB — no quotation, the
     paraphrase records the tradition's existence and scope only, and `notes` begins
     "RECORD-ONLY (CARE): content deliberately not extracted; sacred/restricted."
   - `consent-gate`: mint normally but `notes` begins "CONSENT GATE: do not publish
     before a community-source consent audit (see ops/DECISIONS.md 2026-07-08)."
10. **`prov`**: {source_report: <path>, extracted_by: "claude-code:s1-p4-v1", pass: 2,
    date: 2026-07-08}.
11. **`notes`**: report's confidence label; misattribution-watchlist relevance;
    re-derivation differences; translation/copyright caveats. Terse but complete.

## After writing your batch

Run `python C:\a-map-for-mortals\tools\validate_units.py` on your files (pass all
paths). Fix errors. Return ONLY: validator output + re-derivations that differed +
difficulties. Do not commit — the coordinating session commits per batch.
