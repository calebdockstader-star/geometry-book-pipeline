# Status — 2026-08-17 — COMPLETE

**`build/book.pdf` — 467 pages, 145×200 mm, compiles twice clean.**
Every unit transcribed verbatim, every figure drawn and reviewed.
Open items for Caleb: `OPEN-QUESTIONS.md` (decisions + two physical-copy
checks). Per-chapter detail: `chapters/*-UNCERTAIN.md`.

| Unit | Text | Figures | Reviews |
|---|---|---|---|
| Front matter | done (plates as placeholders) | n/a | text ✓ |
| Ch 1–16 | done, verbatim incl. the book's own errata | 380+ figures, all constraint-checked | fresh text + figure reviews on every chapter |
| Appendix | done, verbatim (restored 2026-08-17) | 1 figure | restore + adversarial verify ✓ |
| Index | NOT transcribed (page numbers invalid in re-typeset edition) | — | decision in OPEN-QUESTIONS §1.4 |

Book-wide gates at delivery:
- `python3 tools/verify_figures.py` → **2038/2038 constraints hold**
- `check_labels.py` → **0 collisions** in every chapter
- placeholder grep (`pending{`/`todo{`) → empty
- exercise-numbering simulation (all exlists, all chapters) → 0 defects
- full visual page-through completed (448-page build + re-check of changed
  regions in the 467-page final)

Copyright: **US public domain since Jan 1, 1989** — verified with positive
controls; evidence in `sources/copyright/renewal-search.md`.

Tooling: tectonic engine; per-chapter constraints in `tools/constraints/`;
`tools/check_labels.py` much improved this run (true line endpoints, Bézier
flattening, white-fill masks, notation-rule filter, sub/superscript merging);
`tools/assemble_book.py` generates `book.tex` (counter resets, raggedbottom,
emergencystretch, local-macro hoisting, TOC splice) — edit chapters, re-run it.
Page map: `sources/PAGEMAP.md`. Scans: `scans/scan01..15.pdf` symlinks,
indexed in `sources/scan-index/`.
