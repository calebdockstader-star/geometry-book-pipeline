#!/usr/bin/env python3
"""
check_labels.py v2 -- vector-based collision audit for figure pages.

Reads the compiled PDF directly (no render tricks):
  chars/words  = label ink          (pdfplumber text objects)
  lines/curves/rects = geometry ink (pdfplumber vector objects)

Reports:
  COLLIDE  label bbox touches geometry (dist <= 0.3pt) or another label
  TIGHT    label within 1.2pt of geometry -- legal but worth eyeballing

Usage: python3 check_labels.py <figures.tex> <chapternum>
"""
import re, subprocess, sys, os, math, tempfile, glob
import pdfplumber

TOUCH, TIGHT = 0.3, 1.2

DRIVER = r"""
\documentclass[11pt]{book}
\usepackage[paperwidth=145mm,paperheight=200mm,margin=8mm]{geometry}
\usepackage{brumfiel}
\input{%s}
\renewcommand{\figcap}[1]{}
\pagestyle{empty}
\setcounter{chapter}{%s}
\begin{document}
%s
\end{document}
"""

def seg_rect_dist(x1,y1,x2,y2, rx0,ry0,rx1,ry1):
    """min distance from segment to rectangle (0 if intersecting)."""
    # quick reject/accept via sampling; fine at pt scale
    n = max(2, int(math.hypot(x2-x1, y2-y1) / 1.5))
    best = 1e9
    for i in range(n+1):
        t = i/n
        px, py = x1+t*(x2-x1), y1+t*(y2-y1)
        dx = max(rx0-px, 0, px-rx1)
        dy = max(ry0-py, 0, py-ry1)
        d = math.hypot(dx, dy)
        if d < best: best = d
        if best == 0: return 0
    return best

def flatten_path(path, steps=16):
    """Walk a pdfplumber path, evaluating cubic Beziers instead of chording them.

    A curve's `pts` are only the ON-curve anchors: pdfplumber drops the
    control points.  Joining those anchors with straight lines turns a
    circle into a DIAMOND through its four cardinal points -- which sits up
    to r*(1-cos45) = 0.29r inside the real circle.  Every label correctly
    placed inside a circle then reads as touching that phantom chord, and
    every label just outside one reads as clear when it is not.  The raw
    `path` keeps the control points, so evaluate the Beziers properly.
    Coordinates in `path` are in the same top-down space as `pts`.
    """
    segs, cur, start = [], None, None
    for op in path:
        code = op[0]
        if code == 'm':
            cur = start = op[1]
        elif code == 'l':
            if cur is not None and len(op) > 1:
                segs.append((cur[0], cur[1], op[1][0], op[1][1]))
            cur = op[1] if len(op) > 1 else cur
        elif code in ('c', 'v', 'y'):
            if cur is None:
                continue
            if code == 'c':
                c1, c2, p = op[1], op[2], op[3]
            elif code == 'v':                      # first control = current pt
                c1, c2, p = cur, op[1], op[2]
            else:                                  # 'y': second control = end
                c1, p = op[1], op[2]
                c2 = p
            prev = cur
            for i in range(1, steps + 1):
                t = i / steps
                m = 1 - t
                x = (m*m*m*cur[0] + 3*m*m*t*c1[0] + 3*m*t*t*c2[0] + t*t*t*p[0])
                y = (m*m*m*cur[1] + 3*m*m*t*c1[1] + 3*m*t*t*c2[1] + t*t*t*p[1])
                segs.append((prev[0], prev[1], x, y))
                prev = (x, y)
            cur = p
        elif code == 'h':
            if cur is not None and start is not None:
                segs.append((cur[0], cur[1], start[0], start[1]))
                cur = start
    return segs


def is_white_fill(r):
    """A rect painted white and not stroked: a mask, not ink."""
    if not r.get('fill') or r.get('stroke'):
        return False
    col = r.get('non_stroking_color')
    if col is None:
        return False
    if isinstance(col, (int, float)):
        col = (col,)
    try:
        return all(abs(c - 1) < 1e-6 for c in col)
    except TypeError:
        return False


def covered(seg, rect):
    """Does the segment run through this rect?  (sampled, fine at pt scale)"""
    x1, y1, x2, y2 = seg
    rx0, ry0, rx1, ry1 = rect
    n = max(2, int(math.hypot(x2 - x1, y2 - y1) / 1.0))
    for i in range(n + 1):
        t = i / n
        px, py = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
        if rx0 <= px <= rx1 and ry0 <= py <= ry1:
            return True
    return False


def white_fill_rects(page):
    """Boxes that a TikZ node paints white before setting its text.

    `node[fill=white]` on a path -- the break every dimension line in this
    book has its label sitting in -- is drawn AFTER the path, so the line
    under it is not on the page any more.  The vector audit still sees the
    line's coordinates and reports the label as touching it.  Collect the
    white boxes so the label-vs-geometry test can treat them as erasers.
    """
    return [(r['x0'], r['top'], r['x1'], r['bottom'])
            for r in page.rects if is_white_fill(r)]


def notation_rule(seg, bb, lw):
    """True for a rule that belongs to the label sitting at bb.

    A \\tfrac's bar and a \\sqrt's overbar are thin horizontal TeX rules that
    live INSIDE their own label's box, so every stacked fraction and every
    radical in a figure reads as a collision with 'geometry'.  Drawing ink
    in this book is never thinner than 0.6pt (fig 0.7, tick and rmark 0.6),
    and a real line crossing a label leaves the box on both sides, so a
    sub-0.5pt segment wholly inside the box can only be notation.
    """
    if lw is None or lw >= 0.5:
        return False
    x1, y1, x2, y2 = seg
    if abs(y2 - y1) > 0.2:                      # rules are horizontal
        return False
    return (min(x1, x2) >= bb[0] - 0.05 and max(x1, x2) <= bb[2] + 0.05 and
            min(y1, y2) >= bb[1] - 0.05 and max(y1, y2) <= bb[3] + 0.05)


def geometry_segments(page):
    """[(segment, linewidth)] for every piece of ink on the page.

    The linewidth rides along so the caller can tell a 0.32pt TeX rule set
    inside a label from the 0.6-0.7pt strokes the figures are drawn with.
    """
    segs = []
    for ln in page.lines:
        # Use the real endpoints.  Rebuilding a line as (x0,top)->(x1,bottom)
        # is only correct for lines that DESCEND left-to-right; for an
        # ascending line it yields a phantom segment mirrored about the
        # horizontal, which can miss the true line by tens of points.
        lw = ln.get('linewidth')
        pts = ln.get('pts')
        if pts and len(pts) >= 2:
            for a, b_ in zip(pts, pts[1:]):
                segs.append(((a[0], a[1], b_[0], b_[1]), lw))
        else:
            segs.append(((ln['x0'], ln['top'], ln['x1'], ln['bottom']), lw))
    for r in page.rects:
        if is_white_fill(r):
            continue            # a node's white background paints nothing
        x0,t,x1,b = r['x0'], r['top'], r['x1'], r['bottom']
        # A filled, unstroked rect is a rule or a node background, not a
        # drawn box; give it the height of its own ink so a fraction bar
        # arriving as a rect is recognised too.
        lw = r.get('linewidth')
        if r.get('fill') and not r.get('stroke'):
            lw = min(x1 - x0, b - t)
        segs += [((x0,t,x1,t), lw), ((x1,t,x1,b), lw),
                 ((x1,b,x0,b), lw), ((x0,b,x0,t), lw)]
    for c in page.curves:
        # Prefer the raw path: it still carries the Bezier control points, so
        # the ink can be evaluated exactly instead of guessed at from the
        # on-curve anchors.  flatten_curve stays as the fallback for curves
        # that arrive without a path.
        lw = c.get('linewidth')
        path = c.get('path')
        exact = flatten_path(path) if path else []
        if exact:
            segs += [(s, lw) for s in exact]
            continue
        pts = [(p[0], p[1]) for p in (c.get('pts') or [])]
        segs += [(s, lw) for s in flatten_curve(pts)]
    return segs


def _circum(a, b, c):
    """centre and radius of the circle through three points, or None."""
    d = 2.0 * (a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))
    if abs(d) < 1e-9:
        return None
    sa, sb, sc = a[0]**2+a[1]**2, b[0]**2+b[1]**2, c[0]**2+c[1]**2
    ux = (sa*(b[1]-c[1]) + sb*(c[1]-a[1]) + sc*(a[1]-b[1])) / d
    uy = (sa*(c[0]-b[0]) + sb*(a[0]-c[0]) + sc*(b[0]-a[0])) / d
    return (ux, uy), math.hypot(a[0]-ux, a[1]-uy)


def flatten_curve(pts, samples=8):
    """Turn a curve's point list into segments that follow the ink.

    pdfplumber hands back only the ON-curve points of a path: a 135-degree
    TikZ arc arrives as three points, and joining them with straight chords
    puts phantom ink up to 0.29r INSIDE the real arc.  Every angle numeral
    drawn inside its arc -- which is where the book puts them -- then reads
    as a collision that is not there.  Reconstruct each span as the circular
    arc through it and its neighbour and sample that instead; fall back to
    the chord when the three points are collinear (a genuine polyline).
    """
    out = []
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        nb = pts[i + 2] if i + 2 < len(pts) else (pts[i - 1] if i else None)
        fit = _circum(a, b, nb) if nb is not None else None
        chord = math.hypot(b[0]-a[0], b[1]-a[1])
        # Only bend a span when its neighbour looks like the next sample of the
        # SAME arc: comparable chord lengths and a gentle turn.  A polyline
        # corner (the braces under Fig 3-19, a right-angle box) fails both, and
        # must stay straight or we invent ink outside the drawing.
        smooth = False
        if fit and nb is not None:
            other = math.hypot(nb[0]-b[0], nb[1]-b[1]) or math.hypot(a[0]-nb[0], a[1]-nb[1])
            lo, hi = sorted((max(chord, 1e-6), max(other, 1e-6)))
            turn = abs(math.degrees(math.atan2(b[1]-a[1], b[0]-a[0])
                                    - math.atan2(nb[1]-b[1], nb[0]-b[0])))
            turn = min(turn, 360 - turn)
            smooth = hi / lo <= 3.0 and turn <= 80.0 and fit[1] <= 40 * chord
        if not smooth:
            out.append((a[0], a[1], b[0], b[1]))
            continue
        (cx, cy), r = fit
        t0 = math.atan2(a[1]-cy, a[0]-cx)
        t1 = math.atan2(b[1]-cy, b[0]-cx)
        while t1 - t0 > math.pi:
            t1 -= 2*math.pi
        while t0 - t1 > math.pi:
            t1 += 2*math.pi
        prev = a
        for k in range(1, samples + 1):
            t = t0 + (t1 - t0) * k / samples
            p = (cx + r*math.cos(t), cy + r*math.sin(t))
            out.append((prev[0], prev[1], p[0], p[1]))
            prev = p
    return out

PRIMES = set("′″‴'’")


def merge_scripts(words):
    """Re-join labels that pdfplumber split into pieces.

    `extract_words()` returns $A'$ as ['A', '′'] and $P_1$ as ['P','1']
    because the script sits off the baseline; the label-vs-label test then
    reports every primed or subscripted label as colliding with its own
    script.  A fragment is absorbed into the word on its left only when it
    is horizontally contiguous, vertically overlapping, AND on a different
    baseline (or a bare prime).  Two labels sharing a baseline are never
    merged, so real label-vs-label collisions still report.
    """
    ws = sorted((dict(w) for w in words), key=lambda w: w['x0'])
    out = []
    for w in ws:
        allprime = w['text'] != '' and all(c in PRIMES for c in w['text'])
        # A primed label with more math after it ($b' = 10$) comes back as
        # ['b', '′=10']: the prime splits the word, but the rest of the atom
        # rides on the host's own baseline, so the "same baseline -> real
        # neighbour" rule below would refuse to put it back together and the
        # label would be reported as colliding with itself.  A fragment that
        # STARTS with a prime is the tail of the label on its left.
        leadprime = w['text'][:1] in PRIMES
        host = None
        for h in out:
            # A subscript can run to several characters -- $P_{n-1}$ splits as
            # ['P', 'n-1'] -- so a character count alone cannot decide.  Font
            # size would be the natural test, but asking extract_words for it
            # makes pdfplumber SPLIT words at every size change, which breaks
            # 'n-1' into pieces.  Use the giveaway that survives: a subscript
            # sits a little BELOW its host's baseline -- about a tenth of the
            # font size, never the several points that separate two labels
            # deliberately placed at different heights.
            drop = w['bottom'] - h['bottom']
            subscript = 0.3 < drop < 0.45 * h['height']
            if not (allprime or leadprime or len(w['text']) <= 2 or subscript):
                continue
            gap = w['x0'] - h['x1']
            # A sub- and a superscript STACKED on the same slot ($\pi_1^+$)
            # arrive as 'π+' and '1': pdfplumber sets the superscript next to
            # its host, so the subscript then lands wholly INSIDE the box
            # already claimed -- a gap of about minus its own width.  Absorb a
            # fragment that sits entirely within the host's horizontal span;
            # two labels far enough apart to be separate never do.
            contained = (w['x0'] >= h['x0'] - 0.5 and w['x1'] <= h['x1'] + 0.5)
            # a prime rides ABOVE a subscript ($r_1'$), so it can start to
            # the left of the host's right edge -- allow the overlap.
            if not (contained or
                    (-3.5 if (allprime or leadprime) else -1.0) <= gap <= 1.2):
                continue
            if not (w['top'] < h['bottom'] and h['top'] < w['bottom']):
                continue                      # no vertical overlap
            if not (allprime or leadprime) and \
                    abs(w['bottom'] - h['bottom']) < 0.3:
                continue                      # same baseline -> real neighbour
            if host is None or h['x1'] > host['x1']:
                host = h
        if host is None:
            out.append(w)
        else:
            host['text'] += w['text']
            host['x0'] = min(host['x0'], w['x0'])
            host['x1'] = max(host['x1'], w['x1'])
            if not (allprime or leadprime):
                host['top'] = min(host['top'], w['top'])
                host['bottom'] = max(host['bottom'], w['bottom'])
            # A prime is set in CMSY10, and pdfplumber gives every char that
            # font's ASCENT rather than the glyph's ink.  Measured on
            # ch04 fig. 4-11 at 600 dpi: the prime's box top sits 4.03 pt
            # above the host letter's box top, but its ink sits 0.96 pt
            # BELOW it -- a ~4 pt overshoot, enough to invent a collision
            # for every primed label anchored under a line.  A text letter's
            # box overshoots its ink by only ~1 pt, which is what the
            # TOUCH/TIGHT thresholds are calibrated against.  So take the
            # prime's horizontal extent (advance widths are reliable) and
            # keep the host's vertical extent.
    return out


def main(figfile, chap):
    if not os.path.exists(figfile):
        sys.exit(f'no such figures file: {figfile} -- a missing chapter is a FAIL, not a pass')
    macros = re.findall(r'\\newcommand\{\\(FIG[A-Z]+)\}', open(figfile).read())
    tmp = tempfile.mkdtemp()
    body = "\n".join(rf"\{m}\clearpage" for m in macros)
    src = os.path.join(tmp, 'drv.tex')
    style = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         '..', 'style'))
    figdir = os.path.dirname(os.path.abspath(figfile))
    figname = os.path.basename(figfile)
    figname = figname[:-4] if figname.endswith('.tex') else figname
    open(src,'w').write(DRIVER % (figname, chap, body))
    r = subprocess.run(['tectonic','-Z',f'search-path={style}',
                        '-Z',f'search-path={figdir}',
                        '--outdir',tmp,src],capture_output=True)
    pdf = src.replace('.tex','.pdf')
    if not os.path.exists(pdf):
        sys.exit('driver compile failed:\n'+r.stdout.decode()[-1200:])

    ncol = ntight = 0
    with pdfplumber.open(pdf) as book:
        for name, page in zip(macros, book.pages):
            words = merge_scripts(page.extract_words(extra_attrs=[]) or [])
            segs = geometry_segments(page)
            erasers = white_fill_rects(page)
            probs = []
            # label vs geometry
            for w in words:
                bb = (w['x0'], w['top'], w['x1'], w['bottom'])
                # White boxes this label sits in: the ink under them is gone.
                # Match on the horizontal span plus any vertical overlap --
                # a glyph's REPORTED box is the font's em box, taller than
                # the ink (a radical overshoots its own node fill by 6pt),
                # so demanding vertical containment would never match.
                mask = [e for e in erasers
                        if e[0] <= bb[0] + 0.5 and e[2] >= bb[2] - 0.5 and
                           e[1] < bb[3] and bb[1] < e[3]]
                live = []
                for s, lw in segs:
                    if notation_rule(s, bb, lw):
                        continue                    # the label's own rule
                    if mask and any(covered(s, e) for e in mask):
                        continue                    # painted over by the node
                    live.append(s)
                dmin = min((seg_rect_dist(*s, *bb) for s in live), default=99)
                if dmin <= TOUCH: probs.append(('COLLIDE', w['text'], 'geometry', dmin))
                elif dmin <= TIGHT: probs.append(('TIGHT', w['text'], 'geometry', dmin))
            # label vs label
            for i in range(len(words)):
                for j in range(i+1, len(words)):
                    a, b = words[i], words[j]
                    if (a['x0'] < b['x1']+TOUCH and b['x0'] < a['x1']+TOUCH and
                        a['top'] < b['bottom']+TOUCH and b['top'] < a['bottom']+TOUCH):
                        probs.append(('COLLIDE', a['text'], 'label '+b['text'], 0))
            if probs:
                print(f'  {name}:')
                for kind, t, vs, d in probs:
                    print(f'    [{kind}] "{t}" vs {vs}  d={d:.2f}pt')
                    if kind=='COLLIDE': ncol += 1
                    else: ntight += 1
    print(f'\n{ncol} collisions, {ntight} tight placements '
          f'across {len(macros)} figure blocks')
    return 1 if ncol else 0

if __name__ == '__main__':
    f = sys.argv[1] if len(sys.argv)>1 else 'figures09.tex'
    c = sys.argv[2] if len(sys.argv)>2 else '9'
    sys.exit(main(f, c))
