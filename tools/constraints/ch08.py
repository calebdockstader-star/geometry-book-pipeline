# Chapter 8 (Parallel Lines) figure constraints.
# Coordinates mirror chapters/figures08.tex exactly.  Every stated hypothesis
# in the text -- parallel / perpendicular / congruent / midpoint / ratio /
# incidence -- is checked here against the drawn geometry.
import math

from figlib import V, ang, par, perp, lerp, dist, foot


def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _on_line(a, b, p):
    """distance of p from line ab, relative to |ab|"""
    return abs(_cross(a, b, p)) / dist(a, b) ** 1


def _convex(pts):
    """1.0 if the polygon is not convex, 0.0 if it is."""
    signs = []
    n = len(pts)
    for i in range(n):
        c = _cross(pts[i], pts[(i + 1) % n], pts[(i + 2) % n])
        signs.append(c > 0)
    return 0.0 if (all(signs) or not any(signs)) else 1.0


def _angle_at(o, p):
    return math.degrees(math.atan2(p[1] - o[1], p[0] - o[0])) % 360


def _angle(o, p, q):
    """measure of angle p-o-q in degrees (0..180)"""
    d = abs(_angle_at(o, p) - _angle_at(o, q))
    return min(d, 360 - d)


def _same_dir(u, v):
    """0 if u and v point the same way, else the angle between them"""
    a = math.degrees(math.atan2(u[1], u[0])) % 360
    b = math.degrees(math.atan2(v[1], v[0])) % 360
    d = abs(a - b)
    return min(d, 360 - d)


def _in_angle(o, p, q, x):
    """0.0 if ray ox lies strictly inside angle p-o-q, else 1.0"""
    a = _angle(o, p, x) + _angle(o, x, q) - _angle(o, p, q)
    return 0.0 if abs(a) < 1e-6 else 1.0


def _seg_cross(p1, p2, p3, p4):
    """True if open segments p1p2 and p3p4 properly cross"""
    d1 = _cross(p3, p4, p1)
    d2 = _cross(p3, p4, p2)
    d3 = _cross(p1, p2, p3)
    d4 = _cross(p1, p2, p4)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))


def _path_self_crossings(pts, closed):
    """number of crossings between non-adjacent sides of a path/polygon"""
    n = len(pts)
    sides = [(pts[i], pts[i + 1]) for i in range(n - 1)]
    if closed:
        sides.append((pts[-1], pts[0]))
    hits = 0
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            if j == i + 1:
                continue
            if closed and i == 0 and j == len(sides) - 1:
                continue
            if _seg_cross(*sides[i], *sides[j]):
                hits += 1
    return hits


def _simple(pts):
    """0.0 if the closed polygon is simple (no non-adjacent side meets)"""
    return 0.0 if _path_self_crossings(pts, True) == 0 else 1.0


def _line_int(p1, p2, p3, p4):
    """intersection point of lines p1p2 and p3p4"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d,
            (a * (y3 - y4) - (y1 - y2) * b) / d)


def _cyc_gap(i, j, n):
    """cyclic index distance, so 1 == adjacent vertices"""
    d = abs(i - j) % n
    return min(d, n - d)


def _orient(pts):
    """+1 counterclockwise, -1 clockwise"""
    s = sum((pts[(i + 1) % len(pts)][0] - pts[i][0]) *
            (pts[(i + 1) % len(pts)][1] + pts[i][1]) for i in range(len(pts)))
    return -1 if s > 0 else 1


def build(check):
    # ---- 8-1 : r1 || r2, both rays on the same side of the line of vertices
    #            (Definition 8-2, "same direction")
    V1, V2 = (0.62, 1.15), (0.16, 0.0)
    r1, r2 = (1, 0), (1, 0)
    check('8-1', 'r1 || r2', par(r1, r2))
    tip1 = (V1[0] + 4.35, V1[1])
    tip2 = (V2[0] + 4.35, V2[1])
    check('8-1', 'both rays on one side of the vertex line',
          0.0 if _cross(V2, V1, tip1) * _cross(V2, V1, tip2) > 0 else 1.0)

    # ---- 8-2 : first proof of Thm 8-1.  n = AB, C on n beyond A, D on m,
    #            E on l, and angle DAC congruent to angle EBA -- so m || l.
    B2 = (1.1470, 0.0000)
    A2 = (1.9220, 1.4756)
    C2 = (2.1993, 2.0035)
    D2 = (3.0194, 1.4756)
    E2 = (2.5110, 0.0000)
    l2a, l2b = (0.4650, 0.0), (3.8440, 0.0)          # l as drawn
    m2a, m2b = (0.4340, 1.4756), (3.3790, 1.4756)    # m as drawn
    check('8-2', 'm || l', par(V(m2a, m2b), V(l2a, l2b)))
    check('8-2', 'A on m', _on_line(m2a, m2b, A2))
    check('8-2', 'D on m', _on_line(m2a, m2b, D2))
    check('8-2', 'B on l', _on_line(l2a, l2b, B2))
    check('8-2', 'E on l', _on_line(l2a, l2b, E2))
    check('8-2', 'C on line n = AB', _on_line(B2, A2, C2))
    check('8-2', 'C beyond A on ray BA', _same_dir(V(A2, C2), V(B2, A2)))
    check('8-2', 'angle DAC == angle EBA',
          abs(_angle(A2, D2, C2) - _angle(B2, E2, A2)))
    # "let D be a point on the same side of n as E" (first proof)
    check('8-2', 'D and E on the same side of n',
          0.0 if _cross(B2, A2, D2) * _cross(B2, A2, E2) > 0 else 1.0)

    # ---- 8-3 : the lemma's figure.  A on m and n, B on l and n, and m is
    #            deliberately NOT parallel to l.
    A3 = (1.5190, 1.4756)
    B3 = (0.7750, 0.0000)
    m3a, m3b = (0.7990, 1.6310), (3.5690, 1.0332)
    l3a, l3b = (-0.0250, -0.0594), (3.1950, 0.1796)
    n3a, n3b = (0.5769, -0.3929), (1.7531, 1.9399)
    check('8-3', 'A on m', _on_line(m3a, m3b, A3))
    check('8-3', 'A on n', _on_line(n3a, n3b, A3))
    check('8-3', 'B on l', _on_line(l3a, l3b, B3))
    check('8-3', 'B on n', _on_line(n3a, n3b, B3))
    # deliberately non-parallel: report the shortfall from 1 degree
    check('8-3', 'm not parallel to l',
          max(0.0, 1.0 - par(V(m3a, m3b), V(l3a, l3b))))
    # angle 1 (at A, between ray A-up-n and ray A-right-m) and angle 2
    # (at B, between ray B-up-n and ray B-right-l) are the corresponding
    # angles the lemma compares; each label must sit inside its own angle.
    Aup = lerp(B3, A3, 1.5)
    Amr = m3b
    Bup = A3
    Blr = l3b
    check('8-3', 'label 1 inside angle 1',
          _in_angle(A3, Aup, Amr, (2.0604, 1.7342)))
    check('8-3', 'label 2 inside angle 2',
          _in_angle(B3, Bup, Blr, (1.3238, 0.3666)))
    # The book puts an arrow "-> P" in the wedge between m and l, pointing the
    # way they converge (they meet far off the page).  Check both facts.
    def _y_at(p, q, xx):
        return p[1] + (q[1] - p[1]) * (xx - p[0]) / (q[0] - p[0])

    ax0, ax1, ay = 2.387, 2.945, 0.620
    check('8-3', 'the P arrow lies between l and m',
          0.0 if _y_at(l3a, l3b, ax1) < ay < _y_at(m3a, m3b, ax1) else 1.0)
    gap_left = _y_at(m3a, m3b, 0.80) - _y_at(l3a, l3b, 0.80)
    gap_right = _y_at(m3a, m3b, ax1) - _y_at(l3a, l3b, ax1)
    check('8-3', 'm and l converge the way the arrow points',
          0.0 if (gap_right < gap_left and ax1 > ax0) else 1.0)

    # ---- 8-4 : third proof.  A on m and n, B on l and n, AQ congruent to BP.
    A4 = (2.8830, 1.6244)
    B4 = (2.0460, 0.0000)
    P4 = (4.5880, 0.9424)
    Q4 = (0.1719, 1.6244)
    n4a, n4b = (1.9269, -0.2311), (3.0342, 1.9177)
    l4a, l4b = (0.0000, 0.0), (2.0460, 0.0)          # l as drawn
    check('8-4', 'AQ == BP', abs(dist(A4, Q4) - dist(B4, P4)) / dist(B4, P4))
    check('8-4', 'A on n', _on_line(n4a, n4b, A4))
    check('8-4', 'B on n', _on_line(n4a, n4b, B4))
    check('8-4', 'B on l', abs(B4[1] - 0.0))
    # m is the line QA; the third proof needs "the indicated angles at A and B
    # congruent to each other".  Those are the two arced corresponding angles
    # between n and each of m, l -- which forces m || l, exactly as the book
    # draws it (m and l both horizontal, each bent by a dashed curve to P).
    check('8-4', 'm || l', par(V(Q4, A4), V(l4a, l4b)))
    ang_A4 = _angle_at(A4, n4b) - _angle_at(A4, lerp(Q4, A4, 2.0))
    ang_B4 = _angle_at(B4, A4) - _angle_at(B4, lerp(l4a, l4b, 2.0))
    check('8-4', 'indicated angle at A == indicated angle at B',
          abs(ang_A4 - ang_B4))
    check('8-4', 'Q on the far side of n from P',
          0.0 if _cross(B4, A4, Q4) * _cross(B4, A4, P4) < 0 else 1.0)

    # ---- 8-5 : l || m and m || n (both given); l and n are drawn meeting at
    #            P, which is the contradiction.
    l5 = V((0.30, 1.90), (2.55, 1.90))
    n5 = V((0.30, 1.12), (2.55, 1.12))
    m5 = V((0.30, 0.34), (2.55, 0.34))
    check('8-5', 'l || m', par(l5, m5))
    check('8-5', 'm || n', par(m5, n5))

    # ---- 8-6 : l || m ; P is on both l and n
    check('8-6', 'l || m', par(V((0.20, 1.70), (3.70, 1.70)),
                               V((0.20, 0.42), (3.70, 0.42))))
    P6 = (1.72, 1.70)
    N6 = (2.86, 0.10)
    # n is drawn as the segment from P + (-0.28)(N6 - P) through to N6
    n6a = lerp(P6, N6, -0.28)
    check('8-6', 'P on l', abs(P6[1] - 1.70))
    check('8-6', 'P on n', _on_line(n6a, N6, P6))
    check('8-6', 'P interior to the drawn part of n',
          0.0 if min(n6a[0], N6[0]) < P6[0] < max(n6a[0], N6[0]) else 1.0)
    check('8-6', 'n != l', max(0.0, 1.0 - par(V(n6a, N6), V((0.20, 1.70),
                                                            (3.70, 1.70)))))
    check('8-6', 'n meets m', 0.0 if (P6[1] - 0.42) * (N6[1] - 0.42) < 0 else 1.0)

    # ---- 8-7 : angle ABC == angle BCD, hence AB || CD
    A7, B7 = (0.0, 0.0), (1.72, 0.0)
    C7 = (2.52, 0.86)
    D7 = (C7[0] + 1.72, C7[1])
    check('8-7', 'angle ABC == angle BCD',
          abs(_angle(B7, A7, C7) - _angle(C7, B7, D7)))
    check('8-7', 'AB || CD', par(V(A7, B7), V(C7, D7)))

    # ---- 8-8 : AB == CD ; angles at B and C right ; AD || BC
    B8, C8 = (0.0, 0.0), (3.05, 0.0)
    A8, D8 = (0.0, 1.72), (3.05, 1.72)
    check('8-8', 'AB == CD', abs(dist(A8, B8) - dist(D8, C8)) / dist(A8, B8))
    check('8-8', 'angle ABC right', perp(V(B8, A8), V(B8, C8)))
    check('8-8', 'angle BCD right', perp(V(C8, B8), V(C8, D8)))
    check('8-8', 'AD || BC', par(V(A8, D8), V(B8, C8)))

    # ---- 8-9 : the transversal meets l1 and l2 in distinct points, and each
    #            of the eight numbers sits inside the angle it names.
    L1a, L1b = (-0.0620, 1.1036), (3.0380, 1.0745)
    L2a, L2b = (0.0620, 0.1240), (3.0380, 0.3887)
    La, Lb = (1.3640, 1.5047), (2.3355, 0.0000)
    X1 = (1.6333, 1.0877)
    X2 = (2.1363, 0.3085)
    check('8-9', 'X1 on l1', _on_line(L1a, L1b, X1))
    check('8-9', 'X1 on l', _on_line(La, Lb, X1))
    check('8-9', 'X2 on l2', _on_line(L2a, L2b, X2))
    check('8-9', 'X2 on l', _on_line(La, Lb, X2))
    check('8-9', 'X1 != X2', max(0.0, 0.5 - dist(X1, X2)))
    # book's orientation: the upper crossing lies LEFT of the lower one
    check('8-9', 'transversal leans as the book draws it',
          0.0 if X1[0] < X2[0] else 1.0)
    nums = {1: ((1.8070, 1.4030), L1b, La), 2: ((1.3180, 1.2614), La, L1a),
            3: ((1.4596, 0.7724), L1a, X2), 4: ((1.9486, 0.9140), X2, L1b),
            5: ((2.2943, 0.6320), L2b, X1), 6: ((1.8128, 0.4665), X1, L2a),
            7: ((1.9783, -0.0150), L2a, Lb), 8: ((2.4598, 0.1505), Lb, L2b)}
    for k, (pt, p, q) in nums.items():
        o = X1 if k <= 4 else X2
        check('8-9', f'label {k} inside its own angle', _in_angle(o, p, q, pt))
    # Definition 8-8's own classification, checked against the drawing.
    pt_of = {k: v[0] for k, v in nums.items()}

    def _same_side(a, b, p, q):
        return _cross(a, b, p) * _cross(a, b, q) > 0

    interior, exterior = (3, 4, 5, 6), (1, 2, 7, 8)
    for k in interior:
        ref = L2a if k <= 4 else L1a
        base = (L1a, L1b) if k <= 4 else (L2a, L2b)
        check('8-9', f'angle {k} is interior',
              0.0 if _same_side(base[0], base[1], pt_of[k], ref) else 1.0)
    for k in exterior:
        ref = L2a if k <= 4 else L1a
        base = (L1a, L1b) if k <= 4 else (L2a, L2b)
        check('8-9', f'angle {k} is exterior',
              0.0 if not _same_side(base[0], base[1], pt_of[k], ref) else 1.0)
    # "corresponding angles have their interiors on the same side of l;
    #  alternate angles have them on opposite sides of l"
    for a, b in ((1, 5), (2, 6), (3, 7), (4, 8)):
        check('8-9', f'corresponding pair {a},{b} on one side of l',
              0.0 if _same_side(La, Lb, pt_of[a], pt_of[b]) else 1.0)
        check('8-9', f'corresponding pair {a},{b} is one interior one exterior',
              0.0 if (a in interior) != (b in interior) else 1.0)
    for a, b in ((3, 5), (2, 8), (1, 7), (4, 6)):
        check('8-9', f'alternate pair {a},{b} on opposite sides of l',
              0.0 if not _same_side(La, Lb, pt_of[a], pt_of[b]) else 1.0)

    # ---- 8-10 : l1 || l2 ; C, A, F on l1 ; B, D on l2 ; E on l beyond A ;
    #             G is drawn just off l1 on purpose -- the proof concludes
    #             that G must in fact lie on l1.
    L1 = ((-0.20, 1.42), (3.60, 1.42))
    L2 = ((-0.20, 0.30), (3.60, 0.30))
    A10, B10 = (1.62, 1.42), (1.34, 0.30)
    C10, F10, D10 = (0.42, 1.42), (3.00, 1.42), (2.85, 0.30)
    E10 = lerp(B10, A10, 1.68)
    G10 = (2.60, 1.86)
    check('8-10', 'l1 || l2', par(V(*L1), V(*L2)))
    for nm, p in (('A', A10), ('C', C10), ('F', F10)):
        check('8-10', f'{nm} on l1', _on_line(L1[0], L1[1], p))
    for nm, p in (('B', B10), ('D', D10)):
        check('8-10', f'{nm} on l2', _on_line(L2[0], L2[1], p))
    check('8-10', 'E on line l beyond A', _on_line(B10, A10, E10))
    check('8-10', 'C and F on opposite sides of l',
          0.0 if _cross(B10, A10, C10) * _cross(B10, A10, F10) < 0 else 1.0)
    check('8-10', 'G interior to angle DBE', _in_angle(B10, D10, E10, G10))

    # ---- 8-11 : AO == CO, BO == OD ; hence AB || CD and BC || AD
    O11 = (2.05, 0.92)
    A11, B11 = (1.15, 0.0), (0.0, 0.72)
    C11 = lerp(A11, O11, 2.0)
    D11 = lerp(B11, O11, 2.0)
    check('8-11', 'AO == CO', abs(dist(A11, O11) - dist(C11, O11)) / dist(A11, O11))
    check('8-11', 'BO == OD', abs(dist(B11, O11) - dist(D11, O11)) / dist(B11, O11))
    check('8-11', 'AB || CD', par(V(A11, B11), V(C11, D11)))
    check('8-11', 'BC || AD', par(V(B11, C11), V(A11, D11)))
    check('8-11', 'O is where AC meets BD',
          dist(O11, _line_int(A11, C11, B11, D11)))
    check('8-11', 'A and C on opposite sides of BD',
          0.0 if _cross(B11, D11, A11) * _cross(B11, D11, C11) < 0 else 1.0)

    # ---- 8-12 : OB is interior to angle AOC
    O12 = (0.0, 0.0)
    A12 = (2.15 * math.cos(math.radians(76)), 2.15 * math.sin(math.radians(76)))
    B12 = (1.80 * math.cos(math.radians(48)), 1.80 * math.sin(math.radians(48)))
    C12 = (2.45 * math.cos(math.radians(-9)), 2.45 * math.sin(math.radians(-9)))
    check('8-12', 'OB interior to angle AOC', _in_angle(O12, A12, C12, B12))
    check('8-12', 'angle AOC is not a straight angle',
          max(0.0, 1.0 - abs(180.0 - _angle(O12, A12, C12))))

    # ---- 8-13 : l || BC through A ; D and E on l, on opposite sides of AB
    B13, C13 = (0.0, 0.0), (3.35, 0.0)
    A13 = (1.675, 1.90)
    l13a = (A13[0] - 1.72, A13[1])
    l13b = (A13[0] + 1.72, A13[1])
    D13 = (A13[0] - 1.15, A13[1])
    E13 = (A13[0] + 1.15, A13[1])
    check('8-13', 'l || BC', par(V(l13a, l13b), V(B13, C13)))
    check('8-13', 'A on l', _on_line(l13a, l13b, A13))
    check('8-13', 'D on l', _on_line(l13a, l13b, D13))
    check('8-13', 'E on l', _on_line(l13a, l13b, E13))
    check('8-13', 'D and E on opposite sides of AB',
          0.0 if _cross(A13, B13, D13) * _cross(A13, B13, E13) < 0 else 1.0)
    check('8-13', 'E on the same side of AB as C',
          0.0 if _cross(A13, B13, E13) * _cross(A13, B13, C13) > 0 else 1.0)

    # ---- 8-14 : A'B'C' is congruent to ABC (opposite sense, as drawn), so
    #             AB == A'B', angle A == angle A', angle C == angle C'
    A14, B14, C14 = (0.0, 1.35), (0.39, 0.0), (2.34, 0.78)
    Cp = (1.2000, 2.1000)
    Ap = (3.4950, 2.8302)
    Bp = (3.1992, 1.4565)
    check('8-14', "AB == A'B'",
          abs(dist(A14, B14) - dist(Ap, Bp)) / dist(A14, B14))
    check('8-14', "BC == B'C'",
          abs(dist(B14, C14) - dist(Bp, Cp)) / dist(B14, C14))
    check('8-14', "CA == C'A'",
          abs(dist(C14, A14) - dist(Cp, Ap)) / dist(C14, A14))
    check('8-14', "angle A == angle A'",
          abs(_angle(A14, B14, C14) - _angle(Ap, Bp, Cp)))
    check('8-14', "angle C == angle C'",
          abs(_angle(C14, A14, B14) - _angle(Cp, Ap, Bp)))
    check('8-14', 'the two triangles do not overlap',
          0.0 if min(Cp[1], Ap[1], Bp[1]) >
          max(A14[1], B14[1], C14[1]) - 0.60 else 1.0)
    # the book draws the primed triangle in the opposite sense (mirrored),
    # up and to the right of ABC -- verified against the source figure
    check('8-14', "A'B'C' drawn in the opposite sense from ABC",
          0.0 if _orient([A14, B14, C14]) != _orient([Ap, Bp, Cp]) else 1.0)

    # ---- 8-15 : angle A right ; AD perpendicular to BC ; D between B and C
    B15, C15 = (0.0, 0.0), (3.45, 0.0)
    M15 = lerp(B15, C15, 0.5)
    A15 = (M15[0] + 1.725 * math.cos(math.radians(65)),
           M15[1] + 1.725 * math.sin(math.radians(65)))
    D15 = foot(B15, C15, A15)
    check('8-15', 'angle BAC right', perp(V(A15, B15), V(A15, C15)))
    check('8-15', 'AD perp BC', perp(V(A15, D15), V(B15, C15)))
    check('8-15', 'D between B and C',
          0.0 if B15[0] < D15[0] < C15[0] else 1.0)

    # ---- 8-16 : D is the midpoint of BC ; BD == AD
    B16, C16 = (0.0, 0.0), (3.45, 0.0)
    D16 = lerp(B16, C16, 0.5)
    A16 = (D16[0] + 1.725 * math.cos(math.radians(62)),
           D16[1] + 1.725 * math.sin(math.radians(62)))
    check('8-16', 'D midpoint of BC',
          abs(dist(B16, D16) - dist(D16, C16)) / dist(B16, C16))
    check('8-16', 'BD == AD', abs(dist(B16, D16) - dist(A16, D16)) / dist(B16, D16))
    check('8-16', 'D between B and C',
          0.0 if B16[0] < D16[0] < C16[0] else 1.0)

    # ---- 8-17 : a plain polygonal path P1..Pn -- the book's does not cross
    #             itself (the crossing case is saved for Fig 8-18)
    path17 = [(0, 0.30), (1.15, 0.92), (0.62, 2.62), (1.72, 1.72),
              (2.35, 2.42), (2.95, 1.05), (2.28, 0)]
    check('8-17', 'path has 7 vertices / 6 sides', abs(len(path17) - 7))
    check('8-17', 'path does not cross itself',
          float(_path_self_crossings(path17, False)))

    # ---- 8-18 : "See Fig. 8-18 for a six-sided path" that does cross itself
    path18 = [(0, 0.62), (3.35, 1.42), (1.05, 2.62), (0.62, 0),
              (1.95, 2.62), (2.05, 0), (0.30, 1.95)]
    check('8-18', 'six-sided path (7 vertices)', abs(len(path18) - 7))
    check('8-18', 'the path really does cross itself',
          0.0 if _path_self_crossings(path18, False) > 0 else 1.0)

    # ---- 8-19 : the three polygons are simple (Fig 8-19 "Simple polygons")
    quad19 = [(0, 0), (0, 1.703), (2.350, 1.862), (2.350, 0.044)]
    tri19 = [(0, 0), (1.01, 1.82), (2.62, 0)]
    pent19 = [(0, 1.275), (1.214, 1.213), (1.565, 2.418),
              (2.621, 1.803), (1.346, 0)]
    check('8-19', 'quadrilateral has 4 vertices', abs(len(quad19) - 4))
    check('8-19', 'triangle has 3 vertices', abs(len(tri19) - 3))
    check('8-19', 'pentagon has 5 vertices', abs(len(pent19) - 5))
    for nm, poly in (('quadrilateral', quad19), ('triangle', tri19),
                     ('pentagon', pent19)):
        check('8-19', f'{nm} is simple', _simple(poly))
    check('8-19', 'the third polygon is not convex', 1.0 - _convex(pent19))

    # ---- 8-20 : the left quadrilateral's two marked angles are consecutive
    #             (they share a side); the right figure is a pentagon and the
    #             two dashed segments join non-adjacent vertices (diagonals).
    a = [(0, 0), (2.42, 0), (2.42, 1.42), (0.55, 1.42)]
    # the two arcs are centred at a[1] and a[2]: Definition 8-8 calls angles
    # "consecutive" exactly when their vertices are adjacent
    check('8-20', 'marked angles are consecutive (adjacent vertices)',
          float(abs(_cyc_gap(1, 2, len(a)) - 1)))
    check('8-20', 'left figure is a simple quadrilateral',
          max(float(abs(len(a) - 4)), _simple(a)))
    b = [(0, 0), (0.373, 1.779), (2.315, 1.779), (2.929, 0.886), (2.286, 0)]
    check('8-20', 'right figure is a pentagon', abs(len(b) - 5))
    # the two dashed segments drawn are b1-b3 and b3-b5; a diagonal joins
    # nonadjacent vertices
    for i, j in ((0, 2), (2, 4)):
        check('8-20', f'b{i+1}b{j+1} joins nonadjacent vertices',
              0.0 if _cyc_gap(i, j, len(b)) > 1 else 1.0)
    # the "adjacent sides" arrows land on b1b2 and b2b3, which share vertex b2
    check('8-20', 'called-out sides are adjacent (share b2)',
          float(abs(_cyc_gap(0, 1, len(b)) - 1) + abs(_cyc_gap(1, 2, len(b)) - 1)))
    check('8-20', 'pentagon is convex', _convex(b))
    check('8-20', 'pentagon is simple', _simple(b))
    # Leaders (rebuilt 2026-08-17 from the book photograph).  Each caption
    # fans BOTH of its leaders from one apex, and the two never cross.
    capex = (1.21, 1.77)
    ctipU = (a[2][0] + 0.40 * math.cos(math.radians(205)),
             a[2][1] + 0.40 * math.sin(math.radians(205)))
    ctipL = (a[1][0] + 0.375 * math.cos(math.radians(131)),
             a[1][1] + 0.375 * math.sin(math.radians(131)))
    check('8-20', 'consecutive-angle arrowheads land on their arcs',
          abs(dist(a[2], ctipU) - 0.40) + abs(dist(a[1], ctipL) - 0.375))
    # the arcs really are the two consecutive angles: the upper tip must lie
    # inside angle a4-a3-a2 and the lower one inside angle a3-a2-a1
    check('8-20', 'upper arrowhead lands inside the upper marked angle',
          _in_angle(a[2], a[3], a[1], ctipU))
    check('8-20', 'lower arrowhead lands inside the lower marked angle',
          _in_angle(a[1], a[2], a[0], ctipL))
    # the shallower leader must reach the UPPER arc and the steeper one the
    # lower arc; serving them the other way round is what made the two cross
    check('8-20', 'shallower consecutive-angle leader serves the upper arc',
          0.0 if (ctipU[1] > ctipL[1] and
                  _angle_at(capex, ctipU) > _angle_at(capex, ctipL)) else 1.0)
    aapex = (0.06, 2.171)
    atipT = lerp(b[1], b[2], 0.15)          # on the top side b2b3
    atipL = lerp(b[0], b[1], 0.74)          # on the left side b1b2
    check('8-20', 'adjacent-side arrowheads land on the two called-out sides',
          _on_line(b[1], b[2], atipT) + _on_line(b[0], b[1], atipL))
    dapex = (1.421, 1.855)
    dtipA = lerp(b[0], b[2], 0.62)          # on diagonal b1b3
    dtipB = lerp(b[2], b[4], 0.53)          # on diagonal b3b5
    check('8-20', 'diagonal arrowheads land on the two dashed diagonals',
          _on_line(b[0], b[2], dtipA) + _on_line(b[2], b[4], dtipB))
    # each apex sits ABOVE the shape it points into, so both of its leaders
    # travel downward -- the book never runs a leader up into the drawing
    for nm, (apex, t1, t2) in (('consecutive', (capex, ctipU, ctipL)),
                               ('adjacent', (aapex, atipT, atipL)),
                               ('diagonal', (dapex, dtipA, dtipB))):
        check('8-20', f'{nm} leaders both run downward from their apex',
              0.0 if apex[1] > t1[1] and apex[1] > t2[1] else 1.0)
    # every leader is short: the book's longest is about 1.8 units here
    for nm, (p0, p1) in (('consecutive upper', (capex, ctipU)),
                         ('consecutive lower', (capex, ctipL)),
                         ('adjacent top', (aapex, atipT)),
                         ('adjacent left', (aapex, atipL)),
                         ('diagonal long', (dapex, dtipA)),
                         ('diagonal vertical', (dapex, dtipB))):
        check('8-20', f'{nm} leader is short', max(0.0, dist(p0, p1) - 1.85))

    # ---- 8-21 : one quadrilateral convex, the other not
    conv = [(0, 0), (1.86, 0), (2.05, 1.42), (0.42, 1.62)]
    nonc = [(0, 0.55), (1.30, 1.05), (2.62, 0.0), (1.15, 0.62)]
    check('8-21', 'left quadrilateral is convex', _convex(conv))
    check('8-21', 'right quadrilateral is not convex', 1.0 - _convex(nonc))
    # Definition 8-9 speaks of a *simple* polygon being convex or not, so both
    # of these must be simple
    check('8-21', 'left quadrilateral is simple', _simple(conv))
    check('8-21', 'right quadrilateral is simple', _simple(nonc))

    # ---- 8-22 : a pentagon splits into three triangles from one vertex, and
    #             carries one exterior angle at each vertex.  Each exterior
    #             ray must be the OPPOSITE ray of the side arrived on, and
    #             each number must sit inside its own exterior angle.
    v = [(1.3360, 0.0000), (2.9500, 0.0230), (2.9090, 1.0060),
         (1.0290, 1.6310), (0.0000, 0.5490)]
    ends = [(1.7060, -0.1520), (3.3500, 0.0287), (2.8923, 1.4057),
            (0.6494, 1.7572), (-0.2757, 0.2591)]
    labs = [(2.1711, -0.1587), (3.2935, 0.3863), (2.6081, 1.4053),
            (0.5245, 1.5050), (0.1044, 0.0600)]
    check('8-22', 'pentagon -> 3 triangles', abs((len(v) - 2) - 3))
    check('8-22', 'pentagon is convex', _convex(v))
    check('8-22', 'pentagon is simple', _simple(v))
    # the two dashed diagonals are drawn from v1, to v3 and v4
    for j in (2, 3):
        check('8-22', f'diagonal v1v{j+1} joins nonadjacent vertices',
              0.0 if _cyc_gap(0, j, len(v)) > 1 else 1.0)
    # the book's own arithmetic: interior angles = 3 straight angles, so the
    # five exterior angles must total two straight angles
    int_sum = sum(_angle(v[i], v[i - 1], v[(i + 1) % 5]) for i in range(5))
    check('8-22', 'interior angles total three straight angles',
          abs(int_sum - 540.0))
    ext_sum = sum(180.0 - _angle(v[i], v[i - 1], v[(i + 1) % 5])
                  for i in range(5))
    check('8-22', 'exterior angles total two straight angles',
          abs(ext_sum - 360.0))
    for i in range(5):
        cur, prv, nxt = v[i], v[i - 1], v[(i + 1) % 5]
        check('8-22', f'exterior ray {i+1} extends the arriving side',
              _same_dir(V(cur, ends[i]), V(prv, cur)))
        check('8-22', f'number {i+1} inside its exterior angle',
              _in_angle(cur, ends[i], nxt, labs[i]))

    # ---- 8-23 : an n-gon splits into n-2 triangles (n = 7 as drawn)
    w = [(0.0000, 1.6150), (0.3610, 2.6980), (0.8740, 2.7930), (3.0400, 1.4630),
         (2.8690, 0.6840), (1.9190, 0.0000), (0.7600, 0.0380)]
    check('8-23', 'heptagon -> 5 triangles', abs((len(w) - 2) - 5))
    check('8-23', 'four diagonals drawn from one vertex', abs(4 - (len(w) - 3)))
    check('8-23', 'heptagon is convex', _convex(w))
    check('8-23', 'heptagon is simple', _simple(w))
    for j in (2, 3, 4, 5):
        check('8-23', f'diagonal w1w{j+1} joins nonadjacent vertices',
              0.0 if _cyc_gap(0, j, len(w)) > 1 else 1.0)
    int_sum7 = sum(_angle(w[i], w[i - 1], w[(i + 1) % len(w)])
                   for i in range(len(w)))
    check('8-23', 'interior angles total (n-2) straight angles',
          abs(int_sum7 - (len(w) - 2) * 180.0))
    check('8-23', 'exterior ray at w3 extends side w2w3',
          _same_dir(V(w[2], (1.4836, 2.9059)), V(w[1], w[2])))
    check('8-23', 'exterior ray at w4 extends side w5w4',
          _same_dir(V(w[3], (3.1729, 2.0686)), V(w[4], w[3])))

    # ---- 8-24 : the star points are the vertices of a regular pentagon
    star = [(1.72 * math.cos(math.radians(90 + 72 * i)),
             1.72 * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
    rads = [dist((0, 0), p) for p in star]
    check('8-24', 'star points equidistant from centre',
          (max(rads) - min(rads)) / max(rads))
    seps = [dist(star[i], star[(i + 1) % 5]) for i in range(5)]
    check('8-24', 'star points equally spaced',
          (max(seps) - min(seps)) / max(seps))
    chords = [dist(star[i], star[(i + 2) % 5]) for i in range(5)]
    check('8-24', 'star drawn by joining every second vertex',
          (max(chords) - min(chords)) / max(chords))

    # ---- 8-25 : the four named quadrilaterals satisfy Definition 8-11
    pgram = [(0, 0), (1.42, 0), (1.86, 1.72), (0.44, 1.72)]
    check('8-25', 'parallelogram: opposite sides parallel',
          max(par(V(pgram[0], pgram[1]), V(pgram[3], pgram[2])),
              par(V(pgram[1], pgram[2]), V(pgram[0], pgram[3]))))
    rect = [(0, 0), (2.05, 0), (2.05, 1.62), (0, 1.62)]
    check('8-25', 'rectangle: is a parallelogram',
          max(par(V(rect[0], rect[1]), V(rect[3], rect[2])),
              par(V(rect[1], rect[2]), V(rect[0], rect[3]))))
    check('8-25', 'rectangle: has a right angle',
          perp(V(rect[0], rect[1]), V(rect[0], rect[3])))
    sq = [(0, 0), (1.62, 0), (1.62, 1.62), (0, 1.62)]
    check('8-25', 'square: is a rectangle',
          max(par(V(sq[0], sq[1]), V(sq[3], sq[2])),
              perp(V(sq[0], sq[1]), V(sq[0], sq[3]))))
    check('8-25', 'square: two congruent perpendicular sides',
          abs(dist(sq[0], sq[1]) - dist(sq[0], sq[3])) / dist(sq[0], sq[1]))
    rh = [(0, 0), (1.62, 0), (2.06, 1.56), (0.44, 1.56)]
    sides = [dist(rh[i], rh[(i + 1) % 4]) for i in range(4)]
    check('8-25', 'rhombus: equilateral',
          (max(sides) - min(sides)) / max(sides))
    check('8-25', 'rhombus: is a parallelogram',
          max(par(V(rh[0], rh[1]), V(rh[3], rh[2])),
              par(V(rh[1], rh[2]), V(rh[0], rh[3]))))
    # the four are meant to look like four different things: the plain
    # parallelogram and the rhombus must not be drawn with right angles, and
    # the rectangle must not be drawn square
    check('8-25', 'parallelogram drawn without a right angle',
          max(0.0, 8.0 - perp(V(pgram[0], pgram[1]), V(pgram[0], pgram[3]))))
    check('8-25', 'rhombus drawn without a right angle',
          max(0.0, 8.0 - perp(V(rh[0], rh[1]), V(rh[0], rh[3]))))
    check('8-25', 'rectangle drawn longer than it is tall',
          max(0.0, 0.15 - abs(dist(rect[0], rect[1]) - dist(rect[0], rect[3])) /
              dist(rect[0], rect[1])))

    # ---- 8-26 : D on BC, E on AB, F on AC, with DE || AC and DF || AB
    B26, C26 = (0.0, 0.0), (3.45, 0.0)
    A26 = (1.72, 1.86)
    D26 = lerp(B26, C26, 0.52)
    E26 = lerp(B26, A26, 0.52)
    F26 = lerp(C26, A26, 0.48)
    check('8-26', 'D on BC', _on_line(B26, C26, D26))
    check('8-26', 'E on AB', _on_line(A26, B26, E26))
    check('8-26', 'F on AC', _on_line(A26, C26, F26))
    check('8-26', 'DE || AC', par(V(D26, E26), V(A26, C26)))
    check('8-26', 'DF || AB', par(V(D26, F26), V(A26, B26)))

    # ---- 8-27 : regular hexagon ; FD perp DC ; FC == 2 * DC ; FC and AD
    #             bisect each other (Ex. 30, 31)
    hexv = [(1.42 * math.cos(math.radians(-60 + 60 * i)),
             1.42 * math.sin(math.radians(-60 + 60 * i))) for i in range(6)]
    hs = [dist(hexv[i], hexv[(i + 1) % 6]) for i in range(6)]
    check('8-27', 'hexagon equilateral', (max(hs) - min(hs)) / max(hs))
    angs = [_angle(hexv[i], hexv[i - 1], hexv[(i + 1) % 6]) for i in range(6)]
    check('8-27', 'hexagon equiangular', max(angs) - min(angs))
    Bh, Ch, Dh, Eh, Fh, Ah = (hexv[0], hexv[1], hexv[2],
                              hexv[3], hexv[4], hexv[5])
    check('8-27', 'FD perp DC', perp(V(Fh, Dh), V(Dh, Ch)))
    check('8-27', 'FC == 2 * DC',
          abs(dist(Fh, Ch) - 2 * dist(Dh, Ch)) / dist(Fh, Ch))
    check('8-27', 'FC and AD bisect each other',
          dist(lerp(Fh, Ch, 0.5), lerp(Ah, Dh, 0.5)))
    # ABCDEF must be consecutive vertices, and the drawn FD a real diagonal
    order = [Ah, Bh, Ch, Dh, Eh, Fh]
    sides = [dist(order[i], order[(i + 1) % 6]) for i in range(6)]
    check('8-27', 'A,B,C,D,E,F are consecutive vertices',
          (max(sides) - min(sides)) / max(sides))
    check('8-27', 'FD joins nonadjacent vertices (a diagonal)',
          0.0 if _cyc_gap(5, 3, 6) > 1 else 1.0)
    check('8-27', 'hexagon is convex', _convex(order))

    # ---- 8-28 : two cevians AQ, AR from A, with the six lettered angles as
    #             the book places them.  The exercise asserts
    #             x + y + t = r + s + z, so check the drawing satisfies it.
    B28, C28 = (0.0, 0.0), (3.45, 0.0)
    A28 = (1.2331, 1.7664)
    Q28 = lerp(B28, C28, 0.369)
    R28 = lerp(B28, C28, 0.620)
    for nm, P in (('Q', Q28), ('R', R28)):
        check('8-28', f'cevian foot {nm} lies on BC', _on_line(B28, C28, P))
        check('8-28', f'cevian foot {nm} lies strictly inside BC',
              0.0 if B28[0] < P[0] < C28[0] else 1.0)
    check('8-28', 'B, Q, R, C in that order',
          0.0 if B28[0] < Q28[0] < R28[0] < C28[0] else 1.0)
    check('8-28', 'A is off BC (a genuine triangle)',
          max(0.0, 0.20 - _on_line(B28, C28, A28)))
    x = _angle(B28, A28, C28)
    y = _angle(A28, B28, Q28)
    s = _angle(A28, R28, C28)
    z = _angle(Q28, A28, C28)
    t = _angle(R28, A28, B28)
    r = _angle(C28, A28, B28)
    check('8-28', 'x + y + t == r + s + z (Ex. 9)',
          abs((x + y + t) - (r + s + z)))
    # each letter must sit inside the angle it names
    lbl = {'x': ((0.4079, 0.2127), B28, A28, C28),
           'y': ((1.0307, 1.0963), A28, B28, Q28),
           's': ((1.7716, 1.1087), A28, R28, C28),
           'z': ((1.5527, 0.2860), Q28, A28, C28),
           't': ((1.7465, 0.2398), R28, A28, B28),
           'r': ((2.8459, 0.2113), C28, A28, B28)}
    for nm, (pt, o, p, q) in lbl.items():
        check('8-28', f'letter {nm} inside its angle', _in_angle(o, p, q, pt))

    # ---- 8-29 : AB == BC ; D on AC with angle CBD == 40 ; E on AB with
    #             BE == BD ; angle B obtuse, as the book draws it
    # The book slopes BC gently down to the right (C below B) -- that slope is
    # what makes angle DBC read as 40 degrees -- so BC runs at -5 degrees and
    # BA at 110 degrees, both of length 3.05.
    B29 = (0.0, 0.0)
    C29 = (3.05 * math.cos(math.radians(-5)), 3.05 * math.sin(math.radians(-5)))
    A29 = (3.05 * math.cos(math.radians(110)), 3.05 * math.sin(math.radians(110)))
    check('8-29', 'AB == BC', abs(dist(A29, B29) - dist(B29, C29)) / dist(B29, C29))
    # D as written into figures08.tex (the 40-degree ray from B meets AC there)
    D29 = (1.407456, 0.985597)
    check('8-29', 'D lies on AC', _on_line(A29, C29, D29))
    check('8-29', 'D between A and C',
          0.0 if min(A29[0], C29[0]) < D29[0] < max(A29[0], C29[0]) else 1.0)
    check('8-29', 'angle CBD == 40 degrees',
          abs(_angle(B29, C29, D29) - 40.0))
    check('8-29', 'BD lies inside angle ABC', _in_angle(B29, A29, C29, D29))
    check('8-29', 'base BC slopes down to the right (C below B)',
          0.0 if C29[1] < B29[1] else 1.0)
    E29 = lerp(B29, A29, 0.563356)
    check('8-29', 'E on AB', _on_line(A29, B29, E29))
    check('8-29', 'BE == BD', abs(dist(B29, E29) - dist(B29, D29)) / dist(B29, D29))
    check('8-29', 'angle ABC obtuse (as drawn)',
          max(0.0, 95.0 - _angle(B29, A29, C29)))

    # ---- 8-30 : AB == A'B' ; B is between A and C
    A30, B30, C30 = (0.0, 0.0), (1.05, 0.0), (1.86, 0.0)
    Ap30, Bp30 = (3.05, 0.0), (4.10, 0.0)
    check('8-30', "AB == A'B'",
          abs(dist(A30, B30) - dist(Ap30, Bp30)) / dist(A30, B30))
    check('8-30', 'B between A and C',
          0.0 if A30[0] < B30[0] < C30[0] else 1.0)

    # ---- 8-31 : angles CAB and ABD right ; CA == DB ; M, N midpoints ;
    #             MN perpendicular to both AB and CD
    A31, B31 = (0.0, 0.0), (3.05, 0.0)
    C31, D31 = (0.0, 1.62), (3.05, 1.62)
    M31 = lerp(C31, D31, 0.5)
    N31 = lerp(A31, B31, 0.5)
    check('8-31', 'angle CAB right', perp(V(A31, C31), V(A31, B31)))
    check('8-31', 'angle ABD right', perp(V(B31, A31), V(B31, D31)))
    check('8-31', 'CA == DB', abs(dist(C31, A31) - dist(D31, B31)) / dist(C31, A31))
    check('8-31', 'M midpoint of CD',
          abs(dist(C31, M31) - dist(M31, D31)) / dist(C31, D31))
    check('8-31', 'N midpoint of AB',
          abs(dist(A31, N31) - dist(N31, B31)) / dist(A31, B31))
    check('8-31', 'MN perp AB', perp(V(M31, N31), V(A31, B31)))
    check('8-31', 'MN perp CD', perp(V(M31, N31), V(C31, D31)))

    # ---- 8-32 : X on ray AP, Y on ray BP, both on the same side of AB, and
    #             angle XAB + angle YBA less than a straight angle (Euclid's
    #             form of the parallel postulate, Ex. 23)
    # Redrawn 2026-08-17 to the book's proportions: the upper line runs nearly
    # horizontal, the lower one climbs about 23 degrees, and the heavy dots
    # marking X and Y sit at 45 per cent -- well inside the solid part, which
    # only breaks into dashes at 70 per cent.
    A32, B32 = (0.0, 1.38), (0.0, 0.0)
    P32 = (3.40, 1.48)
    dot32, dash32, tip32 = 0.45, 0.70, 1.09   # ratios used in figures08.tex
    X32 = lerp(A32, P32, dot32)
    Y32 = lerp(B32, P32, dot32)
    # the dots must fall clear of the solid/dashed break, or they read as
    # marking the change of dash style rather than a point
    check('8-32', 'dots X, Y sit well inside the solid part',
          max(0.0, (dot32 + 0.10) - dash32))
    # the dashed tips cross AT P and run a little way past it, as the book
    # draws them -- no arrowhead, no stopping short
    check('8-32', 'dashed tips run past the meeting point P',
          max(0.0, 1.02 - tip32))
    # upper line nearly horizontal, lower one climbing: they close on P at a
    # very acute angle, which is the whole point of Euclid's postulate figure
    check('8-32', 'AP is nearly horizontal',
          max(0.0, abs(_angle_at(A32, P32)) - 5.0))
    check('8-32', 'rays AP and BP meet at an acute angle under 30 degrees',
          max(0.0, _angle(P32, A32, B32) - 30.0))
    check('8-32', 'X on ray AP', _on_line(A32, P32, X32))
    check('8-32', 'Y on ray BP', _on_line(B32, P32, Y32))
    sX = _cross(A32, B32, X32)
    sY = _cross(A32, B32, Y32)
    check('8-32', 'X and Y on the same side of AB',
          0.0 if sX * sY > 0 else 1.0)
    check('8-32', 'angle XAB + angle YBA < a straight angle',
          max(0.0, (_angle(A32, X32, B32) + _angle(B32, Y32, A32)) - 179.0))
    # X and Y are *constructed* on the segments AP and BP in figures08.tex, so
    # "the rays meet at P" is true by construction and worth nothing as a
    # check.  What is not automatic, and is what Euclid's postulate asserts, is
    # that the meeting point lies beyond X and Y on the X/Y side of AB -- i.e.
    # the dashed continuations really do converge, away from AB.
    check('8-32', 'meeting point is off AB (rays not collinear with AB)',
          max(0.0, 0.20 - abs(_cross(A32, B32, P32)) / dist(A32, B32)))
    check('8-32', 'they meet on the same side of AB as X and Y',
          0.0 if _cross(A32, B32, P32) * sX > 0 else 1.0)
    check('8-32', 'X between A and P', 0.0 if A32[0] < X32[0] < P32[0] else 1.0)
    check('8-32', 'Y between B and P', 0.0 if B32[0] < Y32[0] < P32[0] else 1.0)
