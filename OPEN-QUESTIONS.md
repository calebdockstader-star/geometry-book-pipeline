# Open questions — Brumfiel *Geometry* restoration

Updated 2026-08-17 after Caleb answered the first round. Everything he
answered is now **done**; the short list at the top is what is genuinely still
open. Per-chapter detail lives in `chapters/*-UNCERTAIN.md`.

***

## STILL OPEN — needs Caleb

1. **One photo would finish the index.** The book's index runs onto **p. 287**
   (roughly *Right angles* through the space-geometry entries), and that page
   was never captured — it appears only edge-on in the curl of the last PDF
   frame, right column entirely absent, and the iPad scans stop at p. 263. The
   index therefore ends mid-R. **A phone photo of p. 287 — and p. 288 if the
   index continues — closes it**, and it splices in without touching anything
   else.

2. **Page count.** The book went 465 → **526 pages**. Roughly all of that is
   the single-column exercise groups that inline figures require at this trim
   (ch01 20→35, ch08 24→34). The figures themselves are not bloated — the
   median figure is 0.47 of the measure against the book's own ~0.48. If you
   would rather have the tighter book, the alternative is column-width figures
   inside two-column groups, which costs figure size. Say the word either way;
   nothing else depends on it.

3. **Two small readings only your copy settles** (both currently drawn the way
   the book appears to print them):
   * **Fig 15-14** — does a dashed perpendicular drop from Q to the x-axis? A
     short stroke appears at x₂ in both plate and scan, but at full zoom it
     reads as a stray tick.
   * **Fig 14-29** — the angle marks are thin slivers in the print; we read
     both vertices at the left end of each horizontal edge. Mirrors trivially.

***

## Done — your answers, applied

| You said | What happened |
|---|---|
| *"DO THIS, I WANT ALL OF THE LINE ART INCLUDED FAITHFULLY"* | All 6 pictorial figures are now scan crops: 1-23, 3-15, 4-1, 5-1, **7-17** (the compass — added to the list; our version was an admitted interpretation) and 14-2. |
| *"TRANSCRIBE THIS WITH NEW PAGE NUMBERS"* (index) | 333 entries transcribed verbatim and re-keyed to this edition by locating each entry's own words inside the chapter its original reference pointed into. 91% resolved that way, 2 by interpolation. |
| *"INCREASE THE DIAGRAM SIZE INSTEAD OF DECREASING THE LABEL SIZE"* | Every figure measured by real ink extent and fitted to the measure. What actually fixed ch09 was splitting the combined macros — Fig 9-23 went 1.3 cm → 5.2 cm of drawn width. |
| *"(-5,-7)"* (Ex 15-7 #16) | Confirmed; the earlier reviewer's lean toward −6 is withdrawn. |
| *"LABEL IS C NOT C'"* (Fig 9-41) | Confirmed against a 500 dpi plate. |
| *"THE 1 TICK NOT BEING PERPENDICULAR TO THE LINE CA"* (Fig 13-17) | Fixed and asserted as a constraint. It had been struck 25° off lying *along* CA, which is exactly why those ticks blurred into a blob. |
| *"KEEP IT"* (half-title) | Kept. |
| *"YEAH GO AHEAD AND ADD IT"* (rights line) | Added under the reproduced 1961 notice. |
| *"I WANT THE ACTUAL HALFTONE PICTURES IN THERE"* | All 8 plates now print the real image from your own scans. |
| *"DON'T WORRY ABOUT THIS"* (display headings) | Left alone. |
| *"NOT A PROBLEM"* (title-page alignment) | Left alone. |

**The four you didn't answer, handled on my stated recommendations** — say so
if you'd rather have any of them the other way: errata reproduced as printed
**plus** the new errata appendix; the book's own segment-overbar
inconsistency kept; running heads accepted as house style; corollary heads set
in italic. Figs 12-28/29/30 and 9-48 reverted to schematic so a ruler no
longer answers those exercises.

***

## Things I changed that you should know about

* **Your text had one real error.** Ex Gp 6-14 #8 read `DE ≅ AC`; your book
  prints `DE ≅ EC`. Verified at 260 dpi on your own scan of p. 110 before
  changing it. Corrected in place — it is our slip, not the book's, so it is
  not in the errata appendix.

* **Two notes from your photos were wrong, and I did not apply them.** Fig
  11-11: the hexagons really are 30° apart and the radius really does carry an
  arrowhead running horizontally right. Three sources agree (flat scan, photo
  PDF, your own photo once de-rotated) — the phone shot caught that page
  mid-curl. Fig 9-12's numerals are segment lengths, not angles, so the
  "missing arcs" there are correctly absent.

* **A gate was lying.** Fig 6-110 drew a 66° "right angle" and passed a 100%
  constraint check, because ch06's reader couldn't parse tikz projection
  syntax — so every dropped perpendicular in that chapter was silently
  unchecked. Fixed at the root. Worth knowing that ch06 is the only chapter
  reading coordinates from the tex; the other fourteen hard-code them, so a
  figure edited without updating its constraints would still report green.

* **Two label collisions remain**, both `B′` in ch04 Figs 4-10/4-12, where the
  arc crosses the label's metric box rather than the visible letter. The
  book's plate grazes identically. Reported rather than rounded to zero.

* **Two scan-index entries were wrong** and are corrected: scan15 p20 and
  scan02 p16 were logged as trash but are in fact the Descartes and Aristotle
  plates — and the only usable sources for them.
