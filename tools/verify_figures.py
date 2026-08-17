#!/usr/bin/env python3
"""
verify_figures.py -- check that each figure actually satisfies the hypothesis
its exercise or theorem states.

The failure mode this catches: a figure whose text says "BE is parallel to CD"
but whose drawing has them at 4 degrees. Eyeballing misses that; arithmetic
doesn't. Each constraint encodes the BOOK's wording; coordinates are read from
the chapter's figuresNN.tex.

Constraints live in per-chapter modules: tools/constraints/chNN.py, each
defining  build(check)  and importing helpers from figlib. One module per
chapter so chapter agents never edit a shared file.

Usage:
    python3 tools/verify_figures.py            # run every chapter's checks
    python3 tools/verify_figures.py 09 11      # only ch09 and ch11
Exit 1 if any constraint fails.
"""
import glob
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from figlib import TOL  # noqa: E402


def main(args):
    if args:
        files = [os.path.join(HERE, 'constraints', f'ch{a.zfill(2)}.py') for a in args]
        missing = [f for f in files if not os.path.exists(f)]
        if missing:
            sys.exit('no constraint module: ' + ', '.join(missing))
    else:
        files = sorted(glob.glob(os.path.join(HERE, 'constraints', 'ch*.py')))
    if not files:
        sys.exit('no constraint modules found in tools/constraints/')

    checks = []

    def check(fig, what, err, tol=TOL):
        checks.append((fig, what, err, err <= tol))

    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        spec = importlib.util.spec_from_file_location(f'constraints_{name}', f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.build(check)

    w = max(len(c[1]) for c in checks)
    bad = 0
    for fig, what, err, ok in checks:
        flag = ' ok ' if ok else 'FAIL'
        print(f'  [{flag}] {fig:<6} {what:<{w}}  err = {err:.4f}')
        bad += not ok
    print(f'\n{len(checks) - bad}/{len(checks)} constraints hold')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
