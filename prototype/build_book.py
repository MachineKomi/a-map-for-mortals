#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Map for Mortals — v0.0.1 prototype (THIN slice).
HTML/CSS -> PDF via WeasyPrint. All diagrams are hand-authored inline SVG
(WeasyPrint runs no JS, so Mermaid will not render).
7 pages, 2 hero diagrams. British English throughout.
"""

from weasyprint import HTML
import html as _html

# ---------------------------------------------------------------- tokens
PAPER   = "#FBF7F0"   # warm ivory page
PANEL   = "#FFFDF9"   # brighter figure panels
INK     = "#16223B"   # primary navy ink + structure
INK2    = "#4A546B"   # secondary text
INK3    = "#717A8C"   # tertiary / fine captions
ORANGE  = "#DD6A3B"   # caution / decisions / the harder road
ORANGE_T= "#F6E2D4"
PINK    = "#CF6A86"   # insight / warmth / the wiser path
PINK_T  = "#F7DDE6"
NAVY_T  = "#E6EAF1"   # neutral node fills / robustness pill
LINE    = "#E3D6C2"   # warm hairlines
WARM    = "#EFB58A"   # sparing warm accent on dark panels

# ---------------------------------------------------------------- svg utils
def esc(s):
    return _html.escape(str(s), quote=True)

def lines(text, x, y, lh, size, color, weight=400, anchor="middle",
          family="Poppins", italic=False, spacing=None):
    """Centred multi-line text as tspans."""
    sty = (f'font-family:{family};font-size:{size}px;font-weight:{weight};'
           f'fill:{color};'
           + (f'font-style:italic;' if italic else '')
           + (f'letter-spacing:{spacing}px;' if spacing else ''))
    out = [f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{sty}">']
    for i, ln in enumerate(text.split("\n")):
        dy = 0 if i == 0 else lh
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(ln)}</tspan>')
    out.append('</text>')
    return "".join(out)

def rnode(x, y, w, h, text, fill, stroke, tcolor, size=14.5, weight=500,
          r=13, lh=18, sw=1.6, family="Poppins"):
    """Rounded-rect node with centred multi-line label."""
    n = len(text.split("\n"))
    ty = y + h/2 - (n-1)*lh/2 + size*0.34
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            + lines(text, x+w/2, ty, lh, size, tcolor, weight, family=family))

def diamond(cx, cy, w, h, text, fill, stroke, tcolor, size=14, lh=17, weight=500):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    n = len(text.split("\n"))
    ty = cy - (n-1)*lh/2 + size*0.34
    return (f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>'
            + lines(text, cx, ty, lh, size, tcolor, weight))

def pill(cx, cy, w, h, text, fill, stroke, tcolor, size=12.5, weight=500, spacing=0.2):
    x = cx - w/2; y = cy - h/2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" ry="{h/2}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
            + lines(text, cx, cy+size*0.34, 0, size, tcolor, weight, spacing=spacing))

def varrow(x, y1, y2, color=INK2, sw=1.8, dash=False):
    d = 'stroke-dasharray="4 4"' if dash else ''
    head = (f'<polygon points="{x-5},{y2-9} {x+5},{y2-9} {x},{y2-1}" fill="{color}"/>')
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-7}" stroke="{color}" '
            f'stroke-width="{sw}" {d}/>' + head)

def harrow(x1, x2, y, color=ORANGE, sw=1.8):
    head = (f'<polygon points="{x2-9},{y-5} {x2-9},{y+5} {x2-1},{y}" fill="{color}"/>')
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-7}" y2="{y}" stroke="{color}" '
            f'stroke-width="{sw}"/>' + head)

def star(cx, cy, r, color, points=8, sw=1.0):
    import math
    segs = []
    for i in range(points):
        a = math.pi/2 + i*2*math.pi/points
        segs.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+r*math.cos(a):.1f}" '
                    f'y2="{cy-r*math.sin(a):.1f}" stroke="{color}" stroke-width="{sw}"/>')
    return "".join(segs)

def svg(vb_w, vb_h, body, extra=""):
    return (f'<svg viewBox="0 0 {vb_w} {vb_h}" width="100%" '
            f'xmlns="http://www.w3.org/2000/svg" {extra}>{body}</svg>')

def arrow(x1, y1, x2, y2, color=INK2, sw=1.9, gap1=0, gap2=0):
    """Straight arrow from (x1,y1)->(x2,y2) at any angle, with end gaps."""
    import math
    dx, dy = x2-x1, y2-y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx/L, dy/L
    sx, sy = x1+ux*gap1, y1+uy*gap1
    ex, ey = x2-ux*gap2, y2-uy*gap2
    hx, hy = -uy, ux                      # perpendicular
    p1 = (ex, ey)
    p2 = (ex-ux*12+hx*5.5, ey-uy*12+hy*5.5)
    p3 = (ex-ux*12-hx*5.5, ey-uy*12-hy*5.5)
    return (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex-ux*8:.1f}" y2="{ey-uy*8:.1f}" '
            f'stroke="{color}" stroke-width="{sw}"/>'
            f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} '
            f'{p3[0]:.1f},{p3[1]:.1f}" fill="{color}"/>')

# ---------------------------------------------------------------- diagrams
def fig_north_star():
    import math
    W, H = 760, 540
    cx, cy = 380, 270
    R = 196
    sats = [
        "Begin with\nquestions",
        "No ideology\nowns the work",
        "Intellectual\nhonesty",
        "No false\ncertainty",
        "Contradiction\nis data",
        "Probabilities,\nnot guarantees",
        "Name every\ntrade-off's cost",
        "Keep a sense\nof humour",
    ]
    b = []
    # faint outer ring + star points behind centre
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R+44}" fill="none" '
             f'stroke="{LINE}" stroke-width="1.2"/>')
    b.append(star(cx, cy, R+70, LINE, points=16, sw=0.8))
    # spokes + satellites
    pw, ph = 150, 50
    for i, s in enumerate(sats):
        a = math.pi/2 - i*2*math.pi/len(sats)
        sx = cx + R*math.cos(a)
        sy = cy - R*math.sin(a)
        b.append(f'<line x1="{cx}" y1="{cy}" x2="{sx:.1f}" y2="{sy:.1f}" '
                 f'stroke="{LINE}" stroke-width="1.3"/>')
        b.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4.5" fill="{PINK}"/>')
        # label box offset further out along the spoke
        lx = cx + (R+44)*math.cos(a)
        ly = cy - (R+44)*math.sin(a)
        b.append(rnode(lx-pw/2, ly-ph/2, pw, ph, s, NAVY_T, "none", INK,
                       size=13, weight=500, r=11, lh=15.5))
    # centre: the fixed star
    b.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="{INK}"/>')
    b.append(star(cx, cy, 120, WARM, points=12, sw=0.9))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="none" stroke="{PINK}" stroke-width="2"/>')
    b.append(lines("TRUTH", cx, cy-6, 0, 21, "#FFFFFF", 600, spacing=2.5))
    b.append(lines("above all else", cx, cy+18, 0, 13, WARM, 400, italic=True))
    return svg(W, H, "".join(b))

def fig_engine():
    import math
    W, H = 760, 560
    cx, cy = 380, 250
    R = 168
    nodes = {
        'choice':         (cx, cy-R),
        'consequence':    (cx+R, cy),
        'interpretation': (cx, cy+R),
        'character':      (cx-R, cy),
    }
    b = []
    # faint loop ring through the node centres
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{LINE}" '
             f'stroke-width="1.3" stroke-dasharray="3 7"/>')
    # clockwise arrows
    order = ['choice', 'consequence', 'interpretation', 'character']
    for i in range(4):
        c1 = nodes[order[i]]; c2 = nodes[order[(i+1) % 4]]
        b.append(arrow(c1[0], c1[1], c2[0], c2[1], INK2, sw=2.0, gap1=98, gap2=98))
    # centre note
    b.append(lines("round and round —\nfor better,\nor for worse", cx, cy-14, 15.5,
                   10.5, INK3, 500, italic=True))
    # nodes
    nw, nh = 178, 74
    def node(c, title, sub, fill, stroke, tcol, subcol, ring=False):
        x, y = c[0]-nw/2, c[1]-nh/2
        out = (f'<rect x="{x}" y="{y}" width="{nw}" height="{nh}" rx="16" fill="{fill}" '
               f'stroke="{stroke}" stroke-width="{2.6 if ring else 1.8}"/>')
        out += lines(title, c[0], c[1]-5, 0, 14, tcol, 600, spacing=0.6)
        out += lines(sub, c[0], c[1]+15, 0, 10.5, subcol, 400, italic=True)
        return out
    b.append(node(nodes['choice'], "CHOICE", "what you do", ORANGE_T, ORANGE, "#7a3a16", "#9a5436"))
    b.append(node(nodes['consequence'], "CONSEQUENCE", "what follows — partly", NAVY_T, INK, INK, INK3))
    b.append(node(nodes['interpretation'], "INTERPRETATION", "what you make of it", PINK_T, PINK, "#7a2f44", "#a0566e", ring=True))
    b.append(node(nodes['character'], "CHARACTER", "who you become", NAVY_T, INK, INK, INK3))
    # hinge tag beneath interpretation
    ty = cy + R + 66
    b.append(arrow(cx, cy+R+nh/2, cx, ty-17, PINK, sw=1.6, gap1=2))
    b.append(pill(cx, ty, 196, 30, "THE HINGE OF FREEDOM", PINK_T, PINK, "#7a2f44",
                  size=10.5, weight=600, spacing=1.4))
    return svg(W, H, "".join(b))


def build_tree(start_text, steps, action_text, lesson_main, lesson_sub):
    """Shared builder so every decision tree composes identically well."""
    W, H = 770, 884
    spine = 232
    rcol  = 550
    ow, oh = 208, 54
    bx = rcol - ow/2             # off-ramp box left edge
    b = []
    labels = []   # (text, x, y, kind) — drawn LAST so nothing is painted over

    def offramp(y, dw, text):
        vx = spine + dw/2       # diamond's right vertex
        return (harrow(vx+2, bx, y)
                + rnode(bx, y-oh/2, ow, oh, text, ORANGE_T, ORANGE,
                        "#7a3a16", size=12.4, weight=500, r=12, lh=15, sw=1.4))

    # start
    b.append(rnode(spine-170, 6, 340, 58, start_text, PANEL, INK, INK,
                   size=14.5, weight=600, r=14, lh=18))
    b.append(varrow(spine, 64, 104))

    ys = [150, 282, 412, 542]
    for i, st in enumerate(steps):
        cy = ys[i]; dw = st.get('w', 162); dh = st.get('h', 88)
        b.append(diamond(spine, cy, dw, dh, st['q'], PANEL, ORANGE, INK, size=st.get('size', 13.5)))
        b.append(offramp(cy, dw, st['off']))
        no_x = (spine + dw/2 + bx) / 2          # centred in the gap, clear of both
        labels.append((st['no'], no_x, cy-9, 'neg'))
        b.append(varrow(spine, cy+dh/2, cy+dh/2+44))
        labels.append((st['yes'], spine + st.get('yx', 15), cy + dh/2 + 22, 'pos'))

    # action
    b.append(rnode(spine-175, 632, 350, 58, action_text, PINK_T, PINK, "#7a2f44",
                   size=14.5, weight=600, r=14, lh=18))
    # lesson box
    ly = 728
    b.append(f'<rect x="65" y="{ly}" width="640" height="138" rx="18" ry="18" '
             f'fill="{INK}" stroke="{PINK}" stroke-width="2"/>')
    cxx = 385
    b.append(lines("THE LESSON", cxx, ly+30, 0, 12.5, WARM, 600, spacing=3))
    b.append(lines(lesson_main, cxx, ly+66, 0, 17, "#FFFFFF", 600, family="Lora"))
    b.append(lines(lesson_sub, cxx, ly+95, 22, 13.5, "#E9EDF4", 400, family="Lora", italic=True))

    # branch labels on cream chips, drawn last
    for t, x, y, kind in labels:
        w = 9.0*len(t) + 16
        b.append(f'<rect x="{x-w/2}" y="{y-12}" width="{w}" height="19" rx="9.5" '
                 f'fill="{PAPER}" stroke="{LINE}" stroke-width="1"/>')
        col = "#2e7d56" if kind == 'pos' else ORANGE
        b.append(lines(t, x, y+2, 0, 11.5, col, 600))

    return svg(W, H, "".join(b))


def fig_tree_truth():
    return build_tree(
        "There's a hard truth I could speak.",
        [
            {'q': "Is it actually true —\nnot just my version?", 'w': 156, 'h': 88,
             'no': "no", 'yes': "yes", 'off': "Then it isn't truth yet.\nWait, and find out."},
            {'q': "Is it mine\nto say?", 'w': 150, 'h': 84, 'size': 14,
             'no': "no", 'yes': "yes", 'off': "Then leave it\nto whose it is."},
            {'q': "Will it help —\nor only wound?", 'w': 162, 'h': 90,
             'no': "only wound", 'yes': "it helps", 'yx': 19, 'off': "Then silence may be\nthe kinder truth."},
            {'q': "Right moment,\nright manner?", 'w': 168, 'h': 92,
             'no': "not yet", 'yes': "yes", 'off': "Then wait for the moment,\nand choose the manner."},
        ],
        "Then speak it —\nplainly, and with care.",
        "Truth above all is never truth without skill.",
        "We do not soften what is true — only choose\nwhen, how, and whether it is ours to say.")


def fig_tree_grit():
    return build_tree(
        "I'm spent, and it isn't working.\nDo I push on, or let it go?",
        [
            {'q': "Still my goal —\nor just my pride?", 'w': 162, 'h': 88,
             'no': "pride", 'yes': "it's mine", 'yx': 20, 'off': "Then lay it down.\nThat isn't defeat."},
            {'q': "Truly tried —\nor only tired?", 'w': 156, 'h': 86,
             'no': "tired", 'yes': "tried", 'off': "Then rest, and return.\nTiredness lies."},
            {'q': "Any road left\nI've not yet walked?", 'w': 184, 'h': 90,
             'no': "none", 'yes': "there is", 'yx': 18, 'off': "Then change course —\nwisdom, not weakness."},
            {'q': "Can I bear\nthe cost of going on?", 'w': 190, 'h': 96, 'size': 13.2,
             'no': "I can't", 'yes': "I can", 'off': "Then carry what you can.\nSurviving counts."},
        ],
        "Then go on — rested, clear-eyed,\nand free to stop later.",
        "Grit and surrender are both virtues.",
        "Wisdom is knowing which the moment asks for —\nand neither one is a failure.")


def fig_tree_enough():
    return build_tree(
        "There's more within reach.\nDo I take it, or am I already full?",
        [
            {'q': "Do I want it —\nor want to win?", 'w': 160, 'h': 88,
             'no': "to win", 'yes': "I want it", 'yx': 18,
             'off': "Then it's the scoreboard.\nThat hunger has no floor."},
            {'q': "Change my life —\nor just the figure?", 'w': 168, 'h': 86,
             'no': "the figure", 'yes': "my life", 'yx': 16,
             'off': "Then you hold already\nthe life it's selling you."},
            {'q': "The cost in time and peace —\ncan I truly spare it?", 'w': 196, 'h': 92, 'size': 13,
             'no': "I can't", 'yes': "I can",
             'off': "Then the cost is the point.\nName it before you pay."},
            {'q': "If it never came,\nwould I be alright?", 'w': 178, 'h': 90,
             'no': "I'd be lost", 'yes': "I would",
             'off': "Then steady that first.\nNeed makes poor bargains."},
        ],
        "Then reach for it — freely,\nand without fear of the losing.",
        "Enough is not an amount. It's a relationship.",
        "Wanting more isn't the trap; being unable to\nstop wanting is. Know which one is driving.")


def fig_tree_forgive():
    return build_tree(
        "Someone has wronged me.\nDo I forgive, or hold the line?",
        [
            {'q': "Am I after peace —\nor after payback?", 'w': 170, 'h': 88,
             'no': "payback", 'yes': "peace", 'yx': 14,
             'off': "Then anger's at the wheel.\nDon't sign anything yet."},
            {'q': "Forgiving — or just\nletting them back in?", 'w': 184, 'h': 88, 'size': 13.2,
             'no': "back in", 'yes': "forgiving",
             'off': "Then split the two apart.\nForgive freely; trust is earned."},
            {'q': "Is the grudge eating\nme more than them?", 'w': 184, 'h': 90, 'size': 13.2,
             'no': "no", 'yes': "yes",
             'off': "Then you're free either way —\nneither chained nor owed."},
            {'q': "Release the debt, yet\nstill keep the boundary?", 'w': 196, 'h': 92, 'size': 13,
             'no': "I can't", 'yes': "I can",
             'off': "Then guard the line first.\nForgiveness can safely wait."},
        ],
        "Then forgive — to set yourself down,\nnot to let them off.",
        "Forgiveness frees the keeper, not the debtor.",
        "It is not the same as trust, or a door reopened.\nYou may drop the weight and still bar the gate.")


def fig_tree_help():
    return build_tree(
        "Someone I love is struggling.\nDo I step in, or step back?",
        [
            {'q': "Are they asking —\nor am I assuming?", 'w': 172, 'h': 88,
             'no': "assuming", 'yes': "they asked", 'yx': 18,
             'off': "Then ask before you act.\nUninvited help can shame."},
            {'q': "Beyond them —\nor merely hard?", 'w': 168, 'h': 86,
             'no': "just hard", 'yes': "beyond them", 'yx': 22,
             'off': "Then let them meet it.\nHard is how they grow."},
            {'q': "Helping them —\nor helping my guilt?", 'w': 178, 'h': 88, 'size': 13.4,
             'no': "my guilt", 'yes': "truly them",
             'off': "Then sit with the guilt.\nRescue isn't yours to need."},
            {'q': "Does my help build them —\nor bind them to me?", 'w': 198, 'h': 92, 'size': 13,
             'no': "it binds", 'yes': "it builds",
             'off': "Then give the kind that frees.\nGood help ends itself."},
        ],
        "Then step in — fully, and aimed\nat the day they won't need you.",
        "The best help works to make itself unneeded.",
        "To rescue can rob; to abandon can wound.\nLove learns the difference, one moment at a time.")


def fig_convergence():
    """Independent voices fanning into a single shared insight."""
    W, H = 760, 540
    b = []
    sources = [
        ("Heraclitus",     "Greece · ~500 BCE", "No one steps in the\nsame river twice."),
        ("The Dhammapada", "India · ~300 BCE",  "All things arise,\nand all things pass."),
        ("Marcus Aurelius","Rome · ~170 CE",    "Time is a river of\nall that happens."),
        ("Ecclesiastes",   "Hebrew wisdom",     "A season for each thing,\nthen it is gone."),
    ]
    cw, ch = 168, 98
    centers = [96, 288, 480, 664]
    top = 20
    insY = 430
    entry = [302, 360, 420, 478]      # spread entry points on the insight node's top
    # source cards
    for i, (t, era, idea) in enumerate(sources):
        cx = centers[i]
        b.append(rnode(cx-cw/2, top, cw, ch, "", PANEL, INK3, INK, r=12, sw=1.2))
        b.append(lines(t, cx, top+27, 0, 13.5, INK, 600, family="Lora"))
        b.append(lines(era, cx, top+45, 0, 9.5, ORANGE, 600, spacing=0.4))
        b.append(lines(idea, cx, top+66, 15, 11, INK2, 400, italic=True))
    # middle note
    b.append(lines("independently — across centuries and continents —",
                   380, 268, 0, 11, INK3, 500, italic=True))
    # converging arrows
    for i in range(4):
        b.append(arrow(centers[i], top+ch+1, entry[i], insY-3, INK3, sw=1.5, gap1=3, gap2=7))
    # insight node
    b.append(rnode(170, insY, 420, 88, "", PINK_T, PINK, INK, r=18, sw=2.6))
    b.append(lines("Everything passes — so hold it lightly.",
                   380, insY+40, 0, 17.5, INK, 600, family="Lora"))
    b.append(lines("CONVERGENT ACROSS TRADITIONS THAT NEVER MET",
                   380, insY+64, 0, 9.5, "#a05a70", 600, spacing=1.4))
    return svg(W, H, "".join(b))


def fig_cascade():
    """One choice paying out across minutes, months and years."""
    W, H = 760, 432
    b = []
    axisY = 226
    # time axis
    b.append(arrow(198, axisY, 726, axisY, INK2, sw=2.0))
    # the choice
    b.append(rnode(34, axisY-34, 156, 68, "You keep a\nhard promise.",
                   ORANGE_T, ORANGE, "#7a3a16", size=13, weight=600, r=14, lh=16))
    b.append(arrow(190, axisY, 214, axisY, ORANGE, sw=2.2, gap2=2))
    stations = [
        (332, "MINUTES", "up",   "A cost paid now —\ninconvenience, effort."),
        (500, "MONTHS",  "down", "You become known as\ngood for your word."),
        (660, "YEARS",   "up",   "Others build on you;\ntrust quietly compounds."),
    ]
    bw, bh = 200, 60
    for x, label, d, text in stations:
        b.append(f'<line x1="{x}" y1="{axisY-7}" x2="{x}" y2="{axisY+7}" '
                 f'stroke="{INK2}" stroke-width="2"/>')
        b.append(lines(label, x, axisY+(25 if d == "up" else -17), 0, 10, INK3, 600, spacing=1.4))
        cy = axisY-94 if d == "up" else axisY+94
        b.append(rnode(x-bw/2, cy-bh/2, bw, bh, text, PANEL, INK3, INK2,
                       size=11.5, weight=500, r=12, lh=14, sw=1.2))
        if d == "up":
            b.append(arrow(x, axisY-8, x, cy+bh/2+1, INK3, sw=1.4, gap2=2))
        else:
            b.append(arrow(x, axisY+8, x, cy-bh/2-1, INK3, sw=1.4, gap2=2))
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- motifs
def motif(stroke=WARM, node_a=WARM, node_b=PINK, ring=True):
    """Forking path inside a north-star ring."""
    b = []
    cx, cy = 90, 92
    if ring:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="74" fill="none" stroke="{stroke}" '
                 f'stroke-width="1" opacity="0.55"/>')
        b.append(star(cx, cy, 86, stroke, points=12, sw=0.6))
    # stem up then fork
    b.append(f'<path d="M{cx},{cy+50} L{cx},{cy+4}" stroke="{stroke}" stroke-width="2" fill="none"/>')
    b.append(f'<path d="M{cx},{cy+4} C{cx},{cy-18} {cx-34},{cy-18} {cx-40},{cy-42}" '
             f'stroke="{stroke}" stroke-width="2" fill="none"/>')
    b.append(f'<path d="M{cx},{cy+4} C{cx},{cy-18} {cx+34},{cy-18} {cx+40},{cy-42}" '
             f'stroke="{stroke}" stroke-width="2" fill="none"/>')
    b.append(f'<circle cx="{cx-42}" cy="{cy-48}" r="6" fill="{node_a}"/>')
    b.append(f'<circle cx="{cx+42}" cy="{cy-48}" r="6" fill="{node_b}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy+50}" r="4.5" fill="{stroke}"/>')
    return svg(180, 184, "".join(b))

# ---------------------------------------------------------------- HTML pieces
def wisdom_card():
    voices = [
        ("Epictetus", "Stoic Rome", "~125 CE",
         "Some things are in our power; others are not."),
        ("Bhagavad Gita", "Vedic India", "~200 BCE",
         "You have a right to your actions, never to their fruits."),
        ("Shantideva", "Buddhist India", "~700 CE",
         "If it can be solved, why worry? If it cannot, what use is worry?"),
        ("The Serenity Prayer", "modern", "attribution debated",
         "…to accept what I cannot change, courage to change what I can."),
    ]
    cells = ""
    for name, place, era, gloss in voices:
        cells += f"""
        <div class="voice">
          <div class="vname">{esc(name)}</div>
          <div class="vmeta">{esc(place)} · {esc(era)}</div>
          <div class="vgloss">{esc(gloss)}</div>
        </div>"""
    return f"""
    <div class="card">
      <div class="eyebrow">A wisdom node</div>
      <div class="claim">Control what you can;<br/>consent, honestly, to what you cannot.</div>
      <div class="card-sub">The same idea, reached by people who never met —</div>
      <div class="voices">{cells}</div>
      <div class="bend">
        <span class="bend-h">Where it bends.</span>
        Pushed too far, “accept what you can't change” becomes an excuse for
        passivity toward an injustice you could in fact affect. The whole skill
        is telling the two apart.
      </div>
      <div class="pillrow">
        <span class="rpill">Recurrent · cross-traditionally convergent · conditional at the margins</span>
      </div>
    </div>"""

def tradeoff_map():
    rows = [
        ("Comfort", "Growth",   "comfort soothes, then narrows you · growth aches, then widens you"),
        ("Security", "Freedom",  "security can harden into a cage · freedom can thin into a void"),
        ("Harmony", "Honesty",  "harmony can curdle into silence · honesty can sharpen into cruelty"),
        ("Ambition", "Peace",    "ambition can devour the present · peace can sleep through a life"),
        ("Loyalty", "Truth",    "loyalty can defend a lie · truth can break a bond worth keeping"),
    ]
    out = ['<div class="spectra">']
    for l, r, note in rows:
        out.append(f"""
        <div class="spectrum">
          <div class="srow">
            <div class="pole l">{esc(l)}</div>
            <div class="track"></div>
            <div class="pole r">{esc(r)}</div>
          </div>
          <div class="snote">{esc(note)}</div>
        </div>""")
    out.append('</div>')
    return "".join(out)


def scope_grid():
    doms = [
        ("Work & Vocation",     "the safe wage, or the calling?"),
        ("Love & Commitment",   "stay and mend, or leave and grow?"),
        ("Money & Enough",      "more, or enough?"),
        ("Anger & Forgiveness", "hold the line, or lay it down?"),
        ("Grief & Loss",        "hold on, or let them rest?"),
        ("Ambition & Rest",     "climb, or arrive?"),
        ("Friendship",          "the hard word, or the kept peace?"),
        ("Fear & Risk",         "leap, or look again?"),
        ("Pride & Humility",    "stand your ground, or bend?"),
        ("Solitude & Company",  "go it alone, or lean on others?"),
        ("Habit & Will",        "ride the urge, or break it?"),
        ("Certainty & Doubt",   "commit, or keep asking?"),
        ("Self & Others",       "tend yourself, or give yourself away?"),
        ("Time & Mortality",    "plan the years, or live the day?"),
        ("Meaning",             "seek it, or make it?"),
    ]
    accents = [INK, ORANGE, PINK]
    out = ['<div class="scope">']
    for i, (d, f) in enumerate(doms):
        out.append(f'<div class="dom" style="border-top-color:{accents[i%3]}">'
                   f'<div class="d">{esc(d)}</div><div class="f">{esc(f)}</div></div>')
    out.append('</div>')
    return "".join(out)


# ---------------------------------------------------------------- CSS
CSS = f"""
@font-face {{ font-family:'Lora'; src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'); font-weight:400 700; font-style:normal; }}
@font-face {{ font-family:'Lora'; src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'); font-weight:400 700; font-style:italic; }}
@font-face {{ font-family:'Poppins'; src:url('file:///usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf'); font-weight:300; }}
@font-face {{ font-family:'Poppins'; src:url('file:///usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf'); font-weight:400; }}
@font-face {{ font-family:'Poppins'; src:url('file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf'); font-weight:500; }}
@font-face {{ font-family:'Poppins'; src:url('file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:'Poppins'; src:url('file:///usr/share/fonts/truetype/google-fonts/Poppins-Italic.ttf'); font-weight:400; font-style:italic; }}

@page {{
  size: 178mm 254mm;
  margin: 19mm 19mm 17mm 19mm;
  background: {PAPER};
  @top-center {{ content:"A MAP FOR MORTALS  ·  v 0.0.1"; font-family:'Poppins'; font-weight:400;
                 font-size:7.5pt; letter-spacing:2px; color:{INK3}; }}
  @bottom-center {{ content: counter(page); font-family:'Poppins'; font-size:8.5pt; color:{INK3}; }}
}}
@page cover  {{ margin:0; background:{INK}; @top-center{{content:""}} @bottom-center{{content:""}} }}
@page bare   {{ @top-center{{content:""}} @bottom-center{{content:""}} }}

* {{ box-sizing:border-box; }}
html {{ font-family:'Lora'; color:{INK}; }}
body {{ margin:0; }}

.page  {{ page-break-after:always; }}
.cover {{ page:cover; }}
.bare  {{ page:bare; }}

.eyebrow {{ font-family:'Poppins'; font-weight:600; font-size:8.5pt; letter-spacing:3px;
            text-transform:uppercase; color:{ORANGE}; margin-bottom:9px; }}
h1.title {{ font-family:'Lora'; font-weight:600; font-size:30pt; line-height:1.12; margin:0 0 12px; }}
h2.title {{ font-family:'Lora'; font-weight:600; font-size:21pt; line-height:1.15; margin:0 0 14px; }}
p {{ font-size:11.6pt; line-height:1.62; color:{INK2}; margin:0 0 11px; }}
p.lead {{ font-size:12.6pt; color:{INK}; }}
em {{ color:{INK}; }}
.fig {{ margin:6px 0 8px; }}
.cap {{ font-family:'Poppins'; font-weight:400; font-size:8.6pt; line-height:1.5;
        color:{INK3}; text-align:center; margin-top:6px; max-width:150mm; margin-left:auto; margin-right:auto; }}
.cap b {{ color:{INK2}; font-weight:600; }}

/* ---- cover ---- */
.cover-wrap {{ width:178mm; height:254mm; background:{INK}; color:#fff;
  display:flex; flex-direction:column; align-items:center; text-align:center;
  padding:34mm 22mm; position:relative; }}
.cover-eyebrow {{ font-family:'Poppins'; font-weight:500; font-size:9pt; letter-spacing:5px;
  color:{WARM}; text-transform:uppercase; }}
.cover-title {{ font-family:'Lora'; font-weight:600; font-size:42pt; line-height:1.05;
  margin:20px 0 0; color:#fff; }}
.cover-rule {{ width:54px; height:2px; background:{PINK}; margin:22px 0; border:0; }}
.cover-sub {{ font-family:'Lora'; font-style:italic; font-size:13.5pt; line-height:1.5;
  color:#E9EDF4; max-width:118mm; }}
.cover-foot {{ position:absolute; bottom:26mm; left:0; right:0;
  font-family:'Poppins'; font-size:8pt; letter-spacing:3px; color:{INK3}; }}
.cover-motif {{ width:46mm; margin:4mm auto 0; }}

/* ---- foreword ---- */
.drop::first-letter {{ font-family:'Lora'; font-weight:600; font-size:50pt; float:left;
  line-height:0.82; padding:6px 10px 0 0; color:{ORANGE}; }}
.dedication {{ margin-top:30px; padding-top:14px; border-top:1px solid {LINE};
  font-family:'Lora'; font-style:italic; font-size:11.5pt; color:{INK3}; }}

/* ---- wisdom card ---- */
.card {{ border:1.5px solid {LINE}; border-radius:16px; background:{PANEL};
  padding:20px 22px 18px; break-inside:avoid; }}
.claim {{ font-family:'Lora'; font-weight:600; font-size:18.5pt; line-height:1.24;
  color:{INK}; margin:2px 0 14px; }}
.card-sub {{ font-family:'Poppins'; font-size:8.8pt; letter-spacing:1px; color:{INK3};
  text-transform:uppercase; margin-bottom:10px; }}
.voices {{ display:grid; grid-template-columns:1fr 1fr; gap:10px 16px; }}
.voice {{ border-left:2px solid {PINK}; padding:1px 0 1px 11px; }}
.vname {{ font-family:'Lora'; font-weight:600; font-size:11.4pt; color:{INK}; }}
.vmeta {{ font-family:'Poppins'; font-size:7.8pt; letter-spacing:.4px; color:{INK3}; margin:1px 0 3px; }}
.vgloss {{ font-family:'Lora'; font-style:italic; font-size:10.2pt; line-height:1.4; color:{INK2}; }}
.bend {{ margin-top:15px; background:{ORANGE_T}; border-radius:11px; padding:11px 14px;
  font-size:10.4pt; line-height:1.5; color:#6f3618; }}
.bend-h {{ font-family:'Poppins'; font-weight:600; color:{ORANGE}; }}
.pillrow {{ text-align:center; margin-top:15px; }}
.rpill {{ display:inline-block; background:{NAVY_T}; color:{INK}; border-radius:20px;
  padding:7px 16px; font-family:'Poppins'; font-weight:500; font-size:8.8pt; letter-spacing:.3px; }}

/* ---- humour / quote ---- */
.bigq {{ font-family:'Lora'; font-style:italic; font-weight:500; font-size:15pt;
  line-height:1.4; color:{INK}; border-left:3px solid {PINK}; padding:2px 0 2px 18px; margin:4px 0 16px; }}
.p16 {{ background:{PANEL}; border:1.5px solid {LINE}; border-radius:14px; padding:16px 20px;
  margin-top:18px; break-inside:avoid; }}
.p16 .num {{ font-family:'Poppins'; font-weight:700; font-size:9pt; letter-spacing:2px;
  color:{ORANGE}; }}
.p16 .h {{ font-family:'Lora'; font-weight:600; font-size:14pt; color:{INK}; margin:4px 0 8px; }}
.p16 p {{ font-size:10.6pt; margin:0; }}

/* ---- limits ---- */
.limit {{ display:flex; gap:12px; margin-bottom:11px; break-inside:avoid; }}
.limit .dot {{ flex:0 0 auto; width:9px; height:9px; border-radius:50%; background:{ORANGE};
  margin-top:6px; }}
.limit p {{ margin:0; font-size:10.8pt; }}
.limit b {{ color:{INK}; font-weight:600; }}
.colo {{ text-align:center; margin-top:30px; padding-top:20px; border-top:1px solid {LINE}; }}
.colo p {{ font-family:'Poppins'; font-size:8.6pt; letter-spacing:.4px; color:{INK3}; text-align:center; }}
.colo-motif {{ width:30mm; margin:0 auto 12px; }}

/* ---- trade-off spectra ---- */
.spectra {{ margin-top:10px; }}
.spectrum {{ margin-bottom:18px; break-inside:avoid; }}
.srow {{ display:flex; align-items:center; gap:16px; }}
.pole {{ font-family:'Lora'; font-weight:600; font-size:13pt; width:110px; flex:0 0 110px; }}
.pole.l {{ text-align:right; color:#b85a30; }}
.pole.r {{ text-align:left; color:#bf5070; }}
.track {{ flex:1; height:9px; border-radius:5px;
  background:linear-gradient(90deg, {ORANGE} 0%, {LINE} 50%, {PINK} 100%); }}
.snote {{ text-align:center; font-family:'Lora'; font-style:italic; font-size:10pt;
  color:{INK3}; margin-top:7px; }}

/* ---- scope grid ---- */
.scope {{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:24px 16px; margin-top:14px; }}
.dom {{ border-top:2.5px solid {INK}; padding-top:8px; break-inside:avoid; }}
.dom .d {{ font-family:'Lora'; font-weight:600; font-size:11.5pt; color:{INK}; line-height:1.2; }}
.dom .f {{ font-family:'Lora'; font-style:italic; font-size:9.6pt; color:{INK2};
  margin-top:4px; line-height:1.36; }}
"""

# ---------------------------------------------------------------- assemble
def build_html():
    cover = f"""
    <section class="cover">
      <div class="cover-wrap">
        <div class="cover-eyebrow">A field guide to the forks in the road</div>
        <div class="cover-title">A Map<br/>for Mortals</div>
        <hr class="cover-rule"/>
        <div class="cover-sub">or, how to be a human — the forks, the trade-offs,<br/>
          and the gathered wisdom of those who walked ahead.</div>
        <div class="cover-motif">{motif()}</div>
        <div class="cover-foot">VERSION 0.0.1  ·  AN EARLY VERTICAL SLICE</div>
      </div>
    </section>"""

    foreword = f"""
    <section class="page">
      <div class="eyebrow">Foreword</div>
      <h1 class="title">You are here.</h1>
      <p class="lead drop">Every life is a long series of forks. Most of them
        arrive unmarked — no sign, no map, just a feeling that something is being
        decided and you are the one deciding it. This book is an attempt to draw a
        few of those forks before you reach them: to label the roads, to show which
        way each tends to run, and to gather what the people who walked ahead — Stoics
        and Buddhists, poets and parents, the named and the long-forgotten — managed
        to learn along the way.</p>
      <p>It promises no certainties, because life offers none. What it offers are
        <em>tendencies</em>: which choices, on balance and over time, tend to leave a
        person freer, kinder, less haunted. The map is never the territory, and no
        diagram holds a whole human being. But a rough map beats no map, especially
        in the dark.</p>
      <p>This is <em>version 0.0.1</em> — an honest, deliberately thin slice. A handful
        of pages, two finished diagrams, one fully-worked idea. It is not the finished
        corpus, not the completed analysis, and not a final claim about how to live.
        It is the first glimpse of a much larger thing, shown early so its shape can be
        judged and argued with.</p>
      <div class="dedication">For my children — who will redraw it anyway. And for
        anyone who ever wished the unwritten rules came written down.</div>
    </section>"""

    north = f"""
    <section class="page">
      <div class="eyebrow">The North Star</div>
      <h2 class="title">One thing does not move.</h2>
      <p>Every other commitment in this work exists to protect a single fixed point:
        <em>truth above all else</em>. Not virtue, not comfort, not the wish to appear
        wise — truth first, and the rest measured against it. The principles around it
        are how that one star is kept honest.</p>
      <div class="fig">{fig_north_star()}</div>
      <p class="cap">One fixed star, and the principles that orbit to guard it.
        These will <b>sharpen as the work deepens</b> — as real insight is mined from the
        corpus, and from the lessons left by people who spent whole lives learning by
        experience and asking questions. The centre, alone, never changes.</p>
    </section>"""

    engine = f"""
    <section class="page">
      <div class="eyebrow">The engine of a life</div>
      <h2 class="title">How a choice becomes a self.</h2>
      <p>No single choice defines you; the <em>loop</em> does. What you do brings
        consequences you only partly control. How you read those consequences — the one
        move that is almost entirely yours — quietly shapes who you become, and who you
        become is what chooses next time round.</p>
      <div class="fig">{fig_engine()}</div>
      <p class="cap">Most of the wheel turns with or without your consent. The
        <b>interpretation</b> is the hinge of freedom — the same event can harden you or
        deepen you, and that reading, repeated, sets into character.</p>
    </section>"""

    cascade = f"""
    <section class="page">
      <div class="eyebrow">The consequence cascade</div>
      <h2 class="title">A choice keeps paying out.</h2>
      <p>One choice rarely ends where it lands. Its consequences unfold along a line of
        time — some in the first minute, most of them long after you've stopped watching.
        Much of the book is learning to feel the <em>far</em> end of that line while
        standing at the near one.</p>
      <div class="fig">{fig_cascade()}</div>
      <p class="cap">A single kept promise costs you now and rewards you later, mostly out
        of sight. <b>Wisdom plays the long game</b> — and trusts the parts of it that
        arrive after the applause has stopped.</p>
    </section>"""

    node = f"""
    <section class="page">
      <div class="eyebrow">How an idea earns its place</div>
      <h2 class="title">A worked example.</h2>
      <p>The unit of this project is not the quote but the <em>node</em>: a claim, the
        independent voices that reached it, the place it bends, and an honest label for
        how far it can be trusted. Here is one.</p>
      <div class="fig">{wisdom_card()}</div>
      <p class="cap">When an idea surfaces independently across traditions that never
        met, that convergence is a signal worth weighing — <b>evidence of robustness,
        never proof of truth</b>.</p>
    </section>"""

    convergence = f"""
    <section class="page">
      <div class="eyebrow">Convergence</div>
      <h2 class="title">When strangers reach the same shore.</h2>
      <p>The strongest signal a wisdom node can carry is <em>convergence</em>: thinkers
        with no contact, no shared language, no common century, arriving at the same idea
        by different roads. It does not make the idea true — but it makes it hard to
        dismiss as one culture's accident.</p>
      <div class="fig">{fig_convergence()}</div>
      <p class="cap">Four voices, separated by oceans and millennia, settle on one quiet
        claim. The book treats that agreement as <b>resonance to be tested, not a verdict
        to be trusted</b> — and always marks where the agreement frays.</p>
    </section>"""

    tradeoffs = f"""
    <section class="page">
      <div class="eyebrow">The trade-off map</div>
      <h2 class="title">No pole is the answer.</h2>
      <p>Many of life's hardest choices are not good against evil but good against
        good — two things you want, pulling opposite ways. Each pole is a virtue that,
        taken too far, curdles into its own quiet harm. The skill is not picking a side
        once and for all, but knowing where to stand <em>this</em> time.</p>
      <div class="fig">{tradeoff_map()}</div>
      <p class="cap">No arrow points to a correct answer — because none holds for every
        situation. <b>Where you stand is a choice, and it moves with the day.</b></p>
    </section>"""

    tree = f"""
    <section class="page">
      <div class="eyebrow">A decision tree · an ordinary, hard choice</div>
      <h2 class="title">“There's a hard truth I could speak — should I?”</h2>
      <div class="fig">{fig_tree_truth()}</div>
    </section>"""

    tree2 = f"""
    <section class="page">
      <div class="eyebrow">A decision tree · the same shape, a different fork</div>
      <h2 class="title">“Do I push on, or let this go?”</h2>
      <div class="fig">{fig_tree_grit()}</div>
    </section>"""

    tree3 = f"""
    <section class="page">
      <div class="eyebrow">A decision tree · the wanting kind</div>
      <h2 class="title">“I could have more — do I reach for it?”</h2>
      <div class="fig">{fig_tree_enough()}</div>
    </section>"""

    tree4 = f"""
    <section class="page">
      <div class="eyebrow">A decision tree · after someone has hurt you</div>
      <h2 class="title">“Do I forgive, or hold the line?”</h2>
      <div class="fig">{fig_tree_forgive()}</div>
    </section>"""

    tree5 = f"""
    <section class="page">
      <div class="eyebrow">A decision tree · the love that lets go</div>
      <h2 class="title">“Do I step in, or let them learn?”</h2>
      <div class="fig">{fig_tree_help()}</div>
    </section>"""

    mapahead = f"""
    <section class="page">
      <div class="eyebrow">The map ahead</div>
      <h2 class="title">What the finished book will chart.</h2>
      <p>You've now seen the working parts — a fixed star, the loop, a cascade, a node,
        a spectrum, and a gallery of worked forks. The book to come applies them across
        the terrain a life actually crosses. A few of those regions:</p>
      <div class="fig">{scope_grid()}</div>
      <p class="cap">Each region holds many forks; each fork becomes a node like the ones
        in these pages — <b>a claim, its converging voices, the place it bends, and an
        honest label for how far to trust it.</b></p>
    </section>"""

    humour = f"""
    <section class="page">
      <div class="eyebrow">On laughing</div>
      <h2 class="title">Take the work seriously. Yourself, lightly.</h2>
      <p>You are a brief, improbable bundle of stardust with a to-do list. The universe
        is enormous, indifferent, and — once you notice — frequently hilarious. The only
        sane reply is to take the work of living seriously and yourself lightly.</p>
      <p>Marcus Aurelius ran an empire and still began each day reminding himself he'd
        meet idiots, that he would die, and that both were fine. Cicero held that a
        well-aimed joke could carry an argument solemn logic would lose. Nietzsche, who
        stared into the abyss longer than was strictly advisable, distrusted any truth
        that couldn't survive a laugh. Douglas Adams looked at the whole terrifying cosmos
        and printed <em>DON'T PANIC</em> on the cover in large, friendly letters. And every
        good monster-hunter knows that when you're up to your knees in muck and the thing
        in the dark is bigger than you, a grim joke is sometimes the only thing keeping
        your sword-hand steady.</p>
      <div class="p16">
        <div class="num">PRINCIPLE 16</div>
        <div class="h">Keep a sense of humour — most of all in the dark.</div>
        <p>Life is by turns absurd, gruelling, and Kafkaesque; a person who can't laugh
          at it will be broken by it. Wit is not the opposite of seriousness — it's how
          the serious stay sane, and stay kind. We let humour in (dry, humane, never cruel)
          not to make light of suffering, but because laughter is a kind of courage: the
          refusal to let the absurd, the grim, or the merely unfair have the last word.</p>
      </div>
    </section>"""

    limits = f"""
    <section class="page bare">
      <div class="eyebrow">Honest limits</div>
      <h2 class="title">What this prototype is not.</h2>
      <div class="limit"><div class="dot"></div><p><b>Not the finished corpus.</b>
        These pages draw on a handful of sources to show the <em>form</em>. The full work
        will span millennia and many traditions; this shows the shape, not the whole.</p></div>
      <div class="limit"><div class="dot"></div><p><b>Not a completed analysis.</b>
        Every diagram here was composed by hand to demonstrate what a finished node will
        look like — not yet generated from a finished dataset.</p></div>
      <div class="limit"><div class="dot"></div><p><b>Not proof.</b> Recurrence is
        resonance, not truth; convergence is robustness, not certainty; correlation is
        not cause. A choice tilts the odds — it does not command the outcome.</p></div>
      <div class="limit"><div class="dot"></div><p><b>Not the whole story.</b> The written
        record skews literate, powerful, recent and Western. We will widen it deliberately,
        and keep naming the gap rather than hiding it.</p></div>
      <div class="limit"><div class="dot"></div><p><b>Not a finished life.</b> No diagram
        contains a whole human being — temperament, time, place, luck and history all bear
        on every fork. The map is never the territory.</p></div>
      <p style="margin-top:16px;font-style:italic;color:{INK};">What it <em>is</em>:
        an honest first glimpse — the opening sketch of a real book about how people choose,
        suffer, trade off, endure, love, lose, and try to live well.</p>
      <div class="colo">
        <div class="colo-motif">{motif(stroke=INK3, node_a=ORANGE, node_b=PINK)}</div>
        <p>A MAP FOR MORTALS · VERSION 0.0.1 · A LIVING DRAFT</p>
        <p>Convergence is robustness, not truth. Recurrence is resonance, not proof.</p>
      </div>
    </section>"""

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
    <body>{cover}{foreword}{north}{engine}{cascade}{node}{convergence}{tradeoffs}{tree}{tree2}{tree3}{tree4}{tree5}{mapahead}{humour}{limits}</body></html>"""

if __name__ == "__main__":
    html = build_html()
    with open("/home/claude/thin.html", "w") as f:
        f.write(html)
    HTML(string=html, base_url="/home/claude/").write_pdf("/home/claude/thin.pdf")
    print("wrote thin.html and thin.pdf")
