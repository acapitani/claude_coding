"""Renderizza pagine del PDF in PNG per l'ispezione visiva (output/anteprime/).

Uso:
    py build/render_pages.py --pdf output/prova.pdf --pagine 1-6,12      # pagine fisiche (da 1)
    py build/render_pages.py --sample 12                                 # campione distribuito
    py build/render_pages.py --tutte --dpi 60                            # tutte, in piccolo
    py build/render_pages.py --foglio                                    # provino: 2 pagine affiancate (vista libro)
"""
import argparse
import sys
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402


def intervallo(spec: str, n: int) -> list[int]:
    out = []
    for parte in spec.split(","):
        if "-" in parte:
            a, b = parte.split("-")
            out += list(range(int(a), int(b) + 1))
        elif parte:
            out.append(int(parte))
    return [p for p in out if 1 <= p <= n]


def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--config", default="book.yaml")
    ap.add_argument("--pagine")
    ap.add_argument("--sample", type=int)
    ap.add_argument("--tutte", action="store_true")
    ap.add_argument("--foglio", action="store_true", help="affianca pagina pari e dispari come in un libro aperto")
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    pdf_path = Path(a.pdf) if a.pdf else comune.OUTPUT / f"{comune.nome_output(comune.carica_config(a.config))}.pdf"
    doc = pymupdf.open(pdf_path)
    n = len(doc)
    if a.pagine:
        pagine = intervallo(a.pagine, n)
    elif a.sample:
        passo = max(1, n // a.sample)
        pagine = sorted(set([1, 2, 3] + list(range(1, n + 1, passo))))
    else:
        pagine = list(range(1, n + 1)) if a.tutte else list(range(1, min(n, 8) + 1))
    dest = comune.OUTPUT / "anteprime"
    dest.mkdir(parents=True, exist_ok=True)
    for vecchio in dest.glob(f"{pdf_path.stem}-*.png"):
        vecchio.unlink()
    if a.foglio:
        # pagina 1 da sola (a destra), poi le coppie (2,3), (4,5)… come in un libro aperto
        coppie = [(None, 1)] + [(k, k + 1 if k + 1 <= n else None) for k in range(2, n + 1, 2)]
        coppie = [c for c in coppie if (c[0] in pagine) or (c[1] in pagine)]
        for sx, dx in coppie:
            imgs = [doc[p - 1].get_pixmap(dpi=a.dpi, alpha=False) if p else None for p in (sx, dx)]
            w = max(i.width for i in imgs if i)
            h = max(i.height for i in imgs if i)
            foglio = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 2 * w + 10, h), False)
            foglio.set_rect(foglio.irect, (120, 120, 120))
            for k, im in enumerate(imgs):
                if im:
                    im.set_origin(k * (w + 10), 0)
                    foglio.copy(im, im.irect)
            nome = dest / f"{pdf_path.stem}-foglio-{(sx or 0):03d}-{(dx or 0):03d}.png"
            foglio.save(nome)
            print(nome.relative_to(comune.RADICE))
    else:
        for p in pagine:
            nome = dest / f"{pdf_path.stem}-p{p:03d}.png"
            doc[p - 1].get_pixmap(dpi=a.dpi).save(nome)
            print(nome.relative_to(comune.RADICE))


if __name__ == "__main__":
    main()
