# Licence — *A Map for Mortals*

This repository deliberately carries **three rights regimes**. The split exists so the
project can be radically transparent — every claim, source, and judgment publicly
auditable — without granting irrevocable reuse rights before the first edition exists.
(Rationale and the adversarial review of this decision: `ops/DECISIONS.md`, 2026-07-06.)

## 1 · Code — MIT

Applies to: `tools/`, `book/generator/`, `prototype/build_book.py`, and any other
executable code in this repository.

> MIT License
>
> Copyright (c) 2026 Jason Jackson
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## 2 · The wisdom graph and the book — all rights reserved, for now

Applies to: `graph/`, `book/page-specs/`, `book/renders/`, `docs/`, `prompts/`,
`runbook/`, `prototype/` (except code), and the governing documents.

© 2026 Jason Jackson. **All rights reserved — deliberately, and temporarily.**

The book is generated from the graph, so openly licensing the graph is equivalent to
openly licensing the book's substance. That is a one-way door (open licences are
irrevocable), and we decline to walk through it before edition 1 exists. **Declared
intent:** revisit at the first frozen edition, with a presumption toward opening the
graph (likely CC-BY 4.0 with machine-readable per-field exclusions for quoted
material) once the trade-off can be judged against a real product.

You are welcome to read, cite, and quote this material within normal fair-dealing /
fair-use limits, and to check every claim against its recorded sources — that
auditability is the point of the public repo.

## 3 · Corpus research reports — no licence granted; audit only

Applies to: `corpus/`.

The files in `corpus/reports/` are AI-generated deep-research outputs that interleave
original synthesis with quotations and close paraphrase of third-party sources. Their
copyright status is mixed and partly unclear (AI-generated text may not attract
copyright at all; quoted material belongs to its rights holders). Accordingly **no
licence is granted**: they are published solely so the project's provenance can be
audited. Do not redistribute or reuse them as data.

## Quotations, throughout

Quoted passages everywhere in this repository remain the property of their respective
rights holders. Primary-source quotations are predominantly public domain; short
excerpts from in-copyright translations appear only as research citations. Every graph
unit carries a `copyright_flag` field — that per-unit marking, not this file, is the
authoritative rights record for graph content. The book itself admits verbatim
quotations only if verified against a primary edition **and** public-domain or licensed
(the print gate, `A-Map-for-Mortals-METHODOLOGY.md` §2).

## Contributions

Code contributions are accepted under MIT (inbound = outbound). Content contributions
(graph, book, corpus) are **not accepted** while the content layers remain unlicensed —
please open an issue instead.
