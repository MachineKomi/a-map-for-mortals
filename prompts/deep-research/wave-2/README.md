# Wave-2 prompts — assembled, ready to run

Eight fully-assembled deep-research prompts (template + gap-block + live do-not-duplicate
notes from `corpus/COVERAGE-INDEX.md` as of 2026-07-06). **Copy the fenced block from each
file into a fresh Claude deep-research chat** — one query per chat, never a continuation.

**Save each output** as Markdown to `corpus/reports/wave-2/` using the same number and
name as its prompt file (e.g. `01-eastern.md`). Partial waves are fine — drop whatever
finishes; the pipeline tolerates any subset in any order.

Priority order:

| # | Prompt | Priority | Why |
|---|---|---|---|
| 01 | `01-eastern.md` | **P0** | the never-run wave-1 module; biggest skew in the corpus |
| 02 | `02-african.md` | P1 | named honesty commitment |
| 03 | `03-indigenous.md` | P1 | named honesty commitment (epistemic care built in) |
| 04 | `04-womens-voices.md` | P1 | corrects the male/literate skew |
| 05 | `05-childhood-old-age.md` | P1 | the book spine's starving ends (3 child units in wave 1) |
| 06 | `06-persian.md` | P2 | breadth |
| 07 | `07-practical-strategic.md` | P2 | breadth; ethically spiky stream handled descriptively |
| 08 | `08-folk-proverbial.md` | P2 | breadth; cross-cultural convergence layer |

The slot-fill source blocks live in `../wave-2-gap-traditions.md`; these files supersede
them for running. If a query is re-run later, re-check the do-not-duplicate notes against
the then-current `COVERAGE-INDEX.md` first.
