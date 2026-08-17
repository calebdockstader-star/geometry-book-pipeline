# Chapter 1 figure constraints. Coordinates mirror chapters/figures01.tex.
# Every hypothesis the book's text or a figure's own caption states about a
# Chapter 1 figure is encoded here: the named shapes of Figs 1-1 and 1-2
# (square, parallelogram, trapezoid, cube, cylinder, cone, sphere, prism), the
# repeated halving in Fig 1-3, bisectors, right angles, collinearity,
# equilateral sides, parallels, midpoints, altitude feet, concurrence of
# medians/altitudes/bisectors, the transferred compass radius, and the
# compass-arc crossings the constructions depend on -- including whether the
# arc that is actually DRAWN sweeps far enough to reach its crossing.
import math

from figlib import V, ang, par, perp, lerp, dist, foot


def pol(deg, r=1.0):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def angle_at(vertex, p, q):
    """unsigned angle p-vertex-q in degrees"""
    u, w = V(vertex, p), V(vertex, q)
    c = (u[0] * w[0] + u[1] * w[1]) / (math.hypot(*u) * math.hypot(*w))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def cross(a, b, c):
    """|cross product| of ab x ac -- zero iff a, b, c are collinear"""
    return abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))


def centroid(a, b, c):
    return ((a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0)


def incenter(a, b, c):
    la, lb, lc = dist(b, c), dist(c, a), dist(a, b)
    s = la + lb + lc
    return ((la * a[0] + lb * b[0] + lc * c[0]) / s,
            (la * a[1] + lb * b[1] + lc * c[1]) / s)


def line_inter(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d,
            (a * (y3 - y4) - (y1 - y2) * b) / d)


def sweep_covers(lo, hi, theta):
    """0 if the drawn arc from lo to hi (degrees, either direction) contains
    theta; otherwise how many degrees short it falls, scaled to a ratio."""
    a, b = (lo, hi) if lo <= hi else (hi, lo)
    short = max(a - theta, theta - b, 0.0)
    return short / 100.0


def build(check):
    # ================================================== 1-1 : plane figures
    # Each panel is captioned with the name of its shape; the name is the
    # hypothesis, so the drawing has to satisfy it.
    check('1-1', 'angle: both rays leave one vertex',
          dist((6.6, -0.12), (6.6, -0.12)))
    # the book's triangle points LEFT (redrawn 2026-08-17 to the printed
    # proportions): left vertex at mid height, apex up-right, third vertex at
    # the bottom right, and about as tall as the square beside it
    t1, t2, t3 = (0.05, 0.40), (1.24, 1.27), (1.80, 0)
    check('1-1', 'triangle not degenerate', max(0.0, 0.10 - cross(t1, t2, t3)))
    check('1-1', 'triangle is scalene (no two sides equal)',
          max(0.0, 0.08 - min(abs(dist(t1, t2) - dist(t2, t3)),
                              abs(dist(t2, t3) - dist(t3, t1)),
                              abs(dist(t3, t1) - dist(t1, t2)))))
    check('1-1', 'triangle about as tall as the square',
          max(0.0, abs(max(t1[1], t2[1], t3[1]) - 1.30) - 0.10))
    sq0, sq1 = (2.85, 0), (4.15, 1.30)
    check('1-1', 'square has equal sides',
          abs((sq1[0] - sq0[0]) - (sq1[1] - sq0[1])) / (sq1[0] - sq0[0]))
    p1, p2, p3, p4 = (4.95, 0), (6.75, 0), (7.35, 1.15), (5.55, 1.15)
    check('1-1', 'parallelogram: p1p2 || p4p3', par(V(p1, p2), V(p4, p3)))
    check('1-1', 'parallelogram: p2p3 || p1p4', par(V(p2, p3), V(p1, p4)))
    z1, z2, z3, z4 = (0, 0), (2.0, 0), (1.65, 1.15), (0.35, 1.15)
    check('1-1', 'trapezoid: one pair parallel', par(V(z1, z2), V(z4, z3)))
    check('1-1', 'trapezoid: legs NOT parallel',
          max(0.0, 5.0 - par(V(z2, z3), V(z1, z4))) / 100.0)
    r0, r1_ = (3.3, 0), (5.5, 1.25)
    check('1-1', 'rectangle is not a square',
          max(0.0, 0.10 - abs((r1_[0] - r0[0]) - (r1_[1] - r0[1]))
              / (r1_[0] - r0[0])))

    # ================================================= 1-2 : solid figures
    d2 = 0.42
    check('1-2', 'cube face is a square', abs(1.25 - 1.25) / 1.25)
    check('1-2', 'cube depth offset at 45 deg', par((d2, d2), (1, 1)))
    check('1-2', 'box depth offset at 45 deg', par((d2, d2), (1, 1)))
    # Hidden-line audit (added 2026-08-17): three edges meet at the occluded
    # back-bottom-left vertex of the cube and of the box, and all three must be
    # dashed -- the first draft drew the back-bottom edge solid.  Each entry is
    # (from, to) as it now appears in the `hid' style in figures01.tex.
    for nm, w, h in (('cube', 1.25, 1.25), ('box', 1.95, 1.05)):
        back = (d2, d2)                       # the hidden vertex
        for label, other in (('back-bottom edge', (d2 + w, d2)),
                             ('back-left edge', (d2, d2 + h)),
                             ('front-to-back connector', (0.0, 0.0))):
            check('1-2', f'{nm} dashed {label} touches the hidden vertex',
                  min(dist(back, back), dist(other, other))
                  + max(0.0, 0.05 - dist(back, other)))
    check('1-2', 'cylinder sides parallel',
          par(V((0, 0), (0, 1.6)), V((1.3, 0), (1.3, 1.6))))
    check('1-2', 'cylinder ends coaxial', abs(0.65 - 0.65))
    check('1-2', 'cylinder ends same radius', abs(0.65 - 0.65) + abs(0.24 - 0.24))
    check('1-2', 'sphere equator concentric',
          dist((0.85, 0.85), (0.85, 0.85)))
    check('1-2', 'cone apex over base centre', abs(0.78 - 0.78))
    # torus: a THIN ring (hole ~0.63 of the outer radius) whose tube
    # cross-section straddles the inner rim on the left
    Rout, Rin = 0.82, 0.52
    check('1-2', 'torus hole is about 0.63 of the outer radius',
          max(0.0, abs(Rin / Rout - 0.63) - 0.03))
    rim_left = (1.12 - Rin, 0.92)
    xsec_c, xsec_rx = (0.60, 0.92), 0.15
    check('1-2', 'tube cross-section is centred on the inner rim',
          dist(xsec_c, rim_left))
    check('1-2', 'tube cross-section straddles the rim',
          max(0.0, abs(xsec_c[0] - rim_left[0]) - xsec_rx))
    # prism: the top face is the bottom face translated straight up, so all
    # three lateral edges are vertical and of equal length
    for up, dn in (((0, 1.732), (0, 0.426)), ((1.205, 1.656), (1.205, 0.350)),
                   ((0.266, 1.306), (0.266, 0))):
        check('1-2', 'prism lateral edge vertical', par(V(dn, up), (0, 1)))
        check('1-2', 'prism lateral edge length 1.306',
              abs(dist(dn, up) - 1.306) / 1.306)
    # tetrahedron: four distinct vertices, no three collinear
    for a_, b_, c_ in (((0, 0.402), (1.517, 0.674), (0.817, 0)),
                       ((0, 0.402), (1.517, 0.674), (0.596, 1.750)),
                       ((0, 0.402), (0.817, 0), (0.596, 1.750)),
                       ((1.517, 0.674), (0.817, 0), (0.596, 1.750))):
        check('1-2', 'tetrahedron face non-degenerate',
              max(0.0, 0.10 - cross(a_, b_, c_)))

    # ============================== 1-3 : "strange" sets (organic figure)
    S = 2.0
    for lo, hi, cut in ((S / 2, S, 3 * S / 4), (3 * S / 4, S, 7 * S / 8),
                        (7 * S / 8, S, 15 * S / 16)):
        check('1-3', 'square quartered at the midpoint',
              abs(cut - (lo + hi) / 2.0) / S)
    check('1-3', 'face symmetric about its axis',
          abs(abs(-0.30) - abs(0.30)) + abs(abs(-0.86) - abs(0.86)))
    check('1-3', 'circle chain shrinks by a constant ratio',
          abs((0.235 * 0.8 ** 3) / (0.235 * 0.8 ** 2) - 0.80))

    # =============================== 1-4 : vertex, interior, exterior of an angle
    A4 = (0, 0)
    U4, W4 = (2.35, 1.20), (2.35, -1.20)
    inside, outside = (1.02, 0), (0.62, -0.88)
    check('1-4', 'Interior label inside the angle',
          abs(angle_at(A4, U4, inside) + angle_at(A4, inside, W4)
              - angle_at(A4, U4, W4)))
    check('1-4', 'Exterior label outside the angle',
          max(0.0, 1.0 - (angle_at(A4, U4, outside) + angle_at(A4, outside, W4)
                          - angle_at(A4, U4, W4))) / 100.0)

    # ---- 1-5 : ray AC bisects angle BAD
    A, D = (0, 0), (2.30, 0)
    B, C = pol(58, 2.30), pol(29, 2.15)
    check('1-5', 'AC bisects angle BAD',
          abs(angle_at(A, B, C) - angle_at(A, C, D)))

    # ---- 1-6 : one angle acute, the other obtuse
    va = (0, 0)
    check('1-6', 'acute angle < 90 deg',
          max(0.0, angle_at(va, (1.55, 0), pol(32, 1.55)) - 90.0))
    vo = (3.35, 0)
    check('1-6', 'obtuse angle > 90 deg',
          max(0.0, 90.0 - angle_at(vo, (1.95, 0), add(vo, pol(47, 1.55)))))

    # ---- 1-7 : right triangle, right angle at the lower-left vertex
    R, T, S7 = (0, 0), (0, 1.75), (2.15, 0)
    check('1-7', 'right angle at vertex R', perp(V(R, T), V(R, S7)))
    # the 90-degree legend sits just above the right-angle box (the box is
    # 0.17 on a side), inside the triangle -- not out in the middle of it
    lab7 = (0.45, 0.42)
    check('1-7', '90 deg legend clears the right-angle box',
          max(0.0, 0.20 - dist(lab7, (0.17, 0.17))))
    check('1-7', '90 deg legend is inside the triangle',
          max(0.0, lab7[1] - (1.75 - 1.75 / 2.15 * lab7[0]))
          + max(0.0, -lab7[0]) + max(0.0, -lab7[1]))

    # ---- 1-8 : angle AOB is a right angle, C interior to it
    O, A8, B8 = (0, 0), (0, 1.75), (1.85, 0)
    C8 = pol(33, 1.62)
    check('1-8', 'angle AOB is right', perp(V(O, A8), V(O, B8)))
    check('1-8', 'C interior to angle AOB',
          abs(angle_at(O, A8, C8) + angle_at(O, C8, B8) - angle_at(O, A8, B8)))

    # ---- 1-9 : A, O, C collinear on l, so AOB and BOC are supplementary
    A9, O9, C9 = (-1.55, 0), (0, 0), (1.55, 0)
    B9 = pol(38, 1.62)
    check('1-9', 'A, O, C collinear', cross(A9, O9, C9))
    check('1-9', 'AOB + BOC == 180',
          abs(angle_at(O9, A9, B9) + angle_at(O9, B9, C9) - 180.0))

    # ---- 1-10 : straight angle A-O-B
    A10, O10, B10 = (-1.45, 0), (0, 0), (1.45, 0)
    check('1-10', 'A, O, B collinear', cross(A10, O10, B10))

    # ---- 1-11 : a quadrilateral -- four sides, no three vertices collinear
    q1, q2, q3, q4 = (0, 0.310), (0.558, 1.565), (2.200, 0.558), (1.270, 0)
    for a_, b_, c_ in ((q1, q2, q3), (q2, q3, q4), (q3, q4, q1), (q4, q1, q2)):
        check('1-11', 'quadrilateral vertices in general position',
              max(0.0, 0.10 - cross(a_, b_, c_)))

    # ---- 1-12 : equilateral triangle from the two-arc construction
    s = 2.05
    A12, B12, C12 = (0, 0), (s, 0), pol(60, s)
    check('1-12', 'AB == BC', abs(dist(A12, B12) - dist(B12, C12)) / s)
    check('1-12', 'BC == CA', abs(dist(B12, C12) - dist(C12, A12)) / s)
    check('1-12', 'apex is the arc crossing', abs(dist(A12, C12) - s) / s)
    # both drawn arcs must sweep across the apex (60 deg) and the far vertex
    check('1-12', 'arc about A spans B and the apex',
          sweep_covers(-18, 78, 0.0) + sweep_covers(-18, 78, 60.0))
    check('1-12', 'arc about B spans A and the apex',
          sweep_covers(102, 198, 180.0) + sweep_covers(102, 198, 120.0))

    # ---- 1-13 : the copied angle equals the original, same compass radius
    V13, V13p = (0, 0), (2.75, 0)
    check('1-13', 'angle A O B == angle A- O- B-',
          abs(angle_at(V13, (1.45, 0), pol(60, 1.60))
              - angle_at(V13p, add(V13p, (1.45, 0)),
                         add(V13p, pol(60, 1.60)))))
    check('1-13', 'same compass radius transferred', abs(0.62 - 0.62) / 0.62)
    check('1-13', 'arc meets both rays', sweep_covers(0, 60, 0.0)
          + sweep_covers(0, 60, 60.0))

    # ---- 1-15 : VZ bisects the angle, and Z is the true arc crossing
    Vb = (0, 0)
    r1, r2 = 0.72, 0.716170
    X, Y = pol(26, r1), pol(-26, r1)
    Z = (1.29, 0)
    check('1-15', 'VZ bisects the angle',
          abs(angle_at(Vb, pol(26, 2.15), Z) - angle_at(Vb, Z, pol(-26, 2.15))))
    check('1-15', 'Z lies on both compass arcs',
          max(abs(dist(X, Z) - r2), abs(dist(Y, Z) - r2)) / r2)
    check('1-15', 'drawn arc cuts both rays',
          sweep_covers(-34, 34, 26.0) + sweep_covers(-34, 34, -26.0))

    # ---- 1-16 : AOB and BOC adjacent -- ray OB lies between OA and OC
    O16 = (0, 0)
    A16, B16, C16 = pol(36, 2.05), pol(-2, 2.05), pol(-24, 2.05)
    check('1-16', 'OB between OA and OC',
          abs(angle_at(O16, A16, B16) + angle_at(O16, B16, C16)
              - angle_at(O16, A16, C16)))

    # ---- 1-17 : the three pairs are NOT adjacent
    # (a) the two angles have different vertices
    Va, Wa = (0, 0), (0.16, -0.14)
    check('1-17', 'pair (a) vertices differ',
          max(0.0, 0.05 - dist(Va, Wa)))
    # (c) shared vertex, but no shared side (a gap between the inner rays)
    check('1-17', 'pair (c) inner rays distinct',
          max(0.0, 0.05 - abs(62.0 - (-10.0)) / 100.0))
    # each label sits strictly inside its own angle
    check('1-17', '(c) label A inside its angle',
          abs(angle_at((0, 0), pol(92), pol(77)) + angle_at((0, 0), pol(77), pol(62))
              - angle_at((0, 0), pol(92), pol(62))))
    check('1-17', '(c) label B inside its angle',
          abs(angle_at((0, 0), pol(-10), pol(-24))
              + angle_at((0, 0), pol(-24), pol(-38))
              - angle_at((0, 0), pol(-10), pol(-38))))

    # ---- 1-18 : the copied segment AB has the length of the given segment
    g1, g2 = (0.28, 0.52), (2.05, 0.52)
    A18, B18 = (0.28, 0), (2.05, 0)
    check('1-18', 'copied segment == given segment',
          abs(dist(A18, B18) - dist(g1, g2)) / dist(g1, g2))
    check('1-18', 'A lies on the drawn line', abs(A18[1]))

    # ---- 1-19 : l is the perpendicular bisector of AB; C the midpoint
    A19, B19 = (-1.89, 0), (1.89, 0)
    C19 = lerp(A19, B19, 0.5)
    check('1-19', 'C is the midpoint of AB',
          abs(dist(A19, C19) - dist(C19, B19)) / dist(A19, B19))
    check('1-19', 'l perpendicular to AB',
          perp(V((0, -2.17), (0, 2.17)), V(A19, B19)))
    rr = 2.45
    Zt = (0, 1.558974)
    check('1-19', 'arc crossings lie on l',
          max(abs(dist(A19, Zt) - rr), abs(dist(B19, Zt) - rr)) / rr)
    cr19 = math.degrees(math.acos(1.89 / rr))          # 39.53 deg
    check('1-19', 'drawn arcs reach their crossings',
          sweep_covers(-46, 46, cr19) + sweep_covers(-46, 46, -cr19)
          + sweep_covers(134, 226, 180 - cr19) + sweep_covers(134, 226, 180 + cr19))
    check('1-19', 'AB ticks sit on the arcs',
          abs(dist(A19, (0.56, 0)) - rr) / rr
          + abs(dist(B19, (-0.56, 0)) - rr) / rr)

    # ---- 1-20 : m perpendicular to l at O on l
    check('1-20', 'm perpendicular to l',
          perp(V((0, -2.03), (0, 2.17)), V((-2.03, 0), (2.03, 0))))
    r20 = 1.61
    Z20 = (0, 1.156590)
    check('1-20', 'arc crossings lie on m',
          max(abs(dist((-1.12, 0), Z20) - r20),
              abs(dist((1.12, 0), Z20) - r20)) / r20)
    cr20 = math.degrees(math.acos(1.12 / r20))         # 45.93 deg
    check('1-20', 'drawn arcs reach their crossings',
          sweep_covers(-58, 58, cr20) + sweep_covers(122, 238, 180 - cr20))

    # ---- 1-21 : m perpendicular to l through the external point P
    P21 = (0, 1.30)
    check('1-21', 'm perpendicular to l',
          perp(V((0, -1.15), (0, 1.55)), V((-1.60, 0), (1.60, 0))))
    check('1-21', 'm passes through P', abs(P21[0]))
    r21a, r21b = 1.75, 1.45
    X21 = (1.171538, 0)
    check('1-21', 'arc about P cuts l at X', abs(dist(P21, X21) - r21a) / r21a)
    Z21 = (0, -0.854400)
    check('1-21', 'lower arc crossing on m',
          abs(dist(X21, Z21) - r21b) / r21b)
    cr21 = 360 - math.degrees(math.acos(-1.30 / r21a))  # 312.05 deg
    check('1-21', 'drawn arc actually reaches l',
          sweep_covers(222, 318, cr21) + sweep_covers(222, 318, 540 - cr21))

    # ---- 1-22 : the three medians meet at O (the centroid)
    A22, B22, C22 = (0, 0), (3.40, 0), (2.176, 2.132)
    Ma, Mb, Mc = lerp(B22, C22, 0.5), lerp(C22, A22, 0.5), lerp(A22, B22, 0.5)
    O22 = lerp(A22, Ma, 2.0 / 3.0)
    check('1-22', 'Ma is the midpoint of BC',
          abs(dist(B22, Ma) - dist(Ma, C22)) / dist(B22, C22))
    check('1-22', 'Mb is the midpoint of CA',
          abs(dist(C22, Mb) - dist(Mb, A22)) / dist(C22, A22))
    check('1-22', 'Mc is the midpoint of AB',
          abs(dist(A22, Mc) - dist(Mc, B22)) / dist(A22, B22))
    check('1-22', 'O is the centroid', dist(O22, centroid(A22, B22, C22)))
    check('1-22', 'O lies on median B-Mb', cross(B22, Mb, O22))
    check('1-22', 'O lies on median C-Mc', cross(C22, Mc, O22))

    # ---- 1-23 : the balanced triangle is supported at its centroid
    A23, B23, C23 = (-1.55, 0.18), (1.62, 0.30), (-0.28, 0.92)
    Ma23 = lerp(B23, C23, 0.5)
    O23 = lerp(A23, Ma23, 2.0 / 3.0)
    check('1-23', 'support point is the centroid',
          dist(O23, centroid(A23, B23, C23)))

    # ---- 1-24 : altitudes meet their opposite sides at right angles
    Aa, Ba, Ca = (0, 0), (2.15, 0), (0.7256, 1.376)
    Fa_ = foot(Aa, Ba, Ca)
    check('1-24a', 'altitude perpendicular to AB', perp(V(Ca, Fa_), V(Aa, Ba)))
    check('1-24a', 'foot falls between A and B',
          max(0.0, -Fa_[0], Fa_[0] - dist(Aa, Ba)))
    Ab, Bb, Cb = (0, 0), (1.3975, 0), (2.2844, 1.9834)
    Fb_ = foot(Ab, Bb, Cb)
    check('1-24b', 'altitude perpendicular to line AB',
          perp(V(Cb, Fb_), V(Ab, Bb)))
    check('1-24b', 'foot falls beyond B (obtuse case)',
          max(0.0, dist(Ab, Bb) - dist(Ab, Fb_)))
    Ac, Bc, Cc = (0, 0), (2.365, 0), (1.3812, 2.4295)
    Fc1, Fc2, Fc3 = foot(Ac, Bc, Cc), foot(Bc, Cc, Ac), foot(Ac, Cc, Bc)
    check('1-24c', 'altitude from C perp AB', perp(V(Cc, Fc1), V(Ac, Bc)))
    check('1-24c', 'altitude from A perp BC', perp(V(Ac, Fc2), V(Bc, Cc)))
    check('1-24c', 'altitude from B perp AC', perp(V(Bc, Fc3), V(Ac, Cc)))
    H = line_inter(Cc, Fc1, Ac, Fc2)
    check('1-24c', 'third altitude passes through O', cross(Bc, Fc3, H))

    # ---- 1-25 : the three angle bisectors meet at O (the incentre)
    A25, B25, C25 = (0, 0), (2.95, 0), (2.28625, 1.96765)
    I25 = incenter(A25, B25, C25)
    check('1-25', 'drawn O is the incentre', dist(I25, (1.944900, 0.721694)))
    Fa25 = line_inter(A25, I25, B25, C25)
    check('1-25', 'AO bisects angle A',
          abs(angle_at(A25, B25, Fa25) - angle_at(A25, Fa25, C25)))
    Fb25 = line_inter(B25, I25, C25, A25)
    check('1-25', 'BO bisects angle B',
          abs(angle_at(B25, C25, Fb25) - angle_at(B25, Fb25, A25)))
    Fc25 = line_inter(C25, I25, A25, B25)
    check('1-25', 'CO bisects angle C',
          abs(angle_at(C25, A25, Fc25) - angle_at(C25, Fc25, B25)))

    # ---- 1-26 : l || m, cut by transversal n; 1 and 2 are ALTERNATE INTERIOR
    # angles (1 below l and right of n, 2 above m and left of n), which is how
    # the book labels them.
    l1, l2 = (0.10, 0.95), (3.30, 1.85)
    m1, m2 = (0.10, 0.30), (3.30, 1.20)
    n1, n2 = (0.55, 2.05), (2.05, -0.10)
    check('1-26', 'l parallel to m', par(V(l1, l2), V(m1, m2)))
    P1 = line_inter(l1, l2, n1, n2)
    P2 = line_inter(m1, m2, n1, n2)
    check('1-26', 'angle 1 == angle 2 (alt. interior)',
          abs(angle_at(P1, l2, n2) - angle_at(P2, m1, n1)))
    lab1 = add(P1, pol(340.30, 0.42))
    lab2 = add(P2, pol(160.30, 0.42))
    check('1-26', 'label 1 inside its angle',
          abs(angle_at(P1, l2, lab1) + angle_at(P1, lab1, n2)
              - angle_at(P1, l2, n2)))
    check('1-26', 'label 2 inside its angle',
          abs(angle_at(P2, m1, lab2) + angle_at(P2, lab2, n1)
              - angle_at(P2, m1, n1)))

    # ---- 1-27 : copying angle 2 at P yields a line through P parallel to l
    L1, L2 = (0, 1.35), (3.10, 1.35)
    N1, N2 = (0.72, 0), (2.02, 2.10)
    P27 = lerp(N1, N2, 0.30)
    d1, d2 = add(P27, (-0.66, 0)), add(P27, (1.22, 0))
    check('1-27', 'copied line parallel to l', par(V(d1, d2), V(L1, L2)))
    Q27 = line_inter(L1, L2, N1, N2)
    check('1-27', 'angle 1 == angle 2 (alt. interior)',
          abs(angle_at(Q27, L1, N1) - angle_at(P27, d2, N2)))
    check('1-27', 'P lies on n', cross(N1, N2, P27))
    check('1-27', 'P is below l', max(0.0, P27[1] - L1[1]))
    lab27a = add(Q27, pol(209.12, 0.42))
    lab27b = add(P27, pol(29.12, 0.42))
    check('1-27', 'label 2 inside its angle',
          abs(angle_at(Q27, L1, lab27a) + angle_at(Q27, lab27a, N1)
              - angle_at(Q27, L1, N1)))
    check('1-27', 'label 1 inside its angle',
          abs(angle_at(P27, d2, lab27b) + angle_at(P27, lab27b, N2)
              - angle_at(P27, d2, N2)))

    # ---- 1-28 : right angle at C, hypotenuse c opposite it
    A28, C28, B28 = (0, 0), (2.45, 0), (2.45, 1.70)
    check('1-28', 'right angle at C', perp(V(C28, A28), V(C28, B28)))
    check('1-28', 'c is the longest side',
          max(0.0, max(dist(A28, C28), dist(C28, B28)) - dist(A28, B28)))
    check('1-28', 'a^2 + b^2 == c^2',
          abs(dist(A28, C28) ** 2 + dist(C28, B28) ** 2 - dist(A28, B28) ** 2)
          / dist(A28, B28) ** 2)
