#!/usr/bin/env python3
"""fetch_fonts.py — fetch the book's fonts (Lora + Poppins, both OFL-licensed).

The SPEC (§3) assumes these exist at a Linux system path; on this machine they don't.
This script downloads them from the official Google Fonts repository into
book/generator/fonts/ (gitignored — run once per machine). The production generator
references them with relative file:/// URLs in @font-face.

Usage: python tools/fetch_fonts.py
"""
import os
import sys
import urllib.request

BASE = "https://github.com/google/fonts/raw/main/ofl"
FILES = {
    "Lora-Variable.ttf": f"{BASE}/lora/Lora%5Bwght%5D.ttf",
    "Lora-Italic-Variable.ttf": f"{BASE}/lora/Lora-Italic%5Bwght%5D.ttf",
    "Poppins-Light.ttf": f"{BASE}/poppins/Poppins-Light.ttf",
    "Poppins-Regular.ttf": f"{BASE}/poppins/Poppins-Regular.ttf",
    "Poppins-Medium.ttf": f"{BASE}/poppins/Poppins-Medium.ttf",
    "Poppins-SemiBold.ttf": f"{BASE}/poppins/Poppins-SemiBold.ttf",
    "Poppins-Bold.ttf": f"{BASE}/poppins/Poppins-Bold.ttf",
    "Poppins-Italic.ttf": f"{BASE}/poppins/Poppins-Italic.ttf",
}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(ROOT, "book", "generator", "fonts")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    ok = 0
    for name, url in FILES.items():
        dest = os.path.join(DEST_DIR, name)
        if os.path.exists(dest):
            print(f"present  {name}")
            ok += 1
            continue
        try:
            print(f"fetching {name} ...")
            with urllib.request.urlopen(url) as resp, open(dest, "wb") as fh:
                fh.write(resp.read())
            ok += 1
        except Exception as e:
            print(f"FAILED   {name}: {e}")
    print(f"\n{ok}/{len(FILES)} fonts in {DEST_DIR}")
    return 0 if ok == len(FILES) else 1


if __name__ == "__main__":
    sys.exit(main())
