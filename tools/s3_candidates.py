#!/usr/bin/env python3
"""s3_candidates.py — S3 candidate-cluster generator (candidate-only, never a decider).

METHODOLOGY §4: S3 clustering is Claude adjudication as the PRIMARY method; embeddings
are an optional cross-check. This script does NOT use embeddings (sentence-transformers
was deliberately deferred — heavy torch). Instead it surfaces candidate same-claim groups
via lightweight lexical overlap within life-domain, for a human/agent adjudicator to
merge or split. Disagreement between this and a later embedding pass → keep split
(splitting is reversible; bad merges poison).

Output: corpus/synthesis/s3-candidates.yaml — a list of candidate groups (≥2 units whose
paraphrases share significant content-word overlap within a domain), plus singletons
count. An adjudicator works through the groups: MERGE (→ one claim) or SPLIT (→ separate).
"""
import collections
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("pyyaml required", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# content-word stoplist (light — keep domain terms, drop glue)
STOP = set("""a an the of to in on at for and or but if then so as is are was were be been being
this that these those it its their his her our your my we us you they them he she him
not no nor with from by into out up down over under again further once here there when
where why how all any both each few more most other some such only own same than too very
can will just should would could may might must one two do does did doing have has had
having what which who whom whose""".split())


def toks(text):
    text = (text or "").lower()
    words = re.findall(r"[a-z']+", text)
    return [w for w in words if w not in STOP and len(w) > 2]


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def main(threshold=0.32):
    # load unclustered units
    clustered = set()
    for f in glob.glob(os.path.join(ROOT, "graph", "claims", "*.yaml")):
        c = yaml.safe_load(open(f, encoding="utf-8"))
        for u in (c or {}).get("member_units", []):
            clustered.add(u)
    units = []
    for f in sorted(glob.glob(os.path.join(ROOT, "graph", "units", "u-0*.yaml"))):
        u = yaml.safe_load(open(f, encoding="utf-8"))
        if u and u.get("id", "").startswith("u-") and u["id"] not in clustered:
            u["_toks"] = toks(u.get("paraphrase", ""))
            units.append(u)
    print(f"unclustered units: {len(units)}")

    # group by primary domain, then find overlap clusters within domain
    by_dom = collections.defaultdict(list)
    for u in units:
        ds = u.get("life_domains") or ["_none"]
        by_dom[ds[0]].append(u)

    groups = []  # list of {domain, units:[{id,paraphrase,tradition,claim_type}], score}
    for dom, ulist in by_dom.items():
        # union-find over units in this domain by pairwise jaccard
        parent = list(range(len(ulist)))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        best_pair_score = {}
        for i in range(len(ulist)):
            for j in range(i + 1, len(ulist)):
                s = jaccard(ulist[i]["_toks"], ulist[j]["_toks"])
                if s >= threshold:
                    union(i, j)
                    best_pair_score[(i, j)] = s
        clusters = collections.defaultdict(list)
        for i in range(len(ulist)):
            clusters[find(i)].append(i)
        for members in clusters.values():
            if len(members) < 2:
                continue
            # average pairwise score
            scores = [best_pair_score[(a, b)] for a in members for b in members
                      if a < b and (a, b) in best_pair_score]
            avg = sum(scores) / len(scores) if scores else 0
            groups.append({
                "domain": dom,
                "avg_overlap": round(avg, 3),
                "units": [{"id": ulist[m]["id"], "tradition": ulist[m].get("tradition", "?"),
                           "claim_type": ulist[m].get("claim_type", "?"),
                           "paraphrase": ulist[m].get("paraphrase", "")}
                          for m in sorted(members)],
            })

    groups.sort(key=lambda g: -g["avg_overlap"])
    in_group = {u["id"] for g in groups for u in g["units"]}
    singletons = len(units) - len(in_group)
    out = {
        "generated": "2026-07-17",
        "method": f"lexical Jaccard overlap >= {threshold} on content words, within primary life-domain. "
                  "CANDIDATE-ONLY — an adjudicator merges or splits each group. Bad merges poison; "
                  "splitting is reversible. Cross-check with embeddings deferred (sentence-transformers "
                  "not installed); disagreement -> keep split.",
        "threshold": threshold,
        "unclustered_total": len(units),
        "candidate_groups": len(groups),
        "units_in_groups": len(in_group),
        "singletons": singletons,
        "groups": groups,
    }
    outpath = os.path.join(ROOT, "corpus", "synthesis", "s3-candidates.yaml")
    with open(outpath, "w", encoding="utf-8") as fh:
        fh.write("# S3 candidate clusters — candidate-only; adjudicate MERGE/SPLIT each.\n")
        yaml.dump(out, fh, sort_keys=False, default_flow_style=False, allow_unicode=True)
    print(f"Wrote {outpath}")
    print(f"  candidate groups: {len(groups)}  units in groups: {len(in_group)}  singletons: {singletons}")


if __name__ == "__main__":
    t = float(sys.argv[1]) if len(sys.argv) > 1 else 0.32
    main(t)
