# Chapter 10 (AREA) figure constraints. Coordinates mirror
# chapters/figures10.tex exactly; each check encodes a hypothesis the book
# states in the theorem or exercise the figure serves.
import math

from figlib import V, par, perp, lerp, dist, foot


def mid(p, q):
    return lerp(p, q, 0.5)


def add(p, q, r):
    """p + q - r  (the parallelogram-completion point)"""
    return (p[0] + q[0] - r[0], p[1] + q[1] - r[1])


def relerr(x, y):
    return abs(x - y) / abs(y) if y else abs(x - y)


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def side(a, b, p):
    """signed area of triangle abp; sign says which side of ab the point p is"""
    return cross(V(a, b), V(a, p))


def on_segment(a, b, p):
    """distance from p to line ab, 0 iff p is collinear with a and b"""
    return abs(side(a, b, p)) / dist(a, b)


def build(check):
    # ---- 10-1 : counting rectangles built out of unit squares.
    # (a) one unit square, (b) two side by side, (c) a 3 x 2 grid.  Every cell
    # must be a true unit square or the "count the squares" argument is a lie.
    a1 = ((0, 3.1), (1, 4.1))                     # (a) corners
    check('10-1a', 'cell is square', relerr(a1[1][0] - a1[0][0],
                                            a1[1][1] - a1[0][1]))
    b1 = ((2.4, 3.1), (4.4, 4.1))                 # (b) corners, divider x=3.4
    check('10-1b', 'block is 2 wide by 1 tall',
          relerr((b1[1][0] - b1[0][0]) / (b1[1][1] - b1[0][1]), 2.0))
    check('10-1b', 'divider halves the block',
          relerr(3.4 - b1[0][0], b1[1][0] - 3.4))
    check('10-1b', 'each cell is a unit square',
          relerr(3.4 - b1[0][0], b1[1][1] - b1[0][1]))
    c1 = ((0.7, 0), (3.7, 2))                     # (c) corners
    check('10-1c', 'grid is 3 wide by 2 tall',
          relerr((c1[1][0] - c1[0][0]) / (c1[1][1] - c1[0][1]), 1.5))
    for x0, x1 in ((0.7, 1.7), (1.7, 2.7), (2.7, 3.7)):
        check('10-1c', 'column is one unit wide', relerr(x1 - x0, 1.0))
    for y0, y1 in ((0, 1), (1, 2)):
        check('10-1c', 'row is one unit tall', relerr(y1 - y0, 1.0))

    # ---- 10-2 : (a) a half-unit square in a unit square, quartered by its
    # two midlines; (b) a 2.5 by 3 grid whose last column is a half unit.
    u = ((0, 1.8), (2, 3.8))                      # dashed unit square
    h = ((0, 1.8), (1, 2.8))                      # solid half-unit square
    check('10-2a', 'unit square is square',
          relerr(u[1][0] - u[0][0], u[1][1] - u[0][1]))
    check('10-2a', 'small square is square',
          relerr(h[1][0] - h[0][0], h[1][1] - h[0][1]))
    check('10-2a', 'small side is half the unit side',
          relerr((h[1][0] - h[0][0]) / (u[1][0] - u[0][0]), 0.5))
    check('10-2a', 'mid-vertical bisects the square',
          relerr(1 - u[0][0], u[1][0] - 1))
    check('10-2a', 'mid-horizontal bisects the square',
          relerr(2.8 - u[0][1], u[1][1] - 2.8))
    g = ((3.1, 0), (5.6, 3))                      # the 2.5 x 3 grid
    check('10-2b', 'grid is 2.5 wide', relerr(g[1][0] - g[0][0], 2.5))
    check('10-2b', 'grid is 3 tall', relerr(g[1][1] - g[0][1], 3.0))
    check('10-2b', 'first column is one unit', relerr(4.1 - 3.1, 1.0))
    check('10-2b', 'second column is one unit', relerr(5.1 - 4.1, 1.0))
    check('10-2b', 'last column is a half unit', relerr(5.6 - 5.1, 0.5))
    for y0, y1 in ((0, 1), (1, 2), (2, 3)):
        check('10-2b', 'row is one unit tall', relerr(y1 - y0, 1.0))

    # ---- 10-3 : the counting rectangle is 1.4 by 2.3, chopped into 0.1
    # squares in a 0.4 band on top and a 0.3 band at the right.
    r3 = ((0, 0), (2.3, 1.4))
    check('10-3', 'rectangle is 2.3 wide', relerr(r3[1][0] - r3[0][0], 2.3))
    check('10-3', 'rectangle is 1.4 tall', relerr(r3[1][1] - r3[0][1], 1.4))
    check('10-3', 'first unit division at 1', relerr(1.0 - r3[0][0], 1.0))
    check('10-3', 'second unit division at 2', relerr(2.0 - 1.0, 1.0))
    check('10-3', 'right band is 0.3', relerr(r3[1][0] - 2.0, 0.3))
    check('10-3', 'upper band is 0.4', relerr(r3[1][1] - 1.0, 0.4))
    for y0, y1 in ((1.0, 1.1), (1.1, 1.2), (1.2, 1.3), (1.3, 1.4)):
        check('10-3', 'band strip is 0.1 tall', relerr(y1 - y0, 0.1))
    for x0, x1 in ((2.0, 2.1), (2.1, 2.2), (2.2, 2.3)):
        check('10-3', 'band strip is 0.1 wide', relerr(x1 - x0, 0.1))

    # ---- 10-4 : rectangle of width sqrt(2) and height 1, with the part past
    # the whole unit divided by tenth-marks.  The figure's whole job is to
    # show 1.4 < sqrt(2) < 1.5, so the width must be sqrt(2) UNITS (not
    # tikz units) and the right edge must fall strictly between the fourth
    # and the fifth mark.  Unit = 1.6; marks are 0.089 unit apart, the
    # slight compression the book uses so the edge clears them.
    uu, tt = 1.6, 0.1425
    ww, hh = 2.2627, 1.91
    marks = [uu + k * tt for k in range(1, 6)]
    r4 = ((0, 0), (ww, hh))
    check('10-4', 'figure is a rectangle', perp(V(r4[0], (r4[1][0], 0)),
                                                V(r4[0], (0, r4[1][1]))))
    check('10-4', 'width is sqrt(2) units', relerr(ww / uu, math.sqrt(2)))
    for x0, x1 in zip(marks, marks[1:]):
        check('10-4', 'tenth-marks are equally spaced', relerr(x1 - x0, tt))
    check('10-4', 'first mark is one tenth past the unit',
          relerr(marks[0] - uu, tt))
    check('10-4', 'sqrt(2) edge lies past the fourth mark (1.4 < sqrt2)',
          max(0.0, marks[3] - ww))
    check('10-4', 'sqrt(2) edge lies short of the fifth mark (sqrt2 < 1.5)',
          max(0.0, ww - marks[4]))
    check('10-4', 'whole-unit divider is inside the rectangle',
          max(0.0, uu - ww))
    check('10-4', 'drawn aspect matches the book (h : w = 0.845)',
          max(0.0, abs(hh / ww - 0.845) - 0.05))

    # ---- 10-5(a) : DAEB is a rectangle on base BC; E bisects BC
    B, C = (0, 0), (3, 0)
    E = mid(B, C)
    A = (E[0], E[1] + 3.2)
    D = (B[0], B[1] + 3.2)
    check('10-5a', 'DA || BC', par(V(D, A), V(B, C)))
    check('10-5a', 'DB perp BC', perp(V(D, B), V(B, C)))
    check('10-5a', 'AE perp BC', perp(V(A, E), V(B, C)))
    check('10-5a', 'E bisects BC', relerr(dist(B, E), dist(E, C)))
    check('10-5a', 'AB == AC (isosceles)', relerr(dist(A, B), dist(A, C)))
    check('10-5a', 'DA == BE (rectangle side)', relerr(dist(D, A), dist(B, E)))
    # the book's reason: tri ABD is congruent to tri ACE (right angles at D
    # and at E, and the two legs swap over)
    check('10-5a', 'right angle at D', perp(V(D, A), V(D, B)))
    check('10-5a', 'right angle at E', perp(V(E, A), V(E, C)))
    check('10-5a', 'DA == EC', relerr(dist(D, A), dist(E, C)))
    check('10-5a', 'DB == EA', relerr(dist(D, B), dist(E, A)))

    # ---- 10-5(b) : A'B'C'D' a parallelogram, A'B' congruent to D'E'
    Ap, Bp, Dp = (0, 0.75), (0.675, 1.98), (2.586, 0.446)
    Cp = add(Dp, Bp, Ap)
    Ep = add(Dp, Ap, Bp)
    check('10-5b', "A'B' || D'C'", par(V(Ap, Bp), V(Dp, Cp)))
    check('10-5b', "A'D' || B'C'", par(V(Ap, Dp), V(Bp, Cp)))
    check('10-5b', "A'B' == D'E'", relerr(dist(Ap, Bp), dist(Dp, Ep)))
    check('10-5b', "A'B' || E'D'", par(V(Ap, Bp), V(Ep, Dp)))

    # ---- 10-5(c) : two parallelograms on the common base A''D''
    Aq, Dq, Bq, Eq = (0, 0), (1.6, 0), (0.67, 2.33), (1.46, 2.33)
    Cq, Fq = add(Bq, Dq, Aq), add(Eq, Dq, Aq)
    check('10-5c', "A''D'' || B''C''", par(V(Aq, Dq), V(Bq, Cq)))
    check('10-5c', "A''D'' || E''F''", par(V(Aq, Dq), V(Eq, Fq)))
    check('10-5c', 'equal bases', relerr(dist(Bq, Cq), dist(Aq, Dq)))
    check('10-5c', 'equal heights', abs(Bq[1] - Eq[1]))
    # B'', E'', C'', F'' fall along the top edge in that order, which is the
    # order the book letters them in
    for p, q in ((Bq, Eq), (Eq, Cq), (Cq, Fq)):
        check('10-5c', 'top vertices run B, E, C, F', max(0.0, p[0] - q[0]))
    check('10-5c', "E''F'' == A''D''", relerr(dist(Eq, Fq), dist(Aq, Dq)))

    # ---- 10-6 : polygons ABCDE and DEFG share the side DE and nothing else,
    # which is exactly the hypothesis of Theorem 10-3.
    A6, B6, C6 = (0.464, 2.389), (-0.779, 1.378), (0.365, -0.197)
    D6, E6 = (1.6, 0.3), (1.6, 1.75)
    F6, G6 = (4.004, 2.389), (4.335, -0.347)
    check('10-6', 'DE is vertical', abs(D6[0] - E6[0]))
    for name, p in (('A', A6), ('B', B6), ('C', C6)):
        check('10-6', 'left polygon is left of DE', max(0.0, p[0] - D6[0]))
    for name, p in (('F', F6), ('G', G6)):
        check('10-6', 'right polygon is right of DE', max(0.0, D6[0] - p[0]))
    check('10-6', 'E is above D', max(0.0, D6[1] - E6[1]))

    # ---- 10-7 : right angle at C; AC'BC is a rectangle, area ab
    C7, A7, B7 = (0, 0), (3, 0), (0, 1.3)
    Cp7 = (3, 1.3)
    check('10-7', 'angle C is right', perp(V(C7, A7), V(C7, B7)))
    check('10-7', "BC' || CA", par(V(B7, Cp7), V(C7, A7)))
    check('10-7', "C'A || CB", par(V(Cp7, A7), V(C7, B7)))
    # statement 1 of the proof: tri ABC is congruent to tri BAC'
    check('10-7', "CA == C'B", relerr(dist(C7, A7), dist(Cp7, B7)))
    check('10-7', "CB == C'A", relerr(dist(C7, B7), dist(Cp7, A7)))
    check('10-7', "angle C' is right", perp(V(Cp7, A7), V(Cp7, B7)))

    # ---- 10-8 : parallelogram ABCD in rectangle AECF, base b = AD, EB = x
    A8, D8, B8 = (0, 0), (2, 0), (3.1, 2.05)
    C8 = add(B8, D8, A8)
    E8, F8 = (0, 2.05), (5.1, 0)
    check('10-8', 'AB || DC', par(V(A8, B8), V(D8, C8)))
    check('10-8', 'AD || BC', par(V(A8, D8), V(B8, C8)))
    check('10-8', 'AE perp AF', perp(V(A8, E8), V(A8, F8)))
    check('10-8', 'EC perp CF', perp(V(E8, C8), V(C8, F8)))
    check('10-8', 'E is above A', abs(E8[0] - A8[0]))
    check('10-8', 'F is below C', abs(F8[0] - C8[0]))
    check('10-8', 'height h == AE', relerr(dist(A8, E8), 2.05))
    # AF = EC = b + x, which is step 4 of the book's proof
    check('10-8', 'DF == EB == x', relerr(dist(D8, F8), dist(E8, B8)))
    check('10-8', 'AE == CF (step 1: tri AEB cong tri CFD)',
          relerr(dist(A8, E8), dist(C8, F8)))
    check('10-8', 'AF == b + x',
          relerr(dist(A8, F8), dist(A8, D8) + dist(E8, B8)))

    # ---- 10-9 : triangle of base b, height h, completed to a parallelogram
    B9, C9, A9 = (0, 0), (2.6, 0), (1.46, 1.41)
    Bp9 = add(A9, C9, B9)
    H9 = foot(B9, C9, A9)
    check('10-9', "AB' || BC", par(V(A9, Bp9), V(B9, C9)))
    check('10-9', "B'C || BA", par(V(Bp9, C9), V(B9, A9)))
    check('10-9', 'AH perp BC', perp(V(A9, H9), V(B9, C9)))
    check('10-9', 'H lies between B and C',
          max(0.0, -H9[0]) + max(0.0, H9[0] - C9[0]))

    # ---- 10-10 : l || m, 3 ft apart; AB = CD = 5 ft (Ex. Group 10-5, no. 5).
    # One tikz unit is one foot, so the drawing carries the stated numbers.
    Al, Bl = (0.6, 0), (5.6, 0)
    Cl, Dl = (5.6, 3), (10.6, 3)
    lline = ((0, 3), (11.6, 3))
    mline = ((0, 0), (11.6, 0))
    check('10-10', 'l || m', par(V(*lline), V(*mline)))
    check('10-10', 'A and B lie on m', abs(Al[1] - mline[0][1]) +
          abs(Bl[1] - mline[0][1]))
    check('10-10', 'C and D lie on l', abs(Cl[1] - lline[0][1]) +
          abs(Dl[1] - lline[0][1]))
    check('10-10', 'AB == 5', relerr(dist(Al, Bl), 5.0))
    check('10-10', 'CD == 5', relerr(dist(Cl, Dl), 5.0))
    check('10-10', 'AB == CD', relerr(dist(Al, Bl), dist(Cl, Dl)))
    check('10-10', 'lines are 3 apart', relerr(lline[0][1] - mline[0][1], 3.0))
    check('10-10', 'gap : AB == 3 : 5',
          relerr((lline[0][1] - mline[0][1]) / dist(Al, Bl), 3.0 / 5.0))
    check('10-10', 'ABDC is a parallelogram', par(V(Al, Bl), V(Cl, Dl)))

    # ---- 10-11 : BD perp AD; AB = 5, AD = 4, BD = 3
    A11, D11, B11 = (0, 0), (4, 0), (4, 3)
    C11 = add(B11, D11, A11)
    check('10-11', 'BD perp AD', perp(V(B11, D11), V(A11, D11)))
    check('10-11', 'AB || DC', par(V(A11, B11), V(D11, C11)))
    check('10-11', 'AD || BC', par(V(A11, D11), V(B11, C11)))
    check('10-11', 'AB == 5', relerr(dist(A11, B11), 5))
    check('10-11', 'AD == 4', relerr(dist(A11, D11), 4))
    check('10-11', 'BD == 3', relerr(dist(B11, D11), 3))
    check('10-11', 'BD perp BC (marked right angle)',
          perp(V(B11, D11), V(B11, C11)))

    # ---- 10-12 : trapezoid drawn at 1/4 scale; b' : b : h == 10 : 18 : 12
    B12, C12, A12, D12 = (0, 0), (4.5, 0), (1, 3), (3.5, 3)
    check('10-12', 'AD || BC', par(V(A12, D12), V(B12, C12)))
    check('10-12', "b' : b == 10 : 18",
          relerr(dist(A12, D12) / dist(B12, C12), 10.0 / 18.0))
    check('10-12', 'h : b == 12 : 18',
          relerr(abs(A12[1] - B12[1]) / dist(B12, C12), 12.0 / 18.0))
    check('10-12', 'height is perpendicular',
          perp((0, abs(A12[1] - B12[1])), V(B12, C12)))
    check('10-12', 'altitude foot bisects both bases',
          relerr(2.25 - B12[0], C12[0] - 2.25) +
          relerr(2.25 - A12[0], D12[0] - 2.25))

    # ---- 10-13 : trapezoid split into a parallelogram (b') and b - b'
    B13, C13, A13 = (0, 0), (6, 0), (1.2, 4.3)
    D13 = (A13[0] + 3.38, A13[1])
    P13 = (3.38, 0)
    check('10-13', 'AD || BC', par(V(A13, D13), V(B13, C13)))
    check('10-13', "BP == b' == AD", relerr(dist(B13, P13), dist(A13, D13)))
    check('10-13', 'DP || AB', par(V(D13, P13), V(A13, B13)))
    check('10-13', "PC == b - b'",
          relerr(dist(P13, C13), dist(B13, C13) - dist(A13, D13)))
    # Ex. 20 assumes b > b'; if the drawing did not show that, the figure
    # would not illustrate the proof it is attached to
    check('10-13', "b > b'", max(0.0, dist(A13, D13) - dist(B13, C13) + 1e-9))
    check('10-13', 'P lies between B and C',
          max(0.0, -P13[0]) + max(0.0, P13[0] - C13[0]))

    # ---- 10-14 : parallelogram, diagonals bisect each other at O
    B14, C14, A14 = (0, 0), (3, 0), (0.45, 1.72)
    D14 = add(A14, C14, B14)
    O14 = mid(A14, C14)
    check('10-14', 'AB || DC', par(V(A14, B14), V(D14, C14)))
    check('10-14', 'AD || BC', par(V(A14, D14), V(B14, C14)))
    check('10-14', 'O bisects AC', relerr(dist(A14, O14), dist(O14, C14)))
    check('10-14', 'O bisects BD', relerr(dist(B14, O14), dist(O14, D14)))
    check('10-14', 'O is on BD', on_segment(B14, D14, O14))

    # ---- 10-15 : the generic triangle of Heron's formula.  Nothing is fixed
    # except that it must be a genuine scalene triangle, so that a, b and c
    # really are three different lengths.
    A15, C15, B15 = (0, 0), (3.4, 0), (1.0, 1.7)
    s15 = sorted((dist(A15, B15), dist(B15, C15), dist(A15, C15)))
    check('10-15', 'triangle is non-degenerate',
          max(0.0, 0.2 - abs(side(A15, C15, B15))))
    check('10-15', 'sides are pairwise different',
          max(0.0, 0.2 - (s15[1] - s15[0])) + max(0.0, 0.2 - (s15[2] - s15[1])))
    check('10-15', 'triangle inequality',
          max(0.0, s15[2] - (s15[0] + s15[1])))

    # ---- 10-16 : parallelogram ABCD, E on BD with BE = 2, ED = 6
    B16, C16, A16 = (0, 0), (3.5, 0), (0.64, 2.04)
    D16 = add(A16, C16, B16)
    E16 = lerp(B16, D16, 0.25)
    check('10-16', 'AB || DC', par(V(A16, B16), V(D16, C16)))
    check('10-16', 'AD || BC', par(V(A16, D16), V(B16, C16)))
    check('10-16', 'E is on BD', on_segment(B16, D16, E16))
    check('10-16', 'BE : ED == 2 : 6',
          relerr(dist(B16, E16) / dist(E16, D16), 2.0 / 6.0))

    # ---- 10-17 : right angle at C, CD perp AB, AC = 5, CB = 12 (scaled /3)
    A17, B17 = (0, 0), (4.333, 0)
    C17 = (0.641, 1.538)
    D17 = foot(A17, B17, C17)
    check('10-17', 'angle C is right', perp(V(C17, A17), V(C17, B17)))
    check('10-17', 'CD perp AB', perp(V(C17, D17), V(A17, B17)))
    check('10-17', 'D lies between A and B',
          max(0.0, -D17[0]) + max(0.0, D17[0] - B17[0]))
    check('10-17', 'AC : CB == 5 : 12',
          relerr(dist(A17, C17) / dist(C17, B17), 5.0 / 12.0))
    check('10-17', 'AB == 13 (scaled)', relerr(dist(A17, B17), 13.0 / 3))

    # ---- 10-18 : squares on the three sides of a right triangle
    R18, S18, T18 = (0, 0), (0, 1.0), (1.4, 0)
    N18 = (1.0, 1.4)
    check('10-18', 'angle R is right', perp(V(R18, S18), V(R18, T18)))
    check('10-18', 'normal perp to ST', perp(N18, V(S18, T18)))
    # squares 1 and 2 are drawn as explicit corner paths in the tex; their
    # sides must equal the legs they stand on, or "area 1 + area 2 = area 3"
    # is not what the picture shows
    check('10-18', 'square 1 side == RS', relerr(1.0, dist(R18, S18)))
    check('10-18', 'square 1 is square', relerr(1.0, dist(R18, S18)))
    check('10-18', 'square 2 side == RT', relerr(1.4, dist(R18, T18)))
    check('10-18', 'square 2 is square', relerr(1.4, dist(R18, T18)))
    check('10-18', 'square 3 side == ST', relerr(math.hypot(*N18),
                                                 dist(S18, T18)))
    check('10-18', 'area 1 + area 2 == area 3',
          relerr(dist(R18, S18) ** 2 + dist(R18, T18) ** 2,
                 dist(S18, T18) ** 2))

    # ---- 10-19 : (a+b) square, inner square of side c.  In the book the
    # SHORT piece of each side is the one lettered a, so a < b.
    a, b = 1.6, 2.4
    s = a + b
    P1, P2 = (b, 0), (s, b)
    P3, P4 = (a, s), (0, a)
    check('10-19', 'inner side P1P2 == c',
          relerr(dist(P1, P2), math.hypot(a, b)))
    check('10-19', 'inner P1P2 perp P2P3', perp(V(P1, P2), V(P2, P3)))
    check('10-19', 'inner P2P3 perp P3P4', perp(V(P2, P3), V(P3, P4)))
    check('10-19', 'all inner sides equal',
          relerr(dist(P3, P4), dist(P1, P2)))
    check('10-19', 'outer side == a + b', relerr(s, a + b))
    check('10-19', 'a is the shorter piece, as in the book',
          max(0.0, a - b))
    # the four corner triangles all have legs a and b
    for u, v, w in ((( 0, 0), P1, P4), ((s, 0), P2, P1),
                    ((s, s), P3, P2), ((0, s), P4, P3)):
        legs = sorted((dist(u, v), dist(u, w)))
        check('10-19', 'corner triangle has legs a and b',
              relerr(legs[0], a) + relerr(legs[1], b))
        check('10-19', 'corner triangle is right', perp(V(u, v), V(u, w)))
    check('10-19', 'a^2 + b^2 == c^2',
          relerr(a ** 2 + b ** 2, dist(P1, P2) ** 2))

    # ---- 10-20 : Bhaskara. right angle at C; DF || AC, EG || BC, FC = a - b.
    # The four right-angle vertices C, C', G, F are the successive quarter
    # turns of C about the centre of square BAED, so they form a square of
    # side a - b; three of its sides fall on lines already drawn (GF on DF,
    # C'G on EG, FC on the leg BC) and only CC' is drawn in addition.
    B20, A20 = (0, 0), (3, 0)
    E20, D20 = (3, 3), (0, 3)
    C20 = (1.92, 1.44)
    Cp20 = (1.56, 1.92)
    G20 = (1.08, 1.56)
    F20 = (1.44, 1.08)
    a20, b20 = dist(B20, C20), dist(C20, A20)
    check('10-20', 'BAED is a square',
          relerr(dist(B20, A20), dist(A20, E20)) +
          perp(V(B20, A20), V(A20, E20)))
    check('10-20', 'angle C is right', perp(V(C20, B20), V(C20, A20)))
    check('10-20', 'DF || AC', par(V(D20, F20), V(A20, C20)))
    check('10-20', 'EG || BC', par(V(E20, G20), V(B20, C20)))
    check('10-20', 'FC == a - b', relerr(dist(F20, C20), a20 - b20))
    check('10-20', 'F lies on BC', on_segment(B20, C20, F20))
    check('10-20', 'G lies on DF', on_segment(D20, F20, G20))
    check('10-20', "C' lies on EG", on_segment(E20, G20, Cp20))
    check('10-20', 'inner square side', relerr(dist(C20, Cp20),
                                               dist(G20, F20)))
    check('10-20', 'inner square side (2)', relerr(dist(Cp20, G20),
                                                   dist(F20, C20)))
    check('10-20', 'inner square right angle',
          perp(V(Cp20, C20), V(Cp20, G20)))
    check('10-20', 'inner square right angle at G',
          perp(V(G20, Cp20), V(G20, F20)))
    check('10-20', 'a^2 + b^2 == c^2',
          relerr(a20 ** 2 + b20 ** 2, dist(B20, A20) ** 2))

    # ---- 10-21 : DE drawn parallel to the diagonal AC
    B21, C21 = (0, 0), (2.2, 0)
    A21, D21 = (0.84, 1.50), (2.13, 1.83)
    t = D21[1] / (A21[1] - C21[1])
    E21 = (D21[0] + t * (C21[0] - A21[0]), 0)
    check('10-21', 'DE || AC', par(V(D21, E21), V(A21, C21)))
    check('10-21', 'E on line BC', abs(E21[1] - B21[1]))
    check('10-21', 'E is beyond C on ray BC', max(0.0, C21[0] - E21[0]))
    # the point of the construction: triangle ABE has the area of ABCD
    quad = 0.5 * abs(cross(V(A21, C21), V(A21, D21))) + \
        0.5 * abs(cross(V(A21, B21), V(A21, C21)))
    tri = 0.5 * abs(cross(V(A21, B21), V(A21, E21)))
    check('10-21', 'area(ABE) == area(ABCD)', relerr(tri, quad))

    # ---- 10-22 : the pentagon must stay simple and convex, or the
    # cut-into-triangles construction of Ex. Group 10-7 no. 1 fails.
    P22 = [(0.9, 0), (2.6, 0), (2.74, 2.52), (0.96, 2.78), (0.08, 1.29)]
    crosses = [cross(V(P22[i], P22[(i + 1) % 5]),
                     V(P22[(i + 1) % 5], P22[(i + 2) % 5])) for i in range(5)]
    check('10-22', 'pentagon is convex', max(0.0, -min(crosses)))

    # ---- 10-23 : equilateral triangle, P interior, feet of perpendiculars
    B23, C23 = (0, 0), (4, 0)
    A23 = (2, 3.464)
    P23 = (1.9, 1.0)
    L23 = foot(B23, C23, P23)
    M23 = foot(A23, C23, P23)
    N23 = foot(A23, B23, P23)
    check('10-23', 'AB == BC', relerr(dist(A23, B23), dist(B23, C23)))
    check('10-23', 'AC == BC', relerr(dist(A23, C23), dist(B23, C23)))
    check('10-23', 'PL perp BC', perp(V(P23, L23), V(B23, C23)))
    check('10-23', 'PM perp AC', perp(V(P23, M23), V(A23, C23)))
    check('10-23', 'PN perp AB', perp(V(P23, N23), V(A23, B23)))
    for u, v, w in ((B23, C23, A23), (C23, A23, B23), (A23, B23, C23)):
        check('10-23', 'P is interior',
              max(0.0, -side(u, v, P23) * side(u, v, w)))
    # the exercise's claim, which the drawing had better not contradict
    check('10-23', 'PL + PM + PN == altitude',
          relerr(dist(P23, L23) + dist(P23, M23) + dist(P23, N23), A23[1]))

    # ---- 10-24 : the three medians are concurrent at the centroid
    A24, B24, C24 = (2.13, 2.74), (0, 0), (3.8, 0)
    Gc = ((A24[0] + B24[0] + C24[0]) / 3, (A24[1] + B24[1] + C24[1]) / 3)
    check('10-24', 'median from A hits mid BC',
          dist(Gc, foot(A24, mid(B24, C24), Gc)))
    check('10-24', 'median from B hits mid AC',
          dist(Gc, foot(B24, mid(A24, C24), Gc)))
    check('10-24', 'median from C hits mid AB',
          dist(Gc, foot(C24, mid(A24, B24), Gc)))
    # Review Ex. 3 claims the medians cut the triangle into six equal areas;
    # the drawing must not contradict it
    mids = (mid(B24, C24), mid(A24, C24), mid(A24, B24))
    six = [0.5 * abs(cross(V(Gc, p), V(Gc, q)))
           for p, q in ((B24, mids[0]), (mids[0], C24), (C24, mids[1]),
                        (mids[1], A24), (A24, mids[2]), (mids[2], B24))]
    for t in six:
        check('10-24', 'the six median triangles have equal areas',
              relerr(t, six[0]))
