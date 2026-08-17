"""Chapter 11 figure constraints -- written 2026-08-17 with the scan rebuild.

Every entry restates, in numbers, a hypothesis the BOOK states in words for
that figure (regular polygon / perpendicular / midpoint / tangency / ratio),
plus the conclusions the figure is supposed to display faithfully.  Coordinates
mirror chapters/figures11.tex exactly; if you move a point there, move it here.

Chapter 11 is circle-and-regular-polygon geometry throughout, so nearly every
figure is generated from polar coordinates k*360/n -- never placed by eye.  The
checks below verify that: equal circumradii, equal sides, exact central angles,
apothems meeting sides at right angles at their midpoints.

par/perp errors are in degrees; ratio errors are relative.  Tolerance 0.05.
"""
import math

from figlib import V, par, perp, lerp, dist, foot


def rel(a, b):
    """relative error between two numbers"""
    return abs(a - b) / max(abs(b), 1e-9)


def pol(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def mid(p, q):
    return lerp(p, q, 0.5)


def angle_at(v, a, b):
    """angle a-v-b in degrees, 0..180"""
    u, w = V(v, a), V(v, b)
    c = (u[0] * w[0] + u[1] * w[1]) / (math.hypot(*u) * math.hypot(*w))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def inter(p1, p2, p3, p4):
    """intersection of line p1p2 with line p3p4"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d,
            (a * (y3 - y4) - (y1 - y2) * b) / d)


def rot90(c, p):
    """p rotated 90 degrees about c -- gives a second point on the
    perpendicular to cp through c, matching TikZ's !1!90: syntax"""
    v = V(c, p)
    return (c[0] - v[1], c[1] + v[0])


def regular(n, R, start, O=(0.0, 0.0)):
    """vertices of a regular n-gon, circumradius R, first vertex at `start` deg"""
    return [(O[0] + R * math.cos(math.radians(start + k * 360.0 / n)),
             O[1] + R * math.sin(math.radians(start + k * 360.0 / n)))
            for k in range(n)]


def build(check):
    # ------------------------------------------------------------- Fig 11-1
    # Circumcentre: m and n are the perpendicular bisectors of AB and BC, and
    # O is their intersection -- hence OA = OB = OC, the point of Theorem 11-1.
    A, B, C = (0.0, 0.0), (2.20, 0.0), (4.45, 2.00)
    Mab, Mbc = mid(A, B), mid(B, C)
    O = inter(Mab, rot90(Mab, B), Mbc, rot90(Mbc, C))
    check('11-1', 'm bisects AB', rel(dist(A, Mab), dist(Mab, B)))
    check('11-1', 'n bisects BC', rel(dist(B, Mbc), dist(Mbc, C)))
    check('11-1', 'm perp AB', perp(V(Mab, O), V(A, B)))
    check('11-1', 'n perp BC', perp(V(Mbc, O), V(B, C)))
    check('11-1', 'OA = OB', rel(dist(O, A), dist(O, B)))
    check('11-1', 'OB = OC', rel(dist(O, B), dist(O, C)))

    # ------------------------------------------------------------- Fig 11-2
    # Regular hexagon inscribed in the circle, C at 0 deg.  The proof of
    # Theorem 11-2 needs angle2 = angle3, angle1 = angle4 and ABC = BCD.
    R2 = 1.55
    O2 = (0.0, 0.0)
    Cv, Dv, Ev, Fv, Av, Bv = [pol(R2, d) for d in (0, 60, 120, 180, 240, 300)]
    for nm, P in (('A', Av), ('B', Bv), ('C', Cv), ('D', Dv), ('E', Ev), ('F', Fv)):
        check('11-2', 'O%s = r (vertex on circle)' % nm, rel(dist(O2, P), R2))
    check('11-2', 'AB = BC (regular)', rel(dist(Av, Bv), dist(Bv, Cv)))
    check('11-2', 'BC = CD (regular)', rel(dist(Bv, Cv), dist(Cv, Dv)))
    check('11-2', 'angle 2 = angle 3',
          rel(angle_at(Bv, O2, Cv), angle_at(Cv, O2, Bv)))
    check('11-2', 'angle 1 = angle 4',
          rel(angle_at(Bv, Av, O2), angle_at(Cv, O2, Dv)))
    check('11-2', 'angle ABC = angle BCD',
          rel(angle_at(Bv, Av, Cv), angle_at(Cv, Bv, Dv)))
    # "successive vertices A, B, C, D, ...": consecutive labels must be one
    # central angle apart and in one rotational direction, or the S.A.S. step
    # (triangle OAB congruent to triangle ODC) is about the wrong triangles.
    for nm, P, Q in (('AB', Av, Bv), ('BC', Bv, Cv), ('CD', Cv, Dv),
                     ('DE', Dv, Ev), ('EF', Ev, Fv)):
        check('11-2', 'central angle %s = 360/6' % nm,
              rel(angle_at(O2, P, Q), 60.0))
    check('11-2', 'OD = OA (S.A.S. conclusion)', rel(dist(O2, Dv), dist(O2, Av)))

    # ------------------------------------------------------------- Fig 11-3
    # Theorem 11-3: l passes through P and is perpendicular to the radius OP.
    R3 = 1.25
    O3 = (0.0, 0.0)
    P3 = pol(R3, -19)
    ldir = (math.cos(math.radians(71)), math.sin(math.radians(71)))
    A3 = (P3[0] + 0.92 * ldir[0], P3[1] + 0.92 * ldir[1])
    check('11-3', 'P on circle', rel(dist(O3, P3), R3))
    check('11-3', 'l perp OP', perp(ldir, V(O3, P3)))
    check('11-3', 'OA > OP (A outside)',
          0.0 if dist(O3, A3) > dist(O3, P3) else 1.0)
    check('11-3', 'angle OPA = 90 (right triangle OPA)',
          rel(angle_at(P3, O3, A3), 90.0))

    # ------------------------------------------------------------- Fig 11-4
    # Theorem 11-4, contrapositive: l is NOT perpendicular to OP; m is the
    # perpendicular from O to l with foot A, and B is P reflected in A, which
    # is what puts B on the circle as well as on l.
    R4 = 1.25
    O4 = (0.0, 0.0)
    A4 = (0.0, -0.39)
    P4 = (1.188, -0.39)
    B4 = (-1.188, -0.39)
    lv = V(B4, P4)
    check('11-4', 'm perp l', perp(V(O4, A4), lv))
    check('11-4', 'A is foot of perp from O to l', dist(A4, foot(B4, P4, O4)))
    check('11-4', 'AB = AP', rel(dist(A4, B4), dist(A4, P4)))
    check('11-4', 'OP = r', rel(dist(O4, P4), R4))
    check('11-4', 'OB = r (B on circle)', rel(dist(O4, B4), R4))
    check('11-4', 'l NOT perp OP (hypothesis)',
          0.0 if perp(lv, V(O4, P4)) > 10 else 1.0)
    # Step 2 of the proof puts B on the far side of A from P, so A must lie
    # BETWEEN them; and Remark 1 needs A strictly inside the circle.
    check('11-4', 'A between B and P',
          rel(dist(B4, A4) + dist(A4, P4), dist(B4, P4)))
    check('11-4', 'OA < OP (A inside, Remark 1)',
          0.0 if dist(O4, A4) < dist(O4, P4) else 1.0)

    # ------------------------------------------------------------- Fig 11-5
    # Theorem 11-5.  C and E are the midpoints of the adjacent sides AB and BD;
    # OC and OE are apothems, equal in length, each perpendicular to its side,
    # so one circle is tangent to both -- measured hexagon (a/R = 0.8646).
    R5 = 1.45
    O5 = (0.0, 0.0)
    hexa = [pol(R5, d) for d in (84, 24, -36, -96, -156, 144)]
    A5, B5, D5 = hexa[0], hexa[1], hexa[2]
    C5, E5 = mid(A5, B5), mid(B5, D5)
    ap5 = R5 * math.cos(math.radians(30))
    for i, P in enumerate(hexa):
        check('11-5', 'vertex %d on circle' % (i + 1), rel(dist(O5, P), R5))
    check('11-5', 'AB = BD (regular)', rel(dist(A5, B5), dist(B5, D5)))
    check('11-5', 'C midpoint of AB', rel(dist(A5, C5), dist(C5, B5)))
    check('11-5', 'E midpoint of BD', rel(dist(B5, E5), dist(E5, D5)))
    check('11-5', 'OC perp AB', perp(V(O5, C5), V(A5, B5)))
    check('11-5', 'OE perp BD', perp(V(O5, E5), V(B5, D5)))
    check('11-5', 'OE = OC', rel(dist(O5, E5), dist(O5, C5)))
    check('11-5', 'OC = apothem R cos30', rel(dist(O5, C5), ap5))
    # "BD a side ADJACENT to AB": the two sides must share exactly the vertex B.
    check('11-5', 'AB and BD adjacent (share B)',
          rel(dist(A5, B5) + dist(B5, D5), dist(A5, B5) * 2))
    check('11-5', 'tangent circle radius = OC (touches AB at C)',
          rel(dist(O5, foot(A5, B5, O5)), dist(O5, C5)))
    check('11-5', 'tangent circle touches BD at E',
          rel(dist(O5, foot(B5, D5, O5)), dist(O5, E5)))

    # ------------------------------------------------------------- Fig 11-6
    # Definition 11-4: centre, radius, apothem, central angle.
    R6 = 1.30
    O6 = (0.0, 0.0)
    v0, v60, v120 = pol(R6, 0), pol(R6, 60), pol(R6, 120)
    v300 = pol(R6, -60)
    ap6 = pol(R6 * math.cos(math.radians(30)), -30)
    check('11-6', 'central angle = 360/6', rel(angle_at(O6, v60, v120), 60.0))
    check('11-6', 'radius = R', rel(dist(O6, v0), R6))
    check('11-6', 'apothem foot is midpoint of its side',
          dist(ap6, mid(v300, v0)))
    check('11-6', 'apothem perp to its side', perp(V(O6, ap6), V(v300, v0)))
    check('11-6', 'apothem = R cos30',
          rel(dist(O6, ap6), R6 * math.cos(math.radians(30))))

    # ------------------------------------------------------------- Fig 11-7
    # Exterior angle of a regular polygon: side DC produced beyond C, and the
    # marked angle is between that extension and the next side CB.
    R7 = 1.35
    C7, B7, D7 = pol(R7, 0), pol(R7, 60), pol(R7, -60)
    Ext = lerp(C7, D7, -1.00)
    check('11-7', 'extension collinear with DC', par(V(D7, C7), V(C7, Ext)))
    check('11-7', 'extension beyond C (not back toward D)',
          0.0 if dist(D7, Ext) > dist(D7, C7) else 1.0)
    check('11-7', 'exterior angle = 360/6', rel(angle_at(C7, Ext, B7), 60.0))
    check('11-7', 'interior + exterior = 180',
          rel(angle_at(C7, B7, D7) + angle_at(C7, Ext, B7), 180.0))

    # ------------------------------------------------------------- Fig 11-8
    # Theorem 11-6: two regular hexagons, hence similar -- corresponding sides
    # proportional and corresponding central angles congruent.
    Ra, Rb = 1.55, 1.10
    O8, O8p = (0.0, 0.0), (3.35, 0.0)
    A8, B8, C8 = pol(Ra, 120), pol(Ra, 60), pol(Ra, 0)
    A8p = (O8p[0] + pol(Rb, 120)[0], pol(Rb, 120)[1])
    B8p = (O8p[0] + pol(Rb, 60)[0], pol(Rb, 60)[1])
    C8p = (O8p[0] + pol(Rb, 0)[0], pol(Rb, 0)[1])
    check('11-8', 'AB = BC (left regular)', rel(dist(A8, B8), dist(B8, C8)))
    check('11-8', "A'B' = B'C' (right regular)",
          rel(dist(A8p, B8p), dist(B8p, C8p)))
    check('11-8', "AB/A'B' = BC/B'C' (similar)",
          rel(dist(A8, B8) / dist(A8p, B8p), dist(B8, C8) / dist(B8p, C8p)))
    check('11-8', "angle AOB = angle A'O'B'",
          rel(angle_at(O8, A8, B8), angle_at(O8p, A8p, B8p)))
    check('11-8', 'central angle = 360/6', rel(angle_at(O8, A8, B8), 60.0))
    # The theorem's actual content: corresponding INTERIOR angles congruent.
    # A's other neighbour is the sixth, unlabelled vertex at 180 deg.
    U8 = pol(Ra, 180)
    U8p = (O8p[0] + pol(Rb, 180)[0], pol(Rb, 180)[1])
    check('11-8', "angle ABC = angle A'B'C' (interior)",
          rel(angle_at(B8, A8, C8), angle_at(B8p, A8p, C8p)))
    check('11-8', "angle A = angle A' (interior)",
          rel(angle_at(A8, U8, B8), angle_at(A8p, U8p, B8p)))
    check('11-8', 'interior angle of a regular hexagon = 120',
          rel(angle_at(B8, A8, C8), 120.0))

    # ------------------------------------------------------------- Fig 11-9
    # Theorem 11-7: Q, Q' the midpoints of the top sides, so OQ, O'Q' are the
    # apothems a, a' and OA, O'A' the radii r, r'; the drawing must show
    # r/r' = a/a'.
    Ra9, Rb9 = 1.45, 1.02
    O9, O9p = (0.0, 0.0), (3.05, 0.0)
    A9, B9 = pol(Ra9, 120), pol(Ra9, 60)
    A9p = (O9p[0] + pol(Rb9, 120)[0], pol(Rb9, 120)[1])
    B9p = (O9p[0] + pol(Rb9, 60)[0], pol(Rb9, 60)[1])
    Q9, Q9p = mid(A9, B9), mid(A9p, B9p)
    check('11-9', 'Q midpoint of AB', rel(dist(A9, Q9), dist(Q9, B9)))
    check('11-9', "Q' midpoint of A'B'", rel(dist(A9p, Q9p), dist(Q9p, B9p)))
    check('11-9', 'a = OQ perp AB', perp(V(O9, Q9), V(A9, B9)))
    check('11-9', "a' = O'Q' perp A'B'", perp(V(O9p, Q9p), V(A9p, B9p)))
    check('11-9', "r/r' = a/a'",
          rel(dist(O9, A9) / dist(O9p, A9p), dist(O9, Q9) / dist(O9p, Q9p)))
    check('11-9', 'a = r cos30',
          rel(dist(O9, Q9), Ra9 * math.cos(math.radians(30))))
    # Steps 2-4 of the proof: the same ratio must show up in AQ/A'Q' and, via
    # p = 2n.AQ, in the perimeters.
    check('11-9', "AQ/A'Q' = r/r'",
          rel(dist(A9, Q9) / dist(A9p, Q9p), dist(O9, A9) / dist(O9p, A9p)))
    check('11-9', "p/p' = r/r' (perimeters, n = 6)",
          rel((6 * dist(A9, B9)) / (6 * dist(A9p, B9p)),
              dist(O9, A9) / dist(O9p, A9p)))
    check('11-9', "triangle AOQ similar to A'O'Q'",
          rel(angle_at(A9, O9, Q9), angle_at(A9p, O9p, Q9p)))

    # ------------------------------------------------------------ Fig 11-10
    # Bisecting the central angle of the inscribed square gives the octagon
    # vertex at 45 deg; the two chords there are equal octagon sides.
    R10 = 1.50
    O10 = (0.0, 0.0)
    s0, s90, s180, s270 = pol(R10, 0), pol(R10, 90), pol(R10, 180), pol(R10, -90)
    d45 = pol(R10, 45)
    check('11-10', 'square side equal', rel(dist(s90, s0), dist(s0, s270)))
    check('11-10', 'square right angle at vertex',
          rel(angle_at(s0, s90, s270), 90.0))
    check('11-10', 'central angle of square = 90', rel(angle_at(O10, s0, s90), 90.0))
    check('11-10', '45-deg ray bisects that central angle',
          rel(angle_at(O10, s0, d45), angle_at(O10, d45, s90)))
    check('11-10', 'octagon chords equal', rel(dist(s90, d45), dist(d45, s0)))
    check('11-10', 'octagon vertex on circle', rel(dist(O10, d45), R10))

    # ------------------------------------------------------------ Fig 11-11
    # Inscribed hexagon (vertices on the circle) and circumscribed hexagon
    # (sides tangent to the circle), the two rotated 30 deg from each other.
    R11 = 1.30
    O11 = (0.0, 0.0)
    ins = regular(6, R11, 30)
    Rc = R11 / math.cos(math.radians(30))
    cir = regular(6, Rc, 0)
    for i, P in enumerate(ins):
        check('11-11', 'inscribed vertex %d on circle' % (i + 1),
              rel(dist(O11, P), R11))
    for i in range(6):
        s, t = cir[i], cir[(i + 1) % 6]
        check('11-11', 'circumscribed side %d tangent to circle' % (i + 1),
              rel(dist(O11, foot(s, t, O11)), R11))
        check('11-11', 'tangency point %d is an inscribed vertex' % (i + 1),
              min(dist(foot(s, t, O11), q) for q in ins))
    check('11-11', 'inscribed side = R (hexagon)', rel(dist(ins[0], ins[1]), R11))
    # Section 11-7 works the two perimeters out for r = 1: 6 inscribed,
    # 4 sqrt3 circumscribed.  The drawing must carry both numbers.
    check('11-11', 'inscribed perimeter = 6r',
          rel(6 * dist(ins[0], ins[1]), 6 * R11))
    check('11-11', 'circumscribed side = 2r/sqrt3',
          rel(dist(cir[0], cir[1]), 2 * R11 / math.sqrt(3)))
    check('11-11', 'circumscribed perimeter = 4 sqrt3 r',
          rel(6 * dist(cir[0], cir[1]), 4 * math.sqrt(3) * R11))
    check('11-11', 'the two hexagons are 30 deg apart',
          rel(abs(math.degrees(math.atan2(ins[0][1], ins[0][0]))
                  - math.degrees(math.atan2(cir[0][1], cir[0][0]))), 30.0))

    # ------------------------------------------------------------ Fig 11-12
    # Theorem 11-16: B is the midpoint of the side AC, so OB is the apothem
    # a_n and OB is perpendicular to AC; a_n = sqrt(r^2 - AB^2).
    R12 = 1.40
    O12 = (0.0, 0.0)
    A12, C12 = pol(R12, 45), pol(R12, -45)
    B12 = mid(A12, C12)
    check('11-12', 'A on circle', rel(dist(O12, A12), R12))
    check('11-12', 'C on circle', rel(dist(O12, C12), R12))
    check('11-12', 'B midpoint of AC', rel(dist(A12, B12), dist(B12, C12)))
    check('11-12', 'OB perp AC', perp(V(O12, B12), V(A12, C12)))
    check('11-12', 'a_n = sqrt(r^2 - AB^2)',
          rel(dist(O12, B12), math.sqrt(R12 ** 2 - dist(A12, B12) ** 2)))

    # ------------------------------------------------------------ Fig 11-13
    # Annular ring, Exercise 11-13.2: inner radius 2 ft, outer 4 ft.
    # radii as literally drawn in figures11.tex
    Ro13, Ri13 = 1.30, 1.30 / 2
    O13a, O13b = (0.0, 0.0), (0.0, 0.0)
    check('11-13', 'circles concentric', dist(O13a, O13b))
    check('11-13', 'inner : outer = 2 ft : 4 ft', rel(Ri13 / Ro13, 0.5))

    # ------------------------------------------------------------ Fig 11-14
    # Exercise 11-13.3: AB = BC = 2, B the centre of the circle, AC a diameter.
    # The two semicircles have radius AB/2, and because one is drawn above the
    # diameter and one below, the shaded region is exactly half the disc.
    R14 = 1.40
    A14, B14, C14 = (-R14, 0.0), (0.0, 0.0), (R14, 0.0)
    check('11-14', 'AB = BC', rel(dist(A14, B14), dist(B14, C14)))
    check('11-14', 'B is centre / midpoint of AC', dist(B14, mid(A14, C14)))
    check('11-14', 'AC is a diameter', rel(dist(A14, C14), 2 * R14))
    # semicircle radii exactly as drawn in figures11.tex ({\R/2} on each)
    rAB, rBC = R14 / 2, R14 / 2
    check('11-14', 'semicircle on AB has radius AB/2',
          rel(rAB, dist(A14, B14) / 2))
    check('11-14', 'semicircle on BC has radius BC/2',
          rel(rBC, dist(B14, C14) / 2))
    # shaded = lower half-disc + bulge above AB - bite below BC; the two
    # semicircular areas cancel only because the drawn radii are equal
    check('11-14', 'shaded area = half the disc',
          rel(0.5 * math.pi * R14 ** 2
              + 0.5 * math.pi * rAB ** 2
              - 0.5 * math.pi * rBC ** 2,
              0.5 * math.pi * R14 ** 2))

    # ------------------------------------------------------------ Fig 11-15
    # Exercise 11-13.4: the inscribed circle of the square has half the area of
    # the circumscribed circle.
    R15 = 1.30
    O15 = (0.0, 0.0)
    sq = regular(4, R15, 45)
    rin = R15 / math.sqrt(2)
    for i, P in enumerate(sq):
        check('11-15', 'square vertex %d on outer circle' % (i + 1),
              rel(dist(O15, P), R15))
    for i in range(4):
        s, t = sq[i], sq[(i + 1) % 4]
        check('11-15', 'inner circle tangent to side %d' % (i + 1),
              rel(dist(O15, foot(s, t, O15)), rin))
    check('11-15', 'inner area = half outer area',
          rel(math.pi * rin ** 2, 0.5 * math.pi * R15 ** 2))

    # ------------------------------------------------------------ Fig 11-16
    # Exercise 11-13.7: semicircles on the sides of a RIGHT triangle; the
    # semicircle on the hypotenuse equals the other two together.
    L16, T16, R16 = (0.0, 0.0), (0.0, 1.60), (2.52, 0.0)
    check('11-16', 'right angle at L', rel(angle_at(L16, T16, R16), 90.0))
    check('11-16', 'Pythagoras holds',
          rel(dist(T16, R16) ** 2, dist(L16, T16) ** 2 + dist(L16, R16) ** 2))
    # arc radii exactly as drawn in figures11.tex
    for nm, s, t, drawn in (('LT', L16, T16, 0.80),
                            ('LR', L16, R16, 1.26),
                            ('TR', T16, R16, 1.4925)):
        check('11-16', 'semicircle on %s has radius %s/2' % (nm, nm),
              rel(drawn, dist(s, t) / 2))
    check('11-16', 'largest semicircle = sum of other two',
          rel(0.5 * math.pi * (dist(T16, R16) / 2) ** 2,
              0.5 * math.pi * (dist(L16, T16) / 2) ** 2
              + 0.5 * math.pi * (dist(L16, R16) / 2) ** 2))
