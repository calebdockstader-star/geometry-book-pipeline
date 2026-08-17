# Chapter 3 ("Concerning Lines") figure constraints.
# Coordinates mirror chapters/figures03.tex. Each entry encodes a hypothesis
# the BOOK states in the text or caption for that figure.
#
# Ch 3 is a postulates chapter: most of its hypotheses are incidence,
# betweenness and side-of-a-line facts (point on line, point between two
# points, two points on the same/opposite side, a ray and its opposite) rather
# than metric ones, so most checks below are stated as collinearity,
# betweenness-overshoot, or 0/1 predicates.
#
# Figures with no stated hypothesis to encode:
#   3-2  the same six lines seen through uneven glass -- the text's point is
#        precisely that NOTHING about them can be read off the picture;
#   3-15 the three-men illustration, carried as a plate.
from figlib import V, ang, par, perp, lerp, dist, foot  # noqa: F401
import math


def _collinear(a, b, p):
    """angular error (deg) of p off line ab"""
    return par(V(a, b), V(a, p))


def _param(a, b, p):
    """position of p along ab: 0 at a, 1 at b (projection)"""
    ab = V(a, b)
    ap = V(a, p)
    return (ap[0] * ab[0] + ap[1] * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)


def _between(a, b, p):
    """0 if p lies strictly between a and b (relative overshoot otherwise)"""
    t = _param(a, b, p)
    return 0.0 if 0.0 < t < 1.0 else min(abs(t), abs(t - 1.0))


def _side(a, b, p):
    """signed area: >0 left of ab, <0 right, 0 on it"""
    return (p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])


def _same_side(a, b, p, q):
    return 0.0 if _side(a, b, p) * _side(a, b, q) > 0 else 1.0


def _opp_side(a, b, p, q):
    return 0.0 if _side(a, b, p) * _side(a, b, q) < 0 else 1.0


def _noncollinear(a, b, c):
    """0 if a, b, c are genuinely not on one line (>=5 deg apart)"""
    return 0.0 if par(V(a, b), V(a, c)) >= 5.0 else 1.0


def _opposite_ray(o, p, q):
    """0 if ray OQ is exactly the ray opposite ray OP.

    Collinearity error in degrees, plus a hard 1.0 if q is on the SAME side of
    o as p (i.e. the same ray rather than the opposite one).
    """
    u, v = V(o, p), V(o, q)
    if u[0] * v[0] + u[1] * v[1] >= 0:
        return 1.0
    return par(u, v)


def _on_ray(o, far, p, line_a, line_b):
    """0 if p is on the ray from o towards far (and on line_a--line_b)"""
    err = _collinear(line_a, line_b, p)
    u, v = V(o, far), V(o, p)
    if u[0] * v[0] + u[1] * v[1] <= 0:
        return 1.0
    return err


def _in_triangle(a, b, c, p):
    s1, s2, s3 = _side(a, b, p), _side(b, c, p), _side(c, a, p)
    return 0.0 if (s1 > 0 and s2 > 0 and s3 > 0) or (s1 < 0 and s2 < 0 and s3 < 0) else 1.0


def _seg_dist(a, b, p):
    """distance from p to the segment ab"""
    t = max(0.0, min(1.0, _param(a, b, p)))
    return dist(p, lerp(a, b, t))


def _on_path(pts, p):
    """distance from p to the polyline through pts (the plotted curve)"""
    return min(_seg_dist(pts[i], pts[i + 1], p) for i in range(len(pts) - 1))


def _polar(o, deg, r):
    return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))


def _intersect(p1, p2, p3, p4):
    d1, d2 = V(p1, p2), V(p3, p4)
    den = d1[0] * d2[1] - d1[1] * d2[0]
    t = ((p3[0] - p1[0]) * d2[1] - (p3[1] - p1[1]) * d2[0]) / den
    return (p1[0] + t * d1[0], p1[1] + t * d1[1])


def build(check):
    # ================================================== 3-1  (book p. 44)
    # "A and B may appear to be the same distance apart as A' and B'."
    # Six digitized lines; A,B ride the baseline L1, A',B' ride L3.
    p1, q1 = (0.18, 0.985), (8.69, 0.80)
    p3, q3 = (4.06, 4.075), (7.60, 0.81)
    A, B = lerp(p1, q1, 0.085), lerp(p1, q1, 0.150)
    Ap, Bp = lerp(p3, q3, 0.83489), lerp(p3, q3, 0.72000)
    check('3-1', 'AB == A-prime B-prime',
          abs(dist(A, B) - dist(Ap, Bp)) / dist(A, B))
    check('3-1', 'A, B on the baseline', _collinear(p1, q1, A) + _collinear(p1, q1, B))
    check('3-1', 'A-prime, B-prime on line L3', _collinear(p3, q3, Ap) + _collinear(p3, q3, Bp))

    # 3-2: the SAME six lines and the SAME two pairs of points, seen through
    # uneven glass.  Nothing metric can be read off the picture (that is the
    # text's point), but A, B must still sit ON the first wobbly curve and
    # A', B' ON the third -- otherwise it is not the same drawing.
    c1_2 = [(0.245, 0.745), (1.30, 0.79), (2.35, 0.755), (3.40, 0.815),
            (4.45, 0.80), (5.50, 0.86), (6.45, 0.90), (7.40, 0.945)]
    c3_2 = [(4.05, 3.87), (4.52, 3.42), (4.95, 2.98), (5.40, 2.55),
            (5.85, 2.09), (6.30, 1.68), (6.75, 1.30), (7.185, 0.905)]
    check('3-2', 'A on the wobbly line L1', _on_path(c1_2, (0.83, 0.775)))
    check('3-2', 'B on the wobbly line L1', _on_path(c1_2, (1.28, 0.79)))
    check('3-2', 'A-prime on the wobbly line L3', _on_path(c3_2, (6.681, 1.359)))
    check('3-2', 'B-prime on the wobbly line L3', _on_path(c3_2, (6.319, 1.664)))

    # ================================================== 3-3, 3-4, 3-5 (p. 45)
    # 3-3: P is a point of the line l
    l0, l1 = (0, 0), (5.0, 0.55)
    P = (2.0, 0.22)
    check('3-3', 'P on l', _collinear(l0, l1, P))

    # 3-4: l and m have the point P in common
    la, lb = (0, 0.10), (4.8, 1.42)
    ma, mb = (0, 1.55), (4.8, 0.02)
    Pp = _intersect(la, lb, ma, mb)
    check('3-4', 'P on l', _collinear(la, lb, Pp))
    check('3-4', 'P on m', _collinear(ma, mb, Pp))

    # 3-5: the drawing that suggests Postulate Group I -- three points NOT all
    # on one line, and the three lines each through two of them.
    A5, B5, C5 = (2.35, 2.55), (0.75, 0.32), (4.25, 0.32)
    check('3-5', 'A, B, C not all on one line', _noncollinear(A5, B5, C5))
    for nm, (u, v) in (('AB', (A5, B5)), ('AC', (A5, C5)), ('BC', (B5, C5))):
        check('3-5', f'line {nm} drawn through both points',
              _collinear(u, v, lerp(u, v, -0.16)))

    # ================================================== 3-6, 3-7  (p. 46)
    # 3-6: the impossible picture for Theorem 3-1 -- l and m share TWO points.
    A6, B6 = (0.45, 0.55), (4.65, 1.15)
    lc1, lc2 = (1.7, 1.55), (3.3, 1.75)      # controls of curve l
    mc1, mc2 = (1.7, 0.10), (3.3, 0.35)      # controls of curve m
    check('3-6', 'A and B are two DIFFERENT points', 0.0 if dist(A6, B6) > 0.5 else 1.0)
    check('3-6', 'l and m are different curves',
          0.0 if dist(lc1, mc1) > 0.5 and dist(lc2, mc2) > 0.5 else 1.0)
    # the four tails continue the curves' end tangents (so A, B read as crossings)
    for nm, (base, ctrl) in (('l at A', (A6, lc1)), ('m at A', (A6, mc1)),
                             ('l at B', (B6, lc2)), ('m at B', (B6, mc2))):
        check('3-6', f'tail {nm} on the tangent', _collinear(base, ctrl, lerp(base, ctrl, -0.09)))

    # 3-7: proof of Theorem 3-2. l = line AB, m = line BC, n = line CA.
    A7, B7, C7 = (0.55, 0.35), (4.35, 0.62), (2.55, 2.60)
    check('3-7', 'A, B, C not all on one line', _noncollinear(A7, B7, C7))
    check('3-7', 'l is the line AB', _collinear(A7, B7, lerp(B7, A7, -0.16)))
    check('3-7', 'm is the line BC', _collinear(B7, C7, lerp(C7, B7, -0.20)))
    check('3-7', 'n is the line CA', _collinear(C7, A7, lerp(C7, A7, -0.20)))

    # ================================================== 3-8, 3-9  (p. 47)
    # 3-8: Ex. 3-1 #3 -- a and b cannot both be lines through P and Q.
    P8, Q8 = (0.40, 0.35), (4.55, 1.35)
    ac1, ac2 = (1.7, 1.35), (3.2, 1.70)
    bc1, bc2 = (1.8, 0.05), (3.4, 0.55)
    check('3-8', 'P and Q are two DIFFERENT points', 0.0 if dist(P8, Q8) > 0.5 else 1.0)
    check('3-8', 'a and b are different curves',
          0.0 if dist(ac1, bc1) > 0.5 and dist(ac2, bc2) > 0.5 else 1.0)
    for nm, (base, ctrl) in (('a at P', (P8, ac1)), ('b at P', (P8, bc1)),
                             ('a at Q', (Q8, ac2)), ('b at Q', (Q8, bc2))):
        check('3-8', f'tail {nm} on the tangent', _collinear(base, ctrl, lerp(base, ctrl, -0.10)))

    # 3-9: Ex. 3-1 #8 -- figure-eight; D and E must lie ON the right-hand lobe.
    A9, B9, C9 = (0.30, 1.05), (2.45, 1.05), (4.60, 0.92)

    def _bez_mid(p0, c1, c2, p3_):
        return ((p0[0] + 3 * c1[0] + 3 * c2[0] + p3_[0]) / 8.0,
                (p0[1] + 3 * c1[1] + 3 * c2[1] + p3_[1]) / 8.0)

    D9 = (3.5625, 1.74625)
    E9 = (3.5625, 0.32125)
    check('3-9', 'D on the upper arc BC', dist(D9, _bez_mid(B9, (3.05, 2.05), (4.10, 1.95), C9)))
    check('3-9', 'E on the lower arc BC', dist(E9, _bez_mid(B9, (3.05, 0.05), (4.10, 0.15), C9)))
    check('3-9', 'A, B, C are three different points',
          0.0 if min(dist(A9, B9), dist(B9, C9), dist(A9, C9)) > 0.5 else 1.0)
    # the book marks D on the upper arc and E on the lower one, so they fall on
    # opposite sides of the line A-C through the three crossings
    check('3-9', 'D and E on opposite sides of ABC', _opp_side(A9, C9, D9, E9))

    # 3-10: Ex. 3-1 #12 -- D on AB, E on AC, and the drawn line joins them.
    A10, B10, C10 = (2.45, 2.85), (0.35, 0.30), (4.55, 0.55)
    D10, E10 = lerp(A10, B10, 0.52), lerp(A10, C10, 0.52)
    check('3-10', 'D on AB', _collinear(A10, B10, D10))
    check('3-10', 'D between A and B', _between(A10, B10, D10))
    check('3-10', 'E on AC', _collinear(A10, C10, E10))
    check('3-10', 'E between A and C', _between(A10, C10, E10))
    check('3-10', 'A, B, C not all on one line', _noncollinear(A10, B10, C10))

    # ================================================== 3-11, 3-12  (p. 48)
    # 3-11 : ABC  (B between A and C)
    n0, n1 = (0, 0), (4.6, 0.62)
    A11, B11, C11 = (0.85, 0.115), (2.95, 0.398), (3.55, 0.478)
    for nm, p in (('A', A11), ('B', B11), ('C', C11)):
        check('3-11', f'{nm} on the line', _collinear(n0, n1, p))
    check('3-11', 'ABC: B between A and C', _between(A11, C11, B11))

    # 3-12 : ADB and ABC -- D between A and B, B between A and C
    A12, D12, B12, C12 = (0.60, 0.081), (2.05, 0.276), (2.60, 0.350), (4.05, 0.546)
    for nm, p in (('A', A12), ('D', D12), ('B', B12), ('C', C12)):
        check('3-12', f'{nm} on the line', _collinear(n0, n1, p))
    check('3-12', 'ADB: D between A and B', _between(A12, B12, D12))
    check('3-12', 'ABC: B between A and C', _between(A12, C12, B12))

    # ================================================== 3-13, 3-14  (p. 49)
    # Definition 3-1. 3-13: P, Q on the SAME side of l (no point of l between).
    la13, lb13 = (0, 0), (4.6, 1.55)
    P13, Q13 = (0.55, 1.95), (2.25, 1.95)
    check('3-13', 'P, Q strictly same side of l', _same_side(la13, lb13, P13, Q13))

    # 3-14: P, Q on OPPOSITE sides of l -- a point R of l is between them.
    la14, lb14 = (0.30, 0.05), (4.30, 2.30)
    P14, Q14 = (1.25, 2.10), (2.85, 0.20)
    R14 = _intersect(la14, lb14, P14, Q14)
    check('3-14', 'P, Q strictly opposite sides of l', _opp_side(la14, lb14, P14, Q14))
    check('3-14', 'R on l', _collinear(la14, lb14, R14))
    check('3-14', 'R between P and Q', _between(P14, Q14, R14))

    # ================================================== 3-16, 3-17  (p. 50)
    # Definition 3-2: P is a point of the segment AB
    A16, B16 = (0.20, 0.15), (3.55, 2.20)
    P16 = lerp(A16, B16, 0.46)
    check('3-16', 'P on segment AB', _collinear(A16, B16, P16))
    check('3-16', 'P between A and B', _between(A16, B16, P16))

    # Definition 3-3: triangle ABC -- three points NOT all on one line
    A17, B17, C17 = (2.05, 2.45), (0.25, 0.20), (3.75, 0.05)
    check('3-17', 'A, B, C not all on one line', _noncollinear(A17, B17, C17))

    # ================================================== 3-18  (p. 52)
    # Ex. 3-2 *15: l contains no vertex of triangle ABC, meets side AB, and
    # does NOT meet side BC (whence it must meet AC).
    C18, B18, A18 = (1.85, 2.60), (0.20, 0.30), (4.30, 0.35)
    X18 = lerp(B18, A18, 0.42)          # on side AB (the base)
    Y18 = lerp(C18, A18, 0.52)          # on side CA
    check('3-18', 'l meets side AB, strictly between', _between(B18, A18, X18))
    check('3-18', 'l meets side CA, strictly between', _between(C18, A18, Y18))
    check('3-18', 'l misses side BC', _same_side(X18, Y18, B18, C18))
    for nm, vtx in (('A', A18), ('B', B18), ('C', C18)):
        check('3-18', f'l does not pass through {nm}',
              0.0 if abs(_side(X18, Y18, vtx)) / dist(X18, Y18) > 0.15 else 1.0)

    # ================================================== 3-19 .. 3-23  (pp. 52-53)
    # 3-19: O is a point of l, separating it into two sides.  The two braces
    # must lie strictly on their own sides of O, and each caption over its brace.
    O19 = (2.55, 0.0)
    check('3-19', 'O on l', _collinear((0, 0), (5.4, 0), O19))
    check('3-19', 'One-side brace is left of O', 0.0 if 2.45 < O19[0] else 1.0)
    check('3-19', 'Other-side brace is right of O', 0.0 if 2.65 > O19[0] else 1.0)
    check('3-19', 'One-side caption over its brace',
          0.0 if 0.35 < 1.40 < 2.45 else 1.0)
    check('3-19', 'Other-side caption over its brace',
          0.0 if 2.65 < 3.80 < 4.95 else 1.0)
    # The spans are curly braces (\IIIbrace{left}{mid}{right}{base}), not the
    # squared brackets of the first draft: each one must point up at its own
    # midpoint, and the two must meet over O without overlapping it.
    for nm, (bl, bm, br) in (('One side', (0.35, 1.40, 2.45)),
                             ('Other side', (2.65, 3.80, 4.95))):
        check('3-19', f'{nm} brace tip is at its own midpoint',
              abs(bm - (bl + br) / 2.0))
        check('3-19', f'{nm} brace clears the point O',
              0.0 if (br < O19[0] or bl > O19[0]) else 1.0)
    check('3-19', 'the two braces do not overlap',
          max(0.0, 2.45 - 2.65))

    # 3-20: proof of Thm 3-3 -- m is the line through O and a point A not on l.
    la20, lb20 = (0.0, 0.55), (4.35, 0.55)
    ma20, mb20 = (1.05, -0.45), (2.95, 2.40)
    O20 = _intersect(la20, lb20, ma20, mb20)
    A20 = lerp(ma20, mb20, 0.79)
    check('3-20', 'O on l', _collinear(la20, lb20, O20))
    check('3-20', 'O on m', _collinear(ma20, mb20, O20))
    check('3-20', 'A on m', _collinear(ma20, mb20, A20))
    check('3-20', 'A is NOT on l', 0.0 if abs(A20[1] - 0.55) > 0.20 else 1.0)

    # 3-21 : POQ -- P and Q are points of l on opposite sides of O
    Q21, P21 = lerp(la20, lb20, 0.138), lerp(la20, lb20, 0.655)
    check('3-21', 'O on m', _collinear(ma20, mb20, O20))
    check('3-21', 'P, O, Q collinear on l', _collinear(Q21, P21, O20))
    check('3-21', 'POQ: O between P and Q', _between(P21, Q21, O20))

    # 3-22 : ray OP -- P is a point of the ray from O; the rest of l is dashed
    O22, l22 = (1.05, 0.35), (4.35, 1.32)
    P22 = lerp(O22, l22, 0.394)
    check('3-22', 'P on ray OP', _on_ray(O22, l22, P22, O22, l22))
    check('3-22', 'dashed part is the opposite ray',
          _opposite_ray(O22, l22, lerp(O22, l22, -0.318)))

    # 3-23 : P is on l, and r is a ray from P not on l
    P23 = (2.05, 0.30)
    check('3-23', 'P on l', _collinear((0.15, 0.30), (4.35, 0.30), P23))
    check('3-23', 'r is not along l',
          0.0 if par(V(P23, (3.35, 2.55)), (1.0, 0.0)) > 5.0 else 1.0)

    # ================================================== 3-24, 3-25  (p. 54)
    # Definition 3-6. (iii) angle AOB is not a straight angle;
    # (iv) the straight angle: O between the two ends of one line.
    O24, A24, B24 = (3.55, 2.20), (2.55, 3.10), (2.85, 1.25)
    check('3-24', 'AOB is a genuine angle', _noncollinear(O24, A24, B24))
    # drawings (i) and (ii): two rays from a common vertex, neither pair being
    # a straight angle (only drawing (iv) is the straight angle)
    check('3-24', '(i) is a genuine angle at O',
          _noncollinear((0.30, 2.05), (1.85, 2.95), (1.85, 2.05)))
    check('3-24', '(ii) is a genuine angle at O',
          _noncollinear((0.62, 1.35), (2.05, 1.05), (-0.15, 0.20)))
    check('3-24', 'straight angle: O on the line', _collinear((0.85, 0.0), (3.35, 0.0), (2.05, 0.0)))
    check('3-24', 'straight angle: O between the ends', _between((0.85, 0.0), (3.35, 0.0), (2.05, 0.0)))

    # 3-25: (a)(b)(c) -- each arc must start and finish ON the two sides.
    for fig, O25, r1, r2, a1, a2, rad in (
            ('3-25a', (0.15, 2.55), (1.90, 3.15), (1.75, 2.10), 18.93, -15.71, 1.05),
            ('3-25b', (0.15, 1.35), (1.90, 1.95), (1.75, 0.90), 18.93, -15.71, 1.05),
            ('3-25c', (0.35, 0.10), (2.10, 0.10), (-0.25, 0.95), 0.0, 125.18, 0.90)):
        check(fig, 'arc starts on the first side', par(V(O25, _polar(O25, a1, rad)), V(O25, r1)))
        check(fig, 'arc ends on the second side', par(V(O25, _polar(O25, a2, rad)), V(O25, r2)))
    # (b) is the SAME angle as (a), drawn with the simpler notation (the text
    # says so outright); (c) is the obtuse one carrying the big arc.
    check('3-25', '(b) draws the same angle as (a)',
          par(V((0.15, 2.55), (1.90, 3.15)), V((0.15, 1.35), (1.90, 1.95)))
          + par(V((0.15, 2.55), (1.75, 2.10)), V((0.15, 1.35), (1.75, 0.90))))
    Oc25, c25u, c25w = (0.35, 0.10), (2.10, 0.10), (-0.25, 0.95)
    du, dw = V(Oc25, c25u), V(Oc25, c25w)
    check('3-25', '(c) is obtuse',
          0.0 if du[0] * dw[0] + du[1] * dw[1] < 0 else 1.0)

    # ================================================== 3-26  (p. 54)
    # Definition 3-7. Two lines through O; 1&2 and 3&4 are vertical pairs,
    # which requires each pair of opposite rays to be collinear through O.
    L1_26, L2_26 = (4.85, 2.05), (0.35, 0.15)
    M1_26, M2_26 = (4.85, 0.35), (0.35, 1.95)
    O26 = _intersect(L2_26, L1_26, M2_26, M1_26)
    check('3-26', 'l1, O, l2 collinear', _collinear(L2_26, L1_26, O26))
    check('3-26', 'm1, O, m2 collinear', _collinear(M2_26, M1_26, O26))
    check('3-26', 'l2 is the ray opposite l1', _opposite_ray(O26, L1_26, L2_26))
    check('3-26', 'm2 is the ray opposite m1', _opposite_ray(O26, M1_26, M2_26))
    # each arc spans exactly one of the four regions, ending on its two rays
    for nm, a, b, ra, rb in (('1', 160.44, 202.89, M2_26, L2_26),
                             ('2', -19.58, 22.90, M1_26, L1_26),
                             ('3', 22.90, 160.44, L1_26, M2_26),
                             ('4', 202.89, 340.42, L2_26, M1_26)):
        check('3-26', f'arc {nm} starts on its ray', par(V(O26, _polar(O26, a, 0.62)), V(O26, ra)))
        check('3-26', f'arc {nm} ends on its ray', par(V(O26, _polar(O26, b, 0.62)), V(O26, rb)))
        mid = _polar(O26, (a + b) / 2.0, 0.95)
        check('3-26', f'numeral {nm} inside its region',
              _same_side(O26, ra, mid, rb) + _same_side(O26, rb, mid, ra))

    # ================================================== 3-27, 3-28  (pp. 54-55)
    # Definition 3-8 (adjacent): a common vertex, a common side, and the two
    # other sides on opposite sides of the common one.
    # angles below are the ones the tex actually draws the arcs at, so the
    # check is that the DRAWN arc lands on the drawn ray, not a tautology.
    for fig, O27, u, mid27, w, rad, a1, am, a2 in (
            ('3-27i', (0.15, 0.55), (1.891, 1.724), (2.261, 0.960), (2.091, 0.066),
             1.25, 34.0, 11.0, -14.0),
            # (ii) is the book's inverted Y: the common side is the ray straight
            # UP, the two noncommon sides run down-left and down-right.
            ('3-27ii', (1.15, 1.35), (0.30, 0.25), (1.15, 2.75), (2.05, 0.25),
             0.80, 232.30, 90.0, -50.71),
            ('3-27iii', (1.25, 0.25), (0.05, 1.35), (1.55, 2.05), (2.85, 0.90),
             1.35, 137.48, 80.54, 22.11)):
        check(fig, 'noncommon sides straddle the common side',
              _opp_side(O27, mid27, u, w))
        check(fig, 'arc 1 ends on the common side', par(V(O27, _polar(O27, am, rad)), V(O27, mid27)))
        check(fig, 'arc 1 starts on the outer side', par(V(O27, _polar(O27, a1, rad)), V(O27, u)))
        check(fig, 'arc 2 ends on the outer side', par(V(O27, _polar(O27, a2, rad)), V(O27, w)))

    # 3-28: Definition 3-9 -- supplementary and adjacent: the noncommon sides
    # form a straight angle, so the base is one straight line through O.
    O28 = (2.05, 0.20)
    check('3-28', 'noncommon sides form a straight angle',
          _collinear((0.20, 0.20), (4.15, 0.20), O28))
    check('3-28', 'O between the noncommon sides', _between((0.20, 0.20), (4.15, 0.20), O28))
    check('3-28', 'big arc ends on the common side',
          par(V(O28, _polar(O28, 45.0, 1.20)), V(O28, (3.55, 1.70))))
    check('3-28', 'small arc ends on the common side',
          par(V(O28, _polar(O28, 45.0, 0.67)), V(O28, (3.55, 1.70))))
    check('3-28', 'big arc starts on the base', par(V(O28, _polar(O28, 180.0, 1.20)), (1.0, 0.0)))
    check('3-28', 'common side is off the base line',
          0.0 if par(V(O28, (3.55, 1.70)), (1.0, 0.0)) > 5.0 else 1.0)

    # ================================================== 3-29  (p. 56)
    # "D lies on one side of l, shaded with VERTICAL lines. C lies on one side
    # of m, shaded with HORIZONTAL lines. The points shaded twice fill up the
    # interior of angle COD."  l = AC, m = BD, on the rectangle ABCD.
    A29, B29 = (0.35, 0.35), (0.35, 2.55)
    C29, D29 = (3.95, 2.55), (3.95, 0.35)
    O29 = _intersect(A29, C29, B29, D29)
    check('3-29', 'O on l = AC', _collinear(A29, C29, O29))
    check('3-29', 'O on m = BD', _collinear(B29, D29, O29))
    check('3-29', 'ABCD is a rectangle', perp(V(A29, B29), V(A29, D29))
          + abs(dist(A29, B29) - dist(D29, C29)) + abs(dist(A29, D29) - dist(B29, C29)))
    # vertical rules are clipped to triangle A-D-C: that region is D's side of l
    check('3-29', 'vertical shading is on D-s side of l',
          _same_side(A29, C29, ((A29[0] + D29[0] + C29[0]) / 3, (A29[1] + D29[1] + C29[1]) / 3), D29))
    # horizontal rules are clipped to triangle B-C-D: that region is C's side of m
    check('3-29', 'horizontal shading is on C-s side of m',
          _same_side(B29, D29, ((B29[0] + C29[0] + D29[0]) / 3, (B29[1] + C29[1] + D29[1]) / 3), C29))
    # and the two families really do overlap -- on triangle OCD, the interior
    # of angle COD.  (The first build shaded two disjoint wedges: no overlap.)
    cod = ((O29[0] + C29[0] + D29[0]) / 3, (O29[1] + C29[1] + D29[1]) / 3)
    check('3-29', 'interior of angle COD is shaded twice',
          _in_triangle(A29, D29, C29, cod) + _in_triangle(B29, C29, D29, cod))
    # the rules are generated from two slope constants in the tex; a sample of
    # each family must land exactly on the line that bounds it
    check('3-29', 'vertical rules stop on l = AC',
          _collinear(A29, C29, (1.55, 0.35 + (1.55 - 0.35) * 0.611111)))
    check('3-29', 'horizontal rules start on m = BD',
          _collinear(B29, D29, (0.35 + (2.55 - 1.45) * 1.636364, 1.45)))

    # ================================================== 3-30, 3-31  (pp. 56-57)
    # Definition 3-10: the sides are the rays r1 and r2 ON the lines l1 and l2,
    # so each dashed piece must be the ray exactly opposite its solid one.
    for fig, O30, R1, R2, f1, f2 in (
            ('3-30', (2.30, 1.35), (4.30, 2.55), (4.10, 0.10), -0.90, -1.00),
            ('3-31', (2.05, 1.35), (4.05, 2.45), (3.95, 0.15), -0.85, -0.95)):
        L1 = lerp(O30, R1, f1)
        L2 = lerp(O30, R2, f2)
        check(fig, 'l1 is the ray opposite r1', _opposite_ray(O30, R1, L1))
        check(fig, 'l2 is the ray opposite r2', _opposite_ray(O30, R2, L2))
        check(fig, 'angle O is not a straight angle', _noncollinear(O30, R1, R2))

    # 3-31 also carries the separate segment PQ with A between P and Q
    P31, Q31 = (5.15, 0.60), (7.15, 0.60)
    A31 = lerp(P31, Q31, 0.5)
    check('3-31', 'A between P and Q', _between(P31, Q31, A31))
    check('3-31', 'P, A, Q collinear', _collinear(P31, Q31, A31))

    # ================================================== 3-32  (p. 57)
    # Theorem 3-5: r1' and r2' are the rays from O on l1 and l2 other than
    # r1 and r2, and r is a further ray from O.
    ta32, tb32 = (0.20, 2.45), (4.05, 0.30)     # line l2: r2' .. r2
    ua32, ub32 = (0.25, 0.20), (4.15, 2.35)     # line l1: r1' .. r1
    O32 = _intersect(ta32, tb32, ua32, ub32)
    r32 = (4.20, 1.34)
    check('3-32', 'r1 and r1-prime collinear through O', _collinear(ua32, ub32, O32))
    check('3-32', 'r2 and r2-prime collinear through O', _collinear(ta32, tb32, O32))
    check('3-32', 'r1-prime is the ray opposite r1', _opposite_ray(O32, ub32, ua32))
    check('3-32', 'r2-prime is the ray opposite r2', _opposite_ray(O32, tb32, ta32))
    check('3-32', 'r lies inside angle r1-O-r2',
          _same_side(O32, ub32, r32, tb32) + _same_side(O32, tb32, r32, ub32))
    check('3-32', 'arc 1 runs r1 -> r',
          par(V(O32, _polar(O32, 28.88, 1.40)), V(O32, ub32))
          + par(V(O32, _polar(O32, 1.06, 1.40)), V(O32, r32)))
    check('3-32', 'arc 2 runs r -> r2',
          par(V(O32, _polar(O32, 1.06, 1.40)), V(O32, r32))
          + par(V(O32, _polar(O32, -29.18, 1.40)), V(O32, tb32)))

    # ================================================== 3-33  (p. 57)
    # Theorem 3-6, position Q_3: "segment Q_3 P must contain a point R of l_1
    # and a point S of l_2."  Q_2 lies ON r_2' and Q_4 ON r_1' (Ex. *14 says
    # Q_4, Q_5 are the same cases as Q_2, Q_1).
    L2L, L2R = (0.30, 1.75), (5.75, 1.95)
    L1B, L1T = (1.95, 0.15), (4.15, 3.35)
    O33 = _intersect(L1B, L1T, L2L, L2R)
    P33, Q3 = (5.15, 2.45), (1.85, 1.15)
    R33 = _intersect(Q3, P33, L1B, L1T)
    S33 = _intersect(Q3, P33, L2L, L2R)
    check('3-33', 'O on l1', _collinear(L1B, L1T, O33))
    check('3-33', 'O on l2', _collinear(L2L, L2R, O33))
    check('3-33', 'P is interior to the angle',
          _same_side(L1B, L1T, P33, L2R) + _same_side(L2L, L2R, P33, L1T))
    check('3-33', 'R on l1', _collinear(L1B, L1T, R33))
    check('3-33', 'R on segment Q3-P', _between(Q3, P33, R33))
    check('3-33', 'R is on the ray r1-prime', _on_ray(O33, L1B, R33, L1B, L1T))
    check('3-33', 'S on l2', _collinear(L2L, L2R, S33))
    check('3-33', 'S on segment Q3-P', _between(Q3, P33, S33))
    check('3-33', 'S is on the ray r2 (a point of the angle)',
          _on_ray(O33, L2R, S33, L2L, L2R))
    # the proof reads Q_3 R P and R S P, hence Q_3 S P: R must come BEFORE S
    # walking from Q_3 to P
    check('3-33', 'order along the segment is Q3, R, S, P',
          0.0 if _param(Q3, P33, R33) < _param(Q3, P33, S33) else 1.0)
    Q1_33 = (2.55, 3.05)
    Q2_33 = lerp(L2L, L2R, 0.22)
    Q4_33 = lerp(L1B, L1T, 0.12)
    Q5_33 = (4.30, 0.80)
    check('3-33', 'Q1 beyond l1, on r1 side of l2',
          _opp_side(L1B, L1T, Q1_33, L2R) + _same_side(L2L, L2R, Q1_33, L1T))
    check('3-33', 'Q2 lies ON the ray r2-prime', _on_ray(O33, L2L, Q2_33, L2L, L2R))
    check('3-33', 'Q3 beyond both lines',
          _opp_side(L1B, L1T, Q3, L2R) + _opp_side(L2L, L2R, Q3, L1T))
    check('3-33', 'Q4 lies ON the ray r1-prime', _on_ray(O33, L1B, Q4_33, L1B, L1T))
    check('3-33', 'Q5 on r2 side of l1, beyond l2',
          _same_side(L1B, L1T, Q5_33, L2R) + _opp_side(L2L, L2R, Q5_33, L1T))

    # ================================================== 3-34, 3-35  (p. 58)
    A34, B34, C34 = (0.20, 0.25), (1.75, 2.35), (3.75, 0.25)
    check('3-34', 'A, B, C not all on one line', _noncollinear(A34, B34, C34))

    # Remark after Def. 3-11: P interior, Q exterior, so PQ meets the triangle.
    A35, B35, C35 = (0.20, 0.25), (1.55, 2.35), (3.55, 0.25)
    P35, Q35 = (1.45, 1.05), (3.55, 2.20)
    inside = (_side(A35, B35, P35) * _side(A35, B35, C35) > 0
              and _side(B35, C35, P35) * _side(B35, C35, A35) > 0
              and _side(C35, A35, P35) * _side(C35, A35, B35) > 0)
    outside = not (_side(A35, B35, Q35) * _side(A35, B35, C35) > 0
                   and _side(B35, C35, Q35) * _side(B35, C35, A35) > 0
                   and _side(C35, A35, Q35) * _side(C35, A35, B35) > 0)
    check('3-35', 'P interior to triangle ABC', 0.0 if inside else 1.0)
    check('3-35', 'Q exterior to triangle ABC', 0.0 if outside else 1.0)
    X35 = _intersect(P35, Q35, B35, C35)
    check('3-35', 'PQ crosses side BC', _between(P35, Q35, X35) + _between(B35, C35, X35))

    # ================================================== 3-36, 3-37  (pp. 58-59)
    # Ex. 3-6 #1: an angle at O, a point A on one side, an angle at A whose
    # other side cuts the other side of angle O in B.
    O36, A36 = (0.75, 0.35), (3.85, 0.15)
    Ot36, At36 = (2.55, 2.85), (1.55, 2.75)
    B36 = _intersect(O36, Ot36, A36, At36)
    check('3-36', 'B on the ray from O', _on_ray(O36, Ot36, B36, O36, Ot36))
    check('3-36', 'B on the ray from A', _on_ray(A36, At36, B36, A36, At36))
    # both drawn sides run PAST B, so the crossing shows as a crossing (as in
    # the book) rather than as two segments meeting end to end
    check('3-36', 'B strictly inside the drawn side of angle O', _between(O36, Ot36, B36))
    check('3-36', 'B strictly inside the drawn side of angle A', _between(A36, At36, B36))
    check('3-36', 'dashed piece extends line OA past O',
          _opposite_ray(O36, A36, lerp(O36, A36, -0.23)))
    check('3-36', 'O, A, B form a genuine triangle', _noncollinear(O36, A36, B36))

    # Ex. 3-6 #7: the angle with sides l1 and m1 marked on the lines l and m.
    V37 = (1.35, 0.65)
    l1_37, m1_37 = (3.95, 0.65), (3.35, 2.75)
    check('3-37', 'l is the ray opposite l1', _opposite_ray(V37, l1_37, (0.15, 0.65)))
    check('3-37', 'm is the ray opposite m1', _opposite_ray(V37, m1_37, lerp(V37, m1_37, -0.45)))
    check('3-37', 'arc starts on l1', par(V(V37, _polar(V37, 0.0, 1.10)), V(V37, l1_37)))
    check('3-37', 'arc ends on m1', par(V(V37, _polar(V37, 46.40, 1.10)), V(V37, m1_37)))

    # ================================================== 3-38, 3-39  (p. 59)
    # Ex. *12 (Q_1: same side of l2 as r1, opposite side of l1 from r2) and
    # Ex. *13 (Q_2: ON r2').  Both claim "there is a point R OF r_1 between
    # Q and P" -- so R must land on the ray r1, not merely on the line l1.
    l2L, l2R = (0.30, 1.05), (4.55, 1.25)
    ka, kb = (1.65, 0.15), (3.35, 2.85)
    O38 = _intersect(l2L, l2R, ka, kb)
    P38 = (4.05, 2.10)
    for fig, Q in (('3-38', (1.35, 2.45)), ('3-39', lerp(l2L, l2R, 0.16))):
        R = _intersect(Q, P38, ka, kb)
        check(fig, 'O is where l1 meets l2',
              _collinear(l2L, l2R, O38) + _collinear(ka, kb, O38))
        check(fig, 'P is interior to the angle',
              _same_side(ka, kb, P38, l2R) + _same_side(l2L, l2R, P38, kb))
        check(fig, 'R on l1', _collinear(ka, kb, R))
        check(fig, 'R between Q and P', _between(Q, P38, R))
        check(fig, 'R is a point of the ray r1', _on_ray(O38, kb, R, ka, kb))
    Q1_38 = (1.35, 2.45)          # the point the tex actually draws as Q_1
    check('3-38', 'Q1: same side of l2 as r1', _same_side(l2L, l2R, Q1_38, kb))
    check('3-38', 'Q1: opposite side of l1 from r2', _opp_side(ka, kb, Q1_38, l2R))
    check('3-39', 'Q2 lies ON the ray r2-prime',
          _on_ray(O38, l2L, lerp(l2L, l2R, 0.16), l2L, l2R))
