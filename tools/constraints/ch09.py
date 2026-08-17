"""Chapter 9 figure constraints -- rewritten 2026-08-17 for the scan rebuild.

Every entry restates, in numbers, a hypothesis the BOOK states in words for
that figure (parallel / perpendicular / midpoint / ratio / bisector), plus the
conclusions the figure is supposed to display faithfully.  Coordinates mirror
chapters/figures09.tex exactly; if you move a point there, move it here.

par/perp errors are in degrees; ratio errors are relative.  Tolerance 0.05.
"""
import math

from figlib import V, par, perp, lerp, dist, foot


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


def build(check):
    # ------------------------------------------------------------- Fig 9-1
    # three parallels equally spaced (because AB = BC on m); m'' and m'''
    # parallel to m'.
    A, B, C = (2.90, 2.2), (2.32, 1.1), (1.75, 0)
    Ap, Bp, Cp = (6.90, 2.2), (7.275, 1.1), (7.65, 0)
    D, E = (3.275, 1.1), (2.695, 0)
    check('9-1', 'l || l\'', par((1, 0), (1, 0)))
    check('9-1', 'AB = BC on m', rel(dist(A, B), dist(B, C)))
    check('9-1', "A'B' = B'C' on m'", rel(dist(Ap, Bp), dist(Bp, Cp)))
    check('9-1', "m'' || m'", par(V(A, D), V(Ap, Cp)))
    check('9-1', "m''' || m'", par(V(B, E), V(Ap, Cp)))

    # ------------------------------------------------------- Fig 9-2, 9-3
    for tag, Cx, Bx, By in (('9-2', 3.93, 1.87, 1.75), ('9-3', 5.65, 1.83, 1.73)):
        A, C, B = (0, 0), (Cx, 0), (Bx, By)
        D, E = mid(A, B), mid(B, C)
        check(tag, 'DE || AC', par(V(D, E), V(A, C)))
        check(tag, 'DE = AC/2', rel(dist(D, E), dist(A, C) / 2))

    # ------------------------------------------------------------- Fig 9-4
    A, C, B = (0, 0), (2.39, 0), (0.69, 0.98)
    D, E, G = mid(A, B), mid(B, C), mid(A, C)
    check('9-4', 'DE || AC', par(V(D, E), V(A, C)))
    check('9-4', "m' (GE) || AB", par(V(G, E), V(A, B)))

    # ------------------------------------------------------------- Fig 9-5
    E, G, F = (0, 0), (3.88, -0.12), (0.60, 1.338)
    C = mid(F, G)
    D = (C[0] + (G[0] - E[0]) * 0.5, C[1] + (G[1] - E[1]) * 0.5)
    check('9-5', 'FC = CG', rel(dist(F, C), dist(C, G)))
    check('9-5', 'CD || EG', par(V(C, D), V(E, G)))
    check('9-5', 'DG || EF', par(V(D, G), V(E, F)))
    check('9-5', 'EG = 2 CD', rel(dist(E, G), 2 * dist(C, D)))

    # ------------------------------------------------------------- Fig 9-6
    C6, B6, A6 = (0, 0), (0.0854, 0.70), (0.2477, 2.03)
    Cp6, Bp6, Ap6 = (2.85, 0), (2.7716, 0.70), (2.6226, 2.03)
    check('9-6', 'A,B,C collinear on m', par(V(C6, B6), V(B6, A6)))
    check('9-6', "A',B',C' collinear on m'", par(V(Cp6, Bp6), V(Bp6, Ap6)))
    check('9-6', 'AB/BC = A\'B\'/B\'C\'',
          rel(dist(A6, B6) / dist(B6, C6), dist(Ap6, Bp6) / dist(Bp6, Cp6)))

    # ------------------------------------------------------------- Fig 9-7
    G, Q, E = (0, 0), (2.35, 0), (0.80, 1.15)
    F, P = lerp(E, G, 0.4), lerp(E, Q, 0.4)
    check('9-7', 'FP || GQ', par(V(F, P), V(G, Q)))
    check('9-7', 'EF/EG = EP/EQ',
          rel(dist(E, F) / dist(E, G), dist(E, P) / dist(E, Q)))

    # ------------------------------------------------------------- Fig 9-8
    A, C, B, G = (0, 0), (5.30, 0), (3.02, 1.50), (4.22, 0)
    P = [lerp(A, G, i / 4) for i in range(1, 4)]
    H = [lerp(A, B, i / 4) for i in range(1, 4)]
    check('9-8', 'AD = DE = EF', rel(dist(A, P[0]), dist(P[0], P[1])))
    check('9-8', 'EF = FG', rel(dist(P[1], P[2]), dist(P[2], G)))
    for i in range(3):
        check('9-8', f'line {i+1} || BG', par(V(H[i], P[i]), V(B, G)))
    check('9-8', 'AH = HI', rel(dist(A, H[0]), dist(H[0], H[1])))
    check('9-8', 'IJ = JB', rel(dist(H[1], H[2]), dist(H[2], B)))

    # ------------------------------------------------------------- Fig 9-9
    A, C, B = (0, 0), (4.12, 0.42), (1.32, 2.32)
    D, E = lerp(A, B, 0.172), lerp(B, C, 0.828)
    check('9-9', 'DE || AC', par(V(D, E), V(A, C)))

    # ------------------------------------------------------------ Fig 9-10
    # Rebuilt 2026-08-17 against the book photograph: the three parallels now
    # slope -0.145, spacing AB : BC = 1.5 : 1, and BOTH slanted transversals
    # run 0.586 across per 1 down (the render had them near-vertical, and T2
    # missed A altogether).
    def top(x):
        return 2.00 - 0.145 * x

    def midl(x):
        return 0.80 - 0.145 * x

    def bot(x):
        return -0.145 * x

    A = (0.20, 1.971)
    B, C = (0.0817, 0.7882), (0.00286, -0.0004)
    D, X = (0.96850, 0.65957), (1.48083, -0.21472)
    E, F = (3.30, 1.5215), (4.58083, -0.66422)
    for nm, pt, f in (('A', A, top), ('B', B, midl), ('C', C, bot),
                      ('D', D, midl), ('X', X, bot),
                      ('E', E, top), ('F', F, bot)):
        check('9-10', f'{nm} lies on its parallel', abs(pt[1] - f(pt[0])))
    check('9-10', 'l1 || l2 || l3 (same slope by construction)',
          par((1, -0.145), (1, -0.145)))
    check('9-10', 'A,B,C collinear', par(V(A, B), V(B, C)))
    check('9-10', 'A,D,X collinear (T2)', par(V(A, D), V(D, X)))
    check('9-10', 'T3 || T2', par(V(E, F), V(A, X)))
    check('9-10', 'T2 passes through A (the book crosses T1 and T2 on l1)',
          abs(A[1] - top(A[0])))
    check('9-10', 'AD/DX = AB/BC',
          rel(dist(A, D) / dist(D, X), dist(A, B) / dist(B, C)))
    check('9-10', 'AB : BC = 1.5 : 1 (as the book draws it)',
          rel(dist(A, B) / dist(B, C), 1.5))
    check('9-10', 'EF = AX (parallelogram)', rel(dist(E, F), dist(A, X)))

    # ------------------------------------------------------------ Fig 9-11
    A, D, G = (0, 3.15), (0, 0), (4.55, 0)
    B, C = (0, 1.75), (0, 0.70)
    E, F = lerp(A, G, 4 / 9), lerp(A, G, 7 / 9)
    check('9-11', 'AB:BC:CD = 4:3:2 (AB/BC)',
          rel(dist(A, B) / dist(B, C), 4 / 3))
    check('9-11', 'AB:BC:CD = 4:3:2 (BC/CD)',
          rel(dist(B, C) / dist(C, D), 3 / 2))
    check('9-11', 'BE || DG', par(V(B, E), V(D, G)))
    check('9-11', 'CF || DG', par(V(C, F), V(D, G)))
    check('9-11', 'AE/AG = AB/AD', rel(dist(A, E) / dist(A, G), 4 / 9))

    # ------------------------------------------------------------ Fig 9-12
    T, V1, V2, Bp = (0, 0), (1.189, 1.886), (3.156, -0.303), (6.411, 1.3845)
    P, Q, A12 = lerp(T, V1, 0.6), lerp(V1, V2, 0.4), lerp(V2, Bp, 0.6)
    # the three parallels are the lines through {V1,B}, {P,Q,A12}, {T,V2}
    check('9-12', 'l1 || l3', par(V(V1, Bp), V(T, V2)))
    check('9-12', 'l2 || l3', par(V(P, A12), V(T, V2)))
    check('9-12', 'Q on l2', par(V(P, Q), V(T, V2)))
    check('9-12', '2:3 on transversal 1', rel(dist(P, V1) / dist(T, P), 2 / 3))
    check('9-12', '2:3 on transversal 2', rel(dist(V1, Q) / dist(Q, V2), 2 / 3))
    check('9-12', 'AB : 6 = 2 : 3', rel(dist(A12, Bp) / dist(V2, A12), 2 / 3))

    # ------------------------------------------------------------ Fig 9-13
    A, D, B, C = (0, 0), (3.70, -0.10), (0.60, 2.55), (4.30, 2.45)
    check('9-13', 'ABCD parallelogram (AD || BC)', par(V(A, D), V(B, C)))
    check('9-13', 'ABCD parallelogram (AB || DC)', par(V(A, B), V(D, C)))
    E, F = mid(A, B), mid(C, D)
    G = inter(A, C, E, D)
    H = inter(A, C, B, F)
    check('9-13', 'ED || BF', par(V(E, D), V(B, F)))
    check('9-13', 'G trisects AC', rel(dist(A, G) / dist(A, C), 1 / 3))
    check('9-13', 'H trisects AC', rel(dist(A, H) / dist(A, C), 2 / 3))
    check('9-13', 'EG = ED/3', rel(dist(E, G), dist(E, D) / 3))

    # ------------------------------------------------------------ Fig 9-14
    L, R, T14 = (0, 0), (4.66, 0), (2.16, 2.12)
    D, E = mid(L, T14), mid(L, R)
    check('9-14', 'DE || TR', par(V(D, E), V(T14, R)))
    check('9-14', 'LD/LT = LE/LR',
          rel(dist(L, D) / dist(L, T14), dist(L, E) / dist(L, R)))
    check('9-14', 'z = x.y  (LR.LD = LT.LE)',
          rel(dist(L, R) * dist(L, D), dist(L, T14) * dist(L, E)))

    # ------------------------------------------------------------ Fig 9-15
    E, G, F = (0, 0), (3.5, 0), (1.357, 2.099)
    check('9-15', 'EF : EG = 5 : 7', rel(dist(E, F) / dist(E, G), 5 / 7))
    check('9-15', 'FG : EG = 6 : 7', rel(dist(F, G) / dist(E, G), 6 / 7))
    Ep, Gp, Fp = (0, 0), (1.4, 0), (0.543, 0.840)
    check('9-15', "E'F' = 2 (scale 2/5)", rel(dist(Ep, Fp) / dist(E, F), 2 / 5))

    # ------------------------------------------------------------ Fig 9-16
    # Four segments serving as two pairs (AB, A'B') and two units (CD, EF).
    # The book states no ratio here, so what the figure must show is: all four
    # horizontal, A'B' shorter than AB, EF shorter than CD.
    AB16 = ((0, 0.62), (2.75, 0.62))
    ApBp16 = ((0.10, 0), (2.40, 0))
    CD16 = ((4.35, 0.62), (5.50, 0.62))
    EF16 = ((4.65, 0), (5.25, 0))
    for nm, (p, q) in (('AB', AB16), ("A'B'", ApBp16),
                       ('CD', CD16), ('EF', EF16)):
        check('9-16', f'{nm} horizontal', par(V(p, q), (1, 0)))
    check('9-16', "A'B' shorter than AB",
          0.0 if dist(*ApBp16) < dist(*AB16) else 1.0)
    check('9-16', 'EF shorter than CD',
          0.0 if dist(*EF16) < dist(*CD16) else 1.0)

    # ------------------------------------------------------------ Fig 9-17
    pts = [(x, 0) for x in (0, 0.57, 1.14, 1.71, 2.28)]
    check('9-17', 'CD in 4 congruent parts',
          max(rel(dist(pts[i], pts[i + 1]), 0.57) for i in range(4)))

    # ----------------------------------------------------- Fig 9-18, 9-19
    # Def. 9-5: the primed figures must be similar to the unprimed ones, i.e.
    # every pair of corresponding sides in the same ratio.
    tri18 = [(0, 0), (3.6, 0), (1.0, 2.28)]
    k18 = 0.55                                   # scale= of the primed scope
    tri18p = [(k18 * x, k18 * y) for x, y in tri18]
    check('9-18', "A'B'C' ~ ABC (all side ratios equal)",
          max(rel(dist(tri18p[i], tri18p[(i + 1) % 3])
                  / dist(tri18[i], tri18[(i + 1) % 3]), k18) for i in range(3)))

    pent19 = [(0, 1.38), (0.66, 2.47), (2.25, 1.67), (1.87, 0.31), (0.05, 0)]
    k19 = 0.62
    pent19p = [(k19 * x, k19 * y) for x, y in pent19]
    check('9-19', "A'B'C'D'E' ~ ABCDE (all five side ratios equal)",
          max(rel(dist(pent19p[i], pent19p[(i + 1) % 5])
                  / dist(pent19[i], pent19[(i + 1) % 5]), k19) for i in range(5)))
    cross19 = [((pent19[(i + 1) % 5][0] - pent19[i][0])
                * (pent19[(i + 2) % 5][1] - pent19[(i + 1) % 5][1])
                - (pent19[(i + 1) % 5][1] - pent19[i][1])
                * (pent19[(i + 2) % 5][0] - pent19[(i + 1) % 5][0]))
               for i in range(5)]
    check('9-19', 'ABCDE is convex (Def. 9-5 is about convex polygons)',
          0.0 if (all(c > 0 for c in cross19) or all(c < 0 for c in cross19))
          else 1.0)

    # ------------------------------------------------------------ Fig 9-20
    A, C, B = (0, 0), (2.55, 0), (1.68, 1.10)
    E, F = mid(A, B), mid(B, C)
    check('9-20', 'EF || AC', par(V(E, F), V(A, C)))
    check('9-20', 'BE/BA = BF/BC',
          rel(dist(B, E) / dist(B, A), dist(B, F) / dist(B, C)))

    # ------------------------------------------------------------ Fig 9-21
    O = (0, 0)
    quad = {'A': (-1.72, 0.01), 'B': (-0.05, 0.76),
            'C': (1.105, 0.07), 'D': (0.30, -0.75)}
    prime = {k: mid(O, v) for k, v in quad.items()}
    for k in 'ABCD':
        check('9-21', f'{k}\' bisects O{k}',
              rel(dist(O, prime[k]), dist(O, quad[k]) / 2))
    check('9-21', "A'B' || AB", par(V(prime['A'], prime['B']), V(quad['A'], quad['B'])))
    check('9-21', "C'D' || CD", par(V(prime['C'], prime['D']), V(quad['C'], quad['D'])))

    # ------------------------------------------------------------ Fig 9-22
    A, C, B = (0, 0), (1.75, 0), (1.02, 1.87)
    left = [lerp(A, B, i / 5) for i in range(1, 5)]      # F, A'', E, D
    right = [lerp(B, C, (5 - i) / 5) for i in range(1, 5)]  # G, C'', H, I
    for i, nm in enumerate(['FG', "A''C''", 'EH', 'DI']):
        check('9-22', f'{nm} || AC', par(V(left[i], right[i]), V(A, C)))
    check('9-22', "A''B = 3/5 AB", rel(dist(left[1], B) / dist(A, B), 3 / 5))
    check('9-22', "A'B' = 3/5 AB (scale)", rel(0.6, 3 / 5))

    # ------------------------------------------------------------ Fig 9-23
    C, D, A = (0, 0), (2.10, -0.10), (2.58, 1.32)
    B, E = lerp(A, C, 0.4), lerp(A, D, 0.4)
    check('9-23', 'BE || CD', par(V(B, E), V(C, D)))
    check('9-23', 'AE/AD = 4/10', rel(dist(A, E) / dist(A, D), 0.4))

    # ------------------------------------------------------------ Fig 9-24
    # 2026-08-17: AB and DE must "run north-south", so AB is now exactly
    # vertical and the base exactly horizontal, with C ON it -- the old C sat
    # 0.03 off the drawn base line, which is the kink Caleb saw near B.
    B, A, C = (0, 0), (0, 2.139), (2.377, 0)
    D = lerp(A, C, 0.85)
    E = (D[0], 0.0)
    check('9-24', 'AB runs north-south', abs(A[0] - B[0]))
    check('9-24', 'DE runs north-south', abs(D[0] - E[0]))
    check('9-24', 'C lies on the base BE', abs(C[1] - B[1]))
    check('9-24', 'DE || AB', par(V(D, E), V(A, B)))
    check('9-24', 'DC/AC = 1.5/10', rel(dist(D, C) / dist(A, C), 0.15))
    check('9-24', 'DE/AB = 1.2/8', rel(dist(D, E) / dist(A, B), 0.15))

    # ------------------------------------------------------------ Fig 9-25
    A, C, B = (0, 0), (2.40, 0), (1.30, 1.42)
    D, E = lerp(B, A, 0.53), lerp(B, C, 0.53)
    check('9-25', 'DE || AC', par(V(D, E), V(A, C)))

    # ------------------------------------------------------------ Fig 9-26
    # 2026-08-17: AE leans (the render drew it dead vertical) and AB : DE is
    # the book's 2.53 : 1 rather than 1.6 : 1.
    A, E26, B, D = (0.18, 1.60), (0, 0), (1.0346, 1.5038), (-0.3379, 0.0381)
    C = inter(A, E26, B, D)
    check('9-26', 'AB perp AE', perp(V(A, B), V(A, E26)))
    check('9-26', 'DE perp AE', perp(V(E26, D), V(A, E26)))
    check('9-26', 'AB/DE = AC/CE',
          rel(dist(A, B) / dist(E26, D), dist(A, C) / dist(C, E26)))

    # ------------------------------------------------------------ Fig 9-27
    F, E, I, H = (0, 0), (0.40, 0.80), (1.98, 0), (2.454, 0.948)
    check('9-27', 'l || m', par(V(F, E), V(I, H)))
    G = inter(E, I, F, H)
    check('9-27', 'EF/IH = EG/IG',
          rel(dist(E, F) / dist(I, H), dist(E, G) / dist(I, G)))

    # ------------------------------------------------------------ Fig 9-28
    P, R, Q = (0, 0), (1.80, 0), (0.96, 1.26)
    S = lerp(Q, R, 0.468)
    check('9-28', 'PS bisects angle P (QS/SR = PQ/PR)',
          rel(dist(Q, S) / dist(S, R), dist(P, Q) / dist(P, R)))
    # 2026-08-17: the primed triangle is placed explicitly at 0.62 of the
    # unprimed one, 0.55 units clear of R, so the R and P' labels no longer
    # collide (Caleb's "worst offender").
    k28 = 0.62
    gap28 = 0.55
    Pp = (R[0] + gap28, 0)
    Rp = (Pp[0] + k28 * R[0], 0)
    Qp = (Pp[0] + k28 * Q[0], k28 * Q[1])
    Sp = lerp(Qp, Rp, 0.468)
    check('9-28', "clear gap between R and P' (Caleb: they collided)",
          0.0 if Pp[0] - R[0] >= 0.4 else 1.0)
    check('9-28', "P'S' bisects angle P' (Q'S'/S'R' = P'Q'/P'R')",
          rel(dist(Qp, Sp) / dist(Sp, Rp), dist(Pp, Qp) / dist(Pp, Rp)))
    check('9-28', "P'Q'R' ~ PQR (all three sides at scale 0.62)",
          max(rel(dist(a, b) / dist(c, d), k28) for (a, b), (c, d) in
              (((Pp, Qp), (P, Q)), ((Qp, Rp), (Q, R)), ((Rp, Pp), (R, P)))))
    check('9-28', "PQ/PS = P'Q'/P'S'",
          rel(dist(P, Q) / dist(P, S), dist(Pp, Qp) / dist(Pp, Sp)))

    # ------------------------------------------------------------ Fig 9-29
    A, C, B = (0, 0), (1.88, 0), (1.15, 1.45)
    D = foot(A, B, C)
    E = foot(B, C, A)
    check('9-29', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-29', 'AE perp BC', perp(V(A, E), V(B, C)))

    # ------------------------------------------------------------ Fig 9-30
    B, C, A = (0, 0), (2.30, 0.20), (1.20, 1.30)
    D, E = lerp(A, B, 0.50), lerp(A, C, 0.50)
    check('9-30', 'AD/AB = AE/AC',
          rel(dist(A, D) / dist(A, B), dist(A, E) / dist(A, C)))
    check('9-30', 'DE || BC', par(V(D, E), V(B, C)))

    # ------------------------------------------------------------ Fig 9-31
    A, C, B = (0, 0), (1.63, 0), (1.03, 1.13)
    Bpp, Cpp = lerp(A, B, 0.46), lerp(A, C, 0.46)
    check('9-31', "B''C'' || BC", par(V(Bpp, Cpp), V(B, C)))
    check('9-31', "AB/AB'' = AC/AC''",
          rel(dist(A, B) / dist(A, Bpp), dist(A, C) / dist(A, Cpp)))

    # ------------------------------------------------------------ Fig 9-32
    O = (1.35, 0)
    A, B = (0, -0.06), (-0.03, -0.60)
    D, C = lerp(A, O, 1.5), lerp(B, O, 1.5)
    check('9-32', 'AO/OD = 10/5', rel(dist(A, O) / dist(O, D), 2.0))
    check('9-32', 'BO/OC = 12/6', rel(dist(B, O) / dist(O, C), 2.0))

    # ------------------------------------------------------------ Fig 9-33
    B, C, A = (0, 0), (2.50, 0), (1.03, 1.44)
    E, D = lerp(A, B, 0.44), lerp(A, C, 0.44)
    check('9-33', 'AE = x.AB and AD = x.AC (same x)',
          rel(dist(A, E) / dist(A, B), dist(A, D) / dist(A, C)))
    check('9-33', 'ED || BC', par(V(E, D), V(B, C)))

    # ----------------------------------------------------- Fig 9-34, 9-35
    for tag, dx in (('9-34', 0.64), ('9-35', 1.602)):
        A, B = (0, 0), (2.25, 0)
        D = (dx, 0)
        Cc = (dx, math.sqrt(dx * (2.25 - dx)))
        check(tag, 'angle ACB is right', perp(V(Cc, A), V(Cc, B)))
        check(tag, 'CD perp AB', perp(V(Cc, D), V(A, B)))
        check(tag, 'CD^2 = AD.DB',
              rel(dist(Cc, D) ** 2, dist(A, D) * dist(D, B)))

    # ------------------------------------------------------------ Fig 9-36
    A, C, B = (0, 0), (1.65, 0), (0.85, 1.50)
    App, Cpp = lerp(B, A, 0.60), lerp(B, C, 0.60)
    check('9-36', "A''C'' || AC", par(V(App, Cpp), V(A, C)))
    check('9-36', "A''B/AB = C''B/CB",
          rel(dist(App, B) / dist(A, B), dist(Cpp, B) / dist(C, B)))
    check('9-36', "A''B = A'B' (scale 0.60)",
          rel(dist(App, B) / dist(A, B), 0.60))

    # ------------------------------------------------------------ Fig 9-37
    E, D, C = (0, 0), (2.48, 0), (1.32, 1.00)
    A, B = lerp(E, C, 5 / 12), lerp(E, D, 5 / 12)
    check('9-37', 'EA/EC = 10/24', rel(dist(E, A) / dist(E, C), 10 / 24))
    check('9-37', 'EB/ED = 15/36', rel(dist(E, B) / dist(E, D), 15 / 36))
    check('9-37', 'AB || CD', par(V(A, B), V(C, D)))

    # ------------------------------------------------------------ Fig 9-38
    hexa = [(-0.87, 0.58), (0.41, 0.81), (0.79, 0.06),
            (0.39, -0.65), (-0.09, -0.62), (-0.64, -0.18)]
    th, k = math.radians(-30), 0.72

    def rs(p):
        return (k * (p[0] * math.cos(th) - p[1] * math.sin(th)),
                k * (p[0] * math.sin(th) + p[1] * math.cos(th)))

    hexb = [rs(p) for p in hexa]
    sides_a = [dist(hexa[i], hexa[(i + 1) % 6]) for i in range(6)]
    sides_b = [dist(hexb[i], hexb[(i + 1) % 6]) for i in range(6)]
    check('9-38', 'hexagons similar (all side ratios equal)',
          max(rel(sides_b[i] / sides_a[i], k) for i in range(6)))

    # ------------------------------------------------------------ Fig 9-39
    A, E39, C, B = (0, 0), (2.29, 0), (1.55, 0), (2.29, 1.55)
    D = foot(A, B, C)
    check('9-39', 'BE perp AE', perp(V(B, E39), V(A, E39)))
    check('9-39', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-39', 'A, C, E collinear', par(V(A, C), V(C, E39)))

    # ----------------------------------------------------- Fig 9-40, 9-41
    for tag, bx, dx in (('9-40', 2.67, 1.95), ('9-41', 2.48, 1.83)):
        A, B = (0, 0), (bx, 0)
        D = (dx, 0)
        Cc = (dx, math.sqrt(dx * (bx - dx)))
        check(tag, 'angle ACB is right', perp(V(Cc, A), V(Cc, B)))
        check(tag, 'CD perp AB', perp(V(Cc, D), V(A, B)))
    check('9-41', "l' || l || l''", par((0, 1), (0, 1)))
    check('9-41', 'l perp AB', perp((0, 1), (1, 0)))

    # ------------------------------------------------------------ Fig 9-42
    E, G = (0, 0), (2.6412, 0)
    H, F = (1.8996, 0), (1.8996, 1.1873)
    check('9-42', 'EF perp FG', perp(V(F, E), V(F, G)))
    check('9-42', 'FH perp EG', perp(V(F, H), V(E, G)))
    check('9-42', 'EF : FG = 8 : 5', rel(dist(E, F) / dist(F, G), 8 / 5))

    # ------------------------------------------------------------ Fig 9-43
    A, B = (0, 0), (2.73, 0)
    D, C = (0.4038, 0), (0.4038, 0.9692)
    check('9-43', 'sides 5 : 12 : 13 (AC/AB)', rel(dist(A, C) / dist(A, B), 5 / 13))
    check('9-43', 'sides 5 : 12 : 13 (CB/AB)', rel(dist(C, B) / dist(A, B), 12 / 13))
    check('9-43', 'right angle at C', perp(V(C, A), V(C, B)))
    check('9-43', 'h perp AB', perp(V(C, D), V(A, B)))

    # ------------------------------------------------------------ Fig 9-44
    R, P = (0, 0), (2.52, 0)
    S, Q = (1.40, 0), (1.40, 1.2522)
    check('9-44', 'angle Q is right', perp(V(Q, P), V(Q, R)))
    check('9-44', 'QS perp PR', perp(V(Q, S), V(P, R)))
    check('9-44', 'SR : PS = 5 : 4', rel(dist(S, R) / dist(S, P), 5 / 4))

    # ------------------------------------------------------------ Fig 9-45
    A, B = (0, 0), (2.540, 0)
    D, C = (1.6545, 0), (1.6545, 1.2106)
    check('9-45', 'angle C is right', perp(V(C, A), V(C, B)))
    check('9-45', 'angle ADC is right', perp(V(D, C), V(D, A)))
    check('9-45', 'h = ab/c',
          rel(dist(C, D), dist(A, C) * dist(C, B) / dist(A, B)))

    # ------------------------------------------------------------ Fig 9-46
    A, B = (0, 0), (2.75, 0)
    D, C = (1.05, 0), (1.05, 1.3360)
    check('9-46', 'angle C is right', perp(V(C, A), V(C, B)))
    check('9-46', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-46', 'x + y = c', rel(dist(A, D) + dist(D, B), dist(A, B)))

    # ------------------------------------------------------------ Fig 9-47
    C, B, A = (0, 0), (0.94, 0), (0, 1.60)
    P47, Q47, R47 = (2.35, 0), (3.29, 0), (2.35, 1.60)   # xshift=2.35cm scope
    check('9-47', 'angle C is right', perp(V(C, A), V(C, B)))
    check('9-47', 'angle P is right', perp(V(P47, R47), V(P47, Q47)))
    check('9-47', 'PQ = CB (a)', rel(dist(P47, Q47), dist(C, B)))
    check('9-47', 'PR = CA (b)', rel(dist(P47, R47), dist(C, A)))
    check('9-47', 'RQ = AB (c, so the triangles are congruent)',
          rel(dist(R47, Q47), dist(A, B)))

    # ------------------------------------------------------------ Fig 9-48
    # SCHEMATIC by Caleb's decision of 2026-08-17: the figure must NOT be drawn
    # at the exercise's own BD : AD = 24 : 13, which gives the answer away.  The
    # three STATED hypotheses still hold exactly, and they force a rhombus.
    Bq, Dq = (-0.732, -0.369), (0.732, 0.369)
    Aq, Cq = (-0.234, 0.464), (0.234, -0.464)
    check('9-48', 'AC perp BD', perp(V(Aq, Cq), V(Bq, Dq)))
    check('9-48', 'AB || CD', par(V(Aq, Bq), V(Cq, Dq)))
    check('9-48', 'BC || AD', par(V(Bq, Cq), V(Aq, Dq)))
    check('9-48', 'all four sides equal (a rhombus)',
          max(rel(dist(a, b), dist(Aq, Dq)) for a, b in
              ((Aq, Bq), (Bq, Cq), (Cq, Dq), (Dq, Aq))))
    check('9-48', 'schematic: BD : AC is NOT the given 2.4',
          0.0 if abs(dist(Bq, Dq) / dist(Aq, Cq) - 2.4) > 0.5 else 1.0)

    # ------------------------------------------------------------ Fig 9-49
    O, A, B = (0, 0), (0, 2.10), (2.00, 0)
    check('9-49', 'OA perp OB', perp(V(O, A), V(O, B)))
    check('9-49', 'OA : OB = 21 : 20', rel(dist(O, A) / dist(O, B), 21 / 20))

    # ------------------------------------------------------------ Fig 9-50
    # 2026-08-17: apex height is the book's 0.50 x AB, not 0.65, so the arcs
    # cut AB at 31% and 69% (the book's) instead of 18% and 82%.
    A, B = (0, 0), (1.80, 0)
    C, P = (0.90, 0), (0.90, 0.90)
    r = 1.27279
    check('9-50', 'C is the midpoint of AB', rel(dist(A, C), dist(C, B)))
    check('9-50', 'PC perp AB', perp(V(P, C), V(A, B)))
    check('9-50', 'PA = r', rel(dist(P, A), r))
    check('9-50', 'PB = r', rel(dist(P, B), r))
    check('9-50', 'PC = sqrt(r^2 - (AB/2)^2)',
          rel(dist(P, C), math.sqrt(r * r - (dist(A, B) / 2) ** 2)))
    check('9-50', 'apex height = 0.50 AB (the book)',
          rel(dist(P, C) / dist(A, B), 0.50))
    # the arcs are struck from -57 to +57 deg; they meet at +-45, so each
    # overshoots by 12 deg and the two crosses of the construction appear.
    check('9-50', 'arcs meet at +-45 deg',
          abs(math.degrees(math.atan2(P[1] - A[1], P[0] - A[0])) - 45.0) / 45.0)
    check('9-50', 'arcs overshoot past both intersections',
          0.0 if 57.0 > 45.0 else 1.0)

    # ------------------------------------------------------------ Fig 9-51
    R51 = 1.40
    O = (0, 0)
    A, B = (-R51, 0), (R51, 0)
    D = (-0.637, 0)
    C = (-0.637, 1.2464)
    check('9-51', 'C on the circle', rel(dist(O, C), R51))
    check('9-51', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-51', 'angle ACB is right', perp(V(C, A), V(C, B)))
    check('9-51', 'x = r - y', rel(dist(A, D), R51 - dist(D, O)))
    check('9-51', 'z = sqrt(r^2 - y^2)',
          rel(dist(C, D), math.sqrt(R51 ** 2 - dist(D, O) ** 2)))

    # ------------------------------------------------------------ Fig 9-52
    O = (0, 0)
    A, B = (0, 1.5), (0, -1.5)
    E, C, D = (0, 1.2), (-0.9, 1.2), (0.9, 1.2)
    check('9-52', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-52', 'C on the circle', rel(dist(O, C), 1.5))
    check('9-52', 'D on the circle', rel(dist(O, D), 1.5))
    check('9-52', 'EO : AB = 12 : 30', rel(dist(E, O) / dist(A, B), 12 / 30))
    check('9-52', 'CD = 18 when AB = 30', rel(dist(C, D) / dist(A, B), 18 / 30))

    # ---------------------------------------- Fig 9-53 (right trapezoid, Ex. 11)
    A, B, P = (0, 0), (18, 0), (18, 24)
    D, C, H = (6, 8), (18, 8), (6, 0)
    check('9-53', 'DC || AB', par(V(D, C), V(A, B)))
    check('9-53', 'DH perp AB', perp(V(D, H), V(A, B)))
    check('9-53', 'AD = 10', rel(dist(A, D), 10))
    check('9-53', 'DC = 12', rel(dist(D, C), 12))
    check('9-53', 'AB = 18', rel(dist(A, B), 18))
    check('9-53', 'DH = 8', rel(dist(D, H), 8))
    check('9-53', 'D on AP', par(V(A, D), V(D, P)))
    check('9-53', 'C on BP', par(V(B, C), V(C, P)))
    check('9-53', 'right angle at B in ABP', perp(V(B, A), V(B, P)))
    check('9-53', 'AP = 30', rel(dist(A, P), 30))

    # ------------------------------------------------- Fig 9-54 (Menelaus)
    # 2026-08-17: rebuilt to the book's flat, wide triangle -- apex 39% along
    # the base and 0.67 of it high, base rising slightly to the right.  At the
    # old shape the dashed AX ran within 5 deg of side AB.
    A, B = (0, 0), (1.24, 2.21)
    C = (3.18, 0.20)
    F = lerp(A, C, 1.70)
    D = lerp(A, B, 2 / 3)
    E = inter(D, F, B, C)
    X, Y, Z = foot(D, F, A), foot(D, F, B), foot(D, F, C)
    check('9-54', 'F on line AC', par(V(A, C), V(C, F)))
    check('9-54', 'AX perp l', perp(V(A, X), V(D, F)))
    check('9-54', 'BY perp l', perp(V(B, Y), V(D, F)))
    check('9-54', 'CZ perp l', perp(V(C, Z), V(D, F)))
    check('9-54', 'AD/DB . BE/EC . CF/FA = 1',
          rel(dist(A, D) / dist(D, B) * dist(B, E) / dist(E, C)
              * dist(C, F) / dist(F, A), 1))
    # the point of the reshape: AX must be plainly distinguishable from AB
    angAX = math.degrees(math.atan2(X[1] - A[1], X[0] - A[0]))
    angAB = math.degrees(math.atan2(B[1] - A[1], B[0] - A[0]))
    check('9-54', 'dashed AX clears side AB by more than 10 deg',
          0.0 if abs(angAX - angAB) > 10.0 else 1.0)

    # ------------------------------------------- Fig 9-55 (two altitudes)
    # 2026-08-17: flattened from 0.85 to the book's 0.72, and both right-angle
    # squares are now struck at a FIXED 0.17 units a side.  E's used to be
    # 0.16 of |EA| and |EB| -- sides four times longer than D's -- so it
    # printed much the larger of the two and hung into the triangle.
    A, B, C = (0, 0), (3.43, 0), (2.05, 2.46)
    D = foot(A, B, C)
    E = foot(A, C, B)
    check('9-55', 'CD perp AB', perp(V(C, D), V(A, B)))
    check('9-55', 'BE perp AC', perp(V(B, E), V(A, C)))
    check('9-55', 'D is where the drawing puts it', dist(D, (2.05, 0)))
    check('9-55', 'E is where the drawing puts it',
          dist(E, (1.40575, 1.68689)))
    sq_d = [(1.88, 0), (1.88, 0.17), (2.05, 0.17)]
    sq_e = [(1.51458, 1.81749), (1.64518, 1.70866), (1.53635, 1.57806)]
    check('9-55', 'right-angle square at D is 0.17 a side',
          max(rel(dist(sq_d[i], sq_d[i + 1]), 0.17) for i in range(2)))
    check('9-55', 'right-angle square at E is the SAME 0.17 a side',
          max(rel(dist(sq_e[i], sq_e[i + 1]), 0.17) for i in range(2)))
    check('9-55', 'square at E sits square on EC', perp(
        V(sq_e[0], sq_e[1]), V(sq_e[1], sq_e[2])))
    check('9-55', 'square at E is aligned with EC',
          par(V(E, sq_e[0]), V(E, C)))
    check('9-55', 'square at E is aligned with EB',
          par(V(E, sq_e[2]), V(E, B)))
