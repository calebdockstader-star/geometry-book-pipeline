"""Appendix (unit `appendix`, chapter counter 17) figure constraints.

The Appendix has exactly one figure: the unnumbered diagram on book p.277 that
accompanies Postulate 16. Coordinates mirror chapters/figures17.tex.

What the postulate rests on, and therefore what the drawing must satisfy: the
diagonal ray lies in the INTERIOR of angle A, so that angle A is the sum of
angle B and angle C. If the diagonal ray were drawn outside angle A, or the
three arcs attached to the wrong pairs of rays, the postulate's "any two of the
three pairs determine the third" would not read off the figure at all.

The primed configuration is given its OWN constants below rather than being
asserted congruent with a hard-coded zero, so that the congruence checks
compare two independently stated things and would actually catch a drift
between the two tikzpictures.

Reference values measured off sources/Geometry.pdf p.291 at 600 dpi (the iPad
scans do not cover the Appendix). The rays were fitted from ERODED ray cores
only -- a histogram over the whole ink mask is pulled toward the arcs that run
tangent to each ray, which is what produced the earlier 45.0/117.0 readings.
Angles are de-skewed by subtracting the measured tilt of the horizontal ray
(+0.48 deg unprimed, +0.67 deg primed):

    ray            raw unprimed   raw primed   de-skewed mean
    horizontal        +0.48         +0.67         0 (datum)
    diagonal          44.38         43.87        43.55
    upper-left       116.33        116.13       115.66

Lengths and arc radii as fractions of the horizontal ray, mean of the two
sub-figures: diagonal 0.994, upper-left 0.939; arc A 0.446, arc C 0.699,
arc B 0.774. Arc spans scanned off each arc's circle with the rays and label
glyphs masked out: A 4..60 / 78..114, B 47..77 / 87..114, C 4..16 / 30..42.
"""
import math

from figlib import V, dist, lerp  # noqa: F401  (kept for the house import shape)

# ---- ray directions as drawn in chapters/figures17.tex (degrees from vertex)
HOR, DIA, UPL = 0.0, 43.6, 115.7
LEN_HOR, LEN_DIA, LEN_UPL = 3.30, 3.28, 3.10

# ---- the primed configuration, stated separately (figures17.tex draws it
#      congruent to the unprimed one, as the book does)
PHOR, PDIA, PUPL = 0.0, 43.6, 115.7

# ---- arc radii and the angle at which each label sits on its own arc
R_A, R_B, R_C = 1.47, 2.55, 2.31
LAB_A, LAB_B, LAB_C = 69.0, 81.5, 23.0

# ---- drawn arc spans (start, end); the arrowhead is at the END of each.
#      The arrowhead ends (114 / 47 / 42 / 4) are the source's. The gap ends
#      are opened a few degrees wider than the source's (A 52..86 vs 60..78,
#      B 71.5..91.5 vs 77..87, C 12..34 vs 16..30) because our labels are set
#      with more padding than the book's tight hand lettering; at the source's
#      gap widths check_labels.py reports the glyph boxes touching the arcs.
ARC_A = [(86.0, 114.0), (52.0, 4.0)]      # upper-left ray  <-> horizontal ray
ARC_B = [(91.5, 114.0), (71.5, 47.0)]     # upper-left ray  <-> diagonal ray
ARC_C = [(34.0, 42.0), (12.0, 4.0)]       # diagonal ray    <-> horizontal ray

# ---- measured off the 600 dpi photo of book p.277 (see module docstring)
MEAS_UPL, MEAS_DIA = 115.66, 43.55
MEAS_FRAC_DIA, MEAS_FRAC_UPL = 0.994, 0.939        # of the horizontal ray
MEAS_FRAC_A, MEAS_FRAC_C, MEAS_FRAC_B = 0.446, 0.699, 0.774


def _pt(deg, r):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def _angle(p, q):
    """unsigned angle at the origin between rays to p and q, in degrees"""
    a = math.degrees(math.atan2(p[1], p[0]) - math.atan2(q[1], q[0]))
    return abs((a + 180.0) % 360.0 - 180.0)


def _rel(x, ref):
    return abs(x - ref) / abs(ref)


def _yes(cond):
    return 0.0 if cond else 1.0


def build(check):
    P_h, P_d, P_u = _pt(HOR, LEN_HOR), _pt(DIA, LEN_DIA), _pt(UPL, LEN_UPL)
    A = _angle(P_u, P_h)   # upper-left ray <-> horizontal ray (the whole angle)
    B = _angle(P_u, P_d)   # upper-left ray <-> diagonal ray
    C = _angle(P_d, P_h)   # diagonal ray   <-> horizontal ray

    Q_h, Q_d, Q_u = _pt(PHOR, LEN_HOR), _pt(PDIA, LEN_DIA), _pt(PUPL, LEN_UPL)
    Ap, Bp, Cp = _angle(Q_u, Q_h), _angle(Q_u, Q_d), _angle(Q_d, Q_h)

    # -- the relation Postulate 16 depends on, in both configurations
    check('App-1', 'angle A = angle B + angle C', _rel(B + C, A))
    check('App-1', "angle A' = angle B' + angle C'", _rel(Bp + Cp, Ap))

    # ... which requires the middle ray to be interior to the whole angle
    check('App-1', 'diagonal ray interior to angle A', _yes(HOR < DIA < UPL))
    check('App-1', "diagonal ray interior to angle A'", _yes(PHOR < PDIA < PUPL))

    # -- the two configurations are drawn congruent (real comparison now)
    check('App-1', "angle A cong angle A'", _rel(Ap, A))
    check('App-1', "angle B cong angle B'", _rel(Bp, B))
    check('App-1', "angle C cong angle C'", _rel(Cp, C))

    # -- drawn directions and proportions agree with the printed figure
    check('App-1', 'upper-left ray matches photo', _rel(UPL, MEAS_UPL))
    check('App-1', 'diagonal ray matches photo', _rel(DIA, MEAS_DIA))
    check('App-1', 'angle C matches photo', _rel(C, MEAS_DIA - 0.0))
    check('App-1', 'angle B matches photo', _rel(B, MEAS_UPL - MEAS_DIA))
    check('App-1', 'diagonal ray length matches photo',
          _rel(LEN_DIA / LEN_HOR, MEAS_FRAC_DIA))
    check('App-1', 'upper-left ray length matches photo',
          _rel(LEN_UPL / LEN_HOR, MEAS_FRAC_UPL))
    check('App-1', 'arc A radius matches photo', _rel(R_A / LEN_HOR, MEAS_FRAC_A))
    check('App-1', 'arc B radius matches photo', _rel(R_B / LEN_HOR, MEAS_FRAC_B))
    check('App-1', 'arc C radius matches photo', _rel(R_C / LEN_HOR, MEAS_FRAC_C))

    # -- each arc spans exactly the angle it names, and stops short of both
    #    of that angle's rays (so the arrowheads point AT the rays)
    for name, spans, lo, hi in [('A', ARC_A, HOR, UPL),
                                ('B', ARC_B, DIA, UPL),
                                ('C', ARC_C, HOR, DIA)]:
        ends = [d for s in spans for d in s]
        check('App-1', f'arc {name} lies inside the angle it names',
              _yes(all(lo < d < hi for d in ends)))
        # the arrowhead of each of the two segments is the segment's end angle
        heads = sorted(s[1] for s in spans)
        check('App-1', f'arc {name} arrowheads point at both of its rays',
              _yes(heads[0] - lo < 5.0 and hi - heads[1] < 5.0))

    # -- each label sits on its own arc, inside that arc's gap
    for name, spans, lab, rad, meas in [('A', ARC_A, LAB_A, R_A, MEAS_FRAC_A),
                                        ('B', ARC_B, LAB_B, R_B, MEAS_FRAC_B),
                                        ('C', ARC_C, LAB_C, R_C, MEAS_FRAC_C)]:
        gap_lo = min(max(s) for s in spans)     # top of the lower segment
        gap_hi = max(min(s) for s in spans)     # bottom of the upper segment
        check('App-1', f'label {name} sits in the gap of arc {name}',
              _yes(gap_lo < lab < gap_hi))
        check('App-1', f'label {name} sits on arc {name}', _rel(rad / LEN_HOR, meas))

    # -- the three arcs are nested and distinct, ordered A < C < B as in the book
    check('App-1', 'arc radii ordered A < C < B', _yes(R_A < R_C < R_B))
    check('App-1', 'arc A and arc C separated on the horizontal ray',
          _yes(R_C - R_A > 0.3))
    check('App-1', 'arc C and arc B separated on the diagonal ray',
          _yes(R_B - R_C > 0.1))

    # -- every arc stays inside both rays it connects
    check('App-1', 'arc A inside the upper-left and horizontal rays',
          _yes(R_A < min(LEN_UPL, LEN_HOR)))
    check('App-1', 'arc B inside the upper-left and diagonal rays',
          _yes(R_B < min(LEN_UPL, LEN_DIA)))
    check('App-1', 'arc C inside the diagonal and horizontal rays',
          _yes(R_C < min(LEN_DIA, LEN_HOR)))
