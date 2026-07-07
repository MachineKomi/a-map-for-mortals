#!/usr/bin/env python3
"""run_gate_tests.py — persistent generator-gate tests (round-3 P0-3/P0-4/P0-5).

The metamorphic proofs in ops/audits/ were scripted-and-captured, not a standing suite.
These test the build_book gates directly and deterministically, so a regression fails CI
rather than silently reopening a fail-open path. No file mutation, no rendering — pure
function-level checks against the live generator.

Usage:  python tools/tests/run_gate_tests.py   (exit 0 = all gates behave)
"""
import os
import sys

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(TOOLS), "book", "generator"))
import build_book as b  # noqa: E402


def expect_raise(fn, needle, label, results):
    try:
        fn()
        results.append((label, False, "did NOT raise"))
    except b.PrintGateError as e:
        ok = needle in str(e)
        results.append((label, ok, "" if ok else f"raised but missing {needle!r}: {e}"))
    except Exception as e:  # noqa: BLE001
        results.append((label, False, f"wrong exception: {type(e).__name__}: {e}"))


def expect_ok(fn, label, results):
    try:
        fn()
        results.append((label, True, ""))
    except Exception as e:  # noqa: BLE001
        results.append((label, False, f"unexpectedly raised: {type(e).__name__}: {e}"))


LICENSED = {"quotation_translation": {"status": "licensed", "spdx": "CC-BY-4.0",
            "commercial_use": True, "attribution_required": True,
            "attribution_text": "trans. X, CC BY 4.0"}}


def main():
    r = []
    U = lambda rights, flag="in-copyright": {"id": "u-t", "copyright_flag": flag, "rights": rights}
    # --- P0-5 rights gate ---
    expect_ok(lambda: b.check_rights(U(LICENSED), "quotation_translation", "c-t"),
              "P0-5 CC-BY-4.0 licensed passes", r)
    expect_raise(lambda: b.check_rights(U({"quotation_translation": {**LICENSED["quotation_translation"], "spdx": "CC-BY-NC-4.0"}}), "quotation_translation", "c-t"),
                 "not on the print-OK whitelist", "P0-5 CC-BY-NC refused", r)
    expect_raise(lambda: b.check_rights(U({"quotation_translation": {**LICENSED["quotation_translation"], "spdx": "CC-BY-SA-4.0"}}), "quotation_translation", "c-t"),
                 "not on the print-OK whitelist", "P0-5 CC-BY-SA refused", r)
    expect_raise(lambda: b.check_rights(U(None), "quotation_translation", "c-t"),
                 "no structured rights record", "P0-5 in-copyright w/o rights refused", r)
    expect_raise(lambda: b.check_rights(U({"quotation": LICENSED["quotation_translation"]}), "quotation_translation", "c-t"),
                 "no structured rights record", "P0-5 licence on wrong field refused", r)
    expect_raise(lambda: b.check_rights(U({"quotation_translation": {k: v for k, v in LICENSED["quotation_translation"].items() if k != "attribution_text"}}), "quotation_translation", "c-t"),
                 "requires attribution", "P0-5 missing attribution refused", r)
    expect_ok(lambda: b.check_rights(U(None, flag="public-domain"), "quotation", "c-t"),
              "P0-5 public-domain unit passes", r)
    # --- P0-4 raw-claim render path disabled ---
    class _Ctx(dict):
        pass
    ctx = {"trace": {"page": "test", "blocks": []}, "used_assertions": [], "page_text": [], "furniture": 0}
    expect_raise(lambda: b.resolve_copy({"claim": "c-0001"}, b.Graph(), ctx, key="claim_label"),
                 "raw-claim render path is disabled", "P0-4 {claim} wrapper refused", r)
    expect_raise(lambda: b.resolve_copy("A bare substantive title", b.Graph(),
                 {"trace": {"page": "test", "blocks": []}, "used_assertions": [], "page_text": [], "furniture": 0}, key="title"),
                 "UNTRACED COPY", "P0-4 bare title (non-furniture) refused", r)
    expect_ok(lambda: b.resolve_copy("Epictetus", b.Graph(),
              {"trace": {"page": "test", "blocks": []}, "used_assertions": [], "page_text": [], "furniture": 0}, key="name"),
              "P0-4 furniture (source name) passes", r)

    fails = [x for x in r if not x[1]]
    for label, ok, msg in r:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {msg}" if msg else ""))
    print(f"\n{len(r) - len(fails)}/{len(r)} gate tests behave correctly.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
