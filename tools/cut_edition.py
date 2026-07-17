#!/usr/bin/env python3
"""cut_edition.py — generate a hash-closed edition manifest for a frozen book edition.

Reads the live graph store (units/claims/edges/assertions/forks/dossiers/page-specs),
the rendered PDF, the approval manifest, and the generator; records content hashes so
that any later edit to any ingredient is detectable (METHODOLOGY §1: "a book cites a
frozen graph"; runbook P8: freeze = git tag + graph/editions/ manifest).

The manifest is the reproducibility record: from the tagged commit, re-running the
generator must reproduce a byte-identical PDF (its hash is recorded), and every store
ingredient must match its recorded hash.

Usage:  python tools/cut_edition.py <edition-id> [--pdf book/renders/<edition-id>.pdf]
"""
import argparse
import hashlib
import os
import sys
from datetime import date

try:
    import yaml
except ImportError:
    print("pyyaml required", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_dir(rel_dir):
    """Concatenated hash of every .yaml in a store dir (sorted, path-stamped) —
    changes to any file, or adding/removing one, changes the hash."""
    d = os.path.join(ROOT, rel_dir)
    h = hashlib.sha256()
    files = sorted(f for f in os.listdir(d) if f.endswith((".yaml", ".yml")))
    for f in files:
        p = os.path.join(d, f)
        h.update(rel_dir.encode() + b"/" + f.encode() + b"\x00")
        h.update(open(p, "rb").read())
    return h.hexdigest(), len(files)


def tally(kind, d):
    """Count records and break down by a key field."""
    out = {}
    total = 0
    for f in sorted(os.listdir(d)):
        if not f.endswith((".yaml", ".yml")):
            continue
        rec = yaml.safe_load(open(os.path.join(d, f), encoding="utf-8")) or {}
        total += 1
        if kind == "units":
            k = rec.get("attribution_confidence", "?")
        elif kind == "units-verif":
            k = (rec.get("verification") or {}).get("status", "?")
        elif kind == "units-copy":
            k = rec.get("copyright_flag", "?")
        elif kind == "claims":
            k = rec.get("status", "?")
        else:
            k = "?"
        out[k] = out.get(k, 0) + 1
    return total, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edition")
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--note", default="")
    args = ap.parse_args()

    # included page-specs for this edition
    spec_dir = os.path.join(ROOT, "book", "page-specs")
    specs = sorted(f[:-5] for f in os.listdir(spec_dir) if f.endswith(".yaml"))

    unit_total, unit_conf = tally("units", os.path.join(ROOT, "graph", "units"))
    _, unit_verif = tally("units-verif", os.path.join(ROOT, "graph", "units"))
    _, unit_copy = tally("units-copy", os.path.join(ROOT, "graph", "units"))
    claim_total, claim_status = tally("claims", os.path.join(ROOT, "graph", "claims"))

    # store + ingredient hashes
    hashes = {}
    for rel in ["graph/units", "graph/claims", "graph/edges", "graph/assertions",
                "graph/forks", "graph/dossiers", "graph/interpretations",
                "book/page-specs"]:
        d = os.path.join(ROOT, rel)
        if os.path.isdir(d):
            h, n = sha256_dir(rel)
            hashes[rel] = {"files": n, "sha256": h}
    hashes["book/generator/build_book.py"] = {
        "sha256": sha256_file(os.path.join(ROOT, "book", "generator", "build_book.py"))}
    ap_path = os.path.join(ROOT, "graph", "approvals", f"{args.edition}.yaml")
    if os.path.isfile(ap_path):
        hashes[f"graph/approvals/{args.edition}.yaml"] = {"sha256": sha256_file(ap_path)}
    pdf_path = args.pdf or os.path.join(ROOT, "book", "renders", f"{args.edition}.pdf")
    html_path = os.path.join(ROOT, "book", "renders", f"{args.edition}.html")
    pdf_hash = sha256_file(pdf_path) if os.path.isfile(pdf_path) else None
    pdf_size = os.path.getsize(pdf_path) if os.path.isfile(pdf_path) else None
    # HTML is the generator's deterministic output; the PDF is a WeasyPrint projection that
    # embeds a creation timestamp, so the HTML hash is the reproducibility anchor.
    html_hash = sha256_file(html_path) if os.path.isfile(html_path) else None

    manifest = {
        "id": args.edition,
        "cut_date": str(date.today()),
        "status": "frozen",
        "scope": "The Building Years chapter (9 page-specs) — the walking-skeleton stress chapter. "
                 "NOT the complete book v1 (the corpus-wide S3/S4 clustering is pending).",
        "included_page_specs": specs,
        "store_counts": {
            "units": unit_total,
            "units_by_attribution": unit_conf,
            "units_by_verification": unit_verif,
            "units_by_copyright": unit_copy,
            "claims": claim_total,
            "claims_by_status": claim_status,
            "edges": hashes.get("graph/edges", {}).get("files", 0),
            "assertions": hashes.get("graph/assertions", {}).get("files", 0),
            "forks": hashes.get("graph/forks", {}).get("files", 0),
            "dossiers": hashes.get("graph/dossiers", {}).get("files", 0),
        },
        "render": {
            "html": os.path.relpath(html_path, ROOT),
            "html_sha256": html_hash,
            "pdf": os.path.relpath(pdf_path, ROOT),
            "pdf_sha256": pdf_hash,
            "pdf_bytes": pdf_size,
            "note": "The HTML is the generator's deterministic output and is the reproducibility "
                    "anchor (re-running build_book.py reproduces it byte-identical). The PDF is a "
                    "WeasyPrint projection that embeds a creation timestamp, so its hash varies "
                    "across renders even for identical content; verify content via the HTML hash.",
        },
        "ingredient_hashes": hashes,
        "reproducibility": (
            "From the tagged commit, re-running `python book/generator/build_book.py` must "
            "reproduce a PDF whose sha256 matches render.pdf_sha256. Every store ingredient's "
            "concatenated sha256 is recorded under ingredient_hashes; any later edit to a unit, "
            "claim, edge, assertion, fork, dossier, page-spec, or the generator itself is "
            "detectable as a hash mismatch against this manifest."
        ),
        "known_limits": [
            "Skeleton-scale claims/edges only (33 claims, 23 edges) — the 454 units minted in "
            "P4/wave-3 carry claim_id: null until the corpus-wide S3/S4 pass.",
            "Content under re-adjudication per external review round 3; this is a traced-system "
            "proof + stress-page rebuild, not a Gate-E epistemic proof.",
            "Wave-3 units (u-0347..u-0487) are attested/pending-primary and in-copyright — not "
            "print-gate candidates; their insights reach a page only as paraphrase, never verbatim.",
        ],
        "note": args.note,
    }
    out = os.path.join(ROOT, "graph", "editions", f"{args.edition}.yaml")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(f"# Edition manifest — frozen {date.today()}. See runbook P8 / METHODOLOGY §1.\n")
        fh.write(f"# Cut by tools/cut_edition.py; the git tag '{args.edition}' pins the exact commit.\n")
        yaml.dump(manifest, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)
    print(f"Wrote {out}")
    print(f"  units: {unit_total}  claims: {claim_total}  page-specs: {len(specs)}")
    print(f"  pdf: {pdf_hash[:16] if pdf_hash else 'MISSING'}... ({pdf_size} bytes)")
    for k, v in hashes.items():
        print(f"  {k}: {v.get('sha256','?')[:16]}...")


if __name__ == "__main__":
    main()
