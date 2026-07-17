# Fork-object redesign — page 4 (ambition), f-0002

**Date:** 2026-07-16 · **Object:** `graph/forks/f-0002.yaml` (the ambition fork) + rewritten
`book/page-specs/by-040-ambition.yaml` + new assertion `graph/assertions/a-0030.yaml`.
**Round-3 recovery #4 (stress-page rebuilds): page-4 fork-object redesign.**

## The problem the round-3 review raised

Page 4 rendered the ambition fork as a `trade-off-spectrum` — a "Striving ⟷ Contentment"
line, both poles good, the reader invited to pick a spot. The review's charge: that frame
**misrepresents the content.** Forced to state when the round-3 stop condition ("a fork's
conditions exist only in page copy") is met, the page had its conditional counsel living in
the `spectra[].note` editorial string, ungated.

## Content analysis — form must follow content (R-V3)

The graph research (see f-0002 `notes`) shows the ambition fork is **structurally unlike**
the time fork (f-0001, page 6), and the structure dictates the form:

- **Time fork (f-0001):** two *positive counsels* (Horace seize / Vauvenargues build), each
  genuinely wise, held in tension by one high edge (e-0008). → `comparison-columns` fits; the
  two columns are the two counsels.
- **Ambition fork:** *not two choosable counsels.* Faust (c-0022) is **cautionary** — a wager
  with forfeit terms, gated "not counsel" (a-0020). Thoreau (c-0014) and Pascal (c-0015) are
  **diagnoses of the ditch**, not a pole (neither has any tension edge). There is no positive
  "strive!" voice in this corner of the corpus. What the sources actually do: Faust *names the
  wager* (striving-as-bet-on-satisfaction); Thoreau/Pascal *name its ditch* (the postponing
  life); Qoheleth (c-0011) names a *third thing* — honest labour enjoyed now, in the face of
  impermanence — which reframes what the striving is *for*, turning down both the bet and
  surrender.

So the content is **a wager most voices warn against, with one counsel that reframes what the
striving is for.** The round-3 review's "when does striving serve vs postpone the life" framing
is exactly right. The two poles of the fork are therefore the two **modes of striving** (serves
the life / wagers the life), not two virtues on a line.

**Form chosen: `comparison-columns` + `fork_ref: f-0002`** (the only fork-aware form). The two
columns become the two modes of striving: "striving that serves" (Qoheleth c-0011) and "striving
that wagers" (Faust c-0022). The ditch-voices (Thoreau/Pascal) become the wager pole's
`failure_mode` — the "curdles into" row. The "take it when*" rows come from the fork's
hypothesised conditions, gated in the object, not page copy. Pages 4 and 6 sharing the form is
permitted: they are non-adjacent (the money page sits between), carry genuinely different
content, and §6's neighbour-variation rule is satisfied.

**Colour:** Faust pole orange (cautionary) / Qoheleth pole pink, per SPEC §2 amended palette.
Unlike the time fork — whose two positive counsels rightly take equal-status neutral colour —
one pole of the ambition fork *is* adjudicated cautionary here, so equal-neutral colour would
itself misrepresent the content.

## The fork object (f-0002)

- `poles`: `serve` (c-0011 Qoheleth) / `wager` (c-0022 Faust).
- `head_ref: c-0015` (Pascal — the postponement diagnosis the fork turns on).
- `relation_refs: [e-0023, e-0009]` — no single edge holds this fork the way e-0008 holds the
  time fork; the ambition tension is distributed (e-0023 Qoheleth↔Faust moderate; e-0009
  Faust↔readiness high).
- `conditions.hypothesised`: two `when` clauses — the gated conditional counsel.
- `status: poles-mapped`, `dossier_ref: null` (prudential, like f-0001 — no empirical layer).

## Mandatory adversarial pass (verbatim verdicts)

Per the f-0001 pilot precedent (whose original conditions were circular and had to be
rewritten), a fresh-context adversary was run on f-0002, charged to reproduce that failure.
Shared weights disclosed.

**The critical circularity test — FAILED to convict. APPROVE on Point 2.** The adversary tried
every angle: (a) same tautology restated; (b) one pole's trigger = the other's failure-mode
rephrased; (c) a mirror returning the walked-in answer. All three failed. The decisive argument:
the two `when` clauses test *different sub-dimensions* (is the goal separable from the activity
/ can it be articulated — vs — is 'enough' specifiable / is the present experienced as cost) and
produce a genuine **mixed state** (a reader can pass both, fail both, or split), which a circular
mirror is structurally incapable of doing. The wager `when` in particular ("the 'enough' has no
fixed shape, only 'more than now' — and the present counts only as its cost") is a clean,
checkable signal. **No rewrite of the conditions.**

Two genuine minor defects found, both WITH-EDIT, edits **accepted whole** (never blended):

1. **Point 3 (counterexamples & danger_conditions):** the serve `when`'s counterfactual ("would
   still choose to be doing some of it even if the goal never arrives") can also be passed by
   *compulsive or escapist labour* — work used to avoid the life wears the same profile as work
   loved for its own sake. Accepted verbatim: a third `danger_conditions` entry added, flagging
   that "name the good the work serves" must mean a good beyond keeping yourself occupied.

2. **Point 6 (undisclosed tilts):** the fork's shared currency is the word "enough" — in the
   question, in serve's `protects` ("enough-in-this-hour"), and in wager's `when`. "Enough" is
   *contentment's* word, not ambition's, so framing the whole ambition question as a question of
   sufficiency is a mild structural lean toward the serve/contentment side. Accepted verbatim: a
   fourth disclosed tilt added to `notes`, on the record rather than smuggled. Kept because c-0011
   is itself a sufficiency claim and the wager `when` turns "enough" back against the wager pole.

Points 1, 4, 5 APPROVE (no edit): poles fairly stated (no quietism smuggled into serve; no
endorsement smuggled into wager); `poles-mapped` + `dossier_ref: null` honest; `claim_type_mix:
[prudential]` correct (Faust's metaphysical tag stays on its claim, not promoted; the normative
premise stays confined to danger_conditions, disclosed not promoted).

**Net: APPROVE-WITH-EDIT.** The circularity disease that sank the pilot is absent.

## Disclosed tilts (on the record)

1. The head `c-0015` (Pascal) is NOT neutral — it diagnoses the wager pole, agreeing with the
   serve direction (mirrors f-0001's Seneca-head disclosure).
2. Putting Qoheleth as the serve pole could tilt toward rest — mitigated because the pole
   specifies honest *labour* (striving), not quietism, and the lesson's two-sided
   self-examination holds the balance.
3. `claim_type_mix: [prudential]` — Faust's metaphysical tag stays on its claim; the normative
   premise stays in danger_conditions.
4. VOCABULARY TILT: "enough" is contentment's word; the sufficiency-framing mildly leans toward
   serve (accepted verbatim from the adversary; see above).
5. Structural note (non-blocking): the fork's *high* edge (e-0009) runs to a claim that is not a
   pole (readiness c-0021) — a future revision may decide whether page-4 is genuinely
   serve-vs-wager or whether the high edge pulls toward an effort-vs-acceptance framing the
   two-pole object under-represents.

## Assertion a-0030 (page-4 caption)

New `relation-summary` assertion marking the fork unresolved and the conditions as hypotheses,
mirroring page 6's a-0019. Carries c-0011 / c-0022 / c-0015, edges e-0023 / e-0009, mandatory
caveat "does not resolve it". Respects a-0020's "not counsel" gate on Faust (prohibited
phrasings block "Faust counsels"). Signed into the `building-years-v0.2.0` approval manifest.

## What this closes / what it owes

- **Closes** the page-4 fork-object redesign (round-3 recovery #4, page-4 piece). The forced
  spectrum is gone; the conditional counsel is gated in f-0002, not page copy.
- **Owed (honest):** `status: poles-mapped`, not `dossier-complete`. Conditions are hypothesised
  editorial readings, not findings. The recurring "enough" fork (SPEC §9) now has its
  Building-Years rendering in a conditional-fork form consistent with the other life-phase
  altitudes.
- **Still queued in #4:** page-5 competing-model chart; fresh role-specific adversarial passes on
  pages 2/7/8.
