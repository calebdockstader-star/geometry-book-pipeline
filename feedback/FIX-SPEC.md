# Figure repair pass — spec for chapter agents (2026-08-17)

Caleb reviewed the whole book against his physical copy and photographed
every figure he wants improved, together with the book page it should be
based on. 149 photos, indexed in `feedback/index_a*.md`. His verdict:

> "overall you did a really good job at capturing the majority of the figures
> well and as far as i can see the text is perfect. most of my feedback is
> nitpicky for the figures, but a lot of it is genuinely substantial and all
> of it should be implemented to make sure it looks good."

**The text is signed off. This pass touches figures and figure placement
only.** Do not re-transcribe prose, do not "fix" the book's own errata (they
are deliberate — see `OPEN-QUESTIONS.md` §3).

## Rights — settled, do not re-litigate

The book is © 1960 and has been in the US public domain since 1 January 1989:
the statutory renewal window (calendar 1988) was swept in the USCO's own
electronic records with positive controls, and no renewal exists. Evidence:
`sources/copyright/renewal-search.md`. Caleb owns two physical copies. If you
find yourself about to raise a rights concern, read that file instead.

***

## 1. What has already been done globally — do NOT redo it

These landed before you started. Inherit them; don't undo or duplicate them.

* **Point dots are now nodes.** `\fill (A) circle (1.4pt)` was scaled by the
  picture's `scale=`, so dots in a `scale=0.62` figure printed at 0.93pt.
  All 170 sites became `\dt{A}`, a node of fixed 3.2pt diameter that ignores
  the coordinate transform. **Use `\dt{X}` for every new point dot.**
* **Every figure has been re-fitted to the measure.** Each figure's true ink
  extent was measured with Ghostscript and its `scale=` multiplied so it grows
  into the room it has (cap ×1.30; ×1.45 in ch09, which Caleb singled out as
  too small). Don't hand-tune `scale=` for size alone — if a figure still
  looks wrong, fix its geometry.
* **Label clearance tightened** (`outer sep` 3.4pt → 2.2pt globally; the
  chapter-local 4.4–5.2pt overrides in ch06/08/09/11/13 → ~2.9pt), because
  Caleb asked for labels "tightened to their thing that they are labeling."
* **Stroke weights retuned**: `fig`/`given` 0.7pt → **0.9pt**, `key` 1.15pt →
  **1.0pt**. The book draws at one weight; our base read too light and `key`
  too heavy. Don't reintroduce heavy strokes to mean "important".
* **The chapter-head figure legend is retired** (`\figurekey` is a no-op).
* Corollary heads are italic now; that is intended.

***

## 2. THE BIG ONE — put exercise-group figures inline

Caleb's headline complaint:

> "MY BIGGEST piece of feedback is that for the exercise groups, the figures
> were not placed inline with the text like they should be. all of the
> exercies came, then after all of the pages were included in one group. In
> earlier points in the chaper, you have figurges showing up mainline with the
> text, and it needs to be the same way in the exercise groups according to
> how it is in the book for all chapters."

Right now a typical group looks like this — every figure dumped after the list:

```latex
\exercisegroup{6--5}
\begin{multicols}{2}
\begin{exlist}
\item In Fig.~6--17, if ... ?
\item In Fig.~6--18, if ... ?
...
\end{exlist}
\end{multicols}

\FIGVISEVENTEENEIGHTEEN

\FIGVININETEENTWENTY
...
```

It must become this — each figure immediately after the exercise that cites it:

```latex
\exercisegroup{6--5}
\begin{exlist}
\item In Fig.~6--17, if ... ?
\exfig{\FIGVISEVENTEEN}
\item In Fig.~6--18, if ... ?
\exfig{\FIGVIEIGHTEEN}
...
\end{exlist}
```

### Rules

1. **`\exfig{\FIG...}` goes inside the list**, on its own line, directly after
   the `\item` whose text names that figure. `\exfig` (defined in
   `style/brumfiel.sty`) pulls the figure out of the list indent so it centres
   on the full measure. It has been compile-tested; exercise numbering
   continues correctly across it.
2. **Drop the `multicols` wrapper from any exercise group that contains a
   figure.** A figure in a 52 mm column would print smaller than the book's
   own, and Caleb wants them bigger, not smaller. Exercise groups with **no**
   figures keep `\begin{multicols}{2}` exactly as they are.
3. **Split combined figure macros.** `\FIGVISEVENTEENEIGHTEEN` holds Figs 6-17
   and 6-18 side by side because they used to be batched. If the two figures
   are cited by *different* exercises, split the macro in `figuresNN.tex` into
   `\FIGVISEVENTEEN` and `\FIGVIEIGHTEEN`, each a full-width `bkfigure` with
   its own `\figcap`. Keep them combined only when **one** exercise cites both
   (e.g. "in Figs. 6-17 and 6-18"), or when the book itself prints them as one
   captioned unit — e.g. `(a)`/`(b)` parts under a single figure number.
   * When you split, drop the now-unneeded `minipage`/`\hfill` scaffolding and
     let each picture stand at full width; then re-run the size fit for that
     chapter (§5) so the freed width is actually used.
   * Update `tools/constraints/chNN.py` if it keys on a macro name.
4. **Placement when a figure is cited by several exercises**: put it after the
   **first** exercise that cites it.
5. **Figures not cited by any exercise** (chapter-body figures) stay exactly
   where they are — those are already inline and Caleb is happy with them.
6. Keep the figure *number order* sane: if following rule 4 would print Fig
   6-20 before Fig 6-19, prefer the order the book prints them in; check the
   source page.

***

## 3. Fix the figures Caleb photographed

Your chapter's entries are in `feedback/index_a*.md` (grep for your chapter).
Each entry names a photo in `feedback/small/<name>.jpg` — **look at the
photos with the Read tool; do not work from the index text alone.** Photos
come in pairs: one of our render, one of the book page. Some chunks are
render-first, some book-first; several are sideways (rotations are noted in
the index — crop/rotate with PIL into your scratch dir if it helps).

`sources/Geometry.pdf` (book page N = PDF page N+14) and the iPad scans in
`scans/scan01..15.pdf` (indexed in `sources/scan-index/`) remain available and
are higher resolution than the phone photos for fine detail.

### The recurring defect classes — sweep your whole chapter for these, not just the photographed figures

Caleb: *"most of your misses were missed angle arcs (the arcs that represent
angles), a few missed lines here and there, a lot of lines that were slightly
over or underdrawn or miss represented as arrows, a few that were completely
wrong and missed the point, diagrams that appeared more cluttered or
intersecting in places they shouldn't."*

1. **Missing angle arcs.** By far the most common defect (7-8, 7-18, 7-29,
   7-32, 8-29, 9-12, 6-97…6-102, 12-22 …). Wherever the book strikes an arc to
   name or mark an angle, strike one. Where the book uses graduated radii for
   nested angles, graduate them. Where it uses two arcs for a second congruent
   pair, draw two.
2. **Missing construction arcs.** Compass work drawn as a plain × or a solid
   tick instead of two crossing dashed arcs (7-23, 7-30, 9-50).
3. **Arrowheads where the book has a dot or a plain junction** — endemic in
   ch13/ch14 (13-6, 14-8, 14-16a, 14-17, 14-38). The book marks a point with a
   heavy dot, not an arrowhead. Use `\dt{}`.
4. **Missing lines.** Whole segments absent, so the figure stops making its
   point: 6-20 (DA, CB), 6-25 (chords CF, FD), 6-26 (below-line stubs), 6-109
   (AB, ED), 7-30 (bisector ray AQ), 14-42 (near base chords).
5. **Over/under-drawn lines.** The book overshoots some rays past their labelled
   point and stops others dead. Match it: 7-28 (l must not extend left of A;
   P/P′ must overshoot), 13-12 (perpendicular bisectors grossly over-extended),
   12-14 (rays running past the brace).
6. **Hidden-line dashing in the 3-D chapters** — ch14's biggest problem, and
   Caleb flagged it by name: *"the spacial geometry stuff is just hard to
   capture well, and i noticed your biggest issue was with representing the
   dotted lines going behind objects."* 14-22's dashing is fully inverted;
   14-17's hidden run stops early; 14-31/14-35 dash the wrong edges. Work out
   which edges are genuinely occluded and dash exactly those.
7. **Labels detached from what they label**, sometimes colliding (6-127, 7-21,
   7-32, 8-29, 9-10). The global clearance change helps; place the remainder
   by hand, close to their point, in the free quadrant.
8. **Clutter / things crossing that shouldn't** (13-17's ticks collapsing into
   a blob, 12-14's ray thicket, 14-9's tangle, 14-29/14-30 merging).
9. **Wrong shape entirely** — a rectangle where the book draws an irregular
   quadrilateral (6-21), a nested circle where the book draws two equal
   circles offset (13-9), a 90° sector where the book draws 65° (12-14),
   a mirrored angle (6-98/6-99/6-100), the wrong hexagon rotation (11-11).

### Figure discipline still applies (project rule, non-negotiable)

Never place a constrained point by eye. Parallels ⇒ `($(A)!t!(B)$)`;
perpendicular feet ⇒ `($(A)!(P)!(B)$)`; crossings ⇒ `(intersection of ...)`;
midpoints ⇒ `($(A)!0.5!(B)$)`. Every hypothesis stated in the exercise text
must hold exactly in the drawing, and must be asserted in
`tools/constraints/chNN.py`. If you add or reshape a figure, add its
constraints too.

***

## 4. Specific decisions Caleb made (apply if they touch your chapter)

* **Ex. 15-7 #16** — the second point is **(−5, −7)**. Confirmed. (ch15)
* **Fig 9-41** — the apex label is **C**, not C′. Confirmed. (ch09)
* **Fig 13-17** — *"YOU DID THIS CORRECT BESIDES THE 1 TICK NOT BEING
  PERPENDICULAR TO THE LINE CA."* Make the single tick mark perpendicular to
  CA. (ch13)
* **Figs 12-28 / 12-29 / 12-30 and 9-48** — revert to the book's schematic
  proportions rather than drawing the quoted lengths exactly, so the drawing
  doesn't give the exercise's answer away.
* **Pictorial line art** (Fig 1-23 hand, 3-15 three men, 4-1 boy with spear,
  5-1 man pacing, 14-2 jet and car) — Caleb wants all of it present and
  faithful. These are being handled centrally as scan crops; **leave them
  alone**, but do not delete their placeholders.

***

## 5. Gates — a chapter is not done until all of these pass

Run from the project root unless noted.

```
cd chapters && tectonic -Z search-path=../style --outdir ../build chNN.tex   # twice, clean
python3 tools/verify_figures.py NN          # must be 100%
python3 tools/check_labels.py chapters/figuresNN.tex NN   # must be 0 COLLIDE
python3 tools/measure_figures.py --fit      # only if you split/reshaped figures
```

Then **rasterise every page you changed and LOOK at it** —
`pdftoppm -r 130 -png -f P -l P build/chNN.pdf out` and Read the image.
Numbers do not replace looking; that is how these defects got through the
first time.

Finally, append what you changed (and anything you could not settle) to
`chapters/chNN-UNCERTAIN.md`. Questions for Caleb go there, nowhere else.
