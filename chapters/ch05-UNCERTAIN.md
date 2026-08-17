# ch05 — Measurement of Segments (book pp. 73–83 / PDF pp. 87–97)

## Build note

This file did not exist before the text review. The unit had been left as a
`\Vpending` **scaffold**: section headings, `\addcontentsline` lines and figure
calls were in place, but *no prose, theorem, postulate or exercise text had
been transcribed at all* — each section held a boxed "text withheld pending
copyright verification" placeholder. The builder's status report
(`ok:true, uncertainCount:0`) did not reflect that.

The rights question is settled at project level
(`sources/copyright/renewal-search.md`), and the review re-verified its
load-bearing claims directly against the local USCO/NYPL renewal data before
transcribing:

- Thomas, *Calculus and Analytic Geometry* (Addison-Wesley, orig. reg.
  A436966, 1960-03-18) renewed RE396444 on 1988-09-30 — positive control holds.
- 21,418 renewals of 1960-registered works in `1988-from-db.tsv` — the window
  is dense, so a null is meaningful.
- Brumfiel / Eicholz / Shanks appear exactly **once** in 128,902 records
  (1986–1991): *Principles of Arithmetic*, orig. 1963, renewed 1991. Not this
  book. `shanks` ∩ `geometr` = 0 hits.

The chapter is now fully transcribed from the photo PDF and compiles clean
twice (17 pages, `build/ch05.pdf`).

## Text review

### Corrections applied

1. **Whole chapter transcribed** — 8 sections, 2 postulates (IV--1, IV--2),
   4 theorems, 11 exercise groups, Review of Chapter 5 and Algebra Review
   replaced the placeholder boxes. The `\Vpending` macro and the "Build
   status" notice were removed.

2. **Exercise-group boundaries were wrong in the scaffold.** It assigned
   Exercise Groups 5--3, 5--4 *and* 5--5 to section 5--3 (Inequalities). In
   the book, 5--3 and 5--4 belong to section **5--2 (Numbers)**; section 5--3
   opens at the foot of book p.75 and owns only Exercise Group 5--5. Fixed.

3. **`\starnote` deliberately omitted.** The scaffold implied a starred-item
   footnote here. Book p.75 carries this chapter's first starred exercises
   (Group 5--3, nos. 4 and 7) but prints **no footnote at all** — verified at
   450 dpi on PDF p.89. ch02 owns the book-wide first use. (ch10 anchors a
   copy with a "drop at integration" comment; ch05 does not, because the page
   demonstrably has none. Integration should confirm ch02 still carries it.)

4. **"irrational" footnote was rendering numbered.** Changed from `\footnote`
   to a local `\Vstarfoot` (unnumbered, bare `*`), matching the book and the
   `\IIstarnote` pattern used in ch02/ch07/ch09/ch10.

5. **Fig. 5--1 placeholder added.** It is a pictorial vignette (a man pacing
   off a building), not a geometric diagram; `figures05.tex` has no `FIGVONE`
   and states it is not redrawn. A local `\FIGVONE` plate placeholder now sits
   in ch05.tex so the figure is not silently missing. `figures05.tex` was not
   modified (figure geometry untouched, per review scope).

### Verified clean

- Every number in every exercise checked against the source pages: the seven
  fractions of Exercise 5--2; the decimal lists of Groups 5--4 and 5--11; the
  fraction lists in Group 5--3 no. 7; all ten Algebra Review problems
  (28 units, +9, ×2, diff 11, 12 more, ×4, +4, =32, 2/3, 3/5, =6, =20, 2·AB,
  +2, six inches, 36 ft, 1 ft, 3 inches, 9 in²).
- Exercise numbering runs 5--1, *Exercise* 5--2 (singular, as printed),
  5--3 … 5--11 — all present, item counts 3/1/7/4/5/2/2/2/4/5/5.
- Starred items: Group 5--3 nos. 4 and 7; Theorems 5--1, 5--2, 5--3 starred;
  **Theorem 5--4 is not starred** (confirmed).
- Postulate numbering IV--1 (Archimedes) and IV--2 (completeness); Archimedes
  dates 287--212 B.C.; the Eudoxus attribution sentence retained.
- Math: subscripts $A_0 \ldots A_n$, $A_{n-1}$, $C_i'$ primes, $\cong$,
  $\geqq/\leqq$, $\neq$, overbars via `\sg{}`, $\iffx$ in the review display.
  No Greek letters occur in this chapter.
- Section headings and all 8 `\addcontentsline` section entries + chapter
  entry present; Review and Algebra Review also carry TOC entries.

### Residual doubts

1. **Theorem 5--4 prints an inconsistent overbar.** The book sets
   "If $\sg{AB} = x$ … and if $\sg{CD} = y$ … then $AB = xy$ …" — the first
   two carry overbars, the third does not, though it plainly denotes a length.
   Confirmed at 450 dpi (PDF p.95); it is not a scan artifact. Transcribed
   **as printed**. Caleb: flag if you would rather silently correct it to
   $\sg{AB}$ — the surrounding Exercise Group 5--11 no. 1 does bar it.

2. **Exercise Group 5--6 no. 1** shows two short inline rules standing for the
   printed segments *AB* and *CD*. Their printed lengths are the whole point
   of the exercise (how many copies of *CD* reach past *B*). I set them at
   2.2 em and 1.3 em — a ratio of about 1.7. Measured off the photo the
   printed ratio is roughly 1.6–1.8, but the photo page is slightly skewed, so
   this is an approximation, not a measurement. A figure-review pass with the
   scans should pin it down.

3. **Fig. 5--1** remains a placeholder (see above) — needs either a redraw
   decision or acceptance as a plate.

4. Book p.73's opening sentence reads "that is for the distance between two
   points" with no comma after "is"; transcribed as printed.

## Figure review

Fresh adversarial pass, 2026-08-17. Nine drawn figures (5--2 … 5--10) in seven
macro blocks, plus Fig. 5--1 (kept as a placeholder, see below). Gates:
**80/80 constraints, 0 collisions, compiles twice clean.**

### Constraint coverage was incomplete — 24 checks added (56 → 80)

The old module verified unit-congruence and betweenness but never encoded
several hypotheses the text actually states. Added, and passing:

- **Order.** Archimedes' postulate IV--1 says the points are "arranged in this
  order"; nothing checked it. Figs. 5--2, 5--3, 5--4, 5--5, 5--7, 5--9 now
  assert strictly increasing abscissas, and 5--4 asserts `B = A4` outright.
- **Fig. 5--8 was missing its own given.** Theorem 5--2's hypothesis is
  |AB| = |A'B'|, so the plate draws AB the same length as A'B' — that was
  never checked. Now asserted, along with the two rows being left- and
  right-aligned.
- **Same-side conditions** ("on the same side of A as B") for 5--2, 5--8, 5--9.
- **Fig. 5--10 furniture:** the brace spans exactly CD, its "1" is centred on
  CD, the "1" under AB is centred on AB's first third, the last tick lands
  exactly on B, and the three groups do not overlap.

### Proportion errors fixed against the plates

Measured off the 150-dpi photo (PDF pp. 90–95) and the high-resolution iPad
scans (scan05 p21, scan06 p7):

1. **Fig. 5--3: B was in the wrong place.** It sat at 0.45 of AA₁; both
   sources put it at **0.32**. Fixed. The line's right-hand run was also
   short (1.42 u vs. the plate's 1.71 u).
2. **Fig. 5--10 was 19% too wide.** A/B/E/D sat at 2.24/5.24/5.92/6.42 CD-units
   from C; the plate has **1.55/4.55/5.15/5.65**. Fixed — the redrawn spread
   now occupies 65% of the text width, matching the plate exactly.
3. **Figs. 5--4 and 5--5 had a phantom stub left of A.** Both plates start the
   drawn line *at* A (unlike 5--2, which does extend left). Removed.
4. **Fig. 5--2's unit segment** sat at 0.55–1.55 u; the scan reads
   **0.50–1.50**. Set to 0.52/1.52, matching Fig. 5--4's own C/D.
5. **Figs. 5--8 and 5--9 rows were too close** (0.11 of the segment length; the
   plates have 0.16–0.17), which crushed the interior labels. Opened to 0.17.
6. **Scale.** 5--2/5--4/5--5 widened to 1.75 cm/unit, 5--6 to 7.5 cm, 5--7 to
   1.9 cm, so that label width relative to the unit gap (0.28) matches the
   plate's rather than exceeding it. This cleared the "A₃B" label graze in
   5--5 (the dots stay at exactly 3 and 3.18; only the text is nudged ±1.5 pt).

### Residual doubts

1. **Fig. 5--10: the book's own plate is not self-consistent.** Measured on
   scan06 p7, AB's thirds are ~432 px while CD is ~360 px — the plate draws
   AB's unit about 20% larger than the CD it is supposed to equal. The text is
   unambiguous (|AB| = 3 when CD is the unit), so the redraw enforces
   AB = 3·CD and AB = 6·ED exactly. A's position (1.55 vs. the measured 1.58)
   still matches the plate; only B moves. **This is a deliberate departure
   from the plate in favour of the stated geometry** — flagging in case Caleb
   wants the drafting error preserved.
2. **Fig. 5--2's two lines sit slightly further apart than the plate.** The
   scan reads 0.26 of the unit; the redraw uses 0.35. Our labels are
   proportionally larger than the book's, and at 0.26 the C/1/D row collides
   with the line *l*. Legibility accommodation, not a geometric claim.
3. **Fig. 5--8 is internally contradictory in the book, and I kept it that
   way.** The proof constructs B″ with AB″ ≅ A'B′ and then shows B″ = B; the
   plate simultaneously draws AB ≅ A'B′ *and* B″ strictly inside AB. That is
   the book's own drawing of the case being refuted, so the constraint module
   asserts the contradiction deliberately ("AB″ drawn shorter than A'B′").
   Do not "fix" this in a later pass.
4. **Ex. 5--6 no. 1 (the two inline rules) — could not be pinned down.**
   Item 2 of the text review asked this pass to measure them. Both sources
   defeat it: the photo page is skewed ~5° so the rule and its adjacent letter
   merge, and at scan resolution no row holds a contiguous run. Depending on
   where the stroke is judged to end, the printed ratio is somewhere in
   **1.25–1.55**; the current setting (2.2 em / 1.3 em = 1.69) is at or just
   above the top of that bracket. **No change made, because the exercise's
   answer is n = 2 for any ratio below 2.0**, so nothing pedagogical turns on
   it. Superseding item 2 of the text review.
5. **Fig. 5--1 remains a placeholder.** Re-confirmed as a pictorial vignette
   (a figure pacing off a building over hatched ground), not a geometric
   diagram — correctly handled under the plate rule. Still needs Caleb's
   redraw-or-accept decision.
6. **40 TIGHT label placements remain, 0 collisions.** All are the standard
   0.65–1.17 pt clearance between a point label and its own dot, which is the
   house style throughout the book; eyeballed at 110 dpi on every figure page
   and all read cleanly.
