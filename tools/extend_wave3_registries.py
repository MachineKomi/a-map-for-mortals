#!/usr/bin/env python3
"""extend_wave3_registries.py — add wave-3 contemporary/* traditions and new
domains to the registries, and bump counts on existing entries.

Wave-3 (u-0347..u-0487) introduces:
  - 19 new tradition raws, all under the new `contemporary/*` family
  - 15 new domain raws
The registry is an alias table (raw -> canonical_id). For the new contemporary/*
traditions the raw is already a descriptive family-prefixed label, so canonical_id
= raw (identity). For new domains, identity unless a true synonym exists.
This is a one-shot migration script; keep as the audit record. Re-runnable: it
recomputes counts from the live store, so it is idempotent.
"""
import collections
import glob
import os
import sys

try:
    import yaml
except ImportError:
    print("pyyaml required", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNITS = os.path.join(ROOT, "graph", "units")
TRAD_REG = os.path.join(ROOT, "graph", "registries", "traditions.yaml")
DOM_REG = os.path.join(ROOT, "graph", "registries", "domains.yaml")

# canonical_id decisions for genuinely new domains (identity by default;
# only fold where a true synonym exists in the existing set).
DOMAIN_CANON = {
    "technology": "technology",
    "mental-health": "mental-health",
    "self-understanding": "self-understanding",
    "wellbeing": "wellbeing",
    "consumption": "consumption",
    "policy": "policy",
    "daily-habits": "daily-habits",
    "civic-life": "civic-life",
    "environment": "environment",
    "geopolitics": "geopolitics",
    "security": "security",
    "philanthropy": "philanthropy",
    "leisure": "leisure",
    "elder-care": "elder-care",
    "childhood-development": "childhood-development",
}


def tally_wave3():
    trad = collections.Counter()
    dom = collections.Counter()
    for f in sorted(glob.glob(os.path.join(UNITS, "u-0*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        if not d or not isinstance(d, dict):
            continue
        n = str(d.get("id", ""))
        if not n.startswith("u-"):
            continue
        num = int(n.split("-")[1])
        if not (347 <= num <= 487):
            continue
        t = d.get("tradition")
        if t:
            trad[t] += 1
        for x in d.get("life_domains") or []:
            dom[x] += 1
    return trad, dom


def extend(reg_path, wave3_counts, canon_map=None):
    reg = yaml.safe_load(open(reg_path, encoding="utf-8"))
    entries = reg["entries"]
    by_raw = {e["raw"]: e for e in entries}

    # Recompute full counts across the WHOLE store (not just wave-3) so the
    # registry stays the source of truth for current counts.
    full_counts = collections.Counter()
    for f in sorted(glob.glob(os.path.join(UNITS, "u-0*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        if not d or not isinstance(d, dict):
            continue
        if "traditions.yaml" in reg_path:
            t = d.get("tradition")
            if t:
                full_counts[t] += 1
        else:
            for x in d.get("life_domains") or []:
                full_counts[x] += 1

    added = 0
    bumped = 0
    for raw, cnt in full_counts.items():
        if raw in by_raw:
            if by_raw[raw]["count"] != cnt:
                bumped += 1
            by_raw[raw]["count"] = cnt
        else:
            # new entry
            canon = raw
            if canon_map and raw in canon_map:
                canon = canon_map[raw]
            entries.append({"raw": raw, "count": cnt, "canonical_id": canon})
            added += 1

    # sort: highest count first (matches existing ordering)
    entries.sort(key=lambda e: (-e["count"], e["raw"]))
    reg["entries"] = entries
    with open(reg_path, "w", encoding="utf-8") as fh:
        yaml.dump(reg, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)
    return added, bumped, len(entries)


def main():
    trad, dom = tally_wave3()
    print(f"wave-3 traditions: {len(trad)} distinct ({sum(trad.values())} units)")
    print(f"wave-3 domains:    {len(dom)} distinct ({sum(dom.values())} tags)")
    print()

    ta, tb, te = extend(TRAD_REG, trad)
    print(f"traditions: added {ta}, count-bumped {tb}, total entries now {te}")
    da, db, de = extend(DOM_REG, dom, DOMAIN_CANON)
    print(f"domains:    added {da}, count-bumped {db}, total entries now {de}")


if __name__ == "__main__":
    main()
