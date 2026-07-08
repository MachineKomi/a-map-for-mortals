#!/usr/bin/env python3
"""validate_graph.py — cross-file integrity for the wisdom-graph store + page-specs.

Complements validate_units.py (local shape) with the checks the external review
showed were missing (P1-6): referential integrity, ID/filename agreement, date
sanity, page-spec reference validity, and a QUOTE LINTER: raw held-quotation
text is FORBIDDEN in all free-copy fields unconditionally — quotes reach the page
only through gate objects (verbatim_quotes / quote_ref) that the renderer fills.
LIMITS (interim tripwire; Gate B replaces copy-carried text entirely): overlaps
shorter than MIN_OVERLAP_WORDS normalised words pass undetected, and quote objects
still select a claim's first member unit (unsafe after real merges).

Exit 0 = no errors (warnings are counted and reported as debt, never hidden);
1 = errors; 2 = environment problem.

Usage:  python tools/validate_graph.py
"""
import datetime
import hashlib
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required")
    sys.exit(2)

ROOT = os.environ.get("MAP_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def approval_hash(a):
    """Must match build_book.approval_hash exactly (round-3 P0-3). Kept as a small local
    copy so the validator has no import dependency on the generator or its ROOT."""
    payload = json.dumps({
        "text": (a.get("text") or "").strip(),
        "mandatory_caveats": sorted(a.get("mandatory_caveats") or []),
        "prohibited_phrasings": sorted(a.get("prohibited_phrasings") or []),
    }, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
TODAY = datetime.date.today()
MIN_OVERLAP_WORDS = 8  # contiguous words of held quotation appearing in page copy

errors, warnings = [], []


def load_store(sub):
    out = {}
    d = os.path.join(ROOT, "graph", sub)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".yaml") or "EXAMPLE" in f:
            continue
        try:
            data = yaml.safe_load(open(os.path.join(d, f), encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"graph/{sub}/{f}: YAML parse failure: {e}")
            continue
        fid = os.path.splitext(f)[0]
        oid = str(data.get("id", ""))
        if oid != fid:
            errors.append(f"graph/{sub}/{f}: id '{oid}' != filename '{fid}'")
        out[oid] = data
    return out


def check_dates(oid, obj, where):
    def walk(v, path):
        if isinstance(v, dict):
            for k, x in v.items():
                walk(x, f"{path}.{k}")
        elif isinstance(v, datetime.date):
            if v > TODAY:
                errors.append(f"{where}/{oid}: future date {v} at {path}")
        elif isinstance(v, str) and re.fullmatch(r"20\d\d-\d\d-\d\d", v.strip()):
            try:
                if datetime.date.fromisoformat(v.strip()) > TODAY:
                    errors.append(f"{where}/{oid}: future date {v} at {path}")
            except ValueError:
                pass
    walk(obj, "")


def norm_words(s):
    return re.findall(r"[a-z0-9']+", re.sub(r"[‘’]", "'", str(s).lower()))


def main():
    units = load_store("units")
    claims = load_store("claims")
    edges = load_store("edges")

    # --- referential integrity ---
    for cid, c in claims.items():
        for m in c.get("member_units") or []:
            if m not in units:
                errors.append(f"claims/{cid}: member unit {m} does not exist")
            elif units[m].get("claim_id") not in (cid, None):
                warnings.append(f"claims/{cid}: unit {m} points at {units[m].get('claim_id')} (non-reciprocal)")
    for uid, u in units.items():
        cid = u.get("claim_id")
        if cid and cid not in claims:
            errors.append(f"units/{uid}: claim_id {cid} does not exist")
        elif cid and uid not in (claims[cid].get("member_units") or []):
            errors.append(f"units/{uid}: claim {cid} does not list it as a member")
    ok_conf = {"high", "moderate", "low"}
    for eid, e in edges.items():
        for end in ("from", "to"):
            v = e.get(end)
            if v not in claims and v not in units:
                errors.append(f"edges/{eid}: endpoint {end}={v} does not exist")
        if e.get("confidence") not in ok_conf:
            errors.append(f"edges/{eid}: confidence '{e.get('confidence')}' not in {sorted(ok_conf)}")

    # --- date sanity everywhere ---
    for store, name in ((units, "units"), (claims, "claims"), (edges, "edges")):
        for oid, obj in store.items():
            check_dates(oid, obj, name)

    # --- held quotation index for the linter ---
    held = []  # (uid, cid, normalised word list)
    for uid, u in units.items():
        for field in ("quotation", "quotation_translation"):
            q = u.get(field)
            if q and len(norm_words(q)) >= MIN_OVERLAP_WORDS:
                held.append((uid, u.get("claim_id"), norm_words(q)))

    def find_overlap(text):
        w = norm_words(text)
        if len(w) < MIN_OVERLAP_WORDS:
            return None
        grams = {" ".join(w[i:i + MIN_OVERLAP_WORDS]) for i in range(len(w) - MIN_OVERLAP_WORDS + 1)}
        for uid, cid, qw in held:
            for i in range(len(qw) - MIN_OVERLAP_WORDS + 1):
                if " ".join(qw[i:i + MIN_OVERLAP_WORDS]) in grams:
                    return uid, cid
        return None

    # --- registry freeze (P0-4): no unregistered taxonomy values ---
    regdir = os.path.join(ROOT, "graph", "registries")
    def reg_values(name):
        f = os.path.join(regdir, name)
        if not os.path.exists(f):
            return None
        data = yaml.safe_load(open(f, encoding="utf-8")) or {}
        return {str(e.get("raw")) for e in (data.get("entries") or [])}
    known_trad, known_dom = reg_values("traditions.yaml"), reg_values("domains.yaml")
    if known_trad is not None:
        for uid, u in units.items():
            tr = str(u.get("tradition"))
            if tr not in known_trad:
                errors.append(f"units/{uid}: tradition '{tr}' not in graph/registries/traditions.yaml "
                              f"— extend the registry in the same commit (freeze, P0-4)")
            for dm in (u.get("life_domains") or []):
                if known_dom is not None and str(dm) not in known_dom:
                    errors.append(f"units/{uid}: domain '{dm}' not in graph/registries/domains.yaml "
                                  f"— extend the registry in the same commit (freeze, P0-4)")

    # --- assertions store (Gate B): refs exist, approved statuses, caveats intact ---
    adir = os.path.join(ROOT, "graph", "assertions")
    assertions = {}
    if os.path.isdir(adir):
        for f in sorted(os.listdir(adir)):
            if not f.endswith(".yaml"):
                continue
            a = yaml.safe_load(open(os.path.join(adir, f), encoding="utf-8"))
            aid = str(a.get("id"))
            if aid != os.path.splitext(f)[0]:
                errors.append(f"assertions/{f}: id '{aid}' != filename")
            assertions[aid] = a
            for req in ("kind", "text", "status", "adjudication_refs", "prov"):
                if not a.get(req):
                    errors.append(f"assertions/{aid}: missing required field {req}")
            if not (a.get("claim_refs") or a.get("relation_refs") or a.get("interpretation_refs") or a.get("dossier_ref")):
                errors.append(f"assertions/{aid}: no source refs — an assertion must trace to something")
            for cr in (a.get("claim_refs") or []):
                if cr not in claims:
                    errors.append(f"assertions/{aid}: claim_ref {cr} does not exist")
            for cav in a.get("mandatory_caveats") or []:
                if str(cav).lower() not in str(a.get("text", "")).lower():
                    errors.append(f"assertions/{aid}: text does not carry mandatory caveat '{cav}'")
            check_dates(aid, a, "assertions")

    # --- interpretations + dossiers + forks shape (v0.4 contracts) ---
    interp_ids, dossier_ids, fork_ids = set(), set(), set()
    for sub, req in (("interpretations", ("unit_ref", "proposition", "claim_type", "scope", "adjudication_refs", "status")),
                     ("dossiers", ("target_ref", "source_frame", "findings", "permitted_inferences", "prohibited_inferences", "status")),
                     ("forks", ("question", "claim_type_mix", "poles", "conditions", "unresolved", "status", "adjudication_refs"))):
        d = os.path.join(ROOT, "graph", sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if not f.endswith(".yaml") or "EXAMPLE" in f:
                    continue
                obj = yaml.safe_load(open(os.path.join(d, f), encoding="utf-8"))
                oid = str(obj.get("id"))
                {"interpretations": interp_ids, "dossiers": dossier_ids, "forks": fork_ids}[sub].add(oid)
                if oid != os.path.splitext(f)[0]:
                    errors.append(f"{sub}/{f}: id != filename")
                for r in req:
                    if obj.get(r) is None or (r not in ("unresolved",) and not obj.get(r)):
                        errors.append(f"{sub}/{oid}: missing required field {r}")
                if sub == "interpretations" and obj.get("unit_ref") not in units:
                    errors.append(f"{sub}/{oid}: unit_ref {obj.get('unit_ref')} does not exist")
                if sub == "forks":
                    # a fork needs >= 2 poles, each pointing to a real claim; conditions must be
                    # marked supported vs hypothesised; a hypothesised condition may never be
                    # rendered as a finding (enforced at build time, contract stated here).
                    poles = obj.get("poles") or []
                    if len(poles) < 2:
                        errors.append(f"forks/{oid}: needs at least 2 poles")
                    for p in poles:
                        if p.get("claim_ref") not in claims:
                            errors.append(f"forks/{oid}: pole claim_ref {p.get('claim_ref')} does not exist")
                    conds = obj.get("conditions") or {}
                    if set(conds) - {"supported", "hypothesised"}:
                        errors.append(f"forks/{oid}: conditions must use only 'supported'/'hypothesised' keys")
                    if obj.get("head_ref") and obj.get("head_ref") not in claims:
                        errors.append(f"forks/{oid}: head_ref {obj.get('head_ref')} does not exist")
                    # a fork claiming dossier-complete must actually carry a dossier_ref
                    if obj.get("status") == "dossier-complete" and not obj.get("dossier_ref"):
                        errors.append(f"forks/{oid}: status 'dossier-complete' but no dossier_ref")
                check_dates(oid, obj, sub)

    # --- typed-reference RESOLUTION (round-3 P0-2): every typed ref must resolve to a real
    #     object or on-disk file. The validator previously checked only that ref lists were
    #     non-empty, which let 6 assertions cite a nonexistent adjudication file. ---
    def resolve_refs(oid, obj, where):
        for aref in (obj.get("adjudication_refs") or []):
            if not os.path.exists(os.path.join(ROOT, str(aref))):
                errors.append(f"{where}/{oid}: adjudication_ref '{aref}' does not exist on disk")
        for rref in (obj.get("relation_refs") or []):
            if rref not in edges:
                errors.append(f"{where}/{oid}: relation_ref {rref} is not an edge")
        for iref in (obj.get("interpretation_refs") or []):
            if iref not in interp_ids:
                errors.append(f"{where}/{oid}: interpretation_ref {iref} does not exist")
        dref = obj.get("dossier_ref")
        if dref and dref not in dossier_ids:
            errors.append(f"{where}/{oid}: dossier_ref {dref} does not exist")
    for aid, a in assertions.items():
        resolve_refs(aid, a, "assertions")
    # forks resolve their adjudication/relation/dossier refs too (round-3 P1-forks)
    fdir = os.path.join(ROOT, "graph", "forks")
    if os.path.isdir(fdir):
        for f in sorted(os.listdir(fdir)):
            if f.endswith(".yaml") and "EXAMPLE" not in f:
                obj = yaml.safe_load(open(os.path.join(fdir, f), encoding="utf-8"))
                resolve_refs(str(obj.get("id")), obj, "forks")

    # --- approval-manifest integrity (round-3 P0-3): every hash recorded in each edition's
    #     manifest must match the live assertion content, and every referenced assertion must
    #     exist. Catches text/caveat drift in CI without needing to render. ---
    apdir = os.path.join(ROOT, "graph", "approvals")
    if os.path.isdir(apdir):
        for f in sorted(os.listdir(apdir)):
            if not f.endswith(".yaml"):
                continue
            man = yaml.safe_load(open(os.path.join(apdir, f), encoding="utf-8")) or {}
            for aid, sig in (man.get("approvals") or {}).items():
                if aid not in assertions:
                    errors.append(f"approvals/{f}: signs {aid} which does not exist")
                elif approval_hash(assertions[aid]) != sig:
                    errors.append(f"approvals/{f}: {aid} content changed since signing "
                                  f"(manifest {str(sig)[:12]} != live {approval_hash(assertions[aid])[:12]}) — re-adjudicate and re-sign")
    for sub, ids in (("interpretations", interp_ids), ("dossiers", dossier_ids)):
        d = os.path.join(ROOT, "graph", sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".yaml"):
                    obj = yaml.safe_load(open(os.path.join(d, f), encoding="utf-8"))
                    resolve_refs(str(obj.get("id")), obj, sub)

    # --- page-spec validation + quote linter ---
    specdir = os.path.join(ROOT, "book", "page-specs")
    if os.path.isdir(specdir):
        for f in sorted(os.listdir(specdir)):
            if not f.endswith(".yaml"):
                continue
            rel = f"book/page-specs/{f}"
            spec = yaml.safe_load(open(os.path.join(specdir, f), encoding="utf-8"))
            declared = set()
            for q in spec.get("verbatim_quotes") or []:
                ref = q["ref"] if isinstance(q, dict) else q
                declared.add(ref)
                if ref not in claims:
                    errors.append(f"{rel}: verbatim_quotes ref {ref} does not exist")
            for r in spec.get("refs") or []:
                if r not in claims and r not in units:
                    errors.append(f"{rel}: ref {r} does not exist")
            # column quote_refs are declared too
            for col in (spec.get("copy", {}).get("columns") or []):
                if col.get("quote_ref"):
                    declared.add(col["quote_ref"])
            for item in spec.get("body") or []:
                if isinstance(item, dict) and "assert" in item:
                    aid = item["assert"]
                    if aid not in assertions:
                        errors.append(f"{rel}: body assertion {aid} does not exist")
                    elif not str(assertions[aid].get("status", "")).startswith("approved-"):
                        errors.append(f"{rel}: body assertion {aid} is not approved (status: {assertions[aid].get('status')})")
                if isinstance(item, dict) and "quote" in item:
                    q = item["quote"]
                    ref = q["ref"] if isinstance(q, dict) else q
                    declared.add(ref)
                    if ref not in claims:
                        errors.append(f"{rel}: body quote ref {ref} does not exist")
            check_dates(f, spec, "page-specs")

            def lint(v, path):
                if isinstance(v, dict):
                    for k, x in v.items():
                        lint(x, f"{path}.{k}")
                elif isinstance(v, list):
                    for i, x in enumerate(v):
                        lint(x, f"{path}[{i}]")
                elif isinstance(v, str):
                    hit = find_overlap(v)
                    if hit:
                        uid, cid = hit
                        errors.append(
                            f"{rel}: RAW QUOTE IN COPY at {path} — >= {MIN_OVERLAP_WORDS} words of "
                            f"{uid}'s held text; quotation text may only reach the page through "
                            f"gate objects the renderer fills, never copy fields")
            lint(spec.get("copy", {}), "copy")

    print(f"validate_graph: {len(units)} units, {len(claims)} claims, {len(edges)} edges checked")
    for e in errors:
        print(f"[ERROR] {e}")
    for w in warnings:
        print(f"[warn ] {w}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) — warnings are counted debt, not noise.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
