# Gate D — the corpus claim: discovery vs validation frames, and stopping rules

**Status: first draft, opened 2026-07-07** in response to round-3 (Gate D had been skipped
A→B→C→E). This document defines what the corpus *is*, what it can and cannot license, and the
named frames + stopping rules that any metric must cite. **Binding rule: no recurrence,
frequency, saturation or coverage number may be stated anywhere — store, book, README —
without naming the frame below it belongs to and that frame's denominator.**

## 1. The discovery frame (what the 346-unit corpus is)

The corpus is a **convenience / opportunistic sample**: expressions surfaced by a fixed set of
deep-research prompts run in Claude chat over a chosen list of traditions and themes (wave 1 + wave
2 reports in `corpus/reports/`). It is **not** a probability sample of anything — not of "human
wisdom", not of a tradition's texts, not of what people believe.

Known, disclosed skews (CLAUDE.md §4.5): WEIRD / Western-canon / digitised-text / English-language
/ male-authored over-representation; retrieval bias toward what is quotable and famous; model
training-data bias shared by extractor and auditors (same weights). The gap-filling waves and CARE
gating reduce but do not remove these.

**What the discovery frame can license:**
- Existence claims, corpus-bounded: "This fork / expression appears in this corpus, attributed to
  these sources." (Subject to the verification tier of each unit.)
- Contrast claims, corpus-bounded: "Within this corpus, tradition A and tradition B express X
  differently."

**What it CANNOT license (prohibited off the discovery frame):**
- "X is a universal human fork." / "Most traditions hold X." / "X is the most common answer."
- Any frequency read as a global rate ("N of the world's wisdom traditions say…").
- Any saturation claim ("we have found all the major forks") beyond "new reports stopped adding
  new forks *in this sampling process*", which is a statement about the process, not the world.

## 2. Validation frames (Model C confirmation dossiers)

A **claim** promoted toward publication (a fork, a convergence, an empirical finding) needs its own
named **validation frame** — separate from discovery — recorded in a dossier
(`graph/dossiers/`, contract in METHODOLOGY §3; pilot d-0001). A validation frame declares:

1. **The precise proposition** being tested (not a theme — a falsifiable statement).
2. **Source-selection rule**: which sources are admissible as confirmation (e.g. SEP for
   positions; primary editions for wording; Quote Investigator / Fake Buddha Quotes for
   attribution), chosen *before* looking.
3. **Negative-search rule**: where a disconfirming instance would be found if it existed, and the
   commitment to look there. A convergence claim must search for the tradition that resolves the
   tension the *other* way; an empirical claim must search for the failed replication.
4. **Independence rule** (for convergence): what would count as genuine independence vs lineage,
   declared before grading (see the by-020 adversarial record for how thin this can get).
5. **Stopping rule**: the condition under which the claim is "confirmed enough to publish at tier
   T", or "refuted", or "escalate". Never "we stopped when we were satisfied."

A recurrence/convergence metric may be reported **only** inside a validation frame that names its
denominator ("k of the m sources admitted by this frame's selection rule", not "k traditions").

## 3. Stopping rules (concrete)

- **Discovery stopping (per wave):** stop a wave when the last R reports add fewer than F new
  distinct forks (record R, F, and the count dropped). This is a *process* stop, reported as such —
  "the wave-2 process reached diminishing returns at …", never "the map is complete."
- **Claim confirmation (Model C, per dossier):** a claim reaches `confirmed-tier-T` only when its
  validation frame's source-selection is exhausted, its negative-search returned no admissible
  disconfirmer (or the disconfirmers are logged as dissent), and an adversarial pass on the
  *publication* wording has run. Missing any → stays provisional; contested → escalate.
- **Verification (print gate):** unchanged — verified-primary + public-domain/licensed, per unit,
  per field.

## 4. What this unblocks / still blocks

- **Unblocks:** honest corpus-bounded existence and contrast statements on the pages (which is what
  the current chapter mostly makes).
- **Still blocks (until per-claim dossiers exist):** the pages 2 (convergence) and 5/7 (empirical)
  strength claims, and the page 1 "five forks" count — none has a validation frame yet. These are
  the stress-page rebuilds queued after this document.

## 5. Open (Jason / next)

- E-0003 (Model C adoption) formalises §2 as the methodology of record.
- Build the dossier objects for the convergence (page 2) and empirical (pages 5, 7) claims — each a
  named validation frame with its negative-search and stopping rule — before those pages are
  re-approved as sound. This document is the contract they must satisfy.
