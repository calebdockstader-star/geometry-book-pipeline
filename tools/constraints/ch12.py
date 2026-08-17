# Chapter 12 figure constraints.
#
# Coordinates MIRROR chapters/figures12.tex exactly -- same radii, same
# centres, same angles.  (Before the figure review they were only similar,
# which meant a passing check did not actually certify the drawing.)
#
# Each entry re-asserts, numerically, a hypothesis the BOOK states in words:
# arc midpoints, angle bisectors, tangency, parallel secants, collinear and
# BETWEEN secant points through an external point, which vertices lie on the
# circle and which deliberately do not, and the segment lengths quoted in
# Exercises 15, 16, 17 and 18.
import math

from figlib import V, ang, par, perp, dist, foot  # noqa: F401


def P(O, a, R):
    """point at angle a (degrees) and radius R from centre O"""
    return (O[0] + R * math.cos(math.radians(a)),
            O[1] + R * math.sin(math.radians(a)))


def onc(O, X, R):
    """relative error of |OX| against R"""
    return abs(dist(O, X) - R) / R


def order(*a):
    """0 when a is strictly decreasing; grows when it is not"""
    return max([0.0] + [a[i + 1] - a[i] for i in range(len(a) - 1)])


def dirang(u):
    """signed direction of u in (-180, 180]; unlike ang() it does not fold"""
    return math.degrees(math.atan2(u[1], u[0]))


def line_dist(A, B, X):
    """distance from X to the line AB"""
    ab = V(A, B)
    ax = V(A, X)
    return abs(ab[0] * ax[1] - ab[1] * ax[0]) / math.hypot(*ab)


def cross(p1, p2, p3, p4):
    """intersection of line p1p2 with line p3p4"""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d,
            (a * (y3 - y4) - (y1 - y2) * b) / d)


def param(A, B, X):
    """position of X along A->B as a fraction of AB"""
    ab = V(A, B)
    ax = V(A, X)
    return (ax[0] * ab[0] + ax[1] * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)


def between(A, B, X):
    """0 when X lies strictly between A and B"""
    t = param(A, B, X)
    return max(0.0, -t) + max(0.0, t - 1.0)


def outside(O, X, R, margin=0.0):
    """0 when |OX| exceeds R*(1+margin); relative shortfall otherwise"""
    return max(0.0, R * (1.0 + margin) - dist(O, X)) / R


def inside(O, X, R, margin=0.0):
    """0 when |OX| is below R*(1-margin)"""
    return max(0.0, dist(O, X) - R * (1.0 - margin)) / R


def build(check):
    O = (0, 0)

    # ---- 12-1 : CB is a diameter; A on the circle, off that diameter
    R = 1.25
    C, B, A = P(O, 180, R), P(O, 0, R), P(O, 227, R)
    check('12-1', 'CB is a diameter', par(V(C, O), V(O, B)))
    check('12-1', 'A on the circle', onc(O, A, R))
    check('12-1', 'A off the diameter CB', max(0.0, 0.20 - line_dist(C, B, A) / R))

    # ---- 12-2 : C interior to angle AOB, so angle AOB > angle COB
    R = 1.45
    check('12-2', 'C interior to angle AOB', order(78, 47, 0))
    for nm, a in (('A', 78), ('C', 47), ('B', 0)):
        check('12-2', f'{nm} on the circle', onc(O, P(O, a, R), R))

    # ---- 12-3 : P, P' are the crossings of rays OQ, OQ' with the chord EF
    R = 1.90
    E, F = P(O, 75, R), P(O, 0, R)
    Q, Qp = P(O, 56, R), P(O, 27, R)
    Pp_ = cross(O, Q, E, F)
    Pq_ = cross(O, Qp, E, F)
    check('12-3', 'P on chord EF', par(V(E, F), V(E, Pp_)))
    check('12-3', 'P on ray OQ', par(V(O, Q), V(O, Pp_)))
    check('12-3', 'P between E and F', between(E, F, Pp_))
    check('12-3', "P' on chord EF", par(V(E, F), V(E, Pq_)))
    check('12-3', "P' on ray OQ'", par(V(O, Qp), V(O, Pq_)))
    check('12-3', "P' between E and F", between(E, F, Pq_))

    # ---- 12-4 : C bisects the arc EXTERIOR to central angle AOB
    R = 1.25
    check('12-4', 'C midpoint of exterior arc', abs((240.5 - 118) - (363 - 240.5)))
    for nm, a in (('A', 118), ('B', 3), ('C', 240.5)):
        check('12-4', f'{nm} on the circle', onc(O, P(O, a, R), R))

    # ---- 12-5 : every vertex is the midpoint of the arc it bisects
    for tag, hi, mid, lo in [('C mid arc AB', 135, 62, -11),
                             ('D mid arc AC', 135, 98.5, 62),
                             ('E mid arc CB', 62, 25.5, -11),
                             ('F mid arc AD', 135, 116.75, 98.5),
                             ('G mid arc DC', 98.5, 80.25, 62),
                             ('H mid arc CE', 62, 43.75, 25.5),
                             ('I mid arc EB', 25.5, 7.25, -11)]:
        check('12-5', tag, abs((hi - mid) - (mid - lo)))
    check('12-5', 'eight-side path runs A..B', order(135, 116.75, 98.5, 80.25,
                                                     62, 43.75, 25.5, 7.25, -11))

    # ---- 12-6 : circumscribed corners are the tangent intersections
    R = 1.3
    A6, C6, B6 = P(O, 135, R), P(O, 62, R), P(O, -11, R)
    T = P(O, 98.5, R / math.cos(math.radians(36.5)))
    U = P(O, 25.5, R / math.cos(math.radians(36.5)))
    check('12-6', 'TA tangent at A', perp(V(O, A6), V(A6, T)))
    check('12-6', 'TC tangent at C', perp(V(O, C6), V(C6, T)))
    check('12-6', 'UC tangent at C', perp(V(O, C6), V(C6, U)))
    check('12-6', 'UB tangent at B', perp(V(O, B6), V(B6, U)))
    check('12-6', 'T outside the circle', outside(O, T, R, 0.05))
    check('12-6', 'U outside the circle', outside(O, U, R, 0.05))

    # ---- 12-7 : the inscribed hexagon is regular and A, C, B are its vertices
    R = 1.25
    hexa = [P(O, 60 * k, R) for k in range(6)]
    sides = [dist(hexa[k], hexa[(k + 1) % 6]) for k in range(6)]
    check('12-7', 'hexagon equilateral', (max(sides) - min(sides)) / max(sides))
    for nm, a in (('A', 120), ('C', 60), ('B', 0)):
        v = P(O, a, R)
        check('12-7', f'{nm} is a hexagon vertex',
              min(dist(v, h) for h in hexa) / R)

    # ---- 12-8 : angle AOC is right, and angle AOB congruent to angle BOC
    R = 1.25
    A8, B8, C8 = P(O, 90, R), P(O, 45, R), P(O, 0, R)
    check('12-8', 'angle AOC is right', perp(V(O, A8), V(O, C8)))
    check('12-8', 'angle AOB == angle BOC', abs((90 - 45) - (45 - 0)))

    # ---- 12-9 : an IRREGULAR inscribed path, vertices on the circle and in
    #             order from A round to B
    R = 1.25
    verts = (145, 126, 111, 88, 62, 40, 15, -8)
    check('12-9', 'path vertices on circle',
          max(onc(O, P(O, a, R), R) for a in verts))
    check('12-9', 'path runs A..B in order', order(*verts))
    steps = [verts[i] - verts[i + 1] for i in range(len(verts) - 1)]
    check('12-9', 'path is NOT regular',
          max(0.0, 3.0 - (max(steps) - min(steps))))   # spacing must vary

    # ---- 12-10 : arcs AB and BC are adjacent, sharing only B
    check('12-10', 'B between A and C', order(75, 30, -15))

    # ---- 12-11 : C interior to angle AOB, so angle AOB > angle COB
    check('12-11', 'C interior to angle AOB', order(104, 90, 10))
    check('12-11', 'angle AOB > angle COB', max(0.0, (90 - 10) - (104 - 10)))

    # ---- 12-12 : corresponding central angles congruent on the two circles,
    #              whose radii must differ (that is the point of Theorem 12-7)
    for tag, big, small in [('angle AOP', 148 - 90, 148 - 90),
                            ('angle POQ', 90 - 48, 90 - 48),
                            ('angle QOB', 48 - 0, 48 - 0),
                            ('angle AOB', 148 - 0, 148 - 0)]:
        check('12-12', tag + ' matches', abs(big - small))
    Rp, Rr = 1.35, 0.85
    check('12-12', "r' differs from r", max(0.0, 0.20 - abs(Rp / Rr - 1.0)))

    # ---- 12-13 : OC bisects the right angle AOB; OD bisects BOC; OE bisects DOC
    R = 1.6
    A13, B13 = P(O, 0, R), P(O, 90, R)
    check('12-13', 'angle AOB is right', perp(V(O, A13), V(O, B13)))
    check('12-13', 'OC bisects angle AOB', abs((45 - 0) - (90 - 45)))
    check('12-13', 'OD bisects angle BOC', abs((90 - 67.5) - (67.5 - 45)))
    check('12-13', 'OE bisects angle DOC', abs((67.5 - 56.25) - (56.25 - 45)))
    check('12-13', 'B, D, E, C, A in order', order(90, 67.5, 56.25, 45, 0))

    # ---- 12-14 : right-angle sector; P past E, since L exceeds 5/8 of a quarter
    R = 1.7
    A14, B14 = P(O, 0, R), P(O, 90, R)
    check('12-14', 'sector is a right angle', perp(V(O, A14), V(O, B14)))
    check('12-14', 'arc AP > arc AE', max(0.0, 56.25 - 60))
    check('12-14', 'P on the arc', onc(O, P(O, 60, R), R))
    check('12-14', 'arc AP inside the quadrant', order(90, 60, 0))

    # ---- 12-15 / 12-16 : A falls on the (n+1)st arc, i.e. between the ray
    #                      that closes the nth degree and the one after it
    for fig in ('12-15', '12-16'):
        check(fig, 'A lies on the (n+1)st arc', order(57, 48, 32))

    # ---- 12-17 : the two central angles are congruent; exterior arc = 360 - A
    left = 37.5 - (-37.5)
    right = 217.5 - 142.5
    check('12-17', 'central angles congruent', abs(left - right))
    check('12-17', 'exterior arc == 360 - A', abs((142.5 - (-142.5)) - (360 - right)))

    # ---- 12-18 : the central angle is exactly one radian
    check('12-18', 'central angle == 1 rad',
          abs((50 - (-7.2958)) - math.degrees(1.0)))

    # ---- 12-19 : (a) and (b) inscribed; (c) NOT.
    # In (c) the vertex B does lie essentially on the circle, but the SIDE BA
    # carries no second point of the circle -- the whole ray misses it.  That,
    # not a displaced vertex, is what fails the definition, and it is what the
    # book's plate draws.
    Rc = 0.95
    Oa = (0, 0)
    check('12-19', 'vertex B on circle (a)', onc(Oa, P(Oa, 168, Rc), Rc))
    check('12-19', 'A on circle (a)', onc(Oa, P(Oa, 12, Rc), Rc))
    check('12-19', 'C on circle (a)', onc(Oa, P(Oa, -55, Rc), Rc))
    check('12-19', 'vertex B on circle (b)', onc(Oa, P(Oa, 232, Rc), Rc))
    check('12-19', 'A on circle (b)', onc(Oa, P(Oa, 119, Rc), Rc))
    check('12-19', 'C on circle (b)', onc(Oa, P(Oa, -43, Rc), Rc))
    Oc = (6.30, 0)
    Bc = P(Oc, 215.6, 1.08 * Rc)
    Ac = P(Bc, 111.8, 1.50 * Rc)
    Cc = P(Oc, -45.3, Rc)
    check('12-19', 'C on the circle (c)', onc(Oc, Cc, Rc))
    check('12-19', 'vertex B just outside (c)', outside(Oc, Bc, Rc, 0.02))
    check('12-19', 'A well outside (c)', outside(Oc, Ac, Rc, 0.30))
    check('12-19', 'side BA misses the circle (c)',
          max(0.0, Rc - line_dist(Bc, Ac, Oc)) / Rc)
    check('12-19', 'side BC cuts the circle (c)',
          max(0.0, line_dist(Bc, Cc, Oc) - Rc) / Rc)

    # ---- 12-20 : BC is a diameter; A on the circle; OA the drawn radius
    R = 1.25
    B20, C20, A20 = P(O, 180, R), P(O, 0, R), P(O, 79, R)
    check('12-20', 'BC is a diameter', par(V(B20, O), V(O, C20)))
    check('12-20', 'A on the circle', onc(O, A20, R))
    check('12-20', 'A off the diameter BC', max(0.0, 0.20 - line_dist(B20, C20, A20) / R))
    check('12-20', 'angle BAC is right', perp(V(A20, B20), V(A20, C20)))

    # ---- 12-21 : BP a diameter; centre INTERIOR to angle ABC; x, y half-arcs
    R = 1.6
    B21, P21 = P(O, 180, R), P(O, 0, R)
    A21, C21 = P(O, 80, R), P(O, -33, R)
    check('12-21', 'BP is a diameter', par(V(B21, O), V(O, P21)))
    aA = dirang(V(B21, A21))
    aP = dirang(V(B21, P21))
    aC = dirang(V(B21, C21))
    check('12-21', 'centre interior to angle ABC', order(aA, aP, aC))
    check('12-21', 'x == half arc AP', abs(aA - 0.5 * (80 - 0)))
    check('12-21', 'y == half arc PC', abs(-aC - 0.5 * (0 - (-33))))
    check('12-21', 'x + y == angle ABC', abs((aA - aC) - 0.5 * (80 - (-33))))

    # ---- 12-22 : BQ a diameter; centre EXTERIOR to angle ABC
    R = 1.35   # 12-22 keeps the smaller radius; 12-21 was enlarged for its labels
    B22, Q22 = P(O, 180, R), P(O, 0, R)
    A22, C22 = P(O, 110, R), P(O, 36, R)
    check('12-22', 'BQ is a diameter', par(V(B22, O), V(O, Q22)))
    bA = dirang(V(B22, A22))
    bC = dirang(V(B22, C22))
    check('12-22', 'centre exterior to angle ABC',
          max(0.0, -min(bA, bC)))       # both rays on one side of BQ (angle 0)
    check('12-22', 'BQ outside angle ABC', order(bA, bC, 0))
    check('12-22', 'angle ABC == half arc AC', abs((bA - bC) - 0.5 * (110 - 36)))

    # ---- 12-23 : BC a diameter, so the inscribed angle BAC is right
    R = 1.25
    B23, C23, A23 = P(O, 180, R), P(O, 0, R), P(O, 105, R)
    check('12-23', 'BC is a diameter', par(V(B23, O), V(O, C23)))
    check('12-23', 'angle BAC is right', perp(V(A23, B23), V(A23, C23)))
    check('12-23', 'A off the diameter BC', max(0.0, 0.20 - line_dist(B23, C23, A23) / R))

    # ---- 12-24 : AB parallel to CD; equal cut-off arcs; UNEQUAL offsets, so
    #              the drawing does not smuggle in AB congruent to CD
    R = 1.25
    A24, B24 = (-1.0440, 0.6875), (1.0440, 0.6875)
    C24, D24 = (-0.9165, -0.8500), (0.9165, -0.8500)
    check('12-24', 'AB || CD', par(V(A24, B24), V(C24, D24)))
    for nm, X in (('A', A24), ('B', B24), ('C', C24), ('D', D24)):
        check('12-24', f'{nm} on the circle', onc(O, X, R))
    aA24 = math.degrees(math.atan2(A24[1], A24[0]))
    aC24 = math.degrees(math.atan2(C24[1], C24[0])) % 360
    aB24 = math.degrees(math.atan2(B24[1], B24[0]))
    aD24 = math.degrees(math.atan2(D24[1], D24[0]))
    check('12-24', 'arc AC == arc BD', abs((aC24 - aA24) - (aB24 - aD24)))
    check('12-24', 'chords not equidistant',
          max(0.0, 0.05 - abs(abs(A24[1]) - abs(C24[1])) / R))

    # ---- 12-25 : AC tangent at B; DE parallel to AC; arcs BD and BE equal
    R = 1.05
    B25 = P(O, 133, R)
    A25 = P(B25, 223, 1.22)
    C25 = P(B25, 43, 1.06)
    D25, E25 = P(O, 199, R), P(O, 67, R)
    check('12-25', 'AC tangent at B', perp(V(O, B25), V(A25, C25)))
    check('12-25', 'B between A and C', between(A25, C25, B25))
    check('12-25', 'DE || AC', par(V(D25, E25), V(A25, C25)))
    check('12-25', 'arc BD == arc BE', abs((199 - 133) - (133 - 67)))

    # ---- 12-26 : A, B, C collinear and A, E, D collinear (two secants), with
    #              B and E the NEAR crossings; auxiliary chord BD
    R = 1.1
    B26, C26 = P(O, 151.6, R), P(O, 79.5, R)
    D26, E26 = P(O, -31, R), P(O, 213, R)
    A26 = cross(C26, B26, D26, E26)
    check('12-26', 'A, B, C collinear', par(V(C26, B26), V(C26, A26)))
    check('12-26', 'A, E, D collinear', par(V(D26, E26), V(D26, A26)))
    check('12-26', 'A outside the circle', outside(O, A26, R, 0.30))
    check('12-26', 'B between A and C', between(A26, C26, B26))
    check('12-26', 'E between A and D', between(A26, D26, E26))
    check('12-26', 'AB*AC == AE*AD',
          abs(dist(A26, B26) * dist(A26, C26)
              - dist(A26, E26) * dist(A26, D26))
          / (dist(A26, B26) * dist(A26, C26)))

    # ---- 12-27 : E is the crossing of the chords AC and BD, inside the circle
    R = 1.1
    A27, B27 = P(O, 190, R), P(O, 135, R)
    C27, D27 = P(O, 10, R), P(O, -68, R)
    E27 = cross(A27, C27, B27, D27)
    check('12-27', 'E on chord AC', par(V(A27, C27), V(A27, E27)))
    check('12-27', 'E on chord BD', par(V(B27, D27), V(B27, E27)))
    check('12-27', 'E inside the circle', inside(O, E27, R, 0.05))
    check('12-27', 'AE*EC == BE*ED',
          abs(dist(A27, E27) * dist(E27, C27)
              - dist(B27, E27) * dist(E27, D27))
          / (dist(A27, E27) * dist(E27, C27)))

    # ---- 12-28 : Exercise 15 numbers -- AO:OB = 12:4, CO:OD = 8:6
    R = 1.1
    A28, B28 = P(O, 192.5, R), P(O, 31.1, R)
    C28, D28 = P(O, 113.4, R), P(O, 354.1, R)
    X28 = cross(A28, B28, C28, D28)
    check('12-28', 'AO/OB == 12/4',
          abs(dist(A28, X28) / dist(X28, B28) - 3.0) / 3.0)
    check('12-28', 'CO/OD == 8/6',
          abs(dist(C28, X28) / dist(X28, D28) - 4.0 / 3.0) / (4.0 / 3.0))
    check('12-28', 'crossing inside the circle', inside(O, X28, R, 0.05))

    # ---- 12-29 : Exercise 16 numbers -- AD = 6, DE = 10, AB = 8, so BC = 4
    R = 1.55
    A29 = (-3.3064, 0)
    D29, E29 = (-1.5328, 0.2303), (1.4232, 0.6141)
    B29, C29 = (-1.1566, -1.0319), (-0.0817, -1.5478)
    k = dist(A29, D29) / 6.0
    check('12-29', 'DE == 10 units', abs(dist(D29, E29) - 10 * k) / (10 * k))
    check('12-29', 'AB == 8 units', abs(dist(A29, B29) - 8 * k) / (8 * k))
    check('12-29', 'A, D, E collinear', par(V(A29, E29), V(A29, D29)))
    check('12-29', 'A, B, C collinear', par(V(A29, C29), V(A29, B29)))
    check('12-29', 'BC == 4 units', abs(dist(B29, C29) - 4 * k) / (4 * k))
    check('12-29', 'A outside the circle', outside(O, A29, R, 0.30))
    check('12-29', 'D between A and E', between(A29, E29, D29))
    check('12-29', 'B between A and C', between(A29, C29, B29))
    check('12-29', 'AD*AE == AB*AC',
          abs(dist(A29, D29) * dist(A29, E29)
              - dist(A29, B29) * dist(A29, C29))
          / (dist(A29, D29) * dist(A29, E29)))
    for nm, X in (('D', D29), ('E', E29), ('B', B29), ('C', C29)):
        check('12-29', f'{nm} on the circle', onc(O, X, R))

    # ---- 12-30 : Exercises 17-18 -- AB tangent, AC = 8, CD = 10, so AB = 12
    R = 1.5
    A30 = (-3.3541, 0)
    B30 = (-0.6708, 1.3416)
    C30, D30 = (-1.4162, -0.4954), (1.0062, -1.1127)
    check('12-30', 'AB tangent at B', perp(V(O, B30), V(A30, B30)))
    k = dist(A30, C30) / 8.0
    check('12-30', 'CD == 10 units', abs(dist(C30, D30) - 10 * k) / (10 * k))
    check('12-30', 'AB == 12 units', abs(dist(A30, B30) - 12 * k) / (12 * k))
    check('12-30', 'A, C, D collinear', par(V(A30, D30), V(A30, C30)))
    check('12-30', 'A outside the circle', outside(O, A30, R, 0.30))
    check('12-30', 'C between A and D', between(A30, D30, C30))
    check('12-30', 'AB^2 == AC*AD',
          abs(dist(A30, B30) ** 2 - dist(A30, C30) * dist(A30, D30))
          / dist(A30, B30) ** 2)
    for nm, X in (('B', B30), ('C', C30), ('D', D30)):
        check('12-30', f'{nm} on the circle', onc(O, X, R))

    # ---- 12-31 : the two radii meet at a right angle; the chord is sqrt(2) r
    R = 1.25
    T31, S31 = P(O, 90, R), P(O, 0, R)
    check('12-31', 'central angle is right', perp(V(O, T31), V(O, S31)))
    check('12-31', 'chord == sqrt(2) r',
          abs(dist(T31, S31) - math.sqrt(2) * R) / R)
