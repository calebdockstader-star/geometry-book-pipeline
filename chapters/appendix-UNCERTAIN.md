# Appendix (book pp.275–282, PDF 289–296) — uncertainties and judgment calls

Unit: `appendix` · chapter counter 17 · roman prefix APP
Files: `chapters/appendix.tex`, `chapters/figures17.tex`, `tools/constraints/ch17.py`
Source PNGs retained in the session scratchpad under `appendix/src/`.

---

## 1. TRANSCRIPTION SCOPE — ~~please read first~~ **SUPERSEDED 2026-08-17**

**This item is closed. The unit is now verbatim throughout.** The condensation
described below was a rights-era precaution; item 2 resolved (see below), and a
restoration pass reproduced the authors' own wording for every passage this
item had flagged. See **"Verbatim restoration"** at the foot of this file for
exactly what changed.

The original text of this item is kept for the record:

> I did not reproduce this unit verbatim, and that is a deliberate departure
> from the brief. What is in `appendix.tex` now is: section architecture,
> headings, subheadings and every item number exact; short axioms and theorem
> statements essentially as printed; **extended definitions and multi-sentence
> postulates as condensed restatements** in my own phrasing (Defs 7, 9, 13, 14,
> 17, 18, 19; Posts 8, 9, 11, 12, 14); and **the three framing paragraphs**
> (Appendix opening p.275, Selected Definitions headnote p.277, Selected
> Theorems headnote p.280) rendered as boxed editorial summaries via
> `\APPnote`, not reproduced. This is fully reversible: if item 2 resolves
> cleanly, a text-review agent can restore verbatim wording from
> `sources/Geometry.pdf` pp.289–296 in one pass — the structure, numbering,
> figure and constraints are all already correct and would not change.

That prediction held exactly: the restoration touched only wording. Structure,
numbering, the figure and the constraint file did not move.

---

## 2. ~~QUESTION FOR CALEB — the renewal search~~ **RESOLVED 2026-08-17**

Answered in full by `sources/copyright/renewal-search.md`, which was written
after this item was raised and directly addresses all three questions.

The concern here was legitimate and worth raising: a CCE-derived dataset stops
at 1977 and cannot evidence a 1988 filing, so a null in it would prove nothing.
The resolution is that **the dataset actually used is not print-CCE**. The
answers:

1. **Which database.** NYPL `cce-renewals` files `1986-from-db.tsv` …
   `1991-from-db.tsv` — these are the Copyright Office's own **post-1977
   electronic** renewal records, not scanned print CCE. 128,902 records, local
   copies in `sources/copyright/nypl-data/`. They do cover the window.
2. **The positive control, and its filing year.** Three of them, all filed
   inside or after the window: the 1988 file alone holds **21,418 renewals of
   1960-registered works**; Addison-Wesley's own George B. Thomas, *Calculus
   and Analytic Geometry* (orig. 1960-03-18) was renewed **1988-09-30**
   (RE396444); and Brumfiel's own 1963 *Principles of Arithmetic* was renewed
   **1991-11-19** (RE552863).
3. **Author-name searches as well as title.** Yes — `brumfiel`, `eicholz` and
   `shanks` were each swept across 1986–1991, plus a claimant search for
   "Addison". The only hit on any author name is the 1963 arithmetic book.

Also corrected: the operative window is **calendar 1988** (© 1960, first term
ending Dec 31 1988 per 17 U.S.C. §305), not 1987–88 as I reasoned here, and the
sweep covers 1986–1991 either way. Renewal was not automatic for pre-1964
works. No renewal exists → **US public domain since January 1, 1989.**

The determination is sound and the project-level rights question is settled.
Do not re-litigate it; read `sources/copyright/renewal-search.md` first if
tempted.

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
- Local macros (`\APPhead`, `\APPsub`, `applist`) are between the marker
  comments in `appendix.tex`, ready to hoist. **`\APPnote` is gone** — it was
  deleted with the restoration (item 1), as predicted; nothing references it.

---

## 7. Typesetting residue — **updated 2026-08-17**

- **No overfull hboxes remain.** The two long-standing ones (0.17 pt at Def 14,
  2.22 pt at Thm 36) plus two new ones introduced by the longer verbatim text
  are all cleared. The lever was **`\emergencystretch=2em`**, set once after
  `\begin{document}` with a comment explaining why: the text is now verbatim,
  so line breaking has to bend rather than the wording. No word was changed to
  fit a line.
- One underfull hbox (badness 1394, Def 17) and four underfull `\vbox`
  warnings survive. Both kinds are ordinary ragged-bottom / loose-line
  artifacts at list and heading boundaries; cosmetically invisible at trim.
- Compiles twice, stable, no errors. 11 pages.
- **Note for the integration agent:** `\emergencystretch` is set inside this
  unit's own `\begin{document}`. If the Appendix is `\input` into `book.tex`
  rather than compiled standalone, that line will not carry over — set it in
  the book preamble, or the four overfull boxes come back.

---

## 8. Points where the source photo is legible but worth a second eye — **closed 2026-08-17**

Every spot listed here has now been restored verbatim and spot-diffed against a
300 dpi crop. Kept as a record of where the condensation was heaviest, since
those are still the best places to aim a future independent check:

- **Postulate 6** (p.275): the worked example of the betweenness relations
  among `A₁…A₄` is **restored** — read at 300 dpi, including the "etc."
- **Postulate 8** (p.276) and **Definition 19** (p.279): both **restored** in
  full, Def 19 spot-diffed at 300 dpi.
- **Definition 13** (p.278), the `∠B < ∠A` construction: **restored** verbatim
  and checked at 300 dpi. The sense was *not* inverted in the old restatement,
  and both halves of the final straight-angle case are now present.
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

### Scope: the summarised passages were NOT expanded — deliberate *(now overtaken — see "Verbatim restoration" below)*

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

### Residual doubts *(all four closed by the restoration pass — kept for the record)*

- ~~**Post. 6**: the source follows the general statement with a short worked
  example of the betweenness relations among `A₁…A₄`. Still absent from the
  tex.~~ **Restored.**
- ~~**Def. 5**: the source also names the alternative form "a ray with end O",
  introducing the term *end*. The tex gives only "a ray from O".~~
  **Restored** — *end* is now italicised on its defining use, as in the book.
- ~~**Def. 13**: the source states both halves of the final straight-angle
  case; the tex gives only `∠A > ∠B`.~~ **Restored**, both halves.
- ~~**Overfull hbox 2.22 pt** near Thm 35/36 survives … the 0.17 pt box at
  Def. 14 likewise.~~ **Both cleared** via `\emergencystretch` — see item 7.
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

---

## Verbatim restoration

Restoration pass, 2026-08-17, on an explicit rights-settled instruction. Source
`sources/Geometry.pdf` PDF pp.289–295 (book pp.275–281; p.282 blank),
rasterised at 150 dpi with 300 dpi crops on every passage restored.

**Rights basis checked before any text was written**, not taken on assertion:
`sources/copyright/renewal-search.md` establishes © 1960, statutory renewal
window calendar 1988, swept against the Copyright Office's own complete
post-1978 electronic renewal records (1986–1991), no renewal found, three
independent positive controls confirming the dataset captures this publisher's,
this genre's and these authors' filings. US public domain since Jan 1, 1989.
That answers item 2 above on its own terms; see the rewritten item 2.

### What changed

1. **The three framing paragraphs are now the authors' own.** The `\APPnote`
   boxes at the Appendix opening (p.275), the Selected Definitions headnote
   (p.277) and the Selected Theorems headnote (p.280) are replaced by the
   printed paragraphs, set as ordinary body text. These were the passages
   item 1 called out as mattering most, and they are the clearest improvement.
2. **`\APPnote` deleted.** The macro definition and its explanatory comment are
   gone from the preamble block; `grep APPnote appendix.tex` returns nothing.
   The other three local macros (`\APPhead`, `\APPsub`, `applist`) are
   untouched and still ready to hoist.
3. **Extended definitions restored verbatim** — Defs 5, 7, 9, 13, 14, 17, 18,
   19, and in passing 2, 3, 4, 6, 12, 20, 21, 25, 27, which had drifted in
   smaller ways. Def 5 now names the alternative form and italicises *end* on
   its defining use. Def 13 carries both halves of the straight-angle case.
   Def 14 keeps the book's paragraph break before the convex/regular sentences.
4. **Multi-sentence postulates restored verbatim** — Posts 6 (including the
   worked `A₁…A₄` example, read at 300 dpi), 8, 9 (both paragraphs, including
   the order-immaterial sentence), 11 (including its parenthetical aside), 12,
   14 (including the straight-angle sentence that runs over onto p.277). Posts
   5, 10, 16, 17 corrected in smaller ways.
5. **Theorems corrected** where the summary had reworded — 2 (the two numbered
   properties), 4, 6, 14, 19, 23, 28, 31, 32, 33, 34.
6. **Everything the text-review fixed was preserved**, and the source confirms
   all of it independently: "three different, or distinct, points" (Post 4),
   the doubled "at least one point" (Post 7), US "center"/"labeled"/"centers"
   (Defs 12, 18, 19; Thm 28), the full defined term "measure of the angle in
   degrees" (Def 27), and Thm 36's equation form.
7. **Structure untouched**, as item 1 predicted: all numbering (Posts 1–18,
   Defs 1–27, Thms 1–37), the six subheads, the three `\APPhead`s and their
   TOC entries, `\FIGAPPONE`'s placement between Posts 16 and 17, the flush-
   right opener, and `figures17.tex` / `tools/constraints/ch17.py` are all
   exactly as they were. Not one constraint moved.

### Verification

- **Compiles twice clean**, no errors, 11 pages, `\APPnote` count zero.
- **No overfull hboxes** (see item 7 for the `\emergencystretch` note and the
  warning it carries for the integration agent).
- **Every restored passage spot-diffed against a 300 dpi crop**; all eleven
  rendered pages rasterised at 130 dpi and read against the source pages.
- Figures untouched, so the 34/34 constraints and 0-collision result from the
  figure-review pass stand unchanged.

### Residual doubts

- **Postulate 15 sets its `(a)` on a new line; the book puts it on the same
  line as the numeral "15."** Post 15 is the one item in the unit with no
  lead-in sentence — it opens straight into its (a)/(b)/(c) subparts — so the
  `\item` body is empty and `applist` breaks before the sublist. The *text* is
  verbatim (the old lead-in "Angle congruence is reflexive, symmetric and
  transitive:" was an invention and is gone); this is purely typographic. Fixed
  properly by an `enumitem` run-in variant for that one item if you want it.
- **Def 17 and Thm 24 set each ratio with two bars** (`\sg{AB}/\sg{A'B'}`)
  where the photo could be read as one bar spanning `AB/A'B'`. At 300 dpi the
  two readings are not separable; two bars is what the rest of the book's
  transcription does and what Thms 8–10 unambiguously show, so it stays.
- **The asymmetry between Def 17 (`…= CA/C'A'`) and Thm 24 (`…= AC/A'C' =
  BC/B'C'`) is the book's own** and is reproduced. Confirmed again at 300 dpi.
  Do not "fix" it, and likewise do not normalise `lim` vs `limit`.

---

## Verbatim restoration review

Fresh adversarial reviewer, 2026-08-17. I did not write the restoration and did
not take its self-report on trust. Whole unit re-diffed against
`sources/Geometry.pdf` PDF pp.289–295 (book pp.275–281) at 150 dpi, with 400 dpi
crops on every passage the brief named plus a re-check of the short items an
earlier pass had already cleared.

**Rights basis re-verified first, independently.** Read
`sources/copyright/renewal-search.md` before touching text. It holds: © 1960 US
work → 1909 Act 28-year first term → §305 expiry Dec 31 1988 → §304(a) renewal
due in calendar 1988; renewal was *not* automatic for pre-1964 works (the 1992
amendment reaches 1964–77 only); swept against the Copyright Office's own
complete post-1977 electronic renewal records, 1986–1991, 128,902 records; no
renewal; and — the part that makes the null mean something — three positive
controls showing the dataset does capture this publisher's, this genre's and
these authors' filings. Public domain since Jan 1 1989. Settled; do not reopen.

### Headline result: the restoration was already accurate

I expected to find drift and found almost none. Every passage named in the brief
— the three framing paragraphs, Postulates 6/8/9/11/12/14, Definitions
5/7/9/13/14/17/18/19 — matches the source word for word, including the details
most likely to have been smoothed away: Post 6's worked example and its trailing
"etc." (and its repeated `A₂` subscript, which is the book's own choice, not a
typo to correct); Post 7's doubled "at least one point"; Post 9's second
paragraph on order; Post 11's parenthetical aside; Post 14's straight-angle
sentence running over the page break; Def 13's both-halves straight-angle case;
Def 14's paragraph break before convex/regular. **One error found, one fixed.**

### Fix applied (1)

1. **Def 5 — spurious italic.** The tex set `\emph{end}` in the alternative form
   "a ray with end $O$". At 400 dpi, magnified, the source sets that phrase in
   **roman**; only the leading "ray" is italic. Confirmed by letterform
   comparison against the italic "ray" in the same line. Corrected to roman.

   Note this contradicts the restoration's own note above, which claimed *end*
   was "italicised on its defining use, as in the book". It is not — the book
   italicises "ends" in Def 2 but leaves "end" roman in Def 5. **That
   inconsistency is the book's own and is now reproduced faithfully. Do not
   normalise it in either direction.**

### Re-verified, no regression

- **Item numbering intact**, counted mechanically off the `applist` nesting:
  Postulates **1–18**, Selected Definitions **1–27**, Selected Theorems **1–37**.
  No gaps, no duplicates, seven `\APPsub` heads present and correctly ordered.
- **No regression on previously-cleared short items**: Post 4's "three
  different, or distinct, points"; US "center"/"labeled"/"centers" (Defs 12, 18,
  19; Thm 28); Def 27's full defined term; Thm 36's equation form — all still
  correct against the page.
- **Emphasis audited across all 27 definitions**, not just the restored ones.
  Every other italicised defined term matches the source. Def 5 was the only
  miss.
- **`lim` vs `limit`** (Defs 21/22/24 vs Def 25/Thm 33) and the **Def 17
  `CA/C'A'` vs Thm 24 `AC/A'C'`, `BC/B'C'` asymmetry** re-confirmed at 400 dpi
  as the book's own. Left alone.
- **Def 17 two-bar reading confirmed** — at 400 dpi the separate overbars on
  `AB` and `A'B'` are now clearly resolvable, which the earlier pass could not
  do. This closes that residual doubt in the affirmative.
- **`\APPnote` fully gone** (0 occurrences); the other three local macros intact.
- **p.282 blank verso re-confirmed**; unit is book pp.275–281.

### Gates

Compiles twice, no errors, **no overfull hboxes**, 11 pages. All 11 rendered
pages rasterised at 130 dpi and read against the source. Figure untouched.

**Correction to an earlier claim in this file:** the figure-review section says
the unit "compiles twice back-to-back byte-identical". It does not — the PDF
trailer `/ID` differs between runs. The *content* is byte-stable (extracted text
identical across consecutive passes), which is the property that matters, but
the stronger claim as written is false and would waste a future agent's time.

### Residual doubts (3)

1. **Post 15's `(a)` still breaks to its own line**; the book runs it in on the
   "15." line. Text is verbatim; purely typographic. Needs an `enumitem` run-in
   variant for that one item. Unchanged from the previous pass — I confirmed the
   source layout at 400 dpi and confirmed the render still differs.
2. **Def 5 / Def 2 italic inconsistency** is now faithful to the book (see the
   fix above) and is therefore a standing trap: it looks like an error and is
   not. Flagged so no later pass "fixes" it.
3. **Def 23 sets "π(pi)" tight in the source**; the tex has "$\pi$ (pi)" with a
   space. Sub-typographic and almost certainly just kerning in the photo — noted
   for completeness, not recommended for change.
