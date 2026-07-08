# Fork object pilot — f-0001 (the time fork, page 6)

**Date:** 2026-07-08 · **Object:** `graph/forks/f-0001.yaml` (first first-class fork object) ·
**Round-3 P1-forks; blueprint §5.** Purpose: move the page-6 conditional counsel out of
unfalsifiable editorial page-copy into a structured, gated fork object with poles, costs,
conditions (supported vs hypothesised), counterexamples, danger conditions, and unresolved
questions — the round-3 stop condition being "a fork's conditions exist only in page copy."

**Method:** lead drafts the fork; **mandatory fresh-context adversarial pass** on the conditions
(the review said this fork's conditional counsel needs testing, not a disclaimer). Verdicts recorded
verbatim below; edits accepted whole (never blended). Shared-weights disclosed by the adversary.

## Adversarial verdict (verbatim), and disposition

**Strongest attack (accepted):** "The two 'hypothesised conditions' are not symmetric hypotheses —
they are the same tautology restated twice, and both smuggle their pole's verdict into the
diagnosis… each condition is its pole's failure-mode-of-the-other, rephrased as a trigger, and the
pair quietly privileges 'build' by casting 'seize' as mood. A reader gains no operational guidance —
only a mirror that returns whichever answer they walked in with." → **Accepted.** This undercut the
whole reason for the object; circular conditions aren't more testable for being structured.

- **Point 1 — poles fairly stated?** APPROVE-WITH-EDIT. Accepted: seize `costs` →
  `[never-builds-anything, discounts-the-future-others-depend-on]` (the recklessness cost had lived
  only in danger_conditions).
- **Point 2 — conditions honest/defensible?** APPROVE-WITH-EDIT (rewrite both, keep `hypothesised`).
  Accepted verbatim: seize `when` → "you keep deferring what you say matters most, and the deferral
  has no end date you actually intend to reach"; build `when` → "a commitment you have freely chosen
  will fail others if you optimise for how any single week feels." Removes "the place you hide"
  (imported build's failure mode) and "the mood of the week" (demoted seize to feeling); gives a
  signal the reader can check without having pre-diagnosed themselves. Tag stays `hypothesised` — none
  is evidence-backed.
- **Point 3 — danger_conditions & counterexamples.** APPROVE-WITH-EDIT. Accepted: added the
  **dissolution** counterexample ("the person whose long-horizon work is itself the life they would
  choose to be living now — for whom the two poles coincide and the fork does not arise") — a fork
  that never notes its own dissolution-case overstates how often the tension bites.
- **Point 4 — status/dossier_ref honest?** APPROVE (no change): `poles-mapped` + `dossier_ref: null`
  + `unresolved` naming the conditions untested are collectively non-overclaiming.
- **Point 5 — claim_type_mix.** APPROVE-WITH-EDIT (disclose, don't promote). Kept
  `claim_type_mix: [prudential]` because the poles and conditions are all prudential; the normative
  premise (you ought not abandon dependants) is confined to `danger_conditions` and is now **disclosed
  in `notes`** rather than promoted — promoting it would overstate how much normative claiming the
  fork's *counsel* does.

**Honesty-contract concern (accepted and logged):** the head `c-0003` (Seneca) is not a neutral
frame — its content *is* the seize pole's argument (confirmed by `e-0021`, which tensions Seneca with
the *build* pole and has no edge to seize). Recorded in `notes` so the tilt is on the record, not
concealed. The Seneca-toward-seize and the (now-removed) mood-toward-build tilts roughly cancelled,
but neither was declared; declaring both is the fix.

## What this pilots for the contract

- `graph/forks/` is now a real store with a validator contract (shape: question, ≥2 poles each
  pointing to a real claim, `conditions` limited to `supported`/`hypothesised`, `unresolved`,
  `status`, `adjudication_refs`; ref resolution for relation/head/pole-claim/dossier/adjudication;
  `dossier-complete` must carry a `dossier_ref`). Negative fixtures added.
- The generator renders the page-6 comparison table **from the fork** (`fork_ref`): each column's
  "speaks to / trusts / curdles into" come from the pole fields and "take it when" from
  `conditions.hypothesised`, marked as the book's hypothesis. The conditions no longer live in page
  copy.
- **Owed (honest):** this is `poles-mapped`, not `dossier-complete`. A prudential fork whose
  conditions are hypothesised is legitimately dossier-free, but the pattern for an *evidence-backed*
  fork (e.g. page 5's money fork, page 7's suffering fork) still needs the empirical dossier object.
