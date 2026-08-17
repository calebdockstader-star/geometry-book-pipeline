# Chapter 4 — Congruence of Segments — uncertainty log

Source: `sources/Geometry.pdf` PDF pp. 77–86 = book pp. 63–72.
Figure cross-check: `scans/scan05.pdf` pp. 6–12 (= book pp. 63–69).
Status: compiles twice clean · 105/105 constraints · 0 label collisions ·
all 13 figures visually inspected and structurally verified against the scans.
(Figure-reviewed 2026-08-17 — see "Figure review" at the foot of this file;
the builder's 50/50 became 105/105 after incidence checks were added, and one
real defect in Fig. 4-2 was fixed.)

---

## Questions for Caleb

### 1. Figure 4-1 is a pictorial illustration, not a diagram
Fig. 4-1 (book p. 63) is a small figurative line drawing: a boy standing on
hatched ground beside a marked spear planted upright, point above his head.
It is line art, not a halftone, so it is not literally a "plate" — but it is
not redrawable as TikZ geometry either. I applied the plate rule and inserted
a **framed placeholder carrying the original caption**. Options:
  a. leave the placeholder,
  b. crop the drawing from the scan and include it as a raster image,
  c. commission/redraw a vector vignette.
**Not decided — needs your call.**

### 2. Segment notation differs from ch09
This chapter's source prints segments as **plain italic `AB`, with no
overbar** (verified at 300 dpi on p. 65 — e.g. the III-2 congruence list).
I transcribed it that way, so ch04 uses `$AB$` while `chapters/ch09.tex` uses
`\sg{AB}` (overbarred). One of the two is inconsistent with the other at book
level. Worth checking whether ch09's source actually prints overbars, or
whether ch09 added them. **Whole-book consistency decision.**

---

## Verified oddities (transcribed faithfully — not errors)

- **p. 64, end of §4-1:** the book reads "We shall see in **the** Section 4-2
  how in geometry we can avoid carrying such sticks." The stray "the" is the
  book's own wording; confirmed at 300 dpi. Left as printed.
- **Def. 4-2 symbols** are `≧` / `≦` (double bar, `\geqq` / `\leqq`), not
  `≥`/`≤`. Confirmed on both the photo PDF and scan05 p. 12.
- **Theorem 4-2** carries a dagger and a *marker-less* footnote ("Although
  this theorem is intuitively obvious, its proof is quite difficult. If the
  teacher wishes, it may be treated as a postulate."). amsthm cannot put the
  dagger before "Theorem", so this one theorem is set by hand with
  `\refstepcounter{theorem}` — numbering still runs 4-1 … 4-4 correctly.
- **No `\starnote` in this chapter.** Starred exercises appear (Ex 4-2 #13,
  #14, #16; Ex 4-4 #9–#12, #14) but the book footnotes the convention only
  once, at first use, which is in ch02. Nothing to emit here.

---

## Layout deviations from the printed page

- The book interleaves figures *inside* its two-column exercise blocks
  (Fig. 4-4 mid-column, Fig. 4-5 at the foot of p. 66; Figs. 4-7/4-8 in the
  left column and 4-9 in the right on p. 68). Placing floats inside
  `multicol` is fragile, so **figures are emitted immediately after their
  exercise list** instead. All in-text references are by figure number, so
  reading order is preserved. Re-flow at book-assembly time if wanted.
- Fig. 4-1 is text-wrapped at the right margin in the book (`wrapfig`
  behaviour). `brumfiel.sty` does not load `wrapfig` and I must not edit it,
  so the placeholder is a centred block.

---

## Tooling: two false-positive classes in `tools/check_labels.py`

`check_labels.py chapters/figures04.tex 04` reports **27 collisions**. I
verified every one; **all 27 are tool artifacts. Real collisions: 0.**
Confirmed by re-running the same distance test against the *true* line
endpoints (`page.lines[...]['pts']`) — script kept at
`…/scratchpad/ch04/truecheck.py`, which reports `0 real collisions, 37 tight`.

**Bug A — ascending lines are mirrored (3 of the 27).**
`geometry_segments()` rebuilds each line as `(x0, top) → (x1, bottom)`. That
is only correct for lines that *descend* left-to-right. For a line that
ascends, the true endpoints are `(x0, bottom) → (x1, top)`, so the tool tests
against a **phantom segment mirrored about the horizontal**, which crosses the
real line and diverges by up to ~50 pt at the ends. Fig. 4-2 / 4-3 both have
ascending lines, and the phantom lands exactly where the `A` labels sit.
Measured: tool distance 0.00 pt, **true** distance 1.85 pt and 2.02 pt.
*Fix:* use `ln['pts']` directly instead of the `top`/`bottom` bbox corners.
This will mis-report in every chapter that has lines rising to the right.

**Bug B — primed labels self-collide (24 of the 27).**
`page.extract_words()` splits `$A'$` into two objects (the letter sits on the
baseline, the prime is raised), so every primed label is reported as colliding
with its own prime: `[COLLIDE] "B" vs label ′ d=0.00pt`. Ch. 4 has 24 primed
labels, hence 24 reports. *Fix:* merge words whose bboxes are contiguous and
whose baselines differ by less than the superscript rise, or ignore `′`.

One collision found this way **was real** and is fixed: `B'` in Fig. 4-2
(true distance 0.00 pt) — its label separation is now 4.8 pt.

---

## Figures — how each was pinned

All 13 constrained in `tools/constraints/ch04.py` (50 checks, all exact to
0.0000). Every congruence the printed figure asserts via tick marks, arcs, or
postulate hypotheses is enforced, plus the betweenness/collinearity each
figure depends on.

| Fig | Enforced | Scan check |
|-----|----------|-----------|
| 4-1 | — (placeholder) | scan05 p6 |
| 4-2 | `AB = A'B'` | scan05 p8 |
| 4-3 | `AB = A'B'`, `BC = B'C'`, both betweennesses | scan05 p8 |
| 4-4 | `AB=BC`, `CD=CE=ED`, `EF=EB`, 3 collinearities | scan05 p9 |
| 4-5 | (a) `AB=A'B'`, `AC=A'C'`; (b) `CA=BD`; (c) `AC=BD` | scan05 p9 |
| 4-6 | `AB = A'B''`, `B'` between `A'` and `B''` | scan05 p10 |
| 4-7 | `AB = CB'`, `B'` between `C` and `D` | photo p. 68 @300 dpi |
| 4-8 | `RS = TS'`, `U` between `T` and `S'` | photo p. 68 @300 dpi |
| 4-9 | `AB = DE`, `BC = EC'` | photo p. 68 @300 dpi |
| 4-10 | `AB = A'C'`, `AC = A'B'` | scan05 p12 |
| 4-11 | `AC = A'B'`, `CX = B'C'` | scan05 p12 |
| 4-12 | `AB = A'B'`, `AC = A'C'` | scan05 p12 |
| 4-13 | `AD' = CD = EF`, `D'` between `A` and `B` | scan05 p12 |

**Fig. 4-4 construction note.** The four stated congruences are not
independent. Placing `A`, `C`, `D` collinear and `E` as the equilateral apex
on `CD` forces ∠ACB = 60°, so `AB = BC` makes △ABC equilateral with
`AB = BC = AC`. The book's own drawing measures that way (AB≈358, BC≈376,
AC≈360 px), so this is the book's figure, not an over-constraint — but it is
a derived fact worth knowing if anyone re-scales it.

**Fig. 4-7 lines drawn horizontal.** The photo shows a slight tilt; that is
page curvature near the gutter, not the printed artwork. Drawn horizontal.

**Minor, accepted:** in Fig. 4-10 the `C` and `B` labels sit close together
(0.95–1.08 pt from the geometry, flagged TIGHT). The book crowds them the
same way. Eyeballed at 110 dpi and 130 dpi — legible; left as is.

---

## Text checks performed

- Every exercise number diffed against the source: Ex 4-1 (1–2), Ex 4-2
  (1–16, starred 13/14/16), Ex 4-3 (1–6), Ex 4-4 (1–14, starred 9/10/11/12/14
  — **13 is not starred**), Review true/false (1–10), Review justify (11–20),
  Algebra Review (1–10). **68 items, all present and correctly numbered.**
- Spot-diffed at 300 dpi: §4-1 opening, §4-2 "equal"/"congruent" paragraph,
  III-1/III-2/III-3 statements, Definition 4-1, the Remark, Theorem 4-2 proof
  and its footnote, Definition 4-2, Theorem 4-4 proof, the Algebra Review
  definitions and worked example (`-3/2 = -5/2 + 2/2`; `0 = 3/4 - 3/4`).
- Caught and fixed during the visual pass: the feet/inches marks in the
  Review ("a 6'8" basketball center") were set with `\rlap` and collapsed into
  the following word; now plain math (`$6'8''$`).

## Not doubtful, recorded for the integration agent

- Local macros are in `ch04.tex` between the hoist markers: `IVproblem`
  (the book's run-in *Problem.* paragraphs) and `\IVhead` (the centred
  "REVIEW OF CHAPTER 4" / "ALGEBRA REVIEW" display headings).
- `figures04.tex` is deliberately self-contained — congruence ticks are
  explicit strokes, not macros — because `check_labels.py` compiles the
  figures file against `brumfiel.sty` alone and would fail on any helper
  defined in `ch04.tex`.
- TOC lines added for the chapter, §4-1…§4-4, "Review of Chapter 4" and
  "Algebra Review".
- `\markboth` is switched to `REVIEW OF CHAPTER 4` at the review, matching the
  book's running head on pp. 71–72.

---

## Text review

Fresh adversarial pass, 2026-08-17, against PDF pp. 77–86 (book pp. 63–72)
rasterised at 150 dpi for reading and 300 dpi for every symbol-level check.
**Corrections applied: 0.** The transcription is verbatim; no dropped,
paraphrased, or renumbered material was found.

### What was checked, and how

- **Every paragraph opening on all ten pages**, plus full word-level diffs of:
  §4-1 ¶1–¶3 and the *Problem*; §4-2 all four paragraphs (incl. the italic
  run in the Euclid paragraph, which starts at "in this book" and closes
  after "the same."); §4-3 III-1/III-2(a,b,c)/III-3(a,b), the *Problem*, and
  both closing paragraphs; §4-4 ¶1–¶2, Definition 4-1, the Remark,
  Theorem 4-1, the pre-Theorem-4-2 paragraph, Theorem 4-2 + dagger footnote,
  the whole proof through "…we have $A'B' < AB$", Theorem 4-3 + proof and
  its follow-up paragraph, Definition 4-2, Theorem 4-4 + proof; all five
  Review paragraphs; the Algebra Review preamble, definitions (1)–(2), and
  worked example.
- **All 68 exercise items** re-diffed independently of the builder's pass and
  counted mechanically out of the tex (2 / 16 / 6 / 14 / 10 / 10 / 10 —
  matches the source group-for-group). Every embedded datum verified:
  12 miles, 153 feet, `6'8''`/`6'2''`, 240-lb/180-lb, `-3/2 = -5/2 + 2/2`,
  `0 = 3/4 - 3/4`, `0 > -4/3`, `a = b+1`, `b = c+2`, `a = b-2`, `b = c-3`,
  `a = b+3`, `3a > 3b`, `-2a < -2b`, `5 > 3`, `5 = 3+2`.
- **Stars.** Ex 4-2 #13/#14/#16 and Ex 4-4 #9–#12/#14 confirmed starred at
  300 dpi; **Ex 4-4 #13 and Ex 4-2 #15 confirmed *not* starred**. All eight
  use `\item[\stex n.]`, which is the same construction ch02/ch07/ch09/ch12
  use. Absence of `\starnote` re-confirmed correct: no star footnote is
  printed anywhere on pp. 63–72.
- **Math/symbols.** All primes and double primes re-read at 300 dpi —
  in particular III-3, Definition 4-1, and the Remark, where `B'` vs `B''`
  carries the argument; a suspected `C''` in III-3 resolved to `C'` (photo
  artifact). `≅`/`≇`/`≠` usages all match. `\geqq`/`\leqq` re-confirmed as
  double-bar glyphs in Review #13 and Definition 4-2 — the builder's reading
  is right. No Greek letters occur in this chapter.
- **Structure.** Four `\section*` headings verbatim and in order; exercise
  groups 4-1…4-4 land at the right places in the text; `\addcontentsline`
  present after `\chapter*` and after all six headings (4 sections + the two
  display headings). Theorem/Definition counters render 4-1…4-4 and 4-1/4-2
  correctly in the built PDF, including the hand-set dagger Theorem 4-2 and
  its marker-less footnote. Chapter opener matches the ch03/ch05/ch08
  pattern. No page-order errors: content follows the recto/verso spread
  sequence 63→72 exactly.
- Recompiled twice after review: clean, only two cosmetic
  `Underfull \hbox` warnings (ch04.tex:270 and :388 — last items of exercise
  lists inside `multicols`).

### Residual doubts

1. **Running head at the Review (new).** `\markboth{REVIEW OF CHAPTER 4}{}`
   sets the *verso* head. In the book the verso head on p. 72 is still
   `CONGRUENCE OF SEGMENTS`; it is the *recto*, p. 71, that reads
   `REVIEW OF CHAPTER 4`. The book generally runs chapter title on verso and
   section title on recto, whereas every unit in this project uses
   `\markboth{TITLE}{}` and leaves recto heads empty. `ch01.tex:649` makes
   the identical switch at its own review. Left unchanged — this is a
   book-wide running-head decision for the integration agent, not a ch04
   bug. If the recto heads are ever populated, the fix here is
   `\markboth{CONGRUENCE OF SEGMENTS}{REVIEW OF CHAPTER 4}`.
2. The builder's two open questions for Caleb (Fig. 4-1 pictorial
   placeholder; unbarred `AB` vs ch09's `\sg{AB}`) stand. On the second, this
   review independently confirms the ch04 source pages print segments
   **unbarred**, so ch04 is faithful to its own pages — the inconsistency, if
   any, is on the ch09 side.
3. Figure geometry was not re-examined (out of scope for the text pass); the
   figure-review agent still owns Figs. 4-1…4-13.

---

## Figure review

Fresh adversarial pass, 2026-08-17, by an agent that did not draw these
figures. All 13 figure blocks re-examined against `sources/Geometry.pdf`
pp. 77-86 and `scans/scan05.pdf` pp. 8-12. **Corrections applied: 3.**
Final state: compiles twice clean (no new warnings) · **105/105 constraints**
(was 50/50) · **0 collisions** · every figure page rasterised and read.

### 1. Real defect found and fixed — Fig. 4-2's primed points were off their line

`B'` floated **2.16 pt clear of line l'**, and `A'` 0.37 pt clear. The dots
did not sit on the stroke they are drawn on.

The builder's 50 checks could not see this: they tested *lengths* (`AB = A'B'`)
and *betweenness*, both of which a floating point satisfies perfectly. Nothing
tested **incidence with the drawn line** — yet Postulate III-1 states `A'` and
`B'` as points *on l'*, so incidence is a stated hypothesis, not decoration.

Fixed by snapping both points onto `l'` (keeping `A'` at its drawn x, then
stepping `|AB|` along the line's unit vector, so `AB = A'B'` stays exact):

    Ap (1.55000,-0.55000) -> (1.55000,-0.53479)
    Bp (5.00754,-0.83427) -> (5.01280,-0.74609)

**Guard added.** `tools/constraints/ch04.py` gained an `on_line()` helper and
**55 incidence checks** covering every labelled point against the line the
figure actually strokes, in all 13 figures. 50 -> 105 checks, all exact.
A point can no longer drift off its line and still score 100%.

### 2. Fig. 4-2's `outer sep=4.8pt` shim on `B'` removed

That shim was compensating for the off-line point (the builder logged it as
"a real collision, now 4.8 pt"). With `B'` back on `l'` the label clears at
0.86 pt unaided — the same clearance `A'` has. scan05 p8 shows `A'` and `B'`
labelled at equal small offsets above the line, so the shim was also a
departure from the book. Removed; the two labels now sit symmetrically.

### 3. `tools/check_labels.py` — three false-positive classes fixed (shared tool)

The audit reported **26 collisions** for this chapter. **All 26 were tool
artifacts**; the two bugs the builder documented are real, and a third was
found here. Each was verified from the PDF before being fixed.

- **Bug A — ascending lines mirrored** (builder-reported, confirmed).
  `geometry_segments()` rebuilt every line as `(x0,top)->(x1,bottom)`, which
  is correct only for lines descending left-to-right. Probing `ln['pts']`
  showed *every* diagonal in ch04 ascends, so the tool was testing labels
  against a phantom segment mirrored about the horizontal. Now uses the real
  endpoints.
- **Bug B — primes split from their labels** (builder-reported, confirmed).
  `extract_words()` returns `$A'$` as `['A','′']`, so every primed label was
  reported as colliding with its own prime. Added `merge_scripts()`, which
  rejoins a fragment only when it is horizontally contiguous, vertically
  overlapping, and on a *different baseline* — two labels sharing a baseline
  are never merged, so genuine label-vs-label collisions still report.
- **Bug C — a prime's metric box overshoots its ink by ~4 pt (new).**
  With A and B fixed, 10 collisions remained, all primed labels anchored
  *below* a line, all at 0.15-0.27 pt. Measured against the 600 dpi raster
  (fig. 4-11): the real gap from the line to the prime's ink is **4.20 pt**,
  and to the letter's ink 5.16 pt. Cause: the prime is set in **CMSY10** and
  pdfplumber gives every char that font's *ascent* rather than the glyph's
  ink, so the prime's box top lands 4.03 pt above the host letter's box top
  while its ink sits 0.96 pt *below* it. A text letter's box overshoots its
  ink by only ~1 pt, which is what the TOUCH/TIGHT thresholds are calibrated
  against. Fixed by taking a prime's *horizontal* extent (advance widths are
  reliable) and keeping the host's vertical extent.
  **These labels were left where the book puts them — the measurement was
  wrong, not the figure.**

This fix is in a shared tool and should clear the same false positives logged
against ch01, ch03, ch07 and the appendix. Those chapters' remaining counts
were not otherwise touched and still need their own review.

### 4. Structure checked against the scans

Every figure with >5 labels was cropped from scan05 and compared vertex by
vertex (fractions are positions along the drawn line, scan vs redraw):

| Fig | Scan | Verdict |
|-----|------|---------|
| 4-2 | p8 | order, slopes, label sides match; `A'` at 0.149 vs 0.149 |
| 4-3 | p8 | all six points exactly on their lines; order correct |
| 4-4 | p9 | zigzag A-B-E-F crossing A-D at C and D confirmed; C and D are true intersections |
| 4-5 | p9 | (a) double tick on the line, single on the arc; (b) `CA`,`BD` ticks; (c) two overlapping arcs — all match. (c) `(C-B)/(B-A)` 0.430 vs 0.433 |
| 4-6 | p10 | `B'` at 0.655 of `A'B''` vs 0.656; `B''` at 0.816 vs 0.823 |
| 4-10 | p12 | arcs above/below, `then`/`if` arrow directions and label sides all match |
| 4-11 | p12 | single tick `A'B'`, double tick `B'C'` — matches |
| 4-12 | p12 | both arcs dip *below* their lines, arrow from `B` — matches |
| 4-13 | p12 | `AD' = CD = EF`, `D'`/`D`/`F` vertically aligned — matches |

Tick placement was verified arithmetically for every figure: each tick sits at
the midpoint of the segment it marks, and each arc tick at the arc's Bezier
midpoint. No tick marks the wrong segment.

### Residual doubts

1. **Fig. 4-13 line slopes.** The three segments are drawn at 7.7%, 8.4% and
   3.7% rise. In the book they read as near-parallel and near-horizontal
   (~3-4%, and part of even that is the photograph's perspective). Purely
   cosmetic — `AD' = CD = EF` and `D'` on `AB` are exact — but if anyone
   wants the flatter book look, flatten all three to a common small slope
   and re-run `verify_figures.py`.
2. **Fig. 4-2 line lengths.** Our drawn lines are a little short relative to
   the segments: `AB/l` is 0.63 against the book's 0.55, `A'B'/l'` 0.72
   against 0.65. The book leaves more line running past the labelled points.
   Cosmetic; the congruence and incidence are exact.
3. **Fig. 4-4 is exactly equilateral, the book's is not.** `A`,`C`,`D`
   collinear plus equilateral `CDE` forces angle `ACB` = 60 degrees, and with
   `AB = BC` triangle `ABC` must be equilateral — so `B` sits above the
   midpoint of `AC`. The book's freehand `B` sits left of that (measured
   `AB` 476 px vs `BC` 534 px, a 12% mismatch it does not intend). Drawing
   the stated congruences exactly is the project rule, so this is correct.
   **Recorded so nobody "corrects" it back toward the photograph.**
4. **Fig. 4-1 is still a framed placeholder** — the builder's open question
   for Caleb (leave it / crop the scan as a raster / redraw a vignette)
   stands. It is line art rather than a halftone, so the plate rule is a
   judgement call, not a certainty.
5. The 35 remaining TIGHT placements were all eyeballed at 110 dpi and one at
   600 dpi. They sit 0.80-1.19 pt out by metric box, i.e. roughly 2 pt of
   real ink clearance, and the book crowds these same labels. Accepted.
