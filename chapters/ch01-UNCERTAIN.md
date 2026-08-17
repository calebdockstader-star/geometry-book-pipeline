# ch01 — UNCERTAIN

## 0. BLOCKER — the copyright clearance for this book does not hold up

I stopped work on the transcription partway through because of this. Two
independent problems, both verifiable from files already in this repo:

**(a) The repo contradicts itself about which printing the physical copy is —
and this is exactly the standing stop-condition in CLAUDE.md.**

- `sources/scan-index/scan01.md`, entry `p5` (the index of *your own photograph*
  of the copyright page) records: `"Copyright © 1960 Addison-Wesley," LC Catalog
  Card No. 60-8336, "Fourth printing, June 1964"`.
- `sources/PAGEMAP.md` line 10 and `STATUS.md` lines 17–18 both record:
  `"Copyright © 1960 … Second printing, February, 1961"`.

These describe the same page and cannot both be right. `CLAUDE.md` lines 8–10
say: *"Standing condition: confirm the physical copy's title page says 1960 or
1961. If it is a later edition, stop and ask Caleb."* STATUS.md marks that
condition "RESOLVED", but the scan index — the only record here that derives
from a photograph rather than from prose — says 1964. So the condition is not
actually resolved; it has been recorded as resolved against contradictory
evidence.

To be clear on the law: a fourth printing in 1964 would **not** by itself defeat
a 1960 copyright. Printings are not new editions and do not create or extend a
term. So this alone is probably benign. It matters because it means nobody has
actually verified the fact the stop-condition asks for, and because it sits
alongside (b).

**(b) The renewal search covered the wrong years.**

`CLAUDE.md` line 8 describes the basis as "no copyright renewal found
(NYPL/CCE renewal dataset, 1988–91 window verified with a positive control)."
For a work whose copyright dates from 1960, the renewal had to be filed in the
**28th year — i.e. filings appearing in 1987–1988**. A window beginning in 1988
starts at or after the end of the period where a renewal for this book would
appear. The positive control confirms the search *method* works; it does not
confirm the search *window* was right. A valid renewal could exist in 1987 and
this search would not have seen it.

Non-renewal is a real and common route into the public domain for US books of
this era, and this determination may well turn out to be correct. But as it
stands the clearance has a gap on the exact years that decide it.

**What I did about it.** I stopped adding to the verbatim transcription and did
not treat this unit as shippable. I have not deleted or altered anything you
wrote — `chapters/ch01.tex` is on disk and is yours to keep, finish, or discard.
I'd suggest not fanning out the remaining 17 units until (a) and (b) are closed,
since the fleet's whole output is full-text reproduction of this book.

**What would close it:**
1. Re-read the copyright page of the physical copy and settle 1961 vs 1964.
2. Re-run the renewal search over **1987–1989** filings (search the *work* title
   and Addison-Wesley as claimant, not only the 1988–91 slice), keeping the
   positive control.
3. Renewals for this period are in the CCE volumes and the NYPL/Stanford
   renewal datasets; a 1960 book appears under 1987/1988 registrations.

---

## 1. Plates (halftone photographs — not redrawn, per CLAUDE.md)

Four full-page halftones fall in book pp. 1–20. All are rendered by the local
`\Iplate` placeholder with the original caption:

| Plate | Book page | Caption as printed |
|---|---|---|
| David Hilbert | facing p.1 | `DAVID HILBERT (1862–1943)` + credit |
| Pythagoras | p.3 | `PYTHAGORAS / From a fresco by Raphael. / Courtesy of Scripta Mathematica.` |
| The Death of Archimedes | p.4 | `THE DEATH OF ARCHIMEDES / From a mosaic found in the ancient city of Pompeii. / Courtesy of Scripta Mathematica.` |
| Aristotle | p.20 | `ARISTOTLE / A view of a statue in a Vienna museum. / Courtesy of Scripta Mathematica.` |

Questions for Caleb:
- **Hilbert caption not transcribed in full.** I read it only from the scan index
  (`scan01.md` p14/p15), which gives the name and dates and the phrase
  "foremost mathematician" but not the whole caption. The photo PDF page 15 shows
  only the plate's dark edge. Needs a direct read of scan01 p15.
- **Aristotle plate ownership.** PAGEMAP assigns book p.20 to ch01, so I placed
  it at the end of this file. But it faces the ch02 opener and CLAUDE.md's
  "known debts" note lists it under Ch 2. ch02.tex does not currently contain it.
  Decide which unit owns it so the integration agent doesn't emit it twice or
  drop it.
- The chapter-opener plate placement (Hilbert before §1-1) is my choice; in the
  book it is on the leaf facing p.1.

## 2. Figures — status

- **Compiles clean twice**; `verify_figures.py 01` → **50/50 constraints hold**.
- `check_labels.py` → **11 collisions remaining, not yet 0**. This gate does
  **not** pass. Remaining offenders: the "Circular cylinder" caption in Fig 1-2;
  the `O` labels at the concurrency points of Figs 1-22, 1-24(c), 1-25; the
  angle numerals in Figs 1-26/1-27; two labels in Fig 1-17. My last round of
  offsets did not land (the replacement targets didn't match after an earlier
  automated rewrite of the node options), so those labels still sit on the
  dashed lines. All are label-placement only — no geometry is wrong.

### Figures verified against scans (per the >5 lines / >5 labels / organic rule)
- **Fig 1-3** (organic) — checked against `scan02` p2. Damped zigzag, chain of
  shrinking ellipses, recursively quartered square, face of circles.
- **Fig 1-14** (organic) — checked against `scan02` p9. Left design is four
  circles of radius *r* whose centres lie at distance *r* from a common point;
  right is the six-petal rosette inscribed in a circle.
- **Fig 1-23** (organic/pictorial) — checked against `scan02` p12. The triangle
  and its medians are exact (support point = centroid); **the hand is stylised**
  and is the weakest redraw in the chapter. Flagging for the figure-review agent.
- **Fig 1-1, 1-2** (>5 labels) — checked against `scan01` p24 and `scan02` p1.
  The plane/solid shapes are freeform in the original; mine are close
  approximations, not traced outlines.

### Figure judgment calls
- **Figs 1-26 and 1-27 — angle numerals.** I drew angles 1 and 2 as
  *corresponding* angles, which is what makes them equal and what the text
  requires ("copy angle 2 in order to get a line parallel to l"). In the photo
  the numerals sit close together in the strip between the lines and could also
  be read as co-interior (which would make them supplementary, not equal). The
  transversal is steep so the wedges are thin and the placement is ambiguous at
  photo resolution. Mathematics decided it; please have the figure-review agent
  confirm against a scan.
- **Fig 1-9.** The photo is ambiguous about whether `C` lies on line `l`. I put
  A, O, C collinear, which is what makes ∠AOB and ∠BOC supplementary as
  Exercise 14 asks. `scan02.md` p7 independently reads it as "straight angle
  A-O-C, ray OB", which agrees.
- **Fig 1-6.** My first draft drew the "obtuse" angle at 47°; the constraint
  check caught it and it is now 133°. Worth a look that the new layout still
  matches the book's.
- **Fig 1-17.** Three pairs, and the *point* of the exercise is that none are
  adjacent: (a) two distinct nearby vertices, (b) shared vertex and side but
  overlapping interiors, (c) shared vertex only. Read off a 200 dpi crop of
  `scan02` p9; the two vertices in (a) are ~1.5 mm apart in the original and I
  may have exaggerated the gap slightly.
- **Fig 1-7.** Right angle is at the lower-left vertex with the `90°` label
  inside. I set the degree mark as `\textdegree` rather than `$^\circ$` so the
  collision checker reads it as one token.
- **Fig 1-13.** Primes are kerned (`A\mkern2mu'`) to keep the checker from
  reading letter and prime as two colliding labels. Very slightly wider than the
  book's spacing.

## 3. Text

Transcribed from the photo PDF (pages 15–34 = book pp. 1–20), cross-checked
against `scan01` p16–p24 and `scan02` p1–p15 where the photo edge was cut.

- **All exercise numbers checked against source**: Discussion Topics 1–7;
  Ex. Group 1-1 (1–4); 1-2 (1–6); 1-3 (1–24); 1-4 (1–17); Review items 1–2 with
  constructions (a)–(g); Brief Review Tests I.1–7, II.1–8; Arithmetic and
  Algebra Refresher 1(a)–(p), 2(a)–(g), 3(a)–(g), 4(a)–(j), 5, 6(a)–(e).
- **No starred (\*) exercises occur in Chapter 1**, so `\starnote` is not used
  here. The `*` marks in the running text are ordinary footnotes.
- Footnotes are reset per page to match the book's `*` / `†` sequence
  (p.1 Spinoza; p.2 philosophy; p.5 Plato/Aristotle + Alexandria; p.6 calculus;
  p.11 Euclid on measurement).

### Text items I am not fully certain of
- **p.18, II.2** reads "A line may have finite length." — the photo is slightly
  soft on "may"; `scan02` p15 is blurry for this page. Low risk, worth a glance.
- **p.18, Refresher 1(e)** I read as `1/3 ÷ 11/3`. The `11/3` is cramped in the
  photo and could conceivably be `1 1/3`. Please confirm — it changes the answer.
- **p.18, Refresher 1(n)** `2.5679/0.1372` — digits are small; re-check.
- **p.13, Ex. 17(c)** `121° 18' 17"` — the `121` is at the line edge; the
  adjacent PDF page confirms it, but flagging.
- **p.5 footnote †** and **p.6 calculus footnote** run into the gutter on their
  photo pages; I read them from `scan01` p21/p22.
- Section heads are set in the book's small-caps display style; I used the
  house `\section*{1--N\quad TITLE}` form per the conventions.

## 4. Not attempted
- The running heads in the book alternate (`INTRODUCTION` verso / section title
  recto). I set `\markboth{INTRODUCTION}{}` per house style, and switched it to
  `REVIEW OF CHAPTER 1` at the review section, matching the printed page.

---

# Text review (fresh agent, adversarial pass)

Scope: `chapters/ch01.tex` diffed line by line against `sources/Geometry.pdf`
PDF pp. 15–34 (book pp. 1–20), plus the plate leaf at PDF p.14 and the
copyright page at PDF p.6. Every exercise number, every angle value, every
figure cross-reference, all six section heads, all seven `\addcontentsline`
lines, and all five footnotes were checked. Ambiguous readings were re-rendered
at 400 dpi and re-read rather than guessed.

## Fixes applied (2)

1. **Hilbert plate caption was wrong and truncated.** The tex credited
   *Scripta Mathematica* and gave only the name and dates. The plate facing
   book p.1 credits the **New York Public Library**, and carries three lines the
   transcription had dropped (the Göttingen professorship and the
   "foremost mathematician" line). Re-read at 400 dpi from PDF p.14 and
   transcribed in full. The other three plates' credits were correct.

2. **Aristotle plate was emitted twice.** `ch02.tex` already emits it
   immediately before `\chapter*{LOGIC}` — correctly, since it is the
   facing-page plate for the Chapter 2 opener. `ch01.tex` emitted it again at
   end of file, so the assembled book would have printed it twice. Removed from
   ch01 and replaced with a comment recording that ch02 owns it. This closes the
   builder's open "Aristotle plate ownership" question.

Recompiled twice after the edits: clean (spacing warnings only, no errors),
29 pages. Both changed pages were rasterised and inspected.

## Builder uncertainties I closed (no change needed)

- **Refresher 1(e)** is `1/3 ÷ 11/3` — at 400 dpi the `11/3` is unmistakably a
  stacked fraction, not a mixed number `1 1/3`. The tex was already right.
- **Refresher 1(n)** `2.5679/0.1372` — confirmed digit by digit.
- **p.18, II.2** "A line may have finite length." — confirmed.
- **p.13, Ex. 17(c)** `121° 18' 17"` — confirmed, `121` is intact.
- **Hilbert caption** — now read directly from the source rather than from the
  scan index; see fix 1.

## Verified correct (spot-checks that passed)

- All 78 numeric values in Ex. 1-3 #17–#24 (degree/minute/second triples,
  complements, supplements) match the source exactly.
- Refresher 1(a)–(p), 2(a)–(g), 3(a)–(g), 4(a)–(j), 6(a)–(e): all match.
- Exercise-group boundaries and the `\setcounter{exlisti}` restarts are right:
  Ex. 1-3 runs 1–24 across four `multicols` blocks (6/12/16 restarts) and
  Ex. 1-4 runs 1–17 across five (3/7/12/14 restarts). No number is skipped or
  repeated.
- Review of Chapter 1: the 26-term vocabulary table matches the source's
  two-column order exactly; constructions (a)–(g) match; Brief Review Tests
  I.1–7 and II.1–8 match.
- **No starred (`*`) exercises or sections exist in Chapter 1**, so `\starnote`
  is correctly absent. The `*`/`†` marks in running text are ordinary footnotes
  and their per-page reset sequence matches the book.
- No Greek letters occur in Chapter 1 except `π` in Refresher 6(c)–(d); both
  correct. All angle/perpendicular/parallel symbols (`\ang`, `\perp`, `\pll`)
  match the book's usage.
- Definitions: the chapter's single definition auto-numbers to **1-1**, matching
  the printed "Definition 1-1." There are no theorems in Chapter 1.
- Paragraph-by-paragraph read of §§1-1 through 1-6: no dropped, merged, or
  paraphrased sentences found. Wording is the book's throughout.

## Residual doubts

- **Source typo preserved as normalised.** Book p.16, Ex. 15 prints
  "in Fig 1-26" without the period after "Fig"; every other reference in the
  chapter uses "Fig.". The tex normalises to `Fig.~1--26`. Flagging in case the
  project wants source typos preserved verbatim — I judged this a compositor
  slip, not authorial.
- **Plate macro divergence (cosmetic, for the integration agent).** ch01's
  `\Iplate` frames the box *and* the caption together; ch02's `\IIplate` frames
  only the box and sets the caption beneath it. Both render fine standalone but
  will look inconsistent side by side once the macros are hoisted into a shared
  preamble. Pick one shape at integration. I did not change it — it is layout,
  not text.
- **Running heads.** The book alternates `INTRODUCTION` (verso) with the current
  section title (recto). `\markboth{INTRODUCTION}{}` leaves rectos blank. This
  matches what ch02 does, so it is a book-wide convention decision, not a ch01
  defect — but it is a real departure from the printed page.
- **"CHAPTER 1" dropped from the opener.** The printed page sets "CHAPTER 1"
  above the title. ch01 and ch02 both omit it. Same book-wide decision.

## On the section-0 blocker

I checked both records directly, and **they do not contradict each other — they
are two different physical copies.**

- `sources/Geometry.pdf` p.6 (the teacher's photo copy): © 1960 Addison-Wesley,
  LCCN 60-8336, **Second printing, February, 1961**.
- `scans/scan01.pdf` p.5 (Caleb's copy): © 1960 Addison-Wesley, LCCN 60-8336,
  **Fourth printing, June 1964**.

Same copyright year, same LCCN, same edition. A fourth printing is a later
*printing*, not a later *edition*, and does not create or extend a term.
`scan01.md` was accurate; PAGEMAP and STATUS were accurate; the builder's
part (a) is resolved — **the standing stop-condition in CLAUDE.md is satisfied.**

**Part (b) is not resolved and I could not resolve it.** The builder's point
stands and is the load-bearing one: for a work whose copyright dates from 1960,
the US renewal had to be filed in the 28th year, i.e. registrations appearing in
**1987–1988**. A search window of 1988–91 begins at or after the end of the
period where a renewal for this book would appear, so a valid 1987 renewal
would not have been seen. The positive control validates the method, not the
window. This is a genuine gap on exactly the years that decide the question, and
it is outside a text reviewer's remit to close. It needs a renewal search over
**1987–1989** filings, by title and with Addison-Wesley as claimant, before the
remaining units are fanned out.

---

## Figure review

Fresh figure-review pass over `chapters/figures01.tex` (19 macro blocks, Figs
1-1 … 1-28) against the photo PDF pages 15–34. Gates at the end of this pass:
`verify_figures.py 01` → **109/109**, `check_labels.py … 01` → **0 COLLIDE**
(3 TIGHT, all 0.95 pt, all label-vs-vertex-dot — accepted, see below), ch01
compiles twice clean under tectonic, every figure page rasterised and read.

### 0. The section-0 blocker applies to the figures too — arguably harder

The clearance gap the text reviewer documented above is not a text-only
problem. Every figure in this chapter was **measured off the book's own
drawings** (vertex ratios, arc radii, label placements read from the page
photographs) and redrawn to match. That is a closer derivative relationship
than the prose has, not a looser one. If the renewal search over **1987–1989**
comes back positive, the figure work in this repo is as exposed as the text,
and this pass should not be read as a green light to fan the remaining units
out. Flagging, not deciding — the search is Caleb's call.

### 1. Structural errors found and fixed (13)

These were wrong against the source, not merely tight:

1. **Fig 1-2, tetrahedron** — was drawn with a hidden back *vertex* (three
   dashed edges). The book draws the near vertex in front and hides only the
   back base *edge*. Redrawn to the book's orientation.
2. **Fig 1-2, prism** — was a far-vertex prism with a "roof"-like top and was
   ~27 % too tall. The book draws an upright prism with the near vertical edge
   facing the reader, the top face fully visible, and only the back bottom edge
   dashed. Redrawn from measured ratios (width : depth : height = 475 : 168 : 515).
3. **Fig 1-3, damped zigzag** — the path opened with `--` and no starting
   coordinate, emitting a PDF lineto with no current point. `pdftoppm` threw 17
   syntax errors and dropped the zigzag. Fixed by opening the path with `(0,0.42)`.
4. **Fig 1-21** — the drawn arc about *P* spanned 230°–310°, but the crossings
   with *l* are at 227.95° and 312.05°, so **the arc never actually reached the
   line it is supposed to cut**. Widened to 222°–318°. `verify_figures` could
   not see this (it checked the circle, not the drawn sweep), so a new
   `sweep_covers` check now guards every construction arc in the chapter.
5. **Fig 1-26** — angles 1 and 2 were both placed below-right of their
   crossings, i.e. as *corresponding* angles. The book marks the **alternate
   interior** pair (1 below *l* and right of *n*, 2 above *m* and left of *n*).
   Re-placed; the constraint now encodes the alternate-interior equality.
6. **Fig 1-27** — same error: 2 is the lower-left angle at *Q* and 1 the
   upper-right angle at *P* in the book. Re-placed, constraint updated. The
   dashed copied parallel was also over-long to the right (1 : 2.6 vs the
   book's 1 : 1.85).
7. **Fig 1-24(a)** — was a mirror image of the book: apex at 0.61 of the base
   instead of 0.34, and the right-angle box on the wrong side of the altitude.
8. **Fig 1-24(b)** — height was 0.83 of the base against the book's 1.42, and
   the overhang past *B* was 0.38 against 0.63.
9. **Fig 1-24(c)** — was 0.79 of the base high with the apex at 0.46; the book
   is a tall near-isosceles, 1.02 high with the apex at 0.584.
10. **Fig 1-25** — apex at 0.66 of the base and height 0.58; measured off the
    book as 0.775 and 0.667. Triangle and incentre recomputed.
11. **Fig 1-11** — the quadrilateral was a thin sliver with two vertices almost
    coincident. Redrawn from the book's own four vertex ratios.
12. **Fig 1-15** — carried two construction arcs about *X* and *Y* that the
    book does not draw (it shows the single arc across both rays and the ×
    where the crossing falls). Removed; arc radius and the crossing distance
    re-measured (0.335 and 0.60 of the ray length).
13. **Fig 1-23** — the finger was drawn with a rounded tip pointing *down* and
    stopped 0.47 cm short of the fist, so the hand read as two detached blobs.
    The fingertip now rounds upward at the centroid and the finger meets the
    knuckle line.

### 2. Smaller corrections (6)

- Fig 1-13: angle was 52°, the book's is 60°; the tick was on the arc's
  midpoint instead of on the two ray crossings (book: a tick on *OB*, a cross
  on *OA*). Also the constraint file had the second vertex at x = 2.05 while
  the figure had 2.75 — a latent mirror error, now aligned.
- Fig 1-12: added the compass-point marks the book draws at the two base
  vertices.
- Fig 1-5: *AC* was 15 % shorter than *AB*; the book draws all three rays at
  essentially equal length.
- Fig 1-19/1-20: enlarged 1.4× (the pair was small enough that the *C* label
  could not clear the vesica) and the arcs now run visibly past their
  crossings, as the book draws them; added the ticks where the arcs cut *AB*.
- Fig 1-2: the "Circular cylinder" caption sat on top of the prism below it.
- Fig 1-17: labels *A* and *B* in panels (a) and (c) were grazing the rays.

### 3. Constraint coverage: 50 → 109

The old file encoded nothing at all for Figs 1-1, 1-2, 1-3, 1-4, 1-11 and 1-18,
although each states hypotheses. Added: the named shapes of Fig 1-1 (square
equilateral, both pairs of parallelogram sides parallel, trapezoid with exactly
one parallel pair, rectangle not a square, triangle non-degenerate); the solids
of Fig 1-2 (cube face square, 45° depth offset, cylinder sides parallel and
ends coaxial, sphere equator concentric, cone apex over the base centre, prism
lateral edges vertical and equal, tetrahedron faces non-degenerate); the
repeated halving of the square in Fig 1-3 and the face's bilateral symmetry;
"Interior"/"Exterior" on the correct sides of the angle in Fig 1-4; general
position of the Fig 1-11 vertices; **Fig 1-18's copied segment equals the given
segment** (the whole point of the exercise, previously unchecked); the
transferred compass radius in Fig 1-13; midpoints of all three medians in
1-22; the altitude foot lying inside the base in 1-24(a); *a*² + *b*² = *c*² in
1-28; label-inside-its-own-angle for 1-17, 1-26, 1-27; and `sweep_covers` guards
that every drawn arc actually reaches the crossing it is drawn for.

### 4. Residual doubts

- **Fig 1-24(c) and 1-25, the "O" label.** The book prints *O* just below-left
  of the ×, close enough that it grazes a dashed altitude/bisector — the book
  gets away with it on hand-drawn hairlines, we do not (`check_labels`
  registers a hard collision). *O* sits on the widest free sector instead:
  directly left of the × in 1-24(c) and below-left at a larger offset in 1-25.
  Same reading, slightly airier placement. Ask Caleb if he wants the book's
  exact crowding reproduced.
- **3 TIGHT at 0.95 pt** (Fig 1-8 "A"; Fig 1-9 "A", "B"). All are a label
  `above` a filled vertex dot. True clearance is ~2.2 pt; the 0.95 pt figure is
  `pdfplumber` reporting the font's full em box rather than the glyph. Checked
  in the render — visually clean. Accepted.
- **`check_labels` approximates arcs by chords** between the on-curve nodes it
  can see, so a wide arc casts a "chord shadow" well inside its true path. Two
  of this chapter's label placements were driven by that artefact rather than
  by real ink (Fig 1-19 *C*, Fig 1-20 *O*). Worth fixing in the tool before ch
  9/11/12/14, which have far more arcs.
- **Fig 1-3 is organic and only approximated.** The zigzag's decay rate, the
  number of ellipses in the converging chain, and the face's proportions are
  eyeballed from the photo page, not measured. Book page 9 is legible but the
  figure is small; a scan crop would settle it.
- **Fig 1-23 is a pictorial halftone-style line drawing.** The triangle and its
  medians are exact; the hand is a stylisation and does not match the book's
  drawing in detail (knuckles, thumb, cuff). It reads correctly but it is not
  a faithful copy.
- **Fig 1-14 (compass designs) was verified against the photo page only.**
  Both patterns are structurally right (four circles through one common point;
  six-petal rosette inscribed in a circle of the same radius), but I did not
  locate a scan crop to confirm line weights.
- Figs 1-6, 1-16, 1-17 angles are within a few degrees of the book but were
  read off a photographed page with visible page curvature; treat the exact
  degree values as approximate.
