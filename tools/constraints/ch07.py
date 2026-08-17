# Chapter 7 figure constraints. Coordinates mirror chapters/figures07.tex.
# Each entry encodes a hypothesis the book's own text states for that figure.
#
# Deliberately NOT constrained:
#   7-5   reductio figure: two "perpendiculars" from P to l are drawn with
#         right-angle boxes at both Q and R. That configuration is impossible
#         by construction -- it is the absurdity the exercise asks you to find.
#   7-1   a triangle with one side produced; no metric hypothesis is stated.
#   7-10  schematic "any polygonal path"; no metric hypothesis is stated.
#   7-17  line drawing of a drafting compass, not a geometric figure.
#   7-19  a circle and a square, no stated relation (the squaring problem).
#   7-20  the two candidate copies of angle A at B are drawn deliberately
#         wider than angle A -- the book's own figure does this; the point
#         is only that there are two of them, one per side of the ray.
#   7-34  only a betweenness/crossing configuration is asserted.
import math

from figlib import V, ang, par, perp, lerp, dist, foot


def polar(deg, r):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def ray_angle(vertex, pt):
    return math.degrees(math.atan2(pt[1] - vertex[1], pt[0] - vertex[0]))


def collinear(a, b, c):
    """degrees between ab and ac; 0 when collinear"""
    return par(V(a, b), V(a, c))


def relerr(x, y):
    return abs(x - y) / abs(y)


def build(check):
    # ---- 7-2 : D on ray AB beyond B, chosen so that BD == AC
    #            ("Choose D, as in the figure, such that BD = AC", p.117)
    A, B, C = (0, 0), (2.6, 0), (1.10, 2.10)
    D = (4.97066, 0)
    check('7-2', 'BD == AC', relerr(dist(B, D), dist(A, C)))
    check('7-2', 'D on ray AB', collinear(A, B, D))
    check('7-2', 'B between A and D', 0.0 if A[0] < B[0] < D[0] else 1.0)

    # ---- 7-3 : C, F, E collinear with F on AB
    A, B, C = (0, 0), (2.4, 0), (1.2, 2.1)
    F = (1.05, 0)
    E = lerp(C, F, 1.245)
    check('7-3', 'C, F, E collinear', collinear(C, F, E))
    check('7-3', 'F on AB', collinear(A, B, F))

    # ---- 7-4 : BG = GC and AG = GH  (G bisects CB and AH)
    A, B, C = (0, 0), (2.6, 0), (1.15, 2.1)
    G = lerp(C, B, 0.5)
    H = lerp(A, G, 2.0)
    check('7-4', 'BG == GC', relerr(dist(B, G), dist(G, C)))
    check('7-4', 'AG == GH', relerr(dist(A, G), dist(G, H)))

    # ---- 7-6 : C' on AB with AC' = AC
    B, C, A = (0, 0), (2.7, 0), (2.5, 1.9)
    Cp = lerp(A, B, 0.60843)
    check('7-6', "AC' == AC", relerr(dist(A, Cp), dist(A, C)))
    check('7-6', "C' on AB", collinear(A, B, Cp))

    # ---- 7-7 : sides are 17, 16, 25 (drawn at 1/10 scale)
    A, C, B = (0, 0), (2.5, 0), (1.316, 1.076)
    check('7-7', 'AB : AC == 17 : 25', relerr(dist(A, B) / dist(A, C), 17 / 25))
    check('7-7', 'BC : AC == 16 : 25', relerr(dist(B, C) / dist(A, C), 16 / 25))

    # ---- 7-8 : QS bisects angle PQR  =>  PS/SR == QP/QR
    P, Q, R = (0, 0), (2.6, 0.35), (1.10, 2.55)
    S = lerp(P, R, 0.49629)
    check('7-8', 'PS/SR == QP/QR',
          relerr(dist(P, S) / dist(S, R), dist(Q, P) / dist(Q, R)))
    check('7-8', 'S on PR', collinear(P, R, S))

    # ---- 7-9 : B' on AC with AB = AB'
    A, C, B = (0, 0), (2.9, 0), (1.0, 1.62)
    Bp = (1.903786, 0)
    check('7-9', "AB == AB'", relerr(dist(A, B), dist(A, Bp)))
    check('7-9', "B' on AC", collinear(A, C, Bp))
    check('7-9', "B' between A and C", 0.0 if 0 < Bp[0] < C[0] else 1.0)

    # ---- 7-11 : D on BA with DB = DC
    B, C, A = (0, 0), (2.6, 0), (1.85, 1.35)
    D = (1.3, 0.948649)
    check('7-11', 'DB == DC', relerr(dist(D, B), dist(D, C)))
    check('7-11', 'D on BA', collinear(B, A, D))

    # ---- 7-12 : CB' = CB and QB = QB', Q on AB
    #             (A' = A and C' = C, so BC = B'C' reads CB' == CB)
    A, B, C = (0, 0), (3.2, 0), (1.8875, 1.43)
    Bp = (1.30, -0.42)
    Q = (2.2036, 0)
    check('7-12', "CB' == CB", relerr(dist(C, Bp), dist(C, B)))
    check('7-12', "QB == QB'", relerr(dist(Q, B), dist(Q, Bp)))
    check('7-12', 'Q on AB', collinear(A, B, Q))
    check('7-12', 'Q between A and B', 0.0 if 0 < Q[0] < B[0] else 1.0)

    # ---- 7-13 : E on BC, and A, D, E collinear
    A, C, B = (0, 0), (3.0, 0), (1.45, 1.93)
    E = lerp(B, C, 0.49)
    D = lerp(A, E, 0.655)
    check('7-13', 'E on BC', collinear(B, C, E))
    check('7-13', 'A, D, E collinear', collinear(A, D, E))

    # ---- 7-14 : l _|_ m and l' _|_ m
    m = V((1.2, 2.03), (1.2, -0.10))
    l = V((0, 1.6), (2.8, 1.6))
    lp = V((0, 0.2), (2.8, 0.2))
    check('7-14', 'l perp m', perp(l, m))
    check('7-14', "l' perp m", perp(lp, m))

    # ---- 7-15 (left) : A on the circle, B interior, C exterior, E and F on it
    r = 1.15
    O = (0, 0)
    check('7-15L', 'OA == r', relerr(dist(O, polar(40, r)), r))
    check('7-15L', 'OB < r', 0.0 if dist(O, polar(95, 0.78)) < r else 1.0)
    check('7-15L', 'OC > r', 0.0 if dist(O, polar(-10, 1.87)) > r else 1.0)
    check('7-15L', 'OE == r', relerr(dist(O, polar(215, r)), r))
    check('7-15L', 'OF == r', relerr(dist(O, polar(293, r)), r))

    # ---- 7-15 (right) : A, B, F, E, G all on the circle
    for nm, a in (('A', 95), ('B', 45), ('F', 178), ('E', 250), ('G', 310)):
        check('7-15R', f'O{nm} == r', relerr(dist(O, polar(a, r)), r))

    # ---- 7-16 : A, B, D, E and the four unlabelled points P1..P4 all lie on
    #             the circle; C is the CENTRE (printed "C = O"), so CD and
    #             CP3 are radii and angle C is a central angle.  Ex. 7-5 #3
    #             asks what kind of angle each of A, B, C, D, E is, so each
    #             must be the vertex of two drawn rays -- listed below.
    r16 = 1.3
    pts16 = (('A', 57), ('B', 132), ('D', 240), ('E', 308),
             ('P1', -4), ('P2', 13), ('P3', -13), ('P4', -34))
    for nm, a in pts16:
        check('7-16', f'O{nm} == r', relerr(dist(O, polar(a, r16)), r16))
    # Each labelled vertex must carry two drawn sides.  That is a property of
    # the tex, not of these coordinates, so it is checked by reading
    # figures07.tex, not asserted here:
    #   A  chord A-P2      + ray outside the circle
    #   B  chord B-D       + chord B-P1
    #   C  radius C-D      + radius C-P3      (central angle)
    #   D  chord D-B/D-C   + chord D-P4/D-E
    #   E  ray             + ray              (both outside the circle)

    # ---- 7-18 : the trisection figure -- three congruent sub-angles
    rays = [45, 18, -9, -36]
    g1, g2, g3 = (rays[0] - rays[1], rays[1] - rays[2], rays[2] - rays[3])
    check('7-18', 'angle B == angle C', relerr(g1, g2))
    check('7-18', 'angle C == angle D', relerr(g2, g3))

    # ---- 7-21 : AD = AE = r, BF = BG = r, and FG = DE
    A21, B21 = (0, 0), (0, 0)
    D21, E21 = polar(38, 1.0), polar(0, 1.0)
    F21, G21 = polar(0, 1.0), polar(38, 1.0)
    check('7-21', 'AD == AE', relerr(dist(A21, D21), dist(A21, E21)))
    check('7-21', 'BF == BG', relerr(dist(B21, F21), dist(B21, G21)))
    check('7-21', 'FG == DE', relerr(dist(F21, G21), dist(D21, E21)))

    # ---- 7-22 : Construction 7-2 -- A'B' = AB (arc of radius AB about A')
    #             and A'C' = AC (C' cut off on the ray).  B'C' is NOT drawn
    #             at this stage of the construction, but B' is placed so that
    #             the copy would be congruent.
    A, B, C = (0, 2.05), (0.95, 3.40), (2.35, 2.05)
    Ap, Bp, Cp = (0, 0), (0.95, 1.35), (2.35, 0)
    check('7-22', "A'B' == AB", relerr(dist(Ap, Bp), dist(A, B)))
    check('7-22', "A'C' == AC", relerr(dist(Ap, Cp), dist(A, C)))
    check('7-22', "B'C' == BC", relerr(dist(Bp, Cp), dist(B, C)))
    check('7-22', "C' on the ray from A'", collinear(Ap, (1, 0), Cp))

    # ---- 7-23 : Construction 7-3 -- B' is cut by two arcs, radius AB about
    #             A' and radius BC about C'
    A, B, C = (0, 2.15), (1.15, 3.45), (2.4, 2.15)
    Ap, Bp, Cp = (0, 0), (1.15, 1.30), (2.4, 0)
    check('7-23', "A'B' == AB", relerr(dist(Ap, Bp), dist(A, B)))
    check('7-23', "B'C' == BC", relerr(dist(Bp, Cp), dist(B, C)))
    check('7-23', "A'C' == AC", relerr(dist(Ap, Cp), dist(A, C)))
    check('7-23', "C' on the ray from A'", collinear(Ap, (1, 0), Cp))

    # ---- 7-24 : equal radii from A and B meet at P and Q
    A, B = (0, 0), (3.0, 0)
    P, Q = (1.5, 1.0828), (1.5, -1.0828)
    for nm, X in (('P', P), ('Q', Q)):
        check('7-24', f'A{nm} == 1.85', relerr(dist(A, X), 1.85))
        check('7-24', f'B{nm} == 1.85', relerr(dist(B, X), 1.85))

    # ---- 7-25 : PQ is the perpendicular bisector of AB, meeting it at C
    C25 = (1.5, 0)
    check('7-25', 'PQ perp AB', perp(V(P, Q), V(A, B)))
    check('7-25', 'C bisects AB', relerr(dist(A, C25), dist(C25, B)))
    check('7-25', 'C on PQ', collinear(P, Q, C25))

    # ---- 7-26 / 7-27 : the circle centred at P meets l in A and B
    P26, A26, B26 = (1.5, 0), (0.55, 0), (2.45, 0)
    check('7-26', 'PA == PB', relerr(dist(P26, A26), dist(P26, B26)))
    P27, A27, B27 = (1.6, 1.75), (0.35, 0), (2.85, 0)
    check('7-27', 'PA == PB', relerr(dist(P27, A27), dist(P27, B27)))

    # ---- 7-28 : AP = AP', angle PAC = angle QAC, PP' _|_ l, D on l
    A, P, Pp = (0, 0), (1.55, 1.8), (1.55, -1.8)
    l28 = V((-0.4, 0), (3.4, 0))
    check('7-28', "AP == AP'", relerr(dist(A, P), dist(A, Pp)))
    check('7-28', "angle PAC == angle QAC",
          abs(ray_angle(A, P) + ray_angle(A, Pp)))
    check('7-28', "PP' perp l", perp(V(P, Pp), l28))
    check('7-28', 'D on l', collinear((-0.4, 0), (3.4, 0), (1.55, 0)))

    # ---- 7-29 : angle 1 = angle 2 and AP = AP'
    A, P, Pp = (0, 0), (1.6, 1.6), (1.6, -1.6)
    check('7-29', 'angle 1 == angle 2',
          abs(ray_angle(A, P) + ray_angle(A, Pp)))
    check('7-29', "AP == AP'", relerr(dist(A, P), dist(A, Pp)))

    # ---- 7-30 : AB = AC (one circle) and QB = QC (perpendicular bisector)
    A30 = (0, 2.0)
    C30, B30 = (0, 1.0), (0.643, 1.234)
    Q30 = (0.5303, 0.5435)
    check('7-30', 'AB == AC', relerr(dist(A30, B30), dist(A30, C30)))
    check('7-30', 'QB == QC', relerr(dist(Q30, B30), dist(Q30, C30)))

    # ---- 7-31 : two radii r and r', P on the bisector of angle A
    A31 = (0, 0)
    C31, Cp31 = polar(0, 1.5), polar(0, 2.1)
    D31, Dp31 = polar(30, 1.5), polar(30, 2.1)
    P31 = (1.633, 0.4373)
    check('7-31', 'AC == AD (radius r)', relerr(dist(A31, C31), dist(A31, D31)))
    check('7-31', "AC' == AD' (radius r')",
          relerr(dist(A31, Cp31), dist(A31, Dp31)))
    check('7-31', "P on DC'", collinear(D31, Cp31, P31))
    check('7-31', "P on D'C", collinear(Dp31, C31, P31))
    check('7-31', 'AP bisects angle A', abs(ray_angle(A31, P31) - 15.0))

    # ---- 7-32 : angle 1 = angle 2, angle 3 = angle 4, angle CAD = angle EBF
    #             (both fans drawn as 30 / 15 / 0 degrees)
    aC, aMid, aD = 30.0, 15.0, 0.0
    bE, bMid, bF = 30.0, 15.0, 0.0
    check('7-32', 'angle 1 == angle 2', relerr(aC - aMid, aMid - aD))
    check('7-32', 'angle 3 == angle 4', relerr(bE - bMid, bMid - bF))
    check('7-32', 'angle CAD == angle EBF', relerr(aC - aD, bE - bF))

    # ---- 7-33 : angle ABD is right, C between B and D
    B33, A33, C33, D33 = (0, 0), (0, 1.85), (1.25, 0), (2.85, 0)
    check('7-33', 'angle ABD right', perp(V(B33, A33), V(B33, D33)))
    check('7-33', 'C between B and D',
          0.0 if 0 < C33[0] < D33[0] else 1.0)

    # ---- 7-35 : AC bisects angle DAB, AE bisects angle DAF, and B, A, F are
    #             collinear -- which is what makes the conclusion (angle CAE
    #             is right) follow.  Ray angles read off scan09 p.5.
    bB, bC, bD, bE, bF = 158.0, 100.5, 43.0, 10.5, -22.0
    check('7-35', 'AC bisects angle DAB', abs(bC - (bD + bB) / 2))
    check('7-35', 'AE bisects angle DAF', abs(bE - (bD + bF) / 2))
    check('7-35', 'B, A, F collinear', abs((bB - bF) - 180.0))
    check('7-35', 'angle CAE is right', abs((bC - bE) - 90.0))

    # ---- 7-36 : AC bisects angle DAB, angle CAE right, AE bisects angle DAF
    cB, cC, cD, cE, cF = 180.0, 127.5, 75.0, 37.5, 0.0
    check('7-36', 'AC bisects angle DAB', abs(cC - (cD + cB) / 2))
    check('7-36', 'angle CAE is right', abs((cC - cE) - 90.0))
    check('7-36', 'AE bisects angle DAF', abs(cE - (cD + cF) / 2))
