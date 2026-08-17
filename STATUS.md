# Status — 2026-08-16

| Unit          | Text                          | Figures                               | Notes                                                                                                                                                                                                                            |
| ------------- | ----------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Front matter  | not started                   | n/a                                   | TOC, intro; Aristotle plate = photo, treat as plate                                                                                                                                                                              |
| Ch 1          | not started                   | few                                   | <br />                                                                                                                                                                                                                           |
| Ch 2          | DONE (skim-verified by Caleb) | none                                  | verify starred ex., grade lists in Ex 2-15 #11                                                                                                                                                                                   |
| Ch 3–8        | not started                   | many                                  | one organic-shape figure in ch 2-or-3 region — locate in scans                                                                                                                                                                   |
| Ch 9          | needs redone                  | 52 drawn; 18 measured, 34 provisional | 16/16 constraints pass; 44 label grazes open; six hard figs (9-12, 9-14, 9-24, 9-38, 9-49, 9-51) must be rechecked, indeed all figures must be rechecked and the entire chapter needs to be redone to ensure maximial accuracy.  |
| Ch 10         | DONE (full transcription)     | 24 drawn; 163/163 constraints         | Complete 2026-08-17. Scans cover the chapter 1:1 (scan13 pp.1-16), not "half". 0 genuine collisions (6 notation artifacts, proven by move test). One open question: Review Ex. 1's fraction is cut off in the photo — see ch10-UNCERTAIN.md §2.1. |
| Ch 11, 12, 14 | not started                   | scans thorough                        | Caleb flagged these as complex                                                                                                                                                                                                   |
| Ch 13         | not started                   | <br />                                | <br />                                                                                                                                                                                                                           |
| Ch 15         | not started                   | coordinate geometry                   | scans sparse on purpose; simple figures                                                                                                                                                                                          |
| Ch 16         | not started                   | none                                  | all text; no scans exist                                                                                                                                                                                                         |
| Appendix      | not started                   | <br />                                | <br />                                                                                                                                                                                                                           |

Title-page condition: **RESOLVED 2026-08-16** — copyright page reads
"Copyright © 1960 … Second printing, February, 1961" (LCC 60-8336). Proceed.

Tooling: verify\_figures.py (constraint audit; per-chapter modules in
tools/constraints/chNN.py), check\_labels.py (collision audit, vector-based,
compiles via tectonic), overlay.py (scan-vs-redraw comparison). All in tools/.
Engine: tectonic (`cd chapters && tectonic -Z search-path=../style --outdir
../build chNN.tex`). Page map: sources/PAGEMAP.md. Scans: scans/scan01..15.pdf
symlinks (chronological); index in sources/scan-index/.
