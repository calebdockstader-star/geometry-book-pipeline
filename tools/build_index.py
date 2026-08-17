#!/usr/bin/env python3
"""
build_index.py -- re-key the book's own index to THIS edition's pagination.

Caleb's answer to OPEN-QUESTIONS 1.4 was "TRANSCRIBE THIS WITH NEW PAGE
NUMBERS".  The book's index is a genuine editorial artefact -- somebody chose
which occurrence of "betweenness" is the one worth pointing at -- so we keep
its entries and its structure and only move the numbers.

Inputs
    chapters/bookindex-terms.tsv   level<TAB>term<TAB>pages   (as printed)
    build/book.pdf                 this edition, already compiled
    build/book.toc                 gives our page for each chapter
    sources/PAGEMAP.md             gives the ORIGINAL page range per chapter

Method.  A printed page number is not something you can translate by
arithmetic -- our measure, figure sizes and page breaks all differ.  What is
stable is *which chapter* a reference lands in, and the words on the page.  So
for each original page reference we
  1. find the chapter that original page falls in (PAGEMAP),
  2. take that chapter's page span in our book (book.toc),
  3. search our pages in that span for the entry's own words, and
  4. fall back to proportional interpolation within the chapter when the words
     cannot be found (an index entry may name a concept the page discusses
     without using the exact heading).
Every fallback is logged so the result can be audited rather than trusted.

    python3 tools/build_index.py            # writes chapters/bookindex.tex
    python3 tools/build_index.py --report   # also print per-entry resolution
"""
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMS = os.path.join(ROOT, 'chapters', 'bookindex-terms.tsv')
PDF = os.path.join(ROOT, 'build', 'book.pdf')
TOC = os.path.join(ROOT, 'build', 'book.toc')
PAGEMAP = os.path.join(ROOT, 'sources', 'PAGEMAP.md')
OUT = os.path.join(ROOT, 'chapters', 'bookindex.tex')


def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]+', ' ', s.lower()).strip()


def page_texts():
    """(normalised, raw) text of every page of our book, 1-indexed.

    The normalised copy is for matching index terms; the raw copy keeps the
    column layout the printed Contents needs to be parsed.
    """
    r = subprocess.run(['pdftotext', '-layout', PDF, '-'],
                       capture_output=True, text=True)
    pages = r.stdout.split('\f')
    return ({i + 1: norm(t) for i, t in enumerate(pages)},
            {i + 1: t for i, t in enumerate(pages)})


def our_chapter_starts(raw_pages=None):
    """{chapter number: our first page}.

    Read off our own printed Contents rather than the .toc: tectonic discards
    intermediates unless asked to keep them, and the printed table is the thing
    a reader actually uses, so if the two ever disagree the printed one wins.
    Falls back to the .toc when it happens to be on disk.
    """
    starts = {}
    if raw_pages:
        for p in sorted(raw_pages)[:14]:          # Contents lives in the front
            for line in raw_pages[p].splitlines():
                m = re.match(r'\s*(\d{1,2})\.\s+([A-Za-z][^.]*?)\s*\.{2,}\s*(\d{1,3})\s*$',
                             line)
                if not m:
                    m = re.match(r'\s*(\d{1,2})\.\s+([A-Za-z][A-Za-z ,\-]{3,40}?)\s{2,}(\d{1,3})\s*$',
                                 line)
                if m:
                    ch, page = int(m.group(1)), int(m.group(3))
                    if 1 <= ch <= 16 and ch not in starts:
                        starts[ch] = page
    if starts:
        return starts
    if os.path.exists(TOC):
        for m in re.finditer(
                r'\\contentsline\s*\{chapter\}\s*\{(.+?)\}\s*\{(\d+)\}',
                open(TOC).read(), re.S):
            label, page = m.group(1), int(m.group(2))
            cm = re.match(r'\s*(\d+)\.', re.sub(r'\\[a-zA-Z]+\s*', '', label))
            if cm:
                starts[int(cm.group(1))] = page
    return starts


def book_chapter_ranges():
    """{chapter number: (first original page, last original page)}.

    PAGEMAP.md writes its ranges with en-dashes, not hyphens.
    """
    out = {}
    dash = r'[-\u2012\u2013\u2014]'
    for line in open(PAGEMAP):
        m = re.match(r'\|\s*Ch\s*(\d+)[^|]*\|\s*(\d+)\s*' + dash + r'\s*(\d+)\s*\|',
                     line)
        if m:
            out[int(m.group(1))] = (int(m.group(2)), int(m.group(3)))
    return out


def parse_terms():
    rows = []
    for line in open(TERMS):
        if line.startswith('#') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 2:
            continue
        level = int(parts[0])
        term = parts[1]
        pages = parts[2] if len(parts) > 2 else ''
        rows.append((level, term, pages))
    return rows


def expand(pages):
    """'45-47, 51' -> [(45,47-ish tokens)] keeping the printed form."""
    toks = []
    for tok in pages.split(','):
        tok = tok.strip()
        if not tok:
            continue
        m = re.match(r'^(\d+)\s*-+\s*(\d+)$', tok)
        if m:
            toks.append(('range', int(m.group(1)), int(m.group(2)), tok))
        else:
            m2 = re.match(r'^(\d+)(.*)$', tok)
            if m2:
                toks.append(('one', int(m2.group(1)), None, tok))
    return toks


class Resolver:
    def __init__(self):
        self.pages, self.raw = page_texts()
        self.ourch = our_chapter_starts(self.raw)
        # The Contents gives PRINTED folios; pdftotext gives SHEET indices, and
        # the front matter puts ~20 roman-numbered sheets in front of printed
        # page 1.  Searching sheet 133 for what is printed on page 133 lands
        # twenty pages early, so map folio -> sheet off the printed numbers.
        self.folio = {}          # sheet index -> printed folio
        self.sheet = {}          # printed folio -> sheet index
        for idx, txt in self.raw.items():
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            for cand in (lines[:2] + lines[-2:]):
                m = re.match(r'^(\d{1,3})\b', cand) or re.search(r'\b(\d{1,3})$', cand)
                if m:
                    f = int(m.group(1))
                    self.folio[idx] = f
                    self.sheet.setdefault(f, idx)
                    break
        # Front matter is numbered in romans, so an arabic folio can only come
        # from the body -- no de-collision needed.  Assert the run is monotonic
        # rather than assuming it: a folio map that jumps backwards means the
        # scrape caught something that is not a page number.
        seq = [(s, f) for s, f in sorted(self.folio.items())]
        self.folio_breaks = [b for a, b in zip(seq, seq[1:]) if b[1] < a[1]]
        self.bookch = book_chapter_ranges()
        self.log = []
        nums = sorted(k for k in self.ourch if isinstance(k, int))
        self.order = nums
        self.last_page = max(self.pages)

    def our_span(self, ch):
        """This chapter's printed folio span in our edition."""
        if ch not in self.ourch:
            return None
        start = self.ourch[ch]
        later = [self.ourch[c] for c in self.order if c > ch]
        end = min(later) - 1 if later else max(self.folio.values(), default=start)
        return start, max(start, end)

    def sheets_for(self, folio_lo, folio_hi):
        """Sheet indices carrying folios in [lo, hi]."""
        return [s for s, f in self.folio.items() if folio_lo <= f <= folio_hi]

    def chapter_of(self, bookpage):
        for ch, (a, b) in self.bookch.items():
            if a <= bookpage <= b:
                return ch
        return None

    def resolve(self, term, bookpage):
        ch = self.chapter_of(bookpage)
        if ch is None:
            self.log.append((term, bookpage, None, 'no chapter'))
            return None
        span = self.our_span(ch)
        if span is None:
            self.log.append((term, bookpage, None, f'ch{ch} not in toc'))
            return None
        lo, hi = span
        a, b = self.bookch[ch]
        frac = (bookpage - a) / max(1, (b - a))
        guess = int(round(lo + frac * (hi - lo)))

        # Search on the entry's own words, but drop the parenthetical
        # qualifiers the index uses to disambiguate headings -- "Postulate(s)
        # (axioms, assumptions) of Group III" is filed under words the page
        # itself never prints, which is what left these interpolated.
        bare = re.sub(r'\([^)]*\)', ' ', term)
        needle = re.sub(r'\b(see|also)\b', ' ', norm(bare)).strip()
        # singularise: the index heads entries "Angles", the page says "angle"
        words = [w.rstrip('s') if len(w) > 4 else w
                 for w in needle.split() if len(w) > 3]
        if not words:
            words = needle.split()

        hits = []
        for s in self.sheets_for(lo, hi):
            txt = self.pages.get(s, '')
            score = sum(1 for w in words if w in txt)
            if score:
                hits.append((score, -abs(self.folio.get(s, guess) - guess), s))
        if hits:
            best = max(hits)
            folio = self.folio.get(best[2])
            if best[0] == len(words) and folio:
                return folio
            if folio and best[0] >= max(1, len(words) - 1):
                self.log.append((term, bookpage, folio, 'partial match'))
                return folio
        self.log.append((term, bookpage, guess, 'interpolated'))
        return guess


def main():
    if not os.path.exists(TERMS):
        sys.exit(f'missing {TERMS} -- transcribe the index first')
    if not os.path.exists(PDF):
        sys.exit('build/book.pdf must exist and be current')
    rows = parse_terms()
    R = Resolver()

    body = []
    parent = ''
    for level, term, pages in rows:
        if level == 0:
            parent = term
        refs = []
        for kind, p1, p2, printed in expand(pages):
            key = term if level == 0 else f'{parent} {term}'
            a = R.resolve(key, p1)
            if a is None:
                continue
            if kind == 'range':
                b = R.resolve(key, p2)
                refs.append(f'{a}--{b}' if b and b > a else f'{a}')
            else:
                refs.append(str(a))
        # collapse duplicates, keep order
        seen, keep = set(), []
        for r in refs:
            if r not in seen:
                seen.add(r)
                keep.append(r)
        esc = term.replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')
        cmd = r'\idxmain' if level == 0 else r'\idxsub'
        body.append(f'{cmd}{{{esc}}}{{{", ".join(keep)}}}')

    with open(OUT, 'w') as fh:
        fh.write(HEAD + '\n'.join(body) + '\n' + TAIL)

    interp = sum(1 for e in R.log if e[3] == 'interpolated')
    partial = sum(1 for e in R.log if e[3] == 'partial match')
    print(f'{OUT}: {len(rows)} entries')
    print(f'  located by their own words : {len(rows) - interp - partial}')
    print(f'  partial word match         : {partial}')
    print(f'  interpolated within chapter: {interp}')
    if '--report' in sys.argv:
        for term, bp, got, why in R.log:
            print(f'    {why:14s} p{bp} -> {got}  {term[:50]}')


HEAD = r"""\documentclass[11pt]{book}
\usepackage[paperwidth=145mm,paperheight=200mm,top=18mm,bottom=20mm,inner=20mm,outer=16mm]{geometry}
\usepackage{brumfiel}

% bookindex.tex -- GENERATED by tools/build_index.py; do not hand-edit.
% The entries and their nesting are the 1960 book's own index; the page
% numbers are this edition's, resolved by locating each entry's words inside
% the chapter the original reference pointed into.

% ---- local macros (hoist into book preamble) ----
\newcommand{\idxmain}[2]{\par\noindent\hangindent=1.2em #1\quad #2\par}
\newcommand{\idxsub}[2]{\par\noindent\hspace*{1.2em}\hangindent=2.4em #1\quad #2\par}
% ---- end local macros ----

\begin{document}
\setcounter{chapter}{19}

\chapter*{\raggedleft\Huge INDEX}
\addcontentsline{toc}{chapter}{Index}
\markboth{INDEX}{}
\vspace{-1em}\noindent\rule{\linewidth}{0.6pt}\vspace{1em}

\begin{multicols}{2}
\small\raggedright
"""

TAIL = r"""\end{multicols}
\end{document}
"""


if __name__ == '__main__':
    main()
