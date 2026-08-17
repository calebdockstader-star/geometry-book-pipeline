# frontmatter — uncertainty log

Unit: front matter (book pp. i–xii = PDF pp. 1–14). Built FULL from
`sources/Geometry.pdf`. No scan consultation was needed: the photo pages are
fully legible and the unit contains no line figures.

---

## Questions for Caleb

### 1. The public-domain determination is the one thing I could not verify here
Everything this project produces rests on a single premise recorded in
`CLAUDE.md` / `STATUS.md`: that the 1960 Addison-Wesley copyright was never
renewed, so the book fell into the US public domain in 1989 (pre-1964 US works
required 28th-year renewal).

What I *did* confirm, from PDF p. 6 at 300 dpi: the copyright page reads
`Copyright © 1960 / ADDISON-WESLEY PUBLISHING COMPANY, INC.`,
`Library of Congress Catalog Card No. 60-8336`, `Second printing, February,
1961`. So the standing edition condition is satisfied — this is the 1960/61
imprint, not a later edition.

What I could **not** do from inside this session is re-run the renewal search
itself; I have no access to the CCE/NYPL renewal records here. I proceeded on
the recorded determination because it is specific and falsifiable (named
dataset, named 1988–91 window, and — the detail that actually makes a negative
result meaningful — a positive control). Please keep that search evidence
(query, dataset snapshot, the positive-control hit) on file with the project.
If it ever turns out a renewal exists, the entire transcription is infringing,
not just this unit. This is the one assumption worth re-auditing before any
public distribution.

### 2. The 1961 "all rights reserved" notice must not read as governing *this* edition
I transcribed the original notice verbatim, as instructed, and as facsimile
reprints do — it is a historical record of the source printing. But on the
current title-verso it sits alone, so a reader could easily take it as this
edition's own rights statement, which would be wrong in both directions (it
claims rights the restoration does not hold, and it contradicts the
public-domain basis). Suggest the integration agent add a short editorial line
below it, e.g. *"The notice above is reproduced from the 1961 printing. This
restored edition is derived from a work believed to be in the US public
domain."* Wording is your call — I did not invent one, since it is a legal
statement and not part of the book.

### 3. Front-matter page numbering will not match the original
The original numbers the front leaves i–iv unnumbered, CONTENTS v–viii, PREFACE
ix–x, FOREWORD xi, Hilbert plate xii. We deliberately drop the four printed
CONTENTS pages (the assembled book generates its own TOC) and I added a
half-title leaf per the unit brief, so in the standalone build PREFACE lands on
vii rather than ix. Harmless in isolation; the integration agent controls final
folios. Flagging so nobody "fixes" it twice.

### 4. Who owns the David Hilbert plate — frontmatter or ch01?
Book p. xii (PDF 14) is a full-page halftone portrait of Hilbert facing the
Chapter 1 opener. It falls inside my page range, so I carried it as a plate
placeholder at the end of this unit. But `CLAUDE.md`'s unit table gives ch01 PDF
15–34 and notes "opener has photo plate on facing page", which reads like ch01
may claim it too. **If ch01 also emits it, drop one copy at integration.** Note
the unit brief for frontmatter described PDF 13–14 as "FOREWORD TO THE STUDENT";
that is off by one — the Foreword is p. xi (PDF 13) only, and PDF 14 is the
plate.

### 5. No separate half-title leaf appears in the photos
PDF 3 (book p. i) is the Addison-Wesley Science Education Series page; there is
no distinct half-title recto visible before it. The unit brief asked for a
half-title, so I added one as an editorial leaf and kept the series page
faithful behind it. Remove the half-title if you want strict fidelity.

---

## Plates (halftone photographs — placeholder only, never redrawn)

| Book p. | PDF p. | Plate | Caption transcribed |
|---|---|---|---|
| ii | 4 | Euclid, engraved portrait medallion | `EUCLID` / `Courtesy of` / *Scripta Mathematica* |
| xii | 14 | David Hilbert, photographic portrait | `DAVID HILBERT` / *(1862–1943)* / Professor of Mathematics, University of Göttingen, Germany / Perhaps the world's foremost mathematician during the first half of the twentieth century. / *Courtesy of the New York Public Library.* |

Both captions were read at 150 dpi and are unambiguous. The Euclid medallion
carries Greek lettering around its rim (partially legible: `…ΑΓΕΜ…` on the left
arc); it is decorative engraving inside the plate image, not typeset text, so
nothing was transcribed from it.

---

## Text confidence

Verified character-by-character against 300 dpi crops:

- **Copyright page** (PDF 6) — every line, including `60-8336` and the comma in
  `February, 1961`. Exact match.
- **Series page** (PDF 3) — all four consulting editors, two-column order
  (Pieters / Rosenbloom, then Thomas Jr. / Wagner). Exact match.
- **Preface sign-off** (PDF 12) — `January 1960` (italic, flush left) and
  `C. B., R. E., M. S.` (flush right, spaced initials). Exact match.

Read confidently at 150 dpi, no ambiguity, but not re-cropped:

- Full PREFACE text, book pp. ix–x (PDF 11–12), 12 paragraphs.
- Full FOREWORD TO THE STUDENT, book p. xi (PDF 13), 3 paragraphs + sign-off.
- Title page (PDF 5) and the three affiliations, which are printed on the facing
  verso (PDF 4) right-aligned so each lines up with its author across the
  gutter. I set them beneath each author name instead, per the unit brief.

Italics preserved where the book sets them: *normal* and *average* (Preface ¶2),
*development* (Foreword ¶1), *The Authors*, *Scripta Mathematica*, and the
italic lines on the copyright page.

Nothing in this unit was illegible. No scan fallback was required.

---

## Build notes

- Compiles twice clean under tectonic. 12 pages.
- One residual warning, accepted: `Underfull \hbox (badness 1092)` in the
  two-line paragraph "Besides its mathematical completeness…". It is a loose
  line in a 145 mm measure, not a layout fault; it survives every
  `\emergencystretch` value, so it is inherent to the paragraph.
- Local macros, all inside the marker block for hoisting: `\FMplate` (framed
  plate placeholder + caption), `\FMauthor` (title-page name/affiliation),
  `\emergencystretch=1.5em`, and a `\cleardoublepage` redefinition so the blank
  verso forced before `\chapter*` carries no folio or running head (without it
  a stray "vi" printed on an otherwise empty page).
- `\pagenumbering{roman}` is set locally for the standalone build; integration
  should manage this via `\frontmatter`.
- No figures, so no `figures00.tex`, no `tools/constraints/ch00.py`, and
  `check_labels.py` / `verify_figures.py` do not apply to this unit.
- TOC: `\addcontentsline` entries emitted for Preface and Foreword to the
  Student. A comment marks where `\tableofcontents` belongs; the printed
  CONTENTS list (pp. v–viii) is deliberately not transcribed.

---

# Text review

Fresh reviewer, second pass. Sources re-rasterized and read at 150 dpi (all of
PDF 1–14) and re-cropped to 300 dpi for the Preface and Foreword prose.
**Corrections applied: 0.** The transcription is accurate. But this unit should
**not** be marked green — see the blocker first.

## BLOCKER (escalated, not resolved here) — the PD basis does not currently hold

The builder's item 1 above records the public-domain premise as "specific and
falsifiable" and proceeds on it. Since that was written, the **ch13 agent found
the recorded renewal search used the wrong window**, and I have checked its
reasoning independently. It is right, and it changes item 1 from *unverified* to
*known-defective*:

- Under the 1909 Act a pre-1964 US work had to be renewed **in the 28th year of
  its original term**. Publication here is **1960** (the Feb-1961 second
  printing neither restarts nor extends the term — confirmed on PDF 6). The
  valid renewal window therefore runs from the 1960 publication anniversary in
  **1987** to the same date in **1988**.
- `CLAUDE.md`/`STATUS.md` record the search as a **1988–91** window. That misses
  **1987 entirely** — roughly the first half of the only period in which a
  renewal could validly have been filed — and spends three years outside the
  window.
- The positive control does not repair this. A control shows the search would
  have surfaced a renewal *inside the range actually searched*; it is silent
  about 1987.
- ch13 also tried the Stanford renewal database and got an empty
  JavaScript shell, not a result. That is **inconclusive**, and must not be
  recorded anywhere as evidence of non-renewal.
- Base-rate caution: the "most copyrights were never renewed" statistic is
  driven by ephemera. A major-publisher school textbook that reached multiple
  printings and later editions is in the category *most* likely to have been
  renewed. The prior runs against non-renewal here.

**This unit is the one that reproduces the copyright page verbatim**, so the
point lands here with particular force: the page I transcribed carries a 1960
notice and an explicit all-rights-reserved statement, and the search that was
supposed to show that notice lapsed did not cover the year it would have lapsed
in. See `ch13-UNCERTAIN.md` for the full write-up and the four searches
(Stanford renewal DB; Online Books Page CCE scans for **1987 and 1988**; author
/ title / **Addison-Wesley as proprietor**; USCO Virtual Card Catalog) that
would actually settle it. Until one of those comes back clean, the honest state
of this unit is *transcription verified, permission to publish unestablished*.

`STATUS.md` currently records only the **edition** question as RESOLVED
(title page = 1960/61). That is a different question from renewal and should not
be read as clearing it.

## Accuracy pass — what was checked

Every page of the unit's range was read; the prose was read twice.

| Item | Source | Result |
|---|---|---|
| Series page, 4 consulting editors, 2-column order | PDF 3 | exact |
| Euclid plate caption (3 lines) | PDF 4 | exact |
| Title page: title, 3 author names, publisher, 2 city lines | PDF 5 | exact |
| Copyright page, all 7 elements incl. `60-8336`, `February, 1961` | PDF 6 | exact |
| Preface, 12 paragraphs, p. ix | PDF 11 @300 dpi | exact, word for word |
| Preface, p. x + sign-off | PDF 12 @300 dpi | exact, word for word |
| Foreword, 3 paragraphs + sign-off | PDF 13 @300 dpi | exact, word for word |
| Hilbert plate caption (6 lines) | PDF 14 | exact |
| Italics (2 in Preface ¶2, 1 in Foreword ¶1, sign-off, plate credits) | — | all correct |
| `\addcontentsline` after each `\chapter*` | — | both present |

Checks that returned **n/a for this unit**: exercises, exercise numbering and
data values, starred exercises / `\stex` / `\starnote`, theorem numbering, Greek
letters, subscripts, primes, congruence and similarity symbols, `\section*`
boundaries. The front matter contains no mathematics and no exercises. The one
asterisk-adjacent item is the Preface sentence describing the convention (harder
material carries an asterisk); it is prose, correctly set, and needs no
`\starnote` — the first *use* of the convention is ch01/ch02's to mark.

Page order verified against the spread photos, which is where this unit was most
at risk: PDF 1 cover, 2 blank endpaper, 3 series (p. i), **4 = frontispiece +
affiliations verso (p. ii), 5 = title recto (p. iii)** — a two-page title
spread — 6 copyright (p. iv), 7–10 CONTENTS (pp. v–viii), 11–12 Preface
(ix–x), 13 Foreword (xi), 14 Hilbert plate (xii). The tex follows this order.
Confirms builder item 4: the Foreword is **p. xi only**, and p. xii is the
plate.

## Residual doubts (all layout, none textual)

1. **The half-title is editorial, not in the book.** Confirmed: PDF 1 is the
   cloth cover, PDF 2 a blank endpaper, PDF 3 the series page. There is no
   half-title leaf. Builder item 5 stands — this is the one piece of the unit
   that is invented rather than transcribed. Drop it for strict fidelity.
2. **The title page is flush left in the original**, not centred: title, all
   three author names, the AW colophon and the three publisher lines share one
   left margin. The tex centres them. Deliberate design choice or not, it is a
   visible departure; left to integration.
3. **The Euclid caption sits to the left of the plate** in the original, not
   centred beneath it.
4. **The Foreword sign-off is an indented block**, not flush right; `The Authors`
   is further indented than `Good luck,`. The tex right-aligns both.
5. **Affiliations** — builder item 2's note is confirmed: they are printed on the
   verso, right-aligned to line up across the gutter. Placing them under each
   name is a reasonable single-page adaptation, not an error.
6. Builder item 2 (the reproduced all-rights-reserved notice needing an editorial
   line beneath it) becomes **more** important given the blocker above, not less.
   Do not write that line until the renewal question is settled — the wording
   depends on the answer.

## Cross-unit note (not mine to fix — shared file)

`sources/PAGEMAP.md`'s section list disagrees with the printed CONTENTS (PDF 7)
for ch 2: the book prints "**The** truth table for implication" (2-4), "**The**
converse of an implication" (2-5) and "**The** contrapositive of an implication"
(2-7); PAGEMAP drops the leading article in all three. Whoever owns ch02 should
check the in-chapter headings against PDF 7 and the chapter body rather than
against PAGEMAP. Confirmed correct in PAGEMAP: the star on 10-6, and every ch
9–14 section page number I could see on PDF 9 and PDF 11.

## Build

Recompiled twice under tectonic after review; unchanged and clean. 12 pp.
The single `Underfull \hbox (badness 1092)` at line 150 is the two-line
paragraph the builder documented — accepted, inherent to the measure.
