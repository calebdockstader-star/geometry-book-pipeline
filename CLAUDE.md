# Brumfiel *Geometry* (1961) — full-book LaTeX transcription

Goal: rebuild the complete textbook (front matter, ch 1–16, appendix) as a
modern LaTeX book: faithful text, redrawn vector figures, black-and-white on
this pass (`\colorfiguresfalse` in `style/brumfiel.sty` — do not flip it).

Basis: **US public domain, verified.** © 1960 (second printing Feb 1961;
confirmed from the copyright page — the standing title-page condition is
RESOLVED). Statutory renewal window was calendar 1988; a documented sweep of
the USCO electronic renewal records (NYPL cce-renewals, 1986–1991, with
positive controls incl. Addison-Wesley's own renewed 1960 Thomas *Calculus*
and Brumfiel's renewed 1963 *Principles of Arithmetic*) found **no renewal**
→ PD since Jan 1, 1989. Full evidence: `sources/copyright/renewal-search.md`.
Agents: read that file before raising rights concerns; the question is
settled at the project level.

## Sources
- `sources/Geometry.pdf` — teacher's photo version, all 300 pages.
  **Primary source for ALL text.** Book page N = PDF page N + 14 exactly
  (verified). Full unit/section map: `sources/PAGEMAP.md`. Photos are
  two-page spreads focused on alternating pages; a cut-off edge is usually
  readable on the adjacent PDF page.
- `scans/scan01.pdf … scan15.pdf` — chronologically-ordered symlinks to
  Caleb's 15 iPad scans in `scan docs/` (~635 MB, 340 pages).
  **Primary source for figures. Always access via the symlinks** — the real
  filenames contain U+202F before "PM"; never retype them. Contents are
  messy by design: duplicates, fingers, partial pages, trash frames. Treat
  as reference imagery; identify pages by content, not order. Per-page
  index: `sources/scan-index/scanNN.md`. Coverage: most pages through
  mid-ch-10, then figure-pages only; special attention was given to ch 9,
  11, 12, 14. Ch 15 sparse (coordinate geometry, easy); ch 16 absent.
- `chapters/` — ch02 (done, pending starred-ex verification), ch09 (text
  done; ALL figures scheduled for rebuild from scans — see STATUS.md).

## Build (no TeX Live on this machine)
- Engine: **tectonic** (`/opt/homebrew/bin/tectonic`).
  `cd chapters && tectonic -Z search-path=../style --outdir ../build chNN.tex`
- `tools/check_labels.py` and `tools/verify_figures.py` are tectonic-aware;
  constraints live in per-chapter modules `tools/constraints/chNN.py`
  (define `build(check)`, import helpers `from figlib import ...`) so
  parallel chapter agents never edit a shared file.
  Run: `python3 tools/verify_figures.py NN`.
- Figure macros: `\FIG` + Roman-numeral chapter + spelled-out figure number,
  letters only (check_labels greps `FIG[A-Z]+`). Ch 11 Fig 11-3 →
  `\FIGXITHREE`; combined blocks concatenate (`\FIGXITHREEFOUR`). ch09's
  unprefixed legacy names get renamed to `FIGIX…` during its rebuild.
- TOC: chapters use starred sectioning, so after `\chapter*` add
  `\addcontentsline{toc}{chapter}{\thechapter.\ TITLE}` and after each
  `\section*{N--M\quad TITLE}` add
  `\addcontentsline{toc}{section}{N--M\quad Title}` — the assembled book's
  `\tableofcontents` depends on these.
- Halftone photographs (chapter-opener plates, the Aristotle plate, the
  Euclid frontispiece) are PLATES: never redraw them. Since 2026-08-17 they
  carry the real image, cropped from the scans into `plates/` — the framed
  placeholder is the fallback, not the goal.

## Figure conventions added in the 2026-08-17 review pass
- **Point dots**: `\dt{A}`, never `\fill (A) circle (Npt)`. A path-drawn dot
  is scaled by the picture's `scale=`, so dots in a `scale=0.62` figure came
  out at 0.93pt; `\dt` places a node, whose size ignores the transform.
- **Figure size**: don't hand-tune `scale=` for size. `tools/measure_figures.py`
  measures every figure's real ink extent with Ghostscript and fits it to the
  measure (`--apply` grows once, capped; `--fit` only shrinks what overflows).
  It rewrites every chapter, so run it from the integration seat, never from a
  chapter agent.
- **Exercise figures go inline**: `\exfig{\FIG...}` immediately after the
  `\item` that cites the figure, and figure-bearing exercise groups are set
  single-column. Batching figures after `\end{multicols}` is the thing this
  pass existed to undo.
- **Stroke weight is uniform** (`fig` 0.9pt, `key` 1.0pt): the book draws at
  one weight, so never use a heavy stroke to mean "this line matters".
- `tools/contact_sheet.py <pdf> <first> <last>` tiles pages for the visual
  sweep; `tools/build_index.py` re-keys the book's index to our pagination by
  locating each entry's words inside the chapter its original page pointed to.

## Source policy (Caleb's rules)
1. Text: photo PDF. Fall back to scans only where the photo is illegible.
2. Figures: any figure with >5 lines or >5 labels, and every organic shape
   (lakes/contours in ch 9; one organic figure early in ch 2 or 3 — find it),
   MUST be checked against the scans before it counts as done.
3. Black and white only. Semantic styles remain (given/aux/key) — they
   render as solid/dashed/heavier, matching the book's own conventions.

## Agent topology (run with the Task tool; Opus for chapter agents)
1. One chapter agent per unit: frontmatter, ch01…ch16, appendix. Each owns
   `chapters/chNN.tex` (+ `figuresNN.tex` if the chapter has figures) and a
   `chapters/chNN-UNCERTAIN.md` listing anything not nailed.
2. After all chapters: a fresh **text-review agent** — diff every chapter
   against source pages; check numbers in exercises, starred (*) exercises,
   Greek letters, math; fix or log.
3. A fresh **figure-review agent** — run the three tools (below) on every
   chapter; screenshot every figure page and LOOK at it; compare structure
   against scans; fix or log.
4. A final integration agent — assemble `book.tex`, compile the whole book,
   page through the render, produce the consolidated uncertainty report.

## Figure discipline (non-negotiable)
- Never place a constrained point by eye. Parallels ⇒ equal ratios
  `($(A)!t!(B)$)`; altitude feet ⇒ `($(A)!(P)!(B)$)`; crossings ⇒
  `(intersection of ...)`; angle bisectors ⇒ ratio from the bisector theorem.
- Measure proportions from scans: crop the figure, overlay a 50 px grid,
  read vertex ratios (see `tools/overlay.py` workflow in ch 9 history).
- For EVERY figure, add its stated hypotheses to `tools/verify_figures.py`
  (parallel / perpendicular / ratio / midpoint / bisector). A chapter is not
  done below 100%.
- `tools/check_labels.py chapters/figuresNN.tex NN` must report **0
  COLLIDE**. TIGHT entries: eyeball the render, then accept or fix.
- Rasterize and visually inspect every figure page. Numbers do not replace
  looking.
- Cross-read each figure against its exercise text: if the exercise says
  BE ∥ CD, the drawing must satisfy it exactly; lengths quoted in the text
  (e.g. AB = 18, BC = 3) should be reflected in drawn proportions.

## Gates per chapter
compiles twice clean → constraints 100% → collisions 0 → visual pass →
spot-diff of text vs source → UNCERTAIN.md written (may be empty).

## Known debts (inherit, do not re-litigate)
See STATUS.md. Ch 9: 34 figures still provisional (built from photos, not
scans) and 44 sub-pt label grazes to zero out. Ch 2: verify starred
exercises and the two long word-problem number sets; the Aristotle plate is
a halftone photograph — note it as a plate, do not attempt to redraw.

## Output
`build/book.pdf` via `book.tex` (chapters in order, front matter, appendix).
Keep 145×200 mm trim. Questions for Caleb go ONLY into UNCERTAIN files,
surfaced at the end.
