# Open questions for Caleb — Brumfiel *Geometry* restoration

Consolidated 2026-08-17 from every `chapters/*-UNCERTAIN.md` (the full per-
chapter files remain on disk with complete detail and evidence). Everything
here is a **decision or a check only you can make** — nothing below blocks
reading or using the book as it stands. Where I have a recommendation it is
marked **→**.

---

## 0. Settled — the copyright question

The book is **© 1960, US public domain since January 1, 1989**. The statutory
renewal window (calendar 1988) was swept in the USCO's own electronic renewal
records (complete for post-1977 filings) across 1986–1991: no renewal exists
under any author, the title, or Addison-Wesley as claimant — while the same
dataset demonstrably contains Addison-Wesley's renewed 1960 Thomas *Calculus*
and Brumfiel's own renewed 1963 *Principles of Arithmetic*. Evidence and
reproduction commands: `sources/copyright/renewal-search.md`. Several agents
independently re-ran the greps and concurred. (Two physical copies exist: the
teacher's photo copy is the 2nd printing, Feb 1961; your scanned copy is the
4th printing, June 1964. Same © 1960 edition either way; printings don't
affect the term.)

---

## 1. Book-wide editorial policies (decide once, applied everywhere)

1. **Printer's-slip policy.** The fleet's standing default was *faithful
   transcription*: every verified slip in the 1960 printing is reproduced
   as printed, each marked with a source comment in the tex. The full catalog
   is in §3 below. Options: (a) keep all as printed; (b) keep as printed +
   an errata appendix in the back matter; (c) silently correct.
   **→ (b)** — it preserves fidelity and helps your kids when a proof
   references the wrong figure.
2. **Segment-overbar normalization.** The book is erratic (e.g. Theorem 7-2
   bare vs Theorem 7-3 barred; ch04 prints segments unbarred throughout while
   ch09's pages bar them). Current state matches each page of the source
   exactly. **→ keep the book's own inconsistency** (it's part of the book).
3. **Pictorial line-art (not geometric diagrams, not halftone plates).**
   Five figures are drawings of people/objects:
   - Fig 1-23 (hand balancing a triangle) — drawn, hand stylized
   - Fig 3-15 (three men on a sight line) — framed placeholder
   - Fig 4-1 (boy with spear) — framed placeholder
   - Fig 5-1 (man pacing off a building) — framed placeholder
   - Fig 14-2 (jet aircraft + automobile) — drawn, silhouettes approximate
   Options per figure: keep placeholder/stand-in, crop the scan as a raster
   image, or redraw properly. **→ crop from scans as raster images** — it's
   faithful, fast, and B&W-safe; say the word and it's one small pass.
4. **The index (book pp.283–287).** Not transcribed — a re-typeset edition
   invalidates its page numbers. Options: omit; regenerate mechanically with
   `makeidx` keyed to the book's own terms (best result, most work); or
   include facsimile pages. **→ regenerate later as a follow-up**; the book
   is fully usable without it.
5. **Figure lettering size.** Our labels run ~2× the book's size relative to
   the drawings (US textbook trim → 145 mm). This single fact drives most of
   the small label-placement deviations the reviewers logged. Fix would be a
   smaller figure font book-wide (e.g. a `\tiny` variant of `slab`).
   **→ leave as is** — current labels are legible at print size; the book's
   own were often cramped.
6. **Running heads & chapter openers.** House style prints the chapter title
   on every page (the book alternates chapter title verso / section title
   recto) and drops the small "CHAPTER N" line above opener titles. Both are
   consistent across all 18 units. **→ accept as house style.**
7. **Display-heading style.** The book centres REVIEW OF CHAPTER N / ALGEBRA
   REVIEW / Test 1 etc.; some chapters set them centred (ch04/ch05 via local
   macros), others left-aligned (`\section*`). **→ standardize centred in a
   future typographic pass** (cosmetic only).
8. **Corollary head weight.** The book italicizes "Corollary" heads; our style
   file sets them bold like theorems. One-line fix in `style/brumfiel.sty`.
   **→ apply the one-liner** in the next pass.

---

## 2. Needs one glance at the physical copy (nothing else can settle these)

- **Ex. 15-7 #16 (book p.257):** second point is **(−5, −7) or (−6, −7)**.
  Photo is soft; no scan of p.257 exists. Currently (−5, −7); the second
  reviewer leans −6.
- **Fig 9-41 (book p.172):** is the apex labelled **C or C′**? Currently C
  (the proof text says C). 400 dpi couldn't resolve an accent.
- *(Optional)* re-shoot book pp.230–232 & 234 (ch13's only unscanned figure
  pages) and p.257 — everything else has scan or sharp-photo coverage.

## 2b. One figure nobody could decode

- **Fig 13-17** (SSA construction, Ex 13-5 *3): reproduced faithfully, but
  neither the builder nor the reviewer could say what the **triple-ticked
  cross-segment** denotes. If you remember this figure from high school,
  you'd settle it in a minute.

---

## 3. The book's own errata (verified real ink, reproduced as printed)

Confirmed at 300–450 dpi, most double-sourced (photo + scan). Each has a
comment at its site in the tex so no later pass "fixes" it silently.

| Where | The book prints | Should read |
|---|---|---|
| p.33, Ex Gp 2-12 #10 | "opposite **lines** of the line l" | sides |
| p.33, Ex Gp 2-12 intro | "equival**a**nce" | equivalence (normalized in tex — flag if you want the typo kept) |
| p.35, §2-8 | a duplicated "If both of these statements are true" clause | (compositor duplication) |
| p.64, §4-1 | "in **the** Section 4-2" | in Section 4-2 |
| p.95, Thm 5-4 | third length unbarred where first two are barred | consistency |
| p.119 | "any two segments**,** are either congruent" | stray comma |
| p.126, Constr 7-3 | "△ABC ≅ A′B′C′" | missing △ |
| p.130, Ex Gp 7-8 #8 | "sides of A" | sides of ∠A |
| p.135, Second Proof | "referring to **Fig. 8-2**" | Fig. 8-3 (angles 1,2 live there) |
| p.147 | "Exercise Group **8-1**" | 8-11 (both reviewers **→ recommend correcting** this one — it's a navigation label) |
| p.180 | "Fig. **9-2**" | Fig. 10-2 (has a transcriber's footnote — confirm you want it) |
| p.204 (ch11) | Shanks's π computation dated "17th century" | 19th (1873) |
| p.197, Ex Gp 11-5 #7 | "center of the inscribed **polygon**…" | circle (both places) |
| p.205 | "Remark**.** 2." | Remark 2. (normalized in tex) |
| p.231, Def 13-2 | union = "all points of S₁ **and** S₂" | or (the book's loose phrasing) |
| p.233, Thm 13-7 | three parallelogram names in inconsistent cyclic order | (as printed) |
| p.235, Rev Ex 3 | first AB unbarred, next two barred | consistency |
| p.242, Thm 14-12 | "AB/**A′B**" | A′B′ (missing prime) |
| p.244, Def 14-6 | "polygon P₁P₂…P_{**n−1**}" | P_n |
| p.244, Thm 14-13 hint | "∠CAV ≅ ∠BAV" (both at A) | angles at V expected |
| p.253ff, Fig 15-14 | P₂ labelled (x₂, **y₁**) — same as Q | (x₂, y₂). **→ recommend correcting** — the transcribed prose now visibly contradicts the figure |
| p.262, Ex 15-11 #1 | vertices (2,6),(5,7),(−8,−2) are **not** a right triangle | no single-digit fix reconstructs one; genuine book error |
| p.268 (ch16) | Berkeley "17th-century" | 18th |
| p.270 | Uranus perturbations "early in the 18th century" | 1840s |
| p.268 fn | "Baltimore: … Co., Baltimore, 1937" | city named twice |
| pp.259–260 | (noted) footnote falls back to † because * is taken by starred theorems | (by design — preserved) |

Also preserved: the book's own =/≅ mixing (ch06 several sites), the
self-congruence △ABE ≅ △ABE on p.184 (a genuine Greek-style dissection
argument — do not "fix"), and Ex 9-33's swapped D/E pairing vs its exercise.

---

## 4. Figure judgment calls awaiting your preference

- **Exact-numbers vs book's-schematic shapes.** Project rule draws quoted
  lengths exactly; in three ch12 figures (12-28/29/30) and ch09's 9-48 this
  makes the drawing *reveal the exercise's answer* where the book's schematic
  concealed it. **→ revert those four to schematic** so the exercises stay
  honest for your kids; everything else stays exact. Say the word.
- **Fig 9-38 hexagon pose** is a fit (rotate −30°, scale 0.72), similarity
  exact by construction. Fine as is.
- **Fig 10-23**: the book draws three straight dashed lines through P that
  cannot all be truly straight; ours kinks slightly at P because it is
  truthful. Kept truthful.
- **Fig 11-8/11-9** drawn at two different scales so both fit one line (book
  draws them equal). Equalizing needs the smaller figure font (§1.5).
- **Fig 11-11**: radius arrow stopped at the circle (book runs it to the
  circumscribed hexagon's vertex despite calling it 1). Kept mathematical.
- **Fig 5-10**: the book's own plate draws AB's unit ~20% larger than the CD
  it equals; ours enforces AB = 3·CD exactly. Kept exact.
- **ch06 figure notes** — see `chapters/ch06-UNCERTAIN.md` (finisher's last
  results land there; the five scan-rebuilt figures 6-42/6-56/6-92/6-112/6-126
  are solid).

---

## 5. Front matter details

- A **half-title leaf** was added editorially; the book has none (cover →
  endpaper → series page). **→ drop it for strict fidelity** — your call.
- The reproduced 1961 rights notice should carry a small editorial line so it
  isn't read as this edition's own claim. Suggested: *"The notice above is
  reproduced from the 1961 printing. This restored edition derives from a
  work in the US public domain (see renewal search, 2026)."* **→ add it.**
- Title page is centred; the book sets it flush left. Euclid caption sits
  beneath the plate; the book sets it to the left. Cosmetic; both flagged.

---

## 6. Already-handled things you may hear about (no action)

- The starred-exercise convention footnote prints **once**, in ch02, as the
  book does. Five chapters' spurious copies were removed by reviewers.
- The Aristotle/Hilbert/Descartes/Gauss/Lobachevsky/Euclid halftones are all
  placed exactly once, as plates with verbatim captions.
- Exercise-numbering (the `\item[\stex]` counter trap) was audited book-wide
  by simulation; every list now prints 1, 2, 3, … correctly.
- Counters (theorems, definitions, footnotes) reset per chapter in the
  assembled book; the TOC is auto-generated and matches the printed
  contents-page wording.
