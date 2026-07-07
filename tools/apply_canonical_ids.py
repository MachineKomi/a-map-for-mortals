#!/usr/bin/env python3
"""apply_canonical_ids.py — fill canonical_id in the taxonomy registries (Gate A).

Reads an adjudicated mapping file (YAML with traditions_mapping / domains_mapping
lists of {raw, canonical_id, ...}) and writes the ids into
graph/registries/traditions.yaml and graph/registries/domains.yaml.

Refuses to write unless the mapping covers every registry entry exactly once and
introduces no unknown raw strings. Idempotent: re-running with the same mapping
is a no-op. The mapping file itself (with contested flags and adjudication notes)
is the audit record — commit it alongside the registries.

Usage:  python tools/apply_canonical_ids.py <mapping.yaml>
"""
import sys
import os
import yaml

ROOT = os.environ.get("MAP_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = {
    "traditions_mapping": os.path.join(ROOT, "graph", "registries", "traditions.yaml"),
    "domains_mapping": os.path.join(ROOT, "graph", "registries", "domains.yaml"),
}


def main(mapping_path):
    with open(mapping_path, encoding="utf-8") as f:
        mapping = yaml.safe_load(f)
    failures = 0
    staged = []  # validate everything first; write only if fully clean
    for key, reg_path in REG.items():
        entries_map = {}
        for m in mapping.get(key) or []:
            raw, cid = m.get("raw"), m.get("canonical_id")
            if not raw or not cid:
                print(f"[error] {key}: entry missing raw/canonical_id: {m}")
                failures += 1
                continue
            if raw in entries_map:
                print(f"[error] {key}: raw string mapped twice: {raw!r}")
                failures += 1
            entries_map[raw] = cid
        with open(reg_path, encoding="utf-8") as f:
            reg = yaml.safe_load(f)
        raws = {e["raw"] for e in reg["entries"]}
        missing = raws - set(entries_map)
        unknown = set(entries_map) - raws
        for r in sorted(missing):
            print(f"[error] {key}: registry raw string not covered by mapping: {r!r}")
        for r in sorted(unknown):
            print(f"[error] {key}: mapping raw string not in registry: {r!r}")
        failures += len(missing) + len(unknown)
        staged.append((reg_path, reg, entries_map))
    if failures:
        print(f"\n{failures} error(s) — nothing applied; fix the mapping and re-run.")
        return 1
    for reg_path, reg, entries_map in staged:
        for e in reg["entries"]:
            e["canonical_id"] = entries_map[e["raw"]]
        with open(reg_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(reg, f, allow_unicode=True, sort_keys=False, width=100)
        ids = sorted(set(entries_map.values()))
        print(f"[ok] {reg_path}: {len(reg['entries'])} raw strings -> {len(ids)} canonical ids")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
