#!/usr/bin/env python3
"""
measure_figures.py -- measure the real INK extent of every figure, then grow
each one into the room it actually has on the page.

Caleb's instruction (OPEN-QUESTIONS 1.5, answered 2026-08-17): make the
DIAGRAMS bigger rather than the labels smaller -- "in chapter 9, almost all of
the diagrams are too small ... it makes it hard to see them well".

A blanket scale bump is the wrong tool: it grows the figures that already fill
the measure and shoves them into the margin.  Box-width probing does not work
either, because 338 sub-figures sit in `minipage's whose width is a fraction of
\\linewidth -- such a box always measures exactly as wide as it was given, no
matter how little ink is in it.

So: set one figure per page at the real trim, ask Ghostscript for each page's
bounding box, and compare the ink to the measure.  Growth is applied by
multiplying each tikzpicture's `scale=' -- which moves coordinates only, so
label type, line weights and dot sizes stay exactly where they were.

Usage:
    python3 tools/measure_figures.py             # measure only, write the tsv
    python3 tools/measure_figures.py --apply     # measure, then rewrite scales
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
BUILD = os.path.join(ROOT, 'build', 'probe')

PT = 2.845276                       # pt per mm
MEASURE = 109 * PT                  # 145mm trim less 20mm inner, 16mm outer
TEXTHEIGHT = 162 * PT               # less 18mm top, 20mm bottom
TARGET_W = 0.96 * MEASURE
TARGET_H = 0.62 * TEXTHEIGHT        # a figure taller than this crowds its page
MAXGROW = 1.30
MINSHRINK = 0.60
GROW_EPS = 1.03                     # ignore growth below this -- not worth churn

# Caleb singled chapter 9 out -- "almost all of the diagrams are too small ...
# it makes it hard to see them well" -- so its ceiling is higher.  Everything
# is still fitted to the measure, so nothing runs into the margin.
CAP = {'figures09.tex': 1.45}


def fig_macros():
    out = []
    for path in sorted(glob.glob(os.path.join(CH, 'figures*.tex'))):
        src = open(path).read()
        for m in re.finditer(r'(?m)^\\newcommand\{(\\FIG[A-Z]+)\}', src):
            out.append((os.path.basename(path), m.group(1)))
    return out


def build_probe(macros):
    inputs = sorted({f for f, _ in macros})
    L = [r'\documentclass[11pt]{book}',
         r'\usepackage[paperwidth=145mm,paperheight=200mm,top=18mm,bottom=20mm,'
         r'inner=20mm,outer=16mm]{geometry}',
         r'\usepackage{brumfiel}']
    L += [r'\input{' + f.replace('.tex', '') + '}' for f in inputs]
    L += [r'\pagestyle{empty}', r'\begin{document}']
    for _, name in macros:
        L.append(name + r'\clearpage')
    L += [r'\end{document}']
    return '\n'.join(L) + '\n'


def gs_bboxes(pdf):
    r = subprocess.run(['gs', '-dNOPAUSE', '-dBATCH', '-q', '-sDEVICE=bbox', pdf],
                       capture_output=True, text=True)
    out = []
    for m in re.finditer(r'%%HiResBoundingBox:\s*([\d.-]+) ([\d.-]+) '
                         r'([\d.-]+) ([\d.-]+)', r.stdout + r.stderr):
        x0, y0, x1, y1 = (float(g) for g in m.groups())
        out.append((x1 - x0, y1 - y0))
    return out


def measure():
    macros = fig_macros()
    os.makedirs(BUILD, exist_ok=True)
    probe = os.path.join(CH, '_probe.tex')
    open(probe, 'w').write(build_probe(macros))
    try:
        subprocess.run(['tectonic', '-Z', 'search-path=../style',
                        '--outdir', BUILD, '_probe.tex'],
                       cwd=CH, capture_output=True, text=True)
    finally:
        os.remove(probe)
    pdf = os.path.join(BUILD, '_probe.pdf')
    if not os.path.exists(pdf):
        sys.exit('probe did not compile')
    boxes = gs_bboxes(pdf)
    if len(boxes) != len(macros):
        sys.exit(f'page/figure mismatch: {len(boxes)} pages vs {len(macros)} '
                 'figures -- a figure spilled onto two pages; fix it first')

    rows = []
    for (fname, name), (w, h) in zip(macros, boxes):
        # Grow towards TARGET_W, but only ever SHRINK a figure whose ink really
        # runs past the measure.  Side-by-side blocks are laid out with \hfill
        # between minipages, which pins their outer edges near the margins, so
        # they always measure ~0.97x the measure however small the drawings
        # inside are -- treating that as an overflow would shave every one of
        # them on every pass.
        gw = TARGET_W / w if w > 0 else 1.0
        gh = TARGET_H / h if h > 0 else 1.0
        g = min(CAP.get(fname, MAXGROW), gw, gh)
        if g < 1.0 and w <= MEASURE and h <= TARGET_H:
            g = 1.0
        g = max(MINSHRINK, g)
        rows.append((fname, name, w, h, g))
    return rows


def apply(rows, shrink_only=False):
    """Multiply each tikzpicture's scale by the figure's growth factor.

    NB: growth is capped, so a figure can finish a pass still narrower than the
    target.  Running the grow pass twice would compound the cap and blow past
    what was intended -- grow ONCE, then use --fit to chase the stragglers that
    still hang into the margin.
    """
    byfile = {}
    for fname, name, w, h, g in rows:
        if GROW_EPS > g > 0.995:
            continue                      # leave it alone
        if shrink_only and g > 0.995:
            continue
        byfile.setdefault(fname, {})[name] = g

    pic = re.compile(r'\\begin\{tikzpicture\}(\[[^\]]*\])?')
    changed = 0
    for fname, wanted in byfile.items():
        path = os.path.join(CH, fname)
        src = open(path).read()
        # split the file into macro-sized chunks so a growth factor can only
        # ever touch the pictures inside its own figure
        parts = re.split(r'(?m)^(\\newcommand\{\\FIG[A-Z]+\})', src)
        for i in range(1, len(parts), 2):
            name = parts[i][len(r'\newcommand{'):-1]
            g = wanted.get(name)
            if g is None:
                continue

            def bump(m):
                opts = (m.group(1) or '[]')[1:-1]
                sm = re.search(r'(?<![a-z])scale\s*=\s*([0-9.]+)', opts)
                if sm:
                    new = float(sm.group(1)) * g
                    opts = opts[:sm.start(1)] + f'{new:.3f}' + opts[sm.end(1):]
                else:
                    opts = (opts + ',' if opts.strip() else '') + f'scale={g:.3f}'
                return r'\begin{tikzpicture}[' + opts + ']'

            parts[i + 1], n = pic.subn(bump, parts[i + 1])
            changed += n
        open(path, 'w').write(''.join(parts))
    print(f'applied growth to {changed} tikzpictures in {len(byfile)} files')


def main():
    rows = measure()
    with open(os.path.join(ROOT, 'build', 'figure-widths.tsv'), 'w') as fh:
        fh.write('file\tmacro\tink_w_pt\tink_h_pt\tgrowth\n')
        for fname, name, w, h, g in rows:
            fh.write(f'{fname}\t{name}\t{w:.1f}\t{h:.1f}\t{g:.3f}\n')
    grow = [r for r in rows if r[4] >= GROW_EPS]
    shrink = [r for r in rows if r[4] < 0.995]
    print(f'measured {len(rows)} figures  (measure {MEASURE:.0f}pt wide)')
    print(f'  to grow  : {len(grow)}  (median x'
          f'{sorted(r[4] for r in grow)[len(grow)//2]:.2f})' if grow else '  to grow  : 0')
    print(f'  to shrink: {len(shrink)}')
    by = {}
    for fname, name, w, h, g in rows:
        by.setdefault(fname, []).append(g)
    for fname in sorted(by):
        gs_ = by[fname]
        print(f'    {fname:18s} n={len(gs_):3d}  mean x{sum(gs_)/len(gs_):.2f}')
    if '--apply' in sys.argv:
        apply(rows)
    elif '--fit' in sys.argv:
        apply(rows, shrink_only=True)


if __name__ == '__main__':
    main()
