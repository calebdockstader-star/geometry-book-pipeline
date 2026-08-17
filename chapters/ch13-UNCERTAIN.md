# ch13 — UNCERTAIN

Unit: Chapter 13 "Loci and Sets", book pp. 227–235 (PDF 241–249).
Status: **BUILT.** `chapters/ch13.tex`, `chapters/figures13.tex`,
`tools/constraints/ch13.py`, `build/ch13.pdf` (15 pp).

Gates: compiles twice, no errors · constraints **82/82** · collisions **0**
(3 TIGHT, inspected and accepted — see below) · visual pass done on all 15
rendered pages · exercise numbers and in-text numerals diffed against source.

This file **replaces** the previous agent's scoping notes, which were written
before any transcription existed. Two of its figure findings were checked and
are resolved below (Fig 13-12; the p.227 star footnote); one is confirmed and
still stands (the scan-coverage gap).

---

## Rights — settled before work began, not re-litigated

I re-verified the on-disk finding (`sources/copyright/renewal-search.md`)
directly against the data rather than taking it on trust, because the previous
agent had halted here. Independently reproduced from
`sources/copyright/nypl-data/`:

- `grep -i brumfiel|eicholz` across **all six** files 1986–1991 → exactly one
  hit, *Principles of Arithmetic* (orig. 1963, RE552863, renewed 1991). Not
  this book. That record names all three authors, so it proves these authors'
  filings do surface in this dataset.
- `shanks` ∩ `geometr` → zero hits.
- Positive control holds: Thomas, *Calculus and Analytic Geometry*,
  Addison-Wesley, orig. **1960**-03-18 → **RE396444, renewed 1988-09-30**.
  Same publisher, same year, same genre, present in the data.
- Window density: 21,594 records touching 1960 in the 1988 file alone.

The previous agent's specific objection was that 1987 had never been searched.
It has been — `1987-from-db.tsv` is present and included. 1909 Act, 28-year
first term for a 1960 work, §305 runs it to Dec 31 1988, renewal
non-automatic pre-1964, post-1977 USCO records complete in electronic form.
Null across 1986–91 is dispositive. **US public domain since Jan 1, 1989.**
No further action needed; this is not an open question for later units.

---

## Text — things I could not nail with certainty

1. **p. 231, Definition 13-2, "the union … is the set of all points of $S_1$
   and $S_2$".** Transcribed verbatim. Note this is the book's own loose
   phrasing (it reads as if it meant "in $S_1$ **or** $S_2$"), and it contrasts
   with the next sentence, which italicises *intersection* but leaves "union"
   roman. I reproduced both the wording and the asymmetric italics exactly as
   printed rather than tidying them. Worth a second reader's eye.

2. **p. 233, Theorem 13-7 outline, the three parallelogram names.** Read at
   320 dpi as **$AC'BC$, $ABCB'$, $ABA'C$**. `AC'BC` looks like a typo (C
   appears twice) but is legitimate — $C'$ and $C$ are distinct points, so the
   four vertices are $A, C', B, C$. I am confident of the glyphs; I am less
   confident the book itself is not mis-set here, since the natural companion
   names would be $AC'BC$, $ABCB'$, $ABA'C$ in some consistent cyclic order and
   these three are not consistently ordered. Transcribed as printed.

3. **p. 235, Review Exercise 3.** The three relations are
   $\overline{AX}+\overline{XB}=\overline{AB}$,
   $\overline{AX}-\overline{XB}=\overline{AB}$,
   $\overline{BX}-\overline{XA}=\overline{AB}$. The overbars in the second and
   third are partly lost in the gutter shadow on PDF 249; I read them as
   present (consistent with the first) and set them so. p. 235 has no scan.

4. **Star footnote convention.** The `*` on *locus* (p. 227) is a glossary
   footnote about the Latin word, **not** the starred-exercise convention, so
   `\starnote` would have been wrong. Confirmed by reading the footnote itself.
   It uses a local unnumbered-footnote macro `\XIIIlocusnote`, matching ch02's
   `\IIstarnote` / ch09's `\IXstarnote` pattern. The starred **exercises** in
   this chapter (13-2 #4, #7, #9; 13-5 #3, #19, #20) carry no footnote on these
   pages — the convention was established earlier in the book — so none is
   emitted here. Verify that an earlier unit does emit it.

Everything else in the chapter was legible at 320 dpi and is transcribed with
confidence, including all 47 exercises, both definitions, all seven theorems,
and the Review section.

### Checked and found correct (no action)

- Exercise counts: 13-1 → 5, 13-2 → 9, 13-3 → 5, 13-4 → 4, 13-5 → 20,
  Review → 4. Starred: 13-2 #4/#7/#9, 13-5 #3/#19/#20. All match the source.
- Numerals: $PP_0=4$; distance 1 from a 3-unit segment; four units / unit
  square / 12 units / eight units; radius five, distance two; base four, area
  four, area $A$; barn $30\times50$ ft, rope 60 ft; $50^\circ$; $R/4$ in $R$;
  $xR$ with $x=\frac12,\frac13$. All verified against the page images.
- "Review Exercises" is its own centred bold heading in the book, with no
  "Exercise"/"Exercise Group" prefix — `\exercise{}` prepends "Exercise", so a
  plain centred heading is used instead.

---

## Figures — 17 drawn, and how far each is trusted

Scan coverage (confirmed against `sources/scan-index/`):
**covered** — scan14 p22–p24 = book pp. 227–229 → Figs 13-1 … 13-6;
scan15 p1–p2 = book p. 233 → Figs 13-15, 13-16.
**not covered** — book pp. 230–232, 234–235 → **Figs 13-7 … 13-14 and 13-17**,
i.e. 9 of 17. Those nine were built from the 320-dpi photo PDF only. Under the
source policy they are **provisional**, the same debt ch09 carries. This is a
real finding and it stands independently of anything else here.

That said, every figure in this chapter is small — no figure exceeds 5 lines
and 5 labels except 13-15 and 13-16, both of which **are** scan-covered — so
the exposure from the gap is much lower than ch09's.

### Resolved (previous agent flagged these; both are now settled from source)

- **Fig 13-12 is the CIRCUMCENTER, not a second incenter.** The previous
  reviewer warned a builder might draw it as an incenter by page adjacency. At
  320 dpi the dashed lines plainly leave the **midpoints of the sides**, not
  the vertices, and $O$ falls **outside** the triangle above $AC$ — which is
  exactly what an obtuse angle at $B$ forces. It matches Theorem 13-5's own
  reference. Drawn as the circumcenter, with $O$ built as the intersection of
  two perpendicular bisectors and $|OA|=|OB|=|OC|$ asserted numerically.
- **Figs 13-9 and 13-10 are not "all line geometry"** (previous agent's
  inventory said they were). 13-9 is the rolling-wheel/cycloid sketch, 13-10
  the hypocycloid setup. Both drawn as circles with the tangency and
  equal-radius conditions enforced.

### Judgement calls I made, each of which a reviewer may want to overturn

1. **Fig 13-8 is drawn to a true $50^\circ$, and therefore does not match the
   printed figure's proportions.** Exercise 13-2 #4 states $\angle APB = 50°$.
   The printed $P$ sits much shallower than $50°$ permits — with $|AB|$ as
   drawn, a $50°$ arc cannot come nearer the chord than about $0.23\,|AB|$,
   and the book's $P$ is nearer than that. Project policy says the drawing must
   satisfy the stated hypothesis exactly, so $P$ is placed on the true $50°$
   arc and sits noticeably deeper below $AB$ than in the book. **Flagging
   explicitly because it is a deliberate, visible departure from the source
   image.** Reverse it if fidelity to the printed picture outranks fidelity to
   the stated angle.

2. **Fig 13-17 I reproduced without being able to rationalise it.** Ex 13-5 *3
   is an SSA construction ("two sides and an angle other than the included
   angle"). The page shows: $C$ upper-left with two rays, one running down to
   $A$ and one running free to the right; $A$–$B$ to the right; a **single**
   tick on $CA$, a **triple** tick on a short segment drawn across from the
   free ray to $CA$, and a **double** tick on $AB$. I could not work out what
   the triple-ticked cross-segment is meant to denote — it is not obviously a
   side, an altitude, or a given length. I drew what is printed rather than
   inventing a tidier figure. **p. 234 has no scan**, so I could not check it.
   This is the figure in the chapter I am least confident about.

3. **Fig 13-15: labels $G$, $F$, $O$ moved off the book's positions.** $G$ and
   $F$ sit in ~20°-wide wedges between a median and side $AC$; at this trim
   there is not room for a label inside the wedge at the book's offset, so both
   labels sit further out along the wedge bisector than the book places them.
   $O$'s label is **below** the crossing, not above as in the book, because
   segment $DE$ passes just above $O$. All three are the TIGHT entries in the
   collision audit (0.68 / 0.40 / 1.14 pt); I looked at the rendered page and
   each reads unambiguously against its own dot. Accepted, not fixed.

4. **Fig 13-16: label $B$ moved from above-left to above-right.** Above-left is
   crossed by the altitude $A$–$O$. Same reasoning; visually checked.

5. **Fig 13-3 dot positions are approximate.** The five locus dots and the
   radial dot are a partial sketch in the book; their *spacing* is eyeballed
   from the scan, though every dot is placed at exactly distance 1 from the
   segment (enforced numerically), and the segment is exactly 3 units with unit
   ticks. The radial dot's 72° bearing off the right endpoint is measured from
   the scan, not stated anywhere in the text.

6. **Fig 13-9's offset between the two wheel positions** (0.42 of a radius) is
   measured off the photo, not stated. Equal radii, level centres and $P$ on
   the rim are enforced; the roll distance is not, because the book does not
   state one.

7. **Fig 13-4's base is labelled 4 but drawn 3.0 units wide.** Only one length
   appears in the figure, so there is no ratio to preserve; the label is the
   book's.

### Caught during the build (recording so a reviewer knows it was a real bug)

- Fig 13-14's $C$ was initially placed by rotating $O$ about $B$ by $-90°$,
  which put $C$ **above** $B$; the book has it below-right. Caught by the
  collision audit (the label was landing on segment $BC$) and fixed to $+90°$.
  Perpendicularity held either way, so the constraint check alone would not
  have caught it — the collision audit and the eyeball did.

---

## Questions for Caleb

1. **Figs 13-7 … 13-14 and 13-17 have no scan coverage** (book pp. 230–232,
   234–235). Accept them as photo-only provisional, ch09-style, or re-shoot
   those four pages? Given how simple most of them are, I'd accept them —
   except **13-17**, which I genuinely could not read (see judgement call 2)
   and which a re-shoot would settle.
2. **Fig 13-8**: I drew the true $50°$, which visibly departs from the printed
   figure. Keep the mathematics or keep the picture?
3. **p. 231 Definition 13-2** reads "the set of all points of $S_1$ and $S_2$"
   for the *union*. Transcribe as-is (what I did), or is this a known
   typo you want silently corrected?

---

## Text review

Fresh adversarial pass, 2026-08-17. Diffed `chapters/ch13.tex` line by line
against PDF 241–249 (book pp. 227–235) rasterised at 320 dpi, with targeted
5x crops wherever a bar, subscript or congruence glyph carried meaning.
Recompiled twice, clean, 15 pp.

### Fixes applied (2)

1. **p. 235, Review Exercise 3 — spurious overbar (substantive).** The tex set
   the right-hand side of the first relation as `\sg{AB}`. The book prints it
   **without** the bar, while the two relations that follow it *do* carry one.
   Checked at 5x: the token opens its line, so nothing is clipped by the
   gutter or the line break. Reproduced as printed and commented in the tex.
   This narrows the builder's doubt #3, which had guessed the other way: the
   two *later* bars are real and correctly set; the *first* one was the error.
   **This is almost certainly a compositor's slip in the 1960 setting** — the
   surrounding convention makes an unbarred right-hand side inconsistent — so
   it belongs on the same question list as Definition 13-2's loose wording.
   Flag for Caleb rather than silently normalising either way.

2. **p. 227, "Examples:" — paragraph indent.** Was forced flush-left with
   `\noindent`; the book indents it as an ordinary paragraph. Removed. (The
   `\noindent\emph{Proof sketch.}` / `\noindent\emph{Outline of proof.}`
   instances were *left alone* — that is established house style across ch02,
   ch04, ch05, ch07 and ch10, and the label paragraphs are set the same way.)

### Checked and confirmed correct (no action)

- **Every numeral in every exercise**, re-read independently of the builder's
  list: 13-1 #1–#5, 13-2 #1–#9, 13-3 #1–#5, 13-4 #1–#4, 13-5 #1–#20,
  Review #1–#4. All data values, all embedded quantities, all figure
  cross-references. No discrepancy.
- **Exercise-group boundaries and numbering.** Five groups plus Review; counts
  5 / 9 / 5 / 4 / 20 / 4 = 47. Group headings land on the correct pages and no
  item drifted across a spread boundary (the 230/231 and 232/233 spreads are
  the tempting ones; both verified).
- **Starred exercises.** 13-2 #4, #7, #9 and 13-5 #3, #19, #20 — exactly six,
  matching the printed stars. No star anywhere else in the unit.
- **`\starnote` correctly absent.** Re-derived from the page rather than from
  the builder's note: the `*` on *locus* (p. 227) is glossed at the foot of
  that page as a note about the Latin word, so it is not the starred-exercise
  convention. That convention fires earlier in the book (ch03/ch07/ch08 all
  emit it). Omission here is right.
- **Theorem and definition numbering** renders 13-1 … 13-7 and 13-1 / 13-2 in
  the compiled PDF, matching the book.
- **Math and glyphs.** The asymmetric triangle namings in Theorem 13-1's proof
  (`PAC`/`PBC` in part (1) vs `PCA`/`PCB` in part (2)) are the book's own and
  are preserved. `=` vs `\cong` distinctions verified individually at the four
  places they differ, including the `\sg{PA} = \sg{PB}` at the top of p. 230.
  Theorem 13-7's three parallelogram names re-read at 5x and confirmed as the
  builder set them; the primes are all correctly placed. No Greek in the unit.
- **No paraphrase.** Every paragraph opening on all nine pages was matched to
  the source, and both definitions, all seven theorems, all four proof
  sketches/outlines and the whole Review section were read verbatim end to
  end. Nothing dropped, nothing summarised, nothing invented.
- **`\addcontentsline`** present after `\chapter*` and after all four
  `\section*` (13-1, 13-2, 13-3, Review).

### Residual doubts

1. **Review Exercise 3's missing overbar (fix 1 above)** — transcribed as
   printed, but it reads as a source typo. Needs a call from Caleb, same
   decision as the Definition 13-2 wording already on the list.
2. The builder's doubts **#1 (Definition 13-2 wording and its asymmetric
   italics)** and **#2 (Theorem 13-7 parallelogram names)** were both
   re-checked against the page and are transcribed correctly. They remain open
   as *editorial* questions about the book's own text, not as transcription
   errors.
3. Nothing else. No text-level uncertainty remains in this unit.

**Note on scope:** this was a text review only. Figure geometry was not
touched, so the builder's figure debts above — the nine photo-only figures,
Fig 13-8's true-50° departure, and the unresolved Fig 13-17 — all stand
unchanged and still need the figure-review pass.

**Note on rights:** I did not independently re-verify the copyright research
and am not the basis for that finding; I proceeded on the project's documented
determination in `sources/copyright/renewal-search.md`.

---

## Figure review

Fresh figure-review pass (did not draw these). Sources used: the 320-dpi photo
PDF pages 241–249, plus `scans/scan14.pdf` p.21–24 (book pp. 226–229) and
`scans/scan15.pdf` p.2 (book p.233) for the scan-covered figures. Every figure
block was measured against the source image (crop + pixel measurement of
vertex ratios), and every figure page of the render was inspected.

**Gates:** compiles twice clean · constraints **102/102** (was 82/82; 20 added)
· collisions **0** (3 TIGHT, all inspected and accepted) · visual pass done.

### Corrections applied (10 figures touched)

1. **Fig 13-8 — the builder's judgement call #1 above is withdrawn.** Measured
   on a 3× crop of the printed figure, the drawn $\angle APB$ is $50.1^\circ$:
   the book's own figure *does* satisfy the stated angle, and there was never a
   conflict between the hypothesis and the picture. The earlier claim (that a
   $50^\circ$ arc could not reach the printed $P$) came from reading vertex
   positions off the whole page instead of a crop. What was actually wrong was
   the *slope*: $AB$ was drawn at $13.9^\circ$ where the book has $29^\circ$,
   and the dashed line was cut short. $A$ kept, $B$ rebuilt at $29^\circ$, and
   $P$ re-derived on the exact $50^\circ$ arc at the printed relative position
   ($0.062\,|AB|$ along, $0.903\,|AB|$ below). The dashed line now overruns by
   $0.68\,|AB|$ past $A$ and $1.00\,|AB|$ past $B$, as printed.
2. **Fig 13-16 — two missing arrowheads.** `scan15` p.2 shows arrowheads at
   $O$ (top of the altitude through $B$) and at $C$, besides the one at $A$
   that was already drawn. Both added; the figure now carries the same five
   arrowheads as the book ($O$, $A$, $C$, $C'$, $A'$).
3. **Fig 13-12 — the perpendicular bisector of $AC$ was drawn as a stub.** The
   book draws it as one continuous line: it overshoots $O$ to the upper left,
   then runs down through $M_{AC}$ into the triangle and dies on $AB$ near $B$.
   Now drawn that way, with the lower end derived as an intersection.
4. **Fig 13-14 — bisector extent.** The dashed perpendicular bisector of $AB$
   was a symmetric stub; the book runs it from a short overshoot above $O$ down
   past the chord to the foot of the circle. Redrawn asymmetric to match.
5. **Fig 13-4 — apex position.** $V$ was at $0.62$ of the base with height
   $0.43\,b$; measured off the print it is $0.741$ along and $0.463\,b$ up.
   Moved.
6. **Fig 13-17 — free ray and cross-segment.** The second ray from $C$ was too
   shallow ($8^\circ$ vs the printed $14^\circ$) and ran too far right; the
   triple-ticked cross-segment met $CA$ at $0.66$ instead of $\approx0.85$.
   Both corrected, which also makes the cross-segment very nearly perpendicular
   to the free ray, as it is in the book. The single tick on $CA$ moved
   $0.40\to0.47$.
7. **Fig 13-3 — dot row.** Spacing tightened to the printed $0.19$ unit and the
   row re-centred so the measuring arrow lands on the *fourth* dot (three left,
   one right), as drawn.
8. **Fig 13-5 — bisector overshoot** above $P$ raised from $0.06\,|AB|$ to
   $0.15\,|AB|$, matching the print.
9. **Fig 13-11 — label $O$** moved from directly above the saltire to the left
   of it ($160^\circ$), where the book puts it. Collision-checked: $150^\circ$
   and $135^\circ$ both collide with the bisector from $A$; $160^\circ$ is
   clear.
10. **Constraints strengthened.** Two vacuous entries in Fig 13-17 (each of the
    form "the distance from a point to a line through itself is 0", true by
    construction) were removed and replaced with real ones. Added: midpoints in
    13-12; $C,D$ on their sides and the equal-ratio condition in 13-13; the
    exercise's own hypothesis that $\angle ABC$ is neither right nor straight,
    plus $Q$'s side, in 13-14; the excluded endpoints $A,B$ in 13-7;
    non-degeneracy in 13-4 and 13-8; and, in 13-17, that the three tick groups
    mark three *different* lengths and that the free ray dies short of $AB$.

### Confirmed correct against the source (no change needed)

Figs 13-1, 13-2, 13-6, 13-7, 13-9, 13-10, 13-13, 13-15 — line weights
(solid = given, dashed = locus/auxiliary), label sides, tick counts, dot
marks, arc directions and vertex ratios all match. Spot values: 13-7's $P$ at
$118^\circ$ vs $119.5^\circ$ measured; 13-10's small circle at $R/4$ and
$-32^\circ$ vs $-27.8^\circ$; 13-9's wheel offset $0.43R$ measured, drawn
$0.43R$; 13-13's $C,D$ at $0.4785$ vs $0.49$ measured; 13-11's vertex ratios
within 5% of the print. Fig 13-6's angle is drawn symmetric about a horizontal
bisector where the book tilts the whole figure $5^\circ$; the aperture
($2\times18^\circ$) is the printed one, so this is a rotation only.

### Residual doubts

1. **Scan coverage is still partial, but the gap is smaller than recorded
   above.** `scan14` p.21–24 covers book pp. 226–229 (Figs 13-1 … 13-6) and
   `scan15` p.2 covers p. 233 (Figs 13-15, 13-16) — so *both* figures that
   exceed the 5-line/5-label threshold are now scan-verified, 13-16 at high
   magnification. Figs 13-7 … 13-14 and 13-17 have no scan and were measured
   from the 320-dpi photo instead; all are small (≤5 lines, ≤4 labels), and
   each now has its printed proportions measured rather than eyeballed. I would
   call them verified-from-photo rather than provisional, but a scan of
   pp. 230–232 and 234 would close it properly.
2. **Fig 13-17's semantics remain unexplained** (builder's judgement call #2).
   I improved the fidelity of the drawing but still cannot say what the
   triple-ticked cross-segment denotes in the SSA construction. Reproduced as
   printed. Still the least-understood figure in the chapter.
3. **Fig 13-15's labels $G$, $F$ stay off the book's positions.** The book puts
   both directly under their dots; at this trim the wedge between the median
   and $AC$ is 0.365 drawing units and the label is 0.27 units tall, so a
   centred label leaves ~1 pt on each side. The existing offsets along the
   wedge (0.68 pt / 0.40 pt clearance, TIGHT) read cleanly in the render and
   were kept. Fixing this properly means enlarging the figure, which would
   break the side-by-side 13-15/13-16 pairing on the page.
4. **Fig 13-16's label $B$** (1.14 pt, TIGHT) sits just above the dashed
   $C'A'$ line that passes through $B$. Inspected at 400 dpi; unambiguous.
5. **Fig 13-6's plus mark at $P$** may be an artefact rather than a mark: in
   the print, the dashed bisector and the two dashed perpendiculars already
   cross at $P$ and could account for what looks like a drawn plus. Kept, as
   it is harmless either way.

**Note on rights:** I did not re-open the copyright question and am not a basis
for it; I proceeded on the project's documented determination in
`sources/copyright/renewal-search.md`.
