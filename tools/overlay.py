#!/usr/bin/env python3
"""
overlay.py -- superimpose a redrawn TikZ figure on its source photograph.

This is the QA loop for figure fidelity. It does NOT chase pixel-identity:
the source is a photograph of a bound book, so its "straight" lines are
already bent by page curvature and camera angle. What it checks is whether
the PROPORTIONS agree -- which is the part that can actually be wrong.

Usage:
    python3 overlay.py --src s18.png --srcbox 380 880 1000 1180 \
                       --fig ch09.pdf --figpage 24 --figbox 0.2 0.3 0.8 0.6 \
                       --out cmp-9-40.png
"""
import argparse, subprocess, tempfile, os
from PIL import Image, ImageChops


def load_pdf_page(pdf, page, dpi=200):
    d = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page),
                    '-l', str(page), pdf, os.path.join(d, 'p')], check=True)
    return Image.open([os.path.join(d, f) for f in sorted(os.listdir(d))][0])


def trim(im, thresh=235):
    """Crop to the ink."""
    g = im.convert('L').point(lambda v: 0 if v < thresh else 255)
    bbox = ImageChops.invert(g).getbbox()
    return im.crop(bbox) if bbox else im


def tint(im, rgb, alpha=0.55):
    """Turn dark pixels into a coloured transparent layer."""
    g = im.convert('L')
    lay = Image.new('RGBA', im.size, rgb + (0,))
    mask = g.point(lambda v: int((255 - v) * alpha))
    lay.putalpha(mask)
    return lay


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--srcbox', nargs=4, type=int, required=True)
    ap.add_argument('--fig', required=True)
    ap.add_argument('--figpage', type=int, required=True)
    ap.add_argument('--figbox', nargs=4, type=float, required=True,
                    help='fractional l t r b of the rendered page')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    src = trim(Image.open(a.src).crop(tuple(a.srcbox)))

    pg = load_pdf_page(a.fig, a.figpage)
    W, H = pg.size
    l, t, r, b = a.figbox
    mine = trim(pg.crop((int(l*W), int(t*H), int(r*W), int(b*H))))

    # scale mine to the source's bounding box -- proportion check, not size check
    mine = mine.resize(src.size, Image.LANCZOS)

    base = Image.new('RGBA', src.size, (255, 255, 255, 255))
    base.alpha_composite(tint(src,  (0, 0, 0)))          # original in black
    base.alpha_composite(tint(mine, (217, 76, 25)))      # redraw in vermillion

    strip = Image.new('RGB', (src.width * 3 + 40, src.height), 'white')
    strip.paste(src.convert('RGB'), (0, 0))
    strip.paste(mine.convert('RGB'), (src.width + 20, 0))
    strip.paste(base.convert('RGB'), (src.width * 2 + 40, 0))
    strip.save(a.out)
    print(f'wrote {a.out}  (original | redraw | overlay)')


if __name__ == '__main__':
    main()
