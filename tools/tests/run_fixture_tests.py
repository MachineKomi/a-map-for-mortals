#!/usr/bin/env python3
"""run_fixture_tests.py — negative fixtures for the honesty rules (review P0-3/P1-6).

Each case builds a minimal temporary store containing exactly one violation, runs
tools/validate_graph.py against it (via MAP_ROOT), and asserts the validator fails
WITH THE EXPECTED ERROR. A positive control asserts a valid store passes. A gate
without a failing test is a convention; these make the rules executable.

Usage:  python tools/tests/run_fixture_tests.py
Exit 0 = all cases behave correctly; 1 = a rule failed to fire (or fired wrongly).
"""
import os
import shutil
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(TOOLS, "validate_graph.py")

UNIT_OK = """id: u-9001
claim_id: c-9001
type: Insight
paraphrase: "A valid test unit."
quotation: null
quotation_translation: "Twelve ordinary words that form a held quotation for linting purposes here."
source: {author: Tester, work: Fixtures, passage: "1", translator: null, edition_year: 2000, language: en, url: null, urn: null}
tradition: fixture-tradition
era: 2000
register: principle
claim_type: prudential
polarity: prescriptive
conditionality: conditional
life_domains: [fixture-domain]
life_stages: [adult]
endorsement: n/a
attribution_confidence: attested
verification: {status: pending-primary, method: "fixture", checked_against: null, date: null}
copyright_flag: public-domain
prov: {source_report: fixtures, extracted_by: test, pass: 1, date: 2020-01-01}
notes: "fixture"
"""

CLAIM_OK = """id: c-9001
canonical_claim: "A valid test claim."
claim_type: prudential
polarity: prescriptive
conditionality: conditional
member_units: [u-9001]
status: adjudicated
prov: {minted_by: test, date: 2020-01-01}
notes: "fixture"
"""

EDGE_OK = """id: e-9001
type: REFINES
from: c-9001
to: c-9001
origin: curated
confidence: low
method: "fixture"
prov: {minted_by: test, date: 2020-01-01}
notes: "fixture"
"""

SPEC_OK = """id: fx-010
stage: fixtures
sequence: 10
form: prose
refs: [c-9001]
copy:
  title: "A fixture page"
  intro:
    - "Editorial copy that quotes nothing at length."
"""

REG_TRAD = 'entries:\n  - raw: "fixture-tradition"\n    count: 1\n    canonical_id: null\n'
REG_DOM = 'entries:\n  - raw: "fixture-domain"\n    count: 1\n    canonical_id: null\n'

FORK_OK = """id: f-9001
question: "A fixture fork question?"
claim_type_mix: [prudential]
poles:
  - {key: a, claim_ref: c-9001, label: "Pole A"}
  - {key: b, claim_ref: c-9001, label: "Pole B"}
conditions: {supported: [], hypothesised: [{pole: a, when: "a fixture condition"}]}
unresolved: ["a fixture unknown"]
status: poles-mapped
adjudication_refs: ["ops/adjudications/fx.md"]
prov: {minted_by: test, date: 2020-01-01}
"""

ASSERT_OK = """id: a-9001
kind: source-summary
text: "A fixture assertion carrying its caveat phrase."
claim_refs: [c-9001]
mandatory_caveats: ["caveat phrase"]
prohibited_phrasings: []
status: approved-for-fixtures
adjudication_refs: ["ops/adjudications/fx.md"]
prov: {minted_by: test, date: 2020-01-01}
"""


def build_store(root):
    for d in ("graph/units", "graph/claims", "graph/edges", "graph/registries",
              "book/page-specs", "ops/adjudications"):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    w = lambda rel, text: open(os.path.join(root, rel), "w", encoding="utf-8").write(text)
    w("graph/units/u-9001.yaml", UNIT_OK)
    w("graph/claims/c-9001.yaml", CLAIM_OK)
    w("graph/edges/e-9001.yaml", EDGE_OK)
    w("graph/registries/traditions.yaml", REG_TRAD)
    w("graph/registries/domains.yaml", REG_DOM)
    os.makedirs(os.path.join(root, "graph", "assertions"), exist_ok=True)
    w("graph/assertions/a-9001.yaml", ASSERT_OK)
    os.makedirs(os.path.join(root, "graph", "forks"), exist_ok=True)
    w("graph/forks/f-9001.yaml", FORK_OK)
    w("ops/adjudications/fx.md", "fixture adjudication record\n")
    w("book/page-specs/fx-010.yaml", SPEC_OK)
    return w


CASES = [
    ("positive control — valid store passes", None, None, 0, "0 error(s)"),
    ("future provenance date rejected",
     "graph/units/u-9001.yaml", UNIT_OK.replace("date: 2020-01-01", "date: 2099-01-01"),
     1, "future date"),
    ("missing claim member rejected",
     "graph/claims/c-9001.yaml", CLAIM_OK.replace("[u-9001]", "[u-9999]"),
     1, "member unit u-9999 does not exist"),
    ("edge endpoint must exist",
     "graph/edges/e-9001.yaml", EDGE_OK.replace("to: c-9001", "to: c-9999"),
     1, "endpoint to=c-9999 does not exist"),
    ("edge confidence must be an enum",
     "graph/edges/e-9001.yaml", EDGE_OK.replace("confidence: low", "confidence: vibes"),
     1, "confidence 'vibes'"),
    ("id must match filename",
     "graph/units/u-9001.yaml", UNIT_OK.replace("id: u-9001", "id: u-8888"),
     1, "!= filename"),
    ("raw held-quotation text forbidden in copy fields",
     "book/page-specs/fx-010.yaml", SPEC_OK.replace(
         "Editorial copy that quotes nothing at length.",
         "He said: Twelve ordinary words that form a held quotation for linting purposes here."),
     1, "RAW QUOTE IN COPY"),
    ("page-spec refs must exist",
     "book/page-specs/fx-010.yaml", SPEC_OK.replace("[c-9001]", "[c-4242]"),
     1, "ref c-4242 does not exist"),
    ("assertion must carry its mandatory caveat",
     "graph/assertions/a-9001.yaml", ASSERT_OK.replace("carrying its caveat phrase", "missing its promise"),
     1, "does not carry mandatory caveat"),
    ("page body assertion must exist",
     "book/page-specs/fx-010.yaml", SPEC_OK + "body:\n  - assert: a-9002\n",
     1, "body assertion a-9002 does not exist"),
    ("unregistered tradition rejected (registry freeze)",
     "graph/units/u-9001.yaml", UNIT_OK.replace("tradition: fixture-tradition", "tradition: brand-new-freetext"),
     1, "not in graph/registries/traditions.yaml"),
    ("unregistered domain rejected (registry freeze)",
     "graph/units/u-9001.yaml", UNIT_OK.replace("[fixture-domain]", "[fixture-domain, novel-domain]"),
     1, "not in graph/registries/domains.yaml"),
    ("dangling adjudication ref rejected (round-3 P0-2)",
     "graph/assertions/a-9001.yaml", ASSERT_OK.replace("ops/adjudications/fx.md", "ops/adjudications/does-not-exist.md"),
     1, "does not exist on disk"),
    ("dangling relation ref rejected (round-3 P0-2)",
     "graph/assertions/a-9001.yaml", ASSERT_OK.replace("adjudication_refs:", "relation_refs: [e-9999]\nadjudication_refs:"),
     1, "relation_ref e-9999 is not an edge"),
    ("dangling interpretation ref rejected (round-3 P0-2)",
     "graph/assertions/a-9001.yaml", ASSERT_OK.replace("adjudication_refs:", "interpretation_refs: [i-9999]\nadjudication_refs:"),
     1, "interpretation_ref i-9999 does not exist"),
    ("dangling dossier ref rejected (round-3 P0-2)",
     "graph/assertions/a-9001.yaml", ASSERT_OK.replace("adjudication_refs:", "dossier_ref: d-9999\nadjudication_refs:"),
     1, "dossier_ref d-9999 does not exist"),
    ("fork with <2 poles rejected (round-3 P1-forks)",
     "graph/forks/f-9001.yaml", FORK_OK.replace("  - {key: b, claim_ref: c-9001, label: \"Pole B\"}\n", ""),
     1, "at least 2 poles"),
    ("fork pole with missing claim rejected",
     "graph/forks/f-9001.yaml", FORK_OK.replace("claim_ref: c-9001, label: \"Pole B\"", "claim_ref: c-4242, label: \"Pole B\""),
     1, "pole claim_ref c-4242 does not exist"),
    ("fork with bad conditions key rejected",
     "graph/forks/f-9001.yaml", FORK_OK.replace("conditions: {supported: [], hypothesised:", "conditions: {proven: [], hypothesised:"),
     1, "conditions must use only"),
    ("fork claiming dossier-complete without a dossier rejected",
     "graph/forks/f-9001.yaml", FORK_OK.replace("status: poles-mapped", "status: dossier-complete"),
     1, "status 'dossier-complete' but no dossier_ref"),
]


def main():
    failures = 0
    for name, path, content, want_code, want_text in CASES:
        root = tempfile.mkdtemp(prefix="map-fixture-")
        try:
            build_store(root)
            if path:
                open(os.path.join(root, path), "w", encoding="utf-8").write(content)
            env = dict(os.environ, MAP_ROOT=root)
            r = subprocess.run([sys.executable, VALIDATOR], capture_output=True, text=True, env=env)
            ok = (r.returncode == want_code) and (want_text in r.stdout)
            print(f"[{'PASS' if ok else 'FAIL'}] {name}")
            if not ok:
                failures += 1
                print(f"       expected exit {want_code} containing {want_text!r}")
                print(f"       got exit {r.returncode}; output tail: {r.stdout[-400:]}")
        finally:
            shutil.rmtree(root, ignore_errors=True)
    print(f"\n{len(CASES) - failures}/{len(CASES)} fixture cases behave correctly.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
