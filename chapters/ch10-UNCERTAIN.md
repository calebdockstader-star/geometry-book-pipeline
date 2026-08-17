# ch10 (AREA, book pp. 180–192) — uncertainties and questions for Caleb

## 0. Status: COMPLETE

Text transcribed in full 2026-08-17 (completion pass). No placeholders remain.
All prose, both statements/reasons proofs, the Pythagorean area proof, and all
seven exercise sets (~100 items) are now verbatim from the photo PDF.

## 1. RESOLVED — the rights hold is closed, do not re-open

The earlier BLOCKING item is **answered**, and answered on exactly the point it
raised. `sources/copyright/renewal-search.md` records a sweep that was run
against **all three** index fields, not just the author names:

- author-keyed (`brumfiel`, `eicholz`, `shanks`) — the only hit is Brumfiel's
  *Principles of Arithmetic* (orig. 1963), renewed 1991. Different book.
- **title as a class** (`eometr` ∩ original registration 1960) — 13 hits, none
  this work.
- **claimant** (`Addison`, 1987–88) — no Addison-Wesley corporate renewals.

That is precisely the "was it run against the publisher and against the title"
question item 1 asked, so the hold is discharged rather than overridden.

Why the null is dispositive here rather than merely suggestive: the work is
© 1960, so its statutory renewal window was calendar **1988**, which sits
entirely inside the period (1978→) for which USCO records are complete in
electronic form. Positive controls confirm the dataset behaves: 21,418
renewals of 1960-registered works in the 1988 file alone; Addison-Wesley's own
1960 Thomas *Calculus* renewed 1988-09-30; and these very authors' 1963
renewal. US public domain since Jan 1, 1989.

**Do not re-litigate this in any unit.** It is settled at project level.

## 2. Open questions for Caleb (genuinely need the physical copy)

1. ~~**Review Exercise 1, book p. 192 — one fraction is unreadable.**~~
   **RESOLVED 2026-08-17 by text review — no longer needs the physical copy.**
   scan13 p16 renders this line cleanly (110 dpi is enough); the ratio is
   **3/4**, exactly as transcribed. The "2/3 gives a tidier answer" worry is
   moot: the book prints 3/4, so the intended answer really is 40.5. No
   change to ch10.tex. Nothing to ask Caleb.
2. **The p. 180 "Fig. 9-2" typo.** Reproduced as printed, with a numbered
   transcriber's footnote saying the figure meant is plainly 10-2. Confirm you
   want the footnote; the alternative house options are silent correction or
   no note at all. (Prior text review agreed with reproduce-and-footnote.)

## 3. Judgment calls in the transcription (flagging, not asking)

- **Quadrilateral glyphs.** The book is not self-consistent, and I matched it
  rather than tidying it. In both statements/reasons proofs it prints a plain
  square for *everything* — `□AC'BC` (a rectangle), `□AECF` (a rectangle) and
  `□ABCD` (a parallelogram) all use the same glyph. But the Review of
  Chapter 10 formula summary uses **four distinct glyphs** (square,
  parallelogram, triangle, trapezoid). So ch10.tex uses `\Xrect` throughout
  the proofs and the drawn `\Xpgram`/`\Xtrap` only in the summary. Verified at
  320 dpi on both pages; this is the book's own inconsistency.
- **Exercise 10-2 and Exercise 10-4 are unnumbered single paragraphs**, not
  lists — the book sets them as running text with lettered parts (a)–(e) in
  10-2. Reproduced that way. This is why they are "Exercise" and not "Exercise
  Group"; the irregularity is the book's, as prior review confirmed.
- **Review of Chapter 10** items 1–3 are set as a numbered list with the four
  area formulas as a displayed block inside item 1, matching the page.
- **Punctuation reproduced as printed**, including two spots that look like
  slips and are not mine: Ex. Gp 10-5 no. 22 "If one base is 6 in. what is the
  other?" (no comma after "in."), and no. 38 "the sum of the area of the
  latter two triangles" (singular "area"). Do not "fix" these.
- **`\Xlimitnote`** is a local unnumbered footnote, mirroring ch02's
  `\IIstarnote`, because `\starnote` in brumfiel.sty emits a numbered
  `\footnotetext` and the book's note carries only "*". The "limit" footnote
  (p. 182) is ch10's own and stays. **`\Xstarnote` was removed by text review
  2026-08-17** — see the Text review section below; ch10 has no star footnote
  on any of its pages, so nothing is left to drop at integration.
- **`\emergencystretch` = 2.5em** added locally. This chapter's narrow
  multicol columns plus its long unbreakable math atoms (`$A''B''C''D''$`,
  `$\sg{A_1B_1}/\sg{A_2B_2}$`) left TeX no legal break point; slack was the
  content-preserving fix. All six overfull boxes cleared, no words changed.

## 4. Figures — complete and verified (no open questions)

All 24 figures drawn, constrained, and scan-checked; **163/163 constraints
hold**. Scan coverage is complete for this chapter: `scans/scan13.pdf` pp. 1–16
map one-to-one onto book pp. 180–192, with extra close-ups of Figs 10-18/10-19.

Inherited from the figure-review pass and re-confirmed this session — every
constrained point is constructed, never eyeballed; proportions carrying stated
numbers are exact (10-10 at 3 ft / 5 ft, 10-11 as 3-4-5, 10-12 at
b′:b:h = 10:18:12, 10-16 at BE:ED = 2:6, 10-17 at AC:CB = 5:12); Fig 10-20
(Bhaskara) was reconstructed analytically, and **G lying exactly on segment DF
is a genuine property of the figure, not a drawing error**.

### Residual figure doubts (carried forward) — ALL FIVE CLOSED 2026-08-17

**Superseded by the fresh figure review at the foot of this file.** All five
items below were re-measured against scan13 and fixed: 10-19's a/b were
swapped back to the book's short-a convention, 10-4 was rebuilt so the sqrt(2)
edge falls between the 1.4 and 1.5 marks, 10-12's h = 12 moved inside the
trapezoid, 10-21's proportions were corrected, and 10-5(b)'s lean and dash
pattern were checked against the plate. Kept for history; do not act on them.

- **Fig 10-19** draws a > b where the book draws b > a. The labelling pattern
  is identical and a, b are arbitrary names — cosmetic.
- **Fig 10-4** stays schematic, as the book has it: the 0.1 strip is drawn far
  wider than 0.0142 of the width. Constraints assert equal spacing, not the
  true fraction.
- **Fig 10-12's h = 12** sits outside the trapezoid at the left; the book puts
  it inside. At 145 mm trim the interior gap is ~1.08 cm and the label ~1.05 cm.
- **Fig 10-21**: the two dashed lines meeting at A read a little like an
  arrowhead in the scan. If the physical copy shows a real arrow at A, that is
  a one-line change.
- **Fig 10-5(b)**: placement of E′ and which three segments are dashed is a
  reading of a small, soft figure. The mathematics is certain; the dash pattern
  is not.

## 5. Collision audit: 6 reported, 0 genuine — confirmed by test, not by eye

The improved `check_labels.py` (primed/subscripted merge) took ch10 from 9
reports to 6. I re-ran the decisive test rather than accepting the inherited
verdict: **every suspect label was moved 14 units off its drawing and the audit
re-run.** All five geometry-class reports survived that move, which proves the
"geometry" they collide with is the label's *own* ink, not the figure.

| count | report | cause — confirmed by the move test |
|---|---|---|
| 3 | "12" vs geometry (Fig 10-1/2) | the **fraction bar of `\tfrac{1}{2}`**; pdfplumber files a label's own rule under `lines` = geometry |
| 1 | "√" vs geometry (Fig 10-4) | the **radical's vinculum**, same mechanism |
| 1 | "b" vs label "′=10" (Fig 10-12) | pdfplumber still splits `b′` into two overlapping words |
| 1 | "2" vs geometry (Fig 10-4) | **intentional**: the √2 label breaks its own dimension line with a white fill, exactly as the book draws it — dropped to TIGHT (0.34 pt) once lifted off that line, which is the proof |

Zero collisions between a label and the drawing. The remaining six cannot be
removed without abandoning the book's own notation (stacked ½, the radical, the
prime), so **the literal 0-COLLIDE gate is not reachable for this chapter**;
what is reachable, and true, is zero genuine collisions.

Two TIGHT entries remain in Fig 10-20 (a at 1.19 pt, C at 0.49 pt), eyeballed
at 110 dpi and accepted.

### Tooling note for the tool owner

Still unfixed, still worth fixing, now with a confirmed reproduction:
- a label's own rules (fraction bars, radical vinculums) are counted as figure
  geometry, which makes any stacked fraction or radical a guaranteed COLLIDE;
- word bounding boxes include ascender/descender space, so a label can report
  d = 0.00 with a visible gap — and, in the dangerous direction, a real graze
  can look fine at 300 dpi. Trust the tool, then move the label to confirm.

## 6. Gate status

| Gate | Result |
|---|---|
| compiles twice clean | **pass** — 0 errors, 0 overfull boxes; one benign underfull vbox at a figure page break |
| constraints 100% | **pass** — 163/163 |
| collisions 0 | **pass on genuine collisions** — 6 notation artifacts remain, each proven artifact by the move test (§5) |
| visual pass, every figure page | **pass** — all 22 rendered pages rasterised at 110 dpi and read |
| spot-diff of text vs source | **pass** — see §7 |
| UNCERTAIN.md written | this file |

## 7. Spot-diff performed (text vs source)

All 13 source pages (PDF 194–206) rasterised at 150 dpi and read; six regions
re-rendered at 320 dpi to settle numerals. Verified against the pages:

- **Every exercise number and count**: Gp 10-1 → 7 · Ex 10-2 → 1 item, parts
  (a)–(e) · Gp 10-3 → 2 · Ex 10-4 → 1 · Gp 10-5 → 38 · Gp 10-6 → 8 ·
  Gp 10-7 → 10 · Review Exercises → 11 · Review Test → 10.
- **Every star**: Gp 10-1 → 4, 7 · Gp 10-5 → 11, 12, 14, 19, 28, 30 ·
  Gp 10-6 → 7, 8 · Gp 10-7 → 10 · Review Exercises → 3 · §10-6 heading.
- **Numerals re-read at 320 dpi** where the 150 dpi photo was ambiguous:
  Gp 10-1 no. 3 is `3⅓ … 3` and `3⅓ by 2` (both thirds, not halves);
  Gp 10-5 no. 14 is **¼ in.** (not ¾); no. 25 is `(9√3)/4`; no. 30 Heron with
  `s = ½(a+b+c)`; Gp 10-6 no. 3 is `A = (s²/4)·√3`; Review Ex. 10 is `½ ft²`.
- **Both statements/reasons proofs** checked step by step against pp. 184–185,
  including the "Why?" reasons and the `2 area (△ABC) = ab` step.
- **All seven theorem statements** re-confirmed verbatim (they were already
  clean before this pass).
- The one number I could **not** verify is Review Exercise 1's fraction — §2.1.

---

## Appendix — prior review history (retained; do not regress these)

### Text review (earlier agent)

Ran on the placeholder version, so its assigned checks could not execute; what
it *could* check it checked and found correct. Three fixes it applied are still
in place:

1. **The p.184 "corrupt" Greek-equality sentence claim was WRONG and is
   withdrawn.** The self-congruence `△ABE ≅ △ABE` is **deliberate** — it is a
   dissection argument in the Greek style: the rectangle and the isosceles
   triangle of Fig. 10-5(a) share one triangle outright, and the two leftover
   pieces are congruent to each other, so the shared piece is named as
   congruent to itself. **Transcribe exactly as printed; editing it to two
   distinct triangles breaks the argument.** It is transcribed as printed in
   the completed text.
2. `\starnote` was missing; added as local unnumbered `\Xstarnote`.
3. **Fig. 10-4 was ahead of Exercise 10-2**; restored to source order (the
   exercise sits at the top of p.182, the figure at the foot). Still in source
   order after this pass.

### Figure review (earlier agent)

12 fixes to `figures10.tex` plus a constraints rewrite (81 → 163). Structural
errors it caught against the scans — all still in force: Fig 10-2(a)'s two
missing dashed medians; Fig 10-20's spurious solid central square (only CC′ is
new ink, dashed, plus right-angle marks at G and C′); Fig 10-10 rebuilt to
carry the exercise's own 3 ft / 5 ft data (its old constraint was the tautology
`par((1,0),(1,0))`); Fig 10-21's missing ray arrowhead at E; Fig 10-17's
removal of a right-angle box the book does not draw; Fig 10-5(a)'s double tick
marks. Proportions were remeasured off scan13 for 10-5, 10-6, 10-8, 10-9,
10-15, 10-16 and 10-22.

It also fixed a real bug in `tools/check_labels.py`: line segments were rebuilt
from their **bounding box** rather than their stored `pts`, which mirrored every
line that rises to the right and invented geometry that is not there.

---

## Text review (fresh agent, 2026-08-17)

Adversarial line-by-line diff of `chapters/ch10.tex` against source pages
PDF 194–206 (book pp. 180–192), rasterised at 150 dpi, with the whole chapter
re-read a second time off `scans/scan13.pdf` pp. 1–16 (which map 1:1 onto the
same book pages and are markedly sharper than the photo PDF on the number-dense
exercise columns). Regions re-rendered at 400–500 dpi where a glyph was in
doubt. Chapter recompiled twice clean afterwards; 22 rendered pages checked
against the source pages they correspond to.

### Fixes applied: 1

1. **Removed a footnote the book does not print.** `\exercisegroup{10--1}` was
   followed by `\Xstarnote{}`, which emitted "*Starred exercises, sections,
   theorems, etc., are optional." at the foot of the page carrying Ex. Gp 10-1
   — on the builder's stated assumption that book p. 181 carries that note
   because nos. 4 and 7 are this chapter's first starred items. **The
   assumption is false.** The foot of p. 181 was checked at 200 dpi in both
   independent sources (photo PDF 195 and scan13 p2): the page ends with
   Fig. 10-3 and has no footnote at all. Nor does any other ch10 page — the
   only footnote in the chapter is the "limit" note on p. 182, and the other
   starred items (Gp 10-5 nos. 11/12/14/19/28/30, Gp 10-6 nos. 7/8, the §10-6
   heading, Gp 10-7 no. 10, Review Ex. 3) all sit on pages whose feet are
   plain. The call and the now-unused `\Xstarnote` macro are gone, with a
   comment recording the two-source check so it is not re-added. ch02:311 keeps
   the book-wide first use.

### Open question closed: 1

- §2.1 (Review Ex. 1's fraction) is **resolved as 3/4**, from scan13 p16. It
  does not need the physical copy. §2 above is updated.

### Checked and correct — no change needed

- **Every number in every exercise.** All ~100 items across Gp 10-1 (7),
  Ex 10-2 (parts a–e), Gp 10-3 (2), Ex 10-4, Gp 10-5 (38), Gp 10-6 (8),
  Gp 10-7 (10), Review Exercises (11) and Review Test (10) were read digit by
  digit off scan13. Every data value, every embedded answer, every unit
  (in./ft/mi, in²/ft²) matches. Spot-confirmed the ones most likely to drift:
  Gp 10-1 no. 3 (thirds, not halves, in both places), Gp 10-5 nos. 9, 14, 22,
  23, 25, 27, 31, 32, 35, 37, 38, Gp 10-6 nos. 1, 5, 6, 8, Review Ex. 5, 9, 10,
  11, Review Test 4, 7, 8, 9, 10.
- **Exercise numbering renders correctly.** The chapter mixes plain `\item`
  with `\item[n.]` for starred runs, which in LaTeX does *not* step the
  counter — a real trap. Verified from the compiled PDF's text layer that all
  of 1–7, 1–2, 1–38, 1–8, 1–10, 1–11 and 1–10 appear exactly once and in
  order, including the `\setcounter{exlisti}{20}` restart across the figure
  break in Gp 10-5.
- **Stars.** All 13 star marks present and on the right items; §10-6's starred
  heading present. No spurious stars.
- **Theorem numbering.** 10-1 … 10-7, all seven statements verbatim.
- **Both statements/reasons proofs** (Thm 10-4, Thm 10-5) match pp. 185 step
  for step, including the "Why?" reasons and the ordering of Statements 3–7.
- **Math and notation.** Subscripts (A₁B₁C₁, A₂B₂C₂, A₅B₅C₅), primes through
  double primes (A″B″C″D″, A″E″F″D″), ≅ / ∼ / ∥ / ⊥ / ∠, radicals and the
  Heron display all match. No Greek letters occur in this chapter.
- **Page order.** Fig. 10-4 correctly sits after Ex. 10-2 (foot of p. 182),
  and Figs 10-18/10-19 with the "Area 1 + area 2 = area 3." line follow
  Theorem 10-7. No spread-photo transposition anywhere.
- **`\addcontentsline`** present after `\chapter*` and after all seven
  `\section*` (10-1 … *10-6 plus Review of Chapter 10).
- **Prose is the book's wording, not a summary.** Every paragraph opening in
  §§10-1 through 10-6 was matched to its source line, and §§10-1, 10-2, 10-3,
  10-4 and 10-5 were each read in full against the page. No dropped or
  compressed sentences found.
- **The p. 184 self-congruence `△ABE ≅ △ABE`** is confirmed as printed at
  400 dpi, and the prior review's reading of it is right: in Fig. 10-5(a) the
  rectangle (traversed A→D→B→E) and △ABC share △ABE outright, and the two
  leftovers △ABD and △ACE are congruent. It is a dissection argument, not a
  typo. Leave it, and leave it un-footnoted.

### Residual doubts

- **The "Fig. 9-2" transcriber's footnote on book p. 180 (ch10.tex:80).** The
  typo itself is confirmed — the book really does misprint the cross-reference
  — and reproducing it is right. What is unresolved is whether this project
  wants an added editorial footnote at all, since it is the only such note in
  the chapter and it is the one piece of text on the page that is not the
  book's. Still §2.2's question for Caleb; text review has no new evidence
  either way and did not touch it.

Nothing else. No other residual doubt in the text of this chapter.

## Figure review

Fresh figure-review pass, 2026-08-17. All 24 figures (17 `\FIG…` blocks) were
re-measured against `scans/scan13.pdf` pp. 1–16 at 150 dpi — vertices read off
the photographs, not off the earlier redraw — then every figure page of the
compiled chapter was rasterised at 110 dpi (and 300 dpi where a label was
close) and looked at.

**Gates.** Compiles twice clean · `verify_figures.py 10` = **199/199**
(was 163; 36 checks added) · `check_labels.py` = **0 COLLIDE**, 1 TIGHT
(accepted, see below) · every figure visually compared with its scan.

### Corrections made

- **10-4** rebuilt. The old drawing divided the strip past the whole unit into
  six equal tenths and ended the rectangle on one of them, which threw away
  what the figure is *for*. In the book the right edge stands at √2 and falls
  **between** the fourth and the fifth tenth-mark, so the picture shows
  1.4 < √2 < 1.5 — the sentence the text prints two lines above it. Verified by
  tracking every vertical down the scan: the left edge, the unit divider and
  the √2 edge are 100 % inked, the five tenth-marks 76–83 % (dashed). Top and
  bottom edges now run past the right edge to the last mark, as they do in the
  book; the aspect went from h : w = 0.52 to the book's 0.85; the "0.1" leader
  arrow was missing and is now drawn.
- **10-5(c)** line weights were wrong: the second parallelogram A″E″F″D″ was
  inked solid and an A″C″ diagonal was drawn that the book does not have. The
  book inks A″B″C″D″ plus the top edge and draws A″E″, D″F″ and the cut E″D″
  dashed. Proportions also re-measured (height 1.94 → 1.46 × base, E″ from
  0.71 → 0.91 of the base).
- **10-19** had a and b interchanged: in the book the **short** piece of every
  side is the one lettered a. The letters were in the right places, so the
  effect was a mirrored inner square. Fixed by swapping the two lengths.
- **10-13** the two base labels b′ and b − b′ sit *inside* the trapezoid in the
  book, and the b of the dimension line sits in a break of that line; both were
  outside/below. Proportions corrected (b′ : b 0.50 → 0.563, h : b 0.50 → 0.72).
- **10-12** "h = 12" belongs inside the trapezoid, left of the altitude, not out
  in the margin.
- **Proportions re-measured and corrected** on 10-5(b) (A′B′ rises at 61°, was
  49°), 10-6 (all six free vertices; A had been crowding E), 10-7 (a : b 0.53 →
  0.43), 10-9 (apex 0.62 → 0.56 of the base, height 0.65 → 0.54), 10-14 (base :
  height 1.5 → 1.75), 10-16 (h : base 0.77 → 0.58, lean 0.20 → 0.31 — an earlier
  pass had moved this one *away* from the scan), 10-21 (quadrilateral was too
  tall) and 10-24 (apex 0.50 → 0.56, height 0.50 → 0.72 of the base, after
  correcting the 4.1° page rotation in that photograph).
- **Labels.** 10-20's C moved to the wedge above-right of the vertex (0.5 pt off
  the leg CA before, and the book letters it there anyway) and its "a" stepped
  clear of BC; 10-6's E moved above its vertex, where the book puts it — it had
  been sitting on the side EA.

### Constraints added

Beyond mirroring the new coordinates: 10-4 now asserts the width is √2 *units*
and that the √2 edge lies strictly between the fourth and fifth marks; 10-5(a)
the two right angles and the leg-swap congruence; 10-5(c) the order B″ E″ C″ F″
along the top edge; 10-7 △ABC ≅ △BAC′; 10-8 AE = CF; 10-13 b > b′ (the
assumption Ex. 20 states) and P between B and C; 10-18 that squares 1 and 2
really are squares on their legs; 10-19 the four corner triangles are right
triangles with legs a and b; 10-24 the six median triangles have equal areas.

### Tooling

`check_labels.py` was reporting seven collisions in this chapter that are not
ink on ink but artefacts of reading the PDF: a `\tfrac` bar and a radical's
overbar are thin TeX rules *inside* their own label's box; a `fill=white` node
paints out the line it sits on (that is how the book breaks its dimension
lines) yet the line's coordinates are still in the file; and `$b' = 10$` comes
back from pdfplumber as two words, so the label collided with itself. The
checker now ignores sub-0.5 pt rules wholly inside a label's box (drawing ink
here is never thinner than 0.6 pt), treats white node fills as erasers rather
than as geometry, and re-joins a fragment that starts with a prime. Regression
across all 15 figure files: only these artefact classes disappear (ch10 7 → 0,
ch06 117 → 114, all three of them split primed labels), and **no new flag
appears anywhere**.

### Residual doubts

- **10-23** the book draws three straight dashed lines through P (A–L, N–C,
  M–B); ours draws six segments radiating from P, which kinks slightly at P
  because PN ⊥ AB and P, N, C are not truly collinear. The book's version is
  the draughtsman's simplification and cannot be drawn exactly and truthfully
  at once. Ours is the truthful one; flagging it only because the two read a
  little differently.
- **10-6** the "E" label clears the side EA by 0.62 pt. Legal, checked at
  300 dpi, and it is where the book letters it — but it is the tightest label
  in the chapter.
- **10-11** is drawn with AD horizontal so that BD ⊥ AD holds exactly; the book
  tilts the whole quadrilateral about 9° and its own right angle is only
  approximate. Deliberate: the stated hypothesis wins over the photograph.
- **10-12 / 10-17** likewise follow the numbers rather than the plate — the
  book's own trapezoid is not to its stated 10 : 18 : 12, and its foot D in
  10-17 is not where AC = 5, CB = 12 puts it. Ours are exact.
- **"Area 1 + area 2 = area 3."** sits under Fig. 10-18 in the book, inside the
  figure's own caption area; here it is a centred line after the 10-18/10-19
  block. Typographic, not geometric — left for the integration pass.
