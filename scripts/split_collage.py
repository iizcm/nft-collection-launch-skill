#!/usr/bin/env python3
"""Split a collage/grid image of NFT characters into individual transparent-PNG tiles.

Usage:
  python3 split_collage.py <collage.jpg> <out_dir> [cols] [rows] [bg]

- cols/rows: grid layout (default 6x3 = 18).
- bg: 'white' (default, threshold >240) or 'lime' (target #CCFF00 = 204,255,0, tolerance 30).

Each cell is cropped, bg made transparent, trimmed to content bbox, padded to a square,
and saved as 01_name.png, 02_name.png, ... (no names -> numbered only).

Requires: Pillow, numpy.
"""
import sys, os
import numpy as np
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("usage: split_collage.py <collage> <out_dir> [cols=6] [rows=3] [bg=white]")
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    rows = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    bg = sys.argv[5] if len(sys.argv) > 5 else "white"
    os.makedirs(out, exist_ok=True)

    img = Image.open(src).convert("RGB")
    W, H = img.size
    cw, ch = W // cols, H // rows
    a = np.array(img)

    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c + 1
            x0, y0 = c * cw, r * ch
            cell = img.crop((x0, y0, x0 + cw, y0 + ch))
            ca = np.array(cell)
            if bg == "lime":
                mask = (np.abs(ca[:, :, 0].astype(int) - 204) < 30) & \
                       (np.abs(ca[:, :, 1].astype(int) - 255) < 30) & \
                       (np.abs(ca[:, :, 2].astype(int) - 0) < 30)
            else:  # white
                mask = (ca[:, :, 0] > 240) & (ca[:, :, 1] > 240) & (ca[:, :, 2] > 240)
            alpha = np.where(mask, 0, 255).astype(np.uint8)
            rgba = np.dstack([ca, alpha])
            png = Image.fromarray(rgba, "RGBA")
            bbox = png.getbbox()
            if bbox:
                png = png.crop(bbox)
            w, h = png.size
            s = max(w, h)
            sq = Image.new("RGBA", (s, s), (0, 0, 0, 0))
            sq.paste(png, ((s - w) // 2, (s - h) // 2))
            fn = os.path.join(out, f"{idx:02d}.png")
            sq.save(fn)
            print("saved", fn, sq.size)
    print("DONE", cols * rows, "tiles ->", out)

if __name__ == "__main__":
    main()
