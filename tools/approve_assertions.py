#!/usr/bin/env python3
"""approve_assertions.py — sign the current assertion content for an edition (round-3 P0-3).

Approval is edition-specific and hash-bound: this writes graph/approvals/<edition>.yaml,
recording, for every assertion whose status is in the approved enum, the SHA-256 of its
approval-relevant content (text + mandatory_caveats + prohibited_phrasings). The generator
then renders an assertion only if the manifest lists it with a matching hash — so any later
edit to the text or either policy list breaks the build until a human/agent RE-SIGNS here.

Signing is therefore the deliberate approval act. Run it only after (re-)adjudicating the
content, and commit the manifest alongside. This is not a substitute for a separate signing
authority — in a solo git repo, the commit history is the backstop — but it converts silent
content drift into a hard, visible failure.

Usage:  python tools/approve_assertions.py <edition>   (defaults to build_book.EDITION)
"""
import os
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
sys.path.insert(0, os.path.join(ROOT, "book", "generator"))
import build_book as b  # noqa: E402
import yaml  # noqa: E402


def main(edition):
    g = b.Graph()
    approvals = {}
    skipped = []
    for aid, a in sorted(g.assertions.items()):
        if str(a.get("status", "")) in b.APPROVED_STATUSES:
            approvals[aid] = b.approval_hash(a)
        else:
            skipped.append((aid, a.get("status")))
    outdir = os.path.join(ROOT, "graph", "approvals")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"{edition}.yaml")
    manifest = {
        "edition": edition,
        "decided_by": "claude-code (lead adjudication; see per-assertion adjudication_refs)",
        "date": "2026-07-07",
        "hash_fields": ["text", "mandatory_caveats (sorted)", "prohibited_phrasings (sorted)"],
        "approvals": approvals,
    }
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(manifest, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"[ok] signed {len(approvals)} assertion(s) for edition '{edition}' -> {out}")
    if skipped:
        print(f"     skipped {len(skipped)} non-approved: " + ", ".join(f"{a}({s})" for a, s in skipped))
    return 0


if __name__ == "__main__":
    ed = sys.argv[1] if len(sys.argv) > 1 else b.EDITION
    sys.exit(main(ed))
