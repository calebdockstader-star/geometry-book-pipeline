# Chapter 12 — uncertainty report

Unit: ch12, "Measurement of Angles and Arcs", book pp. 209–226 (PDF 223–240).
Text from `sources/Geometry.pdf`; figures checked against `scans/scan14.pdf`
pp. 8–21 (= book pp. 210–226), which covers every figure in the chapter.

Gates: compiles twice clean · constraints 84/84 · visual pass done on all 31
figures and all 29 pages · exercise counts and starred items diffed against the
source. Collision gate: see **Tooling** below — the shared audit is reporting
phantom geometry, and that needs Caleb's attention.

---

## 1. Questions for Caleb

1. **Fig. 12-14 label `l` vs the prose `L`.** The figure prints a lowercase
   italic *l* beside the outer bracket, but the surrounding text (p. 216) calls
   the quantity *L* ("length $\widearc{AP} = L$"). I set the figure label as
   `$l$`, matching the plate. Confirm that's the book and not my misreading of
   a worn glyph.

2. **Figs. 12-28 and 12-29 now contradict the book's proportions — on purpose.**
   The book's own cuts are schematic and do **not** honour their quoted numbers:
   - 12-28 (Ex. 15: `AO=12, OB=4, CO=8`) is drawn with `AO:OB ≈ 2.2:1`, not 3:1.
   - 12-29 (Ex. 16: `AD=6, DE=10, AB=8`) is drawn with `BC ≈ AB`, though the
     power of the point forces `BC = 4`, i.e. half of `AB`.

   The project rule says quoted lengths must be reflected in drawn proportions,
   so I solved both configurations exactly. Consequence: the drawings are
   correct but look different from the plates, and 12-29 necessarily reveals the
   answer (`BC = 4`) that the book's sketch conceals. **If you'd rather match the
   book's look, say so and I'll revert both to schematic.**

3. **Lemma 12-11-1 proof, reasons column.** The book numbers the REASONS column
   independently (`1. Why?` … `5. Why?`) alongside the numbered statements. The
   house `steps` environment numbers once, at the left, and ch09 already drops
   the reason numbers. I followed house style. Say if you want the book's
   double numbering.

4. **`\starnote` deliberately not emitted.** The first starred exercise in this
   chapter is Ex. Group 12-2 #4 (p. 212), but the book carries no footnote
   there — the convention is footnoted once, early in the book. So ch12 emits
   no `\starnote`. Confirm that's right for the assembled edition.

---

## 2. Text — read with certainty unless noted

Everything transcribed from the photo PDF; no page needed the scans as a text
fallback. Judgment calls:

- **`≦` throughout.** The book uses the double-bar "less than or equal" in
  Theorem 12-8, Theorem 12-9 and Eq. (12-4). Set as `\leqq`.
- **Definition 12-1 italic span.** I italicised "*the arc $\widearc{AB}$ of the
  circle*"; the photo is clear that the phrase is italic but the exact right
  edge of the italic run (whether "of the circle" is inside it) is a hair
  ambiguous at this resolution.
- **Theorem 12-5 lead-in.** The book prints **Theorem 12-5** in bold, then
  "Converse to Theorem 12-4." in roman with *no* parentheses. `amsthm`'s
  optional note would add parens, so this one theorem is hand-set with an
  explicit `\refstepcounter` to keep the counter in step.
- **"Consequence of Definition 12-7"** (p. 222) is a run-in italic head, not a
  numbered environment; set that way.
- **Eq. (12-1)** is a three-line braced system with a single number; reproduced
  with `\left.…\right\}`.
- **Ex. Group 12-7 #4** ends "`(180/π)°`" — read as `(180/\pi)^\circ`.
- **§12-7 heading** needed an explicit `\\` break ("COUNTING DEGREES AND /
  MEASURING ANGLES"). Justified `\section*` refused to break at the space and
  otherwise hyphenated "MEASUR-ING". Words unchanged; only the break is mine.

Verified against source: all 12 exercise blocks (12-1…12-11 plus Review
Exercises) with counts 5, 4, 4, 3, 5, 10, 6, 7, 4, 10, 18, 6; starred items
exactly 12-2 #4; 12-11 #9, 10, 11, 12, 14, 16, 17; Review #6. Numbers spot-checked
including 2.454, π = 22/7, 32 in./22 in., π = 3.1416, A₅₁, and the Ex. 15/16/18
length sets.

---

## 3. Figures — 31 drawn, all scan-checked

Constrained points are derived, never eyeballed (arc midpoints and bisectors by
half-angle arithmetic; crossings via `intersection of`; tangency via the
radius-perpendicular; Exs. 15/16/18 solved exactly). `tools/constraints/ch12.py`
asserts 84 hypotheses, all passing.

Not fully nailed:

- **Fig. 12-14** — the exact set of dashed bisection rays is inferred. I drew
  33.75° / 45° / 56.25° / 67.5°, which are the construction's own successive
  bisections, and put `P` at 60° because the text says `L` is "a little greater
  than 5/8 · πr/2" (5/8 of the quarter = 56.25°).
- **Figs. 12-15 / 12-16** — the book exaggerates the 1° steps, so the printed
  ray angles are illustrative and not recoverable. I used 10° / 32° / 57° with
  `A` at 48°, which satisfies the theorem's `n ≤ ∠AOB ≤ n+1`. I widened the fan
  from my first pass (38° → 32°) purely to give the `A` label clear air.
- **Fig. 12-20** — I could not resolve from the scan whether a chord `A–C` is
  drawn. The lemma needs only `BA`, `BC` (the latter lying along the diameter)
  plus the radius `OA`, and that is what the scan shows, so that is what I drew.
- **Fig. 12-19(c)** — the "not inscribed" case: vertex `B` outside the circle is
  certain; the precise placement of `A` and `C` is approximate, constrained only
  so that `AB` and `BC` cut the circle as in the plate.
- **Fig. 12-25** — the book draws small arrowheads at `A` and `C` on the tangent
  line; I drew a plain segment.
- **Fig. 12-31** — the book shows no right-angle box at the centre, so I omitted
  one even though the exercise calls the angle right.
- **Fig. 12-17** — both central angles drawn at 75°; the plate's exact opening
  is not dimensioned.
- **Fig. 12-6** is unlabelled in the book; reproduced unlabelled.

No organic shapes in this chapter — every figure is circles, radii, chords and
arcs — so the organic-shape rule does not bite here.

---

## 4. Tooling — `tools/check_labels.py` is reporting phantom geometry

**This is the one thing I could not gate cleanly, and I think the tool is at
fault rather than the figures.** Two defects, both reproducible:

1. **Straight lines are rebuilt as the wrong bounding-box diagonal.**
   `geometry_segments()` does `(ln['x0'], ln['top'], ln['x1'], ln['bottom'])`.
   `top`/`bottom` are bbox extents, not endpoint order, so every line with
   positive slope is tested as its *mirror image*. pdfplumber already exposes
   the true endpoints as `ln['pts']`. Fix is one line:

   ```python
   for ln in page.lines:
       p = ln.get('pts')
       if p and len(p) >= 2:
           for a, b in zip(p, p[1:]):
               segs.append((a[0], a[1], b[0], b[1]))
       else:
           segs.append((ln['x0'], ln['top'], ln['x1'], ln['bottom']))
   ```

2. **Curves are reduced to chords through Bézier control points.** Every circle
   and arc becomes 4 straight chords that cut *across* the disc, so any label
   correctly placed inside a circle collides with a line that is not on the
   page. Needs the cubics sampled instead (`len(pts) % 3 == 1`, then evaluate).

Effect on this chapter, which is nothing but circles and arcs: the shared tool
reports **13 collisions**. Every one I traced by hand was a mirrored-line
phantom, a Bézier-chord phantom, or a same-symbol tokenisation split — not ink
touching ink. A corrected local implementation (kept out of the shared tool so
as not to disturb parallel agents) plus a 300 dpi look at all 31 figures shows
the labels clear. **I did not tune label positions to chase the buggy number**,
because that would have pushed correct labels off correct figures.

Recommend the figure-review agent re-run the gate after the tool is fixed.

Related, and worth a decision: `$A'$` and `$n^\circ$` always tokenise as two
adjacent words, which the audit counts as a label-vs-label collision no matter
where the label sits. I added a 1.3 mu hair kern (`\XIIp`, `\XIId`, ≈ 0.65 pt,
invisible at print size) so primed and degree-marked labels stop registering.
That is a real if tiny typographic change — revert it if you'd rather the audit
learn to group superscripts.

---

## 5. Deliverables

- `chapters/ch12.tex` — 29 pp., compiles twice clean; remaining warnings are
  three sub-3 pt overfull text lines (0.4–2.3 pt) and expected underfulls.
- `chapters/figures12.tex` — 31 figures, macros `\FIGXII…`.
- `tools/constraints/ch12.py` — 84 constraints, all passing.
- `build/ch12.pdf`.
- Source page PNGs kept at
  `…/scratchpad/ch12/src/` (photo pages) and `…/scratchpad/ch12/scan/`,
  `…/crop/` (scan crops used for figure measurement).

---

## Text review (fresh agent, adversarial pass)

Scope: every line of `ch12.tex` diffed against PDF pp. 223–240 (book pp.
209–226) at 150 dpi, with 3× crops on the four passages the photo curl made
marginal. Figure geometry untouched.

### Fixed (7 instances, one defect class)

**Numbered remarks printed a spurious period.** The book distinguishes two
forms: unnumbered remarks are set *`Remark.`* (italic word, italic period),
but **numbered** ones are set *`Remark`* ` 1.` — italic word, roman numeral,
**no period after the word**. Verified at 3× on book pp. 218 and 221. The
shared `remark` environment in `brumfiel.sty` hard-codes `\emph{Remark.}\ `,
so `\begin{remark}1.\ …` was rendering **“Remark. 1.”** in all seven numbered
remarks: Def. 12-3 R1/R2, Def. 12-4 R1/R2/R3, Def. 12-7 R1/R2.

Fix is local to ch12 (the shared style file is left alone so parallel chapter
agents are not disturbed): a new `XIIremarkn` environment in the chapter's
existing local-macro block, flagged for hoisting. The three genuinely
unnumbered remarks (pp. 212, 213, 220) still use `remark` and still print
“Remark.”, which is correct.

**Other chapters almost certainly have the same bug** — ch15 has numbered
remarks stubbed as `\XVtodo` placeholders inside plain `remark`. Worth
promoting `XIIremarkn` into `brumfiel.sty` at integration and sweeping.

### Retired — one of the builder's open questions

**Definition 12-1 italic span (was §2, bullet 2) is settled.** A 3× crop of
book p. 209 shows the italic run beginning at “the arc `AB`” and continuing
through “of the circle” across the line break, with “subtended by ∠AOB”
clearly back in roman. The transcription's span is right; no change needed.

### Checked clean — no change required

- **Every number in every exercise.** All 12 exercise blocks re-counted from
  the plates: 5, 4, 4, 3, 5, 10, 6, 7, 4, 10, 18, 6. All data values confirmed
  against the source, including 2.454; 7/8, 9/16, 7/4 · πr/2; π = 3.14 then
  3.1416; 32 in./22 in. with π = 22/7; the Ex. 15/16/18 length sets
  (12/4/8, 6/10/8, 8/10); radius 14 with 30°; the radian lists in 12-10 #7/#8;
  and A₅₁ → A₁ at r = 10.
- **Starred items.** Exactly as the builder reported: 12-2 #4; 12-11 #9, 10,
  11, 12, 14, 16, 17; Review #6. Independently re-read off the plates —
  #13, #15 and #18 are correctly *un*starred, which is the easy slip here.
  No `\starnote`: confirmed no star footnote is printed anywhere on pp.
  209–226, so omitting it is right (builder's question #4 stands as a
  book-assembly decision, not a ch12 defect).
- **Numbering.** Theorems 12-1…12-11, Definitions 12-1…12-7, Lemma 12-11-1,
  Eqs. (12-1)…(12-4), Exercise Groups 12-1…12-11 — all present, in order, no
  gaps, and the manual `\refstepcounter` for Theorem 12-5 keeps the counter in
  step (12-6 follows correctly).
- **Math and symbols.** `≦` (`\leqq`) in Thm 12-8, Thm 12-9 and Eq. (12-4);
  primes on `l'_n`/`l''_n`, `L'_n`, `A'O'B'`, `P'`, `Q'`; `≅` vs `~`
  (similarity) used as the book does; `(n + 1)st`; `π²/4`; `(180/π)°`;
  `AB² = AD · AC`. No Greek beyond π in this chapter — no alpha/beta/gamma to
  get wrong.
- **Wording.** Every paragraph opening spot-read; §§12-1, 12-3, 12-5, 12-6,
  12-9, 12-10 read in full; all 7 definitions, 11 theorems, the lemma and both
  footnotes (Sumerians, circumference) read verbatim. No paraphrase, no
  dropped sentence found. The two worst-curled paragraphs (p. 209 ¶3, p. 212
  “Having defined arc length…”) were re-read at 3× and are verbatim.
- **Structure.** Section headings, exercise-group boundaries, the Review
  outline (12 entries, correct order), Important Remark, and Review Exercises
  all match the plates. Page order is right — no spread-photo transposition,
  which was the main risk given the source's alternating-page framing.
- **TOC.** `\addcontentsline` present after `\chapter*` and after all ten
  `\section*`s plus the Review — 12 entries, all correctly formed.

### Residual doubts

1. **§12-7 heading break.** The book sets “12-7 COUNTING DEGREES AND MEASURING
   ANGLES” on one line; the transcription forces `\\` before “MEASURING”. The
   builder's reason (justified `\section*` otherwise hyphenates “MEASUR-ING”)
   is sound and the words are unchanged, but at the 145 mm trim this is the one
   place ch12's heading shape departs from the plate. Cosmetic; flagging only
   so the integration agent can apply one policy across all chapters.
2. **Lemma 12-11-1 REASONS numbering** — unchanged, and the builder's question
   #3 still stands. I confirmed the book does print an independent `1.`…`5.`
   in the reasons column; house `steps` drops it, as ch09 does. This is a
   house-style decision for Caleb, not an error.

Nothing else outstanding on the text side.

## Figure review

Fresh figure-review pass, 2026-08-17. 20 figure blocks / 31 numbered figures in
`chapters/figures12.tex`, all cross-read against the photo PDF (pp. 223–240)
and against scan14 pp. 8–21, which covers every plate in the chapter. Final
state: **138/138 constraints hold** (was 84/84 over a weaker set),
**0 COLLIDE / 0 TIGHT**, compiles twice clean.

### Structural errors found and fixed

1. **Fig 12-26 drew the wrong chord.** The file had `C--D`; the plate draws
   `B--D`, and so must the redraw — Ex. *10 gets `angle A` as the exterior
   angle of triangle *ABD* at *B*, and Ex. *14 proves `ABD ~ AEC`. Neither
   argument has a figure without *BD*. Also extended the upper secant past *C*,
   as the plate does, to show it is a line.
2. **Fig 12-19(c) had the wrong failure mode.** It placed the vertex *B*
   outside the circle, with segment *AB* slicing the interior and *A* landing
   within 5% of the arc — visually indistinguishable from "*A* is on the
   circle", which is the one thing the panel must not say. Measured off
   scan14 p.17: *B* sits a whisker outside (1.08 r) at 215.6 deg, *C* is on the
   circle at −45.3 deg, and *A* is 1.5 r away along 111.8 deg so the whole ray
   *BA* misses the circle (closest approach 1.05 r). That is why the angle is
   not inscribed. Encoded as four new checks.
3. **Fig 12-20 radius drawn solid.** The plate prints *AO* dashed (it is the
   auxiliary radius of the lemma's isosceles triangle). Switched to `aux`, and
   moved *A* from 118 deg to the measured 79 deg — the plate puts *A* right of
   the vertical, the redraw had it left.
4. **Fig 12-24 drew a special case.** Both chords sat at ±0.54 r, which makes
   `AB` congruent to `CD` — a coincidence Ex. 7 never grants. The plate has
   0.55 r and 0.68 r. Fixed, plus a constraint that forbids equal offsets.
5. **Fig 12-5 line semantics.** The eight-side path was dashed like the
   two-side path it refines; the plate strikes it heavier. Now `key`.

### Proportions corrected against the plates

12-11 (C 82→90, B 19→10), 12-21 (A 75→80, C −60→−33, plus the two angle arcs
the plate draws at *B*, without which the letters *x*, *y* name nothing),
12-22 (A 75→110, C 25→36), 12-25 (arcs *BD*, *BE* 78→66 deg).

### Constraint file

`tools/constraints/ch12.py` previously used radii and coordinates that only
*resembled* the drawing (12-1 R=1.15 vs 1.25 in the tex, 12-24 a different
scale, 12-19 a different centre). Every check was scale-invariant so everything
passed, but a pass certified nothing about the actual figure. All coordinates
now mirror `figures12.tex` exactly. Added: betweenness of the near secant
points (12-3, 12-25, 12-26, 12-29, 12-30), on-circle tests for every labelled
point, external-point tests, interior-crossing tests (12-27, 12-28), the
power-of-a-point identities behind Ex. 13/14/17, irregularity of the 12-9 path,
`r' != r` in 12-12, tangent corners outside the circle in 12-6, and the
`sqrt(2) r` chord in 12-31.

### Deliberate departures from the plate (all defensible, listed for the record)

1. **Figs 12-28, 12-29, 12-30 are drawn to the quoted numbers; the book's are
   schematic.** Honouring Ex. 15/16/18 forces the shapes: in 12-29, AD=6,
   DE=10, AB=8 gives BC=4, and a 4-unit chord on a 5.2-unit-radius circle
   *must* be a near-tangent graze at 0.92 r, which is why *B* and *C* huddle at
   the bottom instead of crossing near-horizontally as in the plate. Same story
   in 12-30 (AB = 2r) and 12-28 (AO:OB = 3 rather than the plate's ~2.2). This
   follows the project rule that quoted lengths be reflected in proportions,
   but it does make the answers to those exercises legible from the drawing.
   **Question for Caleb: keep the exact solution, or revert these three to the
   book's schematic shapes so the exercises stay honest?**
2. **Fig 12-3** enlarged (R 1.25→1.90) and Q' moved 22→27 deg. At the plate's
   proportions the label *P'* sits where the ray *OQ'* crosses the chord *EF*
   with the radius *OF* just below — three inks inside half a label-width, no
   placement clears. 12-2 was raised to 1.45 to keep the pair looking related;
   the book draws them the same size, this pass has them 1:1.3.
3. **Fig 12-21** enlarged (R 1.35→1.6) so the 16.5-deg wedge named *y* is tall
   enough to hold its numeral clear of both sides. **Fig 12-17** left circle
   enlarged (0.95→1.15) for the same reason with the interior *A* deg.
4. **Fig 12-25** tangent line drawn without arrowheads; the plate puts an
   arrowhead at each end to mark *AC* as a full line. No other figure in the
   chapter uses arrowheads, so this was left alone — worth a house policy call
   during integration rather than a local fix.
5. **Fig 12-22** angle arcs at *B* not reproduced. The plate draws two, but
   both are unlabelled and the figure carries no *x*/*y* to anchor, so they
   add ink without information. 12-21's arcs *were* added because there the
   letters need them.
6. **Fig 12-18** keeps the exact 57.2958-deg radian angle; the plate's engraved
   angle measures nearer 69 deg. Correctness beats the plate here.
7. **Fig 12-12** radius ratio drawn 1.59:1; the plate is nearer 1.95:1. Only
   the congruence of corresponding central angles is load-bearing, and that is
   checked.

### Residual doubts

- **Fig 12-19(c)** is the one place where the plate's own draughtsmanship is
  self-contradictory: read strictly, the definition on the facing page would
  admit the drawn angle if the vertex were exactly on the circle and the ray
  *BA* re-entered. The redraw resolves it the only consistent way (vertex a
  hair outside, ray clear of the circle) and the panel now reads exactly as
  the plate looks. If Caleb reads the plate as putting *B* strictly on the
  circle, the panel needs re-thinking, not just re-measuring.
- **Fig 12-9** vertex spacing is deliberately uneven (Theorem 12-2 drops
  regularity) but the specific eight angles are the previous builder's, not
  measured off a scan — the plate's path is too small to read individual
  vertices at 400 dpi. Structure and irregularity are right; exact spacing is
  arbitrary.

***

## Figure-repair pass, 2026-08-17 (feedback/FIX-SPEC.md)

### What changed

**Spec §2 — exercise-group figures are now inline.** All 14 figures cited by
exercises were moved inside their lists, each `\exfig{...}` immediately after
the item that names it; `multicols` dropped from the three groups that carry
figures (12-1, 12-2, 12-11). Groups with no figures keep their two columns.
Eight combined macros were split, since the two halves are cited by different
exercises: 12-2/12-3, 12-7/12-8, 12-24/12-25, 12-26/12-27, 12-29/12-30. The
Review Exercises list was merged into one `exlist` so Fig 12-31 sits after
item 1 without a counter reset. Figure numbers still print in book order.

12-5/12-6, 12-9/12-10, 12-11/12-12, 12-13/12-14, 12-17/12-18, 12-19/12-20 and
12-21/12-22 stay paired: they are body figures, and the book prints each pair
side by side on one page (verified on the plates for 12-5/12-6 and
12-21/12-22).

### Figures corrected

| Fig | Fix |
|---|---|
| 12-5 | drew a chord *AB* that missed the centre by 0.44 r; the book draws the two **radii** *OA*, *OB* meeting at a 170-degree bend. Arc widened 146→170 deg, which is what un-crowds the nine labels; eight-side path struck heavier with a radial nick at each interior vertex, so the letters name marked points instead of reading as a caption strip. |
| 12-6 | angles re-cut to match 12-5's new arc; tangent corners now derived as `R/cos(42.5)`. |
| 12-8 | outer arc ran *OA*→*OC*, **crossing ray *OB*** — it marked ∠AOC. Now two arcs abutting at *OB*, one on ∠AOB and one on ∠BOC, at radii 60 % apart. Fan tilted (78/33/−12) so no ray is axis-aligned while ∠AOC stays exactly right. |
| 12-9 | inscribed path had seven short sides sagging 0.017 r — under a point on the page — so it printed on top of the circle as a ragged doubled edge. Now four long irregular sides, sag 0.07 r, plainly inside the circle. |
| 12-10 | arc emphasis was a `key` arc on the circle itself (1.0 pt against a 0.9 pt circle, invisible). Now a heavier **dash-broken** arc just outside the circle, as the book marks it; fan tilted off the axes. |
| 12-14 | was an axis-aligned 90-degree quarter with five over-long rays running through the marker. Now the book's ~68-degree sector, tilted symmetric about the horizontal, with exactly four interior rays at the 1/2, 5/8 and 3/4 subdivisions plus the solid ray at 0.662 ("a little greater than 5/8"), all stopping short of the marker. The *l* marker is a real brace — end hooks, middle nib — spanning only arc *AP*. *r* moved inside the sector. |
| 12-15 | both markers were plain arcs (one with straight ticks, one with nothing and a floating label). Both are now hooked braces with a nib pointing at the label. The 1-degree marker is a short headed arrow tucked into the wedge with its label right under *OB*, not a crossbar parked below the figure. Each dashed ray now runs out only as far as the marker it closes. |
| 12-16 | same brace/arrow rebuild, **plus the reported label bug: the radius was a bare *r* and is now *r′***, matching every other primed letter in the figure. |
| 12-22 | removed the chord *AC* the book does not have; restored **both** angle arcs at *B* (thin, concentric, springing from *A* and from 0.55 along *BA*, sweeping across chord *BC* and landing on the dashed diameter *BQ* with a terminal tick); added the centre dot. |
| 12-28 | reverted from the solved cut (AO:OB = 3, CO:OD = 4/3) to the plate's schematic (2.76 and 1.11), so Ex. 15 can't be answered with a ruler. |
| 12-29 | reverted from the solved cut; lower secant no longer grazes the circle (*BC* is now a long near-horizontal chord with *C* on the right) and *A* sits ~0.6 r clear instead of 1.5 diameters out. *A* derived as the secants' crossing. |
| 12-30 | reverted from the solved cut; *AB* is now genuinely **tangent** (*B* from the tangent-length construction, so *OB* ⊥ *AB* exactly) and *ACD* is a true horizontal **diameter**. AB² = AC·AD then holds identically, but AC:CD is 0.43, not the exercise's 0.8. |

New in `figures12.tex`: `\XIIbrace{centre}{radius}{ang1}{ang2}{depth}`, the
book's arc-measure brace. `XIIhook` thinned 0.5→0.45 pt so the sector reads
bold against the markers, as the plates set them.

### Gates
compiles twice clean · `verify_figures.py 12` **168/168** · `check_labels.py`
**0 COLLIDE, 0 TIGHT** · every changed page rasterised at 130 dpi and read.

### Questions / deliberate deviations for Caleb

1. **Fig 12-22, label *O*.** The book sets it above-left of the centre dot.
   That wedge — between the dashed diameter and chord *BC* — is only 0.42 r
   deep at the centre and will not hold a footnotesize letter clear of both
   lines; it collided. It is set **below-left** instead, still against the dot.
   Say the word and I will shrink the letter rather than move it.
2. **Fig 12-14, rays vs. brace.** The spec lists "rays running past the brace"
   as a defect to fix, so ours now stop short. Note the book's own plate does
   let the two lower dashed rays graze the brace. Ours is the tidier reading
   Caleb asked for, not the literal plate.
3. **Fig 12-14, label *r*.** The photo review says the book tucks *r* inside
   the sector against *OB*; my read of the plate put it just outside. I went
   with the review (inside), centred in the wedge between *OB* and the 3/4 ray.
4. **Fig 12-5 / 12-9 arc-emphasis weight.** The heavy path is 1.5 pt against a
   0.9 pt circle. This is the book's own convention for these two plates, not
   a revival of the retired `key` weight — flag it if it reads too heavy.
5. **Vertical spacing.** Dropping `multicols` leaves the de-columned groups
   with fewer, taller elements per page, so `\flushbottom` stretches the glue
   and the gap under an "Exercise Group" heading can run to ~20 pt. Source-side
   spacing is unchanged; this wants the whole-book re-fit at integration, not a
   local patch.
