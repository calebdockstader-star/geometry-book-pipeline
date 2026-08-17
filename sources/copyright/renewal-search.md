# Copyright renewal search — Brumfiel/Eicholz/Shanks, *Geometry* (Addison-Wesley)

Performed 2026-08-17 ~02:50 MDT, replacing the earlier under-documented search.
Conclusion: **no renewal exists; the work entered the US public domain on
January 1, 1989.**

## The work

- *Geometry*. Charles F. Brumfiel, Robert E. Eicholz, Merrill E. Shanks.
  Addison-Wesley Publishing Company, Inc.
- Copyright page of Caleb's physical copy (also sources/Geometry.pdf p.6):
  "Copyright © 1960 … Printed in the United States of America …
  Library of Congress Catalog Card No. 60-8336. Second printing, February 1961."
- **© 1960**, not 1961 (the second printing is not a new copyright).

## Legal frame

- US work published 1960 with notice → 1909 Act, 28-year first term.
- 17 U.S.C. §305: pre-1978 terms run to Dec 31 of the expiry year → first term
  ended **Dec 31, 1988**.
- §304(a): renewal had to be filed **within the final calendar year, i.e. 1988**
  (registrations were also accepted somewhat early in practice; the sweep below
  covers 1986–1991 to moot every interpretation).
- Renewal was NOT automatic for pre-1964 works (the 1992 automatic-renewal
  amendment covers 1964–77 only). No renewal in the window → PD on Jan 1, 1989.
- USCO records from 1978 forward are complete in electronic form, so for a
  1988-window work a clean null in those records is dispositive — unlike
  print-era CCE nulls.

## Dataset

NYPL `cce-renewals` (github.com/NYPL/cce-renewals), files
`data/1986-from-db.tsv` … `1991-from-db.tsv` — these are the US Copyright
Office's own post-1977 electronic renewal records (not scanned print CCE).
Local copies in `sources/copyright/nypl-data/` (128,902 records across the six
files). TSV fields include author, title, original reg no./date, renewal
no./date, claimant(s).

## Queries and results (reproduce with grep from nypl-data/)

| Query | Files | Result |
|---|---|---|
| `grep -i brumfiel` | 1986–1991 | **1 hit**: *Principles of arithmetic* (A616889, orig. 1963-03-25) renewed 1991-11-19, RE552863, claimant Charles F. Brumfiel. Different book. |
| `grep -i eicholz` | 1986–1991 | same single hit |
| `grep -i shanks` ∩ `geometr` | 1986–1991 | **0 hits** |
| `grep -i eometr` ∩ orig-date 1960 | 1986–1991 | 13 hits — other publishers' geometry texts; none is this work |
| claimant contains "Addison" | 1987–1988 | no Addison-Wesley-as-claimant renewals (the era's renewals were author-filed) |

## Positive controls (why the null is trustworthy)

1. **Window density**: the 1988 file alone holds **21,418 renewals of
   1960-registered works** — the window and dataset behave exactly as the law
   predicts.
2. **Same publisher, same year, same genre**: George B. Thomas,
   *Calculus and Analytic Geometry* (Addison-Wesley, A436966, orig. 1960-03-18)
   **was** renewed — RE396444, 1988-09-30, by the author. Addison-Wesley
   authors who renewed in the window appear in this data.
3. **Same authors**: Brumfiel's own 1991 renewal of the 1963 *Principles of
   Arithmetic* shows these specific authors' filings surface in this dataset —
   and that they renewed selectively, not as a matter of course.

## Conclusion

No renewal was filed for *Geometry* (© 1960) in or around its statutory 1988
window, while the dataset demonstrably captures its publisher's, its genre's,
and its own authors' renewals. First-term copyright expired Dec 31, 1988; the
work is in the **US public domain** (since Jan 1, 1989). The transcription
project may proceed. (Caleb also owns the physical copy; the project is
personal/educational, which this finding makes moot.)

## Correction to earlier project notes

CLAUDE.md previously said "1961 US publication … 1988–91 window". The work is
© 1960 and the operative window is calendar 1988 — which the 1988–91 sweep did
include, so the earlier null was directionally right but under-documented and
mislabeled. This file supersedes it.
