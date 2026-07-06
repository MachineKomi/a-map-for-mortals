#!/usr/bin/env python3
"""fetch_weasyprint.py — fetch the official WeasyPrint standalone Windows executable.

Why: pip-installed weasyprint needs GTK/Pango DLLs that aren't reliably present on
Windows. The WeasyPrint project publishes a self-contained weasyprint.exe with every
release; that is our renderer. This script downloads the pinned release zip from the
official GitHub releases page and places weasyprint.exe in tools/bin/ (gitignored —
run this once per machine).

Usage: python tools/fetch_weasyprint.py
"""
import io
import os
import sys
import urllib.request
import zipfile

VERSION = "v69.0"  # pinned; bump deliberately and re-test the render QA loop
URL = (f"https://github.com/Kozea/WeasyPrint/releases/download/"
       f"{VERSION}/weasyprint-windows.zip")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "tools", "bin", "weasyprint.exe")


def main():
    if os.path.exists(DEST):
        print(f"Already present: {DEST} — delete it first to re-fetch.")
        return 0
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    print(f"Downloading {URL} ...")
    with urllib.request.urlopen(URL) as resp:
        data = resp.read()
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        member = next((n for n in zf.namelist() if n.endswith("weasyprint.exe")), None)
        if member is None:
            print("ERROR: weasyprint.exe not found in the release zip.")
            return 1
        with zf.open(member) as src, open(DEST, "wb") as dst:
            dst.write(src.read())
    print(f"Wrote {DEST} ({os.path.getsize(DEST)} bytes). "
          f"Verify with: tools/bin/weasyprint.exe --version")
    return 0


if __name__ == "__main__":
    sys.exit(main())
