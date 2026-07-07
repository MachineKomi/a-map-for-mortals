# Adjudication — external review round 3 (traced proof + Gates A–E)

**Review file:** `review-feedback/2026-07-07-adversarial-review-round-3.md` · **baseline `d854b6b`**
**Adjudicator:** Claude Code (lead). **Verification-first:** every falsifiable charge below was
checked against the repo or the primary source *before* a verdict was written. Where I concede,
I say so plainly; where I push back, I give the evidence. Per the never-blend rule, the review's
wording and my verdict both stand.

## Headline verdict

**The review is substantially correct, and its central charge is upheld: infrastructure that
places strings in containers was reported as proof that content is graph-gated and
re-adjudicated. It is not. "A traced overclaim is still an overclaim" is exactly the project's
own fixed star, turned on my own status claims — and it lands.** I concede all seven P0s in
substance (two with scope notes), most P1s, and I am withdrawing the "Gate C complete — no
quarantines" and "Gate E complete" claims. Three charges were factually verified this session:

- **P0-2 confirmed:** `ops/adjudications/2026-07-07-gateE-by040-050.md` does not exist; a-0020…a-0025
  and the by-040/by-050 specs all cite it. The validator passed because it only checks that
  `adjudication_refs` is non-empty.
- **P0-5 confirmed:** `printable_quote()` uses `"cc-by" in notes.lower()` — u-0012's notes contain
  both "CC-BY-NC" and "CC-BY"; the gate cannot tell them apart. Fail-open.
- **P0-6 confirmed against the primary paper** (Frazier 2009, doi:10.1111/j.1467-9280.2009.02381.x,
  abstract fetched this session): interval **is** two months; n=122 **is** the trauma-exposed
  analytic group. My "repair" (a-0015) dropped the real two-month interval and asserted a false
  narrative that "two-month" belonged to the habit study. **One of the five "defects caught" at
  Gate E was itself a false correction produced by trusting the report over the primary source.**
  This must be corrected publicly, not silently.

## Per-finding adjudication

### P0-1 — Gate C zeroed the errors it measured · **CONCEDE**
The threshold was applied post-repair, which converts an independent stop-rule into a discretionary
score. A wrong `source.translator` field is a false structured assertion (a material minted-data
defect), not "declared uncertainty" — a note cannot neutralise a contradictory structured field.
On the sample, wave-1 Nietzsche shows 2/2 translation mismatches — far over the 5% pre-repair
threshold; that batch (and any similarly triggered batch) must be quarantined and re-audited.
**Action:** rerun Gate C reporting two rates (observed pre-repair / residual post-repair); apply
quarantine to the pre-repair rate; redefine materiality (correctly-structured uncertainty may
mitigate severity; a false structured field remains a defect); preserve immutable per-unit
first-pass verdicts; report lead-overturn rates. Until then the "no quarantines" claim is withdrawn.

### P0-2 — dangling adjudication references · **CONCEDE (confirmed)**
Reopen Gate E for pages 4 and 5; treat them as never independently adjudicated (do not reconstruct
the missing file from memory); make the validator resolve every typed ref (`adjudication_refs`,
`relation_refs`, `interpretation_refs`, `dossier_ref`, `evidence`) and add a dangling-ref fixture.

### P0-3 — "approved" is mutable metadata · **CONCEDE**
Approval is bound to nothing; deleting a caveat from *both* the list and the text passes the build;
any string starting `approved-` passes. **Action:** hash-bound approval objects (assertion content
hash + edition ref); the generator accepts only an approval whose hash matches the live assertion;
enum, not prefix test; approval is edition-specific. Add fixtures for content-changed-after-approval
and policy-deleted-with-protected-wording.

### P0-4 — traceability mistaken for evidentiary support · **CONCEDE, with one scope note**
- `card_claim` and `{claim}` render raw legacy-claim text after only a `status: adjudicated` check —
  remove those publication paths; a raw claim may inform an assertion but not render.
- `{editorial:}` is an unchecked escape hatch recording only a char count — must classify content and
  store the exact rendered text (or a content hash) in the trace.
- Titles/poles whitelisted as furniture while carrying claims ("The weight is partly a verdict",
  "Raising others without owning them") — reclassify; furniture = identifiers with no propositional
  content only.
- Editorial voice is not visibly marked to the reader — a backend flag does not satisfy "visibly
  separate"; add a reader-facing marker.
**Scope note (not a pushback on direction):** the book legitimately *has* an editorial voice
("this book's editorial eye"). The fix is not "every sentence becomes a premised assertion" but:
(a) a visible editorial marker, (b) promote any editorial string carrying an empirical/historical/
attributive/interpretive claim to a `basis: editorial` publication assertion with scope, while
genuinely non-propositional connective tissue may remain editorial. I adopt the reviewer's
mechanism and this calibration together.

### P0-5 — print-rights gate is fail-open · **CONCEDE (confirmed)**
Replace the substring test with field-specific structured rights (SPDX id, licence URL, licensor,
commercial_use, attribution text, modifications, checked_at); the renderer whitelists compatible
SPDX ids and emits the credit; quotes reference a specific expression/unit id, not a claim
first-member. Add the CC-BY-NC / "not CC-BY" / licence-on-wrong-field / missing-attribution fixtures.

### P0-6 — the empirical correction record contains a new factual error · **CONCEDE (confirmed vs primary)**
Correct publicly: the verified Frazier design is a **two-month prospective interval, undergraduate
sample, n=122 trauma-exposed analytic group**; the ~1,500 recruitment figure is not in the abstract
and was report-carried — it must not be stated as fact. Restore the two-month interval; keep
"measurement caution, not a verdict on every survivor's report." Amend a-0015, its notes, the Gate E
plan, package 2, `STATE.md`, and the "five defects caught" narrative (it is four caught + one
self-inflicted-then-now-fixed). Replace bare "grade B/C" with a dossier summary.

### P0-7 — page 5 repeats the 2024 quantile overreading · **CONCEDE**
"unhappiest ~15–20%: flattens" presents a conditional-quantile result as a subgroup of people —
Rohrer & Wenz 2024 is precisely about that identification problem, not a generic causal caution.
Use "15th conditional quantile" language; show the competing model (Bennedsen 2024 ~ $200k) or a
comparison form, not a single authoritative curve; change the title to association language; remove
"the old claim survives" (income↔well-being cannot test Schopenhauer's "what one is" comparative
claim). Rebuild page 5 from an empirical dossier with three rows (KKM 2023 / Rohrer-Wenz 2024+reply
/ Bennedsen 2024). This is the second v0.4 stress page.

### P1 — no first-class forks · **CONCEDE**
Implement the fork object (question, poles, protects/costs, conditions, actor/context/outcome/horizon,
counterexamples, danger conditions, per-consequence evidence). Pilot on page 6 (needs genuine tension
+ conditional counsel). For page 4, drop the single striving/contentment axis in favour of "when does
striving serve the life vs postpone it" (two-axis / comparison) so Faust, Thoreau, Pascal and Qoheleth
occupy distinct positions.

### P1 — registry false precision · **CONCEDE the overclaim; KEEP the artifact**
The tradition field mixes schools/religions/peoples/languages/regions/genres/periods/method on one
axis; "118 controlled IDs under 18 families" oversold an alias table as an analytic ontology. I keep
the mapping as a **migration alias table** (it is still the right freeze mechanism and the reviewer
concedes it is an improvement) and stop calling it a coverage ontology; recurrence/independence must
use argued source-family components, not raw or canonical tradition counts. Typed facets + canonical
entity records are the correct next step, queued, not claimed done.

### P1 — adversarial protocol not applied at the publication gate · **CONCEDE**
Only by-020 got a genuine fresh adversarial pass; the rest were lead-only, and an edge being sound is
a different question from whether page wording/selection/design mislead. Role-specific passes owed:
page 5 (empirical methodologist + publication adversary), page 7 (empirical + trauma-informed), page 2
(conceptual + genealogy + publication adversary), page 9 (literary/source critic + publication
adversary). Persist full verdicts, not accepted-edit summaries.

### P1 — no frozen edition / reproducible trace · **CONCEDE**
`graph/editions/` is empty, no git tag, no hashes; traces point to mutable IDs and omit exact editorial
text. Cut a real edition manifest (all included object ids; SHA-256 of every dependency and rendered
block; git commit + tag; generator/Python/WeasyPrint/font hashes; PDF hash; QA image hashes + inspector/
date/outcome; open escalations + known limits). Rebuilding the tag must reproduce the trace and a
materially identical PDF.

### Ledger inconsistencies · **CONCEDE**
`STATE.md`/`README.md` point to deleted `building-years-v0.1.0.pdf`; README claims "adversarial second
pass at every interpretive gate" (contradicted by the Gate E records) and "every unit/claim/edge records
who judged it and how much to trust it" (untrue for the transitional set). Correct all three.

### Gate D · **CONCEDE — it was skipped**
A→B→C→E skipped Gate D ("corpus claim defined: discovery vs validation frames; bounded metrics only").
No validation frames or corpus-claim protocol exist. Mark D not-done; close it before any recurrence
metric is reported.

## Where I calibrate rather than fully concede
1. **Registry (P1):** keep the alias table; drop the ontology framing. Not "it was worthless" —
   "it was oversold." The reviewer agrees it is an improvement.
2. **Editorial classification (P0-4):** adopt the mechanism, but the book keeps a marked editorial
   voice; the fix is classify-and-mark, not abolish. (Mechanism-level agreement; scope calibration.)
No verdict is blended: each concession is whole, each calibration is a named scope boundary, not an
averaging.

## Status reset (adopted from the review's table)
| Gate | Was | Now |
|---|---|---|
| A | complete | **partial** — validator/fixtures/alias-table exist; v0.4/approval/rights/fork/edition contracts do not |
| B | complete | **trace pilot complete; content approval provisional** |
| C | complete, no quarantines | **invalid; rerun required** (pre-repair rate governs quarantine) |
| D | (unlisted) | **not done** |
| E | complete | **trace migration complete; epistemic re-adjudication incomplete** |
| F | next | **blocked** until A/C/D/E reconciled |

Package 2 → reclassified **trace-system proof; content still under re-adjudication** (not a completed
Gate E epistemic proof).

## Execution order (adopted from the review's recovery sequence)
1. Correct the ledger + Frazier record publicly (this commit set). 
2. Harden the confirmed bugs with fixtures: typed-ref resolution, structured rights, remove raw-claim
   render paths + furniture reclassification, hash-bound approvals.
3. Rerun Gate C honestly (pre/post rates, triggered batch re-audits, immutable verdicts).
4. Close Gate D (frames + stopping rules).
5. Re-adjudicate stress pages 5 and 6 with role-specific fresh passes; then 2/4/7/8/9.
6. First-class fork object; pilot page 6.
7. Cut a real hash-closed mini-edition + tag.
8. Next external review against the frozen tag.

Honest scope: items 1–3 are this session's target; 4–8 are larger and will be labelled precisely as
done / in-progress / queued — no completion claim without the evidence, which is the whole point.
