"""figlib.py -- shared geometry helpers for per-chapter figure constraints.

Chapter constraint modules (tools/constraints/chNN.py) do:

    from figlib import V, ang, par, perp, lerp, dist, foot

    def build(check):
        A, B = (0,0), (4,0)
        check('11-3', 'AB horizontal', par(V(A,B), (1,0)))

check(fig, what, err, tol=0.05) records one constraint; err <= tol passes.
Errors are degrees for par/perp, relative for ratios.
"""
import math


def V(p, q):
    return (q[0] - p[0], q[1] - p[1])


def ang(v):
    return math.degrees(math.atan2(v[1], v[0])) % 180


def par(u, v):
    d = abs(ang(u) - ang(v))
    return min(d, 180 - d)


def perp(u, v):
    return abs(par(u, v) - 90)


def lerp(p, q, t):
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))


def dist(p, q):
    return math.hypot(*V(p, q))


def foot(a, b, p):
    """perpendicular foot of p on line ab"""
    ab, ap = V(a, b), V(a, p)
    t = (ap[0] * ab[0] + ap[1] * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)
    return lerp(a, b, t)


TOL = 0.05
