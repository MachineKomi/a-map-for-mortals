# Page 5 — competing-model chart (closes the owed item)

**Date:** 2026-07-17 · **Object:** `book/page-specs/by-050-money.yaml` figure + the
`form_threshold_curve` renderer in `book/generator/build_book.py`.
**Closes:** the "competing-model chart" item recorded as owed in BOTH
`ops/adjudications/2026-07-07-gateE-by040-050.md` (round-3 P0-7, error #2) and
`graph/dossiers/d-0002.yaml` (notes: "the page still draws one model's curve").

## The defect that was owed

The chart fixed a single ~$100k band and drew essentially one model's shape (one solid +
one dashed curve at the same point). The caption and dossier *described* a contest between
the ~$100k reading (KKM 2023 / Rohrer-Wenz 2024 lower conditional quantiles) and the ~$200k
plateau (Bennedsen 2024), but the figure did not *show* it — so the figure under-represented
the disagreement the evidence actually exhibits.

## The fix — form follows content (R-V3; R-V5: a form must express tension)

**Overlaid competing curves**, keeping the `threshold-curve` form. The dose-response below the
band IS agreed across models (experienced well-being rises with log-income — d-0002's one
permitted inference), so abandoning the curve-form for a table would over-react; the right move
is to make the curve-form carry the tension (R-V5). The figure now draws:

- A **solid curve — "flattening ~$100k"** (KKM/Rohrer-Wenz lower-conditional-quantile reading):
  rises with log-income, then flattens at the ~$100k break.
- A **dashed curve — "plateau ~$200k"** (Bennedsen 2024): rises with log-income *past* the
  ~$100k break, then plateaus later/higher.
- A **contested band spanning ~$100k–~$200k**, labelled "where the flattening sits depends on
  the model."

The two curves share an identical rise below the band (they meet at the ~$100k point), then
visibly diverge inside it — the solid one flattening while the dashed one keeps climbing toward
its later plateau. That is the contest, made visible.

## Honesty guardrails (from d-0002 permitted/prohibited inferences)

- **Schematic only** — model *directions*, never plotted data. The caption says so explicitly
  ("competing models' directions, not plotted data").
- **Below the band, agreement** — both curves rise with log-income (the one permitted inference;
  a strong "money doesn't matter" reading fails).
- **Inside the band, disagreement** — no curve reads as "the" result; both are one model each,
  labelled, with the band marking the contest.
- **No subgroup-of-people regression** — the round-3 P0-7 error (reading a conditional-quantile
  result as a class of unhappy individuals) stays fixed: the curve label says "lower conditional
  quantiles", and a-0024 carries the Rohrer-Wenz caveat. The figure does not reintroduce
  "unhappy people."
- **No causal claim** — observational; a-0025 states "whether money *causes* any of it remains
  open."

## What did NOT change

The assertions a-0023 / a-0024 / a-0025 and the dossier d-0002 are **unchanged** — the chart
now visualizes what they already say. The Schopenhauer verbatim quote (c-0013) is excerpted to
its load-bearing first sentence ("what a man is contributes much more to his happiness than what
he has...") so the page fits one page with the taller figure; the "[…] pain and boredom" tail is
a separate Schopenhauer thought not needed here. No assertion text edited → approval manifest
still valid (verified: build passes the hash-bound assertion gate without re-signing).

## Generator change

`form_threshold_curve` generalized to accept a `curves:` list (each `{breakpoint, after, style,
color, label}`) + `contested_band: {from, to, label}`, driving N competing model shapes over the
shared log-income axis. The legacy single-model path (one solid + one dashed curve at a fixed
band) is preserved for any future dose-response page. `label` added to FURNITURE_KEYS and
`style/color/breakpoint/after/from/to` to CONFIG_KEYS (figure-internal tokens, like axis names).

## QA

Rendered → PDF text-extracted pages 5/6 (definitive — the vision tool returned cached CDN URLs):
page 5 complete (both curve labels, the contested-band label, both axes, the Schopenhauer
excerpt, the full caption a-0024 and outro a-0025 ending "both remain open"); book a clean 9
pages; pages 4 (ambition fork) and 6 (time fork) intact. Curve geometry verified numerically:
both curves meet at the ~$100k point (y=176), then diverge (flatten curve flat at 175–176;
plateau curve rising to 160) — the contest is visible. Validators 0 err/0 warn (graph) +
0 err/17 counted warnings (units, pre-existing); fixtures 20/20; gate tests 14/14.
