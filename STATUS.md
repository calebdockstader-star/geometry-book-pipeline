# Status — 2026-08-17 — COMPLETE (figure review pass)

**`build/book.pdf` — 526 pages, 145×200 mm, compiles twice clean.**

Second full pass, driven by Caleb's review of the first build against his
physical copy: 149 photographs of figures needing work, each paired with the
book page it should be based on, plus his answers to every open question.

## What this pass changed

| Area | Change |
|---|---|
| **Exercise figures** | **300+ figures moved inline**, each directly after the exercise that cites it, as the book sets them. Figure-bearing exercise groups are now single-column at full measure; figure-free groups keep two columns. |
| **Combined macros** | **85 split into ~200** single-figure macros. This, not scaling, is what fixed ch09: Fig 9-23 went from 1.3 cm to 5.2 cm of drawn width once it stopped sharing a line with six other figures. |
| **Point dots** | All 170 path-drawn dots became `\dt{}` nodes. A path dot is scaled by the picture's `scale=`, so dots in a 0.62-scale figure printed at 0.93 pt; nodes ignore the transform, so every point in the book is now one size. |
| **Figure size** | Every figure measured by real ink extent (Ghostscript bbox) and fitted to the measure. Median figure now sits at **0.47 of the measure** — the book's own proportion is ~0.48. |
| **Stroke weight** | `fig` 0.7→0.9 pt, `key` 1.15→1.0 pt, and ch09's 32 `key` strokes retired outright. The book draws at one weight; ours read too light against it while `key` — a survivor of the abandoned colour edition — read too heavy. |
| **Labels** | Clearance tightened book-wide and in the five chapters that had raised it locally. Floor is the 3.2 pt dot; below that a label lands on the point it names. |
| **Plates** | All 8 halftones (Euclid, Hilbert, Pythagoras, Archimedes, Aristotle, Gauss, Lobachevsky, Descartes) now print the real image, cut from Caleb's own scans. |
| **Line art** | All 6 pictorial figures (1-23, 3-15, 4-1, 5-1, 7-17, 14-2) are scan crops, replacing 3 framed placeholders and 3 stylised tracings. |
| **Back matter** | Errata appendix added (policy 1.1(b)); the book's own index transcribed and **re-keyed to this edition's pagination** — 91% of entries located by their own words in the chapter their original reference pointed into. |

## Gates at delivery

- `python3 tools/verify_figures.py` → **2298/2298 constraints hold**
- `check_labels.py` → **0 collisions** in 14 of 15 figure files; **2 accepted
  grazes** in ch04 (Figs 4-10/4-12, label `B′` — the arc crosses the label's
  metric box, not the glyph, and the book's own plate grazes identically).
  This is stated rather than rounded to zero.
- compiles twice clean; all 20 standalone unit PDFs build clean
- **full visual sweep**: all 526 pages read as 33 contact sheets
- placeholder grep (`pending{`/`todo{`) → empty

## A verification hole found and closed

Fig 6-110 drew a "right angle" measuring 66° and passed a 100 % gate. The
cause was not the figure: ch06's constraint reader could not parse tikz
projection syntax, so **every dropped perpendicular in the chapter was
silently unchecked**. The reader now understands it, the foot is derived
rather than placed, and the perpendicularity is asserted.

Note for future work: ch06 is the only chapter whose constraints are read
from the tex. The other fourteen hard-code their coordinates, so a figure
edited without updating its constraint module would still report green. That
is pre-existing architecture, not a regression, but it is the weakest link in
the gate.

## Known, deliberate departures

- Single-column exercise groups cost pages (ch01 20→35, ch08 24→34; book
  465→526). It is the price of full-width inline figures at this trim.
- Ex Gp 6-14 #8 read `DE ≅ AC` against the book's `DE ≅ EC`; ours was the
  transcription slip, verified at 260 dpi, and is corrected in place.
- The index stops mid-R: book p.287 was never photographed. See
  OPEN-QUESTIONS.

Copyright: **US public domain since Jan 1, 1989** — verified with positive
controls; evidence in `sources/copyright/renewal-search.md`.

Tooling added this pass: `tools/measure_figures.py` (ink-extent fitting),
`tools/dots_to_nodes.py`, `tools/build_index.py` (index re-keying),
`tools/contact_sheet.py` (visual sweep). Conventions in `CLAUDE.md`.
