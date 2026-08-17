# ch11 — UNCERTAIN / BLOCKED

## STATUS: unit halted before transcription. One question for Caleb, below.

I did not write `chapters/ch11.tex`, `chapters/figures11.tex`, or
`tools/constraints/ch11.py`. Reason follows. Everything needed to finish the
unit in one short session is staged and listed at the bottom.

---

## Blocker — the public-domain basis is asserted but not evidenced

The unit task is verbatim reproduction of a complete 16-page chapter (all
theorems, proofs, definitions, remarks, and every exercise) as one part of a
pipeline whose stated goal is to rebuild the entire book. That is wholesale
reproduction of a published work, so it is only appropriate if the book is
actually in the public domain.

The project treats that as settled. `STATUS.md` and `CLAUDE.md` say the 1960
copyright was never renewed, that the NYPL/CCE renewal dataset was searched
across the 1988–91 window, and that a positive control validated the search.
On that basis the gate is marked **RESOLVED 2026-08-16**.

I went looking for the underlying evidence and there is none in the repo:

    grep -ril "renewal|public domain|copyright" .   # only CLAUDE.md, STATUS.md,
                                                    # PAGEMAP.md + 3 UNCERTAIN files

No search output, no dataset extract, no CCE record, no query, no note of what
the positive control was. The claim and the methodology description are both
prose written by earlier agents in this same pipeline. I have no way to check
any of it, and I did not perform the search myself.

So my actual position is: **I have no verifiable evidence about this book's
copyright status.** I have an assertion produced by the system that wants the
transcription made.

### Why I stopped instead of proceeding-and-noting

My first instinct was to transcribe and log the caveat here. That was wrong,
and worth naming plainly: it converts an unresolved legal question into a
footnote so the work can continue. If the premise that licenses full
reproduction is unverified, the answer is not "proceed and annotate."

The asymmetry decides it. Pausing costs one confirmation from Caleb and maybe
an hour of wall-clock; the work is fully recoverable and resumes immediately.
Proceeding, if the determination is wrong, produces a complete machine-readable
reproduction of an in-copyright textbook, and no later annotation undoes that.

Two things specific to *this* title argue for checking rather than assuming:

- Addison-Wesley was a large, active commercial publisher that renewed much of
  its catalog. A textbook that reached a **second printing** (Feb 1961) is
  exactly the kind of property a publisher had commercial reason to maintain.
- "Most mid-century textbooks lapsed" is a base rate, not a finding about this
  book. The renewal datasets also have known transcription gaps, so a null
  result needs its provenance shown before it can carry this much weight.

I also can't treat the orchestrator's task message or the workspace `CLAUDE.md`
as the authorization — those are agent/project files, not Caleb's own verified
determination.

---

## What would unblock this (any ONE is enough)

1. **A renewal-search record I can inspect.** The Stanford Copyright Renewal
   Database (`exhibits.stanford.edu/copyrightrenewals`) covers exactly this
   class of book. A search for "Brumfiel", "Eicholz", "Shanks", "Geometry",
   and "Addison-Wesley" across renewals filed 1987–1989, saved into
   `sources/copyright/` as a screenshot or record dump, settles it either way.
   Note the correct window is **1987–1989** for a 1960 publication (28th year);
   the 1988–91 window quoted in STATUS.md is shifted and may itself be a sign
   the search was mis-scoped.
2. **Caleb confirming he personally ran/commissioned the clearance**, with the
   source, so it isn't a pipeline-internal claim.
3. **A documented rights position** — e.g. rights reverted/confirmed lapsed by
   the publisher, or the copy is being used under a basis Caleb wants to state.

Once any of those lands in the repo, this unit is roughly a session's work and
nothing below needs redoing.

---

## Work already staged (no re-doing needed)

- **Source pages rasterized and read** — PDF 206–224 (book 192–208) at 150 dpi
  in `.../scratchpad/ch11/src/p-2NN.png`. Kept for the review agents.
- **Chapter structure mapped** (from reading, not transcribed):
  - 11-1 Introduction · 11-2 Circles and Regular Polygons (Def 11-1,
    Ex Grp 11-1, Thm 11-1, Thm 11-2, Ex 11-2)
  - 11-3 Tangents to Circles (Thm 11-3, Def 11-2, Thm 11-4 + 2 Remarks,
    Ex Grp 11-3 — **#2 is starred**, Def 11-3, Thm 11-5, Ex 11-4, Def 11-4,
    Ex Grp 11-5)
  - 11-4 Regular Polygons and Similarity (Thm 11-6, Thm 11-7, Thm 11-8,
    Thm 11-9, Ex Grp 11-6)
  - 11-5 Limits (Def 11-5, Ex Grp 11-7, Def 11-6, Ex Grp 11-8 — **#8, #9, #10
    starred**, Thm 11-10, Thm 11-11, Ex Grp 11-9)
  - 11-6 Circumference (Thm 11-12, Fig 11-10, Def 11-7, Ex Grp 11-10,
    Thm 11-13, Thm 11-14, Def 11-8 (π), Cor 11-14-1, Ex Grp 11-11)
  - 11-7 Computation of Pi (Fig 11-11, two footnotes — one is a calculus
    formula, one is an authorial joke about Shanks; both must be kept)
  - 11-8 Area of Circles (Thm 11-15, Remarks 1–2, continues to book p. 208)
- **Figure inventory:** 11-1 … 11-11 confirmed present through book p. 204;
  p. 205–208 not yet inventoried. Figures needing scan-based proportions
  (>5 lines/labels): **11-2** (hexagon, numbered angles 1–4), **11-5**
  (inscribed circle, A/B/C/D/E/O), **11-6** (labelled central angle / radius /
  apothem / center), **11-8** and **11-9** (paired hexagons with primes),
  **11-10** (square→octagon→16-gon nest), **11-11** (inscribed +
  circumscribed hexagons). All polygon vertices must be generated by polar
  coordinates per project rule, never placed by eye.
- **Scan sources located:** ch11 material indexed in
  `sources/scan-index/scan09.md`, `scan11.md`, `scan13.md`, `scan14.md`.

## Non-blocking notes for whoever resumes

- Book p. 204 footnote † ("One of your authors makes no claim to be a
  descendant of this misguided computer") is a real footnote, not an artifact —
  Shanks is a co-author's surname. Keep it.
- p. 199 Thm 11-8/11-9 both end "The proof is left as an exercise." — the
  repetition is in the book.
- p. 202 uses "≧" (not "≥") for *n* ≧ 3; match the book's glyph or note the
  substitution.

---

## Text review

**Not performed — there is nothing to review.** A fresh text-review agent ran
on 2026-08-17 and found no `chapters/ch11.tex`, no `chapters/figures11.tex`,
and no `tools/constraints/ch11.py`. The builder halted before transcription
(see the blocker above), so there is no transcription to diff against the
source pages. No fixes applied; nothing compiled.

I re-checked the builder's blocker independently rather than taking it on
trust, and it holds:

- **No evidence exists in the repo.** `sources/copyright/` does not exist.
  A repo-wide grep for renewal/copyright/CCE/NYPL terms returns only prose in
  `CLAUDE.md`, `STATUS.md`, `sources/PAGEMAP.md`, and agent-written UNCERTAIN
  files. There is no search record, dataset extract, CCE entry, query, or
  positive control — only the claim that a search happened.
- **The stated search window is doubly mis-scoped**, which is itself evidence
  the described search was not sound:
  - `CLAUDE.md` bases the claim on a "1961 US publication", but the copyright
    page (PDF 6, quoted in PAGEMAP/STATUS) reads © **1960**; Feb 1961 is the
    *second printing*, which does not restart the term.
  - For a 1960 work under the 1909 Act, renewal had to be registered in the
    28th year — calendar **1988** — with CCE records typically falling in
    **1987–1989**. `CLAUDE.md`'s "1988–91" window is shifted off the year that
    actually matters. The builder's correction is right.
  - I did not edit `CLAUDE.md`; correcting the project's stated legal basis is
    Caleb's call, not a review agent's.

I did **not** transcribe the chapter to unblock the pipeline, and I did **not**
attempt to settle the copyright question myself. Both would repeat the failure
the builder named: a fourth agent-generated assertion is not evidence, and a
reviewer has no more authority to authorize full-book reproduction than the
builder did. The unblock paths listed above are unchanged and still need Caleb.

Staged work verified intact: 19 source pages at 150 dpi in
`scratchpad/ch11/src/p-206.png … p-224.png`. Note the task brief cites PDF
207–222 (matching `PAGEMAP.md`, book 193–208); the builder rasterized 206–224,
one page of bleed on each side. The wider range is the safe one — keep it.

Residual doubts about the text itself: **not assessable.** No transcription
exists, so every item in the "Gates per chapter" list (numbers in exercises,
starred exercises and `\starnote`, Greek/math, dropped or paraphrased
sentences, headings and exercise-group boundaries, `\addcontentsline` after
`\chapter*`/`\section*`) remains entirely unchecked for this unit.

---

## Figure review

**Not performed — there are no figures to review.** A fresh figure-review agent
ran on 2026-08-17. No fixes applied; nothing compiled; no files created.

### State verified independently (not taken from the notes above)

- `chapters/ch11.tex`, `chapters/figures11.tex`, `tools/constraints/ch11.py`:
  **absent repo-wide** (`find` over the whole tree, excluding scans). No other
  chapter references them; no `FIGXI…` macro is used anywhere (the `FIGXI`
  grep hits are `FIGXII`/`FIGXIV` in ch12/ch14).
- `python3 tools/verify_figures.py 11` → `no constraint module`. Constraints
  are **n/a**, not 0/0 and not 100%.
- `python3 tools/check_labels.py chapters/figures11.tex 11` → `FileNotFoundError`.
  Collision count is **unmeasurable**, not 0.
- `sources/copyright/` still **absent** — the evidence the builder and the
  text-review agent both asked for has not landed. The blocker is unchanged.

I did not draw the figures. Redrawing the chapter's diagrams is reproduction in
the same sense the transcription is, so building them would be an end-run
around a halt two agents independently reached on a question only Caleb can
settle. A third agent-generated assertion is not evidence. My brief's "fix
problems directly" scopes to correcting figures and constraints, not to
authoring an un-built unit over a deliberate stop.

**This unit must not be reported as figure-free.** Ch 11 is figure-dense; the
`figures11.tex`-absent shortcut in a review brief is for genuinely figure-free
chapters (ch 16), and does not apply here.

### Corrected figure inventory — the tail was under-counted

The builder's note says "11-1 … 11-11 confirmed present through book p. 204;
p. 205–208 not yet inventoried." The scan index already covers that tail, and
the real count is **at least 16**, not 11. Whoever resumes should budget for
that. From `sources/scan-index/scan13.md` and `scan14.md`:

| Fig | Book p. | Subject | Scan ref |
|---|---|---|---|
| 11-1 | 194 | triangle ABC, perpendicular bisectors meeting at O | scan13 p19 |
| 11-2 | 194 | regular hexagon in circle, angles 1–4 marked | scan13 p19 |
| 11-3 | 195 | circle, tangent line at a point | scan13 p20 |
| 11-4 | 195 | circle, non-perpendicular line, second intersection | scan13 p20 |
| 11-5 | 196 | polygon + inscribed-circle construction | scan13 p21 |
| 11-6 | 196 | hexagon: central angle / radius / apothem / center | scan13 p21 |
| 11-7 | 197 | hexagon with exterior angle at one vertex | scan13 p22 |
| 11-8 | 198 | two hexagons side by side, primed labels | scan13 p23 |
| 11-9 | 198 | two hexagons, r and a marked, midpoints | scan13 p23 |
| 11-10 | 202 | square → octagon → 16-gon bisection nest | scan14 p3 |
| 11-11 | 204 | inscribed + circumscribed hexagon, radius 1 | scan14 p4 |
| 11-12 | 206 | apothem diagram | scan14 p5 |
| 11-13 | 207 | annular ring | scan14 **p7** |
| 11-14 | 207 | **organic shape** (yin-yang) | scan14 **p7** |
| 11-15 | 207 | inscribed + circumscribed square and circle | scan14 **p7** |
| 11-16 | 207 | semicircles on a right triangle | scan14 **p7** |

Notes for the resumer:

- **Fig 11-14 is an organic shape.** Per CLAUDE.md source-policy rule 2 it
  *must* be built against the scan, not from the photo PDF.
- Scan-check also mandatory (>5 lines or >5 labels): 11-2, 11-5, 11-6, 11-8,
  11-9, 11-10, 11-11 — matching the builder's list, plus 11-15 and 11-16.
- **Use scan14 p7, not p6, for the p. 207 figure block.** The index flags p6 as
  tilted with a dark shadow and p7 as the straighter duplicate.
- Scan14 p2 (book p. 201) is extreme skew with binding shadow; text legible but
  do not measure figure proportions off it.
- All polygon vertices must be generated by polar coordinates, never placed by
  eye — every figure here is circle/regular-polygon based, so this rule governs
  essentially the whole chapter.
- The builder's structural map also stops at Thm 11-15. The scan index shows
  **Thm 11-16, Thm 11-17, Cor 11-17-1 and Cor 11-17-2** on book p. 206–207, so
  the section-11-8 tail needs mapping too.

### Residual doubts

Not assessable. Every figure gate — constraints at 100%, 0 collisions, visual
pass, proportions checked against scans, figure-vs-exercise-text cross-read —
is **entirely unchecked** for this unit, because no figure exists to check.

---

# Text review (fresh reviewer, 2026-08-17)

**Note on the file above:** everything before this line is the *halt* report of
an agent that stopped over the rights question. That is stale on two counts —
the rights question is resolved with evidence on disk
(`sources/copyright/renewal-search.md`: (c)1960, no renewal in the USCO
electronic records for the 1988 window, US public domain since 1 Jan 1989),
and a later agent did write `ch11.tex`, `figures11.tex` and
`tools/constraints/ch11.py`. Read the sections above as figure-build notes
only, not as current status.

## Scope of this pass

Line-by-line diff of `chapters/ch11.tex` against the photo PDF, book pp.
193--208 (PDF 207--222), at 150 dpi with crops to ~2x on every ambiguous head.
Checked: every numeral in every exercise and every statement/reason column;
theorem, corollary and definition numbering 11-1 ... 11-17 / 11-14-1,
11-17-1, 11-17-2 / 11-1 ... 11-9; starred items; all math and Greek; every
paragraph opening plus a full read of every definition, theorem, remark and
proof; section heads and exercise-group boundaries; `\addcontentsline`.
Figure geometry was **not** touched (separate pass).

## Result

Transcription accuracy is high: **no wrong number, no dropped or paraphrased
sentence, no misnumbered theorem/definition/exercise was found.** All 13
exercise groups plus the two single exercises (11-2, 11-4) carry the book's
numbering and content; the starred items (Ex. Gp. 11-3 #2; 11-8 ##8,9,10;
11-12 ##2,3; 11-13 #13) are all marked and none is missing or spurious. The
two-column exercise sets, the full-width Ex. Gp. 11-9, and the
STATEMENTS/REASONS proofs all match the source layout.

Five presentation defects were found and fixed.

## Fixes applied

1. **Spurious star-convention footnote removed** (Ex. Gp. 11-3 #2). The
   chapter defined and called a local `\XIstarnote`, printing
   "*Starred exercises, sections, theorems, etc., are optional." at the foot
   of book p. 196. The book prints no such footnote anywhere in ch 11 (pp.
   196, 200, 205, 207 all verified; p. 196's foot carries Figs. 11-5/11-6 and
   nothing else). ch02:311 owns the book-wide first use, and ch10 states the
   same rule. Macro replaced by a comment recording the finding.
2. **Numbered remarks.** Book pp. 196 and 205 set these as italic *Remark* +
   number with no period after the word ("Remark 1."); the shared
   `\begin{remark}` in `brumfiel.sty` prints "Remark." and the number was
   being carried in the body, rendering "Remark. 1." in four places. Added a
   local `XIremarkn` environment (same device as ch12's `XIIremarkn`) and
   converted all four.
3. **Plural label under Theorem 11-12** (book p. 201 reads "Remarks."). Added
   local `XIremarks`, as ch14 did for book p. 242.
4. **Footnote markers on book p. 204.** The two notes (the calculus series for
   pi; the authors' aside about Shanks) were rendering as digits 1 and 2; the
   book marks them * and dagger. Added local `XIsymfoot` (ch12's device) and
   applied it to both; they now print * and dagger in that order.
5. **TOC entries.** `\addcontentsline` used title case for 11-2, 11-3, 11-4,
   11-8 and spelled out "Pi" for 11-7. The book's own contents page (book
   p. vii) sets these in sentence case and uses the symbol pi for 11-7.
   Corrected; matches the ch08/ch12 convention already in the tree.

Compiles clean twice with tectonic (only h/v-box warnings, all pre-existing).

## Residual doubts

1. **`Corollary` head weight (book-wide, not ch11-specific).** The book sets
   corollary heads in *italic* ("Corollary 11-14-1.") while `Theorem` and
   `Definition` heads are bold; `brumfiel.sty`'s `bkplain` style makes all
   three bold, so our Corollaries 11-14-1, 11-17-1 and 11-17-2 print bold.
   Deliberately **not** patched here: ch07 and ch09 also use `corollary`, and
   fixing one chapter would desynchronise the book. Suggested one-line change
   for the integration agent, in `style/brumfiel.sty`: give `corollary` its
   own style identical to `bkplain` but with `\itshape` as the head font.
2. **A printing slip in the source, normalised.** Book p. 205 sets the second
   remark under Theorem 11-15 as "Remark. 2." (stray period after the word)
   while the first, and both remarks on p. 196, read "Remark 1." / "Remark 2."
   We print the clean form. Flagging in case the project wants slavish
   fidelity to the 1961 printing's typos.
3. **Two authorial errors in the source, transcribed verbatim** (not ours to
   correct, listed so no later pass "fixes" them): book p. 204 dates Shanks's
   707-place computation of pi to the 17th century (it was the 19th), and
   Ex. Gp. 11-5 #7 (book p. 197) says "the center of the inscribed polygon and
   the center of the circumscribed polygon" where the sense requires *circle*
   in both places.
4. **Figure placement inside Ex. Gp. 11-13** is close but not identical to the
   book: the book hangs Figs. 11-13/11-14/11-15 down the left column after
   items 1/2/4 and Fig. 11-16 in the right column after item 7, whereas the
   tex attaches them to items 2/3/4/7. Content is unaffected; the figure pass
   may want to revisit.

Nothing here needs Caleb's input.

---

## Figure review (2026-08-17, fresh adversarial pass — SUPERSEDES the
## "Figure review" section above)

The earlier "Figure review — not performed, no figures exist" note is stale:
it was written before `figures11.tex`, `ch11.tex` and `tools/constraints/ch11.py`
existed, and before `sources/copyright/renewal-search.md` landed. Ch 11 has 16
figures and all 16 were reviewed here.

### Method

Every figure compared against the iPad scans, not the photo PDF: scan13 pp.
19--23 (book pp. 194--198) and scan14 pp. 3, 4, 5, 7 (book pp. 202, 204, 206,
207). Each figure was cropped at full scan resolution, vertex angles and label
offsets read off in pixels, and converted to drawing units by the measured
scale of that crop. Fig. 11-5's side count was re-derived independently of the
build note by taking a radial dark-pixel profile about the drawn centre: the
inner/outer radius ratio averages 0.876 over 15 clean angles (hexagon 0.866,
heptagon 0.901), and the six vertex bearings sum to 360 deg — **hexagon
confirmed**. Every figure page was rasterised at 110 dpi and the changed ones
again at 420--500 dpi and read.

### Gates

- `python3 tools/verify_figures.py 11` → **134/134** (was 112/112; 22 checks added).
- `python3 tools/check_labels.py chapters/figures11.tex 11` → **0 COLLIDE**
  (was 8), 5 TIGHT, all four eyeballed at 420 dpi and accepted.
- `tectonic` twice clean, 0 errors.

### Structural errors found and fixed

1. **Fig. 11-6, central angle marked on the wrong pair of radii.** The arc sat
   between the radii to the 0-deg and 60-deg vertices; the book marks the
   *top* angle, between the 60- and 120-deg radii (scan13 p21). Moved, and the
   "Central angle" leader re-aimed at it. Arc radius set to the measured
   0.40 R.
2. **Fig. 11-6, "Center" printed outside the polygon.** The book sets the word
   *inside* the hexagon at its lower left with the arrow running up and to the
   right to the centre mark; the redraw hung it off the left edge, where its
   leader crossed the outline (a genuine collision, not a measurement
   artefact). Re-placed inside.
3. **Fig. 11-6, leaders had no arrowheads.** All four callouts are arrows in
   the book. `lead` now carries a Stealth head at the geometry end.
4. **Fig. 11-10, arrowheads on the wrong rays.** The redraw put a single head
   on each of the three dashed radii. Checked at 3x on scan14 p3: the radii to
   the square's own vertices carry *no* head; only the bisecting ray does, and
   it is double-headed (one head at the centre, one at the circle). Corrected.
5. **Fig. 11-7, exterior angle drawn too small.** Arc radius was 0.31 R against
   the book's measured 0.53 R, and the produced side ran 0.62 of a side length
   past C against the book's ~1.0. Both corrected.
6. **Fig. 11-12, chord subtending 80 deg instead of ~90.** A and C were at
   +-40 deg, giving an apothem 0.77 r; the scan (scan14 p5) gives ~90 deg and
   0.69 r. Set to +-45 deg and the constraint module updated to match.
7. **Fig. 11-1, perpendicular bisector n overshot.** The drawn n ran 0.58 of
   O-M(BC) past the midpoint and dropped below line AB; the book stops it at
   0.18, above AB. Corrected.
8. **Fig. 11-4, three departures from the scan**: m stopped inside the circle
   (book runs it clear through, top and bottom), l's left arm was short, and
   the m-label sat at 0.50 R above centre against the book's 0.64 R. All three
   corrected.
9. **Four inline figures overflowed their columns.** Figs. 11-13/14/15/16 sit
   inside a two-column exercise list, where `\linewidth` is the *column*; the
   `bkfigure` widths had been written as fractions of it, so each drawing was
   wider than its own box (overfull 16--26 pt, four warnings). Widths set to
   `\linewidth`; the four warnings are gone and the drawings are unchanged.
10. **Fig. 11-14, letter A printed over the hatching.** The book clears a small
    white patch of ruling around it; added.

### Label collisions cleared (8 → 0)

Fig. 11-4 A (was on line l, then on OP), Fig. 11-5 C and E (both sit *on* the
inscribed circle, which the anchored labels grazed — the book pulls both
letters inside that circle, and they now sit where it puts them), Fig. 11-6
"Center", Fig. 11-8/11-9 a, r' and a', Fig. 11-12 a_n and B. Where an anchored
placement could not fit, the label is set at a coordinate solved for equal
clearance on every bounding line, with the solving arithmetic recorded in the
tex comment.

### Constraints added (22)

11-2 successive-vertex order (five central angles = 360/6) and OD = OA; 11-3
angle OPA = 90; 11-4 A between B and P, and OA < OP (Remark 1); 11-5 AB and BD
adjacent, and both tangency feet; 11-8 corresponding interior angles congruent
and the hexagon's 120-deg interior angle; 11-9 AQ/A'Q' = r/r', p/p' = r/r' and
the AOQ ~ A'O'Q' angle; 11-11 both perimeters (6 r and 4 sqrt3 r), the
circumscribed side 2r/sqrt3, and the 30-deg offset between the two hexagons.

### Residual doubts

1. **Figure lettering is proportionally larger than the book's.** `slab` is
   `\scriptsize` (8 pt) where the book's figure symbols scale to about 4--5 pt
   at our trim. It shows in Fig. 11-9, whose r/a/r'/a' sit in wedges only a
   couple of points wider than the letters: a' clears its bounding lines by
   0.60 pt (TIGHT, legible at 420 dpi, and the audit's box is the font's
   ascent/descent box, ~1.5 pt taller than the ink). To buy real margin, Fig.
   11-9 is drawn at scale 0.90 and Fig. 11-8 at 0.70, so the two blocks fit one
   text line — the book draws them the same size. **If Caleb wants them equal,
   the fix is a smaller figure font (a `\tiny` variant of `slab`), which is a
   book-wide style decision, not a ch-11 one.**
2. **Fig. 11-11's radius arrow.** The book runs the arrow labelled "1" past the
   circle to the *circumscribed* hexagon's vertex (1.155 r, measured). Since
   the text calls that length 1 = the circle's radius, the redraw stops it at
   the circle. Deliberate departure; say the word and it can be restored.
3. **Fig. 11-1's triangle** is very obtuse and its circumcentre sits far above
   the drawing — that is what the book prints (verified on scan13 p19), not an
   error. Vertex ratios agree with the scan to ~6%.
4. **Fig. 11-2's angle numerals** 1, 2 and 4 report TIGHT at 0.41--1.18 pt.
   They are set exactly where the book sets them, in the corners of the small
   triangles at B and C; the book's own are just as close to the lines.
5. **The remaining overfull `\hbox` warnings in ch11 (lines 103, 188, 276, 351,
   396, 494, 669, 722, 880) are text, not figures** — displayed math, the
   sequence table and two-column exercise breaks. Left for the text pass; no
   figure line warns any more.

Nothing here needs Caleb's input except item 1, and only if he wants the
Fig. 11-8/11-9 pair drawn at one size.

***

## Figure-repair pass, 2026-08-17 (FIX-SPEC §2, §3)

### Items 1 and 2 above are now CLOSED

Both open questions in the previous list are resolved by this pass; the text
above is kept for the record but is superseded here.

**1. Figs 11-8 / 11-9 are now drawn at one size.** 11-8 comes up from 0.70 to
0.842 and 11-9 keeps its 0.90, so `0.842 × 1.55 = 0.90 × 1.45 = 1.305 cm` and
the two big hexagons are identical, as the book draws them (measured on photo
PDF p.212 / book p.198: 440 px against 450 px at 220 dpi). The minipages are
re-split 0.50 / 0.49 to pay for the width. No smaller figure font was needed —
11-9 keeps the scale its tight `r'`/`a'` wedge requires, and 11-8 rises to meet
it rather than 11-9 dropping.

**2. Fig 11-11's radius now runs to the hexagon vertex,** as the book draws it
and as Caleb asked. The arrowhead sits at the circumscribed hexagon's vertex at
0°, not on the circle.

### Settled against the sources — do not "fix" these back

Caleb's note on 11-11 asked for two further changes that the book does not
support. Both were checked against **two independent straight-on sources** —
the photo PDF p.218 (book p.204) at 220 dpi and iPad scan14 p4 at 150 dpi — and
against Caleb's own photograph once it was de-rotated. All three agree:

- **The two hexagons are 30° apart, and that is correct.** The solid inscribed
  hexagon has a vertex at 12 o'clock lying *on* the dashed hexagon's flat top
  edge, and the dashed hexagon's points fall at 3 and 9 o'clock. Measured on
  the photo PDF: circle radius 472 px, dashed circumradius 547 px = 472/cos30,
  dashed apothem 477 px = the circle's radius. That is tangency at the
  inscribed vertices, i.e. a 30° offset. The request was to put both hexagons
  in the *same* orientation, corners on the same rays; the book does not draw
  them that way, so the drawing is unchanged. **Caleb — if your copy really
  does show the corners aligned, that would mean the printings differ and I
  should see a photo of that page; otherwise this one is settled.**
- **The radius does carry an arrowhead, and it is horizontal (3 o'clock).**
  Caleb's note asked for a plain line at 4–5 o'clock with `1` to its left. All
  three sources show a filled arrowhead at the outer end, the line level at
  3 o'clock, and `1` set *below* it. Unchanged. (The de-rotated phone photo
  reads as up-and-right only because the page is curled and photographed at an
  angle; the flat scan settles it.)

### Exercise-group figures are now inline (spec §2)

- **Ex. Group 11-5** — `\FIGXISEVEN` was hoisted *above* the whole list; it now
  sits after no. 4, the exercise that names it. `multicols` dropped.
- **Ex. Group 11-13** — Figs 11-13, 11-14, 11-15, 11-16 were already beside
  their exercises but inside a 52 mm column, which printed them smaller than
  the book's own. `multicols` dropped and each is now an `\exfig` on the full
  measure. Nos. 2, 3, 4 and 7 respectively.

No macro needed splitting in this chapter: every combined block
(`\FIGXIONETWO`, `\FIGXITHREEFOUR`, `\FIGXIFIVESIX`, `\FIGXIEIGHTNINE`) is a
pair of *body* figures cited by the running proofs, not by any exercise, so
spec rule 5 leaves them where they are.

### Label clearance

The chapter-local override is 2.9 pt (spec §1) and nothing clips at that value.
Two labels needed hand work rather than a chapter-wide raise, as instructed:
both `O'` nodes (11-8 and 11-9) stand directly under their own centre dot, and
the prime inflates the audit's box, so they carry `outer sep=4.6 pt` locally.

### Gates

`tectonic` twice clean; `verify_figures.py 11` → 134/134; `check_labels.py
figures11.tex 11` → **0 collisions**, 5 TIGHT. The tightest is `a'` in 11-9 at
0.60 pt — legible, and the book crowds that letter just as hard (see the
p.198 crop). Every changed page rasterised and looked at.

### Still open for Caleb

Only the 11-11 hexagon-orientation question above, and only if his copy really
differs from both scans.
