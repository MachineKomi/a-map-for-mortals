#!/usr/bin/env python3
"""validate_units.py — schema validator for the wisdom-graph store.

Validates YAML files in graph/units/, graph/claims/, graph/edges/ against the
canonical schema (A-Map-for-Mortals-METHODOLOGY.md §3). Run before every graph
commit. Exit 0 = clean; 1 = errors; 2 = environment problem.

Usage:
  python3 tools/validate_units.py            # validate the whole store
  python3 tools/validate_units.py PATH ...   # validate specific files/dirs
"""
import sys
import os
import glob

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml --break-system-packages")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRS = [os.path.join(ROOT, "graph", d) for d in ("units", "claims", "edges")]

ENUMS = {
    "type": {"Insight", "Dilemma", "Virtue", "Danger", "Practice", "Consequence"},
    "register": {"aphorism", "principle", "argument", "parable", "metaphor", "poem",
                 "proverb", "narrative"},
    "claim_type": {"empirical", "normative", "prudential", "metaphysical", "observational"},
    "polarity": {"prescriptive", "cautionary", "descriptive"},
    "conditionality": {"universal-ish", "conditional", "contested"},
    "attribution_confidence": {"verified-primary", "verified-secondary", "attested",
                               "dubious", "apocryphal", "communal"},
    "endorsement": {"endorsed", "complicated", "undercut", "ambiguous", "n/a"},
    "copyright_flag": {"public-domain", "in-copyright", "unknown"},
    "life_stage": {"child", "youth", "young-adult", "adult", "midlife", "elder"},
    "claim_status": {"candidate", "adjudicated", "publish-ready"},
    "edge_origin": {"inferred", "curated", "inferred-then-curated"},
    "rating": {"high", "moderate", "low", "very-low"},
    "independence_basis": {"strong", "partial", "weak", "none"},
}

EDGE_TYPES = {"EXPRESSED_BY", "FROM_WORK", "IN_TRADITION", "INFLUENCED", "FUNCTIONAL_ANALOGY",
              "CONVERGES_WITH", "REFINES", "QUALIFIES", "CONTRADICTS",
              "IN_TENSION_WITH", "ADDRESSES", "CULTIVATES", "GUARDS_AGAINST",
              "LEADS_TO", "APPLIES_IN", "SUPPORTED_BY", "UNDERMINED_BY"}

UNIT_REQUIRED = ["id", "type", "paraphrase", "claim_type", "polarity",
                 "conditionality", "attribution_confidence", "copyright_flag",
                 "source", "prov"]
CLAIM_REQUIRED = ["id", "canonical_claim", "claim_type", "member_units", "status", "prov"]
EDGE_REQUIRED = ["id", "type", "from", "to", "origin", "confidence", "method", "prov"]

PROFILE_DIMS = ["recurrence", "source_diversity", "temporal_spread", "claim_type_dim",
                "empirical_support", "contestation", "attribution_integrity",
                "survives_scrutiny"]


def kind_of(data, path):
    i = str(data.get("id", ""))
    if i.startswith("u-"):
        return "unit"
    if i.startswith("c-"):
        return "claim"
    if i.startswith("e-"):
        return "edge"
    if "/units/" in path.replace(os.sep, "/"):
        return "unit"
    if "/claims/" in path.replace(os.sep, "/"):
        return "claim"
    if "/edges/" in path.replace(os.sep, "/"):
        return "edge"
    return None


def check_enum(val, enum_key, field, errors):
    if val is not None and val not in ENUMS[enum_key]:
        errors.append(f"{field}: '{val}' not in {sorted(ENUMS[enum_key])}")


def validate_unit(d, errors, warnings):
    for f in UNIT_REQUIRED:
        if d.get(f) in (None, "", []):
            errors.append(f"missing required field: {f}")
    check_enum(d.get("type"), "type", "type", errors)
    check_enum(d.get("claim_type"), "claim_type", "claim_type", errors)
    check_enum(d.get("polarity"), "polarity", "polarity", errors)
    check_enum(d.get("conditionality"), "conditionality", "conditionality", errors)
    check_enum(d.get("attribution_confidence"), "attribution_confidence",
               "attribution_confidence", errors)
    check_enum(d.get("copyright_flag"), "copyright_flag", "copyright_flag", errors)
    if d.get("register") is not None:
        check_enum(d.get("register"), "register", "register", errors)
    if d.get("endorsement") is not None:
        check_enum(d.get("endorsement"), "endorsement", "endorsement", errors)
    for ls in d.get("life_stages") or []:
        check_enum(ls, "life_stage", "life_stages[]", errors)
    src = d.get("source")
    if isinstance(src, dict):
        if not src.get("author") and d.get("attribution_confidence") != "communal":
            warnings.append("source.author empty on a non-communal unit")
        if not src.get("work"):
            warnings.append("source.work empty")
    elif src is not None:
        errors.append("source must be a mapping")
    # Truth discipline: a verbatim quotation must carry a verification block.
    if d.get("quotation") or d.get("quotation_translation"):
        v = d.get("verification")
        if not isinstance(v, dict) or not v.get("status"):
            warnings.append("quotation present but verification.status missing "
                            "(must exist before this unit can be a print candidate)")
    if d.get("attribution_confidence") == "verified-primary":
        v = d.get("verification") or {}
        if not (isinstance(v, dict) and v.get("checked_against")):
            errors.append("verified-primary requires verification.checked_against "
                          "(URL/edition + matched text) — do not self-certify")


def validate_claim(d, errors, warnings):
    for f in CLAIM_REQUIRED:
        if d.get(f) in (None, "", []):
            errors.append(f"missing required field: {f}")
    check_enum(d.get("claim_type"), "claim_type", "claim_type", errors)
    check_enum(d.get("status"), "claim_status", "status", errors)
    mu = d.get("member_units")
    if isinstance(mu, list):
        for u in mu:
            if not str(u).startswith("u-"):
                errors.append(f"member_units entry '{u}' is not a unit id (u-####)")
    prof = d.get("robustness_profile")
    if d.get("status") == "publish-ready":
        if not isinstance(prof, dict):
            errors.append("publish-ready claim missing robustness_profile")
        else:
            for dim in PROFILE_DIMS:
                cell = prof.get(dim)
                if not isinstance(cell, dict) or not cell.get("rating"):
                    errors.append(f"robustness_profile.{dim} missing or lacks rating")
                elif cell.get("rating") not in ENUMS["rating"]:
                    errors.append(f"robustness_profile.{dim}.rating "
                                  f"'{cell.get('rating')}' invalid")
                elif not cell.get("basis"):
                    warnings.append(f"robustness_profile.{dim} has no basis line")
    elif isinstance(prof, dict):
        for dim in prof:
            if dim not in PROFILE_DIMS:
                warnings.append(f"robustness_profile has unknown dimension '{dim}'")


def validate_edge(d, errors, warnings):
    for f in EDGE_REQUIRED:
        if d.get(f) in (None, ""):
            errors.append(f"missing required field: {f}")
    if d.get("type") is not None and d.get("type") not in EDGE_TYPES:
        errors.append(f"type: '{d.get('type')}' not in {sorted(EDGE_TYPES)}")
    check_enum(d.get("origin"), "edge_origin", "origin", errors)
    if d.get("type") == "CONVERGES_WITH":
        ib = d.get("independence_basis")
        if isinstance(ib, dict):
            check_enum(ib.get("grade"), "independence_basis",
                       "independence_basis.grade", errors)
            if not ib.get("evidence"):
                warnings.append("CONVERGES_WITH independence_basis has no evidence line")
        else:
            errors.append("CONVERGES_WITH requires independence_basis "
                          "{grade, evidence}")


def collect_paths(args):
    paths = []
    targets = args or DEFAULT_DIRS
    for t in targets:
        if os.path.isdir(t):
            paths += sorted(glob.glob(os.path.join(t, "*.yaml"))) \
                   + sorted(glob.glob(os.path.join(t, "*.yml")))
        elif os.path.isfile(t):
            paths.append(t)
    return paths


def main():
    paths = collect_paths(sys.argv[1:])
    if not paths:
        print("No YAML files found to validate (store may be empty — that's fine).")
        return 0
    total_err = 0
    total_warn = 0
    ids_seen = {}
    for p in paths:
        rel = os.path.relpath(p, ROOT)
        try:
            with open(p, "r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except yaml.YAMLError as e:
            print(f"[ERROR] {rel}: YAML parse failure: {e}")
            total_err += 1
            continue
        if not isinstance(data, dict):
            print(f"[ERROR] {rel}: top level must be a mapping")
            total_err += 1
            continue
        errors, warnings = [], []
        kind = kind_of(data, p)
        if kind == "unit":
            validate_unit(data, errors, warnings)
        elif kind == "claim":
            validate_claim(data, errors, warnings)
        elif kind == "edge":
            validate_edge(data, errors, warnings)
        else:
            errors.append("cannot determine kind (id should start u-/c-/e-, "
                          "or file should live under units/claims/edges)")
        uid = data.get("id")
        if uid:
            if uid in ids_seen:
                errors.append(f"duplicate id '{uid}' (also in {ids_seen[uid]})")
            else:
                ids_seen[uid] = rel
        for e in errors:
            print(f"[ERROR] {rel}: {e}")
        for w in warnings:
            print(f"[warn ] {rel}: {w}")
        total_err += len(errors)
        total_warn += len(warnings)
    print(f"\nValidated {len(paths)} file(s): {total_err} error(s), "
          f"{total_warn} warning(s).")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
