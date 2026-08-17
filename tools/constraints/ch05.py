# Chapter 5 figure constraints. Coordinates mirror chapters/figures05.tex.
# Chapter 5's figures are all number-line diagrams, so the stated hypotheses
# are congruence of laid-off unit segments, betweenness, ORDER of the laid-off
# points, midpoints, and integer multiples of the unit -- not
# parallels/perpendiculars.
from figlib import dist, lerp


def between(t):
    """0 when the parameter t puts the point strictly inside the segment."""
    return max(0.0, -t) + max(0.0, t - 1.0)


def relerr(a, b):
    return abs(a - b) / abs(b) if b else abs(a - b)


def ordered(xs):
    """0 when the abscissas are strictly increasing, i.e. the points are
    'arranged in this order' (Archimedes' postulate IV-1)."""
    return sum(1.0 for a, b in zip(xs, xs[1:]) if not a < b)


def build(check):
    # ---- 5-2 : AA1 = A1A2 = A2A3 = A3A4 = CD (the unit); B between A3, A4
    u = 1.75
    A = (0, 0)
    A1, A2, A3, A4 = ((u, 0), (2 * u, 0), (3 * u, 0), (4 * u, 0))
    B = (3.36 * u, 0)
    C, D = (0.52 * u, -0.61), (1.52 * u, -0.61)
    check('5-2', 'CD is the unit', relerr(dist(C, D), u))
    for nm, P, Q in (('AA1', A, A1), ('A1A2', A1, A2),
                     ('A2A3', A2, A3), ('A3A4', A3, A4)):
        check('5-2', '%s congruent to CD' % nm, relerr(dist(P, Q), dist(C, D)))
    check('5-2', 'B between A3 and A4', between((B[0] - A3[0]) / (A4[0] - A3[0])))
    check('5-2', 'A3 between A and B', between((A3[0] - A[0]) / (B[0] - A[0])))
    check('5-2', 'A, A1, A2, A3, B, A4 in this order',
          ordered([A[0], A1[0], A2[0], A3[0], B[0], A4[0]]))
    check('5-2', 'A1 on the same side of A as B',
          0.0 if (A1[0] - A[0]) * (B[0] - A[0]) > 0 else 1.0)
    check('5-2', 'the unit CD is drawn clear of the line l',
          0.0 if C[1] < A[1] and D[1] < A[1] else 1.0)

    # ---- 5-3 : unit too large -- B lies between A and A1
    u = 1.75
    A, B, A1 = (0, 0), (0.32 * u, 0), (u, 0)
    check('5-3', 'B between A and A1', between((B[0] - A[0]) / (A1[0] - A[0])))
    check('5-3', 'A, B, A1 in this order', ordered([A[0], B[0], A1[0]]))

    # ---- 5-4 : Archimedes' integer n = 4, with B = A4 exactly
    u = 1.75
    P = [(k * u, 0) for k in range(5)]          # A=A0, A1, A2, A3, A4=B
    B = P[4]                                    # the plate labels A4 = B
    C, D = (0.52 * u, -0.61), (1.52 * u, -0.61)
    check('5-4', 'CD is the unit', relerr(dist(C, D), u))
    for k in range(4):
        check('5-4', 'A%dA%d congruent to CD' % (k, k + 1),
              relerr(dist(P[k], P[k + 1]), dist(C, D)))
    check('5-4', 'B = A4 exactly', dist(B, P[4]))
    check('5-4', 'A0..A4 arranged in this order', ordered([p[0] for p in P]))
    check('5-4', 'the unit CD is drawn clear of the line',
          0.0 if C[1] < P[0][1] and D[1] < P[0][1] else 1.0)

    # ---- 5-5 : n = 4 again, but B strictly between A3 and A4
    u = 1.75
    Q = [(k * u, 0) for k in range(5)]
    B = (3.18 * u, 0)
    for k in range(4):
        check('5-5', 'A%dA%d equal units' % (k, k + 1),
              relerr(dist(Q[k], Q[k + 1]), u))
    check('5-5', 'B between A3 and A4',
          between((B[0] - Q[3][0]) / (Q[4][0] - Q[3][0])))
    check('5-5', 'A0..A3, B, A4 arranged in this order',
          ordered([Q[0][0], Q[1][0], Q[2][0], Q[3][0], B[0], Q[4][0]]))

    # ---- 5-6 : the unit interval CD cut into ten congruent parts
    C, D = (0, 0), (1, 0)
    marks = [(k / 10.0, 0) for k in range(11)]
    check('5-6', 'CD divided into tenths: 9 interior marks',
          abs(len(marks) - 2 - 9))
    for k in range(10):
        check('5-6', 'tenth %d congruent' % (k + 1),
              relerr(dist(marks[k], marks[k + 1]), dist(C, D) / 10.0))

    # ---- 5-7 : AB is about 2.3 units; CD alongside, also cut into tenths
    u = 1.9
    A, A1, A2 = (0, 0), (u, 0), (2 * u, 0)
    B = (2.30 * u, 0)
    C, D = (2.64 * u, 0), (3.64 * u, 0)
    check('5-7', 'CD is the unit', relerr(dist(C, D), u))
    check('5-7', 'AA1 congruent to CD', relerr(dist(A, A1), dist(C, D)))
    check('5-7', 'A1A2 congruent to CD', relerr(dist(A1, A2), dist(C, D)))
    check('5-7', 'AB = 2.3 units', relerr(dist(A, B) / dist(C, D), 2.3))
    check('5-7', 'B between A2 and A2+unit',
          between((B[0] - A2[0]) / u))
    check('5-7', 'A, A1, A2, B in this order', ordered([A[0], A1[0], A2[0], B[0]]))
    check('5-7', 'the unit CD is drawn clear to the right of B',
          0.0 if C[0] > B[0] else 1.0)
    tenths = [(C[0] + k * u / 10.0, 0) for k in range(11)]
    for k in range(10):
        check('5-7', 'CD tenth %d congruent' % (k + 1),
              relerr(dist(tenths[k], tenths[k + 1]), dist(C, D) / 10.0))

    # ---- 5-8 : Thm 5-2 given |AB| = |A'B'|, so AB is DRAWN congruent to
    # A'B'.  B'' (the point the proof assumes distinct from B, for
    # contradiction) is drawn between A and B, so AB'' is drawn shorter than
    # A'B' -- that is the book's own plate, not an error.
    L = 4.6
    Ap, Bp = (0, 0.80), (L, 0.80)
    A, Bpp, B = (0, 0), (0.77 * L, 0), (L, 0)
    check('5-8', "AB drawn congruent to A'B' (given |AB| = |A'B'|)",
          relerr(dist(A, B), dist(Ap, Bp)))
    check('5-8', "A directly below A' (rows left-aligned)", abs(A[0] - Ap[0]))
    check('5-8', "B directly below B' (rows right-aligned)", abs(B[0] - Bp[0]))
    check('5-8', "AB'' drawn shorter than A'B' (the B'' != B case)",
          0.0 if dist(A, Bpp) < dist(Ap, Bp) else 1.0)
    check('5-8', "B'' between A and B", between((Bpp[0] - A[0]) / (B[0] - A[0])))
    check('5-8', "B'' on the same side of A as B",
          0.0 if (Bpp[0] - A[0]) * (B[0] - A[0]) > 0 else 1.0)

    # ---- 5-9 : AB = CE with D between C and E
    L = 4.6
    A, B = (0, 0.75), (L, 0.75)
    C, D, E = (0, 0), (0.66 * L, 0), (L, 0)
    check('5-9', 'AB congruent to CE', relerr(dist(A, B), dist(C, E)))
    check('5-9', 'D between C and E', between((D[0] - C[0]) / (E[0] - C[0])))
    check('5-9', 'C directly below A (rows left-aligned)', abs(C[0] - A[0]))
    check('5-9', 'C, D, E in this order', ordered([C[0], D[0], E[0]]))
    check('5-9', 'D on the same side of C as E',
          0.0 if (D[0] - C[0]) * (E[0] - C[0]) > 0 else 1.0)
    check('5-9', 'CD drawn shorter than CE (AB > CD)',
          0.0 if dist(C, D) < dist(C, E) else 1.0)

    # ---- 5-10 : E is the midpoint of the unit CD; AB = 3 CD = 6 ED
    u = 1.25
    C, E, D = (0, 0), (0.5 * u, 0), (u, 0)
    check('5-10', 'E is the midpoint of CD',
          relerr(dist(C, E), dist(E, D)))
    check('5-10', 'E is on CD at t = 1/2',
          dist(E, lerp(C, D, 0.5)) / u)
    A, B = (1.55 * u, 0.55), (4.55 * u, 0.55)
    check('5-10', 'AB = 3 units of CD', relerr(dist(A, B) / dist(C, D), 3.0))
    check('5-10', 'AB = 6 units of ED', relerr(dist(A, B) / dist(E, D), 6.0))
    E2, D2 = (5.15 * u, 0.30), (5.65 * u, 0.30)
    check('5-10', 'the ED shown alongside is half of CD',
          relerr(dist(E2, D2), dist(C, D) / 2.0))
    check('5-10', 'the ED alongside is congruent to ED on CD',
          relerr(dist(E2, D2), dist(E, D)))
    ticks = [(A[0] + k * u, 0.55) for k in range(4)]
    for k in range(3):
        check('5-10', 'AB third %d congruent to CD' % (k + 1),
              relerr(dist(ticks[k], ticks[k + 1]), dist(C, D)))
    check('5-10', 'AB last tick lands exactly on B', dist(ticks[3], B))
    # the brace over CD spans exactly CD, and its "1" is centred on it
    brace = ((0, 0.16), (1 * u, 0.16))
    check('5-10', 'the brace spans exactly CD',
          relerr(dist(*brace), dist(C, D)))
    check('5-10', 'the brace label 1 is centred over CD',
          abs(0.5 * u - (brace[0][0] + brace[1][0]) / 2.0) / u)
    # the "1" under AB is centred on AB's first third
    check('5-10', 'the label 1 is centred under AB first third',
          abs(2.05 * u - (ticks[0][0] + ticks[1][0]) / 2.0) / u)
    check('5-10', 'CD, AB and the ED alongside do not overlap',
          0.0 if D[0] < A[0] and B[0] < E2[0] else 1.0)
