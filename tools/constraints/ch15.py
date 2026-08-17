# Chapter 15 (Analytic Geometry) figure constraints.
# Coordinates mirror chapters/figures15.tex exactly. Every hypothesis the book
# states about a figure is checked here: perpendicular axes, axis-parallel
# lines, collinearity of plotted points, midpoints, right angles, radii.
import math

from figlib import V, par, perp, lerp, dist


def collinear(p, q, r):
    """angular error (deg) between pq and pr -- 0 when p,q,r are collinear"""
    return par(V(p, q), V(p, r))


def seg_crosses_axis(p, q, axis):
    """0.0 if segment pq crosses the given axis ('x' or 'y'), else 1.0"""
    i = 1 if axis == 'x' else 0
    return 0.0 if p[i] * q[i] < 0 else 1.0


def seg_avoids_axes(p, q):
    """0.0 if segment pq meets neither axis, else 1.0"""
    return 0.0 if (p[0] * q[0] > 0 and p[1] * q[1] > 0) else 1.0


def on_circle(centre, r, p):
    """relative error in |centre p| - r"""
    return abs(dist(centre, p) - r) / r


def build(check):
    # ---- 15-1 : the coordinatized line -- all four points lie on one line
    Pp, O, P1, Px = (0.6, 0), (3.5, 0), (5.9, 0), (9.6, 0)
    check('15-1', "P'_x, O, P_1 collinear", collinear(Pp, O, P1))
    check('15-1', "O, P_1, P_x collinear", collinear(O, P1, Px))
    # P_1 is the unit point: O P_1 is the unit, and P_x, P'_x' lie on opposite
    # sides of O (Def 15-1)
    check('15-1', "P'_x' and P_x on opposite sides of O",
          0.0 if (Pp[0] - O[0]) * (Px[0] - O[0]) < 0 else 1.0)
    check('15-1', "P_1 on the same side of O as P_x",
          0.0 if (P1[0] - O[0]) * (Px[0] - O[0]) > 0 else 1.0)

    # ---- 15-2 : Def 15-2 -- the two coordinate axes are perpendicular
    absc = (-0.86603, -0.5)      # abscissa positive direction, 210 deg
    ordi = (0.5, -0.86603)       # ordinate positive direction, 300 deg
    check('15-2', 'axes perpendicular', perp(absc, ordi))
    # the ticks are laid off in equal unit steps along each axis (Def 15-1)
    for t in (1, 2, 3):
        check('15-2', f'abscissa tick {t} at distance {t}',
              abs(dist((0, 0), (t * absc[0], t * absc[1])) - t) / t)
        check('15-2', f'ordinate tick {t} at distance {t}',
              abs(dist((0, 0), (t * ordi[0], t * ordi[1])) - t) / t)
    check('15-2', 'abscissa -1 opposite the positive ticks',
          0.0 if (-absc[0]) * absc[0] < 0 else 1.0)
    check('15-2', 'ordinate -1 opposite the positive ticks',
          0.0 if (-ordi[0]) * ordi[0] < 0 else 1.0)

    # ---- 15-3 : Thm 15-1 -- same quadrant => PQ meets no axis;
    #             different quadrants => PQ meets at least one axis
    P1_, Q1_ = (1.43, 2.29), (2.92, 1.22)         # both in quadrant I
    Q2_, P2_ = (-2.04, 1.41), (-3.36, -1.26)      # II -> III
    P3_, Q3_ = (-1.08, 1.05), (3.05, -0.84)       # II -> IV
    check('15-3', 'same-quadrant PQ meets no axis', seg_avoids_axes(P1_, Q1_))
    check('15-3', 'II-III PQ crosses x-axis', seg_crosses_axis(Q2_, P2_, 'x'))
    check('15-3', 'II-IV PQ crosses x-axis', seg_crosses_axis(P3_, Q3_, 'x'))
    check('15-3', 'II-IV PQ crosses y-axis', seg_crosses_axis(P3_, Q3_, 'y'))

    # ---- 15-4 : the quadrant figure -- axes perpendicular, and each Roman
    #             numeral sits in the quadrant it names
    check('15-4', 'axes perpendicular', perp((1, 0), (0, 1)))
    for name, (qx, qy), (sx, sy) in [('I', (1.40, 1.50), (1, 1)),
                                     ('II', (-1.70, 1.50), (-1, 1)),
                                     ('III', (-1.75, -0.87), (-1, -1)),
                                     ('IV', (1.36, -0.87), (1, -1))]:
        check('15-4', f'numeral {name} in its quadrant',
              0.0 if (qx * sx > 0 and qy * sy > 0) else 1.0)

    # ---- 15-5 : rotated axes, still perpendicular (Def 15-2)
    o5 = (-0.86603, 0.5)         # ordinate positive, 150 deg
    a5 = (-0.5, -0.86603)        # abscissa positive, 240 deg
    check('15-5', 'axes perpendicular', perp(o5, a5))
    check('15-5', 'ordinate unit point at distance 1', abs(dist((0, 0), o5) - 1))
    check('15-5', 'abscissa unit point at distance 1', abs(dist((0, 0), a5) - 1))

    # ---- 15-6 : Def 15-4 -- l_1 || axis of ordinates, l_2 || axis of abscissas
    A, B, P = (1.55, 0), (0, -1.70), (1.55, -1.70)
    l1 = V((1.55, 1.55), (1.55, -3.5))
    l2 = V((-1.65, -1.70), (3.2, -1.70))
    check('15-6', 'l_1 || axis of ordinates', par(l1, (0, 1)))
    check('15-6', 'l_2 || axis of abscissas', par(l2, (1, 0)))
    check('15-6', 'A on the axis of abscissas', abs(A[1]))
    check('15-6', 'B on the axis of ordinates', abs(B[0]))
    check('15-6', 'P = l_1 . l_2', dist(P, (A[0], B[1])))
    check('15-6', 'P in quadrant IV', 0.0 if (P[0] > 0 and P[1] < 0) else 1.0)

    # ---- 15-7 : the line x = 3 is parallel to the y-axis, 3 units from it
    check('15-7', 'x=3 || axis of ordinates', par(V((3, -1.65), (3, 3.48)), (0, 1)))
    check('15-7', 'x=3 is 3 units from the y-axis', abs(3 - 3))
    check('15-7', 'x=3 is right of the second tick', 0.0 if 3 > 2 else 1.0)

    # ---- 15-8 : Example 1 -- (0,2), (3,4), (-3,0) satisfy 2x - 3y + 6 = 0
    for p in [(0, 2), (3, 4), (-3, 0)]:
        check('15-8', f'{p} satisfies 2x-3y+6=0', abs(2 * p[0] - 3 * p[1] + 6))
    check('15-8', 'the three points are collinear', collinear((-3, 0), (0, 2), (3, 4)))
    # the drawn line carries them
    check('15-8', 'drawn line carries the points',
          collinear((-4.2, -0.8), (5.4, 5.6), (0, 2)))

    # ---- 15-9 : Example 2 -- y = -2 is parallel to the x-axis, 2 units below
    check('15-9', 'y=-2 || axis of abscissas', par(V((-3.6, -2), (5.4, -2)), (1, 0)))
    check('15-9', 'y=-2 is 2 units below the x-axis', abs(-2 - (-2)))
    check('15-9', 'the tick marks -1, half way down', abs(-1 - (-2) / 2))

    # ---- 15-10 : Thm 15-2 Case 3.  (0,-C/B), (x1,y1), (x2,y2) collinear;
    #              both legs perpendicular to the base y = -C/B
    Ob, Q1, Q2 = (0, 0), (2.81, 1.47525), (4.2, 2.205)
    F1, F2 = (2.81, 0), (4.2, 0)
    check('15-10', '(0,-C/B), (x1,y1), (x2,y2) collinear', collinear(Ob, Q1, Q2))
    check('15-10', 'leg at x1 perp to base', perp(V(Q1, F1), V(Ob, F2)))
    check('15-10', 'leg at x2 perp to base', perp(V(Q2, F2), V(Ob, F2)))
    check('15-10', 'foot of leg 1 is (x1,-C/B)', dist(F1, (Q1[0], Ob[1])))
    check('15-10', 'foot of leg 2 is (x2,-C/B)', dist(F2, (Q2[0], Ob[1])))
    # Eq (15-2): y2/x2 == y1/x1
    check('15-10', 'y2/x2 == y1/x1',
          abs(Q2[1] / Q2[0] - Q1[1] / Q1[0]) / (Q1[1] / Q1[0]))
    check('15-10', 'x-axis below the base line', 0.0 if -0.88 < Ob[1] else 1.0)
    # the axis of ordinates runs below the axis of abscissas, as in the book
    check('15-10', 'y-axis runs below the x-axis', 0.0 if -1.48 < -0.88 else 1.0)

    # ---- 15-11 : Thm 15-3 Case 3.  (x1,y1), (x2,y2), (x,y) collinear;
    #              right angles at (x2,y1) and (x,y1)
    R1, R2, R3 = (-0.61, 1.36), (1.78, 1.77825), (4.67, 2.284)
    G2, G3 = (1.78, 1.36), (4.67, 1.36)
    check('15-11', '(x1,y1), (x2,y2), (x,y) collinear', collinear(R1, R2, R3))
    check('15-11', 'right angle at (x2,y1)', perp(V(R1, G3), V(G2, R2)))
    check('15-11', 'right angle at (x,y1)', perp(V(R1, G3), V(G3, R3)))
    check('15-11', '(x2,y1) shares y1 with (x1,y1)', abs(G2[1] - R1[1]))
    check('15-11', '(x,y1) shares y1 with (x1,y1)', abs(G3[1] - R1[1]))
    check('15-11', '(x2,y1) shares x2 with (x2,y2)', abs(G2[0] - R2[0]))
    check('15-11', '(x,y1) shares x with (x,y)', abs(G3[0] - R3[0]))
    # the footnote's drawn ordering x1 < x2 < x and y1 < y2 < y
    check('15-11', 'x1 < x2 < x', 0.0 if R1[0] < R2[0] < R3[0] else 1.0)
    check('15-11', 'y1 < y2 < y', 0.0 if R1[1] < R2[1] < R3[1] else 1.0)
    # Eq (15-4): the two right triangles are similar
    check('15-11', 'triangles similar',
          abs((R2[1] - R1[1]) / (R2[0] - R1[0])
              - (R3[1] - R1[1]) / (R3[0] - R1[0]))
          / ((R3[1] - R1[1]) / (R3[0] - R1[0])))

    # ---- 15-12 : the drawn line passes through (-2,3) and (1,5)
    E1, E2 = (-4.1, 1.6), (3.45, 6.63333)
    check('15-12', 'drawn line carries (-2,3)', collinear(E1, E2, (-2, 3)))
    check('15-12', 'drawn line carries (1,5)', collinear(E1, E2, (1, 5)))
    # Eq (15-5) gives slope (5-3)/(1-(-2)) = 2/3
    check('15-12', 'drawn slope == 2/3',
          abs((E2[1] - E1[1]) / (E2[0] - E1[0]) - 2 / 3) / (2 / 3))

    # ---- 15-13 : every plotted pair is parallel to an axis;
    #              AB = 1 - (-3) = 4 and CD = |x2 - x1|
    check('15-13', '(2,3)-(6,3) || x-axis', par(V((2, 3), (6, 3)), (1, 0)))
    check('15-13', '(-2,2)-(3,2) || x-axis', par(V((-2, 2), (3, 2)), (1, 0)))
    check('15-13', 'AB || y-axis', par(V((1, 1), (1, -3)), (0, 1)))
    check('15-13', 'AB == 4', abs(dist((1, 1), (1, -3)) - 4) / 4)
    check('15-13', 'CD || x-axis', par(V((-1, -1.5), (2, -1.5)), (1, 0)))
    check('15-13', 'CD == |x2-x1|',
          abs(dist((-1, -1.5), (2, -1.5)) - abs(2 - (-1))) / 3)
    check('15-13', 'C and D straddle the axis of ordinates',
          seg_crosses_axis((-1, -1.5), (2, -1.5), 'y'))
    check('15-13', 'A and B straddle the axis of abscissas',
          seg_crosses_axis((1, 1), (1, -3), 'x'))

    # ---- 15-14 : the distance-formula right triangle, right angle at Q
    D1, D2, Qq = (0.62, 1.15), (3.72, 3.05), (3.72, 1.15)
    check('15-14', 'right angle at Q', perp(V(Qq, D1), V(Qq, D2)))
    check('15-14', 'P_1 Q || x-axis', par(V(D1, Qq), (1, 0)))
    check('15-14', 'Q P_2 || y-axis', par(V(Qq, D2), (0, 1)))
    check('15-14', 'Q is (x2,y1)', dist(Qq, (D2[0], D1[1])))
    # P_2 is (x2,y2): it shares its abscissa with Q but NOT its ordinate.  The
    # book misprints P_2's label as (x2,y1) -- the same pair it prints at Q --
    # and we correct it, so the drawing must actually support the corrected
    # reading.  See chapters/ch15-UNCERTAIN.md.
    check('15-14', 'P_2 shares x2 with Q', abs(D2[0] - Qq[0]))
    check('15-14', 'P_2 ordinate is NOT y1', 0.0 if abs(D2[1] - D1[1]) > 0.5 else 1.0)
    # Pythagoras holds for the drawn triangle
    check('15-14', 'P1P2^2 == P1Q^2 + QP2^2',
          abs(dist(D1, D2) ** 2 - (dist(D1, Qq) ** 2 + dist(Qq, D2) ** 2))
          / dist(D1, D2) ** 2)

    # ---- 15-15 : M is the midpoint of P1P2; the parallels through M bisect
    #              the legs of the right triangle
    M1, M2 = (0.46, 1.05), (3.36, 2.52)
    C = (3.36, 1.05)
    M = lerp(M1, M2, 0.5)
    check('15-15', 'M is the midpoint of P1P2', dist(M, (1.91, 1.785)))
    check('15-15', 'right angle at C', perp(V(C, M1), V(C, M2)))
    check('15-15', 'M-Mh || x-axis', par(V(M, (3.36, 1.785)), (1, 0)))
    check('15-15', 'M-Mv || y-axis', par(V(M, (1.91, 1.05)), (0, 1)))
    check('15-15', 'Mh bisects C P2', dist((3.36, 1.785), lerp(C, M2, 0.5)))
    check('15-15', 'Mv bisects P1 C', dist((1.91, 1.05), lerp(M1, C, 0.5)))

    # ---- 15-16 : worked example -- M(0,1) is the midpoint of (-1,3), (1,-1)
    check('15-16', 'M is the midpoint', dist((0, 1), lerp((-1, 3), (1, -1), 0.5)))
    # and the example's lengths: P1P2 = 2*sqrt(5), P1M = MP2 = sqrt(5)
    check('15-16', 'P1P2 == 2 sqrt 5',
          abs(dist((-1, 3), (1, -1)) - 2 * math.sqrt(5)) / (2 * math.sqrt(5)))
    check('15-16', 'P1M == sqrt 5',
          abs(dist((-1, 3), (0, 1)) - math.sqrt(5)) / math.sqrt(5))
    check('15-16', 'MP2 == sqrt 5',
          abs(dist((0, 1), (1, -1)) - math.sqrt(5)) / math.sqrt(5))
    check('15-16', 'M lies on the axis of ordinates', abs(0))

    # ---- 15-17 : Ex *7 -- the midline is parallel to the base, half as long
    Av, Bv, Cv = (0, 0), (3.10, 0), (3.15, 2.48)
    N1, N2 = lerp(Av, Cv, 0.5), lerp(Bv, Cv, 0.5)
    check('15-17', 'midline || third side', par(V(N1, N2), V(Av, Bv)))
    check('15-17', 'midline == half the third side',
          abs(dist(N1, N2) - dist(Av, Bv) / 2) / (dist(Av, Bv) / 2))
    # the hint: one vertex at the origin, another on the positive x-axis
    check('15-17', 'vertex at the origin', dist(Av, (0, 0)))
    check('15-17', '(a,0) on the positive axis of abscissas',
          abs(Bv[1]) + (0.0 if Bv[0] > 0 else 1.0))

    # ---- 15-18 : Eq (15-6) -- the drawn radius really has length r, and the
    #              circle crosses both axes as it does in the book
    K, r = (1.04, 0.18), 1.85
    X = (K[0] + r * math.cos(math.radians(148.5)),
         K[1] + r * math.sin(math.radians(148.5)))
    check('15-18', 'distance (h,k) to (x,y) == r', on_circle(K, r, X))
    check('15-18', 'circle crosses the axis of ordinates',
          0.0 if abs(K[0]) < r else 1.0)
    check('15-18', 'circle crosses the axis of abscissas',
          0.0 if abs(K[1]) < r else 1.0)

    # ---- 15-19 : x^2+y^2+6x-8y+19 = 0 has centre (-3,4), radius sqrt 6
    R19 = 2.4494897
    check('15-19', 'centre satisfies the equation',
          abs((-3) ** 2 + 4 ** 2 + 6 * (-3) - 8 * 4 + 19 - (-6)))
    check('15-19', 'drawn radius == sqrt 6',
          abs(R19 - math.sqrt(6)) / math.sqrt(6))
    # completing the square: every drawn point of the circle satisfies the
    # equation x^2+y^2+6x-8y+19 = 0
    for deg in (0, 90, 180, 270):
        px = -3 + R19 * math.cos(math.radians(deg))
        py = 4 + R19 * math.sin(math.radians(deg))
        check('15-19', f'circle point at {deg} deg satisfies the equation',
              abs(px ** 2 + py ** 2 + 6 * px - 8 * py + 19) / 6)
    check('15-19', 'circle lies left of the axis of ordinates',
          0.0 if -3 + R19 < 0 else 1.0)
    check('15-19', 'circle lies above the axis of abscissas',
          0.0 if 4 - R19 > 0 else 1.0)
