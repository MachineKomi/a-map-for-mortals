#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Map for Mortals — production generator (v0.1: walking-skeleton chapter).

Three-layer separation (SPEC §12): the graph holds the truth; page-specs hold
the curation; this file holds only rendering. It reads book/page-specs/*.yaml,
pulls quotations and sources FROM THE GRAPH (never hand-copied into specs),
enforces the print gate (verbatim quotes require attribution_confidence
verified-primary AND copyright public-domain-or-licensed; the build refuses
otherwise), assembles HTML, and renders via the standalone WeasyPrint exe
(tools/bin/weasyprint.exe — the pip package cannot render on this machine).

Usage:  python book/generator/build_book.py
Output: book/renders/<edition>.html + .pdf  → then run the mandatory QA loop:
        python tools/pdf_to_png.py book/renders/<edition>.pdf book/renders/qa
        and VIEW EVERY PAGE.
"""
import html as _html
import math
import os
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GEN = os.path.join(ROOT, "book", "generator")
SPECS = os.path.join(ROOT, "book", "page-specs")
RENDERS = os.path.join(ROOT, "book", "renders")
WEASY = os.path.join(ROOT, "tools", "bin", "weasyprint.exe")
EDITION = "building-years-v0.1.1"
HEADER = "A MAP FOR MORTALS  ·  VISUAL PROOF v 0.1.1 · CONTENT UNDER RE-ADJUDICATION"

# ---------------------------------------------------------------- tokens (SPEC §2)
PAPER = "#FBF7F0"; PANEL = "#FFFDF9"; INK = "#16223B"; INK2 = "#4A546B"
INK3 = "#717A8C"; ORANGE = "#DD6A3B"; ORANGE_T = "#F6E2D4"; PINK = "#CF6A86"
PINK_T = "#F7DDE6"; NAVY_T = "#E6EAF1"; LINE = "#E3D6C2"; WARM = "#EFB58A"

# ---------------------------------------------------------------- graph access
class PrintGateError(RuntimeError):
    pass


class Graph:
    def __init__(self):
        self.units, self.claims = {}, {}
        for d, store in (("units", self.units), ("claims", self.claims)):
            p = os.path.join(ROOT, "graph", d)
            for f in sorted(os.listdir(p)):
                if not f.endswith(".yaml") or "EXAMPLE" in f:
                    continue
                data = yaml.safe_load(open(os.path.join(p, f), encoding="utf-8"))
                store[data["id"]] = data

    def unit_for(self, cid):
        c = self.claims[cid]
        return self.units[c["member_units"][0]]

    def printable_quote(self, cid, excerpt=None):
        """Return (text, credit) for a verbatim quote, enforcing the print gate.
        An excerpt may shorten with ellipses, but every segment between the
        ellipsis marks must be a verbatim substring of the unit's text —
        checked here, so an excerpt can never alter wording.
        Raises PrintGateError if the unit does not qualify."""
        u = self.unit_for(cid)
        conf = u.get("attribution_confidence")
        flag = u.get("copyright_flag")
        licensed = "cc-by" in str(u.get("notes", "")).lower()
        if conf != "verified-primary" or (flag != "public-domain" and not licensed):
            raise PrintGateError(
                f"PRINT GATE REFUSAL: {u['id']} (for {cid}) is {conf}/{flag} - "
                f"verbatim quotation forbidden. Use a paraphrase block instead.")
        text = u.get("quotation_translation") or u.get("quotation")
        if excerpt:
            for seg in excerpt.replace("...", "…").split("…"):
                seg = seg.strip()
                if seg and seg not in text:
                    raise PrintGateError(
                        f"PRINT GATE REFUSAL: excerpt segment not verbatim in {u['id']}: '{seg[:60]}...'")
            text = excerpt
        s = u.get("source", {})
        credit = f"{s.get('author', '')}, {s.get('work', '')}"
        if s.get("passage"):
            credit += f" {s['passage']}"
        if s.get("translator"):
            credit += f" · trans. {s['translator']}"
        return text, credit


# ---------------------------------------------------------------- svg helpers
def esc(s):
    return _html.escape(str(s), quote=True)


def tlines(text, x, y, lh, size, color, weight=400, anchor="middle",
           family="Poppins", italic=False, spacing=None):
    sty = (f'font-family:{family};font-size:{size}px;font-weight:{weight};fill:{color};'
           + ('font-style:italic;' if italic else '')
           + (f'letter-spacing:{spacing}px;' if spacing else ''))
    out = [f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{sty}">']
    for i, ln in enumerate(str(text).split("\n")):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{esc(ln)}</tspan>')
    out.append('</text>')
    return "".join(out)


def rnode(x, y, w, h, text, fill, stroke, tcolor, size=14.5, weight=500, r=13, lh=18, sw=1.6):
    n = len(str(text).split("\n"))
    ty = y + h / 2 - (n - 1) * lh / 2 + size * 0.34
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            + tlines(text, x + w / 2, ty, lh, size, tcolor, weight))


def arrow(x1, y1, x2, y2, color=INK2, sw=1.9, gap1=0, gap2=0, dash=False):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    sx, sy = x1 + ux * gap1, y1 + uy * gap1
    ex, ey = x2 - ux * gap2, y2 - uy * gap2
    hx, hy = -uy, ux
    d = 'stroke-dasharray="4 4"' if dash else ''
    return (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex - ux * 8:.1f}" y2="{ey - uy * 8:.1f}" '
            f'stroke="{color}" stroke-width="{sw}" {d}/>'
            f'<polygon points="{ex:.1f},{ey:.1f} {ex - ux * 12 + hx * 5.5:.1f},{ey - uy * 12 + hy * 5.5:.1f} '
            f'{ex - ux * 12 - hx * 5.5:.1f},{ey - uy * 12 - hy * 5.5:.1f}" fill="{color}"/>')


def svg(w, h, body):
    return f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


# ---------------------------------------------------------------- form builders
def form_journey_map(spec, g):
    """Stage opener: a road through the chapter's forks (SPEC §6 E)."""
    c = spec["copy"]
    W, H = 760, 470
    b = []
    b.append(f'<path d="M60,410 C220,390 170,300 330,280 S520,250 520,170 S660,90 700,70" '
             f'fill="none" stroke="{LINE}" stroke-width="7" stroke-linecap="round"/>')
    pts = [(60, 410), (255, 330), (415, 262), (540, 160), (700, 70)]
    for i, ((x, y), fork) in enumerate(zip(pts, c["landmarks"])):
        col = PINK if i % 2 else ORANGE
        b.append(f'<circle cx="{x}" cy="{y}" r="7.5" fill="{col}"/>')
        b.append(f'<line x1="{x}" y1="{y - 7}" x2="{x - 11}" y2="{y - 22}" stroke="{col}" stroke-width="2"/>')
        b.append(f'<line x1="{x}" y1="{y - 7}" x2="{x + 11}" y2="{y - 22}" stroke="{col}" stroke-width="2"/>')
        anchor = "start" if x < 560 else "end"
        tx = x + 18 if x < 560 else x - 16
        b.append(tlines(fork, tx, y + 4, 15, 12.5, INK, 600, anchor=anchor))
    cxs, cys, r = 690, 330, 46
    for i in range(8):
        a = math.pi / 2 + i * math.pi / 4
        b.append(f'<line x1="{cxs}" y1="{cys}" x2="{cxs + r * math.cos(a):.0f}" '
                 f'y2="{cys - r * math.sin(a):.0f}" stroke="{LINE}" stroke-width="1"/>')
    b.append(f'<circle cx="{cxs}" cy="{cys}" r="4" fill="{WARM}"/>')
    return svg(W, H, "".join(b))


def form_convergence_map(spec, g):
    """Voices across distance and time meeting at one claim; line style = independence."""
    import textwrap
    c = spec["copy"]
    W, H = 760, 428
    cx, cy = 380, 226
    b = [rnode(cx - 170, cy - 44, 340, 88, c["claim_label"], NAVY_T, INK, INK, size=15, weight=600, lh=19)]
    styles = {"partial": (INK2, False), "weak": (INK3, True)}
    voices = c["voices"]
    n = len(voices)
    for i, v in enumerate(voices):
        vx = 90 + i * (580 / max(1, n - 1))
        vy = 66 if i % 2 == 0 else 106
        col, dash = styles.get(v["independence"], (INK2, False))
        b.append(arrow(vx, vy + 26, cx + (i - (n - 1) / 2) * 56, cy - 48, color=col, sw=1.6, gap2=6, dash=dash))
        b.append(tlines(v["name"], vx, vy - 8, 15, 12.5, INK, 600))
        b.append(tlines(v["meta"], vx, vy + 9, 12, 9.2, INK3, 400))
    frays = "\n".join(textwrap.wrap(c["frays"], 96))
    fh = 22 + 15 * len(frays.split("\n"))
    b.append(rnode(70, H - fh - 8, 620, fh, frays, ORANGE_T, ORANGE, "#6f3618", size=10.5, weight=400, lh=15, sw=1.2))
    ly = H - fh - 30
    b.append(f'<line x1="120" y1="{ly}" x2="160" y2="{ly}" stroke="{INK2}" stroke-width="1.6"/>')
    b.append(tlines("independence: partial (argued)", 262, ly + 4, 0, 9.5, INK3, 400))
    b.append(f'<line x1="400" y1="{ly}" x2="440" y2="{ly}" stroke="{INK3}" stroke-width="1.6" stroke-dasharray="4 4"/>')
    b.append(tlines("lineage (transmitted)", 528, ly + 4, 0, 9.5, INK3, 400))
    return svg(W, H, "".join(b))


def form_spectrum(spec, g):
    """Trade-off spectrum with curdle-notes at both ends (HTML form)."""
    c = spec["copy"]
    rows = []
    for s in c["spectra"]:
        rows.append(
            f'<div class="spectrum"><div class="srow">'
            f'<div class="pole l">{esc(s["left"])}</div><div class="track"></div>'
            f'<div class="pole r">{esc(s["right"])}</div></div>'
            f'<div class="curdles"><span>curdles into {esc(s["left_curdle"])}</span>'
            f'<span>curdles into {esc(s["right_curdle"])}</span></div>'
            f'<div class="snote">{esc(s["note"])}</div></div>')
    return f'<div class="spectra">{"".join(rows)}</div>'


def form_threshold_curve(spec, g):
    """Dose-response with an honest contested band (SPEC §6 C)."""
    c = spec["copy"]
    W, H = 760, 400
    x0, y0, x1, y1 = 90, 330, 700, 60
    b = [f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{INK2}" stroke-width="1.6"/>',
         f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{INK2}" stroke-width="1.6"/>',
         tlines(c["x_label"], (x0 + x1) / 2, y0 + 34, 0, 11, INK2, 500),
         tlines(c["y_label"], x0 - 14, y1 - 18, 0, 11, INK2, 500, anchor="start")]
    pts = []
    for i in range(31):
        t = i / 30
        pts.append((x0 + 26 + t * (x1 - x0 - 60), y0 - 36 - (y0 - y1 - 120) * math.log1p(9 * t) / math.log(10)))
    b.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) +
             f'" fill="none" stroke="{PINK}" stroke-width="3.2"/>')
    pts2 = []
    for i in range(31):
        t = i / 30
        base = math.log1p(9 * min(t, 0.55)) / math.log(10) + (0.05 * (t - 0.55) if t > 0.55 else 0)
        pts2.append((x0 + 26 + t * (x1 - x0 - 60), y0 - 20 - (y0 - y1 - 190) * base))
    b.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts2) +
             f'" fill="none" stroke="{ORANGE}" stroke-width="2.6" stroke-dasharray="7 5"/>')
    bx = x0 + 26 + 0.55 * (x1 - x0 - 60)
    b.append(f'<rect x="{bx - 34:.0f}" y="{y1}" width="88" height="{y0 - y1}" fill="{ORANGE_T}" opacity="0.55"/>')
    b.append(tlines(c["band_label"], bx + 10, y1 + 16, 13, 9.5, "#8a4a26", 500))
    b.append(tlines(c["main_label"], x1 - 4, pts[-1][1] - 16, 13, 10.5, PINK, 600, anchor="end"))
    b.append(tlines(c["minority_label"], x1 - 4, pts2[-1][1] + 26, 13, 10.5, "#b85a30", 600, anchor="end"))
    return svg(W, H, "".join(b))


def form_comparison_columns(spec, g):
    c = spec["copy"]
    cols = []
    for col in c["columns"]:
        q = ""
        if col.get("quote_ref"):
            text, credit = g.printable_quote(col["quote_ref"])
            q = (f'<div class="cquote">{esc(text)}</div>'
                 f'<div class="ccredit">— {esc(credit)}</div>')
        rows = "".join(f'<div class="crow"><div class="ch">{esc(r["h"])}</div>'
                       f'<div class="cv">{esc(r["v"])}</div></div>' for r in col["rows"])
        accent = ORANGE if col.get("accent") == "orange" else PINK
        cols.append(f'<div class="ccol" style="border-top-color:{accent}">'
                    f'<div class="ctitle">{esc(col["title"])}</div>{q}{rows}</div>')
    return f'<div class="compare">{"".join(cols)}</div>'


def form_node_card(spec, g):
    """Wisdom-node card: claim, voices, where it bends, robustness pill; optional evidence strip."""
    c = spec["copy"]
    voices = "".join(
        f'<div class="voice"><div class="vname">{esc(v["name"])}</div>'
        f'<div class="vmeta">{esc(v["meta"])}</div>'
        f'<div class="vgloss">{esc(v["gloss"])}</div></div>' for v in c["voices"])
    ev = ""
    if c.get("evidence"):
        items = "".join(f'<div class="erow"><span class="edot"></span><p>{esc(e)}</p></div>' for e in c["evidence"])
        ev = f'<div class="estrip"><div class="ehead">{esc(c.get("evidence_head", "What the studies add"))}</div>{items}</div>'
    return (f'<div class="card"><div class="card-sub">{esc(c["kicker"])}</div>'
            f'<div class="claim">{esc(c["claim_label"])}</div>'
            f'<div class="voices">{voices}</div>'
            f'<div class="bend"><span class="bend-h">Where it bends · </span>{esc(c["bend"])}</div>{ev}'
            f'<div class="pillrow"><span class="rpill">{esc(c["pill"])}</span></div></div>')


def form_ladder(spec, g):
    """Progression rungs, bottom to top (SPEC §6 C)."""
    c = spec["copy"]
    W = 760
    rungs = c["rungs"]
    H = 62 * len(rungs) + 30
    b = []
    for i, r in enumerate(rungs):
        y = H - 56 - i * 58
        highlight = (i == len(rungs) - 1)
        fill = PINK_T if highlight else PANEL
        stroke = PINK if highlight else LINE
        b.append(rnode(150, y, 470, 46, r, fill, stroke, INK, size=12,
                       weight=600 if highlight else 500, lh=15, sw=1.4))
        if i < len(rungs) - 1:
            b.append(arrow(660, y + 8, 660, y - 16, color=INK3, sw=1.4))
        b.append(tlines(str(i + 1), 122, y + 29, 0, 12, INK3, 600))
    return svg(W, H, "".join(b))


FORMS = {
    "journey-map": form_journey_map,
    "convergence-map": form_convergence_map,
    "trade-off-spectrum": form_spectrum,
    "threshold-curve": form_threshold_curve,
    "comparison-columns": form_comparison_columns,
    "node-card": form_node_card,
    "ladder": form_ladder,
}


# ---------------------------------------------------------------- page assembly
def quote_block(g, q):
    cid, excerpt = (q["ref"], q.get("excerpt")) if isinstance(q, dict) else (q, None)
    text, credit = g.printable_quote(cid, excerpt)
    return f'<div class="bigq">{esc(text)}<div class="qcredit">— {esc(credit)}</div></div>'


def render_page(spec, g):
    c = spec.get("copy", {})
    body = [f'<div class="page" id="{esc(spec["id"])}">']
    if c.get("eyebrow"):
        body.append(f'<div class="eyebrow">{esc(c["eyebrow"])}</div>')
    if c.get("title"):
        tag = "h1" if spec.get("form") == "journey-map" else "h2"
        body.append(f'<{tag} class="title">{esc(c["title"])}</{tag}>')
    intro = c.get("intro", [])
    for i, para in enumerate(intro):
        cls = ' class="lead"' if i == 0 else ""
        body.append(f'<p{cls}>{para}</p>')
    for q in spec.get("verbatim_quotes", []):
        body.append(quote_block(g, q))
    if spec.get("form") and spec["form"] != "prose":
        fig = FORMS[spec["form"]](spec, g)
        body.append(f'<div class="fig">{fig}</div>')
    if c.get("caption"):
        body.append(f'<div class="cap">{c["caption"]}</div>')
    for para in c.get("outro", []):
        body.append(f'<p>{para}</p>')
    if c.get("lesson"):
        body.append(f'<div class="lesson">{esc(c["lesson"])}</div>')
    body.append('</div>')
    return "".join(body)


# ---------------------------------------------------------------- css
def css():
    F = "file:///" + GEN.replace("\\", "/") + "/fonts"
    return f"""
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Variable.ttf'); font-weight:400; }}
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Variable.ttf'); font-weight:600; }}
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Variable.ttf'); font-weight:700; }}
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Italic-Variable.ttf'); font-weight:400; font-style:italic; }}
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Italic-Variable.ttf'); font-weight:500; font-style:italic; }}
@font-face {{ font-family:'Lora'; src:url('{F}/Lora-Italic-Variable.ttf'); font-weight:600; font-style:italic; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-Light.ttf'); font-weight:300; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-Regular.ttf'); font-weight:400; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-Medium.ttf'); font-weight:500; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-SemiBold.ttf'); font-weight:600; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:'Poppins'; src:url('{F}/Poppins-Italic.ttf'); font-weight:400; font-style:italic; }}

@page {{
  size: 178mm 254mm;
  margin: 19mm 19mm 17mm 19mm;
  background: {PAPER};
  @top-center {{ content:"{HEADER}"; font-family:'Poppins'; font-weight:400;
                 font-size:7.5pt; letter-spacing:2px; color:{INK3}; }}
  @bottom-center {{ content: counter(page); font-family:'Poppins'; font-size:8.5pt; color:{INK3}; }}
}}
* {{ box-sizing:border-box; }}
html {{ font-family:'Lora'; color:{INK}; }}
body {{ margin:0; }}
.page {{ page-break-after:always; }}
.eyebrow {{ font-family:'Poppins'; font-weight:600; font-size:8.5pt; letter-spacing:3px;
            text-transform:uppercase; color:{ORANGE}; margin-bottom:9px; }}
h1.title {{ font-family:'Lora'; font-weight:600; font-size:29pt; line-height:1.12; margin:0 0 12px; }}
h2.title {{ font-family:'Lora'; font-weight:600; font-size:20pt; line-height:1.16; margin:0 0 12px; }}
p {{ font-size:11.2pt; line-height:1.6; color:{INK2}; margin:0 0 10px; }}
p.lead {{ font-size:12.2pt; color:{INK}; }}
em {{ color:{INK}; }}
.fig {{ margin:8px 0 6px; break-inside:avoid; }}
.cap {{ font-family:'Poppins'; font-size:8.6pt; line-height:1.5; color:{INK3}; text-align:center;
        margin:6px auto 0; max-width:150mm; }}
.cap b {{ color:{INK2}; font-weight:600; }}
.lesson {{ margin-top:14px; background:{NAVY_T}; border-radius:12px; padding:12px 16px;
  font-family:'Lora'; font-style:italic; font-size:11.5pt; color:{INK}; break-inside:avoid; }}
.bigq {{ font-family:'Lora'; font-style:italic; font-weight:500; font-size:13.5pt; line-height:1.45;
  color:{INK}; border-left:3px solid {PINK}; padding:2px 0 2px 16px; margin:6px 0 14px; break-inside:avoid; }}
.qcredit {{ font-family:'Poppins'; font-style:normal; font-size:8.2pt; letter-spacing:.5px;
  color:{INK3}; margin-top:6px; }}

/* node card */
.card {{ border:1.5px solid {LINE}; border-radius:16px; background:{PANEL};
  padding:18px 20px 16px; break-inside:avoid; }}
.claim {{ font-family:'Lora'; font-weight:600; font-size:16.5pt; line-height:1.24; color:{INK}; margin:2px 0 12px; }}
.card-sub {{ font-family:'Poppins'; font-size:8.6pt; letter-spacing:1px; color:{INK3};
  text-transform:uppercase; margin-bottom:8px; }}
.voices {{ display:grid; grid-template-columns:1fr 1fr; gap:9px 15px; }}
.voice {{ border-left:2px solid {PINK}; padding:1px 0 1px 10px; }}
.vname {{ font-family:'Lora'; font-weight:600; font-size:10.8pt; color:{INK}; }}
.vmeta {{ font-family:'Poppins'; font-size:7.6pt; letter-spacing:.4px; color:{INK3}; margin:1px 0 3px; }}
.vgloss {{ font-family:'Lora'; font-style:italic; font-size:9.8pt; line-height:1.4; color:{INK2}; }}
.bend {{ margin-top:13px; background:{ORANGE_T}; border-radius:11px; padding:10px 13px;
  font-size:10pt; line-height:1.5; color:#6f3618; }}
.bend-h {{ font-family:'Poppins'; font-weight:600; color:{ORANGE}; }}
.pillrow {{ text-align:center; margin-top:13px; }}
.rpill {{ display:inline-block; background:{NAVY_T}; color:{INK}; border-radius:20px;
  padding:6px 15px; font-family:'Poppins'; font-weight:500; font-size:8.6pt; letter-spacing:.3px; }}
.estrip {{ margin-top:13px; border-top:1px solid {LINE}; padding-top:10px; }}
.ehead {{ font-family:'Poppins'; font-weight:600; font-size:8.4pt; letter-spacing:1.5px;
  text-transform:uppercase; color:{INK3}; margin-bottom:7px; }}
.erow {{ display:flex; gap:10px; margin-bottom:6px; }}
.erow .edot {{ flex:0 0 auto; width:8px; height:8px; border-radius:50%; background:{ORANGE}; margin-top:5px; }}
.erow p {{ margin:0; font-size:9.6pt; line-height:1.45; }}

/* spectrum */
.spectra {{ margin-top:8px; }}
.spectrum {{ margin-bottom:20px; break-inside:avoid; }}
.srow {{ display:flex; align-items:center; gap:15px; }}
.pole {{ font-family:'Lora'; font-weight:600; font-size:12.5pt; width:118px; flex:0 0 118px; }}
.pole.l {{ text-align:right; color:{INK}; }}
.pole.r {{ text-align:left; color:{INK}; }}
.track {{ flex:1; height:9px; border-radius:5px;
  background:linear-gradient(90deg, {NAVY_T} 0%, {LINE} 50%, {NAVY_T} 100%); }}
.curdles {{ display:flex; justify-content:space-between; margin:5px 128px 0;
  font-family:'Poppins'; font-size:8pt; color:{INK3}; }}
.snote {{ text-align:center; font-family:'Lora'; font-style:italic; font-size:10pt;
  color:{INK3}; margin-top:6px; }}

/* comparison columns */
.compare {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:8px; }}
.ccol {{ border-top:3px solid; padding-top:10px; break-inside:avoid; }}
.ctitle {{ font-family:'Lora'; font-weight:600; font-size:13.5pt; color:{INK}; margin-bottom:8px; }}
.cquote {{ font-family:'Lora'; font-style:italic; font-size:10.6pt; line-height:1.5; color:{INK}; }}
.ccredit {{ font-family:'Poppins'; font-size:7.6pt; letter-spacing:.4px; color:{INK3}; margin:5px 0 10px; }}
.crow {{ margin-bottom:8px; }}
.ch {{ font-family:'Poppins'; font-weight:600; font-size:7.8pt; letter-spacing:1.2px;
  text-transform:uppercase; color:{INK3}; }}
.cv {{ font-family:'Lora'; font-size:10.2pt; line-height:1.45; color:{INK2}; }}
"""


# ---------------------------------------------------------------- build
def main():
    g = Graph()
    specs = []
    for f in sorted(os.listdir(SPECS)):
        if f.endswith(".yaml"):
            specs.append(yaml.safe_load(open(os.path.join(SPECS, f), encoding="utf-8")))
    specs.sort(key=lambda s: s["sequence"])
    if not specs:
        print("No page-specs found - nothing to build.")
        return 1
    try:
        pages = [render_page(s, g) for s in specs]
    except PrintGateError as e:
        print(str(e))
        return 1
    html_doc = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
                f'<title>A Map for Mortals - {EDITION}</title><style>{css()}</style></head>'
                f'<body>{"".join(pages)}</body></html>')
    os.makedirs(RENDERS, exist_ok=True)
    hp = os.path.join(RENDERS, f"{EDITION}.html")
    pp = os.path.join(RENDERS, f"{EDITION}.pdf")
    open(hp, "w", encoding="utf-8", newline="\n").write(html_doc)
    r = subprocess.run([WEASY, hp, pp], capture_output=True, text=True)
    if r.returncode != 0:
        print("WeasyPrint failed:\n", r.stderr[-3000:])
        return 1
    print(f"Rendered {len(specs)} page-specs -> {pp}")
    print("NOW RUN THE QA LOOP: python tools/pdf_to_png.py \"%s\" \"%s\" --dpi 110 - and view every page."
          % (pp, os.path.join(RENDERS, "qa")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
