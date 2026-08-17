# Chapter 4 figure constraints. Coordinates mirror chapters/figures04.tex
# exactly; every congruence the printed figure asserts (tick marks, arcs,
# postulate hypotheses) is checked here.
from figlib import V, par, lerp, dist


def build(check):
    def eq(fig, what, p, q, r, s):
        """|pq| == |rs| as a relative error."""
        a, b = dist(p, q), dist(r, s)
        check(fig, what, abs(a - b) / a)

    def collinear(fig, what, p, q, r):
        check(fig, what, par(V(p, q), V(p, r)))

    def between(fig, what, p, m, q):
        """m lies on segment pq (collinear and interior)."""
        check(fig, what, (dist(p, m) + dist(m, q) - dist(p, q)) / dist(p, q))

    def on_line(fig, lname, P, Q, named):
        """Every named point lies ON the line the figure actually draws
        from P to Q.

        Length and betweenness checks cannot see this: a point may carry
        the right distances to its neighbours and still float off the
        stroke.  Fig. 4-2's B' did exactly that (2.16 pt clear of l').
        Postulates III-1/III-3 and Definition 4-1 all state their points
        as lying on a named line, so incidence is a stated hypothesis.
        """
        for nm, R in named:
            check(fig, f'{nm} on {lname}', par(V(P, Q), V(P, R)))

    # ---- 4-2 : III-1, AB congruent to A'B'
    A = (1.00000, 0.42000)
    B = (4.20000, 1.76000)
    Ap = (1.55000, -0.53479)
    Bp = (5.01280, -0.74609)
    eq('4-2', 'AB = A\'B\'', A, B, Ap, Bp)
    on_line('4-2', 'l', (0.12371, 0.05306), (5.21465, 2.18488),
            [('A', A), ('B', B)])
    on_line('4-2', "l'", (0.83242, -0.49100), (5.62546, -0.78347),
            [("A'", Ap), ("B'", Bp)])

    # ---- 4-3 : III-3, AB = A'B' and BC = B'C', with B between A,C
    A = (0.86972, 0.09602)
    B = (2.70855, 0.29902)
    C = (3.41923, 0.37748)
    Ap = (1.09193, -1.07678)
    Bp = (2.93545, -0.92196)
    Cp = (3.64794, -0.86212)
    eq('4-3', 'AB = A\'B\'', A, B, Ap, Bp)
    eq('4-3', 'BC = B\'C\'', B, C, Bp, Cp)
    between('4-3', 'B between A and C', A, B, C)
    between('4-3', 'B\' between A\' and C\'', Ap, Bp, Cp)
    on_line('4-3', 'l', (0.46519, 0.05136), (4.96981, 0.54866),
            [('A', A), ('B', B), ('C', C)])
    on_line('4-3', "l'", (0.68636, -1.11084), (5.20247, -0.73157),
            [("A'", Ap), ("B'", Bp), ("C'", Cp)])

    # ---- 4-4 : Ex 4-2 #7.  AB=BC, CD=CE=ED, EF=EB
    A = (0, 0)
    C = (3.60000, 0)
    D = (6.50000, 0)
    E = (5.05000, -2.51147)
    B = (1.80000, 3.11769)
    F = (8.30000, 3.11769)
    eq('4-4', 'AB = BC', A, B, B, C)
    eq('4-4', 'CD = CE', C, D, C, E)
    eq('4-4', 'CE = ED', C, E, E, D)
    eq('4-4', 'EF = EB', E, F, E, B)
    collinear('4-4', 'A, C, D collinear', A, C, D)
    collinear('4-4', 'B, C, E collinear', B, C, E)
    collinear('4-4', 'E, D, F collinear', E, D, F)
    between('4-4', 'C between A and D', A, C, D)
    between('4-4', 'C between B and E', B, C, E)
    between('4-4', 'D between E and F', E, D, F)

    # ---- 4-5(a) : the two halves are congruent copies
    A = (0.60000, 2.90000)
    B = (2.55000, 2.90000)
    C = (3.45000, 2.90000)
    Ap = (5.20000, 2.90000)
    Bp = (7.15000, 2.90000)
    Cp = (8.05000, 2.90000)
    eq('4-5a', 'AB = A\'B\' (double tick)', A, B, Ap, Bp)
    eq('4-5a', 'AC = A\'C\' (arc tick)', A, C, Ap, Cp)
    between('4-5a', 'B between A and C', A, B, C)
    between('4-5a', 'B\' between A\' and C\'', Ap, Bp, Cp)

    # ---- 4-5(b) : CA = BD, order C, A, B, D
    Cb = (2.11900, 1.45000)
    Ab = (2.86900, 1.45000)
    Bb = (5.27600, 1.45000)
    Db = (6.02600, 1.45000)
    eq('4-5b', 'CA = BD', Cb, Ab, Bb, Db)
    between('4-5b', 'A between C and B', Cb, Ab, Bb)
    between('4-5b', 'B between A and D', Ab, Bb, Db)

    # ---- 4-5(c) : AC = BD, order A, B, C, D
    Ac = (1.35000, 0)
    Bc = (3.67000, 0)
    Cc = (4.67000, 0)
    Dc = (6.99000, 0)
    eq('4-5c', 'AC = BD', Ac, Cc, Bc, Dc)
    between('4-5c', 'B between A and C', Ac, Bc, Cc)
    between('4-5c', 'C between B and D', Bc, Cc, Dc)
    on_line('4-5b', 'the drawn line', (0.60, 1.45), (7.60, 1.45),
            [('C', Cb), ('A', Ab), ('B', Bb), ('D', Db)])
    on_line('4-5c', 'the drawn line', (0.60, 0), (7.60, 0),
            [('A', Ac), ('B', Bc), ('C', Cc), ('D', Dc)])

    # ---- 4-6 : Definition 4-1.  AB = A'B'', B' between A' and B''
    A = (0.90000, 1.32000)
    B = (4.55000, 2.28000)
    Ap = (0.85000, 0)
    Bp = (3.32023, 0.09490)
    Bpp = (4.62134, 0.14489)
    eq('4-6', 'AB = A\'B\'\'', A, B, Ap, Bpp)
    between('4-6', 'B\' between A\' and B\'\'', Ap, Bp, Bpp)
    on_line('4-6', "l'", Ap, (5.47071, 0.17752),
            [("B'", Bp), ("B''", Bpp)])

    # ---- 4-7 : Ex 4-3 #1.  AB = CB', with C-B'-D
    A = (1.20000, 0.95000)
    B = (2.40000, 0.95000)
    C = (0.92000, 0)
    Bp = (2.12000, 0)
    D = (3.34000, 0)
    eq('4-7', 'AB = CB\'', A, B, C, Bp)
    between('4-7', 'B\' between C and D', C, Bp, D)
    on_line('4-7', 'upper line', (0.30000, 0.95000), (3.35000, 0.95000),
            [('A', A), ('B', B)])
    on_line('4-7', 'lower line', (0, 0), (4.40000, 0),
            [('C', C), ("B'", Bp), ('D', D)])

    # ---- 4-8 : Ex 4-3 #2.  RS = TS', with T-U-S'
    R = (0.65000, 1.30000)
    S = (3.00000, 1.30000)
    T = (0.62000, 0)
    U = (2.32000, 0)
    Sp = (2.97000, 0)
    eq('4-8', 'RS = TS\'', R, S, T, Sp)
    between('4-8', 'U between T and S\'', T, U, Sp)
    on_line('4-8', 'upper line', (0, 1.30000), (3.60000, 1.30000),
            [('R', R), ('S', S)])
    on_line('4-8', 'lower line', (0, 0), (3.65000, 0),
            [('T', T), ('U', U), ("S'", Sp)])

    # ---- 4-9 : Ex 4-3 #3.  AB = DE, BC = EC'
    A = (0.75000, 0.95000)
    B = (2.60000, 0.95000)
    C = (3.40000, 0.95000)
    D = (0.75000, 0)
    E = (2.60000, 0)
    Cp = (3.40000, 0)
    eq('4-9', 'AB = DE', A, B, D, E)
    eq('4-9', 'BC = EC\'', B, C, E, Cp)
    between('4-9', 'B between A and C', A, B, C)
    between('4-9', 'E between D and C\'', D, E, Cp)
    on_line('4-9', 'upper line', (0, 0.95000), (4.30000, 0.95000),
            [('A', A), ('B', B), ('C', C)])
    on_line('4-9', 'lower line', (0, 0), (4.30000, 0),
            [('D', D), ('E', E), ("C'", Cp)])

    # ---- 4-10 : Thm 4-2.  AB = A'C' (arcs), AC = A'B' (single tick)
    A = (0.30000, 1.15000)
    C = (2.75000, 1.15000)
    B = (3.45000, 1.15000)
    Ap = (0.30000, 0)
    Bp = (2.75000, 0)
    Cp = (3.45000, 0)
    eq('4-10', 'AB = A\'C\'', A, B, Ap, Cp)
    eq('4-10', 'AC = A\'B\'', A, C, Ap, Bp)
    between('4-10', 'C between A and B', A, C, B)
    between('4-10', 'B\' between A\' and C\'', Ap, Bp, Cp)
    on_line('4-10', 'upper line', (0, 1.15000), (3.80000, 1.15000),
            [('A', A), ('C', C), ('B', B)])
    on_line('4-10', 'lower line', (0, 0), (3.80000, 0),
            [("A'", Ap), ("B'", Bp), ("C'", Cp)])

    # ---- 4-11 : AC = A'B', CX = B'C'
    A = (0.60000, 0.95000)
    C = (2.55000, 0.95000)
    X = (3.35000, 0.95000)
    Ap = (0.60000, 0)
    Bp = (2.55000, 0)
    Cp = (3.35000, 0)
    eq('4-11', 'AC = A\'B\'', A, C, Ap, Bp)
    eq('4-11', 'CX = B\'C\'', C, X, Bp, Cp)
    between('4-11', 'C between A and X', A, C, X)
    between('4-11', 'B\' between A\' and C\'', Ap, Bp, Cp)
    on_line('4-11', 'upper line', (0, 0.95000), (4.20000, 0.95000),
            [('A', A), ('C', C), ('X', X)])
    on_line('4-11', 'lower line', (0, 0), (4.20000, 0),
            [("A'", Ap), ("B'", Bp), ("C'", Cp)])

    # ---- 4-12 : Thm 4-3.  AB = A'B' (double tick), AC = A'C' (arcs)
    A = (0.30000, 1.25000)
    B = (2.75000, 1.25000)
    C = (3.50000, 1.25000)
    Ap = (0.30000, 0)
    Bp = (2.75000, 0)
    Cp = (3.50000, 0)
    eq('4-12', 'AB = A\'B\'', A, B, Ap, Bp)
    eq('4-12', 'AC = A\'C\'', A, C, Ap, Cp)
    between('4-12', 'B between A and C', A, B, C)
    between('4-12', 'B\' between A\' and C\'', Ap, Bp, Cp)
    on_line('4-12', 'upper line', (0, 1.25000), (3.90000, 1.25000),
            [('A', A), ('B', B), ('C', C)])
    on_line('4-12', 'lower line', (0, 0), (3.90000, 0),
            [("A'", Ap), ("B'", Bp), ("C'", Cp)])

    # ---- 4-13 : Thm 4-4.  AD' = CD = EF, D' between A and B
    A = (0, 1.45000)
    Dp = (3.34012, 1.70701)
    B = (5.63333, 1.88347)
    C = (0, 0.72000)
    D = (3.33824, 1.00033)
    E = (0, 0)
    F = (3.34776, 0.12274)
    eq('4-13', 'AD\' = CD', A, Dp, C, D)
    eq('4-13', 'CD = EF', C, D, E, F)
    between('4-13', 'D\' between A and B', A, Dp, B)
    on_line('4-13', 'AB', A, B, [("D'", Dp)])
