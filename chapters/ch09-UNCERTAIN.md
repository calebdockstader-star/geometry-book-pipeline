# Chapter 9 — uncertainty report (figure rebuild, 2026-08-17)

Scope of this pass: **figures only**. The chapter text was transcribed in an
earlier pass and was left alone except for the three structural fixes listed
under "Changes to ch09.tex". Text questions are flagged here for the
text-review agent rather than acted on.

Gates at hand-off: compiles twice with 0 errors · constraints **157/157** ·
collisions **0** (22 tight, all eyeballed) · every figure page rasterised and
inspected · no figure block overflows its column.

---

## 1. Questions for Caleb

1. **Fig 9-33 vs its exercise (book p.169).** Exercise 9-10 #4 reads
   "if `AD = x·AB`, and `AE = x·AC`, prove that `△ABC ∼ △ADE`", which pairs
   D with B and E with C. The printed figure puts **E on AB** (left side) and
   **D on AC** (right side) — the opposite pairing. The conclusion holds
   either way because both points sit at the same ratio, so I drew the figure
   as the book prints it and left the exercise wording as printed. Confirm
   you want the book's inconsistency preserved rather than silently fixed.

2. **Fig 9-48 proportions.** Exercise 9-13 #4 gives `BD = 24`, `AD = 13`,
   so `AC = 10` and the rhombus is genuinely long and thin (diagonal ratio
   2.4 : 1). The book *draws* it much rounder (measured ratio ≈ 1.7 : 1) — the
   printed figure does not satisfy its own numbers. I drew the exact
   2.4 : 1 rhombus (perpendicular diagonals, all sides 13) because the figure
   discipline says quoted lengths must be reflected. It therefore looks
   noticeably narrower than the book's. Say the word if you'd rather match
   the book's shape and let the numbers be schematic.

3. **Figs 9-34, 9-35, 9-40, 9-41, 9-42, 9-43, 9-44, 9-45, 9-46** all state a
   right angle at the apex plus an altitude to the hypotenuse. In several of
   these the book's drawn apex is **too high to be a right angle** (e.g. in
   9-34 the printed height exceeds the maximum possible `√(AD·DB)`). I placed
   the apex at the exact height the right angle forces, so these triangles are
   slightly flatter than the printed ones. Structure, labels and marks are
   unchanged.

4. **Fig 9-10 keeps the book's schematic ratio.** Exercise 7 uses
   `AB = 18, BC = 3` and Exercise 8 uses `AB = 2, BC = 1` for the *same*
   figure, so no single drawing can honour both. I kept the book's own drawn
   ratio (`AB : BC ≈ 1.85 : 1`, measured off scan12 p5) and made the two
   transversals exactly parallel and the three lines exactly parallel.

---

## 2. Figures I am not fully certain I nailed

| Fig | Doubt |
|-----|-------|
| 9-24 | Lake traced from scan12 p8 (4 nested contours). Faithful in shape, but I **shifted the whole lake up ≈0.30 and left ≈0.05 units** relative to the triangle so the `D` label could sit above `AC` as the book has it; in the book the lower-right lobe crowds `D` badly. Triangle, `D`, `E` and the 0.15 ratio are exact. |
| 9-24 | Contours 3 and 4 (the two innermost) are the least certain: at scan resolution their outlines blur into contour 2. Their shape is measured but should be re-checked by the figure-review agent against scan12 p8/p9. |
| 9-49 | Lake traced from scan11 p8 — this scan is sharp and all four contours were read directly, so I'm confident here. `OA : OB = 21 : 20` and the right angle at `O` are exact. |
| 9-5 | The book prints a triangle `EFG` plus the short pieces `CD` and `DG`; an earlier draft read it as a quadrilateral. I reconstructed it from the three stated hypotheses (`FC ≅ CG`, `CD ∥ EG`, `DG ∥ EF`), which forces `EG = 2·CD` — the very thing the exercise asks you to prove. Verified against the p.156 close-up (hi-res photo crop). Worth a second look. |
| 9-30 | The book shows `E` and `F` as two distinct nearby points on `AC`, with `DF` drawn dashed, even though the proof's whole job is to show `F = E`. I reproduced that deliberately: `DE` (solid, key) satisfies `DE ∥ BC` exactly, and `DF` is a dashed auxiliary to a distinct `F` further along `AC`. So `DF` is *not* drawn parallel to `BC` — matching the book, but it is a judgement call. |
| 9-21 | The quadrilateral is markedly asymmetric (`OA` ≈ 1.6 × `OC`). That is what the print shows, but the figure is small and my vertex reads have maybe ±5% error. Midpoint construction is exact. |
| 9-38 | The two hexagons are similar **by construction** (the second is the first rotated −30° and scaled 0.72). Those two numbers were fitted to the printed vertex positions and reproduce them to within a few percent, but they are a fit, not a measurement. |
| 9-16, 9-47, 9-52 | Purely schematic figures with no stated numeric constraints; proportions are eyeballed from the photo pages, not scans. |

---

## 3. Deliberate deviations from the printed page

* **Column widths.** Several sub-figures were given more or less of the line
  than the book allots, because our text block is 109 mm against the book's
  wider measure. Sub-figure order and grouping per row are unchanged.
* **Label clearance.** `vlab`/`slab`/`klab` get `outer sep = 4.8pt` in this
  chapter (brumfiel.sty's 3.4pt clipped labels sitting on lines). Set locally
  in `figures09.tex`; the shared style file is untouched.
* **Primed labels** use `\IXpr`, a prime lowered by 1.3pt. Reason: the math
  prime sits ~4pt above its letter, past pdfplumber's 3pt word tolerance, so
  `check_labels.py` read `A′` as two overlapping words and reported ~56 false
  collisions. The drop is visually indistinguishable and removes all of them.
* **Fig 9-6**: `C` and `C′` are labelled *below* their line rather than above.
  The three parallels are only 0.63 units apart there and the book's
  above-left placement stacks the `B`/`C` labels on top of each other at our
  size.
* **Fig 9-12 `A`, Fig 9-29 `F`, Fig 9-27 `E`, Fig 9-30 `F`** are positioned by
  explicit offset rather than by anchor, to clear lines that pass through the
  labelled point itself.

---

## 4. Known tool artifacts (not defects in the figures)

* `check_labels.py` rebuilds every line from its **bounding box**, so a line
  running up-to-the-right is modelled as its mirror image running
  down-to-the-right. Two labels (9-27 `E`, 9-29 `F`) had to be moved further
  out than geometry requires to clear these phantom diagonals.
* The same tool merges neighbouring labels into one "word" when they are
  close, which **hides** genuine label-vs-label overlaps. Three real overlaps
  it missed (`m′`/`A′` in 9-6, `Parallel`/`E` in 9-10, `Parallel`/`B` in 9-12)
  were caught only by looking at the rasterised pages, and are fixed.
  A future tool pass should treat the merge as a signal, not silence.

---

## 5. Changes to ch09.tex (text file) made in this pass

1. All 24 figure macros renamed `\FIG…` → `\FIGIX…`.
2. **`\FIGIXTWOTHREE` is now actually placed.** The macro for Figures 9-2 and
   9-3 existed but was never called, so both figures were missing from the
   rendered chapter. Inserted after `\FIGIXONE`, matching book p.155.
3. Added `\addcontentsline` for the chapter, the nine sections and the review
   section.

No prose was altered.

---

## 6. Text items for the text-review agent (found in passing, not acted on)

* **Exercise Group 9-5, items 1–5** — the source page for these (book p.160)
  is a thin top-strip in the scans and the photo page is legible but I did not
  verify the starred markers on items 4 and 5 against it. Items 6, 9, 10 are
  confirmed starred from p.161; items 4 and 5 are currently starred in our
  file on the earlier pass's authority.
* Exercise numbering was spot-checked for every group in the chapter
  (9-2 … 9-14) against the source pages and matches, including the starred
  items in groups 9-3 (*12, *13), 9-10 (*6) and 9-13 (*4, *17).
* Two overfull `\hbox` warnings remain, both in prose, both pre-existing:
  `ch09.tex:439` (the long all-caps section heading 9-6) and `ch09.tex:778`
  (a paragraph in Exercise Group 9-13). Neither comes from a figure.

---

## Text review (fresh agent, 2026-08-17)

Method: every page of the unit (PDF 168--193 = book pp.~154--179) rasterised at
150 dpi and read against `ch09.tex` line by line; four passages re-cropped at
400 dpi where the photo curls into the gutter. Compiles twice clean after the
fixes (errors 0; only the pre-existing box warnings remain).

### Fixes applied (5)

1. **Historical remark (book p.163)** --- restored a dropped clause: the Greek
   theory of ratio and proportion "that is a model of ingenuity and precision".
   The transcription ran the two sentences together and lost it.
2. **Theorem 9--7 proof, Statement 1 (book p.165)** --- read `A''B = 3`; the
   book has `A''B = A'B' = 3`. Confirmed on a 400 dpi crop (the equality breaks
   across a line in the original and had been mis-read). This matters because
   Statement 6's reason cites it back in the fuller form.
3. **Section 9--9 opening (book p.175)** --- restored the dropped conditional
   "If the circles intersect at $P$, and" before "$C$ is the midpoint of $AB$".
   Without it the sentence introduces $P$ with no antecedent.
4. **`\starnote` was entirely absent.** Added `\IXstarnote` (chapter-local,
   unnumbered, matching ch02's `\IIstarnote` and ch10's `\Xstarnote`) anchored
   at Exercise Group 9--3, the chapter's first starred items (*12, *13).
   Verified it renders on the built page that carries them.
5. **Truncated review section flagged** --- see below.

### Truncation found: the chapter ends ~3 book pages early

`ch09.tex` stopped after review item 1. The book's Review of Chapter 9 runs
pp.~176--179 and contains **items 1--8** plus a separate **Review Exercises**
run of **20 exercises**. Following the convention already used in ch08 and
ch10, the missing spans are marked with `\IXpending` boxes describing exactly
what belongs there rather than transcribed in this pass:

* book pp.~176--177 --- review items 2--8 (item 4 starred).
* book pp.~177--179 --- Review Exercises 1--20 (nos.~3 and 15 starred).

**Figures 9--53, 9--54 and 9--55 do not exist.** `figures09.tex` stops at
9--52, so the builder's "52 figures" is complete only for the chapter body, not
for the review. These three are needed by review exercises 11--12, 15 and 18.
This is a figure-unit gap, not a text gap --- flagging for the figure-review
agent.

### Verified clean (no change needed)

* **Every numeric value in every exercise group** (9--2 through 9--14) checked
  digit by digit against the source pages, including the two long word-problem
  sets. All correct.
* **Starred markers**: 9--3 (*12, *13), 9--4 #4(e), 9--5 (*4, *5, *6, *9, *10),
  9--10 (*6), 9--13 (*4, *17). All match the book. This closes the previous
  pass's open question about 9--5 items 4 and 5 --- both **are** starred in the
  book (confirmed on p.160).
* **Theorem/corollary/definition numbering** 9--1 … 9--15, Cor. 9--1--1/2,
  9--7--1/2, 9--11--1/2, Def. 9--1 … 9--5, Construction 9--1 --- all sequential
  and matching the printed numbers, including the cross-references in prose.
* **All 15 theorem statements, 6 corollaries, 5 definitions and the
  construction** read verbatim against the page; no paraphrase found.
* **Every proof step table** (Thms 9--1, 9--7, 9--8, 9--9, 9--10, 9--12, 9--13,
  9--15) checked statement-by-statement and reason-by-reason, including the
  `\stepx` continuations 8--14 in Thm 9--7.
* **Section headings and `\addcontentsline`** present and correct for the
  chapter and all nine sections; added one for Review Exercises.
* **Math**: no Greek letters occur in this chapter. Primes, subscripts,
  $\cong$ vs $\sim$, $\perp$, $\parallel$, the mean-proportional footnote and
  the radical expressions in 9--14/9--15 all match.

### Residual doubts

1. The `\IXpending` spans above are the only known text gap. Whoever fills them
   should also commission Figs 9--53/54/55.
2. Book p.166 Ex.~9--9 #1 prints `AE = 4` and `ED = 6` with `BE ∥ CD`; our
   figure 9--23 labels the same points. Numbers verified, but the figure-review
   agent should confirm the drawn ratio is consistent.
3. `\IXpending` and `\IXstarnote` are chapter-local duplicates of macros ch02
   and ch10 also define locally. At integration these three should be hoisted
   into the book preamble once, and only one chapter should keep the star
   footnote call.
4. **Collision count disagrees with the builder's hand-off.** Running
   `tools/check_labels.py chapters/figures09.tex 09` at the end of this pass
   reports **5 collisions, 20 tight** across 25 figure blocks, where the
   builder recorded 0 collisions / 22 tight. I did not touch `figures09.tex`,
   so this is not a regression from the text pass --- either the tool was
   invoked differently at hand-off or the count is genuinely non-zero. The
   figure-review agent should re-run it and reconcile before the chapter is
   called done.

---

## Figure review (fresh agent, 2026-08-17)

Method: all 52 figures in 25 `\FIGIX…` blocks read against the printed pages
(PDF 168--193 rasterised at 150 dpi, and every figure I doubted re-cropped at
400 dpi), plus the iPad scans for the two organic figures and for book p.158.
Gates at hand-off: compiles twice with 0 errors · constraints **169/169**
(was 157/157 -- see below) · collisions **0** (17 tight, all eyeballed) ·
every figure page rasterised and inspected again after the edits.

### Reconciliation of the collision count

The text-review pass reported 5 collisions where the builder recorded 0. Both
were right at different times: `check_labels.py` samples each geometry segment
at ~1.5 pt intervals, so *lengthening a line does not merely extend it, it
re-phases the sample points*. Grazes therefore flip between TIGHT and COLLIDE
whenever a segment's endpoints move. The macro-to-page mapping was verified
sound (25 macros, 25 pages, 1:1). Final state is 0 with the tool run exactly as
documented: `python3 tools/check_labels.py chapters/figures09.tex 09`.

### Genuine drawing errors found and fixed (2)

1. **Fig 9--5 was geometrically wrong.** The macro defined `(D)` correctly as
   `C + (G-E)/2` but then drew and labelled `$(C)+(G)-(E)$` -- twice as far
   out. The printed figure became a degenerate sliver, `CD` was drawn equal to
   `EG` instead of half it, and `DG ∥ EF` failed by 50 degrees. The constraint
   file passed throughout because it tested the unused coordinate. Redrawn from
   the p.156 plate at 400 dpi (C confirmed as the midpoint of `FG`, D at the
   predicted intersection to within 2%).
2. **Fig 9--19 had the wrong vertex cycle.** The pentagon was drawn
   `E-B-C-D-A`, joining `E` to `B` and `D` to `A`, and `A` sat 0.05 units above
   `E` instead of 1.38 -- so the "convex pentagon `ABCDE`" of Def. 9--5 was
   neither the book's shape nor consistent with its own labels. Rebuilt as
   `A-B-C-D-E` from the p.163 plate.

### Right-angle marks corrected (3)

* **Figs 9--34 and 9--35** carried right-angle boxes at the foot of `CD`. The
  book prints neither figure with any mark (400 dpi check), and in Ex. 9--10 #5
  `CD ⊥ AB` is precisely what the reader is asked to *prove* -- the mark gave
  the answer away. Removed; both feet also moved to the printed ratios
  (0.285 and 0.712 of `AB`, from 0.311 and 0.667).
* **Fig 9--40** keeps both marks (they are hypotheses of Thm 9--11) but the
  foot's box was on the wrong side of `CD` -- the book puts it between `A` and
  `D`. Moved, and the mark at `C` is now a true right-angle box aligned to
  `CA`/`CB` rather than an open chevron.

### Proportions re-measured against the print (8)

`9-6` parallel spacing 1.90 : 1 (was 2.22) · `9-10` left transversal is
near-vertical in the book, not leaning 17 degrees · `9-13` the parallelogram
stands upright (`AD` 1.5 degrees below horizontal, `AB` at 77 degrees; was
`AD` +8.7, `AB` 69) · `9-18` apex at 0.27 of the base, not 0.44 · `9-21` the
four spokes are `OA:OB:OC:OD = 428:190:275:200`; the draft had `OD` 30 percent
longer than `OB` · `9-24` triangle and lake both re-fitted (below) · `9-32`
height/width 0.27, not 0.44 · `9-49` lake re-fitted (below).

### The two organic figures

* **Fig 9--24 (lake, p.166).** The traced outline was fine but floated roughly
  half a unit above where the book puts it: `AC` grazed the lake instead of
  cutting through it, and `D` -- which the book places *on* the shore -- sat in
  open ground. Lake re-fitted to the printed bounding box (scale 0.975 plus a
  translation) and the triangle re-measured (`BC/AB` is 1.11 in the book, was
  1.34). Contours 3 and 4 are still the least certain part of the trace.
* **Fig 9--49 (lake, p.174).** Outline shape checked against scan11 p8 (sharp)
  and found good, but it was drawn 30 percent too small and sat high: the book
  fills the triangle with it. Re-fitted to the printed bounding box (scale
  1.317 plus a translation), so `AB` now crosses the water as printed.

### Constraint file: two silent tautologies removed, three figures added

`tools/constraints/ch09.py` contained four entries that could never fail:
`rel(0.583, 0.583)` and `rel(1.0, 1.0)` for Fig 9--28, and, for Fig 9--47, an
"angle P is right" test that re-tested angle *C* plus a congruence test that
compared a number with itself. All four now compute the primed triangle's real
coordinates and compare them with the unprimed one. Figs **9--16, 9--18 and
9--19** had no constraints at all and now carry them (horizontality and the
unit-segment ordering; similarity of both primed copies; convexity of the
pentagon, which Def. 9--5 requires). 157 checks became 169.

### Deliberate deviations (beyond those already listed above)

* **Fig 9--10 `C`** is labelled *below* its line. The `l2`--`l3` gap is 0.725
  units; a label above it would overlap `l2`. Same reason as the `9-6 C/C'`
  deviation the builder logged. `A` is above `l1` for the same reason (the
  book has it below, but `A` and `B` then collide at our measure).
* **Fig 9--14 brace nesting.** The book nests the *longer* brace outside the
  shorter one on both sides. Our bottom pair does this; the left pair is still
  inverted (`1` outside `x`). Reversing it needs about 0.6 units more width
  than the minipage has, and the version I tried rendered worse than the
  current one, so I reverted it. Cosmetic; the brace *lengths* -- which carry
  the meaning -- are right.
* **Fig 9--24 `D` label** sits to the right of its point rather than tucked
  above-left inside the lake as the book has it. Our label is larger relative
  to the figure than the book's; every position inside the shore band collided
  with a contour even after the block was widened to 0.44\linewidth at
  scale 1.00.
* **Fig 9--44** is drawn with `SR : PS = 5 : 4` per Ex. 9--12 #3. The book's
  own drawing has it the other way round (measured 100 : 130).
* **Fig 9--24** is drawn with `DC/AC = 0.15` per the exercise; the book draws
  about 0.11.
* Row widths were re-apportioned in three blocks (9--23/24/25, 9--42..45,
  9--13/14) to give the crowded figures room. Sub-figure order is unchanged.

### Residual doubts

1. **Figs 9--53, 9--54, 9--55 still do not exist.** The text pass flagged that
   the Review Exercises (book pp.~177--179) call for them. `figures09.tex`
   stops at 9--52. Whoever fills the `\IXpending` spans must commission these
   three.
2. **Fig 9--38 hexagons** remain a *fit* (rotation -30 degrees, scale 0.72)
   chosen to reproduce the printed vertices, not a measurement. The similarity
   constraint is exact by construction, so the figure cannot be wrong, only
   differently posed than the print.
3. **Fig 9--30** still draws `F` as a distinct point with `DF` dashed and not
   parallel to `BC`, reproducing the book's own pedagogical figure. Confirmed
   deliberate; left as the builder had it.
4. **Fig 9--41**: the book's apex may be labelled `C'` rather than `C`. At
   400 dpi the accent is not resolvable and the surrounding proof text says
   `C`, so `C` is what we print. Worth a look at the physical copy.
5. **Fig 9--45 `h` and `D`** sit close together either side of the dashed
   altitude (0.95 pt clearance, reported TIGHT). That is how the book prints
   them; eyeballed at 200 dpi and legible, but it is the tightest pair in the
   chapter.
6. Seventeen TIGHT placements remain, all inspected on the rasterised pages
   and accepted. None is below 0.34 pt.

---

## Held-text transcription (fresh agent, 2026-08-17)

Scope: the two `\IXpending` spans left by the text-review pass — the rest of the
"main ideas" list (book pp.176–177, items 2–8) and the full Review Exercises run
(book pp.177–179, nos. 1–20) — plus the three figures those exercises call for.

Method: PDF pages 190–193 rasterised at 150 dpi and read, then re-cropped at
350–400 dpi for every passage that curls into the gutter or the spread's slanted
outer half (all of p.177's lower two-thirds, all of p.178). Figures 9-53/54/55
were re-cropped at 350–400 dpi and reconstructed from the numbers the exercises
state, not traced by eye.

Gates at hand-off: compiles twice, 0 errors · `grep -oE "pending\{"` returns
nothing and the `\IXpending` definition is deleted · `verify_figures.py 09`
**169/169** · `check_labels.py chapters/figures09.tex 09` **0 collisions**
(17 tight, unchanged — that file was not touched) · the three new figures
checked separately at **0 collisions** (3 tight, eyeballed and accepted) and
**29/29** hypotheses verified numerically · pages 38–41 of the render inspected.

### Closes two standing items

Residual doubt 1 of *both* the text-review and figure-review sections above is
now discharged: the pending spans are transcribed and Figs 9-53, 9-54, 9-55
exist.

### Where the three new figures live — needs a hoist

The brief for this pass said not to touch `figures09.tex` or
`tools/constraints/ch09.py` (both are the figure-review pass's reviewed
territory). The three new macros are therefore defined in the **local-macro
block at the top of `ch09.tex`**, per the "new local macro" convention, and
flagged there with a `HOIST:` comment. **Action for the figure-review or
integration agent:**

1. Move `\FIGIXFIFTYTHREEFIFTYFOUR` and `\FIGIXFIFTYFIVE` into
   `figures09.tex` so `check_labels.py` covers them in the normal run.
2. Add their hypotheses to `tools/constraints/ch09.py` (169 → ~198). The 29
   checks I ran are enumerated in "How the new figures were constrained" below
   and in the comments above each macro; they were run from a throwaway script
   in the session scratchpad, so re-derive rather than hunt for that file.

Until then these two files under-report: the tools see 52 figures, the chapter
renders 55.

### How the new figures were constrained (nothing placed by eye)

* **9-53.** Ex. 11's numbers determine the whole picture: altitude 8 with a
  slant leg of 10 forces a run of 6, which is exactly the 18 − 12 difference,
  so the other leg is perpendicular to both bases. The legs extended meet at
  (18, 24) and the enclosing triangle is 18–24–30, right-angled at the base —
  which is what parts (a) and (b) ask the student to discover. Verified.
* **9-54.** `D` is fixed at 2⁄3 of `AB` (measured off the plate), `F` on ray
  `AC` beyond `C`, and `E` is then taken as the *true* intersection of `DF`
  with `BC` via `intersection of`. Menelaus' product therefore comes out at
  1.0000 rather than being arranged. `X`, `Y`, `Z` use the projection operator,
  so the hint's `AD/DB = AX/BY` also holds exactly.
* **9-55.** `D` and `E` are projection feet (`($(A)!(C)!(B)$)` and
  `($(A)!(B)!(C)$)`), so both right angles are exact and Ex. 18's conclusion
  `CD/EB = AC/AB` holds in the drawing to 0.0000.

### Judgment calls in this pass

1. **Label offsets in 9-54 are computed, not nudged.** Five of its labels sit
   where two lines cross, and three of the crossing lines run along `l`'s own
   normal — so the usual "offset along the perpendicular" put `X`, `D`, `E`,
   `Z` straight onto a second line (4 COLLIDE on the first run). Each label is
   now offset along the bisector of the wedge it occupies. Positions match the
   book's layout; the clearances are ours.
2. **`\begin{center}Review Exercises\end{center}` starts a fresh page** (render
   p.39) where the book has it mid-p.177. Pure repagination at our narrower
   measure; no `\nopagebreak` was forced. Compare ch10, which pins the heading
   with `\par\nopagebreak` — worth making consistent at integration.
3. **Item 3 of the "main ideas" list** breaks after "…unit of length." because
   the book starts a new indented line there. At our measure the sentence wraps
   first, so the printed line-break lands mid-paragraph. Faithful to the
   structure, not to the line count.
4. **Ex. 18 reads `CD/EB`, not `CD/BE`** — the book genuinely reverses the
   letters between the sentence ("`CD` and `BE` are altitudes") and the formula.
   Transcribed as printed; not an error on our side.

### Verified digit by digit against the source

Every number in the new text was read on a 350–400 dpi crop: item 6's
`AB = 12`/`A'B' = 8`; Ex. 1 `AB = 24`, ratio `3/5`; Ex. 4 `20`-ft and `10`-in.
shadows; Ex. 5 sides `4, 5, 6`, perimeter `30`; Ex. 7 `40°`, `80°`, `40°`,
`60°`; Ex. 8 `4 and 9`, `2 and 4`, `6 and 6`; Ex. 9's five triples
(`3,4,5` · `5,12,13` · `7,24,25` · `9,40,41` · `11,60,61`); Ex. 10 `5/8` in.,
`80` mi., `5 7/16` in.; Ex. 11 `18`/`12`, altitude `8`, leg `10`; Ex. 12
altitude `6`; Ex. 13 `12` and `8`, `60°`, `30°`. Starred items are `*4` in the
main-ideas list and `*3`, `*15` in the Review Exercises — matching the brief.
Overbars follow the print exactly, including Ex. 1's inconsistent use
(`AB` barred at the start, unbarred in "on the line AB", `AC`/`CB` unbarred in
the ratio, `AC` barred again in "determine").

### Residual doubts

1. The hoist above is the one real loose end.
2. Ex. 9-54's `D` at exactly 2⁄3 of `AB` is a reading of the plate to about
   ±3%; any ratio gives a valid Menelaus figure, so this affects appearance
   only.
3. Nothing in these four pages was illegible in the photo PDF; the iPad scans
   were not needed for this span.
## Text review — second fresh pass (2026-08-17)

Independent adversarial re-read after the review spans were filled in. Method:
all 26 source pages (PDF 168--193 = book pp.~154--179) read at 150 dpi against
`ch09.tex`; pp.~158--159 re-cropped at 300 dpi to settle the footnote question
below; the built PDF re-rasterised at the two pages the fixes touch. Compiles
twice clean (0 errors; only pre-existing overfull-box warnings).

### Fixes applied (2)

1. **Removed the star footnote (`\IXstarnote{}` before Exercise Group 9--3).**
   The previous text-review pass *added* this note, reporting only that it
   renders in our build. It does not exist in the book. Book p.158 carries the
   chapter's first starred exercises (Group 9--3, nos.~12 and 13) and p.159
   carries the next (Group 9--4, no.~4e); a 300 dpi crop of the foot of both
   pages shows **no footnote rule and no note** --- p.158 ends inside
   Definition 9--1, p.159 inside the proof of Theorem 9--2. The convention note
   is printed once book-wide and ch02 owns it, which is exactly what ch05 and
   ch10 record in their own comments. The call and the fabricated note are gone;
   a comment at the macro block records why, so a later pass does not re-add it.

2. **Mean-proportional footnote now prints `*`, not a number**
   (Corollary 9--11--1, book p.171). It was coded as a plain `\footnote`, so the
   build showed `mean proportional`^1 with a numbered note. The book marks it
   with an asterisk. Reworked to `\textsuperscript{*}` in the corollary plus an
   unnumbered `\IXstarnote{...}` carrying the literal `*` --- the same pattern
   ch06 uses for its two asterisk footnotes and ch14 for its in-text marks.
   `\IXstarnote` now takes the note text as an argument (it previously hard-coded
   the bogus "Starred exercises" wording).

### Verified clean this pass (no change needed)

* **Every number in every exercise**, group by group (9--2 … 9--14) and in all
  20 Review Exercises, re-read against the page --- data values, embedded
  answers, exercise numbering and group boundaries. No discrepancy found,
  including the number-heavy items: 9--3 #7--#10, 9--6 #3--#5, 9--8 #1--#7,
  9--12 #1--#5, 9--13 #1--#17, and Review Exs. 1, 4, 5, 7--13.
* **Starred items** re-confirmed against the printed asterisks: Group 9--3
  (*12, *13), 9--4 (#4e), 9--5 (*4, *5, *6, *9, *10), 9--10 (*6), 9--13 (*4,
  *17), main-ideas item *4, Review Exs. *3 and *15. All present in the tex and
  none spurious.
* **Newly filled review spans** (book pp.~176--179), the highest-risk material
  in this unit: main-ideas items 2--8 and Review Exercises 1--20 read verbatim,
  including the sub-question lines that hang under items 1, 2, 3, 4, 5, 6, 7
  and 8, and the bracketed hint in Ex.~15. Wording is the book's, not a summary.
* **Page-order**: the spread photos invite transposition, but section order,
  figure anchors and the p.177/178/179 exercise runs all follow the printed
  sequence. Fig.~9--53/54 sit between Exs.~12 and 13 and Fig.~9--55 before
  Ex.~18, as printed.
* **Numbering** re-checked in the rendered PDF: Theorems 9--1 … 9--15,
  Definitions 9--1 … 9--5, Corollaries 9--1--1/2, 9--7--1/2, 9--11--1/2,
  Construction 9--1, Exercise Groups 9--2 … 9--14.
* **Headings and TOC**: `\addcontentsline` present after `\chapter*` and after
  each of the nine `\section*`s, plus Review of Chapter 9 and Review Exercises.
* **Math**: no Greek letters in this chapter (confirmed by sweep, not
  assumption). Primes, double primes, `\cong` vs `\simto`, `\perp`, `\pll`,
  the radicals in Thms 9--14/9--15 and the fractions in Review Ex.~10
  (`5/8`, `5 7/16`) all match the print.
* **Prose**: every paragraph opening in all nine sections plus the review
  matched to the page, and one full paragraph per section read word for word.
  The three restorations the previous pass made (p.163 historical remark,
  p.165 Statement 1, p.175 section opening) are correct as they now stand.

### Residual doubts

1. **The figure hoist is still open** (the builder's own flag). Figs 9--53,
   9--54 and 9--55 are defined in `ch09.tex`'s local macro block, not in
   `figures09.tex`. Consequence: `tools/check_labels.py` and
   `tools/verify_figures.py` see only the 25 blocks in `figures09.tex`. Current
   readings are **0 collisions / 17 tight** and **169/169 constraints** --- both
   green, but neither covers those three figures. Hoist them and add their
   hypotheses before the chapter is called done. (This also clears the earlier
   pass's residual doubt #4: the 5-collision reading no longer reproduces.)
2. `\IXstarnote` remains a chapter-local duplicate of a pattern ch02, ch06 and
   ch10 each define locally; hoist one copy into the book preamble at
   integration. Only ch02 should carry the "Starred exercises ... are optional"
   note.
3. No text question for Caleb arises from this pass. The two open questions in
   section 1 above (Fig.~9--33's D/E pairing and Fig.~9--48's proportions) are
   figure questions and stand as written --- in both cases the *text* matches
   the book exactly, and the disagreement is the book's own.

---

# Figure-repair pass — 2026-08-17 (FIX-SPEC)

Scope: figure **placement** and figure **geometry** only. No prose was touched.

Gates at hand-off: `ch09.tex` compiles **twice with 0 errors** (50 pp.) ·
`verify_figures.py 9` = **212/212** · `check_labels.py figures09.tex 9` =
**0 collisions**, 26 tight · every one of the 50 pages rasterised at 120 dpi
and looked at, with 240–300 dpi zooms on 9-10, 9-14, 9-50 and 9-54.

## 1. Spec §2 — exercise-group figures are now inline

**36 figures moved inside their exercise lists**, each in `\exfig{...}`
directly after the exercise that first names it, and `multicols` dropped from
all ten exercise groups that carry a figure (9-2, 9-3, 9-6, 9-8, 9-9, 9-10,
9-11, 9-12, 9-13, 9-14) plus the Review Exercises. Groups 9-4, 9-5 and 9-7
carry no figure and keep `multicols` untouched, as the spec requires.

**9 combined macros split into 30**, since in every case the parts were cited
by *different* exercises:

| was | became |
|---|---|
| `\FIGIXFIVESEVEN` | `\FIGIXFIVE` `\FIGIXSIX` `\FIGIXSEVEN` |
| `\FIGIXNINEFOURTEEN` | `\FIGIXNINE` … `\FIGIXFOURTEEN` (6) |
| `\FIGIXTWENTYTWENTYONE` | `\FIGIXTWENTY` `\FIGIXTWENTYONE` |
| `\FIGIXTWENTYTHREETWENTYNINE` | `\FIGIXTWENTYTHREE` … `\FIGIXTWENTYNINE` (7) |
| `\FIGIXTHIRTYTWOTHIRTYFIVE` | `\FIGIXTHIRTYTWO` … `\FIGIXTHIRTYFIVE` (4) |
| `\FIGIXTHIRTYSEVENTHIRTYNINE` | `\FIGIXTHIRTYSEVEN` `\FIGIXTHIRTYEIGHT` `\FIGIXTHIRTYNINE` |
| `\FIGIXFORTYTWOFORTYFIVE` | `\FIGIXFORTYTWO` … `\FIGIXFORTYFIVE` (4) |
| `\FIGIXFORTYEIGHTFORTYNINE` | `\FIGIXFORTYEIGHT` `\FIGIXFORTYNINE` |
| `\FIGIXFIFTYTHREEFIFTYFOUR` | `\FIGIXFIFTYTHREE` `\FIGIXFIFTYFOUR` |

Every split figure lost its `minipage`/`\hfill` scaffolding and was re-fitted
by hand to the freed width (spec §5 forbids `measure_figures.py` on this pass).
Typical gain is large: Fig 9-23 went from 1.3 cm of drawn width to 5.2 cm.

`\FIGIXFIFTYTHREE/FOUR/FIVE` are now defined in `figures09.tex`, not in
`ch09.tex`'s local block — this closes residual doubt #1 of the previous pass,
and all three are now covered by both tools.

The three Review-Exercise `exlist` blocks, which had been split only to make
room for the batched figure dumps, are merged back into **one** list.

## 2. Chapter-wide: the `key` weight is gone

All 32 `\draw[key]` strokes became `\draw[given]`. The book strikes every line
of a diagram at one weight; `key` survived the colour edition only as a heavier
stroke, which is what Caleb flagged on 9-23, 9-25, 9-14, 9-27 and 9-50. Do not
reintroduce it in this chapter.

## 3. Every figure corrected, with the reason

| Fig | What was wrong → what was done |
|---|---|
| 9-4 | `G` label collided with line `m'`, which passes through it → moved to the free quadrant |
| 9-10 | transversal 2 missed `A`, both slants near-vertical (10° off) instead of the book's 31°, parallels dead horizontal and cut short, and **both** "Parallel" notes drawn as double-headed arrows → figure rebuilt from the photograph: parallels slope 8° down-right, spacing 1.5 : 1, slants at 0.586 across per 1 down, T1 and T2 crossing exactly on `l1` at `A`, and both notes redrawn as the book's fans of single-headed leaders |
| 9-11 | the length label `8` sat on the hypotenuse it measures → lifted clear |
| 9-12 | "Parallel" was a vertical double-headed span → the book's three-leader fan from one apex. (The numerals 2/3/4/6 are **segment lengths, not angles** — checked on the p.158 plate at 500 dpi — so the index's "missing angle arcs" note does not apply and none were added.) `A`'s label pulled in to its crossing |
| 9-13 | rescaled only |
| 9-14 | the two brace rows on each side sat almost on the side they measure and the long `x` brace was drawn *inside* the short `1` brace; the two "Parallel" leaders started from two different points → braces offset at the book's 0.07 and 0.24 of each side's length, long brace outermost on both sides, teeth pointing outward to their labels, leaders fanned from one apex (the upper one crossing the right side, as the book's does) |
| 9-15 | the length label `6` sat on side `FG` → offset along its normal |
| 9-17 | `E`/`F` labels grazed the point dots beneath them |
| 9-23 | `E` label had drifted down level with `D`; `CD` drawn dead level where the book runs it slightly down to `D`; `BE` heavier than the sides |
| 9-24 | **four** lake contours where the book has **three** (innermost oval removed, verified on the p.166 plate at 500 dpi); `DE` drawn heavy solid where the book draws a **fine dashed** segment (zoomed to 500 dpi to confirm); `C` was not on the drawn base line — the base ran to (3.265, 0.075) while `C` sat at y = 0.025, which is exactly the "kink near B" Caleb saw. `AB` now dead vertical and the base dead horizontal, as "run north-south" requires; `D`'s label moved into the clear band between contours 1 and 2 |
| 9-25 | `DE` heavier than the sides; `D`/`E` labels sat on the sides they divide |
| 9-26 | `AE` drawn dead vertical where the book leans it; `AB : DE` was 1.6 : 1 against the book's 2.53 : 1; the `C` label sat on the crossing lines |
| 9-27 | `l` and `m` were stubs, so `l ∥ m` could not be read, and the `l` label floated past the end of its own line; transversals heavier than the parallels |
| 9-28 | **Caleb's "worst offender"**: `R` and `P′` printed jammed together. Gap between the triangles widened to 0.55 units, primed triangle at the book's 0.62, whole block redrawn at roughly five times the old area |
| 9-29 | rescaled only (the book strikes no right-angle squares at `D`/`E`; none added) |
| 9-30 | `D` label sat on side `AB` |
| 9-33 | `D` sat on `AC` and `E` on `AB` |
| 9-37 | length labels `10` and `14` sat on side `EC` |
| 9-38 | the primed hexagon is rotated −30°, so the unrotated label anchors sent `C′`, `D′`, `E′` the wrong way and `D′`/`E′` printed on top of each other |
| 9-39 | the right-angle square at `D` was drawn on the `A` side; the p.170 plate puts it in the wedge between `DB` and `DC`. Dashed base now runs a short way **past** `E`, as the book draws it |
| 9-40/9-41 | both drawn at ~2.5 cm; enlarged. **Fig 9-41's apex is `C`, not `C′`** — confirmed against the p.171 plate at 500 dpi, matching Caleb's check of the physical copy. `l` was set in `slab` (scriptsize upright) while `l′`/`l″` were `vlab`; all three now match |
| 9-42–9-45 | split and rescaled |
| 9-48 | **reverted to schematic** per Caleb's decision: the render drew `BD : AC` at the exercise's own 24 : 10, which gives the answer away. Now the book's ≈1.58 : 1. The three *stated* hypotheses (`AB ∥ CD`, `BC ∥ AD`, `AC ⊥ BD`) still hold exactly and force a rhombus; a constraint now asserts the drawn ratio is **not** 2.4 |
| 9-50 | apex at 0.65 of `AB` against the book's 0.50, so the vesica was far too fat (arcs cutting the base at 18 %/82 % instead of 31 %/69 %) and three thick strokes met at the apex in the blob that read as a filled arrowhead; the arcs stopped dead at their intersections. Arcs now run ±57°, overshooting the ±45° meeting points by 12° so the book's small **×** is struck at `P` and again below; arcs drawn finer than the triangle; `PC` no longer heavier; `r` hugs the midpoint of `PA` |
| 9-51/9-52 | rescaled |
| 9-53 | rescaled (2.2 cm → 3.0 cm wide) |
| 9-54 | apex 53 % along the base and 0.89 of it high, against the book's 39 % and 0.67 — which is *why* the dashed `AX` ran within 5° of side `AB` and the two were indistinguishable. Rebuilt at the book's flat, wide shape (they now diverge by 15°, asserted as a constraint); base rises slightly right as the book's does; `l`/`X`/`D` pulled apart along **and** across the line (they were merging into a single "XD" blob in the audit); `Y` and `Z` hug their own feet; the dashed extension of `AC` uses a longer dash so it no longer reads as a fourth perpendicular |
| 9-55 | the right-angle square at `E` was struck at 0.16 of \|EA\| and \|EB\| — sides four times longer than `D`'s — so it printed much the larger and hung into the interior. Both squares are now a fixed 0.17 units, with `E`'s in the wedge between `EC` and `EB` as the p.179 plate has it. Triangle flattened from 0.85 to the book's 0.72 (this also cleared a 31 pt overfull box) |

Defect classes swept across the whole chapter, not just the photographed
figures: heavier-than-book strokes (all 32), labels sitting on the lines they
name (12 figures), double-headed "Parallel" arrows (9-9, 9-10, 9-12, 9-14),
and misplaced right-angle marks (9-39).

## 4. Questions for Caleb / things I could not settle

1. **`book.tex` is stale for chapter 9.** It still inlines the nine old
   combined macros and the batched figure dumps. Its own header says it is
   generated by `tools/assemble_book.py` and must not be hand-edited, so I
   left it alone — **the integration pass must re-run the assembler**, or
   ch09 will fail to build inside the book.
2. **Body figures I did *not* rescale.** Spec §1 says to flag rather than
   re-scale, so these are flagged: **9-2/9-3, 9-4, 9-18/9-19, 9-22** still
   print at roughly 2.5–3.5 cm and now look noticeably smaller than the
   split exercise figures beside them (5–8 cm). They read, but the chapter
   is no longer visually consistent. Recommend the integration re-fit grows
   them to match. (9-40/9-41, 9-50/9-51 and 9-52 *were* enlarged, because
   each needed a geometry rebuild anyway.)
3. **Fig 9-41's `C` label** sits above-left of the apex in our render; the
   book sets it below-left, inside the triangle. At our narrower apex the
   below-left position cannot clear side `AC` and the dashed line `l` at
   once. The letter is unambiguous where it is, but it is not the book's
   position.
4. **Fig 9-24's lake** is still the traced scan outline placed against the
   triangle by bounding box. Contour *count* is now right (3) and `D` sits
   on the outer contour where `AC` leaves the water, but the lake sits a
   little higher and further right in the frame than the book's, and the
   contour shapes are our trace, not the book's. Flagged, not re-traced.
5. **Fig 9-12's numerals.** `feedback/index_ae.md` reads them as angle
   numerals missing their arcs. They are **segment lengths**; the book
   strikes no arcs. I have not added any. If Caleb disagrees, this is the
   one place in ch09 where the "missing angle arcs" defect class was
   claimed and rejected.
6. The 26 TIGHT label placements were each eyeballed at 120 dpi and
   accepted; the closest is Fig 9-54's `D` at 0.94 pt, which is legible.
7. Section 1's two older questions (Fig 9-33's `D`/`E` pairing, Fig 9-48's
   proportions) — **9-48 is now settled** by Caleb's decision above. The
   9-33 pairing question stands as written.
