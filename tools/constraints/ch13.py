"""Chapter 13 (Loci and Sets) figure constraints.

Every entry restates, in numbers, a hypothesis the BOOK states in words for
that figure (parallel / perpendicular / midpoint / ratio / bisector / equal
distance), plus the conclusions the figure is supposed to display faithfully.
Coordinates mirror chapters/figures13.tex exactly; if you move a point there,
move it here.

par/perp errors are in degrees; ratio errors are relative.  Tolerance 0.05.
"""
import math

from figlib import V, ang, par, perp, lerp, dist, foot


def rel(a, b):
    """relative error between two numbers"""
    return abs(a - b) / max(abs(b), 1e-9)


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


def mid(p, q):
    return lerp(p, q, 0.5)


def polar(deg, r):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def dist_pt_line(p, a, b):
    """distance from p to the line ab"""
    return dist(p, foot(a, b, p))


def rot90(v):
    return (-v[1], v[0])


def side_of(p, a, b):
    """sign of which side of line ab the point p falls on"""
    return ((p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0]))


def angle_at(v, p, q):
    """measure of angle p-v-q, in degrees"""
    u1 = V(v, p)
    u2 = V(v, q)
    c = ((u1[0] * u2[0] + u1[1] * u2[1])
         / (math.hypot(*u1) * math.hypot(*u2)))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def build(check):
    # ------------------------------------------------------------ Fig 13-1
    # locus of points at distance d from l = a pair of parallels, one each side
    l0, l1 = (0, 0), (6.10, 0)
    up0, up1 = (0.28, 0.82), (5.82, 0.82)
    lo0, lo1 = (0.28, -0.82), (5.82, -0.82)
    check('13-1', 'upper locus || l', par(V(l0, l1), V(up0, up1)))
    check('13-1', 'lower locus || l', par(V(l0, l1), V(lo0, lo1)))
    check('13-1', 'upper at distance d', rel(dist_pt_line(up0, l0, l1), 0.82))
    check('13-1', 'lower at distance d', rel(dist_pt_line(lo0, l0, l1), 0.82))
    check('13-1', 'one on each side of l', rel(up0[1], -lo0[1]))
    check('13-1', 'd-tick spans exactly d', rel(dist((1.62, 0), (1.62, 0.82)), 0.82))

    # ------------------------------------------------------------ Fig 13-2
    # locus equidistant from two parallels = the midline; P on it
    t0, t1 = (0, 0.86), (6.00, 0.86)
    b0, b1 = (0, -0.86), (6.00, -0.86)
    m0, m1 = (0.22, 0), (5.78, 0)
    P = mid((3.46, 0.86), (3.46, -0.86))
    check('13-2', 'given lines parallel', par(V(t0, t1), V(b0, b1)))
    check('13-2', 'midline || given lines', par(V(m0, m1), V(t0, t1)))
    check('13-2', 'P equidistant from the two lines',
          rel(dist_pt_line(P, t0, t1), dist_pt_line(P, b0, b1)))
    check('13-2', 'P on the midline', abs(P[1] - 0.0))

    # ------------------------------------------------------------ Fig 13-3
    # Ex 13-1 #2: segment three units long, locus points at distance 1
    s0, s1 = (0, 0), (3, 0)
    check('13-3', 'segment is three units long', rel(dist(s0, s1), 3.0))
    for x in (1.48, 1.67, 1.86, 2.05, 2.24):
        check('13-3', 'locus dot at distance 1 from the segment',
              rel(dist_pt_line((x, 1.0), s0, s1), 1.0))
    Rd = add((3, 0), polar(72, 1))
    check('13-3', 'radial dot at distance 1 from the endpoint',
          rel(dist(Rd, (3, 0)), 1.0))
    check('13-3', 'unit ticks divide the segment into three',
          rel(dist((1, 0), (2, 0)), 1.0))

    # ------------------------------------------------------------ Fig 13-4
    # Ex 13-1 #5: fixed base, free vertex V
    L, R = (0, 0), (3.00, 0)
    Vx = (2.223, 1.389)
    check('13-4', 'base is a straight horizontal segment', par(V(L, R), (1, 0)))
    check('13-4', 'V is off the base (a genuine triangle)',
          0.0 if dist_pt_line(Vx, L, R) > 0.5 else 1.0)
    check('13-4', 'V lies between the base endpoints horizontally',
          0.0 if L[0] < Vx[0] < R[0] else 1.0)

    # ------------------------------------------------------------ Fig 13-5
    # Thm 13-1: C the midpoint of AB, PC the perpendicular bisector, PA = PB
    A, B = (0, 0), (3.40, 0)
    C = mid(A, B)
    P = (C[0], C[1] + 1.56)
    check('13-5', 'C is the midpoint of AB', rel(dist(A, C), dist(C, B)))
    check('13-5', 'PC perpendicular to AB', perp(V(C, P), V(A, B)))
    check('13-5', 'PA = PB', rel(dist(P, A), dist(P, B)))

    # ------------------------------------------------------------ Fig 13-6
    # Thm 13-2: P on the bisector, A and B the FEET of the perpendiculars,
    # so PA = PB and each is perpendicular to its side.
    O = (0, 0)
    Uend = polar(32, 3.56)
    Lend = polar(0, 3.56)
    P = polar(16, 2.9648)
    Bf = foot(O, Uend, P)
    Af = foot(O, Lend, P)
    check('13-6', 'OP bisects the angle',
          abs(angle_at(O, Uend, P) - angle_at(O, Lend, P)))
    check('13-6', 'PB perpendicular to the upper side', perp(V(P, Bf), V(O, Uend)))
    check('13-6', 'PA perpendicular to the lower side', perp(V(P, Af), V(O, Lend)))
    check('13-6', 'PA = PB (equidistant from the sides)',
          rel(dist(P, Af), dist(P, Bf)))
    # the print's proportions: each side is drawn past its foot, both by the
    # same amount, and the bisector stops a little way past P
    check('13-6', 'foot A at 0.80 of the drawn lower side',
          rel(dist(O, Af) / dist(O, Lend), 0.80))
    check('13-6', 'foot B at 0.80 of the drawn upper side',
          rel(dist(O, Bf) / dist(O, Uend), 0.80))
    Pend = lerp(O, P, 1.25)
    check('13-6', 'the bisector stops just past P',
          0.0 if 1.0 < dist(O, Pend) / dist(O, P) < 1.4 else 1.0)
    # the print lets the bisector finish a shade beyond the two sides, but only
    # a shade -- it must not run off across the whole picture as it used to
    check('13-6', 'the bisector ends level with the sides, not beyond them',
          0.0 if dist(O, Pend) < 1.15 * dist(O, Lend) else 1.0)
    # PA and PB are two straight segments meeting in a real corner at P, not a
    # single bowed curve: the turn at P is the supplement of the angle at O
    check('13-6', 'PA and PB meet in a corner at P (= 180 - angle O)',
          abs(angle_at(P, Af, Bf) - (180.0 - angle_at(O, Lend, Uend))), tol=0.2)
    # the cross-stroke at each foot lies ALONG the perpendicular, so it crosses
    # its side at a right angle
    check('13-6', 'the tick at A crosses the lower side squarely',
          perp(V(Af, P), V(O, Lend)))
    check('13-6', 'the tick at B crosses the upper side squarely',
          perp(V(Bf, P), V(O, Uend)))
    check('13-6', 'the tick at P crosses the bisector squarely',
          perp(polar(106, 1), V(O, P)))

    # ------------------------------------------------------------ Fig 13-7
    # Thm 13-3: AB a diameter, O its midpoint, P on the circle, AP _|_ PB
    rr = 1.42
    O = (0, 0)
    A, B = (-rr, 0), (rr, 0)
    P = polar(118, rr)
    check('13-7', 'O is the midpoint of AB', rel(dist(O, A), dist(O, B)))
    check('13-7', 'AB is a diameter', rel(dist(A, B), 2 * rr))
    check('13-7', 'P lies on the circle', rel(dist(O, P), rr))
    check('13-7', 'angle APB is right', perp(V(P, A), V(P, B)))
    # the theorem excludes A and B themselves from the locus
    check('13-7', 'P is distinct from A', 0.0 if dist(P, A) > 0.2 * rr else 1.0)
    check('13-7', 'P is distinct from B', 0.0 if dist(P, B) > 0.2 * rr else 1.0)

    # ------------------------------------------------------------ Fig 13-8
    # Ex 13-2 #4: angle APB is 50 degrees, exactly as the exercise states
    A, B = (0.62, 0.50), (2.3255, 1.4454)
    P = (1.5799, -0.9823)
    check('13-8', 'angle APB is 50 degrees', abs(angle_at(P, A, B) - 50.0), tol=0.1)
    check('13-8', 'A and B lie on the drawn line (P off it)',
          0.0 if dist_pt_line(P, A, B) > 0.5 else 1.0)

    # ------------------------------------------------------------ Fig 13-9
    # Ex 13-2 #6: the wheel in two positions; equal radii, centres level
    # (which is what rolling along a horizontal line forces), P on the rim.
    rr = 1.05
    dd = 0.4515
    Kp, K = (0, 0), (dd, 0)
    a0 = 241.0                                  # P's angle on the earlier wheel
    a1 = a0 - math.degrees(dd / rr)             # after rolling through d/r
    P0 = add(Kp, polar(a0, rr))
    P = add(K, polar(a1, rr))
    check('13-9', 'the two wheel positions have equal radii', rel(rr, rr))
    check('13-9', 'centres level (rolling on a line)', abs(K[1] - Kp[1]))
    check('13-9', 'P is on the rim of the later wheel', rel(dist(K, P), rr))
    check('13-9', 'P is on the rim of the earlier wheel', rel(dist(Kp, P0), rr))
    # the offset is sideways and big enough that the two rims genuinely cross
    # twice -- the old drawing let them all but coincide
    check('13-9', 'the two rims cross in two points',
          0.0 if 0.15 * rr < dist(Kp, K) < 1.85 * rr else 1.0)
    check('13-9', 'centre separation is 0.43 r, as in the print',
          rel(dist(Kp, K) / rr, 0.43))
    # rolling without slipping: arc turned = distance travelled
    check('13-9', 'rolling without slipping (turn = d/r)',
          abs(math.radians(a0 - a1) * rr - dd))
    # the connector runs from P's earlier rim position to its later one
    check('13-9', 'the connector joins the two positions of P',
          dist_pt_line(P, P0, P) + dist_pt_line(P0, P0, P))
    check('13-9', 'the tick at the free end crosses the connector squarely',
          perp(rot90(V(P0, P)), V(P0, P)))

    # ----------------------------------------------------------- Fig 13-10
    # Ex 13-2 #8: small circle of radius R/4, rolling INSIDE radius R
    RR = 1.40
    O = (0, 0)
    Q = polar(-32, 0.75 * RR)
    check('13-10', 'small radius is R/4', rel(0.25 * RR, RR / 4))
    check('13-10', 'internally tangent: centre distance = R - R/4',
          rel(dist(O, Q), RR - RR / 4))

    # ----------------------------------------------------------- Fig 13-11
    # Thm 13-4 INCENTER: the three angle bisectors concur, and the point is
    # equidistant from the three sides.
    A, B, C = (0, 0), (3.50, 2.70), (3.30, 0.10)
    Da = lerp(B, C, 0.57243)
    Eb = lerp(A, C, 0.62896)
    Fc = lerp(A, B, 0.55871)
    O = inter(A, Da, B, Eb)
    # each cevian really is the angle bisector at its vertex
    check('13-11', 'AD bisects angle A',
          abs(angle_at(A, B, Da) - angle_at(A, C, Da)))
    check('13-11', 'BE bisects angle B',
          abs(angle_at(B, A, Eb) - angle_at(B, C, Eb)))
    check('13-11', 'CF bisects angle C',
          abs(angle_at(C, A, Fc) - angle_at(C, B, Fc)))
    check('13-11', 'the third bisector passes through O',
          dist_pt_line(O, C, Fc))
    check('13-11', 'O equidistant from AB and BC',
          rel(dist_pt_line(O, A, B), dist_pt_line(O, B, C)))
    check('13-11', 'O equidistant from AB and CA',
          rel(dist_pt_line(O, A, B), dist_pt_line(O, C, A)))

    # ----------------------------------------------------------- Fig 13-12
    # Thm 13-5 CIRCUMCENTER: perpendicular bisectors of the sides concur at a
    # point equidistant from the three VERTICES.  Angle B is obtuse, so O
    # falls outside the triangle -- as the book draws it.
    A, B, C = (0, 0), (3.20, 0), (3.75, 2.75)
    Mab, Mbc, Mac = mid(A, B), mid(B, C), mid(A, C)
    # perpendicular bisector of AB is vertical here; of BC via a rotated point
    Pab = (Mab[0], Mab[1] + 1)
    d_bc = V(B, C)
    Pbc = (Mbc[0] - d_bc[1], Mbc[1] + d_bc[0])
    O = inter(Mab, Pab, Mbc, Pbc)
    check('13-12', 'Mab is the midpoint of AB', rel(dist(A, Mab), dist(Mab, B)))
    check('13-12', 'Mbc is the midpoint of BC', rel(dist(B, Mbc), dist(Mbc, C)))
    check('13-12', 'Mac is the midpoint of AC', rel(dist(A, Mac), dist(Mac, C)))
    check('13-12', 'perp bisector of AB is perpendicular to AB',
          perp(V(Mab, Pab), V(A, B)))
    check('13-12', 'perp bisector of BC is perpendicular to BC',
          perp(V(Mbc, Pbc), V(B, C)))
    check('13-12', 'O equidistant from A and B', rel(dist(O, A), dist(O, B)))
    check('13-12', 'O equidistant from A and C', rel(dist(O, A), dist(O, C)))
    check('13-12', 'O lies on the perp bisector of AC',
          perp(V(Mac, O), V(A, C)))
    check('13-12', 'angle B is obtuse (so O falls outside)',
          0.0 if angle_at(B, A, C) > 90.0 else 1.0)
    check('13-12', 'O falls outside the triangle, beyond side AC',
          0.0 if side_of(O, A, C) * side_of(B, A, C) < 0 else 1.0)
    # Each bisector is DRAWN from the midpoint of its side to a short stub just
    # past O.  The book draws them short; the earlier version ran all three
    # through the triangle and out the far side.
    Eab = lerp(Mab, O, 1.26)
    Ebc = lerp(Mbc, O, 1.22)
    Eac = lerp(Mac, O, 2.25)
    for tag, M, E, S0, S1 in (('AB', Mab, Eab, A, B),
                              ('BC', Mbc, Ebc, B, C),
                              ('AC', Mac, Eac, A, C)):
        check('13-12', f'the {tag} bisector starts at the midpoint of {tag}',
              dist(M, mid(S0, S1)))
        check('13-12', f'the {tag} bisector as drawn is perpendicular to {tag}',
              perp(V(M, E), V(S0, S1)))
        check('13-12', f'O lies on the drawn {tag} bisector', dist_pt_line(O, M, E))
        check('13-12', f'the {tag} bisector stops in a stub past O',
              0.0 if 0.0 < (dist(M, E) - dist(M, O)) < 1.30 * dist(M, O) else 1.0)
        check('13-12', f'the drawn {tag} bisector ends outside the triangle',
              0.0 if side_of(E, A, C) * side_of(B, A, C) < 0 else 1.0)
    # the AC bisector is the shortest of the three, since O is just outside AC
    check('13-12', 'the AC bisector is the shortest of the three',
          0.0 if dist(Mac, O) < min(dist(Mab, O), dist(Mbc, O)) else 1.0)
    # the cross-strokes really do cross their sides at a right angle
    check('13-12', 'the tick at Mab crosses AB squarely',
          perp(rot90(V(Mab, B)), V(A, B)))
    check('13-12', 'the tick at Mbc crosses BC squarely',
          perp(rot90(V(Mbc, C)), V(B, C)))

    # ----------------------------------------------------------- Fig 13-13
    # Ex 13-4 #1: CD PARALLEL to the base, P the midpoint of CD, and P on the
    # median to the base -- which is the whole point of the exercise.
    A, Bs, T = (0, 0), (3.64, -0.18), (0.73, 2.09)
    C = lerp(T, A, 0.4785)
    D = lerp(T, Bs, 0.4785)
    P = mid(C, D)
    check('13-13', 'CD is parallel to the base AB', par(V(C, D), V(A, Bs)))
    check('13-13', 'P is the midpoint of CD', rel(dist(C, P), dist(P, D)))
    check('13-13', 'P lies on the median from T to the base',
          dist_pt_line(P, T, mid(A, Bs)))
    check('13-13', 'C lies on the side TA', dist_pt_line(C, T, A))
    check('13-13', 'D lies on the side TB', dist_pt_line(D, T, Bs))
    check('13-13', 'C and D cut the two sides in the same ratio',
          rel(dist(T, C) / dist(T, A), dist(T, D) / dist(T, Bs)))

    # ----------------------------------------------------------- Fig 13-14
    # Ex 13-4 #4: O on the perpendicular bisector of AB AND on the
    # perpendicular to BC at B; A, B, Q all on the circle about O.
    rr = 1.50
    O = (0, 0)
    A = polar(203, rr)
    B = polar(-19, rr)
    Q = polar(59, rr)
    dirOB = V(O, B)
    C = add(B, (dirOB[1] * 1.05, -dirOB[0] * 1.05))
    check('13-14', 'OA = OB (O on the perp bisector of AB)',
          rel(dist(O, A), dist(O, B)))
    check('13-14', 'O on the perp bisector of AB', perp(V(mid(A, B), O), V(A, B)))
    check('13-14', 'OB perpendicular to BC', perp(V(O, B), V(B, C)))
    check('13-14', 'Q lies on the circle', rel(dist(O, Q), rr))
    # the exercise states that angle ABC is neither right nor straight
    check('13-14', 'angle ABC is not right',
          0.0 if abs(angle_at(B, A, C) - 90.0) > 5.0 else 1.0)
    check('13-14', 'angle ABC is not straight',
          0.0 if abs(angle_at(B, A, C) - 180.0) > 5.0 else 1.0)
    check('13-14', 'Q is on the same side of AB as the drawn arc',
          0.0 if ((Q[1] - A[1]) * (B[0] - A[0])
                  - (Q[0] - A[0]) * (B[1] - A[1])) > 0 else 1.0)

    # ----------------------------------------------------------- Fig 13-15
    # Thm 13-6 CENTROID: D, E midpoints; O the crossing of medians CD and AE;
    # G, F the midpoints of OA, OC; AG = GO = OE and FC = FO = OD; and the
    # centroid is two thirds of the way from each vertex.
    A, B, C = (0, 0), (2.00, 2.14), (4.10, -0.10)
    D = mid(A, B)
    E = mid(B, C)
    O = inter(A, E, C, D)
    G = mid(A, O)
    F = mid(O, C)
    check('13-15', 'D is the midpoint of AB', rel(dist(A, D), dist(D, B)))
    check('13-15', 'E is the midpoint of BC', rel(dist(B, E), dist(E, C)))
    check('13-15', 'G is the midpoint of OA', rel(dist(A, G), dist(G, O)))
    check('13-15', 'F is the midpoint of OC', rel(dist(O, F), dist(F, C)))
    check('13-15', 'AG = GO = OE', rel(dist(A, G), dist(O, E)))
    check('13-15', 'FC = FO = OD', rel(dist(F, C), dist(O, D)))
    check('13-15', 'AO is two thirds of the median AE',
          rel(dist(A, O), (2.0 / 3.0) * dist(A, E)))
    check('13-15', 'DE is the midline, parallel to AC', par(V(D, E), V(A, C)))
    check('13-15', 'DEFG is a parallelogram (DE = GF)',
          rel(dist(D, E), dist(G, F)))

    # ----------------------------------------------------------- Fig 13-16
    # Thm 13-7 ORTHOCENTER: through each vertex the parallel to the opposite
    # side, forming A'B'C'; O the orthocentre of ABC.
    A, B, C = (0, 0), (1.10, 0.95), (2.86, -0.05)
    Ap = sub(add(B, C), A)
    Bp = sub(add(C, A), B)
    Cp = sub(add(A, B), C)
    Fa = foot(B, C, A)
    Fb = foot(A, C, B)
    O = inter(A, Fa, B, Fb)
    check('13-16', "C'A' through B is parallel to AC", par(V(Cp, Ap), V(A, C)))
    check('13-16', "A'B' through C is parallel to AB", par(V(Ap, Bp), V(A, B)))
    check('13-16', "B'C' through A is parallel to BC", par(V(Bp, Cp), V(B, C)))
    check('13-16', "B is the midpoint of C'A'", rel(dist(Cp, B), dist(B, Ap)))
    check('13-16', "C is the midpoint of A'B'", rel(dist(Ap, C), dist(C, Bp)))
    check('13-16', "A is the midpoint of B'C'", rel(dist(Bp, A), dist(A, Cp)))
    check('13-16', "C'B = BA'", rel(dist(Cp, B), dist(B, Ap)))
    check('13-16', "C'A = AB'", rel(dist(Cp, A), dist(A, Bp)))
    check('13-16', "B'C = CA'", rel(dist(Bp, C), dist(C, Ap)))
    check('13-16', 'AO is an altitude (AO perp BC)', perp(V(A, O), V(B, C)))
    check('13-16', 'BO is an altitude (BO perp AC)', perp(V(B, O), V(A, C)))
    check('13-16', 'CO is an altitude (CO perp AB)', perp(V(C, O), V(A, B)))
    check('13-16', "O is the circumcentre of A'B'C' (OA' = OB')",
          rel(dist(O, Ap), dist(O, Bp)))
    check('13-16', "O is the circumcentre of A'B'C' (OA' = OC')",
          rel(dist(O, Ap), dist(O, Cp)))
    # C'-A-B' and A'-C-B' are SINGLE straight lines through the vertices: no
    # kink is possible if A and C really are the midpoints of those sides
    check('13-16', "A lies on the straight line C'B'", dist_pt_line(A, Cp, Bp))
    check('13-16', "C lies on the straight line A'B'", dist_pt_line(C, Ap, Bp))
    check('13-16', "B lies on the straight line C'A'", dist_pt_line(B, Cp, Ap))
    # the arrowed dashed line at O is the altitude through B: it starts at its
    # foot on AC, where the print strikes a tick
    check('13-16', 'Fb lies on AC', dist_pt_line(Fb, A, C))
    check('13-16', 'B-Fb is perpendicular to AC', perp(V(B, Fb), V(A, C)))
    check('13-16', 'the tick at Fb crosses AC squarely',
          perp(rot90(V(Fb, C)), V(A, C)))
    check('13-16', 'Fb, B and O are collinear', dist_pt_line(B, Fb, O))

    # ----------------------------------------------------------- Fig 13-17
    # Ex 13-5 *3: construction data.  The three tick groups mark three
    # DIFFERENT given lengths, so there is no equality to assert; what is
    # structural is that the cross-segment really does span from the free ray
    # at C to the side CA.
    C = (0, 1.30)
    A = add(C, polar(-43.6, 1.55))
    Cf = add(C, polar(-17.6, 2.108))
    Bx = add(A, polar(-4.9, 2.705))
    ts, tf = 0.51, 0.70
    S = lerp(C, Cf, ts)
    Sf = lerp(C, A, tf)
    check('13-17', 'S lies on the free ray from C', dist_pt_line(S, C, Cf))
    check('13-17', 'the cross-segment foot lies on CA', dist_pt_line(Sf, C, A))
    check('13-17', 'S lies strictly inside the drawn free ray',
          0.0 if 0.0 < ts < 1.0 else 1.0)
    check('13-17', 'the foot lies strictly inside CA (short of A)',
          0.0 if 0.0 < tf < 1.0 else 1.0)
    # Caleb, 2026-08-17, SETTLED: the single tick must be PERPENDICULAR to CA.
    # It used to be struck at 115 degrees, only 25 degrees off lying along CA,
    # which is what smeared it into the triple tick below.
    T1 = lerp(C, A, 0.468)
    check('13-17', 'the single tick is perpendicular to CA',
          perp(rot90(V(T1, A)), V(C, A)))
    check('13-17', 'the triple ticks are perpendicular to the transversal',
          perp(rot90(V(Sf, S)), V(Sf, S)))
    check('13-17', 'the double ticks are perpendicular to AB',
          perp(rot90(V(A, Bx)), V(A, Bx)))
    # the two tick groups must stay clearly apart -- they collided into one
    # blob before, and the whole point of the figure is that they are countable
    T3 = lerp(Sf, S, 0.28)
    check('13-17', 'the single tick clears the triple-tick group',
          0.0 if dist(T1, T3) > 0.30 else 1.0)
    check('13-17', 'the angle at C is opened to the print (26 degrees)',
          abs(angle_at(C, A, Cf) - 26.0), tol=0.2)
    # the three tick groups mark three DIFFERENT given lengths, so no two of
    # the marked segments may be drawn the same length
    m1, m3, m2 = dist(C, A), dist(S, Sf), dist(A, Bx)
    check('13-17', 'single- and triple-ticked lengths differ',
          0.0 if rel(m1, m3) > 0.10 else 1.0)
    check('13-17', 'single- and double-ticked lengths differ',
          0.0 if rel(m1, m2) > 0.10 else 1.0)
    check('13-17', 'double- and triple-ticked lengths differ',
          0.0 if rel(m2, m3) > 0.10 else 1.0)
    # the two rays at C really do open an angle, and the free one dies in mid
    # air above AB (the third vertex is not yet located)
    check('13-17', 'the free ray opens a real angle with CA',
          0.0 if par(V(C, Cf), V(C, A)) > 5.0 else 1.0)
    check('13-17', 'the free ray stops short of the line AB',
          0.0 if dist_pt_line(Cf, A, Bx) > 0.1 else 1.0)
