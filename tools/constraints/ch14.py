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


def build(check):
    # ---- 14-1 : the first solid is TWO planes meeting in a line.  Both
    #             parallelograms must be built on that common line, and their
    #             offset directions must differ enough to read as two planes.
    L1, L2 = (0.30, 2.10), (2.00, 0.10)
    u1, u2 = (-0.68, -0.38), (0.30, 0.72)
    for nm, u in (('plane 1', u1), ('plane 2', u2)):
        near = (_add(L1, _mul(u, -0.10)), _add(L2, _mul(u, -0.10)))
        far = (_add(L1, u), _add(L2, u))
        check('14-1', f'{nm} built on the common line', par(V(L1, L2), V(*near)))
        check('14-1', f'{nm} far edge parallel to it', par(V(L1, L2), V(*far)))
    check('14-1', 'the two planes are not coplanar',
          max(0.0, 30.0 - par(u1, u2)) / 30.0)

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

    # ---- 14-8 : l_1 and l_2 meet at R
    P8, Q8 = (0.75, 0.88), (0.55, 0.36)
    E1, E2 = (2.60, 0.98), (2.65, 0.28)
    d1, d2 = V(P8, E2), V(Q8, E1)
    den = d1[0] * d2[1] - d1[1] * d2[0]
    s = ((Q8[0] - P8[0]) * d2[1] - (Q8[1] - P8[1]) * d2[0]) / den
    R8 = _add(P8, _mul(d1, s))
    check('14-8', 'R on l_2 (P..E2)', _collinear(P8, R8, E2))
    check('14-8', 'R on l_1 (Q..E1)', _collinear(Q8, R8, E1))

    # ---- 14-9 : PQ is the line common to both planes, so it is parallel to
    #             the long edge of each parallelogram (built on PQ).
    I1, I2 = (1.05, 0.42), (2.62, 0.86)
    ua, ub = (-0.72, 1.02), (0.62, 0.95)
    for nm, u in (('pi_1', ua), ('pi_2', ub)):
        top = (_add(I1, _mul(u, 1.15)), _add(I2, _mul(u, 1.15)))
        check('14-9', f'PQ lies in {nm}', par(V(I1, I2), V(*top)))

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

    # ---- 14-20 / 14-21 : l_1' || l_1 and l_2' || l_2
    check('14-20', "l_1' || l_1", par((1.30, 0.52), (1.05, 0.42)))
    check('14-20', "l_2' || l_2", par((1.20, -0.72), (1.10, -0.66)))

    # ---- 14-22 : two planes perpendicular to the same line are parallel
    L22 = ((0.35, 0.20), (0.95, 0.66), (0.95, 2.32), (0.35, 1.86))
    R22 = tuple(_add(p, (2.0, 0.0)) for p in L22)
    for i in range(4):
        check('14-22', f'plane edge {i + 1} parallel',
              par(V(L22[i], L22[(i + 1) % 4]), V(R22[i], R22[(i + 1) % 4])))

    # ---- 14-23 : three parallel planes; AB : BC == A'B' : B'C'
    dx23, dy23, w23 = 0.72, 0.62, 2.60
    orig = [(0.55, 2.30), (0.28, 1.15), (0.00, 0.00)]
    for i in range(2):
        o1, o2 = orig[i], orig[i + 1]
        check('14-23', f'planes {i + 1},{i + 2} parallel (long)',
              par(V(o1, _add(o1, (w23, 0))), V(o2, _add(o2, (w23, 0)))))
        check('14-23', f'planes {i + 1},{i + 2} parallel (side)',
              par(V(o1, _add(o1, (dx23, dy23))), V(o2, _add(o2, (dx23, dy23)))))
    A23, C23 = (1.62, 2.62), (0.92, 0.32)
    Ap23, Cp23 = (2.05, 2.58), (2.72, 0.28)
    B23, Bp23 = lerp(A23, C23, 0.52), lerp(Ap23, Cp23, 0.52)
    r1 = dist(A23, B23) / dist(B23, C23)
    r2 = dist(Ap23, Bp23) / dist(Bp23, Cp23)
    check('14-23', 'AB/BC == A\'B\'/B\'C\'', abs(r1 - r2) / r1)

    # ---- 14-24 : P is a POINT OF the polygon (Definition 14-5 takes the rays
    #              through all points P of P_1..P_n), so it lies on side
    #              P_4P_3; Q is then the point of ray VP beyond the plane.
    V24 = (1.72, 3.05)
    Q4_24, Q3_24 = (1.42, 0.42), (2.62, 1.22)
    P24 = lerp(Q4_24, Q3_24, 0.58)
    Q24 = lerp(V24, P24, 1.30)
    check('14-24', 'P lies on side P4P3', _collinear(Q4_24, P24, Q3_24))
    check('14-24', 'V, P, Q collinear', _collinear(V24, P24, Q24))

    # ---- 14-25 : D lies on AB
    A25, B25 = (0.28, 0.32), (3.05, 0.86)
    D25 = lerp(A25, B25, 0.46)
    check('14-25', 'D on AB', _collinear(A25, D25, B25))

    # ---- 14-26 : the flattened faces do NOT encircle the common point
    C26 = (1.52, 1.30)
    ring = [(2.38, 2.52), (0.92, 2.52), (0.15, 1.30), (0.90, 0.06), (2.32, 0.05)]
    tot = 0.0
    for p, q in zip(ring, ring[1:]):
        u, v = V(C26, p), V(C26, q)
        cosang = (u[0] * v[0] + u[1] * v[1]) / (dist((0, 0), u) * dist((0, 0), v))
        tot += math.degrees(math.acos(max(-1.0, min(1.0, cosang))))
    check('14-26', 'face angles sum < 360 deg', max(0.0, tot - 360.0) / 360.0)

    # ---- 14-31 : prism -- bases in parallel planes, lateral edges parallel
    check('14-31', 'the two planes are parallel',
          par(V((0, 0), (3.55, 0)), V((0.15, 2.85), (3.70, 2.85))))
    lat = []
    for i in range(6):
        a = (1.92 + 0.98 * math.cos(math.radians(30 + 60 * i)),
             0.48 + 0.40 * math.sin(math.radians(30 + 60 * i)))
        b = (2.07 + 0.98 * math.cos(math.radians(30 + 60 * i)),
             3.33 + 0.40 * math.sin(math.radians(30 + 60 * i)))
        lat.append(V(a, b))
    for i in range(1, 6):
        check('14-31', f'lateral edge {i + 1} || edge 1', par(lat[0], lat[i]))

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
    O42, ap42, a42, b42 = (0.0, 0.0), (0.0, 2.42), 1.32, 0.46
    check('14-42', 'the axis is vertical', perp(V(O42, ap42), (1, 0)))
    for i in range(8):
        th = math.radians(202 + 45 * i)
        x, y = a42 * math.cos(th), b42 * math.sin(th)
        check('14-42', f'vertex {i + 1} on the base ellipse',
              abs((x / a42) ** 2 + (y / b42) ** 2 - 1.0))
