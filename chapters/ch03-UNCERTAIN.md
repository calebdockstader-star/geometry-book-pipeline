# ch03 — Concerning Lines — uncertainty log

Unit: Chapter 3, book pp. 43–62 (PDF 57–76). Roman prefix `III`.
Full text + figure build. Text transcribed 2026-08-17 from
`sources/Geometry.pdf` PDF pp. 57–76, all 20 pages rasterized at 150 dpi and
read, with 320-dpi crops for every fraction, subscript and dense two-column
exercise block.

Gates at close: compiles twice with **0 errors**; **172/172 constraints hold**;
**0 collisions / 10 tight**; all 31 rendered pages inspected; all 14 exercise
numbering sequences audited against the source.

---

## 1. Prior BLOCKER — RESOLVED, text is now transcribed

Earlier passes delivered this chapter as figures-and-structure only, with the
prose withheld behind `\IIIpending{...}` boxes pending the copyright question.
**All 8 pending spans are gone and the macro definition is deleted.**

The unblock condition the previous reviewer set out has been met, and I checked
it against the primary data rather than accepting the project note:

- The work is **© 1960** (copyright page, PDF p. 6), so the renewal window is
  calendar **1988** — the exact window the earlier reviewer correctly said a
  "1988–91" sweep might miss on the early side.
- `sources/copyright/nypl-data/` holds the USCO post-1977 electronic renewal
  records for **1986–1991** (128,902 records, count verified).
- `grep -i` for `brumfiel` / `eicholz` across all six years returns **one**
  record — *Principles of Arithmetic* (orig. 1963-03-25, renewed 1991), a
  different book. `shanks` ∩ `geometr` returns **zero**.
- Positive control, re-run here: George B. Thomas, *Calculus and Analytic
  Geometry*, **same publisher, orig. reg. 1960-03-18**, appears as renewed —
  `A436966 … RE396444, 1988-09-30`. The dataset demonstrably captures
  Addison-Wesley renewals of 1960 works, so the null is a real null.
- Density control: 21,594 records in the 1988 file alone mention 1960.

1909 Act, 28-year first term; §305 runs it to 1988-12-31; §304(a) required
renewal in that final year; automatic renewal (1992 amendment) covers only
1964–77 works. No renewal → **US public domain since Jan 1, 1989.** Nothing in
this chapter is held back on rights grounds. Full write-up:
`sources/copyright/renewal-search.md`.

---

## 2. Text — judgment calls and residual doubts (for Caleb)

Nothing in the chapter was illegible; the photo pages carried every word. The
items below are typographic/structural choices, not reading failures.

### 2.1 Worth a second pair of eyes

1. **Algebra Review item 3, first fraction pair.** I read
   **9/5 − 3/5** (both denominators 5) off a 320-dpi crop. At 150 dpi the
   second denominator can read as an 8 (an earlier note in this file recorded
   "9/5 − 3/8"). The 320-dpi crop shows two 5s. Worth one confirming look at
   the physical copy, p. 61, since it is the one number in the chapter where
   the two readings are both plausible.
2. **Exercise Group 3-2 item 10** ends with two fill-in blanks and, as printed,
   **no terminal period**. I reproduced it that way; if the house rule is to
   normalise punctuation, this is the one place it shows.

### 2.2 Deliberate typographic deviations

3. **Theorem 3-3 head.** The book prints "**Theorem 3-3** The two-side theorem."
   — no period after the number. `brumfiel.sty`'s `bkplain` style always emits
   one, so mine reads "**Theorem 3-3.** The two-side theorem." The name is set
   roman inside the italic body to match the book.
4. **Theorem 3-3 clauses (1) and (2)** are printed on their own lines in the
   book; mine run on inside the italic statement.
5. **Starred theorems.** 3-4, 3-5 and 3-6 carry a printed asterisk. Implemented
   as a local `\newtheorem{IIIsthm}[theorem]{*Theorem}` sharing the `theorem`
   counter, so numbering stays exact and the head reads "*Theorem 3-4."
   Theorems 3-1/3-2/3-3 are unstarred (confirmed).
6. **Three unnumbered `*` footnotes**, all via the local `\IIIstarfn`:
   p. 43 (Latin "demand" / Greek "worthy"), p. 50 (the *collinear* note hanging
   off Definition 3-3), p. 52 (starred **proofs** are difficult and may be
   omitted). Ch 3 does **not** reprint ch 2's "starred exercises … are
   optional" note — that convention is introduced in ch 2 and must survive
   there for ch 3's starred exercises to make sense. Flag for the integration
   agent.
7. **Exercise Group 3-2 item 7** — the book prints a Statements/Reasons frame
   with line 1 filled and lines 2–4 blank for the student. Rendered with the
   `steps` environment and rules.
8. **Review of Chapter 3, item 2** — the 15-term vocabulary list is printed 7
   in the left column and 8 in the right; `multicol` balances it 8/7. Cosmetic.
9. **Running heads.** `\markboth{CONCERNING LINES}{}` per house style; the book
   alternates verso "CONCERNING LINES" against recto section titles ("THE
   POSTULATES", "POSTULATES OF BETWEENNESS", "RAYS AND ANGLES", "INTERIOR AND
   EXTERIOR", "REVIEW OF CHAPTER 3"). Chapter-wide convention — for the
   integration agent, not this unit.
10. **Fig. 3-18 placement.** Exercise Group 3-2 breaks across the p. 51/52
    spread and the book sets Fig. 3-18 at the top of p. 52, physically above
    the 3-5 heading but belonging to item \*15. I place it after the group, at
    the end of §3-4.

### 2.3 Verified correct (checked, no change needed)

- Section headings/numbering 3-1 … 3-6 and their page starts match the printed
  TOC and page headers; `\addcontentsline` present after `\chapter*` and all
  seven `\section*`.
- Postulate Group I (I-1/I-2/I-3) and Group II (II-1 … II-5) names, order and
  wording.
- Theorems 3-1 … 3-6, Definitions 3-1 … 3-11: contiguous and correctly placed.
- **Exercise numbering, all 14 sequences audited in the source and in the
  render:** 3-1 → 1–12; 3-2 → 1–6, 7 (full width), 8–18; Exercise 3-3
  (singleton, not a group); 3-4 → 1–11; 3-5 → 1–2; 3-6 → 1–14; Review of
  Chapter 3 → 1–3; Review Questions → 1–10; Review Test → 1–3 (item 2 has
  (a)–(h), item 3 (a)–(c)); Algebra Review → 1–14.
- **Starred inventory (complete):** Exercise Group 3-2 items \*5, \*12–\*18
  (eight — the group runs onto p. 52); Exercise Group 3-6 items \*12, \*13,
  \*14; Theorems \*3-4, \*3-5, \*3-6; the starred *proof* of Theorem 3-3;
  Algebra Review item \*6.
- Greek letters: this chapter uses **none**. The math load is subscripts
  ($l_1$, $l_2$, $m_1$, $m_2$, $r_1$, $r_2$, $P_1$, $P_2$, $A_1$–$A_5$,
  $Q_1$–$Q_5$, $s_1$, $s_2$, $t_1$, $t_2$), primes ($r_1'$, $r_2'$), $\angle$
  and $\triangle$. Every occurrence of the error-prone $r_1'$/$r_2'$ was
  checked individually.
- A caught-and-fixed render bug worth recording: `enumitem` does **not** advance
  the counter across an explicit `\item[...]` label, so Algebra Review item 8
  initially printed as "6". All five lists that mix explicit starred labels with
  automatic ones were then audited; only that one was wrong.

---

## 3. Figures — status

All 39 figures (3-1 … 3-39) drawn. `python3 tools/verify_figures.py 03`
reports **172/172 constraints hold**;
`python3 tools/check_labels.py chapters/figures03.tex 03` reports
**0 collisions, 10 tight**. Every figure page rasterized at 110 dpi and read.

### 3.1 Changed in this pass

Two genuine label grazes (`d = 0.00pt`, i.e. glyph box touching the stroke)
appeared once the real text reflowed the figures onto new pages:

- **Fig. 3-6** — `B` sat on the upper curve at the right crossing. `B` moved to
  a polar offset above the crossing; that in turn collided with the `l` label,
  so `l` moved back along its own stroke to (3.92, 1.50). **Deviation to note:**
  the book sets `l` close to the right crossing, just above `B`; mine names the
  same curve but earlier along it. Structurally correct, positionally a
  compromise forced by the collision gate.
- **Fig. 3-9** — `B` sat on the left lobe at the middle crossing; now pinned
  0.58 units directly above it, in the open waist. Reads clean at 300 dpi.

No other figure code was touched.

### 3.2 Inherited residual doubts (unchanged, still open)

- **Figs 3-6, 3-8, 3-9** are Bézier lens / figure-eight shapes at printed
  proportion, not traced from the scans. Structure is right (crossings at both
  ends, D and E provably on the right-hand lobe); exact curvature is ours.
  `scan04.pdf` p7 and p8 cover them if anyone wants a proper trace.
- **Fig. 3-29 hatch pitch** — rules at 0.10 units both ways; the scan shows the
  vertical rules noticeably denser. Regions and the doubly-shaded overlap (the
  interior of ∠COD, which is the whole point of the figure) are correct.
- **Fig. 3-24** — relative placement of the four sub-drawings reconstructed
  from the photo.
- **Fig. 3-27(i)** — fan opened from 18°/24° to 23°/25°; at this type size the
  numerals cannot clear both rays at the printed angles.
- **Figs 3-38, 3-39** — l₂ sits 0.30 units lower than the first build to give
  R's label room.
- **Figs 3-1, 3-2** — A′ and B′ slid down L3 (t 0.700→0.835, 0.585→0.720) past
  its crossing with L6 for label air. |A′B′| = |AB| still holds exactly; the
  printed positions are a little further up the line.
- **Ten tight (<1.2 pt) placements** remain, all eyeballed and accepted: the
  "AB" pair and B′ (×2) in 3-1/3-2, B and C in 3-9, O and the numeral in
  3-24/3-25, the numerals in 3-27, Q₂ in 3-39.
- `check_labels.py`'s label-vs-label test can still mask an overprint when the
  merge rule absorbs a short neighbouring label into its host. Worth a proper
  fix in the tool for the whole book.

### 3.3 Plate

- **Fig. 3-15** — the three-men illustration (book p. 49) is original artwork,
  not a geometric diagram. Rendered as a framed placeholder with a description,
  per the plate rule. Not redrawn.

### 3.4 Scan-checked

- **Figs 3-1 / 3-2** (the organic pair the brief predicted for the ch 2–3
  region) — digitized from `scans/scan04.pdf` p4 at 170 dpi. It is here, in
  §3-2, and it is *wobbled straight lines*, not a blob or contour.
- **Figs 3-29, 3-33, 3-39** confirmed against `scan04.pdf` pp. 20, 21, 24.

---

## Text review

Fresh adversarial text review, 2026-08-17. Diffed `chapters/ch03.tex` line by
line against source pages PDF 57–76 (book pp. 43–62), all twenty pages read at
150 dpi, with 600-dpi crops from the photo PDF and 200–400 dpi renders from the
iPad scans (`scan04.pdf` pp. 13, 15, 16; `scan05.pdf` pp. 3, 5) for every zone
where a numeral or a fraction carries meaning. Compiles twice, 0 errors.

### Fix applied (1)

1. **Exercise Group 3-2, item 10** — the item ends with a terminal period after
   the second fill-in blank. The build omitted it, and §2.1 item 2 of this file
   asserted the book prints none. `scan04.pdf` p. 13 (book p. 51) is sharp
   enough to settle it: the period is there. Added; §2.1 item 2 is superseded.

### Doubt closed, no change needed

2. **Algebra Review item 3, first fraction pair** (§2.1 item 1) — **resolved as
   9/5 − 3/5**, both denominators 5. The photo PDF is genuinely ambiguous here
   even at 600 dpi, but `scan05.pdf` p. 3 (book p. 61) resolves both glyphs
   cleanly at 400 dpi. The build is correct; the "3/8" reading is dead. No
   remaining need to check the physical copy for this.

### Verified against source, no defect found

- **Every paragraph opening in the chapter** is present, in order, with no
  dropped, merged or paraphrased sentence. Prose is the book's wording
  throughout, including all italic emphasis spans.
- **Definitions 3-1 … 3-11, Theorems 3-1 … 3-6, Postulates I-1 … I-3 and
  II-1 … II-5** read verbatim, in place, correctly numbered and contiguous.
  Postulate II-3's eight betweenness strings and their four reversals are
  character-correct.
- **All 14 exercise sequences and every number inside them** re-audited against
  the source: groups 3-1 (1–12), 3-2 (1–18), Exercise 3-3, 3-4 (1–11),
  3-5 (1–2), 3-6 (1–14), Review of Chapter 3 (1–3), Review Questions (1–10),
  Review Test (1–3 with (a)–(h) and (a)–(c)), Algebra Review (1–14). Every
  betweenness triple in the exercises checked individually against the sharp
  scans — the collision-prone ones (3-2 #4 CAD/ADB, #5 CAD/CAB, #8 CAD/BDE/BCA,
  #12 ABC/BCD, #13 ACB/CDB/DEB) are all correct. Algebra Review #5, #7, #10
  and #13 numerals and fraction lists all correct.
- **Starred inventory** matches the printed asterisks exactly: 3-2 items *5 and
  *12–*18; 3-6 items *12–*14; Theorems *3-4, *3-5, *3-6; the starred *Proof* of
  Theorem 3-3; Algebra Review *6. Theorems 3-1/3-2/3-3 correctly unstarred.
- **Three `*` footnotes** (pp. 43, 50, 52) present and verbatim. Ch 3 correctly
  prints no "starred exercises are optional" note — the book does not have one
  here; the convention is carried in from ch 2, so `\IIstarnote` must survive in
  ch02 for ch 3 to make sense. Still an integration-agent item.
- **Greek letters: none in this chapter** — confirmed independently. Math load
  is subscripts, primes (r₁′, r₂′), ∠ and △; all checked.
- **Headings and page order**: section titles/numbers 3-1 … 3-6 and the
  Review/Important Remark/Review Questions/Review Test/Algebra Review sequence
  match the printed running heads page for page. No spread-photo ordering error.
  `\addcontentsline` present after `\chapter*` and after all seven `\section*`.
- **Book-order oddity preserved correctly**: Exercise Group 3-5 really is
  printed *before* Definition 3-10 on p. 56, and the build keeps that order.

### Residual doubts (typographic only)

3. §2.2 items 3 and 4 confirmed accurate against `scan04.pdf` p. 15: the book
   sets "**Theorem 3-3**" with **no period** (3-1 and 3-2 do take one), and
   breaks clauses (1) and (2) onto their own lines. Both deviations stand as
   the builder described; neither is a transcription error. A house-style call
   for the integration agent, not a text defect.
4. Nothing else outstanding. No question for Caleb arising from the text.

## Figure review

Fresh adversarial pass over all 26 figure blocks (Figs 3-1 … 3-39), 2026-08-17.
Tools: `verify_figures.py 03` → **190/190**; `check_labels.py … 03` → **0
collisions**, 10 tight; chapter compiled twice clean; all 31 rendered pages read
at 110 dpi and the changed figures at 300 dpi; every figure cross-read against
the photo PDF (pp. 57–76) and the key ones against `scans/scan04.pdf`.

### Fixed in this pass

1. **Fig 3-25(a) — arrowheads were on the wrong element.** The build put
   arrowheads on the two *sides*; the book puts them on the two *ends of the
   arc*, pointing at the sides (unambiguous on `scan04.pdf` p18, book p.54, and
   consistent with the text: "the arrowheads indicating the sides are not
   vital"). Sides are now plain, the arc is `<->`.
2. **Fig 3-27(ii) — wrong configuration.** The build drew three rays fanning
   *upward* (two ~32° angles). The book draws an inverted Y: the common side
   runs straight up, the two noncommon sides run down-left and down-right
   (~138° each). Rebuilt from the scan's proportions; constraint entry updated.
3. **Fig 3-29 — lines truncated at A and B.** The book runs l and m *past* A
   and B (they are points on the lines, not endpoints). Added short tails and
   moved the A/B labels clear of them.
4. **`ch03.py`: stale coordinates.** The two Q₁ side-checks for Fig 3-38 tested
   a point (1.55, 2.05) that appears nowhere in the tex; the drawn Q₁ is
   (1.35, 2.45). Now checks the real point (still passes).
5. **`ch03.py`: vacuous constraint.** Fig 3-36's "A on the other side of angle
   O" was `_collinear(O, A, A)` — identically zero, so it asserted nothing.
   Replaced with two real ones: B lies strictly inside both drawn sides, which
   is what makes the crossing read as a crossing.
6. **Constraints added (18 new)** where the book states a hypothesis that was
   not encoded: 3-2 (A, B on the wobbly L1 and A′, B′ on L3 — the "same lines"
   claim), 3-9 (D and E on opposite lobes), 3-19 (each brace and caption on its
   own side of O), 3-24 (drawings (i) and (ii) are genuine, non-straight
   angles), 3-25 ((b) is the same angle as (a); (c) is obtuse), 3-28 (common
   side off the base line), 3-29 (both hatch families terminate exactly on
   their bounding line — guards the two slope constants), 3-33 (order along the
   segment is Q₃, R, S, P, per "Q₃RP and RSP, hence Q₃SP").

### Residual doubts

- **Fig 3-15 is carried as a plate.** It is *line art* (three men on a ground
  line, dashed sight line), not a halftone photograph, so it is not obviously
  covered by the "plates are not redrawn" rule. Redrawing human figures is out
  of scope for the geometry tooling, so the placeholder stands. **Question for
  Caleb: leave as a plate note, or commission a redraw?**
- **Fig 3-26, label O.** The book seats O just below-left of the crossing,
  inside the ring of arcs. At this type size the label's padding cannot clear
  the two lines there (it collides), so O stays outside the ring, below-right.
  Cosmetic deviation, deliberate.
- **Fig 3-29 framing.** In the book the shading is bounded by the drawing's own
  rectangle, with A and B sitting *inside* the left edge; the redraw makes A and
  B the corners themselves. Region membership, the double-hatched wedge OCD and
  the interior of ∠COD are all identical — only the outer framing differs.
- **10 tight placements, all accepted.** Figs 3-1/3-2 ("A B" and B′ hug their
  lines exactly as the book prints them), 3-9 (B, C at the lobe crossings),
  3-24/3-25 (O, numeral 1), 3-27 (numerals 1, 2 in the narrow fan (i)), 3-39
  (Q₂ on l₂). Each eyeballed at 300 dpi; all read cleanly.
- **Fig 3-2 wobble is traced, not derived.** The eight-point spline paths carry
  the printed hand-wobble as digitized; they are faithful in amplitude but are
  not a pixel-exact recovery of the plate.

---

## Figure-repair pass, 2026-08-17 (feedback/FIX-SPEC.md)

Caleb photographed no Chapter 3 figures, so this pass is the structural fix
(§2) plus a full sweep of the chapter against `sources/Geometry.pdf`
(book pp. 44–59 = PDF pp. 58–73).

### Exercise-group figures are now inline (§2)

All **7** exercise figures now sit immediately after the exercise that cites
them, wrapped in `\exfig{…}`. Checked against the source pages: the book does
place each of these directly beneath its own exercise.

* `multicols` dropped from **Exercise Groups 3-1, 3-2 and 3-6** (the three that
  carry figures). Groups 3-4 and 3-5 carry none and keep their two columns.
* Placement: Fig 3-8 after Ex. 3-1 #3, Fig 3-9 after #8, Fig 3-10 after #12;
  Fig 3-18 after Ex. 3-2 *15; Fig 3-36 after Ex. 3-6 #1, Fig 3-37 after #7,
  Fig 3-38 after *12, Fig 3-39 after *13.
* **1 combined macro split into 2:** `\FIGIIITHIRTYEIGHTTHIRTYNINE` →
  `\FIGIIITHIRTYEIGHT` + `\FIGIIITHIRTYNINE`, each a full-width `bkfigure`
  with its own `\figcap`; `scale=` raised 0.675 → 1.15 for the freed width.
  (Ex. *12 cites 3-38 and *13 cites 3-39, so they had to come apart.)
* Group 3-2's `steps` table splits its list into three blocks; all three lost
  `multicols` so the group reads as one column throughout. Exercise numbering
  verified unchanged (1–6, 7, 8–18).
* `\FIGIIITWENTYTWOTWENTYTHREE` was **left combined**. Fig 3-23 is cited by
  *Exercise 3-3*, which is a single unnumbered paragraph rather than a list, and
  the book itself prints 3-22 and 3-23 side by side immediately above it — so
  the existing placement already matches the source. Fig 3-33 is cited by
  Ex. 3-6 *14 but is a body figure printed earlier in the book (rule 5),
  so it stayed put.

### Figures corrected against the source

* **Fig 3-19 — wrong shape.** The two spans over the line were drawn as
  squared-off brackets; the book sets proper **curly braces**, each end curling
  down toward *l* and each middle carrying a point up toward its caption. Added
  a chapter-scoped `\IIIbrace` helper (pure Bézier, no new tikz library, so it
  cannot clash with another chapter's figure file) and raised the two captions
  to clear the new tips.
* **Fig 3-32 — missing arrowheads.** The two arcs marking ∠(r₁,r) and ∠(r,r₂)
  were plain; in the book each is struck outward from *r* and lands on its ray
  with an arrowhead — the same "indicating the sides" notation the book itself
  introduces in Fig 3-25(a). Both arcs now run outward and carry `->`.
* **Fig 3-7 — label on a line.** *B* was set `below right`, which put it
  straight on the two tails that run past the crossing. Moved into the free
  wedge below.
* **Fig 3-24 — label on a ray.** The *O* of drawing (ii) was grazing the
  down-left ray. Pushed further left.
* **Label clearance, 30 collisions cleared.** All but two were the same defect
  — a letter set directly on its own `\dt` point, which the global `outer sep`
  tightening turned into a touch. Cleared with a 1.5 pt shift away from the dot
  in Figs 3-1, 3-2, 3-3, 3-9, 3-10, 3-11, 3-12, 3-13, 3-14, 3-16, 3-22, 3-24,
  3-31, 3-33 and 3-39, plus the two placement fixes above.

### Verified correct, left alone

Figs 3-5, 3-6, 3-8, 3-9, 3-10, 3-17, 3-18, 3-20, 3-21, 3-22, 3-23, 3-25, 3-26,
3-27, 3-28, 3-29, 3-30, 3-31, 3-33, 3-34, 3-35, 3-36, 3-37, 3-38, 3-39 were
each compared against the source page and are structurally faithful. In
particular the angle arcs of 3-25(a)(b)(c), 3-26 (four arcs, numerals 1–4),
3-27 (three drawings, two arcs each), 3-28 and 3-37 are all present and land on
their own rays; the dashed opposite rays of 3-30/3-37/3-38/3-39 and the solid
ones of 3-31 match the book; the double-hatched wedge of 3-29 is correct.
**Fig 3-15 (the three men on a sight line) was not touched** — pictorial line
art handled centrally; its placeholder is intact and still in the body text.

The brief mentions one organic/freehand figure early in ch02 or ch03: in this
chapter it is the **Fig 3-1 / 3-2 pair**, whose six lines and hand-wobble were
already digitized from `scans/scan04.pdf` p4 in the first build (noted above in
this file). I re-checked it against the photo page and left the geometry alone.

### Gates

* `tectonic` — compiles twice clean, 32 pp.
* `python3 tools/verify_figures.py 3` — **195/195 constraints hold** (a new
  group added for the Fig 3-19 braces: tip at the span's own midpoint, each
  brace clear of *O*, the two not overlapping).
* `python3 tools/check_labels.py chapters/figures03.tex 3` — **0 collisions**,
  40 tight placements.
* Every changed page rasterised at 70–600 dpi and inspected.

### Open / unsettled

* **40 tight placements**, up from 19. The 1.5 pt shifts used to clear the
  dot-collisions land most of those letters in the 0.9–1.2 pt band, which the
  tool calls tight but legal. Eyeballed at 100 dpi and again at 600 dpi on
  Figs 3-13, 3-14, 3-19, 3-32, 3-33, 3-38, 3-39; all read cleanly, and they are
  tight in the direction Caleb asked for (letters close to what they label).
  Flagging the count because it is a large jump.
* **Fig 3-26 label *O*.** Still parked outside the ring of arcs, where the book
  sets it just inside, below the crossing. The global clearance change was not
  enough to fit it there at this type size. Unchanged from the earlier note in
  this file; would need the figure grown rather than the label moved.
* **Two small overfull hboxes (2.2 pt, 3.2–3.9 pt) on the figure lines for
  3-1/3-2 and 3-3/3-4/3-5** — pre-existing, in body figures I did not touch;
  worth catching in the book-wide re-fit.
* Figs 3-8, 3-9, 3-10, 3-18, 3-36 and 3-37 were already standalone macros, so
  per §5 I left their `scale=` alone; they now read smaller than the split
  3-38/3-39 beside them. Left for the book-wide re-fit.
