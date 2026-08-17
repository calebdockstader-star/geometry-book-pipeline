# Brumfiel *Geometry* (1960) — LaTeX restoration

A complete, re-typeset edition of Brumfiel, Eicholz & Shanks, *Geometry*
(Addison-Wesley, 1960): full text, ~420 figures redrawn as vector art, plus
an errata list and the book's own index re-keyed to this edition's pages.

Output: `build/book.pdf` — 526 pp, 145×200 mm, black and white.

## Rights

**US public domain since 1 January 1989.** The book was published in 1960 with
copyright renewal due in calendar 1988; a sweep of the Copyright Office's
electronic renewal records finds no renewal under any author, the title, or
Addison-Wesley — while the same dataset does contain other Addison-Wesley
renewals from the period, confirming the search was sound. Full evidence and
reproduction commands: [`sources/copyright/renewal-search.md`](sources/copyright/renewal-search.md).

This is a US determination. Elsewhere the term may differ.

## Build

No TeX Live needed — [tectonic](https://tectonic-typesetting.github.io/) only:

```sh
python3 tools/assemble_book.py
tectonic -Z search-path=style -Z search-path=chapters --outdir build book.tex
```

Individual units build standalone: `cd chapters && tectonic -Z search-path=../style --outdir ../build ch06.tex`

## Checks

Figures are constrained, not eyeballed — every stated hypothesis (parallel,
perpendicular, midpoint, bisector) is asserted numerically and must hold.

```sh
python3 tools/verify_figures.py                      # 2298/2298 constraints
python3 tools/check_labels.py chapters/figures06.tex 6   # label/geometry collisions
```

## Not included

The source photographs and scans of the physical book are local-only, so the
symlinks in `scans/` are dead in a fresh clone. Everything needed to *build*
the edition is here; the sources are only needed to revise figures.

Working notes (build status, open questions, agent conventions) are kept
locally and are not part of this repo.
