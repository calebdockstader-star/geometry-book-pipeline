# ch07 — uncertainties and questions for Caleb

Unit: Chapter 7, "Use of the Congruence Theorems", book pp. 116–132
(PDF pp. 130–146). Figures 7-1 … 7-36.

**Status: COMPLETE.** Verbatim text pass done 2026-08-17. All 143 `\VIItodo`
spans replaced with the transcription; the `\VIItodo` macro definition is
deleted. Gates: compiles twice clean · 0 todos · constraints 91/91 ·
collisions 0 · all 26 rendered pages inspected · all 10 exercise blocks
count-checked against the source.

---

## 1. RESOLVED — the copyright block that held this unit

The previous builder left this unit's prose untranscribed, writing: *"I could
not verify any of that myself … it is an assertion in a project file."* That
was the right call at the time. It is now discharged, and I verified it
**myself against the primary records**, not by trusting a project file.

`sources/copyright/nypl-data/` now holds the USCO's own post-1977 electronic
renewal records (NYPL `cce-renewals`), 128,902 rows across 1986–1991. I ran
the searches and reproduced every claim:

| Check | Command | Result |
|---|---|---|
| Authors | `grep -ih "brumfiel\|eicholz" *.tsv` | **1 row**, and it is *Principles of arithmetic* (orig. A616889, 1963-03-25 → RE552863, 1991-11-19). Not this book. |
| Title | `grep -ih shanks *.tsv \| grep -ic geometr` | **0** |
| Positive control 1 | `grep -ih "calculus and analytic geometry" *.tsv` | Thomas, *Calculus and Analytic Geometry* — Addison-Wesley, orig. A436966 **1960-03-18** → **renewed** RE396444, 1988-09-30 |
| Positive control 2 | `grep -c 1960 1988-from-db.tsv` | 21,594 |

The controls are what make the null dispositive. Control 1 is the same
publisher, same year, same genre, and its renewal **is** in the dataset — so a
renewal of *Geometry* would have been too. Control 2 shows the 1988 file is
dense with exactly the 1960-registered cohort the statute predicts. And the one
Brumfiel hit lists all four authors including Shanks, so a *Geometry* renewal
would have surfaced on the identical query.

Legal frame (checkable independently): US work published 1960 with notice →
1909 Act, 28-year first term → §305 runs it to **Dec 31, 1988** → §304(a)
required renewal in that final year, and renewal was **not** automatic for
pre-1964 works (the 1992 automatic-renewal amendment reaches only 1964–77). No
renewal filed ⇒ **US public domain since January 1, 1989.**

Nothing further is needed from you on this. Full write-up:
`sources/copyright/renewal-search.md`.

---

## 2. Printer's slips in the original, preserved verbatim

I transcribed these **exactly as printed**. Each is the book's error, not a
typo of mine. Say the word if you would rather silently correct any of them in
the rebuilt edition; my default was fidelity.

1. **p.119, converse of Theorem 7-2** — stray comma after "segments":
   "…from the fact that any two segments, are either congruent to each other…"
   Verified at 300 dpi; the comma is unambiguously there.
2. **p.126, Construction 7-3, last sentence** — the triangle sign is missing on
   the second triangle: "We will then have △ABC ≅ A′B′C′." The *Proof*
   sentence immediately below sets it correctly as "△ABC ≅ △A′B′C′", which is
   what makes it clearly a slip.
3. **p.130, Exercise Group 7-8 #8** — "These circles intersect the sides of A
   in four points", missing the ∠ before A. Everywhere else in the same
   exercise the book writes ∠A.
4. **Inconsistent overlines.** The book is erratic about segment bars, and I
   followed it line by line rather than normalising:
   - Ex. 7-8 #5 prints "such that AB = AC" with **no** bars, though `=` between
     segments elsewhere always carries them.
   - Review Ex. 16 prints "AD > AC" bare; Review Ex. 17 immediately after
     prints "AD + CB > AB + CD" fully barred.
   - Theorem 7-2 is bare throughout; Theorem 7-3 is fully barred.
   If you want a single house convention instead, this is the list to sweep.

---

## 3. Judgment calls in the text pass

### `\starnote` is ours, not the book's
The book prints **no** star footnote on p.118, where ch. 7's first starred
exercise (Ex. Group 7-2 #3) appears — the convention was introduced earlier in
the book. The scaffold and the prior text review both placed `\VIIstarnote`
here, and I kept it, because each chapter also has to compile standalone. In
the assembled book this note will be redundant with ch. 2's. **Decide at
integration time whether to keep per-chapter star notes or hoist one to the
front matter.**

### Exercise 7-4 #7 references a point the text never introduces
The hint reads "[*Hint:* Consider first △ABE and △DEC.]" but `E` is defined
only in Fig. 7-13, never in the exercise's prose. Transcribed as printed; the
figure supplies E, so it is not an error, just terse.

### Section head casing
"REVIEW OF CHAPTER 7" is set by the book as a centred display head; our
scaffold renders it as a left-aligned `\section*` like the numbered sections.
Kept the scaffold's structure (house style), not the book's centring.

---

## 4. BUG FOUND AND FIXED — and it probably affects other chapters

The visual pass caught misnumbered exercises. `\item[\stex N.]` sets a custom
label but **does not step the enumerate counter**, so every plain `\item`
following a starred one was numbered too low:

- Ex. Group 7-2 — #4 printed as "3."
- Ex. Group 7-4 — #8, #9, #10 printed as "4.", "5.", "6."
- Ex. Group 7-7 — #4 printed as "3."

Fixed in ch07 by appending `\stepcounter{exlisti}` to all 11 starred items
(applied to every one, not just the failing three, so the counter stays true
under later reordering). Verified in the render: 7-4 now reads 1, 2, 3, \*4,
\*5, \*6, \*7, 8, 9, 10.

**Action for the fleet:** any unit where a starred exercise is followed by an
unstarred one has the same latent defect. ch06's Ex. Group 6-2 happens to be
safe only because its star is the last item. Worth grepping all chapters for
`\item[\stex` followed by a plain `\item` in the same list, or fixing `\stex`
centrally in `brumfiel.sty` (I did not touch the shared style file, per the
brief). Note that constraint/collision tooling cannot catch this class — only
looking at the page does.

---

## 5. Text I could not read with certainty

**None.** The photo pages (PDF 130–146) are legible throughout for this
chapter. Five passages I judged tight were re-cropped at 300 dpi and resolved
conclusively: the p.119 comma, the p.126 missing triangle sign, the p.128
abbreviated "PQ is the ⊥ bis AB", the p.130 "sides of A", and Ex. 7-4 #5's
hint chain "AB = AQ + QB = AQ + QB′". Crops kept in
`scratchpad/ch07/crops2/`.

Exercise counts and starred positions, re-verified programmatically against
the source after transcription:

| Group | items | starred |
|---|---|---|
| 7-1 | 3 | — |
| 7-2 | 4 | 3 |
| 7-3 | 3 | — |
| 7-4 | 10 | 4, 5, 6, 7 |
| 7-5 | 5 | — |
| 7-6 | 4 | — |
| 7-7 | 4 | 3 |
| 7-8 | 9 | 8, 9 |
| Review Exercises | 19 | — |
| Algebra Review | 9 | 7, 8, 9 |

All numeric data spot-checked against the page: 61°/54°; 5 and 7 in.; 6, 8, 15;
radius 5 with AB=4, AC=5, AD=17, AE=5; r > ½AB; ¼AB; 45°, 60°/30°, 15°/75°;
32°/120°; 65°/145°/150°; 7 in.; 17, 12, (x−6)(x−4)=0; 5/3 and 10 in.; 3/5 and
MB=3; BC=4; 33 and 11.

---

## 6. Figure cross-read against the new prose

Every figure reference in the transcribed text was checked against the drawing;
**no mismatches found**, and no figure was modified (per the brief,
`figures07.tex` and `tools/constraints/ch07.py` were left untouched).

Two confirmations worth recording, since both were open questions in earlier
passes:

- **Fig. 7-16** — Ex. 7-5 #3 asks what kind of angle each of ∠A, ∠B, ∠C, ∠D,
  ∠E is. The transcribed exercise confirms all five must be drawn angles, which
  is what the figure now provides. Consistent.
- **Fig. 7-13** — Ex. 7-4 #7's hint names △ABE and △DEC, so the figure must
  carry both D and E inside/near the triangle. It does. Consistent.

### Residual figure doubts (inherited, unchanged by this pass)

These are from the figure-review pass and remain open; I did not re-litigate
them:

1. **Fig. 7-16** — the four unlabelled chord endpoints on the right-hand arc
   are a careful reading, not a measurement. Worth redoing from a sharper crop.
2. **Fig. 7-17** — the compass is a schematic redraw, not a trace.
   scan08 p.19 is a tight crop if anyone wants to trace it properly.
3. **Fig. 7-9** apex at 0.56 of AC (book ~0.70) — deliberate, to keep the
   ∠B′BC wedge wide enough for the numeral 4.
4. **Fig. 7-12** apex at 0.59 (book ~0.70) — the book's own drawing violates
   the BC ≅ B′C′ the exercise states; constraint kept exact instead.
5. **Fig. 7-33** carries a right-angle box at B that the book does not draw
   (Review Ex. 16 states it, so it adds no claim).
6. **Fig. 7-5** is a deliberate *reductio* — two perpendiculars from P to l —
   and is intentionally left unconstrained.
7. **15 TIGHT label placements** remain (all ≥ 0.32 pt, none touching); each
   was re-inspected in this pass's 110 dpi render and is legible.

---

## 7. Open questions for Caleb

1. **Star footnote policy** (§3) — one per chapter, or hoisted once to the
   front matter at integration?
2. **Printer's slips** (§2) — preserve verbatim as I have done, or silently
   correct in the rebuilt edition? This is an editorial call, and it should be
   made once for the whole book rather than per chapter.
3. **Overline normalisation** (§2.4) — follow the book's erratic usage, or
   impose one convention?

---

## Text review

Fresh adversarial pass, 2026-08-17, by an agent that did not build this unit.
Method: all 17 source pages (PDF 130–146 = book pp. 116–132) rasterised at
150 dpi and read line by line against `ch07.tex`, plus targeted 300 dpi crops
where a claim in the builder's report depended on a single mark. Recompiled
twice clean afterwards; render re-inspected at the pages that changed.

**Corrections applied: 1.**

### FIX — `\VIIstarnote` removed (macro definition + its single use)

The builder's §3 left this as an open judgment call, keeping the note "because
each chapter also has to compile standalone." Two independent checks say it
should go, so I removed it rather than passing the question on:

1. **The source does not print it.** Ch. 7's first starred exercise is Ex.
   Group 7-2 #3 on p.118. I cropped the foot of that page at high
   magnification: the text block ends after the Theorem 7-2 remark and the
   rest of the page is blank. There is no rule, no asterisk, no footnote. No
   other page in pp.116–132 carries one either.
2. **Project convention already assigns it elsewhere.** `ch02.tex:311` holds
   the book-wide first use (`\IIstarnote`). `ch05.tex:142` carries the comment
   *"ch02 owns the book-wide first use; deliberately no \starnote here"*, and
   `ch10.tex:7` says the same of ch10. Ch07 was the outlier, not the pattern.

Note the distinction from ch06/ch09/ch16, which legitimately keep star-notes:
those take an argument and carry **real footnote content** printed in the book.
Ch07's took no argument and re-emitted ch02's generic convention sentence.

This closes open question #1 in §7 for ch07. The general policy question — one
per chapter vs. hoisted to front matter — is now moot for this unit, since the
book itself prints nothing here. Standalone compiles are unaffected: nothing
in ch07 references the macro any more.

### Verified clean (no change needed)

- **Every number**, re-derived from the page rather than trusted from §5:
  61°/54° · 5 and 7 in. · 6, 8, 15 · radius 5 with AB=4, AC=5, AD=17, AE=5 ·
  r > ½AB · ¼AB · 45° · 60°/30° · 15°/75° · 32°/120° · 65°/145°/150° · 7 in. ·
  17 and 12 with (x−6)(x−4)=0 · 5/3 with 10 in. · 3/5 with MB=3 · BC=4 ·
  33 and 11 · the "result will be 2" trick. All correct.
- **Exercise structure**: 7-1(3) 7-2(4) 7-3(3) 7-4(10) 7-5(5) 7-6(4) 7-7(4)
  7-8(9), Review(19), Algebra(9) — counts and starred positions all match the
  source. 11 `\stex` against 11 `\stepcounter{exlisti}`, balanced; numbering
  confirmed in the render at Ex. 7-2 (1,2,*3,4), 7-4 (1,2,3,*4–*7,8,9,10) and
  7-8. The builder's counter bug is genuinely fixed.
- **Numbered environments**: Definitions 7-1…7-6, Theorems 7-1…7-4,
  Corollary 7-3-1, Constructions 7-1…7-7 — all present, in source order, and
  the `.sty` counters resolve to the book's printed numbers.
- **Verbatim spot-check**: all six definitions, all four theorems, the
  corollary and all seven constructions read word for word against the page;
  both proofs of Theorem 7-1, the 8-step proof of Theorem 7-3 and the 6-step
  proof of Construction 7-4 checked statement-by-statement *and*
  reason-by-reason. Every paragraph opening in §§7-1 to 7-8 and the chapter
  review checked; no dropped or paraphrased sentences found.
- **Math and symbols**: no Greek letters occur anywhere in ch. 7 (confirmed by
  grep as well as by eye), so there is nothing to get wrong there. Primes
  (C′, A′B′C′, P′, r′, D′), numbered angles ∠1–∠4, `\leqq` in Ex. 7-5 #5, and
  the ≅ / > / < / ⊥ usage all match the source.
- **Headings and TOC**: 8 numbered sections plus "REVIEW OF CHAPTER 7", each
  with its `\addcontentsline` (10 total = 1 chapter + 9 sections). Page order
  is correct — no spread-photo transposition.
- **The three printer's slips** in §2 (p.119 stray comma, p.126 missing △,
  p.130 missing ∠) — I confirmed all three independently from the source. The
  builder read them right; they are the book's, and preserving them is correct
  unless Caleb rules otherwise. §2.4's overline inconsistencies likewise check
  out as the book's own.

### Residual doubts from this pass

**None on the text.** Every passage in pp.116–132 is legible in the photo PDF;
I needed no fallback to the scans. Questions #2 (printer's slips) and #3
(overline normalisation) in §7 remain genuinely open, but they are editorial
policy for the whole book, not ch07 uncertainties. Figure debts in §6 were out
of scope and are untouched.

---

## 9. Figure repair pass — 2026-08-17 (`feedback/FIX-SPEC.md`)

Second pass, figures only. Text untouched (signed off). Gates re-run:
compiles twice clean · constraints **95/95** · `check_labels` **0 COLLIDE**
(32 TIGHT, all eyeballed) · all 29 rendered pages rasterised and inspected.

### §2 — exercise-group figures moved inline

**15 figures inlined** with `\exfig{}`, each directly after the exercise that
cites it, and `multicols` dropped from the five exercise groups that carry
figures (7-2, 7-3, 7-4, 7-5, 7-7, 7-8 and the Review Exercises). Exercise
groups 7-1, 7-6 and the Algebra Review have no figures and keep their two
columns, as the spec requires.

| group | figures now inline after |
|---|---|
| 7-2 | 7-5 (ex. 4) |
| 7-3 | 7-7 (ex. 1), 7-8 (ex. 3) |
| 7-4 | 7-11 (\*4), 7-12 (\*5), 7-13 (\*7), 7-14 (ex. 9) |
| 7-5 | 7-16 (ex. 3) |
| 7-7 | 7-29 (ex. 4) |
| 7-8 | 7-31 (\*8), 7-32 (\*9) |
| Review | 7-33 (16), 7-34 (17), 7-35 (18), 7-36 (19) |

**6 combined macros split** into 12 full-width ones, `minipage`/`\hfill`
scaffolding dropped and each picture re-fitted by hand (the spec forbids
running `measure_figures.py` in a parallel pass):
`\FIGVIISEVENEIGHT` → `\FIGVIISEVEN` + `\FIGVIIEIGHT`;
`\FIGVIITHIRTEENFOURTEEN` → `\FIGVIITHIRTEEN` + `\FIGVIIFOURTEEN`;
`\FIGVIITWENTYNINETHIRTY` → `\FIGVIITWENTYNINE` + `\FIGVIITHIRTY`;
`\FIGVIITHIRTYONETHIRTYTWO` → `\FIGVIITHIRTYONE` + `\FIGVIITHIRTYTWO`;
`\FIGVIITHIRTYTHREETHIRTYFOUR` → `\FIGVIITHIRTYTHREE` + `\FIGVIITHIRTYFOUR`;
`\FIGVIITHIRTYFIVETHIRTYSIX` → `\FIGVIITHIRTYFIVE` + `\FIGVIITHIRTYSIX`.

Fig 7-30 is **not** an exercise figure — it belongs to Construction 7-7 — so
splitting it out of the 7-29/7-30 pair let it move to the body, beside that
construction, exactly where the book prints it (p.129).

Left combined on purpose (the book prints each pair/triple as one captioned
unit on one line, and none is cited by an exercise): 7-2/7-3, 7-9/7-10,
7-15 (two panels under a single figure number), 7-18/7-19, 7-20/7-21,
7-22/7-23, 7-24/7-25, 7-26/7-27/7-28.

### §3 — figures corrected

| fig | what was wrong → what was done |
|---|---|
| 7-8 | both angle arcs at *Q* missing, leaving two stray ticks that read as segment marks → struck the two graduated arcs (∠*PQS* inner, ∠*SQR* outer) with one radial tick each |
| 7-17 | blunt parallel legs, under-drawn hinge, square bracket → redrawn: collar band, capsule hinge over the pivot circle, rounded shoulders, tapered legs, solid needle point, pencil clamp (sleeve + thumb-screw tab) with protruding lead, and a true curly brace with a cusp, *r* tucked under it |
| 7-18 | three small arcs at *B*, *C*, *D* missing so the labels floated → struck all three at graduated radii (0.70 / 0.82 / 0.94) and moved *B*, *C*, *D* to just outside their own arcs |
| 7-21 | *E* and *H* dragged together into the gap between the two constructions → *E* set tight under its point, the two constructions separated (A raised 1.75 → 1.95); also added the arc of radius *DE* about *E* that the book strikes at *D*, and stopped both compass arcs **on** the horizontal ray as the book does |
| 7-22 | *C*′ drawn as a solid tick → dashed compass arc crossing the ray; *B*′ arc lengthened so its dashes show |
| 7-23 | *B*′ a plain solid ×, *C*′ a straight solid tick → both are now dashed construction arcs (arc spans 20° → 30°, which is what makes the dash pattern read); *B*′ label moved above-right of the crossing |
| 7-26 | *P*'s label sat on its own dot → lifted clear |
| 7-28 | one merged arc at *A*, *l* extended left of the apex, rays stopping dead at *P*/*P*′, tick-like marks at *B*/*C* → two equal-radius arcs with a break at *l*; *l* now begins at *A*; both rays and the perpendicular overshoot their crossings so *P* and *P*′ read as ×'s; *B*/*C* spaced wider with their labels clear of the dots |
| 7-29 | no angle arcs, ray *AP*′ stopping dead, no dots at *P*/*P*′, over-long left stub of *l* → arcs for ∠1 and ∠2 at 30 % of *AP*, ray *AP*′ runs 22 % past *P*′, *AP* overshoots by a hair, `\dt` at both points, stub shortened and *l*'s right-hand tail lengthened so *PP*′ crosses at 42 % of *l* (the book's proportion) |
| 7-30 | **bisector ray *AQ* missing entirely**, construction arcs shrunk to a `( • )`, no tick at *B* → ray *AQ* drawn through *Q* and just past it; the two equal-radius arcs about *B* and *C* now cross in an X at *Q*; tick added at *B*; proportions rebuilt from the source (side *AC* short and near-vertical, side *AB* long at −28.9°, *r* = *AB* = *AC*) |
| 7-31 | *P*'s label thrown 0.4 units down-**left** of the crossing it names → moved immediately right of the dot, as the book sets it; *C*′ label to below-right |
| 7-32 | all four angle arcs missing, numerals halfway out along the rays, both fans rotated above the horizontal, *E*/*D* colliding → four arcs struck near the vertex with each numeral hugging its own arc; fans now straddle the horizontal (28° / 13° / −2°); ray lengths follow the book (top ray shortest); *D* and *E* now 1.26 cm apart |
| 7-13 | *D*'s label lay on segment *ADE* → moved to the free quadrant |

Sweep of the rest of the chapter turned up no further missing arcs: 7-2, 7-3,
7-6, 7-9, 7-11 (double arcs), 7-24, 7-25 and 7-27 already carry every mark the
book draws, checked figure by figure against pp.130–146.

### Open / unsettled

1. **Fig 7-32 numeral radius.** The book sets its numerals at ~33 % of the ray
   length; ours sit at ~41 %. Going closer makes the glyph box touch the
   middle ray and `check_labels` reports COLLIDE — the printed digits are
   physically larger relative to our figure than the book's are. The arcs sit
   just inside the numerals, so each still reads as "arc + its number", which
   was the substance of the complaint. Flagging in case Caleb wants the
   numerals tighter at the cost of a TIGHT/COLLIDE entry.
2. **Fig 7-17 is pictorial, not geometric**, so it carries no constraints and
   cannot be verified numerically — only by eye against p.123. It is much
   closer now (hinge, taper, tips, brace) but the hinge assembly is an
   interpretation, not a trace. If Caleb wants it exact it should become a
   scan crop like the other pictorial line art in §4 of the spec.
3. **Page 24 of the standalone chapter render is loosely filled** (Fig 7-31
   now stands full width between exercises \*8 and \*9). That is chapter-level
   pagination only; it will re-flow when `book.tex` is assembled, so I have
   not fought it here.
4. `figures07.tex` now loads `decorations.pathreplacing` (for Fig 7-17's
   curly brace). Harmless and idempotent, but the integration agent may prefer
   to hoist that `\usetikzlibrary` into `style/brumfiel.sty`.
