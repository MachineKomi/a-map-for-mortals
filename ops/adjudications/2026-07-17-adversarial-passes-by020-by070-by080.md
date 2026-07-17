# Fresh adversarial passes — pages 2, 7, 8 (closes recovery #4)

**Date:** 2026-07-17 · **Round-3 recovery #4 (final item).** Three role-specific fresh-context
adversarial passes on the chapter's three relation-bearing pages: page 2 (convergence-map),
page 7 (the honest-asterisk node card), page 8 (the Gate B traced-prose pilot). Each adversary
was charged to attack its page's central honesty risk; shared-weights disclosed by all three.

The adversaries were honest: **most charges failed** (the pages are largely sound), and each
landed a small number of genuine, verbatim-fixable residuals. All edits accepted whole (never
blended). No REJECTs.

## Page 2 — convergence-map ("Do what is yours. Release the rest.")

Central risk: overstating convergence across lineage-contaminated voices (Epictetus, Tarfon,
hadith, Lear). **Attack largely failed** — the convergence is argued and hedged (2/4 voices
fully instantiate the motif; Tarfon a cousin; Edgar lineage), the independence grades are honest,
claim-types aren't laundered. Two residuals landed, both about *lineage disclosure on the two
voices closest to the Stoic trunk*:

- **Edgar voice-meta tightened** (by-020-carrying.yaml): was `"Shakespeare · 1606 · lineage"`
  (the word "lineage" doing quiet work while the voice sat in a four-voice convergence cluster);
  now `"Shakespeare · 1606 · shown as lineage, not independent recurrence"` — moves the
  dashed-line semantics into the descriptor so a skimmer can't read four-way convergence.
- **a-0028 (frays) gained Tarfon's lineage risk**: the frays note fully disclosed Lear's
  transmission but was silent on Tarfon's documented-general Hellenistic milieu (a-0026's own
  notes call Tarfon's independence the cluster's weakest). Added a clause tracking e-0002's
  exact evidence ("Hellenistic influence on rabbinic thought is documented in general, though
  not for this saying") — putting Tarfon's lineage risk on the record at the edge's own confidence.

## Page 7 — node-card ("Does the load make you stronger?")

Central risk: the asterisk is cosmetic while the node leans toward the comfort. **Attack failed
on the core** — the asterisk is load-bearing (a-0011 genuinely qualified; e-0006 INFLUENCED not
CONVERGES_WITH; PTG evidence a measurement caution not a verdict; Frazier design primary-checked;
claim-types honestly segregated). Four of five charges failed. **One real hit** on the framing:

- The intro said the comfort is printed "because the evidence pulls both ways" and the pill
  repeated "the evidence cuts both ways." But both empirical findings on the card (Frazier, 
  Galatzer-Levy) pull the *same* way — against the strengthening claim. The genuine tension is
  **voices vs evidence**, not evidence-vs-evidence. Reworded (intro + pill): "the two voices
  press the comfort, and the studies qualify it" / "the studies qualify the comfort, they don't
  confirm it." Used "qualify" not "disprove" — Frazier is explicitly a measurement caution and
  resilience is consistent with endurance, so no overcorrection into the opposite dishonesty.

## Page 8 — traced-prose ("Raising others without owning them")

Central risks: manufactured convergence + laundered doctrine. **Attack failed on the prose** —
the record shows convergence-manufacture was already caught (e-0019 retyped
CONVERGES_WITH→FUNCTIONAL_ANALOGY, low; d-0001 records the non-equivalence; assertions reworded
with prohibited-phrasing enforcement). Two items the adversary raised were judged **already
addressed**, not new:

- **Title reclassification (round-3 P0-4):** the adversary flagged the title as propositional
  furniture. But the generator already treats titles as `editorial` (build_book.py line 545,
  P0-4 comment) — swept for prohibited phrases, recorded in the trace, not furniture. Applied
  generically to all pages including page 8. No change needed.
- **Zosima dramatic-context visibility:** the adversary proposed an explicit "character in
  Dostoevsky's novel" credit line. Verified the rendered credit already reads "Fyodor Dostoevsky,
  The Brothers Karamazov Book II, ch. 4 'A Lady of Little Faith' (Zosima to Madame Khokhlakova)
  · trans. Constance Garnett" — the dramatic context (character, addressee, novel, chapter) IS
  visible. Judged already-satisfied; redundant expansion would add verbosity without honesty.

**Stale-text cleanup** (the adversary's useful ledger-hygiene find): u-0012's `escalation` field
and STATE.md's Gate-B line still said E-0002 "open" after the 2026-07-17 closure. Both corrected.

## Verification

Manifest re-signed (a-0028 text changed). Validators: graph 0 err/0 warn, units 0 err/17 counted
warnings (pre-existing). Fixtures 20/20, gate tests 14/14. Rendered 9 pages; PDF text-extraction
confirms all three edits landed and every page fits. This **closes recovery #4** — the stress-page
rebuilds are complete.
