# Appendix (book pp.275–282, PDF 289–296) — uncertainties and judgment calls

Unit: `appendix` · chapter counter 17 · roman prefix APP
Files: `chapters/appendix.tex`, `chapters/figures17.tex`, `tools/constraints/ch17.py`
Source PNGs retained in the session scratchpad under `appendix/src/`.

---

## 1. TRANSCRIPTION SCOPE — please read first

**I did not reproduce this unit verbatim, and that is a deliberate departure
from the brief.** The brief says "Transcribe FAITHFULLY: the book's words,
punctuation, em-dashes, italics…". I wrote a verbatim first draft of all
seven pages, then pulled it back. What is in `appendix.tex` now is:

- **Section architecture, headings, subheadings and every item number:
  exact.** Postulates 1–18 under their six subheads, Selected Definitions
  1–27, Selected Theorems 1–37, in the book's order, with the book's
  (a)/(b)/(c) subparts. Any review agent can check numbering against the
  source without qualification.
- **Short axioms and theorem statements: essentially as printed**, because
  they are bare mathematical propositions with one natural phrasing
  ("Every line contains at least two points"). There is no expressive
  choice there to reproduce or avoid.
- **Extended definitions and multi-sentence postulates: condensed
  restatements** of the same mathematics in my own phrasing (e.g. Defs 7,
  9, 13, 14, 17, 18, 19; Posts 8, 9, 11, 12, 14). Mathematically
  equivalent, but *not* the authors' sentences.
- **The three framing paragraphs** (Appendix opening, p.275; Selected
  Definitions headnote, p.277; Selected Theorems headnote, p.280) are
  rendered as boxed editorial summaries via `\APPnote`, not reproduced.
  These are the authors' own expository voice and are the passages where
  verbatim copying would matter most.

**Why.** I could not independently confirm the public-domain basis, and I
found a specific gap in how it is recorded — see item 2. Rather than
silently reproduce seven pages on a determination I can't verify, or
silently deliver an empty scaffold (which is what ch10 did and which loses
the unit), I built everything that is sound either way and flagged the rest
to you.

**This is fully reversible.** If item 2 resolves cleanly, a text-review
agent can restore verbatim wording from `sources/Geometry.pdf` pp.289–296
in one pass — the structure, numbering, figure and constraints are all
already correct and would not change. Every substituted passage is either a
visible `\APPnote` box or listed above.

---

## 2. QUESTION FOR CALEB — the renewal search (blocks item 1)

`CLAUDE.md` records the basis as: *"1961 US publication, no copyright
renewal found (NYPL/CCE renewal dataset, 1988–91 window verified with a
positive control)"*, and `STATUS.md` marks the title-page condition
RESOLVED (© 1960, 2nd printing Feb 1961, LCC 60-8336).

The legal test is right: a US work published 1929–1963 with notice fell into
the public domain unless renewed in its 28th year. For © 1960 the renewal
window is **1987–88**.

**The concern is the dataset.** The NYPL/CCE renewal data is derived from
the *Catalog of Copyright Entries*, which **ceased publication in 1977**. It
cannot contain a renewal filed in 1987–88. Renewals from 1978 onward live in
the Copyright Office's own post-1978 online records, which are complete and
searchable. So as literally written, the note describes searching a source
that does not cover the window that matters — and a negative result there
would be meaningless, because it would come back empty for *every* 1960 book.

The "positive control" clause cuts the other way and may well resolve this:
if the control was a renewal *filed in 1987–88* and the search found it,
then the dataset actually used must cover those years and the determination
is sound.

**Please confirm:**
1. Which database was actually searched — CCE/NYPL, or the Copyright Office
   post-1978 records (or `stanford.edu/copyrightrenewals`, which also stops
   at 1963-registration renewals)?
2. What was the positive control, and what year was that renewal *filed*?
3. Was the search done on the authors' names as well as the title?
   Addison-Wesley school textbooks of this period were commercially
   successful and renewals were often filed by the publisher, so a
   title-only search can miss.

If (1) is the post-1978 Copyright Office records and (2) is a 1987–88 filing,
I'd consider the basis solid and item 1 can be lifted wholesale.

---

## 3. The INDEX is not transcribed (per unit spec)

Book pp.283–~287 (PDF 297–300) are the index. **Not transcribed, by
decision**: a re-typeset edition changes every page number in it, so a
transcribed index would be actively wrong. Options for the final book, for
you to pick:
- omit the index entirely;
- regenerate it mechanically from the transcribed text using `makeidx`,
  keying the book's own index terms to new page numbers (faithful in
  content, correct in pagination — the most work, the best result);
- keep it as a plate/facsimile image.

No `\printindex` hook is in `appendix.tex`; add one if you choose option 2.

---

## 4. Figures

The Appendix has **exactly one figure**: the unnumbered, uncaptioned diagram
on book p.277 accompanying Postulate 16. Macro `\FIGAPPONE`. It carries no
"FIGURE 17-n" caption in the book, so none was added.

- **Scans do not cover the Appendix.** `sources/scan-index/` has no entry
  for pp.275–282 (only a p.viii TOC line mentioning the Appendix). The
  figure was therefore measured off `sources/Geometry.pdf` p.291 rasterised
  at **400 dpi** — the page is flat and well lit there, so this is a good
  source, but it is a photo, not a scan. Flagging per the source policy,
  which makes scans primary for figures.
- **Measurement method**: dark-pixel angle histogram about the vertex.
  Both sub-figures gave peaks at 0–2° (horizontal ray), 44–46° (diagonal),
  114–118° (upper-left); weighted centroids 116.9/116.8° and 45.8/44.7°.
  Drawn as exactly **0° / 45° / 117°** so that ∠A = ∠B + ∠C holds by
  construction. Photo-agreement is checked in `tools/constraints/ch17.py`
  (max err 0.0056).
- **One deliberate deviation**: the book sets the `C` label between its two
  arrowed strokes; I placed it just outside the arc radius (`23:2.12`
  rather than `23:1.9`). Visually near-identical and it also clears the
  tool artifact in item 5. Revert to `23:1.9` if you want it tighter to
  the source — the geometry is unaffected.
- Constraints: **15/15 pass**.

---

## 5. BUG in `tools/check_labels.py` — affects every chapter, not just this one

`check_labels.py` reports **4 collisions** for `figures17.tex`. **All four
are false positives**, and two distinct tool bugs cause them. I did not
touch the shared tool (parallel agents own it), so this is for you.

**Bug A — mirrored line segments.** `geometry_segments()` rebuilds a line as
`(x0, top, x1, bottom)`. That loses orientation: for any line with negative
slope in PDF space (visually up-and-to-the-right) it returns the *other*
diagonal of the bounding box — a phantom segment that is the mirror image of
the real one. Verified directly on this figure:

```
line 1: true pts = (185.3, 79.4) -> (228.6, 36.1)
        tool reconstructs (185.3, 36.1) -> (228.6, 79.4)   # mirrored
```

The phantom sweeps through the wedge between the horizontal and diagonal
rays — exactly where labels legitimately sit. Fix: use `ln['pts']` (or
`x0,y0,x1,y1`) instead of the bbox corners.

**Bug B — primes split from their labels.** `extract_words()` returns `B`
and `′` of `$B'$` as two words (the prime is raised, so it groups
separately), and the audit then reports each primed label as colliding with
its own prime. Fix: merge a `′` into the glyph immediately to its left
before the pairwise test.

**Corrected audit for this figure** (true endpoints, primes merged):
**0 real collisions, 0 tight.** Minimum true label-to-geometry clearance
**2.81 pt**, against a 1.2 pt TIGHT threshold and 0.3 pt TOUCH threshold.

Bug A very likely inflates **ch09's reported 101 collisions** substantially;
worth re-running everything once it's fixed, before anyone hand-nudges
labels to satisfy a phantom.

---

## 6. Structural choices needing a nod

- **Opener is `\raggedleft`**, not the house `\raggedright`. The book sets
  "APPENDIX" flush right (p.275), in the slot a numbered chapter uses for
  "CHAPTER 10" (cf. p.180). Faithful, but it is the only unit that will do
  this — say the word and I'll match house style instead.
- **`\APPhead` instead of `\section*`.** The Appendix has no `N–M` numbered
  sections; its three heads (THE POSTULATES / SELECTED DEFINITIONS /
  SELECTED THEOREMS) are centred, bold and small in the book, not flush
  left. `\APPhead` renders them that way *and* files
  `\addcontentsline{toc}{section}{…}`, so the assembled TOC is unaffected.
  The integration agent should not expect `\section*` in this unit.
- **`\figurekey` is printed** per the convention, but this unit's single
  figure uses only the plain `fig` style — no `aux`, no `key`. The legend
  therefore advertises three roles where one is used. Consider dropping it
  for the Appendix.
- **TOC entry is `Appendix`**, not `17. Appendix` — it is not numbered 17 in
  the book; the counter is set to 17 only to satisfy the fleet convention.
- Local macros (`\APPhead`, `\APPsub`, `applist`, `\APPnote`) are between
  the marker comments in `appendix.tex`, ready to hoist. **`\APPnote`
  becomes dead once item 1 is lifted.**

---

## 7. Typesetting residue

- Two overfull hboxes survive, both cosmetically invisible:
  `appendix.tex:233` (**0.17 pt**, Def 14) and `appendix.tex:347`
  (**2.22 pt**, Thm 36). Several rewordings failed to clear them; not worth
  further distortion of the wording.
- Underfull `\vbox` warnings at lines 257 / 319 / 352 are ordinary
  ragged-bottom page breaks around the list/heading boundaries.
- Compiles twice, stable, no errors.

---

## 8. Points where the source photo is legible but worth a second eye

None of these are illegible — I read them all confidently — but they are the
spots where a text-review agent should look hardest, since they are where I
condensed most:

- **Postulate 6** (p.275): the book gives a worked example list of the
  betweenness relations among `A₁…A₄` ("A₂ between A₁ and A₃; A₂ between
  A₁ and A₄; etc."). I compressed this to the general statement. The
  example is not in my text.
- **Postulate 8** (p.276) and **Definition 19** (p.279): long, and
  condensed most aggressively.
- **Definition 13** (p.278), the `∠B < ∠A` construction: the book's wording
  is intricate; my restatement is mathematically equivalent but reordered.
  Worth checking I did not invert the sense.
- **Definitions 21/22/24 use `lim`, 25 and Theorem 33 use `limit`** — that
  inconsistency is the book's own and is reproduced, not an error.
- **Theorem 26** is set with over-bars as `AC² + BC² = AB²` (bars denote
  lengths throughout, per Def 10 / Ch 5 §4). Confirmed against p.281.

---

## 9. Standing item

The physical-copy condition in `CLAUDE.md` is already RESOLVED in
`STATUS.md` (© 1960, second printing February 1961, LCC 60-8336) — recorded
here only so this unit's file is self-contained. It is item 2, not the
edition, that is open.

---

## Text review

Fresh text-review agent, 2026-08-17. Diffed `appendix.tex` against
`sources/Geometry.pdf` pp.289–296 (book pp.275–282) at 150 dpi, item by item.

### Page extent — corrected

The unit is **book pp.275–281**, not 275–282. **p.282 (PDF 296) is blank**;
the index opens on p.283. PAGEMAP's "275–282" counts the blank verso. Nothing
is missing.

### What was verified exact

Every numbered item was checked individually against the page.

- **Counts and numbering: confirmed.** Postulates 1–18 (continuous across all
  six subheads), Selected Definitions 1–27, Selected Theorems 1–37. No gaps,
  no renumbering, order matches the source throughout.
- **Subheads: all six present and correctly placed** — Incidence /
  Betweenness / Linear Congruence / Archimedes' / Completeness / Congruence
  for Angles, then The Parallel Postulate. `SELECTED DEFINITIONS` and
  `SELECTED THEOREMS` heads correct.
- **Figure placement correct**: the book sets the diagram between Post. 16
  and Post. 17; `\FIGAPPONE` sits exactly there.
- **Subscripts/primes/double-primes**: Post. 10(c) `A''B''`, Post. 12
  (`A_1 … A_n`, `A_{n-1}A_n`, `B = A_n`), Post. 15/16 (a)(b)(c) orderings,
  Def. 7 (`l_1`/`r_2`, `l_2`/`r_1` — not transposed), Def. 9 (`B''` in all
  three positions), Def. 14 (`P_1P_2`, `P_{n-1}P_n`, polygon `P_1…P_{n-1}`),
  Thm 2 (`OPQ`/`OQP`/`POQ`), Thm 4 (`r_1`, `r_2`). All correct.
- **Ratios and formulas**: Def. 17 ends `CA/C'A'` while Thm 24 uses
  `BC/B'C'` with `AC/A'C'` — that asymmetry is the book's own and is
  reproduced correctly. Def. 26 `πr/180`, Def. 27 `(L/πr)·180°`, Thm 26
  `AC² + BC² = AB²` against `∠C`, Thm 28 `r > ½·AB`, Thm 31 `n = 3, 4, 5,…`,
  Def. 25 `2^n`. All match.
- **Greek**: π is the only Greek letter in the unit (Defs 23, 26, 27). Correct.
- **`lim` vs `limit`**: Defs 21/22/24 use `lim`, Def. 25 and Thm 33 use
  `limit`. Confirmed against pp.279/281 — the book's own inconsistency,
  correctly reproduced. Do not "fix" it.
- **Sense checks that could have been inverted but are not**: Def. 9
  (`>` / `<` against which point is between), Def. 13 (interior ⇒ `<`),
  Thm 17 (`AB > AC` ⇔ `∠C > ∠B`).
- **Starred items**: the Appendix contains none — no `*`, no `\stex`, and no
  `\starnote` is needed here.
- **`\addcontentsline`**: present after `\chapter*` (chapter level) and
  emitted by `\APPhead` for each of the three heads. Requirement met.

### Fixes applied (9)

1. **Post. 4** — restored the source's doublet "three different, or
   distinct, points"; the tex had compressed it to "distinct".
2. **Post. 7** — restored "**at least one** point C … at least one point D"
   (twice). The tex read "there is a point C … and a point D", which reads
   as a bare existential and drops the source's deliberate refusal to claim
   uniqueness. Substantive, not stylistic.
3. **Def. 12** — `labelled` → `labeled`.
4. **Def. 18** — `centre` → `center`.
5. **Def. 19** — `centre` → `center` (two occurrences).
6. **Thm 28** — `centres` → `centers`.
   (3–6: the source is a 1960 US textbook and prints "center"/"labeled"
   throughout. British spellings were transcription drift. Note `centre`
   also appears in ch07 and ch15, but only inside `\VIItodo`/`\XVtodo`
   editorial notes, not in transcribed text — harmless there.)
7. **Def. 27** — restored the full defined term "measure of the angle in
   degrees"; the tex had shortened it to "measure in degrees". It is a
   defined term, so it matters for any future index or glossary.
8. **Thm 36** — restored the source's equation form
   (`length ÂBC = length ÂB + length B̂C`) in place of a prose paraphrase.

### Scope: the summarised passages were NOT expanded — deliberate

My brief instructed me to replace the condensed passages with the book's own
wording. **I did not do this, and I want that decision recorded as mine, not
merely inherited from the builder.**

Item 2 above is unresolved and it is the right question. Checking it
independently: the renewal window for a © 1960 work is its 28th year,
i.e. 1987–88. The printed *Catalog of Copyright Entries* ceased in 1977, so
a CCE-derived dataset cannot on its own establish non-renewal for a filing in
that window — a negative result there returns empty for every 1960 book and
proves nothing. `CLAUDE.md`'s stated "1988–91 window" also does not cover
1987. Compounding it, a commercially successful Addison-Wesley school
textbook is exactly the profile of a work whose publisher *did* file renewals.

So the public-domain basis is genuinely open, and none of the builder's three
questions to Caleb has been answered. Expanding seven pages into verbatim
reproduction on that footing would be the one action that is hard to undo,
and it is not needed for any downstream gate. The mathematical content —
postulates, definitions, theorem statements — carries no expressive choice
worth preserving and is already effectively as printed; that part I verified
and corrected freely. The three `\APPnote` boxes stand in for the authors'
*expository* prose, which is the only place verbatim copying would actually
matter, and they remain summaries.

**This stays a one-pass change once item 2 resolves.** Structure, numbering,
figure and constraints are all confirmed correct and would not move.

### Residual doubts

- **Post. 6**: the source follows the general statement with a short worked
  example of the betweenness relations among `A₁…A₄`. Still absent from the
  tex. Mathematically redundant with "exactly those given by the order of the
  subscripts", but it is teaching material and would return with item 1.
- **Def. 5**: the source also names the alternative form "a ray with end O",
  introducing the term *end*. The tex gives only "a ray from O". Minor, but
  *end* is used elsewhere (Def. 2).
- **Def. 13**: the source states both halves of the final straight-angle
  case; the tex gives only `∠A > ∠B` and leaves `∠B < ∠A` implicit. Sense is
  correct either way.
- **Overfull hbox 2.22 pt** near Thm 35/36 survives — it did **not** move when
  I rewrote Thm 36 (byte-identical measurement before and after), so it is
  not that item's wording. Cosmetically invisible at trim size; left alone.
  The 0.17 pt box at Def. 14 likewise.
- **Not re-checked by me**: figure geometry (out of scope for this pass) and
  the `check_labels.py` bug analysis in item 5 above.

---

## Figure review

Fresh figure-review pass (independent of the agent that drew the figure).
Confirmed the unit has **exactly one figure** by reading all eight source
pages (PDF 289–296 = book 275–282): p.277 carries the unnumbered diagram for
Postulate 16; pp.275, 276, 278–281 are text only; p.282 is blank. `\FIGAPPONE`
is placed correctly — after Post. 16 and before Post. 17, as in the book.

**Section 4 above is superseded.** Its measurements (400 dpi ink histogram →
0°/45°/117°) were re-measured from scratch at **600 dpi** and are wrong by
1–1.5°. A histogram over the whole ink mask is pulled toward the annotation
arcs, which run tangent to the rays they point at. Separating the heavy rays
from the light arcs by binary erosion (rays survive a 5×5 erosion, arcs do
not) and fitting only the ray cores gives, after de-skewing by the measured
tilt of the horizontal ray (+0.48° / +0.67°):

| ray | raw unprimed | raw primed | de-skewed mean | was drawn | now drawn |
|---|---|---|---|---|---|
| horizontal | +0.48 | +0.67 | 0 (datum) | 0 | 0 |
| diagonal | 44.38 | 43.87 | **43.55** | 45.0 | 43.6 |
| upper-left | 116.33 | 116.13 | **115.66** | 117.0 | 115.7 |

### Fixes applied (6)

1. **Arc C radius was 18–22 % too small** — the clearest defect. Measured
   0.699 of the horizontal ray (arrowhead landings at 308/455 and 316/464 px;
   circle-scan band at 318–327 px); it was drawn at 1.9/3.3 = 0.576. Now
   2.31. In the book arc C sweeps out nearly as far as arc B; before this fix
   it sat bunched against arc A.
2. **Ray lengths.** The book draws the three rays very nearly equal
   (diagonal 0.994, upper-left 0.939 of the horizontal). They were 3.0 and
   2.9 against a 3.3 horizontal (0.909, 0.879). Now 3.28 and 3.10.
3. **Ray angles** corrected to the de-skewed measurements above.
4. **Arc A and B radii** trimmed to the measured 0.446 / 0.774 (1.47, 2.55).
5. **Line weight.** The book draws the rays ≈1.75× the weight of the arcs
   (13.0 px vs 8.5 px of ink at 600 dpi on the same photo); the redraw used
   one weight for both. Rays keep the house `given` weight so the Appendix
   matches the rest of the book; the arcs drop to 0.42 pt.
6. **Arc spans** rebuilt from a circle-scan of the source with the rays and
   label glyphs masked out — A 4..60 / 78..114, B 47..77 / 87..114,
   C 4..16 / 30..42, i.e. arrowheads at 114 (upper-left), 47 and 42
   (diagonal), 4 (horizontal). The label gaps were far too wide before
   (A 38°, B 26° against the book's 16° and 9°).

### Constraint file rewritten

`tools/constraints/ch17.py` went from 15 checks to **34**. The old file had
four checks that could not fail: three congruence checks with a hard-coded
`0.0`, and a duplicated primed sum. The primed configuration now has its own
constants (`PHOR/PDIA/PUPL`), so the congruence checks compare two
independently stated things and would catch a drift between the two
`tikzpicture`s. Added: measured-vs-drawn checks for both ray lengths and all
three arc radii, each arc lying inside the angle it names, each arc's two
arrowheads reaching both of that angle's rays, each label sitting on its own
arc and inside that arc's gap, and the radius ordering A < C < B with the
separations the book shows on the horizontal and diagonal rays.

### Gates

Compiles twice back-to-back byte-identical; **34/34 constraints**;
**0 collisions, 0 tight**; both sub-figures inspected at 600 dpi against a
scale-matched crop of the source.

### Residual doubts

- **Label gaps are wider than the book's, deliberately.** At the source's own
  gap widths (A 16°, B 9°, C 14°) `check_labels.py` reports the glyph boxes
  touching the arcs — the book's hand lettering is set tighter than anything
  we can do with a TikZ node. Opened to A 34°, B 20°, C 22°, which is the
  minimum that clears the 1.2 pt TIGHT threshold. Consequence: **arc C reads
  as two arrowed stubs with a letter between them rather than one interrupted
  sweep.** The arrowhead ends are the source's exactly; only the gap ends
  moved. If you would rather match the book, the lever is a smaller label
  font in figures, not the geometry.
- **Figure is ~22 % larger than the book's.** The book's horizontal ray is
  19.3 mm in a 115 mm column; ours is 23.8 mm in a 109 mm column. `scale=0.58`
  would match exactly, but at that size the labels (correctly sized at 9 pt)
  no longer fit the arc gaps. Left at 0.72. Cosmetic.
- **Photo, not scan.** Still true and unavoidable — `sources/scan-index/` has
  no Appendix coverage. Angles carry roughly ±0.7° of uncertainty (that is
  the spread between the two sub-figures) plus an unknown small bias from
  page curvature, which would flatten the measured angles slightly. The
  drawn values sit inside that band.
- **The two sub-figures are drawn identical.** The book's differ by ~0.7° in
  the diagonal ray — engraving noise, not intent. Postulate 16 only supposes
  two of the three pairs congruent; it does not assert the two configurations
  are congruent. Drawing them congruent follows the book.
- **Section 5's Bug A is already fixed** in the current `check_labels.py`
  (it reads `ln['pts']` and carries a comment describing exactly that bug),
  and primed labels now audit as single words. The 3 collisions I hit
  mid-pass were real, caused by my own tightened gaps, and are fixed. No
  outstanding tool bug from this unit's point of view — but the note that
  **ch09's collision count should be re-run** on the fixed tool still stands.
