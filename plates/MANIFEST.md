# `plates/` — extracted halftone plates and pictorial line art

Real images lifted from Caleb's own captures of the book, replacing the framed
placeholder boxes in the LaTeX restoration. **Images only — no `.tex` file was
touched.** The integration pass splices these in.

Every item was cropped to the artwork itself: **printed captions are excluded**
(the LaTeX side sets them), as are page edges, facing pages and fingers.
All files are 8-bit grayscale PNG with a small even white margin.

Total: 13 files, 8.6 MB.

## Where each image came from

The iPad scans beat the photo PDF everywhere. The photo PDF (`sources/Geometry.pdf`)
stores each page as a single ~1186×1582 px photograph of a curved, glare-lit
spread; the scans hold 1900–3200 px per page, flat and square-on. **The scans won
all 13 items.** Photo-PDF pages were rendered and compared for every item and are
listed below as the fallback that lost.

### Two scan-index entries are wrong — worth fixing

* `sources/scan-index/scan02.md` calls **p16** `trash/partial … unidentified
  halftone plate … ~65% black cutoff`. It is in fact a clean, square-on capture of
  the **Aristotle** plate with its full caption. It is the source used here.
* `sources/scan-index/scan15.md` calls **p20** `trash — unidentifiable content …
  bottom two-thirds unusable`. It is in fact a full, sharp capture of the
  **Descartes** plate. This one mattered: the documented fallback (photo PDF p.264)
  holds that plate at only ~506×636 px, which would have made Descartes the one
  genuinely weak item in the set. From scan15 p20 it is 2114×2685 px and good.

---

## Halftone plates (8)

| file | plate | source | quality |
|---|---|---|---|
| `plate-euclid.png` | Euclid frontispiece, engraved portrait (facing the title page) | `scans/scan01.pdf` p.3 | **good** |
| `plate-hilbert.png` | David Hilbert, seated portrait (leaf facing book p.1) | `scans/scan01.pdf` p.15 | **good** |
| `plate-pythagoras.png` | Pythagoras, from a fresco by Raphael (leaf near book pp.2–3) | `scans/scan01.pdf` p.19 | **good** |
| `plate-archimedes.png` | The Death of Archimedes, from a mosaic (leaf near book p.6) | `scans/scan01.pdf` p.20 | **good** |
| `plate-aristotle.png` | Aristotle, statue in a Vienna museum (facing book p.21, Ch.2 opener) | `scans/scan02.pdf` p.16 | **good** |
| `plate-gauss.png` | Karl Friedrich Gauss (leaf in Ch.8, ~facing book p.137) | `scans/scan09.pdf` p.12 | **good** |
| `plate-lobachevsky.png` | Nicolai Ivanovich Lobachevsky (leaf in Ch.8, ~facing book p.138) | `scans/scan09.pdf` p.13 | **good** |
| `plate-descartes.png` | René Descartes (facing book p.251, Ch.15 opener) | `scans/scan15.pdf` p.20 | **good** |

### `plate-euclid.png` — 1120×1454
* **Source:** `scans/scan01.pdf` p.3 (embedded image 2442×4002). Fallback not used: photo PDF p.4.
* **Crop / processing:** perspective-rectified from the quad
  (1053,180)–(2414,186)–(2414,1974)–(1053,1968), expanded 3 px outward; grayscale;
  level stretch p0.4–p99.4; resampled to 1400 px long edge; 2.5% white margin.
  Right edge located from a column-darkness profile — a first pass cut ~40 px into
  the roundel lettering and was redone.
* **Printed caption:** `EUCLID` / `Courtesy of` / *`Scripta Mathematica`*
* **Assessment:** good. Full medallion, lettering intact on both sides, engraving
  hatching crisp.

### `plate-hilbert.png` — 1349×1464
* **Source:** `scans/scan01.pdf` p.15 (2271×4114) — the square-on retake. scan01 p.14
  is the same plate shot skewed with the right edge clipped; not used. Fallback not
  used: photo PDF p.14.
* **Crop / processing:** rectified from (480,768)–(1992,750)–(2022,2418)–(498,2406),
  pad 6 px; grayscale; levels p0.3–p99.7; fit 1400; 2.5% margin.
* **Printed caption:** `DAVID HILBERT` / `(1862–1943)` / `Professor of Mathematics,` /
  `University of Göttingen, Germany` / `Perhaps the world's foremost mathematician
  during the first half of the twentieth century.` / *`Courtesy of the New York
  Public Library.`*
* **Assessment:** good. Best plate in the set — face, wicker chair and coat texture
  all hold detail.

### `plate-pythagoras.png` — 1170×1456
* **Source:** `scans/scan01.pdf` p.19 (2422×4173). Fallback not used: photo PDF p.17.
* **Crop / processing:** rectified from (378,606)–(1944,654)–(1962,2598)–(378,2622),
  pad 4 px; grayscale; illumination-flattened (divide by heavy blur, strength 0.7)
  to kill the page-curl gradient; levels p0.4–p99.0; fit 1400; 2.5% margin.
* **Printed caption:** `PYTHAGORAS` / `From a fresco by Raphael.` / `Courtesy of`
  *`Scripta Mathematica`*`.`
* **Assessment:** good. Soft chalk/fresco drawing reproduces cleanly; the page bow
  is corrected but a faint residual curve remains at the extreme left edge.

### `plate-archimedes.png` — 1462×1313
* **Source:** `scans/scan01.pdf` p.20 (1954×3338). Fallback not used: photo PDF p.18.
* **Crop / processing:** rectified from (282,690)–(1830,648)–(1836,2034)–(288,2070),
  pad 6 px; grayscale; levels p0.5–p99.5; fit 1400; 2.5% margin.
* **Printed caption:** `THE DEATH OF ARCHIMEDES` / `From a mosaic found in the
  ancient city of Pompeii.` / `Courtesy of` *`Scripta Mathematica`*`.`
* **Assessment:** good. Individual mosaic tesserae are resolved across the whole
  panel including the vine border. Brightest tesserae clip slightly — that clipping
  is in the book's own halftone, not introduced here.

### `plate-aristotle.png` — 1007×1448
* **Source:** `scans/scan02.pdf` p.16 (1901×3009) — see the index-correction note
  above. Fallback not used: photo PDF p.34 (visibly softer).
* **Crop / processing:** rectified from (450,408)–(1590,396)–(1578,2082)–(426,2070),
  pad 6 px; grayscale; levels p0.3–p99.7; fit 1400; 2.5% margin.
* **Printed caption:** `ARISTOTLE` / `A view of a statue in a Vienna museum.` /
  `Courtesy of` *`Scripta Mathematica`*`.`
* **Assessment:** good, with one caveat — shadow detail in the dark background is
  slightly crushed. The plate as printed is a very dark halftone, so most of that is
  faithful; if you want the background mottling to read more openly, this is the one
  image where a lighter re-grade would help. The bust itself is correctly exposed.

### `plate-gauss.png` — 1196×1456
* **Source:** `scans/scan09.pdf` p.12 (2117×3731). Fallback not used: photo PDF p.151.
* **Crop / processing:** rectified from (217,496)–(1635,478)–(1640,2225)–(222,2233),
  pad 3 px; grayscale; flatten 0.6; levels p0.4–p99.3; fit 1400; 2.5% margin. Bounds
  taken from a dark-fraction profile at threshold 200 so the plate's light outer rule
  is kept, not just the dark image core.
* **Printed caption:** `KARL FRIEDRICH GAUSS` / `(1777–1855)` / `Probably the first
  mathematician to recognize the existence of non-Euclidean geometries.` /
  `Courtesy of` *`Scripta Mathematica`*`.`
* **Assessment:** good. The engraving's octagonal corner chamfers are fully within
  the crop; stipple in the coat and face is clean.

### `plate-lobachevsky.png` — 965×1454
* **Source:** `scans/scan09.pdf` p.13 (2301×3478). Fallback not used: photo PDF p.152.
* **Crop / processing:** the four printed border rules were located by edge-scanning
  35 rows and 22 columns and least-squares fitted; the four line intersections gave
  the quad (602.7,614.5)–(1951.3,588.4)–(1871.2,2681.9)–(569.0,2597.9). That is a real
  keystone (top edge 1349 px, bottom edge 1302 px), so the perspective transform is
  doing genuine work. Then grayscale; flatten 0.6; levels p0.4–p99.3; fit 1400;
  2.5% margin. A first pass showed the printed rule on the top and right only; the
  border fit put it evenly on all four sides.
* **Printed caption:** `NICOLAI IVANOVICH LOBACHEVSKY` / `(1793–1856)` /
  `Co-inventor, with Johann Bolyai, of non-Euclidean geometry.` / `Courtesy of`
  *`Scripta Mathematica`*`.`
* **Assessment:** good. Square, evenly framed, medals and epaulettes legible.

### `plate-descartes.png` — 1109×1462
* **Source:** `scans/scan15.pdf` p.20 (3195×5414) — see the index-correction note
  above. Fallback rejected: photo PDF p.264, where the plate is only ~506×636 px.
* **Crop / processing:** border-rule fit as for Lobachevsky, restricted to the
  y-range where the right-hand rule is clean (the scan's lower right is contaminated
  by a page artifact that corrupted a first fit). Quad
  (624.9,1128.8)–(2749.9,1076.6)–(2358.3,3825.1)–(465.7,3723.8) — a strong keystone
  (top edge 2125 px, bottom edge 1892 px) from the tilted capture, fully corrected.
  Grayscale; flatten 0.6; levels p0.4–p99.4; fit 1400; 2.5% margin.
* **Printed caption:** `RENÉ DESCARTES` / `(1596–1650)` / `Courtesy of`
  *`Scripta Mathematica`*`.`
* **Assessment:** good. This was the item most at risk and it came out well —
  the engraving's line work in the hair, collar and background hatching is fully
  resolved. **No re-shoot needed.**

---

## Pictorial line art (5)

High-contrast grayscale (not bilevel — bilevel broke up the stipple fills in
Figs. 5-1 and 3-15). Pipeline for all five: crop → grayscale → illumination-flatten
at full strength → level stretch p1.5–p99.9 so paper reads pure white and ink pure
black → unsharp mask (radius 1.0, 90%, threshold 3) → 5% white margin → paper-white
lift (values ≤188 untouched, 188–214 smoothly ramped to 255, ≥214 clamped to 255).
That last step clears the faint grey blotching the flatten left on the paper in
Figs. 1-23 and 4-1; because it only touches the near-white band it leaves ink and
the Fig. 5-1 / 3-15 stipple fills intact. Pure-white coverage afterwards is
85–92% per file. The `FIGURE n-m` caption line is cropped out of every one.

| file | figure | subject | source | native crop | eff. dpi at printed size | quality |
|---|---|---|---|---|---|---|
| `fig-1-23.png` | Fig. 1-23 (book p.16) | hand balancing a triangle at the median intersection | `scans/scan02.pdf` p.12 | 358×331 | ~434 dpi @ 21 mm | **good** |
| `fig-3-15.png` | Fig. 3-15 (book p.49) | three men A, B, C on a sight line | `scans/scan04.pdf` p.10 | 807×332 | ~402 dpi @ 51 mm | **good** |
| `fig-4-1.png` | Fig. 4-1 (book p.63) | boy beside a marked spear on hatched ground | `scans/scan05.pdf` p.6 | 458×406 | ~463 dpi @ 25 mm | **good** |
| `fig-5-1.png` | Fig. 5-1 (book p.73) | man pacing off a building | `scans/scan05.pdf` p.18 | 592×443 | ~376 dpi @ 40 mm | **good** |
| `fig-14-2.png` | Fig. 14-2 (book p.237) | jet aircraft and an automobile | `scans/scan15.pdf` p.4 | 1130×717 | ~617 dpi @ 47 mm | **good** |

Effective dpi is measured against the figure's width **as printed in the book**
(px/mm derived from the text-measure on the same scan page, taken as 108 mm). All
five clear the 300 dpi target comfortably, so none was upsampled — each file is at
its native captured resolution.

Crop rectangles, in source-page pixels:

* `fig-1-23.png` — (528,304)–(886,635) on scan02 p.12.
* `fig-3-15.png` — (588,2233)–(1395,2565) on scan04 p.10. `scan04.md` describes this
  page as "partial (bottom half black/cut off)", which is true of the page but not of
  the figure: Fig. 3-15 sits entirely in frame. A first crop was 100 px too high and
  swallowed the body-text line above while clipping the men's feet and the A/B/C
  labels; re-measured from a zoomed grid overlay.
* `fig-4-1.png` — (1300,1946)–(1758,2352) on scan05 p.6. Widened from a first attempt
  after a column profile showed the hatched groundline runs ~40 px past the boy and
  spear on both sides.
* `fig-5-1.png` — (1098,1462)–(1690,1905) on scan05 p.18. Bottom edge set at 1905 from
  the ink-gap between the groundline (ends y≈1898) and the caption (starts y≈1930);
  an earlier pass to 1934 caught the tops of the caption glyphs.
* `fig-14-2.png` — (530,448)–(1660,1165) on scan15 p.4.

---

## Honest summary

**No item failed, and nothing needs a re-shoot.** All 13 rank *good*; none is
*acceptable* or *poor*.

The one image with a real caveat is **`plate-aristotle.png`**, whose dark background
is slightly shadow-crushed. That is largely faithful to a very dark original halftone
and the subject itself is well exposed, so it is not a re-shoot candidate — at most a
lighter re-grade if you dislike it.

Two risks that were anticipated did **not** materialise:

* The **Descartes** plate was expected to be the weak one, since the only documented
  source (photo PDF p.264) carries it at ~506×636 px. A mis-indexed scan page
  (scan15 p.20) turned out to hold it at 2114×2685 px.
* The **Aristotle** plate had no indexed scan coverage at all; scan02 p.16, indexed as
  trash, is a clean capture of exactly that plate.

Sizes: the eight halftone plates are ~0.8–1.3 MB each as PNG, because screened
halftone texture does not compress. If `build/book.pdf` gets uncomfortably large,
converting the eight plates (not the line art) to quality-90 JPEG would cut roughly
7 MB with no visible loss on a halftone.
