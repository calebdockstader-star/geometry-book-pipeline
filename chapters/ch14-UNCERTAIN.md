# ch14 — Space Geometry (book pp. 236–250) — uncertainty log

Sources used: `sources/Geometry.pdf` PDF pp. 250–264 (all fifteen pages
photographed flat and fully legible — no page needed a scan fallback for
text); figures checked against `scans/scan15.pdf` pp. 3–19, which covers
book pp. 236–249 page-for-page.

Gates: compiles twice with no errors and no overfull \hbox; constraints
60/60; `check_labels` 2 COLLIDE (both the same unavoidable case, item 14);
every figure page rasterised and inspected.

---

## Text — printed oddities preserved verbatim

1. **Theorem 14–12 / the line under it (book p. 242).** The book prints
   `AB/A'B = BC/B'C'`. The first denominator is missing its prime — it
   should read `A'B'`. Confirmed at high zoom on both the photo (PDF 256)
   and scan15 p. 10. Transcribed **as printed**. Say the word and I will
   silently correct it.

2. **Definition 14–6 (book p. 244).** The book prints "a simple plane
   polygon $P_1P_2\ldots P_{n-1}$", then lists the edges as
   $P_1P_2, P_2P_3, \ldots$ — the subscript should almost certainly be $n$,
   not $n-1$. Confirmed on the photo (PDF 258) and scan15 p. 13.
   Transcribed **as printed**.

3. **Theorem 14–13 hint (book p. 244).** "Choose $C$ such that
   $\angle CAV \cong \angle BAV$." Both named angles have their vertex at
   $A$, which is not what the usual trihedral-angle proof does (one expects
   the angles at $V$). Read twice at 2.6× zoom; the letters are
   unambiguous. Transcribed **as printed**.

4. **Theorem 14–24 (book p. 249).** "The volume of a sphere of radius $r$
   is $\tfrac{4}{3}\pi r^3$." The fraction glyph is the one genuinely
   blurred spot in my page range — at maximum zoom the numerator could be
   read as 1 or 4. Set as $\frac{4}{3}$ on mathematical grounds. Worth one
   glance at the physical copy.

## Text — judgment calls (no content at stake)

5. The chapter title and the word *sum* in Theorem 14–13 each carry a bare
   `*` footnote in the book (not a numbered note). Reproduced with an
   unnumbered `\footnotetext` via the local `\XIVnote` macro.

6. **No starred (optional) exercises occur in this chapter**, so
   `\stex`/`\starnote` are not used. The asterisks in this chapter are the
   two footnotes above only.

7. Headings 14–4 and 14–5 carry a manual `\\` break, because
   "PERPENDICULAR LINES AND PLANES" and "POLYHEDRA AND POLYHEDRAL ANGLES"
   otherwise hyphenate across the measure ("AN-GLES"). Purely typographic.

8. `\begin{postulate}{VII--1}` is a new local environment (bold run-in
   label, roman body) defined in the marker block of `ch14.tex`, since
   `brumfiel.sty` has no postulate environment yet. Worth hoisting into the
   shared style file once another chapter needs it — Postulate Groups I–VI
   appear in ch 3–8.

## Figures — not fully nailed

9. **Fig 14–2 (jet aircraft + automobile) — the weak point of this unit.**
   This is a pictorial illustration with no geometric content; it exists
   only to show "sets of points that do not lie in a plane". I have drawn
   approximate line art of a swept-wing jet and a period sedan on a hatched
   ground line. The silhouettes are *not* a faithful copy of the original
   artwork — proportions, panel lines and styling all differ. **Question
   for Caleb:** accept the stand-in, have it traced properly from scan15
   p. 4, or treat it as artwork (framed placeholder + caption) the way we
   treat halftone plates?

10. **Fig 14–1, first object.** Two intersecting planes, drawn as two long
    crossing strips. The book's own rendering is hard to resolve even on
    the scan; the strip widths and the crossing angle are my reading of
    scan15 p. 3, not measured.

11. **Fig 14–12 (irregular polyhedron).** The book's facet layout is
    arbitrary and I have not copied it vertex-for-vertex — redrawn as a
    comparable irregular solid of the same silhouette and face count.

12. **Fig 14–26.** I read the book's flattened polyhedral angle as **four**
    triangles meeting at a point that lies on the boundary (a flattened
    tetrahedral angle, 4 faces ≈ 248°, so it visibly fails to encircle the
    point). At first glance it can read as six. Counted off scan15 p. 13 at
    5× zoom; a second pair of eyes would be welcome.

13. **Fig 14–31, 14–35, 14–42, 14–43 are schematic**, not measured: the
    prism's bases sit at the two plane levels (the book lets the solid poke
    slightly through), and the hatched interior face of 14–35, the
    inscribed pyramid of 14–42 and the "small pyramid" wedge of 14–43 are
    drawn to convey the idea at the book's proportions rather than copied
    point-for-point.

## Method notes for the figure-review agent

14. `check_labels` reports 2 remaining COLLIDE, both in Fig 14–10 and both
    of the same kind: the "π" glyph of $\pi_1^+$ / $\pi_2^+$ against **its
    own subscript**, which pdfplumber splits into a separate word. There is
    no placement that separates a letter from its own subscript, so these
    cannot be driven to zero without changing the notation. All
    label-vs-geometry collisions **are** cleared. Two TIGHT entries remain
    (Fig 14–13 "B" at 1.05 pt, Fig 14–25 "C" at 0.90 pt); both were
    eyeballed in the render at 200 dpi and are clean.

15. Beware when reading `check_labels` output: pdfplumber groups maths
    glyphs into "words" differently depending on what else is on the page,
    so `$P_1$` may appear as one word `P1` on one run and as `P` + `1` on
    another, and the label-vs-label count moves accordingly. Judge by the
    **`vs geometry`** lines, and confirm in the render.

16. Chapter 14 is drawn in a 2-D oblique projection, so most of its stated
    hypotheses (line ⟂ plane, dihedral angle, right angles in space) are
    *not* visible as such in the drawing — the book itself draws them as
    non-right angles, and a numeric check would be wrong to demand them.
    `tools/constraints/ch14.py` therefore checks only what an affine
    projection preserves: parallelism, collinearity/betweenness, ratios
    along a line, similarity ratios, plus the two genuinely face-on right
    angles in Fig 14–13. The reasoning is written at the head of that file.

## Boundary question

17. Book p. 250 (PDF 264) is the **René Descartes halftone plate** facing
    the Chapter 15 opener ("RENÉ DESCARTES (1596–1650), Courtesy of
    *Scripta Mathematica*"). Although p. 250 falls inside the page range I
    was given, it belongs to Chapter 15, so I have **left it out of ch14**
    and drawn nothing for it. It is a halftone photograph and must be
    handled as a plate by whoever owns ch15.

## Cosmetic, expected to disappear on assembly

18. The standalone render has stretched whitespace around Exercises 14–9
    and 14–10 (p. 15) and one `Overfull \vbox (7.8 pt)` at the page break
    near Fig 14–40. Both are page-breaking artifacts of setting the chapter
    on its own; they should resolve when the chapter is set in `book.tex`.
    No overfull `\hbox` remains.

---

## Text review

Fresh adversarial diff of `chapters/ch14.tex` against `sources/Geometry.pdf`
PDF pp. 250–264 (book pp. 236–249) line by line, with `scans/scan15.pdf`
pp. 3–19 used to settle every glyph the photo left ambiguous. Every paragraph
opening, all 24 theorems, all 9 definitions, all 4 postulates, all 17 exercise
headings and all 3 part headings were read against the page; 13
`\addcontentsline` entries present (1 chapter + 9 sections + 3 parts).
Recompiled twice, clean, no overfull `\hbox`.

### Fixes applied (2)

- **Theorem 14–12 (book p. 242).** The trailing sentence ("In Fig. 14–23, we
  would have …") is set *italic, inside the theorem block* in the book, not as
  a following roman paragraph. Merged into the `theorem` environment. Verified
  at high zoom on scan15 p. 10.
- **"Remarks." (book p. 242).** The book's run-in label is plural; the shared
  `\begin{remark}` in `brumfiel.sty` prints the singular "Remark." Added a
  local `XIVremarks` environment in the marker block (same pattern ch12 uses
  for its numbered remarks) and switched the one occurrence. The shared style
  file was not touched.

### Doubts closed (no change needed)

- **Item 4 above is resolved.** scan15 p. 19 shows Theorem 14–24 unambiguously
  as $\tfrac{4}{3}\pi r^3$. The photo's blur was the only reason for doubt; no
  need to consult the physical copy.
- **Exercise Group 14–17 #2** reads "oranges **3** in. in diameter" (the photo
  makes the digit look like an 8; scan15 p. 19 is unambiguous). The tex was
  already correct.
- Items 1, 2 and 3 above (the missing prime in `A'B`, the `P_{n-1}` subscript,
  and `∠CAV ≅ ∠BAV`) were each re-read on the scans at high zoom. All three
  are genuine printer's slips in the book and are correctly transcribed as
  printed. Every other number in the chapter — 14–1 … 14–24, 14–1 … 14–9,
  VII–1 … VII–4, exercise labels 14–1 … 14–17, "four right angles", "but five
  … regular polyhedra", "4 ft square", "factor of 8", "50¢ per dozen",
  $V/V'=l^3/l'^3$, $lwh$, $\tfrac13 Bh$, $4\pi r^2$ — matches the page.
- No starred (optional) exercises, sections or theorems occur in this chapter,
  so `\stex` / `\starnote` are correctly unused; the only asterisks are the
  chapter-title footnote and the *sum* footnote, both already handled.

### Residual doubts (typographic only, flagged not fixed)

- A roman sentence that the book runs on the same line as a theorem is set as
  a separate unindented paragraph here in three places: "Figure 14–7 may
  suggest a proof." (Thm 14–3), "See Fig. 14–16(a)." (Thm 14–7) and "See Fig.
  14–34." (Thm 14–18). Content and roman/italic contrast are right; only the
  line break and the extra leading differ. Left as house style — worth one
  decision from the integration agent so all chapters agree.
- The paragraph "A *polyhedron* is the set of points on a finite number of
  polygonal cells…" (book p. 244) is set outside `\begin{definition}` 14–6.
  The book runs it as the next paragraph of the same block; since definition
  bodies are roman, the rendered result is identical, but a purist would fold
  it in.

## Figure review

Fresh reviewer, 2026-08-17. 26 figure blocks (Figs 14–1 … 14–43) re-read
against the photo PDF (PDF pp. 250–264) and, for the crowded ones, against
scan15 pp. 3–19. Final gates: **97/97 constraints, 0 COLLIDE, 0 TIGHT**,
chapter compiles twice clean with no overfull hbox.

### Fixed — the drawing contradicted the book or its own text

18. **Fig 14–5 — hidden/solid inverted.** The stretch of $l$ *behind* the
    plane was drawn solid and the stretch above it dashed. On the page (and
    on scan15 p. 5) the line is solid below $\pi$, **dashed from the near
    edge up to $P$**, solid above $P$. Rebuilt with the crossing taken as
    `intersection of`; $P$ was also lowered so its label clears the far edge.

19. **Fig 14–5 — $l$ was not straight.** The three drawn segments did not lie
    on one line: $P$ missed the line through the two ends by 4.7°. The lower
    end is now derived from $P$ and the upper end, so $l$ is one line.

20. **Fig 14–14 — $m$ missed $P$.** Definition 14–3 says $l$ is perpendicular
    to *every* line of $\pi$ through $P$; the drawn $m$ passed 0.12 units
    above $P$. It now runs through $P$, and the **second line of $\pi$ that
    the book also draws through $P$** has been added (the book shows an X at
    $P$, not a single line). Plane widened to the book's flatter slant.

21. **Fig 14–15 — the figure did not match Theorem 14–6's hint.** Three
    defects: $l_1$ was drawn through $B$ but *not* through $P$; the segment
    labelled $m$ ran from $B$ instead of from $P$; and $Q$ did not lie on
    $BC$ (off by 0.32 units), although the hint places $D$… $Q$ on it and
    derives $AQ \cong A'Q$. Rebuilt: $l_1=PB$ and $l_2=PC$ radiate from $P$
    with the book's arrowheads at $B$ and $C$, $BC$ is drawn as the auxiliary
    (dashed) segment, $Q$ sits on it by construction, and $m$ is the ray $PQ$.

22. **Fig 14–24 — $P$ was a vertex, not a point of a side.** Definition 14–5
    takes the rays through *all points* $P$ of the polygon; the drawing had
    made $P$ a fifth vertex, so the polygon $P_1P_2P_3P_4$ read as a
    pentagon. $P$ now lies on side $P_4P_3$ by construction.

23. **Fig 14–7 — $m$ missed the four far corners** it is supposed to cut
    (0.044 units at the left-hand dot, ~1.2 pt on the page). $m$ is now drawn
    along the same step vector that places the corners.

24. **Fig 14–13 — the dashed rays were placed by eye.** The ray completing
    the line of $OA$ was 0.69° off the true opposite ray; it is now derived.
    The book's arrowheads on $OA$, $OB$, $r'$ and $r''$ were missing and have
    been added, as has **the dashed opposite ray of $r'$ inside $\pi'$**,
    which the book draws and the redraw omitted.

25. **Fig 14–37 — the "altitude" was not an altitude.** It was a copy of the
    lateral edge, i.e. parallel to the leaning edge $ec$, so it measured the
    edge and not the height. It is now a true vertical of the drawing, head
    on the top face's edge $B_1B_2$ and foot inside the base face, with the
    book's two tick marks; the constraint file checks all three facts.

26. **Fig 14–39 — the altitude was invisible.** With a symmetric base the
    apex, the base centre and the front vertex were collinear, so $h$, the
    hidden edge to the back vertex and the front edge all lay on one vertical
    line. The base is now the book's skew parallelogram (front vertex left of
    centre), so $h$ reads as its own dashed arrow, as on p. 247.

27. **Fig 14–1, first object** (item 10 above, now resolved). The two strips
    were nearly coincident and read as one folded sheet. Both parallelograms
    are now built on a common line with clearly different offset directions,
    reproducing the book's X with its small spikes at each end.

28. **Fig 14–28, icosahedron.** The redraw used an inner *rectangle*; the
    book's projection is a hexagonal silhouette with a chord across the top
    pair of vertices carrying two interior nodes, a chord across the bottom
    pair carrying one, and no hidden edges. Rebuilt to that pattern.

29. **Fig 14–8** now carries the book's arrowheads at $P$ and $Q$ (it had
    dots), and **Fig 14–10**'s edge $l$ runs past both vertices as printed.

### Constraints added

30. `tools/constraints/ch14.py` grew from 60 to 97 checks. New hypotheses
    encoded: Figs 14–1 (both planes on the common line, planes distinct),
    14–5 (straightness, pierce point, where the hidden stretch starts), 14–7
    (all four corners on $m$), 14–13 (both dashed rays are true opposite
    rays), 14–14 (both lines through $P$, right-angle mark sheared correctly),
    14–15 ($Q$ on $BC$, $m$ through $P$, $l$ vertical), 14–24 ($P$ on side
    $P_4P_3$), 14–37 (altitude vertical, endpoints on the two faces, length =
    height), 14–42 (axis vertical, inscribed vertices on the base ellipse).
    Fig 14–42's old entry was a placeholder, `abs(0.0 - 0.0)`, that could
    never fail; it has been replaced with the real tests.

### Tool fix

31. Item 14 above is **resolved, and it was a tool bug, not a notation
    problem**. `merge_scripts` in `tools/check_labels.py` could not re-join a
    *stacked* sub- and superscript: pdfplumber emits `$\pi_1^+$` as `π+` plus
    a separate `1` whose box lies wholly *inside* the first, i.e. at a
    negative gap, so the subscript was reported as a colliding label. The
    merge now also absorbs a fragment contained within its host's horizontal
    span. Only ch14 has such a label (`grep '\^' chapters/figures*.tex`), so
    no other chapter's count is affected. `$\pi_1^+$` keeps the book's
    stacked notation.

### Residual doubts

32. **Fig 14–2** — item 9 above stands unchanged; still a stand-in, still a
    question for Caleb.

33. **Fig 14–13, $\pi'$ panel.** The diamond is small relative to 11 pt type,
    so its four labels ($r'$, $r''$, $O'$, $\pi'$) are not in exactly the
    book's positions: the book seats $O'$ hard against the vertex, and here
    it sits a little further right so that it clears $\pi'$. Legible and
    unambiguous, but not a facsimile.

34. **Fig 14–40.** The book labels the *left* lateral edge of the small
    pyramid $l$ and the *right* edge of the large one $l'$; both are labelled
    on the corresponding (right) edge here, so the similarity ratio the
    constraint checks is the one the drawing shows. Cosmetic.

35. **Fig 14–12, 14–26, 14–31, 14–35, 14–42, 14–43** — items 11–13 above
    stand. I re-counted Fig 14–26 on scan15 p. 13 independently and agree
    with the chapter agent: four triangles about a point on the boundary.

36. Not re-derived from the scans: the exact strip widths of Fig 14–1's first
    object, the facet layout of Fig 14–12, and the aircraft/car silhouettes.
    Everything else in the chapter is either constrained or was measured
    against the printed page at 300 dpi.
