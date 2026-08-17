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

    # ---- 12-5 : every vertex is the midpoint of the arc it bisects.
    # Arc A(145) to B(-25), as the book draws it: 170 degrees, so OA and OB are
    # two RADII meeting at a shallow bend, not a chord that misses the centre.
    R = 1.5
    check('12-5', 'OA and OB are radii',
          max(onc(O, P(O, 145, R), R), onc(O, P(O, -25, R), R)))
    check('12-5', 'central angle AOB is the book\'s 170 degrees',
          abs((145 - (-25)) - 170))
    for tag, hi, mid, lo in [('C mid arc AB', 145, 60, -25),
                             ('D mid arc AC', 145, 102.5, 60),
                             ('E mid arc CB', 60, 17.5, -25),
                             ('F mid arc AD', 145, 123.75, 102.5),
                             ('G mid arc DC', 102.5, 81.25, 60),
                             ('H mid arc CE', 60, 38.75, 17.5),
                             ('I mid arc EB', 17.5, -3.75, -25)]:
        check('12-5', tag, abs((hi - mid) - (mid - lo)))
    check('12-5', 'eight-side path runs A..B',
          order(145, 123.75, 102.5, 81.25, 60, 38.75, 17.5, -3.75, -25))
    check('12-5', 'all nine vertices on the circle',
          max(onc(O, P(O, a, R), R) for a in
              (145, 123.75, 102.5, 81.25, 60, 38.75, 17.5, -3.75, -25)))
    # the nine labels must be far enough apart along the label circle to read
    # as separate points; at 170 degrees over eight gaps they are 21.25 apart,
    # which is what fixes the crowding Caleb saw at the old 146-degree span
    check('12-5', 'label spacing at least 15 degrees',
          max(0.0, 15.0 - min(
              a - b for a, b in zip(
                  (145, 123.75, 102.5, 81.25, 60, 38.75, 17.5, -3.75),
                  (123.75, 102.5, 81.25, 60, 38.75, 17.5, -3.75, -25)))))

    # ---- 12-6 : circumscribed corners are the tangent intersections
    R = 1.3
    A6, C6, B6 = P(O, 145, R), P(O, 60, R), P(O, -25, R)
    T = P(O, 102.5, R / math.cos(math.radians(42.5)))
    U = P(O, 17.5, R / math.cos(math.radians(42.5)))
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

    # ---- 12-8 : angle AOC is right, and angle AOB congruent to angle BOC.
    # The fan is TILTED (78 / 33 / -12) so no ray is axis-aligned, as the book
    # sets it -- axis-aligned rays made the right angle read as the frame.
    R = 1.25
    aA8, aB8, aC8 = 78, 33, -12                     # ray directions, from .tex
    arc_in, r_in = (33, 78), 0.36                   # inner arc, from .tex
    arc_out, r_out = (-12, 33), 0.60                # outer arc, from .tex
    A8, B8, C8 = P(O, aA8, R), P(O, aB8, R), P(O, aC8, R)
    check('12-8', 'angle AOC is right', perp(V(O, A8), V(O, C8)))
    check('12-8', 'angle AOB == angle BOC', abs((aA8 - aB8) - (aB8 - aC8)))
    check('12-8', 'no radius is axis-aligned',
          max(0.0, 5.0 - min(min(abs(a % 360 - q) for q in (0, 90, 180, 270, 360))
                             for a in (aA8, aB8, aC8))))
    # The two angle arcs must ABUT on ray OB, one naming each angle.  The fault
    # Caleb caught was an outer arc running OA -> OC, straight ACROSS ray OB,
    # so it named angle AOC and the pair read as nested rather than adjacent.
    check('12-8', 'inner arc runs exactly OB to OA',
          abs(arc_in[0] - aB8) + abs(arc_in[1] - aA8))
    check('12-8', 'outer arc runs exactly OC to OB',
          abs(arc_out[0] - aC8) + abs(arc_out[1] - aB8))
    for nm, (lo, hi) in (('inner', arc_in), ('outer', arc_out)):
        crossed = [a for a in (aA8, aB8, aC8) if lo < a < hi]
        check('12-8', f'{nm} arc crosses no ray', float(len(crossed)))
    # and they must be told apart by radius: the book's differ by about 60%
    check('12-8', 'arc radii clearly different',
          max(0.0, 0.40 - (r_out - r_in) / r_in))

    # ---- 12-9 : an IRREGULAR inscribed path, vertices on the circle and in
    #             order from A round to B
    R = 1.25
    verts = (152, 112, 78, 30, -8)
    check('12-9', 'path vertices on circle',
          max(onc(O, P(O, a, R), R) for a in verts))
    check('12-9', 'path runs A..B in order', order(*verts))
    steps = [verts[i] - verts[i + 1] for i in range(len(verts) - 1)]
    check('12-9', 'path is NOT regular',
          max(0.0, 3.0 - (max(steps) - min(steps))))   # spacing must vary
    # The sides must be long enough that the dashed path stands visibly INSIDE
    # the circle.  The old seven-side path sagged 0.017 r -- under a point on
    # the page -- so it printed on top of the circle as a doubled edge, which
    # is the defect Caleb reported.  Demand at least 0.05 r of sag.
    sag = min(R * (1 - math.cos(math.radians(s / 2.0))) for s in steps)
    check('12-9', 'inscribed path visibly inside the circle',
          max(0.0, 0.05 - sag / R))

    # ---- 12-10 : arcs AB and BC are adjacent, sharing only B; fan tilted
    check('12-10', 'B between A and C', order(82, 37, -8))
    check('12-10', 'no radius is axis-aligned',
          max(0.0, 5.0 - min(min(abs(a % 360 - q) for q in (0, 90, 180, 270, 360))
                             for a in (82, 37, -8))))

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

    # ---- 12-14 : the book's sector, NOT a right angle.  It opens 68 degrees,
    # tilted symmetric about the horizontal so neither bounding radius is
    # level; the interior rays are the same halvings 12-13 constructs, read as
    # fractions of the opening measured up from OA, and the SOLID ray sits at
    # 0.662 -- "a little greater than 5/8", which is what the text claims of L.
    R = 1.7
    a14, b14 = -34.0, 34.0
    span = b14 - a14
    ray = {f: a14 + f * span for f in (0.500, 0.625, 0.662, 0.750)}
    A14, B14 = P(O, a14, R), P(O, b14, R)
    check('12-14', 'sector opening is the book\'s 68 degrees', abs(span - 68.0))
    check('12-14', 'sector symmetric about the horizontal', abs(a14 + b14))
    check('12-14', 'no bounding radius is level',
          max(0.0, 5.0 - min(abs(a14), abs(b14))))
    check('12-14', 'A and B on the arc',
          max(onc(O, A14, R), onc(O, B14, R)))
    check('12-14', 'P on the arc', onc(O, P(O, ray[0.662], R), R))
    check('12-14', 'rays in order B, 3/4, P, 5/8, 1/2, A',
          order(b14, ray[0.750], ray[0.662], ray[0.625], ray[0.500], a14))
    check('12-14', 'arc AP a little greater than 5/8 of the sector',
          max(0.0, 0.625 - 0.662) + max(0.0, 0.662 - 0.700))
    # the l brace spans exactly arc AP, and the rays must stop SHORT of it --
    # they used to run clear through, so the crossings read as ticks on it
    # brace endpoints and radii as the .tex writes them (\XIIbrace{O}{\R+0.36}
    # {\rP}{\Alo}{0.14}, rays drawn out to \R+0.15)
    brace_from, brace_to = ray[0.662], a14
    brace_r, brace_amp, ray_end = R + 0.36, 0.14, R + 0.15
    check('12-14', 'brace spans exactly arc AP',
          abs(abs(brace_from - brace_to) - abs(ray[0.662] - a14)))
    # it must NOT span the whole sector, which is how it used to be drawn
    check('12-14', 'brace is shorter than the whole sector',
          max(0.0, 1.0 - (span - abs(brace_from - brace_to))))
    check('12-14', 'rays stop short of the brace',
          max(0.0, ray_end - (brace_r - brace_amp)))

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
    # The two angle arcs at B, restored 2026-08-17.  Both sweep the whole of
    # angle ABQ; chord BC falls strictly inside that sweep (asserted just
    # above as 'BQ outside angle ABC'), which is what lets the figure carry
    # angle ABC = angle ABQ - angle CBQ.
    #
    # The .tex cannot call atan2, so it lays the arcs out from the closed forms
    # "the ray from the point at angle p to the point at angle q runs at
    # (p+q)/2 - 90" and "the chord measures 2 r sin((p-q)/2)".  Those two
    # formulae are what the drawing actually depends on, so verify THEM against
    # the true geometry -- if either is wrong the arcs miss A and miss BQ.
    check('12-22', 'chord-direction formula gives the ray B->A',
          abs((0.5 * (180 + 110) - 90) - dirang(V(B22, A22))))
    check('12-22', 'chord-length formula gives |BA|',
          abs(2 * R * math.sin(math.radians(0.5 * (180 - 110)))
              - dist(B22, A22)) / dist(B22, A22))
    # outer radius is |BA| (so the outer arc springs from A itself); the inner
    # is 0.55 of it, far enough in to read as a separate arc
    check('12-22', 'arc radii clearly different', max(0.0, 0.30 - (1.0 - 0.55)))

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

    # ---- 12-28 : the BOOK's schematic cut, not Exercise 15's numbers.
    # Drawing AO:OB = 12:4 and CO:OD = 8:6 to scale let the student read the
    # answer off the page with a ruler, so Caleb asked for the plate's own
    # proportions back.  What the figure must still assert is the structure --
    # four points on the circle, two chords, one crossing strictly inside --
    # plus, positively, that the drawn ratios are NOT the quoted ones.
    R = 1.1
    A28, B28 = P(O, 198, R), P(O, 31, R)
    C28, D28 = P(O, 105, R), P(O, -18, R)
    X28 = cross(A28, B28, C28, D28)
    for nm, X in (('A', A28), ('B', B28), ('C', C28), ('D', D28)):
        check('12-28', f'{nm} on the circle', onc(O, X, R))
    check('12-28', 'crossing inside the circle', inside(O, X28, R, 0.05))
    check('12-28', 'O between A and B', between(A28, B28, X28))
    check('12-28', 'O between C and D', between(C28, D28, X28))
    # the two chords must genuinely cross, not merely meet near an endpoint
    check('12-28', 'chords properly cross',
          max(0.0, 0.15 - min(param(A28, B28, X28), 1 - param(A28, B28, X28),
                              param(C28, D28, X28), 1 - param(C28, D28, X28))))
    # ...and must NOT encode the answer: both drawn ratios stay clear of the
    # values Exercise 15 quotes (3 and 4/3).
    check('12-28', 'AO/OB is NOT the quoted 3',
          max(0.0, 0.05 - abs(dist(A28, X28) / dist(X28, B28) - 3.0) / 3.0))
    check('12-28', 'CO/OD is NOT the quoted 4/3',
          max(0.0, 0.05 - abs(dist(C28, X28) / dist(X28, D28) - 4.0 / 3.0)
              / (4.0 / 3.0)))

    # ---- 12-29 : the BOOK's schematic cut (plate p.225), not Exercise 16's
    # numbers.  A is DERIVED as the crossing of the two secants, so the two
    # collinearities are exact rather than plotted.
    R = 1.4
    D29, E29 = P(O, 186, R), P(O, 47, R)
    B29, C29 = P(O, 203, R), P(O, -21, R)
    A29 = cross(D29, E29, B29, C29)
    check('12-29', 'A, D, E collinear', par(V(A29, E29), V(A29, D29)))
    check('12-29', 'A, B, C collinear', par(V(A29, C29), V(A29, B29)))
    check('12-29', 'A outside the circle', outside(O, A29, R, 0.30))
    check('12-29', 'D between A and E', between(A29, E29, D29))
    check('12-29', 'B between A and C', between(A29, C29, B29))
    check('12-29', 'AD*AE == AB*AC',
          abs(dist(A29, D29) * dist(A29, E29)
              - dist(A29, B29) * dist(A29, C29))
          / (dist(A29, D29) * dist(A29, E29)))
    for nm, X in (('D', D29), ('E', E29), ('B', B29), ('C', C29)):
        check('12-29', f'{nm} on the circle', onc(O, X, R))
    # the lower secant must cut a LONG chord, not graze the circle -- B and C
    # landing together on the bottom arc was the defect Caleb reported
    check('12-29', 'chord BC spans most of the circle',
          max(0.0, 1.5 * R - dist(B29, C29)))
    # the chords DE and BC do NOT cross inside the circle, as on the plate
    check('12-29', 'chords DE and BC do not cross',
          1.0 if 0 < param(D29, E29, cross(D29, E29, B29, C29)) < 1
          and 0 < param(B29, C29, cross(D29, E29, B29, C29)) < 1 else 0.0)
    # A stays close in: the book keeps it about 0.6 r clear, not 1.5 diameters
    check('12-29', 'A close to the circle',
          max(0.0, (dist(O, A29) - R) / R - 1.0))
    # ...and the drawing must not encode Exercise 16's answer BC = 4 given
    # AD = 6, DE = 10, AB = 8: on those numbers BC/AB = 0.5.
    check('12-29', 'BC/AB is NOT the quoted 1/2',
          max(0.0, 0.05 - abs(dist(B29, C29) / dist(A29, B29) - 0.5) / 0.5))

    # ---- 12-30 : likewise schematic.  The two facts Exercises *17-18 lean on
    # ARE built in: AB tangent at B, and ACD a true diameter.
    R = 1.4
    OA30 = 2.59
    A30 = (-OA30, 0.0)
    C30, D30 = P(O, 180, R), P(O, 0, R)
    B30 = P(O, 180 - math.degrees(math.acos(R / OA30)), R)
    check('12-30', 'AB tangent at B', perp(V(O, B30), V(A30, B30)))
    check('12-30', 'CD is a diameter', par(V(C30, O), V(O, D30)))
    check('12-30', 'CD == 2r', abs(dist(C30, D30) - 2 * R) / (2 * R))
    check('12-30', 'A, C, D collinear', par(V(A30, D30), V(A30, C30)))
    check('12-30', 'A outside the circle', outside(O, A30, R, 0.30))
    check('12-30', 'C between A and D', between(A30, D30, C30))
    check('12-30', 'AB^2 == AC*AD',
          abs(dist(A30, B30) ** 2 - dist(A30, C30) * dist(A30, D30))
          / dist(A30, B30) ** 2)
    for nm, X in (('B', B30), ('C', C30), ('D', D30)):
        check('12-30', f'{nm} on the circle', onc(O, X, R))
    # ...and must not encode Exercise 18's numbers, AC = 8 with CD = 10.
    check('12-30', 'AC/CD is NOT the quoted 4/5',
          max(0.0, 0.05 - abs(dist(A30, C30) / dist(C30, D30) - 0.8) / 0.8))

    # ---- 12-31 : the two radii meet at a right angle; the chord is sqrt(2) r
    R = 1.25
    T31, S31 = P(O, 90, R), P(O, 0, R)
    check('12-31', 'central angle is right', perp(V(O, T31), V(O, S31)))
    check('12-31', 'chord == sqrt(2) r',
          abs(dist(T31, S31) - math.sqrt(2) * R) / R)
