"""Genera le immagini di anteprima usate nel README (docs/img/).

Uso (dopo py build/update_indexes.py):
    py build/immagini_readme.py                 # copertina + doppia pagina 36-37 (cap. 6)
    py build/immagini_readme.py --pagine 52-53  # altra coppia di pagine fisiche (pari, dispari)
"""
import argparse
import sys
from pathlib import Path

import pymupdf
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402

DEST = comune.RADICE / "docs" / "img"


def copertina(larghezza_px: int) -> Path:
    img = Image.open(comune.RADICE / "assets" / "copertina" / "cover.png").convert("RGB")
    img = img.resize((larghezza_px, round(img.height * larghezza_px / img.width)), Image.LANCZOS)
    out = DEST / "copertina.jpg"
    img.save(out, "JPEG", quality=88, optimize=True)
    return out


def doppia_pagina(pdf: Path, sx: int, dx: int, dpi: int) -> Path:
    doc = pymupdf.open(pdf)
    pagine = []
    for p in (sx, dx):
        pix = doc[p - 1].get_pixmap(dpi=dpi, alpha=False)
        pagine.append(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
    w, h = pagine[0].size
    piega, bordo = 6, 1
    foglio = Image.new("RGB", (2 * w + piega + 2 * bordo, h + 2 * bordo), (190, 186, 178))
    foglio.paste(pagine[0], (bordo, bordo))
    foglio.paste(pagine[1], (bordo + w + piega, bordo))
    out = DEST / f"pagine-{sx}-{dx}.png"
    foglio.save(out, optimize=True)
    return out


def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser()
    ap.add_argument("--pagine", default="52-53", help="coppia di pagine fisiche del PDF, es. 52-53")
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--larghezza-copertina", type=int, default=700)
    a = ap.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)
    sx, dx = (int(x) for x in a.pagine.split("-"))
    pdf = comune.OUTPUT / "claude-coding.pdf"
    for f in (copertina(a.larghezza_copertina), doppia_pagina(pdf, sx, dx, a.dpi)):
        print(f"✔ {f.relative_to(comune.RADICE)}  ({f.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
