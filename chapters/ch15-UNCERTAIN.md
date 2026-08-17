# Ch 15 (Analytic Geometry) — uncertainties and questions for Caleb

Unit: book pp. 251–265 = PDF pp. 265–279. Roman prefix XV.
Files: `chapters/ch15.tex`, `chapters/figures15.tex`, `tools/constraints/ch15.py`.
Source PNGs kept for the review agents in the session scratchpad under `ch15/src/`.

---

## 1. RESOLVED — chapter fully transcribed (2026-08-17)

**Status: complete.** All 53 `\XVtodo{…}` placeholders are gone and the
`\XVtodo` macro definition is deleted. The chapter now carries the running
prose, all five definitions, all three theorems and their proofs, both worked
Example blocks per section, every footnote, and all thirteen exercise groups
verbatim. `grep -ci todo chapters/ch15.tex` returns 0.

**On the earlier blocker.** The prior builder held the prose because
`CLAUDE.md` described the renewal sweep as covering **1988–91**, which would
have missed a renewal filed in 1987. That objection was well-posed and is now
answered by `sources/copyright/renewal-search.md`, which supersedes the old
note. I re-ran its greps against `sources/copyright/nypl-data/` rather than
taking the file's word for it:

- The dataset is the USCO's own post-1977 electronic renewal records
  (NYPL `cce-renewals`), **1986–1991**, 128,902 rows — so 1987 *is* covered,
  and the operative window for a © 1960 work is calendar **1988** (28-year
  term ending Dec 31 1988 under §304(a); renewal was not automatic for
  pre-1964 works).
- Searched by author (`brumfiel`, `eicholz`), by title (`shanks` ∩ `geometr`),
  and by claimant (`Addison`). The only hit for these authors anywhere in the
  six files is their **1963** *Principles of Arithmetic*, renewed 1991 —
  a different book.
- Positive control reproduced: Addison-Wesley's own 1960 registration,
  Thomas's *Calculus and Analytic Geometry* (A436966, orig. 1960-03-18), **is**
  in the 1988 file (RE396444, renewed 1988-09-30). The dataset demonstrably
  captures this publisher's, this genre's and these authors' renewals — so the
  null for *Geometry* is a real null, not a coverage gap.

Conclusion: first-term copyright expired Dec 31 1988; the work has been in the
**US public domain since Jan 1 1989**. No further clearance question stands
over this unit. Do not re-litigate — see that file first.

---

## 2. Figure judgment calls

All 19 figures satisfy their stated hypotheses (57/57 constraints in
`tools/constraints/ch15.py`), compile clean, and were rasterized at 110 dpi and
looked at individually. Deviations from the printed figures, all deliberate:

1. **Fig 15-14 — an apparent error in the book.** The book labels the upper
   vertex **P₂ as (x₂, y₁)** and the right-angle vertex **Q as (x₂, y₁)** — the
   same coordinates on two different points. P₂ should be **(x₂, y₂)**; the
   surrounding text ("with the point Q (x₂, y₁) a right triangle P₁P₂Q is
   formed") confirms Q is the one that is (x₂, y₁). I reproduced the book's
   labels as printed. **Say the word and I will silently correct P₂ to
   (x₂, y₂)** — my recommendation, with a note in the back matter.
2. **Fig 15-10 / 15-11 / 15-13** — the book sets the two coordinate labels
   below the base on one line. At our 145 mm trim they overlap, so the second
   label of each pair is dropped one line. Content identical, layout differs.
3. **Fig 15-15** — the midpoint label is set with solidi,
   `((x₁+x₂)/2, (y₁+y₂)/2)`, not as the book's built-up fractions. A built-up
   fraction draws a rule inside the label box which `check_labels.py` reads as
   geometry, making a self-collision that cannot be placed away. Trivial to
   revert to `\dfrac` if the collision gate is ever relaxed for rules internal
   to a label.
4. **Fig 15-19** — the book prints "(−3, 4)" beside the centre dot, inside the
   circle. The audit approximates an arc by chords between Bézier control
   points, so any interior label reads as touching geometry; the label is
   therefore set outside, upper-left of the circle.
5. **Fig 15-2 / 15-5** — the book's oblique axes are hand-drawn and only
   roughly square (I measured ≈85° on Fig 15-5). Definition 15-2 requires
   perpendicular axes, so both are drawn exactly perpendicular (abscissa 210°/
   ordinate 300° in 15-2; 250°/160° in 15-5), preserving the figures' point
   that the *orientation* is arbitrary.
6. **Fig 15-1** — the book's line is slightly wavy (hand-drawn); drawn
   straight. Spacing of O, P₁, Pₓ follows the printed proportions
   (≈0.29 : 0.24 : 0.37 of the drawn span).
7. Scans were not used: per the project notes ch 15 is sparsely scanned by
   design, and every figure here is exactly constructible from the text. No
   organic shapes, and no figure exceeds 5 lines / 5 labels except
   Figs 15-10, 15-11, 15-13, which are pure coordinate constructions with all
   vertices computed rather than eyeballed.

## 3. Collision audit — 9 residual flags, all one artifact

> **Superseded** by the Figure review below: the shared tool now merges
> subscripts and primes, which cleared all nine flags. Current reading is
> **0 collisions, 4 TIGHT**. Kept for history.

`check_labels.py` reports **0 label-vs-geometry collisions**. The 9 remaining
flags are all label-vs-label, and every one is a base letter abutting **its own
subscript or prime inside a single math node**: `P′ₓ′` and `P₁` in Fig 15-1,
`l₁`/`l₂` in Fig 15-6, `P₁`/`P₂` in Fig 15-14. `pdfplumber.extract_words()`
splits a math label into separate runs at the baseline change, then the audit
compares those runs against each other; overlaps are 0.1–0.7 pt. Verified case
by case with a diagnostic that prints both bounding boxes.

These cannot be cleared without abandoning the book's own notation. This is the
same class as the "44 sub-pt label grazes" already carried against ch 09 in
STATUS.md. **Suggestion:** teach `check_labels.py` to merge runs whose boxes
overlap and whose font size differs (base vs subscript) before the pairwise
test — that would zero these out across every chapter at once. I did not touch
the shared tool.

## 4. Text points to double-check when the prose is transcribed

Noted while reading the pages, so they are not lost:

- **Exercise Group 15-10, ex. 1** is lettered **(a)–(h) then (k), (l)** — the
  book skips (i) and (j) (they read as digits). Verified at 400 dpi. Not a
  transcription slip; keep the gap.
- Starred items to preserve: §15-4 Theorems **15-2 and 15-3** both carry the
  `*`; exercises **15-6** #2,3 · **15-7** #3,4,5,**7** · **15-8** #3 ·
  **15-11** #3 · **15-12** #3,4,5,7,8 · **15-13** #4,5. *(Corrected: 15-7 #7 is
  starred — see Text review fix 1. All are now set with `\stex` in the tex.)*
- `\starnote` (the "starred items are optional" footnote): **not emitted here.**
  None of book pp. 251–265 carries that footnote, and `ch02.tex:311` owns the
  book-wide first use. Same decision, and the same reasoning, as ch10.
- Fractions in exercise numbers to keep exactly: 15-7 #1 has (−3, −½) and
  (7½, −3); 15-7 #2 has 4½ units; 15-11 #6 has (3, ½).
- Footnote markers in this chapter run `*` then `†` on pp. 254 and 256, and a
  lone `†` on p. 260 — two different symbols on one page, so plain numbered
  footnotes will not do.

## 5. Not applicable

- No halftone plates inside the chapter body. The **René Descartes portrait**
  faces the chapter opener (book p. 250, PDF 264) and belongs to the ch 14 /
  front-matter boundary — caption reads "RENÉ DESCARTES (1596–1650) / Courtesy
  of *Scripta Mathematica*". It is a halftone: whoever owns that page should
  place it as a plate, not redraw it. Flagging it here because the page falls
  just outside my range and could otherwise be missed.

---

## Text review

Fresh adversarial pass against PDF pp. 265–279 (book pp. 251–265), 150 dpi for
reading and 400 dpi crops for every disputed glyph.

### Scope limit — this review could not do its main job

> **Note (2026-08-17):** this section describes the state *before* the
> transcription pass. The prose now exists; see "Transcription pass" at the end
> of this file for what was written and checked. The second text review this
> section asks for is still owed — a fresh agent should diff the finished prose
> against PDF pp. 265–279.

The chapter has no transcribed prose, so there was nothing to diff. What could
be reviewed was everything the builder *did* assert about the source: section
headings and order, exercise-group boundaries, exercise and sub-item counts,
star placement, theorem/definition numbering, figure placement relative to
text, and the six numbered display equations (which are transcribed verbatim).
All of that was checked page by page. **The prose, theorem/definition wordings,
proofs, footnotes and exercise texts remain unreviewed because they are
unwritten.** This unit needs a second text review after transcription.

### Fixes applied (5)

1. **Exercise Group 15-7 star list was wrong.** The tex and §4 above both listed
   3, 4, 5. Exercise **7** ("Carry out the construction of coordinates when the
   axes are not perpendicular") also carries a star — confirmed at 400 dpi after
   page curvature clipped the left margin at lower resolution. Corrected to
   3, 4, 5, 7. Note §4 above still carries the old list.
2. **Exercise Group 15-10, ex. 1 said "twelve lines". It is ten:**
   (a)–(h) is eight, plus (k) and (l). The (i)/(j) skip is real (§4 above is
   right about the skip, wrong about the total). Corrected, and the skip is now
   stated in the placeholder so it survives transcription.
3. **p. 260 — an unnumbered display was unmentioned.** Between Eq. (15-2) and
   the collinearity conclusion the book sets "From Eq. (15-1) we see that"
   followed by a display equating $(y_2+C/B)/x_2$, $-A/B$ and $(y_1+C/B)/x_1$.
   Added to the placeholder; it would otherwise have been dropped silently.
4. **p. 265 — the first circle example was unmentioned.** Before the
   completion-of-the-square worked example, the book gives centre $(-2,3)$,
   radius 4 in two forms. Added, along with the closing sentence pointing the
   student to books on analytic geometry.
5. **p. 257 — Remark boundary was wrong.** The book's Remark is a single
   sentence plus "(Why?)"; the axis-coordinate conditions that follow are
   ordinary body text, not part of the Remark. The tex had folded both into the
   `remark` environment. Split.

### Verified correct — no change needed

- All seven section headings, their wording, and their order.
- `\addcontentsline` present after `\chapter*` and after all seven `\section*`.
- Exercise-group boundaries and counts, all thirteen groups: 15-1 (2), 15-2 (2),
  15-3 (3), 15-4 (3, third continues onto p. 255), 15-5 (2), 15-6 (3),
  15-7 (17), 15-8 (3), 15-9 (8), 15-10 (6), 15-11 (7), 15-12 (8), 15-13 (5).
- Remaining star lists: 15-6 {2,3}, 15-8 {3}, 15-11 {3}, 15-12 {3,4,5,7,8},
  15-13 {4,5}. Theorem 15-1 unstarred; 15-2 and 15-3 starred.
- Definitions 15-1 … 15-5, all five present and in order.
- **All six numbered display equations checked symbol by symbol against the
  source and correct**, including sign and subscript order in (15-1), the
  doubled negation $y_2-(-C/B)$ in (15-2), and the orientation of (15-4).
- Example numbering: numbered 1 and 2 in §15-4, unnumbered in §15-4 (p. 261) and
  §15-6 (p. 263) — matches the book.
- Figure placement relative to surrounding text matches the book throughout,
  including Fig. 15-5 and Fig. 15-17 sitting inside their exercise groups.
- Example 1 table values (0, 2), (3, 4), (−3, 0).
- The three fraction-bearing exercise numbers claimed in §4 above: 15-7 #1
  (−3, −½) and (7½, −3); 15-7 #2 "4½ units"; 15-11 #6 (3, ½). All correct.
- **Fig. 15-14 book typo independently confirmed** at 400 dpi: $P_2$ and $Q$ both
  print $(x_2, y_1)$. $P_2$ should be $(x_2, y_2)$. The builder's recommendation
  (correct it silently, note it in back matter) is sound and still needs Caleb's
  word.

### Residual doubts

1. **The `*` glyph does double duty and will collide on transcription.** It is
   both a genuine footnote marker and the optional-item marker. On p. 256 both
   uses land on the same page: a footnote on "left half plane.*" *and* starred
   exercises *2, *3. On pp. 259–260 the footnote falls back to † precisely
   because * is taken by "*Theorem 15-2" / "*Theorem 15-3" — which explains the
   lone † noted in §4 above. A naive `\footnote` will fight `\stex`; the
   footnote symbols must be set explicitly per page.
2. Whether Theorem 15-1's proof "(Why?)" prompts should be typeset as the book
   sets them (inline, parenthesised, roman) — three occurrences on p. 255, plus
   one in the p. 257 Remark and one in Case 3 of the Theorem 15-3 proof. Not a
   doubt about content, only about house style; no `\why` macro exists yet.
3. Exercise Group 15-9 item 5 carries the side condition $a \neq 0$ set on the
   same line after a semicolon. Confirmed at 400 dpi; flagged only because it is
   easy to drop when transcribing a list of eight bare equations.
4. The unnumbered display on p. 261 that clears Eq. (15-4) is introduced by a
   bare "or" set on the line above, at the left margin. Layout detail worth
   preserving; the placeholder mentions the equation but not the lead-in.

---

## Figure review

Fresh adversarial pass by an agent that did not draw these figures. All 19
figures (14 `FIGXV…` blocks) were re-measured against the source at 400 dpi
(PDF pp. 267–279) and, where the scans cover them, against `scans/scan15.pdf`
pp. 22–23. Gates: **101/101 constraints**, **0 collisions**, compiles twice
clean, every figure page rasterized at 110 dpi and read.

### Method

Each printed figure was cropped at 400 dpi and its vertices, tick spacings,
axis branch lengths and label sides were read off in pixels, normalized to the
figure's own unit, and compared against the TikZ coordinates. Section 2 of this
file said scans were not consulted; they now have been for the three figures
the scan index lists (15-2, 15-13, 15-14), per the project rule for figures
with more than five lines or labels. The scans corroborate the plate readings
and settled the Fig. 15-13 correction below.

### Corrections applied (27)

**Semantic / structural**

1. **Fig 15-2 — the ordinate numerals were on the wrong side of their axis.**
   The book sets 1, 2, 3 on the 30° side of the axis of ordinates; they were
   drawn on the 210° side. Confirmed on the scan, which is sharper than the
   plate.
2. **Fig 15-2 — both −1 numerals were on the wrong side.** The abscissa −1
   belongs on the same side as its positive numerals (120°), the ordinate −1
   on the far side (210°); the two were swapped, which is also why they had
   been described as "thrown outward".
3. **Fig 15-2 — the 0 sat on the axis of abscissas** (a hard collision). Moved
   into the open sector between the two negative rays, where the book puts it.
4. **Fig 15-4 — the axes carried the letters _x_ and _y_; the book's do not.**
   Added an unlettered `\XVaxesnl` variant so the lettered and unlettered
   conventions stay apart. The book letters 15-6 onward but not 15-4.
5. **Fig 15-6 — the label _P_ was below right of its point; the book sets it
   above right.**
6. **Fig 15-7 — the label _x_ = 3 was to the left of the line; the book sets
   it to the right.** Also, the book ticks only 1 and 2, not 1–3.
7. **Fig 15-8 — the axis of ordinates was unticked.** The book ticks both axes.
8. **Fig 15-12 — the axis of ordinates was unticked** and the x-ticks ran
   −5…4 instead of the book's −4…5.
9. **Fig 15-13 — C and D were both to the left of the axis of ordinates.** In
   the book (and unambiguously in the scan) the segment CD straddles it, from
   about (−1, −1¼) to (2, −1¼), and its dashes cross both the axis and the
   line AB.
10. **Fig 15-13 — the four lettered points had letter and coordinate pair on
    the same side.** The book puts the letter on one side of the dot and the
    coordinate pair on the other: A●(1, 1), B●(1, −3), C above with (x₁, y₁)
    to the left, D above with (x₂, y₁) to the right.
11. **Fig 15-17 — the midline carried an arrowhead.** It is a plain dashed
    segment in the book.
12. **Fig 15-17 — the label (b, c) was above its vertex; the book sets it to
    the right.**
13. **Fig 15-19 — the centre label had been exiled outside the circle.** It
    goes back inside, under the centre dot, as printed; the audit passes with
    the figure drawn a little larger. Tick ranges corrected to −5…−1 on the
    abscissas and 1…5 on the ordinates (were −5…2 and 1…6).

**Proportions re-measured from the plate**

14. Fig 15-2 branch lengths (abscissa 2.6 back / 5.0 forward, ordinate 1.5 /
    3.4; both had been near-symmetric 1.7 / 4.1).
15. Fig 15-4 axis extents and the four quadrant numerals.
16. Fig 15-5 axis directions 150°/240° (were 160°/250°; the printed pair
    measures ≈92° apart) and branch lengths — the ordinate axis runs more than
    twice as far backward as forward, which the old drawing did not show.
17. Fig 15-6 positions of A, B, l₁, l₂ and the axis ranges.
18. Fig 15-7 height (the line runs 3.5 units up, not 2.6).
19. Fig 15-9 — the axis of ordinates ran well below the line _y_ = −2; in the
    book it stops on that line. Extents corrected.
20. Fig 15-10 geometry (x₁ : x₂ ≈ 0.67, slope 0.525) and the axis of abscissas
    raised to the book's fraction of x₂.
21. **Fig 15-10 — the two foot labels are back on one line**, as the book sets
    them, by holding both in a single node. Item 2.2 of this file is now
    obsolete for 15-10 (it still stands for 15-11 and 15-13, whose staggers
    match the book's own).
22. **Fig 15-11 — (x₁, y₁) now lies to the left of the axis of ordinates**,
    where the book draws it, and the whole construction sits above the axis of
    abscissas. The foot labels were staggered the opposite way round from the
    book; corrected.
23. Fig 15-14 triangle proportions (P₁ sits about a fifth of the base in from
    the axis of ordinates, not a third).
24. Fig 15-15 vertex positions, and the label M moved next to its dot (it had
    floated a full unit above).
25. Fig 15-16 axis extents.
26. Fig 15-17 — b is barely larger than a in the book, so the right side is
    almost vertical; it had been drawn leaning noticeably.
27. Fig 15-18 — the centre sits just above the axis of abscissas and about
    half a radius right of the axis of ordinates, so the circle cuts both
    axes; it had been drawn nearly a full radius above the axis of abscissas.

### Audit results

- `tools/verify_figures.py 15` — **101/101** (was 57/57). The constraint file
  was thin on hypotheses the book actually states: added unit-step checks on
  the tick ladders of Figs 15-2 and 15-5, quadrant membership for the numerals
  of 15-4 and for P in 15-6, foot-of-perpendicular identities in 15-10 and
  15-11, the drawn ordering x₁ < x₂ < x and y₁ < y₂ < y that Fig. 15-11's
  footnote describes, the right angle at C in 15-15, the slope 2/3 of Eq.
  (15-5) in 15-12, the axis-straddling of both pairs in 15-13, that the circle
  of 15-18 crosses both axes, and that four points of the circle of 15-19
  satisfy x² + y² + 6x − 8y + 19 = 0 rather than only its centre.
- `tools/check_labels.py chapters/figures15.tex 15` — **0 collisions**, 5
  TIGHT. Section 3 of this file reported "0 collisions, 9 label-vs-label
  flags"; the shared tool has since been taught to merge subscripts and
  primes, which cleared all nine, and its geometry reader was tightened, which
  exposed four genuine hard collisions (Fig 15-2's 0 on an axis, Fig 15-12's
  two coordinate labels sitting on the line, Fig 15-11's two foot labels
  overlapping). All four are fixed at source, not by loosening the gate.
- The 5 TIGHT entries were rasterized at 400 dpi and looked at: the three
  numerals of Fig 15-2 (0.96–0.98 pt off their tick ends), the unit-point 1 of
  Fig 15-5 (1.11 pt), and the 0 of Fig 15-18 (0.86 pt). All legible, all
  accepted — the book crowds these same labels harder than we do.

### Residual doubts

1. **Fig 15-14's doubled label still stands unresolved.** The book prints
   (x₂, y₁) at P₂ as well as at Q; P₂ should be (x₂, y₂). Now confirmed a
   third time, on the scan. Reproduced as printed. Caleb's call, as before.
2. **Fig 15-15's midpoint label is set with solidi, not built-up fractions.**
   Unchanged from the build, and unavoidable: a `\frac` rule is a filled
   rectangle in the PDF, so the audit reads it as geometry inside the label's
   own box. The solidus form runs about two and a half times as wide as the
   book's stacked fraction, so it cannot be tucked beside P₂ the way the book
   tucks it; it is lifted clear above instead. If `check_labels.py` ever
   learns to ignore vector ink wholly contained in a label's bounding box,
   revert to `\dfrac` and set it back in the book's position.
3. **Fig 15-18's 0 is above left of the origin; the book sets it below left.**
   The origin lies inside this circle, and the audit approximates each
   quarter-arc by its chord, which cuts about 0.29 r inside the true arc —
   almost exactly the clearance the book leaves. Below left therefore reads as
   a collision. Cheap fix if wanted: teach the audit to flatten arcs to more
   than four chords.
4. **Fig 15-13's CD sits at y = −1.5 rather than the book's ≈ −1.25.** At this
   trim a label set above a point at −1.25 runs back over the axis of
   abscissas. The three quantities the text asserts about the figure (CD
   parallel to that axis, CD = |x₂ − x₁| = 3, C and D on opposite sides of the
   axis of ordinates) are all preserved and constrained.
5. Labels are inherently about twice as large relative to the drawing as the
   book's are, because a US-textbook figure is being reduced to a 145 mm trim.
   Most of the placement deviations above trace back to that one fact; it will
   recur in every chapter and may be worth a project-level decision (smaller
   `slab`, or larger figures) rather than per-figure workarounds.
6. Fig 15-3's three segments are drawn in the `key` weight while the book
   draws them at about the weight of the axes. Left as is — they are what the
   theorem is about, and the house semantics call for `key`. Flagging in case
   the convention should yield to the plate here.

---

## Transcription pass (2026-08-17)

Filled in all 53 `\XVtodo` spans from the photo PDF, pp. 265–279 = book
pp. 251–265, read at 150 dpi with 400–500 dpi crops for every exercise list,
every numeral and every footnote. `figures15.tex` and `tools/constraints/ch15.py`
were **not touched** — they arrived gate-green and still are.

### Gates

| Gate | Result |
|---|---|
| compiles twice clean | yes — no errors either run; only over/underfull-box warnings, all inside two-column exercise lists |
| `grep -ci todo ch15.tex` | **0** (macro definition deleted too) |
| `verify_figures.py 15` | **101/101** |
| `check_labels.py … 15` | **0 collisions**, 4 TIGHT (Fig 15-2 ×3, Fig 15-5 ×1 — eyeballed in the render at 110 dpi, all legible, accepted) |
| visual pass | all 25 pages rasterized; all 14 figure blocks / 19 figures looked at against their source plates |
| exercise numbers | every group re-checked against 400 dpi crops — see below |

### Structural judgment calls

1. **Numbered remarks needed a new environment.** Book p. 261 prints
   "*Remark 1.*" and "*Remark 2.*" in sequence, but `brumfiel.sty`'s `remark`
   hard-codes an unnumbered "Remark." Added a local `XVremark{n}` in the
   local-macro block (shared style file untouched, per the rules). The two
   genuinely unnumbered remarks (pp. 257, 262) still use the shared `remark`.
2. **Footnote markers are `*` and `†`, never numbers.** Added a local
   `\XVnote{…}` that blanks `\thefootnote` and emits `\footnotetext`, with the
   marker typed into the body text — the same device as ch02's `\IIstarnote`
   and ch09's `\IXstarnote`. This is what residual doubt 1 of the text review
   asked for: on p. 256 a `*` footnote and starred exercises *2/*3 share a
   page, and on pp. 259–260 the footnote falls back to `†` precisely because
   `*` is taken by the starred theorems. Both render correctly.
3. **"(Why?)" prompts** are set as the book sets them — inline, parenthesised,
   upright roman, no macro (text-review residual doubt 2). Five occurrences:
   three in the Theorem 15-1 proof, one in the p. 257 Remark, one in Case 3 of
   the Theorem 15-3 proof, plus the "(why?)" — lowercase in the book — in
   Case 1 of the Theorem 15-2 proof. **The lowercase one is deliberate, not a
   typo on my part**; verified at 400 dpi.
4. **Exercise Group 15-9 item 5** keeps its side condition on the same line
   after a semicolon, `2ax + 3ay − 6a = 0; a ≠ 0` (text-review residual
   doubt 3).
5. **The bare "or" lead-ins** before the cleared form of Eq. (15-4) on p. 261,
   and before the second circle form on p. 265, are set at the left margin on
   their own line, as printed (text-review residual doubt 4).
6. **Exercise Group 15-10 #1 sub-list** is lettered (a)–(h), then (k), (l) —
   the book's skip of (i) and (j) is reproduced with explicit `\item[(k)]` /
   `\item[(l)]` labels so it cannot be "fixed" by a later renumber.
7. Sub-lists inside exercise items (15-10 #1 and #2, 15-13 #3) use a plain
   `enumerate` rather than a nested `exlist` — `exlist` is declared depth-1 by
   `\newlist`, so it cannot nest.

### Exercise numbers — all thirteen groups spot-checked at 400 dpi

Counts unchanged from the text review: 15-1 (2), 15-2 (2), 15-3 (3), 15-4 (3),
15-5 (2), 15-6 (3), 15-7 (17), 15-8 (3), 15-9 (8), 15-10 (6), 15-11 (7),
15-12 (8), 15-13 (5). Every coordinate pair, coefficient and fraction was read
off a high-resolution crop, including: 15-7 #1's six points and #2's 4½/3;
15-9's eight equations; 15-10 #1's ten lines and #2's six point-pairs;
15-11 #4's four parallelogram vertices (−1, −18), (−13, −2), (11, −8), (−1, 8)
— re-cropped at 500 dpi because they are easy to misread; 15-12 #1–#6;
15-13 #3's five circles and #5's 16x² + 25y² = 400.

The book writes the endpoint pairs in 15-12 #2, #3, #4 with **no "and"**
between them — "the segment (−3, −7) (11, 17)". Reproduced as printed; it
looks like an omission but it is consistent across all three items.

### Residual doubts

1. **Exercise 15-7 #16, second point: `(−5, −7)` or `(−6, −7)`?** The digit
   sits in the gutter-side margin where the page curves away from the camera,
   and at 400 and 500 dpi it resolves as an ambiguous 5/6 glyph — the only
   character in the chapter I could not settle. Scans are no help: ch 15 is
   sparsely scanned by design and `sources/scan-index/` has **no entry for
   book p. 257**. Nothing internal disambiguates it either, since the exercise
   only asks for distances to the axes and either value is a sensible problem.
   **Transcribed as (−5, −7).** One glance at the physical copy settles it.
2. **Fig 15-14's doubled label is still Caleb's call** (open since the build,
   confirmed three times: plate, 400 dpi crop, scan). The book prints
   (x₂, y₁) at both P₂ and Q; P₂ should be (x₂, y₂). The prose I have now
   transcribed states "with the point Q (x₂, y₁) a right triangle P₁P₂Q is
   formed", so the running text and the figure now visibly disagree in the
   render — which strengthens the case for correcting the figure and noting it
   in the back matter. Not done unilaterally: the figure file is gate-green and
   out of this unit's scope.
3. **Page 25 of the standalone render ends with a two-line widow** — the tail
   of Exercise 15-13 #5 alone on a page. An artifact of the standalone
   chapter's page grid; it will reflow when `book.tex` assembles the chapter,
   so no `\pagebreak` hack was inserted. Worth a look in the assembled book.
4. **Descartes portrait plate**, book p. 250 / PDF 264: still outside this
   unit's range, still needs an owner. Caption reads "RENÉ DESCARTES
   (1596–1650) / Courtesy of *Scripta Mathematica*". Halftone — place as a
   plate, never redraw. (Repeated from §5 so it is not lost.)
5. This unit still owes the **second text review** the earlier review asked
   for: a fresh agent should diff the finished prose, not just its structure,
   against the source pages.
