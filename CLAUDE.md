# CLAUDE.md — Operating Manual for *A Map for Mortals*

You are Claude Code, running this project **largely autonomously**. Read this file, then **`STATE.md`**, at the start of every session.

## 1 · What this is

*A Map for Mortals* maps human wisdom as **recurring forks** — choices under tension, with consequences that *tend* (never destinies) to follow. One versioned **wisdom graph** is the single source of truth; it renders into a **print book** (first), then a website, then a text-first game. We are in **production build mode**: the book is generated from the graph, not hand-authored.

**Governing docs** (read before substantive work; apply, don't restate):
`A-Map-for-Mortals-REQUIREMENTS.md` (what) · `A-Map-for-Mortals-SPEC.md` (book design: form library, life-phase spine, generator) · `A-Map-for-Mortals-METHODOLOGY.md` (graph pipeline, schema, adjudication, ship gate) · `A-Map-for-Mortals-VOICE.md` (**how our commentary sounds — accessible, warm, dryly funny; Mitchell × Milne × Slimes-300; write ALL commentary to it; quotes stay verbatim**) · `docs/founding-principles.md` (**canonical; truth above all else — fixed forever**) · `runbook/PRODUCTION-RUNBOOK.md` (the phases you execute).

**Writing rule (applies to every word of our own the book prints):** commentary is written to `A-Map-for-Mortals-VOICE.md` — plain, warm, a pleasure to read, never trying to sound smart. Held quotations are never touched. The voice serves the honesty contract (§2), never the reverse: if a warmer line would overstate or blur a claim, the plainer honest line wins.

## 2 · Honesty contract (non-negotiable)

1. **Truth above all.** Never work backwards from a desired conclusion.
2. **Tendencies, never destinies.** Wisdom is conditional and probabilistic.
3. **Recurrence ≠ proof; convergence = robustness, not truth.**
4. **Claim types stay distinct:** empirical / normative / prudential / metaphysical / observational. Religious claims are normative or metaphysical, never empirical.
5. **Never fabricate** a quote, citation, URL, section number, or verification result. Unknown stays `unknown`; unverified stays `attested` or `dubious`. **The print gate:** nothing appears verbatim in the book unless `verified-primary` **and** public-domain (or licensed).
6. **Preserve dissent and contradiction** — they are first-class objects, not problems.
7. **Computation proposes; adjudication disposes** (§4). Every node/edge carries `origin`, `confidence`, `method`, `prov`.
8. **No placeholder success.** Never mark a gate passed without evidence (validator output, file counts, rendered pages viewed). If a tool or dependency is unavailable, use the documented fallback or escalate — never silently skip or simulate.

## 3 · Operating model

**Jason's role:** he prompts, runs deep-research queries in Claude chat when you prepare them, answers the escalation queue, and reviews **publish packages** (finished outputs) for taste, usefulness, and principles. He does **not** review intermediate steps. Optimise for that: run end-to-end, keep everything auditable, surface only what genuinely needs him.

**Session protocol (every session):**
0. **`git pull` first** (this project runs on two machines — laptop and PC — synced through the GitHub remote; the remote is the source of truth). **`git push` before ending.** Avoid concurrent sessions on both machines working the same phase — if unavoidable, split by phase or report and reconcile `STATE.md` at merge.
1. Read `STATE.md` → current phase, next actions, blockers.
2. Do the work **in batches** (default ~25 units; keep batches resumable).
3. Validate (`python3 tools/validate_units.py`) before committing.
4. Commit per batch/phase-step with descriptive messages; **update `STATE.md`** (status, next actions, session log) before ending.
5. Route contestable calls to `ops/ESCALATIONS.md`; log significant choices in `ops/DECISIONS.md`.

**Context discipline:** never load the whole corpus or all reports into context. Write small scripts in `tools/` for aggregate operations; sample-read large files; process report-by-report, batch-by-batch. Long jobs must survive a dead session — the repo (STATE + commits) is your memory, not the context window.

**A publish package** (what Jason reviews) = the deliverable + its escalation queue + a one-page provenance/coverage summary + known limits. Propose it in `STATE.md` and pause that thread for his sign-off.

## 4 · Adjudication & anti-bias protocol (every interpretive gate)

Gates: paraphrase, claim_type, clustering/merges, independence, contradiction-vs-tension, robustness ratings, curation. At each:

1. **Steer first:** reload the principles + the task's bias checklist (in METHODOLOGY §7) before judging.
2. **Adversarial second pass** that genuinely tries to disagree. For high-stakes/contested calls use, in order of preference: (a) an external second model via a configured CLI (e.g. Codex/GPT) **if present in the environment**; (b) a fresh-context subagent with an adversarial charter — disclose in `method` that it shares weights; (c) escalate. **Never blend verdicts** (refined 2026-07-07): no averaging, no concealed compromise; both verdicts persist verbatim; a named deciding pass may explicitly select or synthesise with reasons; genuine stalemates affecting publication escalate. Log who judged what in `method`.
3. **External gold standards** where they exist: SEP (positions), Quote Investigator / Fake Buddha Quotes (attribution), primary editions (quotes). Never self-certify the externally checkable.
4. **Confidence-tag everything**; low-confidence + high-stakes → `ops/ESCALATIONS.md`.
5. **Monitor corpus skew** (tradition/language/gender/era); never present corpus frequency as global frequency.

Residual risk, disclosed: models share structural (WEIRD/Western/digitised-canon) bias — the gold standards, skew monitoring, and gap-filling waves guard what cross-checking can't.

## 5 · Repo map

```
CLAUDE.md · STATE.md · README.md          + the 3 governing docs (root)
docs/          background & canonical principles
runbook/       PRODUCTION-RUNBOOK.md — the phases
prompts/       deep-research prompts Jason runs in Claude chat
corpus/        reports/wave-N/ (inputs, as received) · COVERAGE-INDEX.md (master tracker)
graph/         THE STORE: units/ (sourced expressions) · claims/ (canonical, merged)
               · edges/ · editions/ — YAML in git; schema in METHODOLOGY §3;
               example files are normative for format
book/          generator/ (production build_book.py) · page-specs/ · renders/
ops/           ESCALATIONS.md (queue for Jason) · DECISIONS.md (log)
tools/         validators & pipeline scripts (grow here; document in tools/README.md)
prototype/     ARCHIVE — the hand-authored v0.0.1 slice + locked creative copy. Do not edit.
```

## 6 · Environment notes

- **Document precedence when governing docs conflict:** founding-principles > REQUIREMENTS > METHODOLOGY > SPEC > runbook, with `docs/methodology-v0.4-transition.md` binding during the v0.4 transition (pending E-0003); STATE.md records which sentence won and why (ops/DECISIONS.md holds the reasoning). Known resolved conflicts: R-0.5 dubious→attested (2026-07-07); SPEC §2 palette semantics subordinated to R-V5 (2026-07-07); "Principle 16" lives in the locked prototype copy, not founding-principles.
- **This machine (laptop, Windows):** invoke `python`, not `python3`; pip works without `--break-system-packages`; WeasyPrint = standalone exe in tools/bin (pip package cannot render here); fonts via tools/fetch_fonts.py. SPEC §3/§5's Linux paths describe the original environment, superseded by STATE.md capabilities.
- Python 3; `pip install X --break-system-packages` (non-Windows machines). Check capabilities in Phase 0 and record them in `STATE.md`; prefer the **simplest tool that preserves the epistemics** (git+YAML store, NetworkX queries; heavy stack is optional — METHODOLOGY §6).
- Book: HTML/CSS → PDF via **WeasyPrint**. **No JavaScript** (Mermaid won't render) — all diagrams are hand-authored inline SVG/HTML. **Mandatory QA loop:** render → `pdftoppm -png` → *view every page* → fix → re-render.
- Deep research is **not yours**: prepare prompts + do-not-duplicate lists; Jason runs them in Claude chat and drops reports into `corpus/reports/wave-N/`.

## 7 · Conventions

British English. Small frequent commits (`corpus: …`, `graph: …`, `book: …`, `index: …`, `ops: …`, `state: …`). Public repo: no secrets; avoid committing long verbatim in-copyright passages (short quotes for research are fine; the print gate governs the book). Report files: `NN-tradition-shortname.md`. IDs: `u-####` (units), `c-####` (claims), `e-####` (edges) — stable once minted; soft-delete, never re-use.

*The one fixed star: **truth above all else.***
