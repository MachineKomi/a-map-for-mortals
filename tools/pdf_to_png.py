#!/usr/bin/env python3
"""pdf_to_png.py — rasterise a PDF to per-page PNGs (pdftoppm replacement).

Why: the mandatory book QA loop is render -> rasterise -> VIEW EVERY PAGE -> fix.
pdftoppm (poppler) is not installed on this machine; pypdfium2 is a pure-pip
equivalent that preserves the same discipline.

Usage:
  python tools/pdf_to_png.py INPUT.pdf OUT_DIR [--dpi 150]

Writes OUT_DIR/page-001.png, page-002.png, ... and prints a per-page manifest.
"""
import argparse
import os
import sys

try:
    import pypdfium2 as pdfium
except ImportError:
    print("ERROR: pypdfium2 is required. Install with: pip install pypdfium2")
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out_dir")
    ap.add_argument("--dpi", type=int, default=150)
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    pdf = pdfium.PdfDocument(args.pdf)
    n = len(pdf)
    for i, page in enumerate(pdf):
        bitmap = page.render(scale=args.dpi / 72)
        img = bitmap.to_pil()
        out = os.path.join(args.out_dir, f"page-{i + 1:03d}.png")
        img.save(out)
        print(f"page {i + 1}/{n} -> {out} {img.size}")
    print(f"\nRasterised {n} page(s) at {args.dpi} dpi. Now VIEW every page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
