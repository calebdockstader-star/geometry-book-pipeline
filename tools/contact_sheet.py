#!/usr/bin/env python3
"""
contact_sheet.py -- tile PDF pages into numbered contact sheets for review.

The project rule is that numbers never replace looking: every page of a build
gets eyeballed before it ships.  At 470+ pages that is only practical as
contact sheets, so this renders a page range and tiles it with the page number
burnt into each cell.

    python3 tools/contact_sheet.py build/book.pdf 1 48
    python3 tools/contact_sheet.py build/ch06.pdf 1 60 --cols 4 --dpi 55

Sheets land in build/sheets/<stem>-NNN.png; the paths are printed so they can
be fed straight to the Read tool.
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('first', type=int)
    ap.add_argument('last', type=int)
    ap.add_argument('--cols', type=int, default=4)
    ap.add_argument('--rows', type=int, default=3)
    ap.add_argument('--dpi', type=int, default=60)
    a = ap.parse_args()

    out = os.path.join(ROOT, 'build', 'sheets')
    os.makedirs(out, exist_ok=True)
    stem = os.path.splitext(os.path.basename(a.pdf))[0]
    per = a.cols * a.rows
    made = []

    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-f', str(a.first), '-l', str(a.last),
                        '-r', str(a.dpi), '-jpeg', '-jpegopt', 'quality=72',
                        a.pdf, os.path.join(td, 'p')], check=True)
        pages = sorted(glob.glob(os.path.join(td, 'p-*.jpg')))
        if not pages:
            sys.exit('no pages rendered')
        for start in range(0, len(pages), per):
            chunk = pages[start:start + per]
            ims = [Image.open(p) for p in chunk]
            w = max(i.width for i in ims)
            h = max(i.height for i in ims)
            sheet = Image.new('RGB', (a.cols * w, a.rows * h), 'white')
            d = ImageDraw.Draw(sheet)
            for k, im in enumerate(ims):
                x, y = (k % a.cols) * w, (k // a.cols) * h
                sheet.paste(im, (x, y))
                num = os.path.basename(chunk[k]).split('-')[-1].split('.')[0]
                d.rectangle([x, y, x + 34, y + 15], fill='white')
                d.text((x + 3, y + 3), num.lstrip('0'), fill='red')
                d.rectangle([x, y, x + w - 1, y + h - 1], outline='#cccccc')
            path = os.path.join(out, f'{stem}-{start // per + 1:03d}.png')
            sheet.save(path)
            made.append(path)
    for p in made:
        print(p)


if __name__ == '__main__':
    main()
