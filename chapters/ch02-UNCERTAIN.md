# ch02 — LOGIC (book pp. 21–42 / PDF 35–56) — uncertainty log

Repair pass, 2026-08-16. Chapter was previously transcribed and skim-verified by
Caleb; this pass verified starred exercises, the word-problem number sets, the
Aristotle plate, and added TOC hooks. No figures in this chapter.

## Questions for Caleb

### 1. Book typo kept verbatim — Exercise Group 2-12 #10 (book p. 33)
The printed text reads **"opposite lines of the line l"** where the parallel
item #10 (same group) reads "same side of the line l". Almost certainly a
printer's error for "opposite **sides**". Verified at 400 dpi on PDF p. 47;
the word is unambiguously "lines".

Kept **verbatim** per the faithful-transcription rule, with a LaTeX comment at
the call site so a later review agent does not silently "fix" it.
**Decide:** keep the typo, or silently correct to "sides"? (If corrected, note
it in an errata list.)

### 2. Aristotle plate — which unit owns it?
The halftone is on **book p. 20 (PDF 34)**, the verso *facing* the chapter-2
opener. `sources/PAGEMAP.md` assigns pp. 15–34 to **ch01**, but it is
functionally the chapter-2 opener plate, and CLAUDE.md lists it under ch 2's
known debts.

I added a framed placeholder at the top of `ch02.tex` (never redrawn), carrying
the book's caption: small-caps ARISTOTLE / "A view of a statue in a Vienna
museum." / "Courtesy of *Scripta Mathematica*."

**Risk of duplication:** if the ch01 agent also emits it, the book will show it
twice. **Action for the integration agent:** keep exactly one, and place it on a
verso so it faces the chapter opener (currently it renders on ch02 p. 1, pushing
the opener to p. 2 — correct once the book is imposed, wrong if ch02 starts on a
verso).

### 3. TOC wording
`\addcontentsline` section entries follow the **printed Contents page**
(PDF 7), not the running section headings — e.g. the printed TOC says
"The truth table for implication" while `PAGEMAP.md` abbreviates it to
"Truth table for implication". Confirm this is the wanted convention before the
other 17 units copy it.

Also added a non-book entry `Review of Chapter 2` (the book's Contents page does
not list the per-chapter reviews). Drop it if the assembled TOC should mirror
the book exactly.

## Fixes applied this pass (verified at 400 dpi against the photo PDF)

| Location | Was | Now (source) |
|---|---|---|
| Ex 2-10 #2 (p. 32) | `x = y - 3` | `x - y = 3` |
| Ex 2-12 #10 (p. 33) | "opposite **sides**" | "opposite **lines**" (book's typo, see Q1) |
| Ex 2-15 #9 (p. 38) | `2x = 3y` | `2x - 3y = 7` |
| Algebra Review Ex 7 (p. 42) | `2x + 7 = 49` | `2x + 7 = 19` |
| Algebra Review Ex 10 (p. 42) | `a(7b - 5) = a` | `r(7b - 5) = r` |

Plus: the star footnote printed a stray footnote number ("0"). `\starnote` in
`style/brumfiel.sty` emits a bare `\footnotetext`, so the counter prints. Rather
than edit the shared style file, `ch02.tex` defines `\IIstarnote` in its local
macro block (unnumbered) and calls that. **`\starnote` is still broken for every
other chapter** — worth fixing centrally in `brumfiel.sty` once the parallel
chapter agents are finished.

## Verified clean (no action needed)

- **All 23 starred exercises** match the source exactly: Ex 2-2 (*8–*11),
  2-3 (*8), 2-4 (*8), 2-5 (*6–*9), 2-6 (*8–*10), 2-11 (*8), 2-13 (*9, *10),
  2-15 (*16–*20), Review Ex (*8), Algebra Review Ex (*12).
- **Star footnote placement**: renders on the same page as Exercise Group 2-2,
  the first starred exercises — matching book p. 25.
- **Exercise counts per group**: 2-1:8, 2-2:11, 2-3:9, 2-4:10, 2-5:9, 2-6:10,
  2-7:28, 2-8:18, 2-9:4, 2-10:12, 2-11:8, 2-12:10, 2-13:10, 2-14:7, 2-15:20,
  Review Exercises:21, Algebra Review Exercises:12. All match.
- **Ex 2-15 #11 grade lists** (digit-by-digit, task item 2): threshold 90%;
  Jim 89, 84, 92, 85, 100; Sally 91, 90, 89, 94, 87. Correct.
- **Ex 2-15 #10 marbles**: 11 marbles = four blue + seven yellow, six given
  away, "not more than four yellow left". Correct.
- **Ex 2-15 #7**: $1200 / $980. Correct.
- **All six truth tables** row-for-row, including the book's non-standard row
  order in §2-4 (TT / TF / FF / FT) — that ordering is the book's, not an error.
- Definitions 2-1 … 2-9 numbering and wording; both statement-reason proof
  blocks in §2-9.

## Judgment calls

- Book pp. 24, 26, 30, 32, 34, 40 photograph at a slant with the outer margin
  compressed; every affected line was re-read on the adjacent PDF page or
  re-rendered at 400 dpi before being accepted. No line was left to guesswork.
- No iPad-scan fallback was needed: the photo PDF was legible throughout this
  range at 400 dpi.
- Overfull/underfull `\hbox` warnings remain in the two-column exercise lists
  (`multicol` + short measure). Cosmetic only; left for a global typographic
  pass rather than hand-tuned per chapter.

---

## Text review

Fresh adversarial text-review pass, 2026-08-17. Every source page (PDF 35–56)
re-rasterised and read against `ch02.tex` line by line: all 17 exercise groups
digit-by-digit, all 23 starred markers, all six truth tables row-for-row, all
nine definitions verbatim, every paragraph opening, and the printed Contents
page (PDF 7) for the TOC hooks. Six corrections applied; chapter recompiles
twice clean (37 pp., no errors).

### Corrections applied

| # | Location | Was | Now (source) |
|---|---|---|---|
| 1 | §2-1, book p. 22 | "combining statements **by letters**, we indicate statements by letters" | "combining statements, we indicate statements by letters" — the phrase was duplicated |
| 2 | §2-1, book p. 24 | "agreed to call **all** statements of the form" | "agreed to call statements of the form" — no "all" in the source |
| 3 | §2-2, book p. 26 | whole quotation italicised | only "*Some*" is italic; the rest is roman |
| 4 | §2-3, book p. 28 | "Both of these are correct" | "Both of these **statements** are correct" — dropped word |
| 5 | §2-2, book p. 25 | `\IIstarnote` anchored mid-paragraph | moved to immediately after Exercise Group 2-2, so the footnote is tied to the first starred exercises (*8–*11) as on p. 25 |
| 6 | 8 sites, whole chapter | `\begin{remark}` + `\emph{Problem.}` | `\begin{IIproblem}` |

**On #6** — this was the largest defect and it was invisible in the `.tex`
source. `brumfiel.sty`'s `{remark}` environment emits an italic **"Remark."**
head, so all eight of the chapter's *Problem.* blocks were rendering as
"*Remark. Problem.*" — a word the book never sets. ch02 was the only chapter
misusing the environment this way; ch04, ch07, ch09, ch12, ch14 and ch15 all use
`{remark}` for genuine Remark blocks, so the shared style file is fine and the
fix is ch02-local (new `{IIproblem}` environment in the local macro block,
same shape as `{remark}` with the correct head). Verified in the render.

### Residual doubts

1. **"equivalance" (book p. 33, Exercise Group 2-12 intro).** The book prints
   the misspelling; `ch02.tex` reads "equivalence". Left normalised, because
   unlike Q1 above this is a pure orthographic slip with no change of meaning —
   but the two decisions should be made together. **Decide:** silently correct
   plain misspellings while preserving substantive errors (current state), or
   preserve both verbatim?
2. **Apparent duplication, §2-8 opening (book p. 35).** The clause "If both of
   these statements are true" opens two consecutive sentences, the first
   concluding in the biconditional and the second in "their conjunction is
   true." Transcribed verbatim and re-read at high magnification to rule out a
   photo artefact — the repetition is genuinely on the page. Reads like a
   compositor's duplication. Kept as printed; flagging only so a later pass does
   not treat it as a transcription slip.
3. **Q1/Q2/Q3 above still stand** (the "opposite lines" typo, plate ownership,
   TOC convention). Nothing in this pass changes them. Q1's heading said
   Exercise Group 2-12 **#11**; the item is **#10** — corrected in place.

### Re-verified clean

Everything the repair pass claimed, independently re-checked against the source
rather than taken on trust: all 23 starred markers and their positions; the
per-group exercise counts (2-7's 28 items and 2-15's 20 items counted
individually); Ex 2-15 #10 marbles, #11 grade lists, #7 dollar figures; the
§2-4 truth table's non-standard TT/TF/FF/FT row order (the book's own); Ex 2-10
#2, Ex 2-15 #9, and Algebra Review #7 and #10 (the repair pass's number fixes —
all correct as now printed); Definitions 2-1…2-9; both statement-reason proof
blocks. The 11 `\addcontentsline` hooks match the printed Contents page word
for word, including the leading "The" in 2-4, 2-5 and 2-7 that `PAGEMAP.md`
abbreviates away.

No figure geometry was touched (this chapter has none).
