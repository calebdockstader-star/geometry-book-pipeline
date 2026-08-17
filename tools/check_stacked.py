#!/usr/bin/env python3
"""
check_stacked.py -- catch labels driven on top of, or hard against, each other.

WHY THIS EXISTS (the hole it plugs in check_labels.py)
-----------------------------------------------------
check_labels tests each *word* pdfplumber hands back.  But pdfplumber groups
glyphs into a word by proximity: two labels placed so close that their glyphs
touch arrive as ONE word, and a single word can never collide with itself.  So
the failure mode the audit is least able to see is exactly the one an automated
placement search will drift into -- two numerals shoved into the same spot.
`merge_scripts` widens the blind spot a second time, since it deliberately
absorbs a short fragment into its left neighbour to reunite $B'$ and $P_1$.

Fig. 6-40 and Fig. 6-42 both showed it: the book sets "1  2" and "3  4" with a
clear gap, the draft had them glyph-to-glyph, and the audit reported one word
"12" / "34" sitting clear of every stroke -- a clean pass on a plate that reads
as a two-digit number.

THE TEST
--------
The TeX knows what each label says, so ask it.  Every label in a figure block
is declared in exactly one of three places -- a `node{...}`, a `\\VInum{}{}{}{}`
or a `\\VInumb{}{}{}{}{}`.  Collect those strings, then require every word on
the rendered page to BE one of them.  A word that is instead the concatenation
of two or more declared labels is two labels fused: report it.

This is a structural test, not a distance test, so it cannot be gamed by
nudging: the only way to clear it is to give the two labels real daylight.

Usage: python3 check_stacked.py <figures.tex> <chapternum> [--gap PT]
       --gap also reports pairs that stay separate words but come within PT
       (default 1.0) of each other, which is the near-miss the book never has.
"""
import math
import os
import re
import subprocess
import sys
import tempfile

import pdfplumber

from check_labels import DRIVER, merge_scripts

# \VIpr and friends render as prime marks; a couple of nodes carry text.
SUBS = [(r'\VIpppr', '\u2034'), (r'\VIppr', '\u2033'), (r'\VIpr', '\u2032'),
        (r'\ang', '\u2220'), (r'\,', ''), (r'\;', ''), (r'\!', ''),
        (r'\ ', ' '), (r'\cong', '\u2245'), (r'\perp', '\u22a5')]


def norm(tex):
    """A label's TeX source reduced to the characters it puts on the page."""
    s = tex
    for a, b in SUBS:
        s = s.replace(a, b)
    s = re.sub(r'\\text(?:bf|it|rm|sf)?\s*\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:mathrm|mathit|mbox|hbox)\s*\{([^{}]*)\}', r'\1', s)
    s = s.replace('$', '').replace('{', '').replace('}', '')
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    return re.sub(r'\s+', '', s)


def brace_arg(s, i):
    """Read a balanced {...} starting at the brace at or after s[i]."""
    while i < len(s) and s[i] != '{':
        if not s[i].isspace():
            return None, i
        i += 1
    if i >= len(s):
        return None, i
    depth, j = 0, i
    while j < len(s):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return None, i


def skip_args(s, i, n):
    for _ in range(n):
        a, i = brace_arg(s, i)
        if a is None:
            return None
    return i


def block_labels(body):
    """Every label string a figure block puts on the page."""
    out = []
    # node[...] at (...) {TEXT}  /  node[...] (name) at (...) {TEXT}
    for m in re.finditer(r'\\node\b', body):
        i = m.end()
        # walk past option brackets, coordinates and keywords up to the text
        depth = 0
        while i < len(body):
            c = body[i]
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif depth == 0 and c == '{':
                break
            elif depth == 0 and c == ';':
                i = -1
                break
            i += 1
        if i is None or i < 0 or i >= len(body):
            continue
        txt, _ = brace_arg(body, i)
        if txt is not None:
            out.append(txt)
    for mac, nargs in (('VInumb', 4), ('VInum', 3)):
        for m in re.finditer(r'\\' + mac + r'(?![a-zA-Z])', body):
            i = skip_args(body, m.end(), nargs)
            if i is None:
                continue
            txt, _ = brace_arg(body, i)
            if txt is not None:
                out.append(txt)
    return [norm(t) for t in out if norm(t)]


def fusions(word, labels):
    """Split `word` into >=2 declared labels, or None."""
    if not word:
        return []
    best = None
    for lab in labels:
        if word.startswith(lab):
            rest = fusions(word[len(lab):], labels)
            if rest is not None:
                cand = [lab] + rest
                if best is None or len(cand) < len(best):
                    best = cand
    if best is not None:
        return best
    return None


def main(figfile, chap, gap):
    src_tex = open(figfile).read()
    blocks = {}
    parts = re.split(r'\\newcommand\{\\(FIG[A-Z]+)\}', src_tex)
    for name, body in zip(parts[1::2], parts[2::2]):
        blocks[name] = block_labels(body)
    macros = list(blocks)

    tmp = tempfile.mkdtemp()
    body = "\n".join(rf"\{m}\clearpage" for m in macros)
    drv = os.path.join(tmp, 'drv.tex')
    root = os.path.dirname(os.path.dirname(os.path.abspath(figfile)))
    style = os.path.join(root, 'style')
    figdir = os.path.dirname(os.path.abspath(figfile))
    open(drv, 'w').write(DRIVER % (os.path.basename(figfile)[:-4], chap, body))
    r = subprocess.run(['tectonic', '-Z', f'search-path={style}',
                        '-Z', f'search-path={figdir}', '--outdir', tmp, drv],
                       capture_output=True)
    pdf = drv.replace('.tex', '.pdf')
    if not os.path.exists(pdf):
        sys.exit('driver compile failed:\n' + r.stdout.decode()[-1200:])

    nfused = nnear = 0
    with pdfplumber.open(pdf) as bk:
        for name, page in zip(macros, bk.pages):
            labels = sorted(set(blocks[name]), key=len, reverse=True)
            raw = page.extract_words(extra_attrs=[]) or []
            hits = []
            for w in raw:
                t = re.sub(r'\s+', '', w['text'])
                if t in labels:
                    continue
                split = fusions(t, labels)
                if split and len(split) > 1:
                    hits.append(('FUSED', t, ' + '.join(split)))
            # near misses between words that did stay apart
            ws = merge_scripts(raw)
            for i in range(len(ws)):
                for j in range(i + 1, len(ws)):
                    a, b = ws[i], ws[j]
                    dx = max(a['x0'] - b['x1'], b['x0'] - a['x1'], 0)
                    dy = max(a['top'] - b['bottom'], b['top'] - a['bottom'], 0)
                    d = math.hypot(dx, dy)
                    if d <= gap:
                        hits.append(('NEAR', f"{a['text']} / {b['text']}",
                                     f'{d:.2f}pt'))
            if hits:
                print(f'  {name}:')
                for kind, t, extra in hits:
                    print(f'    [{kind}] "{t}"  {extra}')
                    if kind == 'FUSED':
                        nfused += 1
                    else:
                        nnear += 1
    print(f'\n{nfused} fused label pairs, {nnear} near misses '
          f'(<= {gap}pt) across {len(macros)} figure blocks')
    return 1 if nfused else 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    g = 1.0
    for a in sys.argv[1:]:
        if a.startswith('--gap'):
            g = float(a.split('=', 1)[1]) if '=' in a else 1.0
    sys.exit(main(args[0], args[1], g))
