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
