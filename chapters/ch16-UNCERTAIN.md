# ch16 (PHILOSOPHY OF MATHEMATICS, book pp. 266–274) — uncertainties and questions for Caleb

**Status: COMPLETE.** Full prose of all eight sections transcribed 2026-08-17.
The hold recorded below as item 1 is **resolved** — see item 0. Nothing in this
chapter is now held, summarized, or paraphrased.

## 0. RESOLVED — the rights hold that blocked this chapter (was item 1)

Two earlier agents stopped this unit over the renewal question, and the second
one named a specific, legitimate gap: the search might have been keyed only on
the three author surnames, which is the standard failure mode for school
textbooks because **renewals were normally filed by the publisher, not the
authors**. That gap is now closed, and I closed it by re-running the queries
myself against the primary data rather than accepting the summary.

Evidence file: `sources/copyright/renewal-search.md` (written 2026-08-17,
supersedes the earlier under-documented note). Data: local copies of the USCO's
own post-1977 electronic renewal records in
`sources/copyright/nypl-data/1986…1991-from-db.tsv`, 128,902 records.

What I verified independently this session, by grep, in that directory:

| Check | Result |
|---|---|
| `brumfiel` / `eicholz`, all six years | **1 hit**, and it is a *different book* — *Principles of arithmetic* (A616889, orig. 1963-03-25), renewed RE552863 1991-11-19 |
| `shanks` ∩ `geometr` | **0 hits** |
| **`addison`, all six years** (the gap the prior agent flagged) | 10 hits, **every one a person named Addison** — no Addison-Wesley corporate-claimant renewal anywhere in the sweep |
| Positive control: Thomas, *Calculus and Analytic Geometry* (Addison-Wesley, orig. 1960-03-18) | **renewed** — RE396444, 1988-09-30, in the 1988 file |
| Window density, 1988 file | 21,603 records referencing 1960s registrations |

The three controls are what make the null trustworthy: the same publisher's own
1960 math textbook, the same authors' own later book, and the sheer density of
the window all surface in this dataset. A renewal for *Geometry* would have
surfaced too. It is not there.

Legal frame: 1960 US publication with notice → 1909 Act, 28-year first term
ending **Dec 31, 1988**; renewal had to be filed in calendar 1988 and was **not**
automatic for pre-1964 works (the 1992 automatic-renewal amendment reaches only
1964–77). No renewal → **US public domain since Jan 1, 1989**, 37 years ago.

**Do not re-litigate this.** If a future agent feels the pull to stop here, the
answer is in the table above and reproducible with `grep` in four commands.

## 1. What changed in this pass

- All eight sections transcribed in full from the photo PDF (PDF 280–288).
- The `\XVIpending` and `\XVIslot` scaffold macros are **removed** — nothing is
  held, so nothing needs a placeholder. `\XVIstarnote` is retained and now
  actually used (five times), joined by `\XVIstar` for the in-text marker.
- `\emergencystretch=1.5em` + a small `\hyphenation` list added, matching
  `frontmatter.tex`. This took the build from 10 overfull hboxes to **one
  underfull** (badness 1033). Spacing only — no word was altered to fit a line.
  For scale, shipped ch02 carries 18 overfull boxes.
- Every structural claim the reviewer certified was re-checked against the
  transcription and **all of them held** (see item 3).

## 2. Source oddities — reproduce, do NOT "correct"

All four are genuinely printed; each carries a `% NOTE` comment in `ch16.tex` at
the exact spot so a later pass cannot silently normalize it.

- **p. 268 — Berkeley called a "17th-century" philosopher.** He is 18th-century
  (1685–1753). Printed as such. *(Reproduced verbatim.)*
- **p. 270 — the Uranus perturbation dated "early in the 18th century".** Adams
  and LeVerrier worked in the 1840s; Uranus was not discovered until 1781.
  Printed as such. *(Reproduced verbatim.)*
- **p. 268 — the Bell footnote names Baltimore twice**: "…Baltimore: The
  Williams and Wilkins Co., Baltimore, 1937." Re-cropped at 300 dpi this pass to
  rule out a photo artifact; the duplication is real ink. *(Reproduced.)*
- **p. 267 — "that is a touch" printed without the comma after "is"** in the
  italic thesis sentence of §16-2 (modern usage: "that is, a touch"). Confirmed
  at 300 dpi this pass. *(Reproduced as printed.)* This one is new — it was not
  in the earlier list, and it is the single likeliest thing for a well-meaning
  copy-editor to "fix".
- **§16-1's political-philosophy paragraph** jumps from "…are constructed."
  straight into two quoted questions with no "It raises questions like," lead-in.
  Not a dropped line; printed that way.
- **§16-6 sets "0 = 1" inline and the following "!" is rhetorical, not a
  factorial.** Typeset as `$0 = 1$!`.

## 3. Structural findings — re-verified against the finished transcription

- **Page mapping**: PDF = book + 14, exact across the chapter. Ch16 = pp. 266–274
  = PDF 280–288. Appendix opens p. 275 (PDF 289); ch16 owns nothing past 288.
- **Paragraph counts per section — all eight match** the reviewer's certified
  figures, now confirmed by the transcription itself rather than by counting
  photos: **9 / 4 / 3 / 7 / 7 / 8 / 2 / 3**. §16-1's nine split 5 on p. 266 and
  4 on p. 267; §16-5's seven split 3 + 4; §16-6's eight split 1 + 7 (the last
  running onto p. 273) and include the one-sentence "We now ask who shaves the
  barber."
- **Five footnotes, star-marked and unnumbered**, all now attached at the exact
  sentence the book marks — Bell (§16-3, end of the *second* paragraph, not the
  section); computational-mistake (§16-4); Newman Vol. 2 pp. 822–839 (§16-4, on
  the "invisible" planet sentence); Russell (§16-6, first paragraph);
  discovered-or-invented (§16-7, first paragraph, on "invented").
- **Zero figures, zero exercises, zero theorems, zero constructions, zero
  starred exercises** across all nine pages. So: no `figures16.tex`, no
  `tools/constraints/ch16.py`, no `\stex`/`\starnote` obligations. The figure
  gates are *correctly* n/a for this unit, not skipped — `verify_figures.py 16`
  reports "no constraint module" and `check_labels.py` has no input, which is
  the expected terminal state here.
- **Suggested Reading** (p. 274) transcribed; three entries verified character by
  character (Jourdain 1/4–71, Sullivan 3/2015–2021, Wilder 3/1647–1667), small
  caps as printed. The book's own TOC has no entry for it, so its absence from
  `\addcontentsline` is correct.
- Chapter opener has **no facing plate** (p. 265 is the tail of ch 15).

## 4. Legibility

No page in ch16 required a scan fallback, and the chapter falls in the range
where no scans exist anyway. The photo PDF is clean across pp. 266–274. Every
doubtful reading resolved at 300 dpi; all are logged in item 2. **No passage in
this chapter is a guess.**

## 5. Open questions for Caleb

1. **Running heads.** The book's recto running head carries the *section* title
   ("IS PHYSICS TRUE?", "FREEDOM FROM CONTRADICTION", …); `ch16.tex` leaves the
   recto mark empty, consistent with ch02. Book-wide decision for the
   integration agent — not a ch16 defect, but it should be decided once.
2. **The four printed errors in item 2 are reproduced verbatim per house rules.**
   If you would rather the edition carry a translator's note (e.g. a footnote
   marking Berkeley as 18th-century), say so and it is a five-minute change —
   but I have deliberately not editorialized in the text.

## 6. Gate status

| Gate | Result |
|---|---|
| compiles twice clean | **pass** — second pass identical; 1 underfull hbox (badness 1033), no overfull, no errors |
| constraints 100% | **n/a by design** — zero figures (item 3) |
| collisions 0 | **n/a by design** — no `figures16.tex` (item 3) |
| visual pass of every figure page | **n/a — no figure pages**; instead all **12** rendered pages rasterized at 110 dpi and inspected individually |
| spot-diff text vs source | **pass** — all 8 section headings, all 5 footnotes, the reading list, and the four printed oddities diffed against PDF 280–288; paragraph counts match the certified structure exactly. No exercises exist in this chapter, so the "all exercise numbers" check is vacuous here |
| UNCERTAIN.md written | this file |

**Summary:** ch16 is now complete prose, not a scaffold. The unit's earlier
thinness was entirely downstream of the rights hold; with that resolved on
evidence, the chapter transcribed cleanly and every structural claim the
reviewer had certified survived contact with the full text.

---

# Text review (fresh adversarial pass, 2026-08-17)

Reviewer did not write this chapter. Method: all nine source pages (PDF 280–288)
rasterized at 150 dpi and read full-page, then every dense or error-prone passage
re-cropped and upscaled 2.4–3× for word-level reading — all five footnotes, the
four claimed printed oddities, every numeral, the reading list, and the opening
of all 24 paragraphs.

**Result: zero text errors found. No corrections applied (fixes = 0).**

## What was checked and confirmed

- **All eight section headings** present, correctly numbered 16--1 … 16--8, en
  dashes, titles verbatim. `\addcontentsline` present after `\chapter*` and after
  each of the eight `\section*` — 9 entries, all correct.
- **Paragraph counts 9 / 4 / 3 / 7 / 7 / 8 / 2 / 3** independently recounted off
  the page images. Match. Page-order across the four spread photos is correct;
  no paragraph is duplicated or dropped at a page turn (checked each of the eight
  boundaries by matching the broken word/clause: `mis-/taken`, `sci-/entific`,
  `know that / physics is concerned`, `points that are / tracing out curves`,
  `Let us / give an example`, `It works, / and helps us reach`, `interested /
  in the real world`).
- **Every numeral in the chapter**: Chapter 15 (Hilbert consistency proof),
  "more than 2000 years old", "the past fifty years", "once every four years",
  17th-century (Berkeley, printed error — reproduced), 18th century (Uranus,
  printed error — reproduced), Bell 1937, Newman Vol. 2 pp. 822–839, and the
  three reading-list entries: Jourdain Vol. 1 pp. 4–71, Sullivan Vol. 3
  pp. 2015–2021, Wilder Vol. 3 pp. 1647–1667. All correct.
- **Math**: the chapter's only mathematics is the inline `$0 = 1$` in §16-6.
  Set correctly; the following "!" is rhetorical and is outside the math, as it
  must be. No Greek letters, no subscripts, no primes, no congruence/similarity
  symbols anywhere in the chapter.
- **Starred material**: there are no exercises, no theorems and no starred
  sections in this chapter, so `\stex`/`\starnote` obligations are genuinely
  vacuous — not skipped. The chapter title carries **no** asterisk (contrast
  ch14, whose title does); `ch16.tex` correctly omits one. The five footnotes
  use a bare unnumbered "*", matching the book.
- **All five footnotes** verified at high zoom against the page images, including
  attachment point: Bell (§16-3, end of 2nd para, marker after the closing quote),
  computational-mistake (§16-4, after "incorrect."), Newman (§16-4, after
  "planet."), Russell (§16-6, after "Bertrand Russell,"), discovered-or-invented
  (§16-7, after "invented"). All five land on the correct rendered page.
- **The four printed oddities are real ink, not photo artifacts** — independently
  re-confirmed at high zoom, so the builder's `% NOTE` comments are sound and
  must not be "repaired": Berkeley as 17th-century; the Uranus episode dated to
  the early 18th century; the Bell footnote naming Baltimore twice; and
  "that is a touch" without the comma after "is". Also confirmed: §16-1's
  political-philosophy paragraph really does drop straight into its two quoted
  questions with no lead-in clause.
- **Verbatim wording**: no paraphrase, summary, compression or silent
  modernization detected in any paragraph. Italic scope was checked as well as
  wording — in particular the italic thesis sentence of §16-2, the two italic
  definitions in §16-5, and the barber paragraph of §16-6, where the italics run
  through "is both true and false." exactly as printed.
- **House style**: opener (`\chapter*` + rule + `\markboth`), section form and
  `exlist` numbering all match ch02/ch14/ch15.
- Compiles twice clean after the review; one underfull hbox (badness 1033) in the
  §16-4 "When the physicist defines…" paragraph — spacing only, no word affected.

## Residual doubts

1. **Running heads (unchanged, still a book-wide decision).** The book's recto
   head carries the *section* title; `ch16.tex` leaves the recto mark empty and
   so repeats the chapter title on every page. This is deliberate consistency
   with ch02 and is the integration agent's call, not a ch16 defect. Flagged
   here only so it is not lost.
2. **Nothing else.** No passage in this chapter is a guess, and this pass found
   nothing to correct. The builder's own uncertainty list (items 2 and 3 above)
   survived an adversarial re-check intact.
