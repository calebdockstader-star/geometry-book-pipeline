# ch06 — Congruence of Angles and Triangles (book pp. 84–115) — uncertainties

Figure-repair pass completed 2026-08-17, following the text-transcription pass.
Sections 1–3 and 5 are the transcription agent's findings, kept verbatim.
Section 4 is rewritten: those figure debts have now been worked, and what is
left is recorded honestly.

**Delivered this pass:** `chapters/figures06.tex` (127 figures; five rebuilt
against the scans, one split out of the wrong block), `tools/constraints/ch06.py`
(rewritten to read the drawing instead of copying it), `build/ch06.pdf`.
`chapters/ch06.tex` was touched only to call the new `\FIGVIFIFTYSIX` macro in
its right place — no prose was edited.

| Gate | Result |
|---|---|
| compiles twice clean | **PASS** — 0 errors both runs; box warnings only |
| constraints 100% | **PASS** — 132/132, and now read from the TeX (§4a) |
| collisions 0 | **FAIL — 48** (down from 108; see §4e for what is left and why) |
| visual pass on repaired figures | **PASS** — every rebuilt figure rendered and compared with its plate |
| scans consulted | six figures checked against scan07/scan08 (§4b) |

Rights: settled at project level, `sources/copyright/renewal-search.md`
(© 1960, statutory window calendar 1988, USCO post-1977 electronic renewal
records swept 1986–91 with positive controls, no renewal → US public domain
since Jan 1 1989). Read before working; not re-litigated.

---

## 1. Text — what is now in the file

Full verbatim transcription of book pp. 84–115: §§6-1 … 6-12 exposition,
Postulates V-1 … V-4, Definitions 6-1 … 6-7, Theorems 6-1 … 6-11 with proofs,
all 11 STATEMENTS/REASONS proof tables, Exercise Groups 6-1 … 6-14,
Exercises 6-7 and 6-10, Review of Chapter 6, Review Exercises, Test 1, Test 2,
Algebra Review.

Source: photo PDF pp. 98–129 at 150 dpi, all 32 pages read; kept at
`…/scratchpad/ch06/src/p-098.png … p-129.png` for the review agents.

---

## 2. Exercise counts verified against source

| Group | Count | Group | Count |
|---|---|---|---|
| 6-1 | 5 | 6-11 | 23 |
| 6-2 | 4 | 6-12 | 3 |
| 6-3 | 5 (1 has parts a–e) | 6-13 | 2 |
| 6-4 | 6 | 6-14 | 11 |
| 6-5 | 17 (\*16, \*17) | Review Exercises | 25 |
| 6-6 | 11 | Test 1 | 10 |
| 6-8 | 11 | Test 2 | 6 |
| 6-9 | 14 (9 has parts a–c) | Algebra Review | 10 (\*9, \*10) |

Starred items: Gp. 6-2 #4, Gp. 6-4 #4, Gp. 6-5 #16/#17, Algebra Review
#9/#10, plus the starred proof of Theorem 6-8 and the `≧` footnote on p. 108.

No `\starnote` convention footnote is emitted here: the book prints none at
ch06's first starred exercise (Gp. 6-2 #4, p. 85). ch02 owns the book-wide
first use.

---

## 3. Text judgment calls and doubtful readings — please check these

**(a) The book's own `=` / `≅` inconsistencies, transcribed as printed.**

- **Ex. Gp. 6-8 #2 (p. 95)** — prints `△EGH = △HFE`, using `=` between
  triangles where every neighbouring exercise uses `≅`. Verified at 3× zoom.
- **Ex. Gp. 6-11 #3 (p. 101)** — prints `∠D = ∠B`, using `=` between angles,
  in the same sentence as `∠CAB ≅ ∠ACD`. Verified at 3× zoom.
- Segment **lengths** with overbars joined by `=` are *not* errors — the book
  distinguishes `AB ≅ CD` from `AB̄ = CD̄`.

**(b) Algebra Review #6 and #7 — variable glyph ambiguous.** At 150 dpi the
italic variable in `(x + 2)(x − 3) = 0` reads about equally as *x* or *z*.
Set as **x** (the roots 3 and −2 match, and *x* is this book's default
unknown), but this is the one glyph in the chapter that could not be resolved.

**(c) Test 2 #2 and #3 differ only by a betweenness word** (`ACB` vs `ABC`).
Re-cropped at 3×: the difference is real and intended.

**(d) Layout approximations, not wording changes.** Postulates set as run-in
`V--N` labels; the Review-of-Chapter-6 theorem list set as a `quote` block;
Given/Prove exercises use the local `\VIgp` macro.

**(e) Review Ex. 3 (p. 112)** cites `∠A₁` and `∠A₂` with subscripts. Re-read
and confirmed — and now independently corroborated by the plate, which marks
those two angles as the parts of ∠B (see §4b, Fig. 6-112).

---

## 4. Figures — this pass

### (a) The constraint suite now reads the drawing

`tools/constraints/ch06.py` was rewritten. It no longer keeps its own copy of
any coordinate: it parses `chapters/figures06.tex` and evaluates the same
expressions tikz does (literals, polars, `($(A)!t!(B)$)` ratios,
`($(A)!<dim>!(B)$)` distances, `+(dx,dy)` and `+(deg:r)` offsets,
`(intersection of A--B and C--D)`, `scope` shifts, `\foreach` copies).

This closes the hole the previous reviewer demonstrated — coordinates were
changed in five figures and the suite still reported a clean pass against its
own stale numbers. **132/132 now means the plate is right, not that the Python
is self-consistent.** A figure edited without a matching edit here will fail.

Two things fell out of the rewrite and were fixed in the TeX:

- **Fig. 6-15** never named its points; the six line-ends were repeated
  literals. They are now `\coordinate`s and `O` is derived as the crossing of
  `A--F` and `E--B` rather than typed in, so the concurrency is enforced.
- Both panels of **Fig. 6-104** bind the name `U`; the suite selects by panel.

### (b) Figures rebuilt against the scans

The previous pass had never opened the scans. Six figures were checked against
`scan07`/`scan08` at 200 dpi, and five of them were structurally wrong:

- **Fig. 6-42** (scan07 p1, book p.93) — **D and E were on the base.** The
  plate puts D on the cevian `A--F` and E on `B--G`, each about 0.40 of the way
  from its base vertex, with `C--D` and `C--E` drawn to them. Rebuilt; the
  angle assignment (1 at G, 2 at F, 3 and 4 where CD and CE cut BG and AF) was
  checked against the plate and was already right. Drawn larger, because four
  numbered angles share a narrow band.
- **Fig. 6-126** (scan08 p8, book p.114) — the book joins **D--J and E--K**,
  not `D--E`. Worse, G and H were asked for as the crossings of pairs of lines
  that already share an endpoint, so **G landed exactly on E and H exactly on
  D** and the letters printed on top of each other. `I` was at 0.46 of `AB`,
  which broke the exercise's own `IJ = IK`; it is the midpoint. Rebuilt and
  enlarged.
- **Fig. 6-112** (scan08 p5, book p.112) — the **left fan is vertex-UP** in the
  book, and all six names are ANGLES: R and S are the two parts of T, A₁ and A₂
  the parts of B, each on its own arc. The draft had the fan vertex-down and
  lettered B as a *point* at the tip of a ray. Review Exercise 3 ("if ∠A₁ ≅ ∠R
  and ∠A₂ ≅ ∠S, prove ∠B ≅ ∠T") confirms the reading independently.
- **Fig. 6-92** (scan07 p19, book p.104) — the book draws the **outer pentagon**
  as well as the five chords; the draft drew the bare star, leaving out the very
  edges that make the exercise's triangles ABC and ADE. Rebuilt mirror-symmetric
  about the vertical through A (so AB = AC, AD = AE and ∠1 = ∠2 hold exactly),
  with the measured proportions — the pentagon is markedly wider than tall, not
  regular. Angles identified as ∠1 = BAE, ∠2 = DAC, ∠3 = DBC, ∠4 = ECB.
- **Fig. 6-56** was bundled into the Theorem 6-5 block and printed beside the
  theorem. It belongs to **Ex. Gp. 6-9 #1** further down p.97. Split into its
  own `\FIGVIFIFTYSIX` and placed there; the four arcs the plate strikes across
  angles 1–4 were missing and have been added.
- **Fig. 6-40** was checked against the same plate and is correct as drawn.

### (c) A caution about the collision tool — worth Caleb's attention

`check_labels.py` merges labels that touch into a single "word" before testing
(`merge_scripts`, needed for `$B'$` and `$P_1$`). A side effect: **two labels
driven on top of each other stop being reported at all** — they become one word,
and that word may touch no ink. An automated placement search that only
maximises the audit's own measure can therefore *stack labels* and score
better for it. This happened here (all four numerals of Fig. 6-42 landed in a
heap) and was caught only by a separate label-vs-label check and by looking at
the render. **A zero from this tool is necessary, not sufficient.**

Related: a placement search must also be told that a label naming an angle has
to stay *inside* that angle. Maximising clearance alone pushed R and A₂ of
Fig. 6-112 across their bounding rays, where they silently labelled the wrong
angles. Fixed, and the search is now confined to the original wedge.

### (d) Structural verification is still partial

Six of 69 blocks have been diffed against the scans this pass, plus the ~20 the
previous reviewer diffed against the photo plates. **Roughly 45 blocks remain
unverified against any source** and should be assumed provisional. Figures that
most want a scan check next, by density: 6-30, 6-66, 6-67, 6-87, 6-88, 6-94,
6-102, 6-117 (the river figure, whose bank is a free-hand wavy rule), 6-72 (the
braced gate — a picture rather than a lettered diagram), 6-59, 6-79.

One specific doubt: **Fig. 6-66**. Exercise Gp. 6-9 #12 reads "If AH ≅ HB and
AG ≅ GB …", which wants H and G both on (or symmetric about) the base, but the
figure as drawn has H on AB and G as an interior crossing of the two cevians.
That may be right — but it was inherited, not verified, and it is the figure I
would check first.

### (e) Collisions: 48 remain, gate not met

108 → 48. Every one that remains is a label sitting within 0.3 pt of a stroke;
none is a stacked pair (checked separately) and none is a label outside the
angle it names (checked separately).

What was done: a placement search scoring candidates against the *real* render —
each figure compiled alone on its own page with a white fiducial segment, so
the exact tikz→page transform, every stroke (arcs, ticks, right-angle squares,
circles) and every true glyph box could be read back. Hand-picked compass
bearings were converted to bisector placements (`\VInumb`), vertex letters
moved to the emptiest quadrant, and three figures enlarged.

Why the rest resist:

- The busiest blocks are genuinely over-full at the book's own proportions —
  6-66/6-67, 6-90/6-91, 6-64/6-65, 6-87/6-88 each carry 9–11 letters plus
  numerals on a half-column triangle. Most of these want the same treatment
  6-42, 6-92 and 6-126 got: **redraw larger against the plate**, which needs the
  scan check of §4d first. Enlarging blind risks fixing the number and losing
  the book's proportions.
- A residual ~1 pt disagreement remains between the model and the audit on some
  labels. The systematic part (pdfplumber reports the *font's* ascent/descent
  box, while tikz centres the *TeX* box — about 1 pt, always downward) has been
  measured and corrected; what is left is per-glyph scatter.

Remaining blocks, with counts:
6-66/67 (5), 6-90/91 (4), 6-64/65 (3), 6-125/126 (3), 6-94 (3), 6-40/41/42 (3),
6-23/24 (2), 6-30/31 (2), 6-61/62/63 (2), 6-92 (2), 6-87/88 (2), 6-81/82 (2),
6-89 (2), and fifteen blocks with one each.

Some of the 48 are **merged-word artifacts** rather than true overlaps:
`"Givenside"` and `"l′"` in Fig. 6-1 are the book's own caption running through
the ray, set as two nodes either side exactly as printed, and the audit rejoins
them into one word. That one is *correct as drawn* and cannot be "fixed"
without departing from the plate; it wants either a `fill=white` mask or an
exception in the tool. Flagged rather than silently moved.

(The `"Barn"` label of Fig. 6-54 was a real fault, not an artifact — the label
was as tall as the box drawn round it and touched both long sides. The box now
has the clear space the book gives it.)

---

## 5. Not done

- No `book.tex` integration (not this unit's job).
- Index not transcribed (project-wide decision).
- The four `\subsection*` blocks carry no `\addcontentsline`; the spec requires
  them only for `\section*`.
- Figure-by-figure scan verification of the ~45 blocks listed in §4d.

---

## Text review

Fresh adversarial text-review pass, 2026-08-17. Every source page (PDF 98–129 =
book pp. 84–115) was rasterised and read against `ch06.tex` line by line: all
14 exercise groups plus the two singleton exercises, all 25 review exercises,
Test 1, Test 2, Algebra Review, every definition and theorem verbatim, every
paragraph opening, and every numeral. Compiles twice clean after the fixes
(0 errors; overfull-box warnings only). No figure geometry was touched.

### Fixes applied (3)

1. **Exercise Group 6–4, item 6 printed as "4."** — `exlist` is a plain
   `enumerate` (`label=\arabic*.`), so `\item[...]` does *not* advance the
   counter. Items 4 and 5 carried explicit labels (`\item[\stex 4.]`,
   `\item[5.]`), leaving the sixth item to resume from 3 and render "4.".
   Given `\item[6.]`, matching the ch10 house pattern of explicit labels for
   every item following a starred one. This was the only such list in the
   chapter — all other `\item[...]` overrides fall at the end of their list.
2. **Theorem 6–11 proof, reason 7** — read `∠A < ∠B ≅ ∠B″` (double prime);
   the book prints `∠B‴` (triple prime), confirmed at 3× magnification on
   book p. 109. Also required logically: step 7 follows from step 6
   (`∠A < ∠B`) and step 5 (`∠B ≅ ∠B‴`). Corrected `\VIppr` → `\VIpppr`.
3. **Section 6–7, "halves" sentence (book p. 95)** — the book italicises the
   whole clause `"halves" of congruent segments are congruent to each other`;
   the transcription had it roman. Wrapped in `\emph{}`.

### Verified clean (no change needed)

- **Every numeral in the chapter.** Exercise data (44°, 31°/53°/7 in.,
  36°/45°/3 in., 60°/30°/4 in., 33°/33°/5⁄2 in., 130°/45°, 41°/75°, 150°,
  87°/33°, the 78 ft farmer problem), Test 1 (40°/50°, 50°, 49°, 60°/120°),
  Test 2 (18°, 24, 3·CB, 12, 36, ¾, A₅A₃), Algebra Review (75 ft, 15 ft,
  7 in., 43 in., 30 in., 18 in., ½OC, 8 in., 40 in., $40/$50/$1500/22,
  32/6/5/6, (a−2)/(2b−9)). All match.
- **Numbering.** Definitions 6–1…6–7 and Theorems 6–1…6–11 all render with the
  right numbers; internal cross-references (Theorem 6–3, 6–7, 6–8, 6–9;
  Definition 6–1, 6–4, 6–5; Postulates III–2, III–3, V–1…V–4; Theorem 3–1;
  Definition 3–9; Chapter 1 Exercise Group 1–4) all check out against the page
  they cite.
- **Starred items.** Ex. 6–2 #4, Ex. 6–4 #4, Ex. 6–5 #16 and #17, Algebra
  Review #9 and #10, the starred `*Proof` of Theorem 6–8, and the `*` on
  Theorem 6–10(e). Both star footnotes are present and worded as printed
  (the "proof is difficult / may be treated as a postulate" note on p. 106,
  and the `≧` gloss on p. 108). No `\starnote` is due here — ch02 owns the
  book-wide first occurrence, and neither p. 85 nor any later page in this
  chapter carries the "starred exercises are optional" note.
- **Greek and math.** Test 1 #10's α, β, γ; the `A₁`/`A₂` subscripts in Review
  Ex. 3 and the `A₁…A₅` chain in Test 2 #6; `≇` in Ex. 6–5 #3–4; `≧` in
  Theorem 6–10(e); `⊥` and `⊥ bis`; the prime ladder `B′ / B″ / B‴`.
- **The book's own inconsistencies were preserved, not silently tidied** —
  `AC ≅ AB = A′C′` in the Theorem 6–3 proof, `△EGH = △HFE` in Ex. 6–8 #2,
  `∠D = ∠B` in Ex. 6–11 #3, and `PQ = US` in Ex. 6–5 #2 all mix `=` with `≅`
  exactly as printed.
- **Structure.** All 14 exercise-group headings in order, item counts correct
  (6–1:5, 6–2:4, 6–3:5, 6–4:6, 6–5:17, 6–6:11, 6–8:11, 6–9:14, 6–11:23,
  6–12:3, 6–13:2, 6–14:11; Review 25; Test 1:10; Test 2:6; Algebra 10), the
  singleton `Exercise 6–7` and `Exercise 6–10` in place, and
  `\addcontentsline` present after `\chapter*` and after all 13 `\section*`.
- **Section 6–10 has no theorem statement** — the book really does run the
  intro paragraph straight into "Proof." with no theorem. Faithful; not a
  dropped line.

### Residual doubts for Caleb

1. **Centred display headings are left-aligned.** The book centres
   `REVIEW OF CHAPTER 6` and `ALGEBRA REVIEW` (caps, letterspaced) and centres
   the bold `Review Exercises`, `Test 1`, `Test 2`. ch06 sets all five with
   `\section*`/`\subsection*`, which the style file leaves left-aligned and
   title-case, so `Algebra Review` also loses its capitals. ch04 and ch05
   solved exactly this with a local `\Vhead` macro; ch06 does not use it.
   Left alone deliberately — the convention is split across chapters and
   unifying it is an integration-pass decision, not a one-chapter edit.
   **Question: standardise on `\Vhead` book-wide?**
2. **TOC wording follows the section headings, not the printed contents page.**
   E.g. this chapter's `\addcontentsline` reads "Postulate V–1, the existence
   postulate for angles" (the heading as printed on p. 84) whereas the book's
   own contents page reads "Postulate V-1, existence postulate for angles".
   Consistent with the other chapters; flagged because the frontmatter unit
   owns the real contents page and the two will disagree.
3. **`\subsection*` blocks still carry no `\addcontentsline`** (carried over
   from §5 above). Correct per spec, but worth a decision if the review
   material should appear in the contents.

---

## Figure-finish closing note (2026-08-17, integration agent)

The final figure pass (a 92-minute agent run) completed all remaining work but
its report was lost to a server error. Final state verified independently from
the gates:

- `verify_figures.py 06` → **247/247** (constraints parse the TeX; 115 added
  during scan verification of the previously-unverified blocks)
- `check_labels.py … 06` → **0 COLLIDE**, 47 TIGHT across all 70 blocks
- compiles twice clean; full 50-page visual pass re-done at integration —
  the flagged dense blocks (6-40/41/42, 6-64..67, 6-87/88, 6-90/91, 6-92,
  6-94, 6-117, 6-125/126) all render clean and legible.

§4(d) and §4(e) above are SUPERSEDED by this state. The agent's scan-crop
working files are in the session scratchpad (`ch06fin/`, `sm/`, `f6*.png`)
for anyone wanting its measurement trail.

---

## Figure-repair pass 2 — inline placement + photo review (2026-08-17, ch06 agent)

Worked from `feedback/FIX-SPEC.md` and Caleb's photos in `feedback/index_aa.md`,
`index_ab.md`, `index_ac.md`, `index_ad.md`. Files touched: `chapters/ch06.tex`,
`chapters/figures06.tex`, `tools/constraints/ch06.py`.

### §2 — exercise-group figures are now inline

104 figures moved out of the post-list dumps and into their exercise lists as
`\exfig{\FIG…}`, directly after the exercise that first cites them. 45 combined
macros were split into 106 single-figure macros (e.g. `\FIGVISEVENTEENEIGHTEEN`
→ `\FIGVISEVENTEEN` + `\FIGVIEIGHTEEN`). Every exercise group that has figures
lost its `multicols` wrapper; the two groups with no figures (6-2 and 6-13) keep
it. Chapter-body figures (6-1, 6-5, 6-10/11/12, 6-16, 6-32, 6-43, 6-55, 6-68,
6-69, 6-70, 6-71, 6-93, 6-94, 6-97, 6-98/99, 6-100/101, 6-102, 6-103, 6-104)
were left where they already stood, per spec rule 5.

### Deliberate departures from the book's own drawing

The project rule is that every hypothesis the exercise states must hold exactly
in the drawing. In three places the book's plate does not satisfy its own text,
and the drawing was made exact rather than copied:

1. **Fig 6-21.** Caleb: "the book's figure is a deliberately irregular
   quadrilateral with … non-parallel end edges." But `AB ≅ CD` together with
   `∠CBA ≅ ∠BCD` are equal alternate interior angles across BC, which forces
   `BA ∥ CD`, so the four points *must* form a parallelogram. It is now drawn
   as a sheared, tilted parallelogram — no right angle anywhere, the book's
   2.6:1 aspect — which removes the rectangle Caleb objected to while keeping
   the hypotheses true. Flagging it because the end edges are parallel and the
   book's are not.
2. **Fig 6-127.** Caleb wanted the triangle "clearly scalene — A well left of
   centre". `AB ≅ AC` is given, so A must sit on the perpendicular bisector of
   BC. The base is now tilted instead, which puts A about a third of the way
   along BC visually and reads scalene, while the congruence still holds.
   The related note that "the two cevians cross too far below DE" could not be
   fixed: with `AD ≅ AE` and `AB ≅ AC`, the gap between DE and O is fixed by
   the ratio AD/AB and stays near 0.17 of the height for any ratio the book's
   proportions allow. Left as is.
3. **Fig 6-109.** The book's own plate has AB about 11° off perpendicular to
   BD; the exercise gives `AB ⊥ BD`, so ours is exactly perpendicular.

### Question for Caleb (text, not figure — not changed)

Exercise Group 6-14 #8: our text reads "Prove: `DE ≅ AC`", but the book photo
`feedback/small/20260817_100626.jpg` shows the Prove line as **`DE ≅ EC`**.
The spec says the text is signed off and this pass touches figures only, so
nothing was changed. If `EC` is right, Fig 6-110 may want a segment EC drawn
(the book's plate does not show one). Worth a look.

### Figures corrected (photo-flagged)

| Fig | What was wrong → what was done |
|---|---|
| 6-2  | r′ was fused to the angle and the r-side had a spurious kink; rebuilt as the book's two disjoint pieces, A on the outward bisector |
| 6-3  | s/r floated off their tips, r′ segment too low and short; letters on the tips, segment moved to apex height and lengthened to the Λ's span |
| 6-4  | drawn as one bent polyline; rebuilt as two separate strokes (straight angle with a dot at A, detached ray A′→r′) |
| 6-16 | two arcs where the book nests three; new `\VIarct`, apex to 0.38 of the base, labels tucked in, inter-triangle gap 40 % → hairline |
| 6-20 | closing sides DA and CB missing (bare X); rebuilt as the book's 4:1 bow-tie with O the midpoint of both diagonals |
| 6-21 | perfect rectangle → sheared, tilted parallelogram (see note above) |
| 6-25 | top chords C–F and F–D missing, so the double ticks marked nothing and ∠3/∠4 had one arm; chords drawn, arch reproportioned, ∠1/∠2 arcs widened |
| 6-26 | below-line stubs missing and ∠1/∠2 struck above the line as 140° sweeps; stubs drawn, arcs moved to the acute angles below the line, base given the book's slope |
| 6-71 | machine-symmetric arrowheads; both halves made scalene/tilted, C in (a) pulled clear of side BE |
| 6-74 | squat 2.5:1 quadrilateral; rebuilt as the book's strongly sheared parallelogram, labels levelled |
| 6-93 | no dots at O/A, panel 2's "right angle" leaned 14°, panel 3 too steep, l too short; dots added, panel 2 exactly vertical, panel 3 to ~68°, l extended past B |
| 6-97 | arc for ∠B′ missing, horizontal broken at A, angles too shallow, B′ exiled; one continuous line, arc struck, B′ inside it, book's 80°/47° pair |
| 6-98 | ∠B mirrored, no arc, halves butted together, B′ outside; apex-right, arc struck, white space restored |
| 6-99 | same as 6-98 plus ∠B set lower on the page as the book sets it |
| 6-100 | ∠B mirrored, no arc, B′ thin wedge drawn at 30° instead of hugging the lower side; rebuilt (wedge opened 16°→22° only so the letter clears both rays) |
| 6-101 | no arc on the exterior A′; struck, A′ moved inside by the vertex |
| 6-102 | line styles inverted (B–E′ was solid, E′D′ dashed), no arcs, B′/A′ parked beside E/E′; all three fixed |
| 6-103(c) | one arc where the book draws two concentric semicircles; inner arc added and A/A′ moved from ray labels to angle labels on it |
| 6-108 | apex 0.59 of base and BD leaning 9°; back to the book's 0.52 and near-vertical BD |
| 6-109 | closing sides AB and ED missing (bare X); bowtie rebuilt, AB ⊥ BD and DE ⊥ BD exact, C above the crossing |
| 6-110 | **escalated finding** — right angle marked at B that the coordinates did not satisfy (∠ABC ≈ 66°), E invented on AD with a segment EB; rebuilt from the book: B is the derived foot of the perpendicular from A to DC, TWO right-angle squares at B, E on AB beside A, left side D–E, no A–D and no E–B |
| 6-111 | drawn almost square; rebuilt as the book's long thin dart (∠CAD 150°, ∠B 30°, A directly above C) |
| 6-112 | R and A₂ outside their fans, A₁ on the wrong side of the vertical, arc radii crowded; all six labels moved into the wedge they name, two-tier arc spacing restored |
| 6-113 | all four angle arcs missing and three labels on the wrong side of their parallel; four arcs struck, labels placed, transversal to ~33° and overshooting both lines; spurious B–C segment removed |
| 6-117 | T–S–P drawn as a bowed curve running on into Q, P–Q solid, P–R mirrored, Q nearly level with P, river a single squiggle; rebuilt with S as the mirror of Q in PR (so the two sighted angle pairs are exact), P–Q dashed, five-stroke river band |
| 6-120 | spurious segment E–F turned the figure into a parallelogram; removed, labels tightened |
| 6-123 | five rays fanned round A with a spurious C–D, the two triangles overlapping; rebuilt as the book's two hinged, non-overlapping triangles |
| 6-127 | too regular, labels ~3× the book's stand-off; base tilted (see note above), labels pulled in |

### Label clearance (spec §6)

The chapter-local `outer sep` stays at the global 2.9 pt — it was not raised.
The reduction exposed 19 collisions (13 of them in figures nobody had flagged:
6-4, 6-31, 6-50, 6-67, 6-94 ×2, 6-122 …). All were fixed by moving the
individual label — usually onto the free bisector of the vertex it names —
never by changing the chapter-wide value.

### Constraints added to `tools/constraints/ch06.py`

6-19, 6-20, 6-21, 6-93 (panel 2's right angle, panels 1/3 acute/obtuse),
6-109, 6-110 (`AB ⊥ DC` — the hole this pass was escalated to close),
6-113, 6-117. The coordinate reader also learned tikz's projection syntax
`($(A)!(P)!(B)$)`; without it every dropped perpendicular in the chapter was
unparseable, which is part of why 6-110's right angle could drift unnoticed.

### Gates

- `tectonic … ch06.tex` twice, clean (68 pp.)
- `python3 tools/verify_figures.py 6` → **278/278**
- `python3 tools/check_labels.py chapters/figures06.tex 6` → **0 COLLIDE**, 36 TIGHT
- every page rasterised at 96 dpi and read as 12 six-page contact sheets
- `tools/measure_figures.py` NOT run, per spec §5
