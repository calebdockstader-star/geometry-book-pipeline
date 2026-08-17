#!/usr/bin/env python3
"""
dots_to_nodes.py -- convert path-drawn point dots to scale-immune node dots.

Why: `\\fill (A) circle (1.5pt)' is a PATH, so tikz's coordinate transform
scales it.  A figure drawn at scale=0.62 therefore printed its points at
0.93pt radius, which is why the dots read faint (Caleb, 2026-08-17: "make the
dots that signify points bigger").  `\\dt{A}' places a node instead, and a
node's minimum size ignores the coordinate transform -- so every point in the
book prints at exactly one size regardless of how its figure is scaled.

Handles the three shapes that occur in the sources:
    \\fill (A) circle (1.2pt);
    \\fill (A) circle (1.2pt) (B) circle (1.2pt);
    \\foreach \\p in {A,B,C} \\fill (\\p) circle (1.4pt);

Run from the project root:  python3 tools/dots_to_nodes.py [--dry]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# one "(coord) circle (Npt)" clause; the coord may itself hold balanced parens
# (e.g. ($(A)!0.5!(B)$)), so allow one level of nesting.
CLAUSE = r'\((?:[^()]|\([^()]*\))*\)\s*circle\s*\(\s*[0-9.]+\s*pt\s*\)'
DOTS = re.compile(r'\\fill\s*((?:' + CLAUSE + r'\s*)+);')
COORD = re.compile(r'\((?:[^()]|\([^()]*\))*\)(?=\s*circle)')
LEFTOVER = re.compile(r'\\fill[^;]*circle\s*\(\s*[0-9.]+\s*pt')


def convert(text):
    def repl(m):
        out = []
        for c in COORD.findall(m.group(1)):
            out.append('\\dt{' + c[1:-1].strip() + '}')
        return ''.join(out)
    return DOTS.subn(repl, text)


def main():
    dry = '--dry' in sys.argv
    total = 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'chapters', 'figures*.tex'))):
        src = open(path).read()
        new, n = convert(src)
        left = LEFTOVER.findall(new)
        if left:
            print(f'  !! {os.path.basename(path)}: {len(left)} unconverted '
                  f'fill-circle sites -- inspect by hand')
        if n and not dry:
            open(path, 'w').write(new)
        total += n
        print(f'{os.path.basename(path)}: {n} dots -> \\dt')
    print(f'total {total} dots converted' + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
