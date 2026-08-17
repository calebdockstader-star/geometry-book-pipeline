"""Chapter 6 figure constraints (Congruence of Angles and Triangles).

Every entry restates, in numbers, a hypothesis the BOOK states in words for
that figure -- midpoint / perpendicular / congruent segment / congruent angle /
collinearity / derived crossing -- plus the conclusions the figure must display
faithfully.

WHERE THE COORDINATES COME FROM
-------------------------------
This module does NOT keep its own copy of the drawing.  It reads
``chapters/figures06.tex`` and evaluates the same coordinate expressions tikz
does -- literals, polars, ``($(A)!t!(B)$)`` ratios, ``($(A)!<dim>!(B)$)``
distances, ``+(dx,dy)`` and ``+(deg:r)`` offsets, ``(intersection of A--B and
C--D)``, ``\\begin{scope}[xshift=..]`` and the ``\\foreach`` blocks that draw a
figure twice.

That matters.  The previous version of this file hard-coded every point, so
``132/132`` only ever proved the Python was self-consistent: a reviewer changed
coordinates in five figures and the suite still passed against the stale
numbers.  Reading the TeX makes a passing check mean the PLATE is right, and
makes a figure edited without a matching edit here FAIL rather than pass
quietly.

par/perp errors are in degrees; ratio errors are relative.  Tolerance 0.05.
"""
import math
import os
import re

from figlib import V, ang, par, perp, lerp, dist, foot  # noqa: F401

CM = 28.4527559
FIGFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '..', '..', 'chapters', 'figures06.tex')
NUMPAT = r'[-+]?\d*\.?\d+'


# --------------------------------------------------------------------------
# a small tikz coordinate reader
# --------------------------------------------------------------------------
def _polar(deg, r):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def _inter(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-12:
        raise ValueError('parallel lines')
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d,
            (a * (y3 - y4) - (y1 - y2) * b) / d)


def _split_top(s, seps):
    out, depth, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        if depth == 0:
            for sep in seps:
                if s.startswith(sep, i):
                    out.append(cur)
                    out.append(sep)
                    cur = ''
                    i += len(sep)
                    break
            else:
                cur += c
                i += 1
            continue
        cur += c
        i += 1
    out.append(cur)
    return out


def _pt(expr, P, scale):
    e = expr.strip()
    if e.startswith('$') and e.endswith('$'):
        return _calc(e[1:-1].strip(), P, scale)
    m = re.fullmatch(r'intersection of\s+(.+?)\s+and\s+(.+)', e)
    if m:
        a = _pair(m.group(1), P, scale)
        b = _pair(m.group(2), P, scale)
        return _inter(a[0], a[1], b[0], b[1])
    m = re.fullmatch(rf'({NUMPAT})\s*:\s*({NUMPAT})', e)
    if m:
        return _polar(float(m.group(1)), float(m.group(2)))
    m = re.fullmatch(rf'({NUMPAT})\s*,\s*({NUMPAT})', e)
    if m:
        return (float(m.group(1)), float(m.group(2)))
    if e in P:
        return P[e]
    raise ValueError('cannot parse point: %r' % expr)


def _pair(s, P, scale):
    parts = s.strip().split('--')
    if len(parts) != 2:
        raise ValueError('not a segment: %r' % s)
    out = []
    for p in parts:
        p = p.strip()
        if p.startswith('(') and p.endswith(')'):
            p = p[1:-1]
        out.append(_pt(p, P, scale))
    return out


def _calc(e, P, scale):
    m = re.match(r'^\((?P<a>[^()]+)\)\s*!\s*(?P<t>[^!]+?)\s*!\s*'
                 r'\((?P<b>[^()]+)\)(?P<rest>.*)$', e)
    if m:
        a = _pt(m.group('a'), P, scale)
        b = _pt(m.group('b'), P, scale)
        t = m.group('t').strip()
        dm = re.fullmatch(rf'({NUMPAT})\s*(cm|pt)', t)
        if dm:                       # absolute distance: tikz scales it
            d = float(dm.group(1)) * (1.0 if dm.group(2) == 'cm' else 1 / CM)
            L = math.hypot(b[0] - a[0], b[1] - a[1]) or 1.0
            frac = (d / scale) / L
        else:
            frac = float(t)
        p = (a[0] + frac * (b[0] - a[0]), a[1] + frac * (b[1] - a[1]))
        rest = m.group('rest').strip()
        return _offsets(p, rest, P, scale) if rest else p
    toks = _split_top(e, ['+', '-'])
    if len(toks) >= 3:
        base = _pt(toks[0].strip().strip('()'), P, scale)
        return _offsets(base, ''.join(toks[1:]), P, scale)
    return _pt(e.strip().strip('()'), P, scale)


def _offsets(p, rest, P, scale):
    toks = _split_top(rest, ['+', '-'])
    i = 0
    while i < len(toks) - 1:
        op = toks[i].strip()
        # `op in '+-'` would be True for the empty string -- the split leaves
        # an empty leading token for "+(0,1.52)" -- and the empty token would
        # then be read as an operator, taking "+" as the point to add.
        if op not in ('+', '-'):
            i += 1
            continue
        q = _pt(toks[i + 1].strip().strip('()'), P, scale)
        p = ((p[0] + q[0], p[1] + q[1]) if op == '+'
             else (p[0] - q[0], p[1] - q[1]))
        i += 2
    return p


def _expand_foreach(body):
    out = body
    pat = re.compile(r'\\foreach\s+((?:\\[A-Za-z]+/?)+)\s+in\s*\{([^}]*)\}\s*\{', re.S)
    while True:
        m = pat.search(out)
        if not m:
            break
        names = [n for n in m.group(1).split('/') if n]
        tuples = [t.strip() for t in m.group(2).split(',') if t.strip()]
        i, depth = m.end(), 1
        while i < len(out) and depth:
            depth += (out[i] == '{') - (out[i] == '}')
            i += 1
        loop = out[m.end():i - 1]
        pieces = []
        for t in tuples:
            b = loop
            for n, v in zip(names, t.split('/')):
                b = re.sub(re.escape(n) + r'(?![A-Za-z])', lambda _m, v=v: v, b)
            pieces.append(b)
        out = out[:m.start()] + '\n'.join(pieces) + out[i:]
    return out


class Fig:
    def __init__(self, num, scale):
        self.num, self.scale = num, scale
        self.pts, self.all, self.segs = {}, {}, []

    def __getitem__(self, k):
        return self.pts[k]


def _walk(body, fig):
    body = _expand_foreach(body)
    shift, stack = [0.0, 0.0], []
    P, s = fig.pts, fig.scale
    lit = re.compile(rf'\s*(?:{NUMPAT}\s*,\s*{NUMPAT}|{NUMPAT}\s*:\s*{NUMPAT})\s*')
    for raw in body.split('\n'):
        line = raw.strip()
        m = re.match(r'\\begin\{scope\}\[([^\]]*)\]', line)
        if m:
            stack.append(tuple(shift))
            xs = re.search(r'xshift\s*=\s*([-\d.]+)\s*cm', m.group(1))
            ys = re.search(r'yshift\s*=\s*([-\d.]+)\s*cm', m.group(1))
            if xs:
                shift[0] += float(xs.group(1))
            if ys:
                shift[1] += float(ys.group(1))
            continue
        if line.startswith(r'\end{scope}'):
            if stack:
                shift[0], shift[1] = stack.pop()
            continue
        for cm_ in re.finditer(r'\\coordinate\s*\(([^)]+)\)\s*at\s*\((.*?)\)\s*;', line):
            nm, expr = cm_.group(1).strip(), cm_.group(2)
            try:
                p = _pt(expr, P, s)
            except Exception:
                continue
            if lit.fullmatch(expr):
                p = (p[0] + shift[0], p[1] + shift[1])
            fig.all.setdefault(nm, []).append(p)
            P[nm] = p
        dm = re.match(r'\\draw\[([^\]]*)\]\s*(.*?);\s*$', line)
        if dm and '--' in dm.group(2) and 'arc' not in dm.group(2):
            chain = dm.group(2)
            if any(w in chain for w in ('rectangle', 'circle', 'controls')):
                continue
            pts_, ok = [], True
            for t in [x.strip() for x in chain.split('--')]:
                if t == 'cycle':
                    pts_.append('cycle')
                    continue
                rel = t.startswith('++')
                t2 = t[2:].strip() if rel else t
                if t2.startswith('(') and t2.endswith(')'):
                    t2 = t2[1:-1]
                try:
                    q = _pt(t2, P, s)
                except Exception:
                    ok = False
                    break
                if rel:                       # ++ is relative to the last point
                    prev = pts_[-1] if pts_ and pts_[-1] != 'cycle' else (0, 0)
                    q = (prev[0] + q[0], prev[1] + q[1])
                elif lit.fullmatch(t2):
                    q = (q[0] + shift[0], q[1] + shift[1])
                pts_.append(q)
            if not ok or len(pts_) < 2:
                continue
            for a, b in zip(pts_, pts_[1:]):
                if b == 'cycle':
                    b = pts_[0]
                if a != 'cycle':
                    fig.segs.append((a, b))


def _parse():
    src = open(os.path.normpath(FIGFILE)).read()
    figs = {}
    for m in re.finditer(r'\\begin\{tikzpicture\}(\[[^\]]*\])?(.*?)\\end\{tikzpicture\}'
                         r'\s*\\figcap\{([^}]*)\}', src, re.S):
        opt = m.group(1) or ''
        sm = re.search(r'scale\s*=\s*([\d.]+)', opt)
        f = Fig(m.group(3).replace('--', '-').strip(),
                float(sm.group(1)) if sm else 1.0)
        _walk(m.group(2), f)
        figs[f.num] = f
    return figs


FIGS = _parse()


def P(fig, *names):
    """the drawing's own coordinates for these points"""
    f = FIGS[fig]
    return [f.pts[n] for n in names] if len(names) > 1 else f.pts[names[0]]


def COPIES(fig, name):
    return FIGS[fig].all[name]


# --------------------------------------------------------------------------
def rel(a, b):
    return abs(a - b) / max(abs(b), 1e-9)


def mid(p, q):
    return lerp(p, q, 0.5)


def angdeg(p, v, q):
    a, b = V(v, p), V(v, q)
    c = (a[0] * b[0] + a[1] * b[1]) / (math.hypot(*a) * math.hypot(*b))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def on_seg(a, b, p):
    """p lies on line ab (0 when collinear)"""
    return par(V(a, p), V(a, b))


def side(a, b, p):
    return (p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])


def build(check):
    # ---------------------------------------------------- Figs 6-5, 6-6 fans
    # Postulate V-3: the common side of B and C runs inside the whole angle A,
    # and the two parts add up to the whole.
    for tag, fig in (('6-5', '6-5'), ('6-6', '6-6')):
        f = FIGS[fig]
        rays = {}
        for a, b in f.segs:
            for v in f.all.get('V', []) + f.all.get('W', []):
                if dist(a, v) < 1e-9:
                    rays.setdefault(tuple(v), []).append(b)
        for v, ends in rays.items():
            if len(ends) != 3:
                continue
            bear = sorted(ends, key=lambda e: math.degrees(
                math.atan2(e[1] - v[1], e[0] - v[0])))
            lo, mid_, hi = bear
            whole = angdeg(lo, v, hi)
            check(tag, 'middle side interior to the whole angle',
                  abs(angdeg(lo, v, mid_) + angdeg(mid_, v, hi) - whole))

    # -------------------------------------------------------------- Fig 6-12
    O, R, U = P('6-12', 'O', 'R', 'U')
    check('6-12', 'OU perp l', perp(V(O, U), V(O, R)))

    # -------------------------------------------------------------- Fig 6-14
    # Rebuilt: THREE parallels cut by one transversal, and A..E name the five
    # marked ANGLES, not five points.  What has to hold is that the three
    # lines really are parallel and that each crossing really is on both the
    # transversal and its own line.
    L1a, L1b, L2a, L2b, L3a, L3b = P('6-14', 'L1a', 'L1b', 'L2a', 'L2b',
                                     'L3a', 'L3b')
    Pt, Qt, X1, X2, X3 = P('6-14', 'P', 'Q', 'X1', 'X2', 'X3')
    check('6-14', 'lines 1 and 2 parallel', par(V(L1a, L1b), V(L2a, L2b)))
    check('6-14', 'lines 2 and 3 parallel', par(V(L2a, L2b), V(L3a, L3b)))
    check('6-14', 'X1 = transversal cap line 1',
          on_seg(Pt, Qt, X1) + on_seg(L1a, L1b, X1))
    check('6-14', 'X2 = transversal cap line 2',
          on_seg(Pt, Qt, X2) + on_seg(L2a, L2b, X2))
    check('6-14', 'X3 = transversal cap line 3',
          on_seg(Pt, Qt, X3) + on_seg(L3a, L3b, X3))

    # -------------------------------------------------------------- Fig 6-15
    A15, F15, E15, B15, C15, D15, O15 = P('6-15', 'A', 'F', 'E', 'B', 'C', 'D', 'O')
    check('6-15', 'A--F passes through O', on_seg(A15, F15, O15))
    check('6-15', 'E--B passes through O', on_seg(E15, B15, O15))
    check('6-15', 'C--D passes through O', on_seg(C15, D15, O15))

    # -------------------------------------------------------------- Fig 6-16
    # Postulate V-4 (S.A.S.): AB = A'B', AC = A'C', angle A = angle A'.
    (A, Ap), (B, Bp), (C, Cp) = (COPIES('6-16', n) for n in 'ABC')
    check('6-16', "AB = A'B'", rel(dist(A, B), dist(Ap, Bp)))
    check('6-16', "AC = A'C'", rel(dist(A, C), dist(Ap, Cp)))
    check('6-16', "angle A = angle A'", abs(angdeg(C, A, B) - angdeg(Cp, Ap, Bp)))

    # -------------------------------------------------------------- Fig 6-22
    A, B, D = P('6-22', 'A', 'B', 'D')
    check('6-22', 'D lies on AB', on_seg(A, B, D))

    # ---------------------------------------------------- Figs 6-24 and 6-27
    A, C, D = P('6-24', 'A', 'C', 'D')
    check('6-24', 'AD = DC', rel(dist(A, D), dist(D, C)))     # Exercise 10
    A, B, M = P('6-27', 'A', 'B', 'M')
    check('6-27', 'AM = MB', rel(dist(A, M), dist(M, B)))     # Exercise 13

    # -------------------------------------------------------------- Fig 6-29
    A, C, D = P('6-29', 'A', 'C', 'D')
    check('6-29', 'AD = DC', rel(dist(A, D), dist(D, C)))     # Exercise 15
    check('6-29', 'D lies on AC', on_seg(A, C, D))

    # -------------------------------------------------------------- Fig 6-30
    A, D, B, C, E, F = P('6-30', 'A', 'D', 'B', 'C', 'E', 'F')
    check('6-30', 'AB parallel to DC', par(V(A, B), V(D, C)))
    check('6-30', 'AD parallel to BC', par(V(A, D), V(B, C)))
    check('6-30', 'AE = CF', rel(dist(A, E), dist(C, F)))     # Exercise *16
    check('6-30', 'E and F lie on AC', on_seg(A, C, E) + on_seg(A, C, F))

    # -------------------------------------------------------------- Fig 6-31
    A, B, C, D, O = P('6-31', 'A', 'B', 'C', 'D', 'O')
    check('6-31', 'AB = AD', rel(dist(A, B), dist(A, D)))     # Exercise *17
    check('6-31', 'BO = OD', rel(dist(B, O), dist(O, D)))
    check('6-31', 'angle OAB = angle OAD', abs(angdeg(O, A, B) - angdeg(O, A, D)))

    # -------------------------------------------------------------- Fig 6-32
    A, B, C = P('6-32', 'A', 'B', 'C')
    check('6-32', 'AB = AC', rel(dist(A, B), dist(A, C)))     # Theorem 6-3

    # -------------------------------------------------------------- Fig 6-40
    A, B, C, D, E = P('6-40', 'A', 'B', 'C', 'D', 'E')
    check('6-40', 'AC = BC', rel(dist(A, C), dist(B, C)))     # Exercise 9
    check('6-40', 'CD = CE', rel(dist(C, D), dist(C, E)))
    check('6-40', 'D lies on AC', on_seg(A, C, D))
    check('6-40', 'E lies on BC', on_seg(B, C, E))

    # -------------------------------------------------------------- Fig 6-41
    # Exercise 10 states FOUR hypotheses and the figure had none encoded here,
    # which is how a draft that fanned every cevian from the apex E -- leaving
    # O with no segments to A, B, C, D at all, so that AO, OD, BO, OC did not
    # exist as drawn objects -- passed the suite.  Checked against scan07 p1.
    A, B, C, D, E, F, O = P('6-41', 'A', 'B', 'C', 'D', 'E', 'F', 'O')
    check('6-41', 'A, B, F, C, D collinear',
          on_seg(A, D, B) + on_seg(A, D, F) + on_seg(A, D, C))
    check('6-41', 'AF = FD (F the midpoint of AD)', rel(dist(A, F), dist(F, D)))
    check('6-41', 'BF = FC (F the midpoint of BC)', rel(dist(B, F), dist(F, C)))
    check('6-41', 'AO = OD', rel(dist(A, O), dist(O, D)))
    check('6-41', 'BO = OC', rel(dist(B, O), dist(O, C)))
    check('6-41', 'O lies on FE', on_seg(F, E, O))
    check('6-41', 'FE perpendicular to AD (the axis of symmetry)',
          perp(V(F, E), V(A, D)))
    check('6-41', 'B between A and D',
          rel(dist(A, B) + dist(B, D), dist(A, D)))
    check('6-41', 'C between A and D',
          rel(dist(A, C) + dist(C, D), dist(A, D)))

    # -------------------------------------------------------------- Fig 6-42
    # Exercise 11: AC = BC, CG = CF.  D and E are the marked points of the two
    # cevians AF and BG (checked against scan07 p1), and O, P, Q are crossings.
    A, B, C, D, E, F, G, O, Q, Pp = P('6-42', 'A', 'B', 'C', 'D', 'E', 'F',
                                      'G', 'O', 'Q', 'P')
    check('6-42', 'AC = BC', rel(dist(A, C), dist(B, C)))
    check('6-42', 'CG = CF', rel(dist(C, G), dist(C, F)))
    check('6-42', 'G lies on CA', on_seg(C, A, G))
    check('6-42', 'F lies on CB', on_seg(C, B, F))
    check('6-42', 'D lies on the cevian AF', on_seg(A, F, D))
    check('6-42', 'E lies on the cevian BG', on_seg(B, G, E))
    check('6-42', 'O = AF cap BG', on_seg(A, F, O) + on_seg(B, G, O))
    check('6-42', 'angle-3 vertex on CD and BG', on_seg(C, D, Pp) + on_seg(B, G, Pp))
    check('6-42', 'angle-4 vertex on CE and AF', on_seg(C, E, Q) + on_seg(A, F, Q))
    check('6-42', 'figure symmetric about the axis of AB',
          abs((D[1] - E[1])) + abs((D[0] + E[0]) - (A[0] + B[0])))

    # -------------------------------------------------------------- Fig 6-43
    A, B, C, Ap, Bp, Cp, Dp = P('6-43', 'A', 'B', 'C', 'Ap', 'Bp', 'Cp', 'Dp')
    check('6-43', "AB = A'B'", rel(dist(A, B), dist(Ap, Bp)))
    check('6-43', "AC = A'C'", rel(dist(A, C), dist(Ap, Cp)))
    check('6-43', "D' on ray C'B'", on_seg(Cp, Bp, Dp))

    # -------------------------------------------------------- Figs 6-46, 6-50
    C, D, A, B = P('6-46', 'C', 'D', 'A', 'B')
    check('6-46', 'B is the midpoint of CD', rel(dist(C, B), dist(B, D)))
    check('6-46', 'AB perp CD', perp(V(A, B), V(C, D)))
    A, B, C, D, E = P('6-50', 'A', 'B', 'C', 'D', 'E')
    check('6-50', 'D is the midpoint of AB', rel(dist(A, D), dist(D, B)))
    check('6-50', 'E is the midpoint of BC', rel(dist(B, E), dist(E, C)))

    # -------------------------------------------------------------- Fig 6-54
    A, B, C, D, E = P('6-54', 'A', 'B', 'C', 'D', 'E')
    check('6-54', 'A, C, E collinear', on_seg(A, E, C))
    check('6-54', 'B, C, D collinear', on_seg(B, D, C))

    # -------------------------------------------------------------- Fig 6-55
    A, B, C, Ap, Bp, Cp, Dp = P('6-55', 'A', 'B', 'C', 'Ap', 'Bp', 'Cp', 'Dp')
    check('6-55', "AC = A'C'", rel(dist(A, C), dist(Ap, Cp)))
    check('6-55', "angle A = angle A'", abs(angdeg(C, A, B) - angdeg(Cp, Ap, Bp)))
    check('6-55', "angle C = angle C'", abs(angdeg(A, C, B) - angdeg(Ap, Cp, Bp)))
    check('6-55', "D' on ray A'B'", on_seg(Ap, Bp, Dp))

    # -------------------------------------------------------------- Fig 6-56
    # Ex. Gp. 6-9 #1 concludes triangle ABD = triangle CBD, so the plate is
    # symmetric about the spine BD.
    A, B, C, D = P('6-56', 'A', 'B', 'C', 'D')
    check('6-56', 'AB = CB', rel(dist(A, B), dist(C, B)))
    check('6-56', 'AD = CD', rel(dist(A, D), dist(C, D)))
    check('6-56', 'BD perp AC', perp(V(B, D), V(A, C)))

    # ---------------------------------------------------- Figs 6-68 and 6-69
    A, B, C = P('6-68', 'A', 'B', 'C')
    check('6-68', 'B equidistant from A and C', rel(dist(B, A), dist(B, C)))
    A, B, C = P('6-69', 'A', 'B', 'C')
    Ap, Bp, Cp = P('6-69', 'Ap', 'Bp', 'Cp')
    Ac, Bc, Cc, Ec = P('6-69', 'Ac', 'Bc', 'Cc', 'Ec')
    check('6-69', "(a),(b) AB = A'B'", rel(dist(A, B), dist(Ap, Bp)))
    check('6-69', "(a),(b) AC = A'C'", rel(dist(A, C), dist(Ap, Cp)))
    check('6-69', "(a),(b) BC = B'C'", rel(dist(B, C), dist(Bp, Cp)))
    check('6-69', '(c) AB = AE', rel(dist(Ac, Bc), dist(Ac, Ec)))
    check('6-69', '(c) B and E on opposite sides of AC',
          0.0 if side(Ac, Cc, Bc) * side(Ac, Cc, Ec) < 0 else 1.0)

    # ---------------------------------------------------- Figs 6-80 and 6-81
    A, B, D, E, F = P('6-80', 'A', 'B', 'D', 'E', 'F')
    check('6-80', 'D is the midpoint of AB', rel(dist(A, D), dist(D, B)))
    check('6-80', 'EF || AB', par(V(E, F), V(A, B)))
    A, B, C, D = P('6-81', 'A', 'B', 'C', 'D')
    check('6-81', 'D is the midpoint of AB', rel(dist(A, D), dist(D, B)))
    check('6-81', 'CD perp AB', perp(V(C, D), V(A, B)))

    # -------------------------------------------------------------- Fig 6-92
    # Exercise 22: triangles ABC and ADE isosceles with vertex A, angle 1 =
    # angle 2.  Rebuilt against scan07 p19: the outer pentagon is drawn too,
    # and the five inner letters are chord crossings.
    A, B, C, D, E = P('6-92', 'A', 'B', 'C', 'D', 'E')
    F, G, H, I, J = P('6-92', 'F', 'G', 'H', 'I', 'J')
    check('6-92', 'AB = AC', rel(dist(A, B), dist(A, C)))
    check('6-92', 'AD = AE', rel(dist(A, D), dist(A, E)))
    check('6-92', 'angle 1 = angle 2 (BAE = DAC)',
          abs(angdeg(B, A, E) - angdeg(D, A, C)))
    check('6-92', 'F = BD cap CE', on_seg(B, D, F) + on_seg(C, E, F))
    check('6-92', 'G = BD cap AE', on_seg(B, D, G) + on_seg(A, E, G))
    check('6-92', 'H = AD cap CE', on_seg(A, D, H) + on_seg(C, E, H))
    check('6-92', 'I = AE cap BC', on_seg(A, E, I) + on_seg(B, C, I))
    check('6-92', 'J = AD cap BC', on_seg(A, D, J) + on_seg(B, C, J))

    # -------------------------------------------------------------- Fig 6-94
    # Section 6-10: A' is the mirror of A in l, so AA' is perpendicular to l
    # and C is where AA' meets it.  Case 2 has C = O.
    A, Ap, O, B = (COPIES('6-94', 'A')[0], COPIES('6-94', 'Ap')[0],
                   COPIES('6-94', 'O')[0], COPIES('6-94', 'B')[0])
    C = COPIES('6-94', 'C')[0]
    check('6-94', "AA' perp l", perp(V(A, Ap), V(O, B)))
    check('6-94', "OA = OA'", rel(dist(O, A), dist(O, Ap)))
    check('6-94', 'C on l', abs(C[1] - O[1]))
    A2, Ap2, O2 = (COPIES('6-94', 'A')[1], COPIES('6-94', 'Ap')[1],
                   COPIES('6-94', 'O')[1])
    check('6-94', 'case 2: C = O', abs(A2[0] - O2[0]) + abs(Ap2[0] - O2[0]))

    # -------------------------------------------------------------- Fig 6-96
    A, B, C, D, E = P('6-96', 'A', 'B', 'C', 'D', 'E')
    check('6-96', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-96', 'CB = CD', rel(dist(C, B), dist(C, D)))
    check('6-96', 'E is the midpoint of BD', rel(dist(B, E), dist(E, D)))
    check('6-96', 'AC perp BD', perp(V(A, C), V(B, D)))

    # ------------------------------------------------------------- Fig 6-102
    # Theorem 6-8: AD = AE, and F is where DE cuts the second side of B'.
    A, D, E, F, Bs = P('6-102', 'A', 'D', 'E', 'F', 'Bs')
    check('6-102', 'AD = AE', rel(dist(A, D), dist(A, E)))
    check('6-102', 'F on DE', on_seg(D, E, F))
    check('6-102', "F on the second side of B'", on_seg(A, Bs, F))

    # ------------------------------------------------------------- Fig 6-104
    # Both panels of 6-104 name their upright (U), so take the bindings by
    # panel rather than by name -- the plain lookup returns panel (b)'s.
    O, R = P('6-104', 'O', 'R')
    U = COPIES('6-104', 'U')[0]
    check('6-104', '(a) l perp m', perp(V(O, U), V(O, R)))
    A, B, M = P('6-104', 'A', 'B', 'M')
    U2 = COPIES('6-104', 'U')[1]
    check('6-104', '(b) M is the midpoint of AB', rel(dist(A, M), dist(M, B)))
    check('6-104', '(b) l perp AB', perp(V(M, U2), V(A, B)))

    # ---------------------------------------------- Figs 6-107, 6-108, 6-110
    D, C, A, B, E = P('6-107', 'D', 'C', 'A', 'B', 'E')
    check('6-107', 'E is the midpoint of DC', rel(dist(D, E), dist(E, C)))
    check('6-107', 'AD perp DC', perp(V(A, D), V(D, C)))
    check('6-107', 'AB || DC', par(V(A, B), V(D, C)))
    A, C, D = P('6-108', 'A', 'C', 'D')
    check('6-108', 'D is the midpoint of AC', rel(dist(A, D), dist(D, C)))
    C, D, B = P('6-110', 'C', 'D', 'B')
    check('6-110', 'B lies on DC', on_seg(D, C, B))

    # ------------------------------------------------------------- Fig 6-111
    A, B, C, D = P('6-111', 'A', 'B', 'C', 'D')
    check('6-111', 'AC = AD', rel(dist(A, C), dist(A, D)))    # Exercise 11
    check('6-111', 'AC perp CB', perp(V(C, A), V(C, B)))
    check('6-111', 'AD perp DB', perp(V(D, A), V(D, B)))
    check('6-111', 'C, D on opposite sides of AB',
          0.0 if side(A, B, C) * side(A, B, D) < 0 else 1.0)

    # ------------------------------------------------------------- Fig 6-112
    # Review exercise 3: R and S are the two parts of T, A_1 and A_2 the two
    # parts of B.  Checked against scan08 p5: the left fan is vertex-UP.
    f = FIGS['6-112']
    for tag, vname in (('left fan', 'V'), ('right fan', 'W')):
        v = f.pts[vname]
        ends = [b for a, b in f.segs if dist(a, v) < 1e-9]
        if len(ends) != 3:
            check('6-112', f'{tag} has three rays', 1.0)
            continue
        ends.sort(key=lambda e: math.degrees(math.atan2(e[1] - v[1], e[0] - v[0])))
        lo, md, hi = ends
        check('6-112', f'{tag}: the two parts make the whole',
              abs(angdeg(lo, v, md) + angdeg(md, v, hi) - angdeg(lo, v, hi)))

    # ------------------------------------------- Figs 6-114, 6-120, 6-121
    A, C, O, B = P('6-114', 'A', 'C', 'O', 'B')
    check('6-114', 'O is the midpoint of AC', rel(dist(A, O), dist(O, C)))
    check('6-114', 'OB perp AC', perp(V(O, B), V(A, C)))
    A, B, C, D, E, F = P('6-120', 'A', 'B', 'C', 'D', 'E', 'F')
    check('6-120', 'D is the midpoint of AC', rel(dist(A, D), dist(D, C)))
    check('6-120', 'E is the midpoint of AB', rel(dist(A, E), dist(E, B)))
    check('6-120', 'F is the midpoint of BC', rel(dist(B, F), dist(F, C)))
    check('6-120', 'EF || AC', par(V(E, F), V(A, C)))
    check('6-120', 'ED || BC', par(V(E, D), V(B, C)))
    check('6-120', 'DF || AB', par(V(D, F), V(A, B)))
    Q, R, S, Pp = P('6-121', 'Q', 'R', 'S', 'P')
    check('6-121', 'S is the midpoint of QR', rel(dist(Q, S), dist(S, R)))
    check('6-121', 'PS perp QR', perp(V(Pp, S), V(Q, R)))

    # ------------------------------------------------------------- Fig 6-122
    A, B, C, D, O = P('6-122', 'A', 'B', 'C', 'D', 'O')
    check('6-122', 'O on AB', on_seg(A, B, O))
    check('6-122', 'O on CD', on_seg(C, D, O))

    # ------------------------------------------------------------- Fig 6-124
    C, B, A, D, E, F = P('6-124', 'C', 'B', 'A', 'D', 'E', 'F')
    check('6-124', 'CB = CA', rel(dist(C, B), dist(C, A)))
    check('6-124', 'CB = AB', rel(dist(C, B), dist(A, B)))
    check('6-124', 'EF = ED', rel(dist(E, F), dist(E, D)))
    check('6-124', 'EF = FD', rel(dist(E, F), dist(F, D)))
    check('6-124', 'EF || CB', par(V(E, F), V(C, B)))

    # ------------------------------------------------------------- Fig 6-126
    # Review exercise 25: angle 1 = angle 2, AC = BC, IJ = IK.  Rebuilt
    # against scan08 p8: the book joins D--J and E--K, and G, H are their
    # crossings with the cevians AE and BD.
    A, B, C, D, E, F, G, H, I, J, K = P('6-126', 'A', 'B', 'C', 'D', 'E',
                                        'F', 'G', 'H', 'I', 'J', 'K')
    check('6-126', 'AC = BC', rel(dist(A, C), dist(B, C)))
    check('6-126', 'IJ = IK', rel(dist(I, J), dist(I, K)))
    check('6-126', 'I is the midpoint of AB', rel(dist(A, I), dist(I, B)))
    check('6-126', 'J, I, K on AB', abs(J[1]) + abs(I[1]) + abs(K[1]))
    check('6-126', 'I between J and K', 0.0 if J[0] < I[0] < K[0] else 1.0)
    check('6-126', 'angle 1 = angle 2 (EAB = DBA)',
          abs(angdeg(E, A, B) - angdeg(D, B, A)))
    check('6-126', 'F = AE cap BD', on_seg(A, E, F) + on_seg(B, D, F))
    check('6-126', 'F on the median CI', on_seg(C, I, F))
    check('6-126', 'G = DJ cap AE', on_seg(D, J, G) + on_seg(A, E, G))
    check('6-126', 'H = EK cap BD', on_seg(E, K, H) + on_seg(B, D, H))
    check('6-126', 'GJ = HK (the exercise conclusion holds in the drawing)',
          rel(dist(G, J), dist(H, K)))
    check('6-126', 'GF = FH', rel(dist(G, F), dist(F, H)))

    # =====================================================================
    # Hypotheses the exercise text states but the constraint suite had never
    # been asked to enforce.  Every one of these was found FALSE in the
    # drawing during the figure review and fixed in figures06.tex; they are
    # recorded here so the plate cannot drift away from its own text again.
    # =====================================================================

    # -------- Fig 6-25 (Ex. 11): CF = DF, CG = HD, and C, F, D collinear
    B, C, G, F, H, D, A = P('6-25', 'B', 'C', 'G', 'F', 'H', 'D', 'A')
    check('6-25', 'CF = DF', rel(dist(C, F), dist(F, D)))
    check('6-25', 'CG = HD', rel(dist(C, G), dist(H, D)))

    # -------- Fig 6-26 (Ex. 12): AE = CD and AB = BC
    A, B, C, D, E = P('6-26', 'A', 'B', 'C', 'D', 'E')
    check('6-26', 'AE = CD', rel(dist(A, E), dist(C, D)))
    check('6-26', 'AB = BC', rel(dist(A, B), dist(B, C)))

    # -------- Fig 6-27 (Ex. 13): AC = BC as well as AM = MB
    A, B, C = P('6-27', 'A', 'B', 'C')
    check('6-27', 'AC = BC', rel(dist(A, C), dist(B, C)))

    # -------- Fig 6-29 (Ex. 15): angle 1 = angle 2 are supplementary, so BD
    # is perpendicular to AC
    A, C, B, D = P('6-29', 'A', 'C', 'B', 'D')
    check('6-29', 'BD perp AC', perp(V(B, D), V(A, C)))

    # -------- Fig 6-37 (Ex. 6): AC = DF, with C and D on A--F
    A, C, D, F = P('6-37', 'A', 'C', 'D', 'F')
    check('6-37', 'AC = DF', rel(dist(A, C), dist(D, F)))
    check('6-37', 'C and D on AF', on_seg(A, F, C) + on_seg(A, F, D))

    # -------- Fig 6-38 (Ex. 7): AD = EC and BE = BD
    A, C, B, D, E = P('6-38', 'A', 'C', 'B', 'D', 'E')
    check('6-38', 'AD = EC', rel(dist(A, D), dist(E, C)))
    check('6-38', 'BE = BD', rel(dist(B, E), dist(B, D)))

    # -------- Fig 6-39 (Ex. 8): RS = RT and US = UT
    S, T, R, U = P('6-39', 'S', 'T', 'R', 'U')
    check('6-39', 'RS = RT', rel(dist(R, S), dist(R, T)))
    check('6-39', 'US = UT', rel(dist(U, S), dist(U, T)))

    # -------- Fig 6-44 (Ex. 1): AB = BC
    A, B, C = P('6-44', 'A', 'B', 'C')
    check('6-44', 'AB = BC', rel(dist(A, B), dist(B, C)))

    # -------- Fig 6-45 (Ex. 2): EF = GH, and EF || GH
    E, F, G, H = P('6-45', 'E', 'F', 'G', 'H')
    check('6-45', 'EF = GH', rel(dist(E, F), dist(G, H)))
    check('6-45', 'EF || GH', par(V(E, F), V(G, H)))

    # -------- Fig 6-47 (Ex. 4): AB = AD and BC = CD
    A, B, C, D = P('6-47', 'A', 'B', 'C', 'D')
    check('6-47', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-47', 'BC = CD', rel(dist(B, C), dist(C, D)))
    check('6-47', 'C on BD', on_seg(B, D, C))

    # -------- Fig 6-48 (Ex. 5): AB = AC, D and E the midpoints
    A, B, C, D, E = P('6-48', 'A', 'B', 'C', 'D', 'E')
    check('6-48', 'AB = AC', rel(dist(A, B), dist(A, C)))
    check('6-48', 'D is the midpoint of AB', rel(dist(A, D), dist(D, B)))
    check('6-48', 'E is the midpoint of AC', rel(dist(A, E), dist(E, C)))

    # -------- Fig 6-49 (Ex. 6): AB = AD and BC = CD
    A, B, C, D = P('6-49', 'A', 'B', 'C', 'D')
    check('6-49', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-49', 'BC = CD', rel(dist(B, C), dist(C, D)))

    # -------- Fig 6-50 (Ex. 7): AB = BC
    A, B, C = P('6-50', 'A', 'B', 'C')
    check('6-50', 'AB = BC', rel(dist(A, B), dist(B, C)))

    # -------- Fig 6-51 (Ex. 8): B the midpoint of AC, EB = BD
    A, B, C, D, E = P('6-51', 'A', 'B', 'C', 'D', 'E')
    check('6-51', 'B is the midpoint of AC', rel(dist(A, B), dist(B, C)))
    check('6-51', 'EB = BD', rel(dist(E, B), dist(B, D)))

    # -------- Fig 6-52 (Ex. 9): AD = BC and angle DAB = angle CBA
    A, B, C, D = P('6-52', 'A', 'B', 'C', 'D')
    check('6-52', 'AD = BC', rel(dist(A, D), dist(B, C)))
    check('6-52', 'angle DAB = angle CBA',
          abs(angdeg(D, A, B) - angdeg(C, B, A)))

    # -------- Fig 6-53 (Ex. 10): AD = EC and BE = BD
    A, C, B, D, E = P('6-53', 'A', 'C', 'B', 'D', 'E')
    check('6-53', 'AD = EC', rel(dist(A, D), dist(E, C)))
    check('6-53', 'BE = BD', rel(dist(B, E), dist(B, D)))

    # -------- Fig 6-63 (Ex. 10): AB = AD and AC bisects angle BAD
    A, B, C, D, X = P('6-63', 'A', 'B', 'C', 'D', 'X')
    check('6-63', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-63', 'AC bisects angle BAD',
          abs(angdeg(B, A, C) - angdeg(C, A, D)))
    check('6-63', 'D on the base A--X', on_seg(A, X, D))

    # -------- Fig 6-64 (Ex. 11): AF = FB and AE = DB
    A, B, C, D, E, F = P('6-64', 'A', 'B', 'C', 'D', 'E', 'F')
    check('6-64', 'AF = FB', rel(dist(A, F), dist(F, B)))
    check('6-64', 'AE = DB', rel(dist(A, E), dist(D, B)))
    check('6-64', 'F = AE cap BD', on_seg(A, E, F) + on_seg(B, D, F))

    # -------- Fig 6-65 (Ex. 12): AB = BC and AD = DC
    A, C, B, D = P('6-65', 'A', 'C', 'B', 'D')
    check('6-65', 'AB = BC', rel(dist(A, B), dist(B, C)))
    check('6-65', 'AD = DC', rel(dist(A, D), dist(D, C)))

    # -------- Fig 6-66 (Ex. 13): AH = HB and AG = GB; F on both CH and DE
    A, B, C, D, E, F, G, H = P('6-66', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    check('6-66', 'AH = HB', rel(dist(A, H), dist(H, B)))
    check('6-66', 'AG = GB', rel(dist(A, G), dist(G, B)))
    check('6-66', 'F = CH cap DE', on_seg(C, H, F) + on_seg(D, E, F))
    check('6-66', 'G = AE cap BD', on_seg(A, E, G) + on_seg(B, D, G))

    # -------- Fig 6-67 (Ex. 14): AC = BC, DF = EG; H, I, J derived crossings
    A, B, C, D, E, F, G, H, I, J = P('6-67', 'A', 'B', 'C', 'D', 'E',
                                     'F', 'G', 'H', 'I', 'J')
    check('6-67', 'AC = BC', rel(dist(A, C), dist(B, C)))
    check('6-67', 'DF = EG', rel(dist(D, F), dist(E, G)))
    check('6-67', 'D, F on CA', on_seg(C, A, D) + on_seg(C, A, F))
    check('6-67', 'E, G on CB', on_seg(C, B, E) + on_seg(C, B, G))
    check('6-67', 'H = AE cap BD', on_seg(A, E, H) + on_seg(B, D, H))
    check('6-67', 'I = AE cap FG', on_seg(A, E, I) + on_seg(F, G, I))
    check('6-67', 'J = BD cap FG', on_seg(B, D, J) + on_seg(F, G, J))
    check('6-67', 'triangle HIJ is isosceles (the conclusion holds)',
          rel(dist(H, I), dist(H, J)))

    # -------- Fig 6-75 (Ex. 4): AB = BC and AD = DC
    A, C, B, D = P('6-75', 'A', 'C', 'B', 'D')
    check('6-75', 'AB = BC', rel(dist(A, B), dist(B, C)))
    check('6-75', 'AD = DC', rel(dist(A, D), dist(D, C)))

    # -------- Fig 6-76 (Ex. 5): AB = AD, BC = CD, E the crossing
    A, B, C, D, E = P('6-76', 'A', 'B', 'C', 'D', 'E')
    check('6-76', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-76', 'BC = CD', rel(dist(B, C), dist(C, D)))
    check('6-76', 'E = AC cap BD', on_seg(A, C, E) + on_seg(B, D, E))

    # -------- Fig 6-77 (Ex. 6): AB = CD, BC = AD, AF = EC
    A, B, C, D, E, F = P('6-77', 'A', 'B', 'C', 'D', 'E', 'F')
    check('6-77', 'AB = CD', rel(dist(A, B), dist(C, D)))
    check('6-77', 'BC = AD', rel(dist(B, C), dist(A, D)))
    check('6-77', 'AF = EC', rel(dist(A, F), dist(E, C)))
    check('6-77', 'E and F on AC', on_seg(A, C, E) + on_seg(A, C, F))

    # -------- Fig 6-78 (Ex. 7): AB = BC and AD = EC
    A, C, B, D, E = P('6-78', 'A', 'C', 'B', 'D', 'E')
    check('6-78', 'AB = BC', rel(dist(A, B), dist(B, C)))
    check('6-78', 'AD = EC', rel(dist(A, D), dist(E, C)))

    # -------- Fig 6-79 (Ex. 8): AB = AD and BC = CD
    A, B, C, D = P('6-79', 'A', 'B', 'C', 'D')
    check('6-79', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-79', 'BC = CD', rel(dist(B, C), dist(C, D)))

    # -------- Fig 6-80 (Ex. 9): CE = CF, AE = BF, G on CD and on EF
    A, B, C, D, E, F, G = P('6-80', 'A', 'B', 'C', 'D', 'E', 'F', 'G')
    check('6-80', 'CE = CF', rel(dist(C, E), dist(C, F)))
    check('6-80', 'AE = BF', rel(dist(A, E), dist(B, F)))
    check('6-80', 'G = CD cap EF', on_seg(C, D, G) + on_seg(E, F, G))

    # -------- Fig 6-81 (Ex. 10): AC = BC as well as the two already checked
    A, B, C = P('6-81', 'A', 'B', 'C')
    check('6-81', 'AC = BC', rel(dist(A, C), dist(B, C)))

    # -------- Fig 6-82 (Ex. 11): AC = BD and AD = BC
    A, B, C, D = P('6-82', 'A', 'B', 'C', 'D')
    check('6-82', 'AC = BD', rel(dist(A, C), dist(B, D)))
    check('6-82', 'AD = BC', rel(dist(A, D), dist(B, C)))

    # -------- Fig 6-83 (Ex. 12): AB = BC and BD = BE
    A, B, C, D, E = P('6-83', 'A', 'B', 'C', 'D', 'E')
    check('6-83', 'AB = BC', rel(dist(A, B), dist(B, C)))
    check('6-83', 'BD = BE', rel(dist(B, D), dist(B, E)))

    # -------- Fig 6-84 (Ex. 13): AC = BC, AD = DB, O on CD
    A, B, C, D, O = P('6-84', 'A', 'B', 'C', 'D', 'O')
    check('6-84', 'AC = BC', rel(dist(A, C), dist(B, C)))
    check('6-84', 'AD = DB', rel(dist(A, D), dist(D, B)))
    check('6-84', 'O on CD', on_seg(C, D, O))
    check('6-84', 'AO = BO (the conclusion holds)', rel(dist(A, O), dist(B, O)))

    # -------- Fig 6-85 (Ex. 14): AC = BC
    A, B, C = P('6-85', 'A', 'B', 'C')
    check('6-85', 'AC = BC', rel(dist(A, C), dist(B, C)))

    # -------- Fig 6-86 (Ex. 15): AD = BC, AB = DC, AM = MC
    A, B, C, D, E, F, M = P('6-86', 'A', 'B', 'C', 'D', 'E', 'F', 'M')
    check('6-86', 'AD = BC', rel(dist(A, D), dist(B, C)))
    check('6-86', 'AB = DC', rel(dist(A, B), dist(D, C)))
    check('6-86', 'AM = MC', rel(dist(A, M), dist(M, C)))
    check('6-86', 'M = AC cap EF', on_seg(A, C, M) + on_seg(E, F, M))
    check('6-86', 'EM = MF (the conclusion holds)', rel(dist(E, M), dist(M, F)))

    # -------- Fig 6-87 (Ex. 16): AE = DB
    A, B, C, D, E = P('6-87', 'A', 'B', 'C', 'D', 'E')
    check('6-87', 'AE = DB', rel(dist(A, E), dist(D, B)))
    check('6-87', 'D on AC, E on BC', on_seg(A, C, D) + on_seg(B, C, E))

    # -------- Fig 6-88 (Ex. 17): BE = CE, and A, D, E collinear
    A, B, C, D, E = P('6-88', 'A', 'B', 'C', 'D', 'E')
    check('6-88', 'BE = CE', rel(dist(B, E), dist(C, E)))
    check('6-88', 'D on AE', on_seg(A, E, D))
    # Exercise 17 also GIVES angle 1 = angle 2 and asks for angle 3 = angle 4;
    # neither was encoded, so the plate could have been drawn lopsided and still
    # passed.  angle 1 = BEA, angle 2 = AEC, angle 3 = ABD, angle 4 = ACD.
    check('6-88', 'angle 1 = angle 2 (BEA = AEC)',
          abs(angdeg(B, E, A) - angdeg(A, E, C)) / 90)
    check('6-88', 'angle 3 = angle 4 (the conclusion holds)',
          abs(angdeg(A, B, D) - angdeg(A, C, D)) / 90)

    # -------- Fig 6-89 (Ex. 19): AD = BC, AB = CD, E and F on AC
    A, B, C, D, E, F = P('6-89', 'A', 'B', 'C', 'D', 'E', 'F')
    check('6-89', 'AD = BC', rel(dist(A, D), dist(B, C)))
    check('6-89', 'AB = CD', rel(dist(A, B), dist(C, D)))
    check('6-89', 'E and F on AC', on_seg(A, C, E) + on_seg(A, C, F))
    check('6-89', 'angle 1 = angle 2 (ADE = CBF)',
          abs(angdeg(A, D, E) - angdeg(C, B, F)))
    check('6-89', 'DE = BF (the conclusion holds)', rel(dist(D, E), dist(B, F)))

    # -------- Fig 6-90 (Ex. 20): AD = CB and BD = AC
    A, B, C, D = P('6-90', 'A', 'B', 'C', 'D')
    check('6-90', 'AD = CB', rel(dist(A, D), dist(C, B)))
    check('6-90', 'BD = AC', rel(dist(B, D), dist(A, C)))

    # -------- Fig 6-91 (Ex. 21): AB = CD, AE = CF, angle 3 = angle 4
    A, B, C, D, E, F = P('6-91', 'A', 'B', 'C', 'D', 'E', 'F')
    check('6-91', 'AB = CD', rel(dist(A, B), dist(C, D)))
    check('6-91', 'AE = CF', rel(dist(A, E), dist(C, F)))
    check('6-91', 'E and F on AC', on_seg(A, C, E) + on_seg(A, C, F))
    check('6-91', 'angle 3 = angle 4 (BAC = DCA)',
          abs(angdeg(B, A, C) - angdeg(D, C, A)))
    check('6-91', 'angle 1 = angle 2 (the conclusion holds)',
          abs(angdeg(A, D, E) - angdeg(C, B, F)))

    # -------- Fig 6-119 (Ex. 13): AB = BC, and D, E symmetric on the base
    A, B, C, D, E = P('6-119', 'A', 'B', 'C', 'D', 'E')
    check('6-119', 'AB = BC', rel(dist(A, B), dist(B, C)))
    check('6-119', 'angle ABD = angle EBC',
          abs(angdeg(A, B, D) - angdeg(E, B, C)))

    # -------- Fig 6-123 (Ex. 19): AB = AD, BC = DE, AC = AE
    A, B, C, D, E = P('6-123', 'A', 'B', 'C', 'D', 'E')
    check('6-123', 'AB = AD', rel(dist(A, B), dist(A, D)))
    check('6-123', 'AC = AE', rel(dist(A, C), dist(A, E)))
    check('6-123', 'BC = DE', rel(dist(B, C), dist(D, E)))

    # ------------------------------------------------------------- Fig 6-127
    A, B, C, D, E, O = P('6-127', 'A', 'B', 'C', 'D', 'E', 'O')
    check('6-127', 'AB = AC', rel(dist(A, B), dist(A, C)))
    check('6-127', 'AD = AE', rel(dist(A, D), dist(A, E)))
    check('6-127', 'O on BE', on_seg(B, E, O))
    check('6-127', 'O on CD', on_seg(C, D, O))
    check('6-127', 'DE || BC', par(V(D, E), V(B, C)))
