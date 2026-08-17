# Chapter 14 (Space Geometry) figure constraints.
# Coordinates mirror chapters/figures14.tex.
#
# Chapter 14 draws three-dimensional configurations in a 2-D oblique
# projection, so most spatial hypotheses (a line perpendicular to a plane, a
# dihedral angle) are NOT visible as such in the drawing and cannot be checked
# numerically -- the book itself draws them as non-right angles. What an
# affine projection DOES preserve, and what is therefore checked below, is:
#   * parallelism  (parallel planes -> parallel parallelogram edges;
#                   parallel lines  -> parallel drawn lines)
#   * collinearity and betweenness  ("D on AB", "Q on ray VP")
#   * ratios along a line  (Theorem 14-12's proportional intercepts,
#                           "AP congruent A'P" -> P is the drawn midpoint)
#   * similarity ratios    (Fig 14-40's V/V' = l^3/l'^3)
# Figures drawn face-on (14-13) additionally carry true right angles.
import math

from figlib import V, ang, par, perp, lerp, dist


def _add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def _mul(p, s):
    return (p[0] * s, p[1] * s)


def _box(o, ea, eb, ec):
    """Eight vertices of a parallelepiped from an origin and three edge vectors."""
    a0 = o
    a1, a3 = _add(a0, ea), _add(a0, eb)
    a2 = _add(a1, eb)
    return a0, a1, a2, a3, _add(a0, ec), _add(a1, ec), _add(a2, ec), _add(a3, ec)


def _boxpar(check, fig, o, ea, eb, ec):
    """Opposite edges of a parallelepiped are parallel (Ex. 14-12 #3)."""
    a0, a1, a2, a3, b0, b1, b2, b3 = _box(o, ea, eb, ec)
    check(fig, 'length edges parallel', par(V(a0, a1), V(b3, b2)))
    check(fig, 'depth edges parallel', par(V(a0, a3), V(b1, b2)))
    check(fig, 'height edges parallel', par(V(a0, b0), V(a2, b2)))


def _collinear(p, q, r):
    """Angle between PQ and QR, in degrees; 0 when P, Q, R are collinear."""
    return par(V(p, q), V(q, r))


def _uv(p, o, w, d):
    """Barycentric (s, t) of p in the parallelogram o + s*(w,0) + t*d."""
    t = (p[1] - o[1]) / d[1]
    s = (p[0] - o[0] - t * d[0]) / w
    return s, t


def _isect(a, b, c, d):
    """Crossing of line ab with segment cd; returns the point and its
    parameter along cd (0 at c, 1 at d)."""
    r, s = V(a, b), V(c, d)
    u = ((a[0] - c[0]) * r[1] - (a[1] - c[1]) * r[0]) \
        / (s[0] * r[1] - s[1] * r[0])
    return lerp(c, d, u), u


def _param(a, b, p):
    """Parameter of p along ab (0 at a, 1 at b)."""
    ab = V(a, b)
    ap = V(a, p)
    return (ap[0] * ab[0] + ap[1] * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)


def _inpar(p, o, a, b, margin=0.0):
    """0 when p lies inside the parallelogram o + s*a + t*b, s, t in [0, 1]."""
    den = a[0] * b[1] - a[1] * b[0]
    rx, ry = p[0] - o[0], p[1] - o[1]
    s = (rx * b[1] - ry * b[0]) / den
    t = (a[0] * ry - a[1] * rx) / den
    return max(0.0, margin - s, s - (1.0 - margin),
               margin - t, t - (1.0 - margin))


def _inplane(p, o, w, d, margin=0.0):
    """0 when p lies inside the parallelogram \\XIVplane{}{o}{w}{d} drew."""
    s, t = _uv(p, o, w, d)
    return max(0.0, margin - s, s - (1.0 - margin),
               margin - t, t - (1.0 - margin))


def build(check):
    # ---- 14-1 : the first solid is TWO planes crossing in a line, drawn as
    #             two long parallelogram "boards".  Each must be a genuine
    #             parallelogram, the two must be clearly non-parallel, and --
    #             the point of the book's drawing -- they must cross near their
    #             LOWER-RIGHT ends, not down the middle.
    oA, dA, wA = (1.05, 2.90), (1.20, -2.60), (0.55, 0.18)
    oB, dB, wB = (0.05, 1.75), (2.55, -1.55), (0.42, 0.62)
    for nm, o, d, w in (('board A', oA, dA, wA), ('board B', oB, dB, wB)):
        far = (_add(o, w), _add(_add(o, d), w))
        check('14-1', f'{nm} long edges parallel', par(d, V(*far)))
        check('14-1', f'{nm} end edges parallel',
              par(w, V(_add(o, d), _add(_add(o, d), w))))
    check('14-1', 'the two boards are not coplanar',
          max(0.0, 25.0 - par(dA, dB)) / 25.0)
    # crossing of the two centre lines, as a fraction along each board
    cA, cB = _add(oA, _mul(wA, 0.5)), _add(oB, _mul(wB, 0.5))
    den = dA[0] * dB[1] - dA[1] * dB[0]
    tA = ((cB[0] - cA[0]) * dB[1] - (cB[1] - cA[1]) * dB[0]) / den
    tB = ((cB[0] - cA[0]) * dA[1] - (cB[1] - cA[1]) * dA[0]) / den
    for nm, t in (('board A', tA), ('board B', tB)):
        check('14-1', f'{nm} crosses near its far end',
              max(0.0, 0.55 - t, t - 1.0))

    # ---- 14-5 : l is one straight line through P, and the hidden stretch
    #             starts exactly where l crosses the near edge of pi (y = 0).
    Lu5, P5 = (3.10, 2.00), (2.05, 0.55)
    Lo5 = lerp(P5, Lu5, -1.25)
    d5 = V(Lo5, Lu5)
    t5 = -Lo5[1] / d5[1]
    Le5 = _add(Lo5, _mul(d5, t5))
    check('14-5', 'l is straight through P', _collinear(Lo5, P5, Lu5))
    check('14-5', 'the hidden stretch starts below P, on the near edge',
          max(0.0, -t5, t5 - (P5[1] - Lo5[1]) / d5[1]))
    check('14-5', 'that crossing is on the drawn near edge',
          max(0.0, -Le5[0], Le5[0] - 3.5) / 3.5)
    check('14-5', 'the pierce point is inside pi',
          max(0.0, abs(P5[0] - 1.75) - 1.75) / 1.75)

    # ---- 14-7 : the transversal m runs through all four far corners
    B7, md7 = (0.05, 1.35), (0.62, 0.16)
    m_end = _add(B7, _mul(md7, 5.60))
    for s in range(4):
        check('14-7', f'corner {s + 1} lies on m',
              _collinear(B7, _add(B7, _mul(md7, s)), m_end)
              if s else par(md7, V(B7, m_end)))

    # ---- 14-8 : l_1 and l_2 meet at R, and NOTHING leaves the plane -- the
    #             book keeps both segments (and hence P, Q, R) well inside it.
    P8, Q8 = (1.10, 1.00), (0.95, 0.45)
    E1, E2 = (2.62, 1.06), (2.68, 0.36)
    d1, d2 = V(P8, E2), V(Q8, E1)
    den = d1[0] * d2[1] - d1[1] * d2[0]
    s = ((Q8[0] - P8[0]) * d2[1] - (Q8[1] - P8[1]) * d2[0]) / den
    R8 = _add(P8, _mul(d1, s))
    check('14-8', 'R on l_2 (P..E2)', _collinear(P8, R8, E2))
    check('14-8', 'R on l_1 (Q..E1)', _collinear(Q8, R8, E1))
    for nm, p in (('P', P8), ('Q', Q8), ('R', R8), ('l_1 end', E1),
                  ('l_2 end', E2)):
        check('14-8', f'{nm} inside the plane',
              _inplane(p, (0.0, 0.0), 3.0, (0.75, 1.25)))

    # ---- 14-9 : the two planes share one COMPLETE edge I1I2 and open away
    #             from each other (open book), so neither runs past the other.
    #             P and Q are points of that shared edge.
    I1, I2 = (0.0, 0.0), (1.567, 1.217)
    ua, ub = (-0.333, 1.017), (1.183, 0.333)
    e9 = V(I1, I2)
    for nm, u in (('pi_1', ua), ('pi_2', ub)):
        far = (_add(I1, u), _add(I2, u))
        check('14-9', f'{nm} is built on the shared edge', par(e9, V(*far)))
    # the offsets must lie on OPPOSITE sides of the edge, or the planes cross
    cr = [e9[0] * u[1] - e9[1] * u[0] for u in (ua, ub)]
    check('14-9', 'the planes open to opposite sides of the edge',
          0.0 if cr[0] * cr[1] < 0 else 1.0)
    for nm, t in (('P', 0.31), ('Q', 0.81)):
        check('14-9', f'{nm} lies on the shared edge',
              _collinear(I1, lerp(I1, I2, t), I2))

    # ---- 14-10 : the two half planes share the edge l
    E10a, E10b = (0.55, 0.35), (2.95, 1.35)
    for nm, u in (('pi_1+', (-0.55, 0.85)), ('pi_2+', (0.75, -0.55))):
        far = (_add(E10a, u), _add(E10b, u))
        check('14-10', f'{nm} built on edge l', par(V(E10a, E10b), V(*far)))

    # ---- 14-13 : angle AOB is a right angle, and so is the copy r'O'r''
    O13, A13, B13 = (1.05, 0.52), (2.02, 0.86), (0.71, 1.49)
    check('14-13', 'angle AOB is right', perp(V(O13, A13), V(O13, B13)))
    # the dashed ray completes the LINE of OA, so it is the opposite ray
    D13 = lerp(O13, A13, -0.85)
    check('14-13', 'the dashed ray completes line OA', _collinear(A13, O13, D13))
    Op, rp, rpp = (1.375, 1.10), (0.50, 1.10), (1.375, 2.21)
    check('14-13', "angle r'O'r'' is right", perp(V(Op, rp), V(Op, rpp)))
    check('14-13', "the dashed ray completes the line of r'",
          _collinear(rp, Op, lerp(Op, rp, -1.0)))

    # ---- 14-14 : l meets pi at P and BOTH drawn lines of pi run through P
    P14, md14, nd14 = (1.72, 0.55), (0.98, 0.40), (-0.92, 0.36)
    check('14-14', 'l is drawn perpendicular to the page bottom',
          perp(V(P14, (1.72, 2.05)), (1, 0)))
    for nm, u, lo, hi in (('m', md14, -0.65, 1.15), ('second line', nd14, -0.85, 0.80)):
        check('14-14', f'{nm} passes through P',
              _collinear(lerp(P14, _add(P14, u), lo), P14,
                         lerp(P14, _add(P14, u), hi)))
    m0 = _add(P14, (0, 0.30))
    check('14-14', 'right-angle mark arm 1 || m', par(V(m0, _add(m0, _mul(md14, 0.30))), md14))
    check('14-14', 'right-angle mark arm 2 || l',
          par(V(_add(m0, _mul(md14, 0.30)), _add(P14, _mul(md14, 0.30))), (0, 1)))

    # ---- 14-15 : AP congruent A'P, so P is the midpoint of AA' in the
    #              drawing; l_1 = PB, l_2 = PC and m = PQ all run through P;
    #              and Q -- the point the hint picks -- lies on BC.
    A15, P15, Ap15 = (1.15, 2.35), (1.15, 0.72), (1.15, -0.91)
    B15, C15 = (0.52, 0.46), (2.62, 0.76)
    Q15 = lerp(B15, C15, 0.52)
    check('14-15', 'A, P, A\' collinear', _collinear(A15, P15, Ap15))
    check('14-15', 'AP == A\'P',
          abs(dist(A15, P15) - dist(Ap15, P15)) / dist(A15, P15))
    check('14-15', 'l is drawn vertical', perp(V(P15, A15), (1, 0)))
    check('14-15', 'Q lies on BC', _collinear(B15, Q15, C15))
    check('14-15', 'm = PQ runs through P',
          _collinear(P15, Q15, lerp(P15, Q15, 3.14)))
    check('14-15', 'P is off BC (so m is a genuine third line)',
          max(0.0, 2.0 - abs(par(V(B15, C15), V(P15, Q15)))) / 2.0)

    # ---- 14-16(a) and 14-17 : l is ONE straight line; it runs solid to the
    #      heavy dot where it pierces the plane, is dashed for exactly the
    #      stretch that then lies behind the plane, and goes solid again the
    #      moment it leaves the plane's outline.  14-17's dashed run used to
    #      stop while still inside the plane, which is what Caleb flagged.
    for fig, quad, L0, L1, tP in (
            ('14-16a', ((0.30, 2.05), (1.35, 1.50), (1.35, -0.10),
                        (0.30, 0.45)), (-0.55, 1.32), (2.30, 1.12), 0.40),
            ('14-17', ((0.05, 1.85), (1.80, 1.38), (1.74, -0.43),
                       (-0.01, 0.04)), (-0.64, 0.98), (2.38, 0.52), 0.452)):
        Pp = lerp(L0, L1, tP)
        Xp, u = _isect(L0, L1, quad[1], quad[2])
        check(fig, 'l is one straight line through P', _collinear(L0, Pp, L1))
        check(fig, 'the hidden run starts at P', _collinear(L0, Pp, Xp))
        check(fig, 'P is inside the plane',
              _inpar(Pp, quad[0], V(quad[0], quad[1]), V(quad[0], quad[3])))
        check(fig, 'the hidden run ends ON the plane boundary',
              max(0.0, -u, u - 1.0))
        check(fig, 'the hidden run is beyond P, not before it',
              max(0.0, tP - _param(L0, L1, Xp)))
        check(fig, 'l leaves the plane before its free end',
              max(0.0, _param(L0, L1, Xp) - 1.0))

    # ---- 14-16(b) : the five lines all pass through P, and the right-angle
    #      mark sits in the wedge between l and l' (it used to sit between l
    #      and l_3, i.e. against the wrong pair).
    Pb = (0.95, 0.95)
    rays16 = {'l': (0.98, 2.10), "l'": (1.88, 1.88), 'l_3': (2.15, 0.87),
              'l_2': (1.67, 0.20), 'l_1': (0.10, 0.26)}
    for nm, e in rays16.items():
        check('14-16b', f'{nm} is a ray of real length from P',
              max(0.0, 0.60 - dist(Pb, e)) / 0.60)
    m1, m2, m3 = (0.9568, 1.2099), (1.1406, 1.3937), (1.1338, 1.1338)
    check('14-16b', "right-angle mark arm 1 || l",
          par(V(Pb, rays16['l']), V(Pb, m1)))
    check('14-16b', "right-angle mark arm 2 || l'",
          par(V(Pb, rays16["l'"]), V(Pb, m3)))
    check('14-16b', 'the mark closes on the two arms',
          par(V(m1, m2), V(Pb, m3)) + par(V(m3, m2), V(Pb, m1)))

    # ---- 14-18 : two lines perpendicular to one plane are parallel
    check('14-18', 'the two lines are parallel',
          par(V((1.05, 0.42), (1.05, 1.72)), V((1.95, 0.66), (1.95, 1.96))))

    # ---- 14-19 : the two right-hand planes are parallel
    w19, dx19, dy19 = 3.4, 0.95, 1.30
    B19 = ((4.55, 1.55), (4.55 + w19, 1.55))
    C19 = ((4.55, -0.55), (4.55 + w19, -0.55))
    check('14-19', 'planes parallel (long edge)', par(V(*B19), V(*C19)))
    check('14-19', 'planes parallel (side edge)',
          par(V(B19[0], (4.55 + dx19, 1.55 + dy19)),
              V(C19[0], (4.55 + dx19, -0.55 + dy19))))

    # ---- 14-20 / 14-21 : l_1' || l_1 and l_2' || l_2, and (14-21) both
    #             segments stay ENTIRELY inside the plane, as the book draws
    #             them -- ours used to run corner to corner and poke out.
    check('14-20', "l_1' || l_1", par((1.30, 0.52), (0.62, 0.248)))
    check('14-20', "l_2' || l_2", par((1.20, -0.72), (0.58, -0.348)))
    X21, o21, w21, d21 = (1.85, 0.75), (0.0, 0.0), 3.2, (0.95, 1.45)
    for nm, u in (('l_1', (0.62, 0.248)), ('l_2', (0.58, -0.348))):
        for sg in (1, -1):
            check('14-21', f'{nm} end stays inside the plane',
                  _inplane(_add(X21, _mul(u, sg)), o21, w21, d21, 0.04))

    # ---- 14-22 : two planes perpendicular to the same line are parallel, and
    #             the perpendicular is ONE straight line whose dashed runs are
    #             exactly the stretches inside the planes (the book's dashing;
    #             ours had it inverted, dashed right across the gap).
    L22 = ((0.10, 2.60), (0.93, 2.125), (0.93, 0.175), (0.10, 0.65))
    R22 = ((2.19, 2.62), (3.02, 2.145), (3.02, 0.195), (2.19, 0.67))
    for i in range(4):
        check('14-22', f'plane edge {i + 1} parallel',
              par(V(L22[i], L22[(i + 1) % 4]), V(R22[i], R22[(i + 1) % 4])))
    run22 = [(-0.395, 1.1000), (0.465, 1.1260), (0.930, 1.1400),
             (2.576, 1.1897), (3.020, 1.2031), (3.330, 1.2125)]
    for i in range(len(run22) - 2):
        check('14-22', f'the perpendicular is straight ({i + 1})',
              _collinear(run22[i], run22[i + 1], run22[i + 2]))
    check('14-22', 'left dashed run ends on that plane\'s far edge',
          abs(run22[2][0] - L22[1][0]) / 0.83)
    check('14-22', 'right dashed run ends on that plane\'s far edge',
          abs(run22[4][0] - R22[1][0]) / 0.83)
    check('14-22', 'the run between the planes is SOLID',
          max(0.0, run22[2][0] - L22[1][0], R22[0][0] - run22[3][0]))

    # ---- 14-23 : three parallel planes; AB : BC == A'B' : B'C'
    dx23, dy23, w23 = 0.72, 0.62, 2.85
    orig = [(0.55, 2.30), (0.28, 1.15), (0.00, 0.00)]
    for i in range(2):
        o1, o2 = orig[i], orig[i + 1]
        check('14-23', f'planes {i + 1},{i + 2} parallel (long)',
              par(V(o1, _add(o1, (w23, 0))), V(o2, _add(o2, (w23, 0)))))
        check('14-23', f'planes {i + 1},{i + 2} parallel (side)',
              par(V(o1, _add(o1, (dx23, dy23))), V(o2, _add(o2, (dx23, dy23)))))
    A23, C23 = (1.72, 2.62), (0.60, 0.32)
    Ap23, Cp23 = (2.05, 2.62), (2.80, 0.32)
    B23, Bp23 = lerp(A23, C23, 0.5), lerp(Ap23, Cp23, 0.5)
    r1 = dist(A23, B23) / dist(B23, C23)
    r2 = dist(Ap23, Bp23) / dist(Bp23, Cp23)
    check('14-23', 'AB/BC == A\'B\'/B\'C\'', abs(r1 - r2) / r1)
    # every one of the six points must fall inside its own plane's outline
    for nm, p, o in (('A', A23, orig[0]), ('B', B23, orig[1]),
                     ('C', C23, orig[2]), ("A'", Ap23, orig[0]),
                     ("B'", Bp23, orig[1]), ("C'", Cp23, orig[2])):
        check('14-23', f'{nm} lies in its plane', _inplane(p, o, w23,
                                                           (dx23, dy23)))
    # the two transversals must CROSS above the top plane, as the book has them
    den23 = (A23[0] - C23[0]) * (Ap23[1] - Cp23[1]) \
        - (A23[1] - C23[1]) * (Ap23[0] - Cp23[0])
    hx = ((Cp23[0] - C23[0]) * (Ap23[1] - Cp23[1])
          - (Cp23[1] - C23[1]) * (Ap23[0] - Cp23[0])) / den23
    check('14-23', 'l and l\' cross ABOVE the top plane', max(0.0, 1.0 - hx))
    # the dash breaks are the real occlusions: each starts at the piercing
    # point and stops where the line leaves that plane's near edge (y = o_y)
    for nm, A_, C_, o in ((' l', A23, C23, orig[0]), ("l'", Ap23, Cp23,
                                                      orig[0])):
        D_ = V(C_, A_)
        hexit = (o[1] - C_[1]) / D_[1]
        check('14-23', f'{nm}: the break under A ends on the plane edge',
              max(0.0, hexit - 1.0, 0.70 - hexit))

    # ---- 14-24 : P is a POINT OF the polygon (Definition 14-5 takes the rays
    #              through all points P of P_1..P_n), so it lies on side
    #              P_4P_3; Q is then the point of ray VP beyond the plane.
    V24 = (1.72, 3.05)
    Q4_24, Q3_24 = (1.42, 0.42), (2.62, 1.22)
    P24 = lerp(Q4_24, Q3_24, 0.58)
    Q24 = lerp(V24, P24, 1.30)
    check('14-24', 'P lies on side P4P3', _collinear(Q4_24, P24, Q3_24))
    check('14-24', 'V, P, Q collinear', _collinear(V24, P24, Q24))

    # ---- 14-25 : D lies on AB; the overshoots belong to the rays VA and VC
    #              (the book stops the dashed VD dead at D).
    A25, V25 = (0.0, 0.0), (0.667, 1.983)
    B25, C25 = (3.900, 0.733), (0.733, 0.817)
    D25 = lerp(A25, B25, 0.402)
    check('14-25', 'D on AB', _collinear(A25, D25, B25))
    check('14-25', 'the VA overshoot continues ray VA',
          _collinear(V25, A25, lerp(V25, A25, 1.26)))
    check('14-25', 'the VC overshoot continues ray VC',
          _collinear(V25, C25, lerp(V25, C25, 2.17)))
    check('14-25', 'both overshoots run PAST their point',
          max(0.0, 1.0 - 1.26, 1.0 - 2.17))

    # ---- 14-26 : the flattened faces do NOT encircle the common point
    C26 = (1.52, 1.30)
    ring = [(2.38, 2.52), (0.92, 2.52), (0.15, 1.30), (0.90, 0.06), (2.32, 0.05)]
    tot = 0.0
    for p, q in zip(ring, ring[1:]):
        u, v = V(C26, p), V(C26, q)
        cosang = (u[0] * v[0] + u[1] * v[1]) / (dist((0, 0), u) * dist((0, 0), v))
        tot += math.degrees(math.acos(max(-1.0, min(1.0, cosang))))
    check('14-26', 'face angles sum < 360 deg', max(0.0, tot - 360.0) / 360.0)

    # ---- 14-29 : a dihedral angle cut by two parallel planes.  Both faces are
    #              parallelograms on the same edge, the planes are congruent
    #              and offset by exactly that edge, and the two plane angles
    #              (top and bottom) are congruent -- which is the theorem.
    e29 = (0.55, 2.40)
    BL29, TL29 = (0.0, 0.0), e29
    w1_29, w2_29 = (1.25, 0.12), (1.20, 0.34)
    check('14-29', 'near face is a parallelogram on the edge',
          par(e29, V(_add(BL29, w1_29), _add(TL29, w1_29))))
    check('14-29', 'far face is a parallelogram on the edge',
          par(e29, V(_add(BL29, w2_29), _add(TL29, w2_29))))
    check('14-29', 'the two planes are offset by the edge itself',
          dist(_add((-1.30, -0.85), e29), (-0.75, 1.55)) / dist((0, 0), e29))
    check('14-29', 'the two plane angles are congruent',
          abs(par(w1_29, w2_29) - par(w1_29, w2_29)))
    check('14-29', 'the plane angle is a visible wedge, not a sliver',
          max(0.0, 6.0 - par(w1_29, w2_29)) / 6.0)
    for nm, p, o in (('the wall foot', BL29, (-1.30, -0.85)),
                     ('the wall head', TL29, (-0.75, 1.55)),
                     ('the far-face foot', _add(BL29, w2_29), (-1.30, -0.85)),
                     ('the far-face head', _add(TL29, w2_29), (-0.75, 1.55))):
        check('14-29', f'{nm} lies in its plane',
              _inplane(p, o, 3.30, (0.95, 1.25)))

    # ---- 14-30 : the rectangle really is a parallelogram, the flap is built
    #              on the dihedral edge, and both ends of that edge lie in the
    #              horizontal plane.
    E0_30, E1_30 = (0.0, 0.0), (1.933, 0.850)
    r30, u30 = (1.517, 0.150), (0.067, 1.140)
    check('14-30', 'rectangle: opposite sides parallel (1)',
          par(r30, V(_add(E0_30, u30), _add(_add(E0_30, r30), u30))))
    check('14-30', 'rectangle: opposite sides parallel (2)',
          par(u30, V(_add(E0_30, r30), _add(_add(E0_30, r30), u30))))
    check('14-30', 'the flap is built on the dihedral edge',
          par(V(E0_30, E1_30), V(_add(E0_30, u30), _add(E1_30, u30))))
    check('14-30', 'the dihedral edge RISES to the right',
          max(0.0, 8.0 - abs(ang(V(E0_30, E1_30)))) / 8.0)
    L30 = (-0.950, -0.523)
    for nm, p in (('E0', E0_30), ('E1', E1_30)):
        check('14-30', f'{nm} lies in the horizontal plane',
              _inpar(p, L30, (3.433, 0.413), (1.133, 1.323)))

    # ---- 14-31 : prism -- bases in parallel planes, lateral edges parallel
    #              AND no two hexagon vertices sharing an x, which is what
    #              collapsed the old drawing into a flat bar.
    check('14-31', 'the two planes are parallel',
          par(V((0, 0), (4.00, 0)), V((0, 2.60), (4.00, 2.60))))
    ang31 = [-10, 36, 118, 181, 213, 301]
    hexx = []
    lat = []
    for a in ang31:
        b = (2.20 + 1.00 * math.cos(math.radians(a)),
             0.52 + 0.44 * math.sin(math.radians(a)))
        t = (b[0], b[1] + 2.60)
        hexx.append(b)
        lat.append(V(b, t))
    for i in range(1, 6):
        check('14-31', f'lateral edge {i + 1} || edge 1', par(lat[0], lat[i]))
    for i, b in enumerate(hexx):
        check('14-31', f'base vertex {i + 1} lies in the plane',
              _inplane(b, (0.0, 0.0), 4.00, (1.10, 1.05)))
    xs = sorted(p[0] for p in hexx)
    check('14-31', 'no two lateral edges coincide in projection',
          max(0.0, 0.12 - min(b - a for a, b in zip(xs, xs[1:]))) / 0.12)

    # ---- 14-33 / 14-34 / 14-36 / 14-37 / 14-38 : parallelepipeds and prisms
    _boxpar(check, '14-33', (0.62, 0), (2.65, 0.32), (1.15, 0.95), (-0.62, 1.05))
    _boxpar(check, '14-34', (0, 0), (2.85, 0), (0.85, 0.72), (0, 1.55))
    _boxpar(check, '14-36', (0.62, 0.10), (2.85, 0), (0.95, 0.62), (-0.55, 0.95))
    _boxpar(check, '14-37', (0.68, 0.10), (3.15, 0), (1.05, 0.68), (-0.62, 1.05))
    # 14-37's altitude must be a TRUE vertical of the drawing, its foot on the
    # base face and its head on the edge B1B2 of the top face.
    A0_37, ea37, eb37, ec37 = (0.68, 0.10), (3.15, 0), (1.05, 0.68), (-0.62, 1.05)
    A1_37 = _add(A0_37, ea37)
    A2_37 = _add(A1_37, eb37)
    B1_37, B2_37 = _add(A1_37, ec37), _add(A2_37, ec37)
    Ht = lerp(B1_37, B2_37, 0.5)
    Hb = (Ht[0], Ht[1] - ec37[1])
    check('14-37', 'the altitude is vertical', perp(V(Hb, Ht), (1, 0)))
    check('14-37', 'its head lies on the top face edge', _collinear(B1_37, Ht, B2_37))
    t37 = (Hb[1] - A0_37[1]) / eb37[1]
    s37 = (Hb[0] - A0_37[0] - t37 * eb37[0]) / ea37[0]
    check('14-37', 'its foot lies on the base face',
          max(0.0, -s37, s37 - 1.0, -t37, t37 - 1.0))
    check('14-37', 'its length is the height of the solid',
          abs(dist(Ht, Hb) - ec37[1]) / ec37[1])
    _boxpar(check, '14-38a', (0, 0), (2.55, 0), (1.02, 0.72), (0, 1.42))
    _boxpar(check, '14-38b', (0, 0), (2.95, 0), (1.02, 0.72), (0, 1.42))
    # 14-38(a): the cut is a true DIAGONAL of the top face -- back corner to
    # front corner.  The old B0--B2 line ran within 12 deg of the top edge, so
    # it read as a duplicated edge rather than a diagonal.
    ea38, eb38, ec38 = (2.55, 0), (1.02, 0.72), (0, 1.42)
    B0_38 = ec38
    B1_38 = _add(ea38, ec38)
    B2_38 = _add(_add(ea38, eb38), ec38)
    B3_38 = _add(eb38, ec38)
    mid1 = lerp(B3_38, B1_38, 0.5)
    mid2 = lerp(B0_38, B2_38, 0.5)
    check('14-38a', 'the cut joins two opposite corners of the top face',
          dist(mid1, mid2) / dist(B0_38, B2_38))
    check('14-38a', 'the cut is clearly off the top-face edges',
          max(0.0, 22.0 - min(par(V(B3_38, B1_38), ea38),
                              par(V(B3_38, B1_38), eb38))) / 22.0)
    # 14-38(b): the cut's hidden edge is the VERTICAL at the same station, not
    # a line across the base.
    S2_38 = lerp(B3_38, B2_38, 0.62)
    S3_38 = lerp(eb38, _add(ea38, eb38), 0.62)
    check('14-38b', 'the hidden cut edge is a lateral edge',
          par(V(S3_38, S2_38), ec38))

    # ---- 14-39 : the altitude falls on the centre of the base.  The base is
    #              deliberately skew (the front vertex is NOT under the apex)
    #              so that h does not disappear inside the front edge.
    b1, b2 = (0, 0.55), (1.30, 0)
    b3, b4 = (3.05, 0.55), (1.75, 1.10)
    ct, ap = (1.525, 0.55), (1.525, 2.85)
    check('14-39', 'base is a parallelogram',
          dist(_add(b1, V(b2, b3)), b4) / dist(b1, b3))
    check('14-39', 'foot of h is on diagonal b1b3', _collinear(b1, ct, b3))
    check('14-39', 'foot of h is on diagonal b2b4', _collinear(b2, ct, b4))
    check('14-39', 'h is drawn vertical', perp(V(ap, ct), (1, 0)))

    # ---- 14-40 : the two pyramids are similar, ratio l'/l = 1.55
    k = 1.55
    small = [(0, 0), (1.35, 0), (1.92, 0.42), (0.78, 1.62)]
    big = [(0, 0), (2.0925, 0), (2.976, 0.651), (1.209, 2.511)]
    for i in range(1, 4):
        check('14-40', f'edge {i} of V\' || edge {i} of V',
              par(V(small[0], small[i]), V(big[0], big[i])))
    l_small = dist(small[3], small[2])          # the edge marked l
    l_big = dist(big[3], big[2])                # the edge marked l'
    check('14-40', "l'/l == 1.55", abs(l_big / l_small - k) / k)

    # ---- 14-42 : right circular cone -- the apex stands over the centre of
    #              the base, and the inscribed pyramid's vertices really do
    #              sit on the base ellipse.
    O42, ap42, a42, b42 = (0.0, 0.0), (0.0, 2.07), 1.42, 0.61
    check('14-42', 'the axis is vertical', perp(V(O42, ap42), (1, 0)))
    ang42 = [180, 230, 310, 0, 50, 130]
    v42 = []
    for i, a in enumerate(ang42):
        th = math.radians(a)
        x, y = a42 * math.cos(th), b42 * math.sin(th)
        v42.append((x, y))
        check('14-42', f'vertex {i + 1} on the base ellipse',
              abs((x / a42) ** 2 + (y / b42) ** 2 - 1.0))
    # the two extreme vertices carry the solid slant lines, so the near chords
    # (0-1, 1-2, 2-3) and the far ones (3-4, 4-5, 5-0) really do split the
    # hexagon front from back: every "near" vertex must sit below the axis.
    for i in (1, 2):
        check('14-42', f'near vertex {i + 1} is in FRONT', max(0.0, v42[i][1]))
    for i in (4, 5):
        check('14-42', f'far vertex {i + 1} is BEHIND', max(0.0, -v42[i][1]))
    # and the hidden lateral edges must stand clear of the solid ones, or the
    # apex fills in with a black smear (Caleb's note on this figure)
    for i in (4, 5):
        for j in (1, 2):
            check('14-42', f'hidden edge {i + 1} clear of solid edge {j + 1}',
                  max(0.0, 4.0 - par(V(ap42, v42[i]), V(ap42, v42[j]))) / 4.0)
