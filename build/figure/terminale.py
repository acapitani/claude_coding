"""Finte schermate di terminale (figure di tipo T) con lo stile del libro → PNG a 300 dpi.

Le righe sono HTML con poche classi:
    a = arancio Claude   t = tenue   v = verde   r = rosso   b = grassetto   c = crema chiaro
    sel = riga selezionata (sfondo)   box = riquadro (casella di input / dialogo)
    n1…n9 = segnalino numerato (callout) allineato a destra, per le figure "anatomia"
Esempio:
    from terminale import finto_terminale
    finto_terminale(['<span class="a">$</span> claude', '<span class="a">✻</span> Clauding…'],
                    "assets/cap06/IMG-06-01-anatomia.png", titolo="~/Download — claude")
Il sorgente HTML generato si salva accanto, in assets/src/, per poterlo ritoccare.
"""
from __future__ import annotations

import html
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

RENDER = Path(__file__).resolve().parent / "render.mjs"

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #FFFFFF; padding: 0.15cm; }
.fin { background: #1F1E1D; border-radius: 0.22cm; overflow: hidden; border: 0.6pt solid #3A3735; }
.barra { height: 0.6cm; background: #2E2C2A; display: flex; align-items: center; gap: 0.16cm; padding-left: 0.3cm;
         font: 7pt "DejaVu Sans Mono"; color: #8C867D; }
.barra i { width: 0.2cm; height: 0.2cm; border-radius: 50%; background: #4A4643; display: block; }
.barra span { flex: 1; text-align: center; margin-right: 1.0cm; }
.corpo { padding: 0.35cm 0.45cm 0.4cm; font: 8.6pt/1.5 Consolas, "DejaVu Sans Mono", monospace; color: #F0EEE6;
         white-space: pre; }
.riga { position: relative; min-height: 1.5em; }
.a { color: #D77757; } .t { color: #8C867D; } .v { color: #8DBF6A; } .r { color: #E06C6C; } .b { font-weight: bold; }
.c { color: #FFFFFF; }
.g { font-family: "DejaVu Sans Mono"; }            /* glifi ✻ ✢ ✶ ✽ ❯ ● */
.sel { background: #3A3633; margin: 0 -0.2cm; padding: 0 0.2cm; }
.box { position: relative; border: 0.8pt solid #6E6962; border-radius: 0.12cm; padding: 0.12cm 0.25cm; margin: 0.1cm 0; white-space: pre; }
.box.a { border-color: #D77757; color: inherit; }
.box .n { right: 0.2cm; top: 0.14cm; }
.n { position: absolute; right: -0.05cm; top: 0.02em; width: 1.35em; height: 1.35em; border-radius: 50%;
     background: #D77757; color: #1F1E1D; font: bold 7.5pt/1.35em Calibri, sans-serif; text-align: center; }
"""

GLIFI = set("✻✢✶✽✳●❯⏺⎿")


def _glifi(s: str) -> str:
    """Avvolge i glifi speciali in <span class="g"> (Consolas non li ha)."""
    out = []
    in_tag = False
    for ch in s:
        if ch == "<":
            in_tag = True
        elif ch == ">":
            in_tag = False
        out.append(f'<span class="g">{ch}</span>' if (ch in GLIFI and not in_tag) else ch)
    return "".join(out)


def finto_terminale(righe: list[str], destinazione: str, titolo: str = "claude",
                    larghezza_cm: float = 13.0, dpi: int = 300) -> Path:
    corpo = []
    for r in righe:
        if r.startswith("<div"):          # blocco già formattato (box, ecc.)
            corpo.append(_glifi(r))
        else:
            corpo.append(f'<div class="riga">{_glifi(r) or "&nbsp;"}</div>')
    doc = (f'<!doctype html><html lang="it"><meta charset="utf-8"><style>{CSS}</style>'
           f'<div class="fin"><div class="barra"><i></i><i></i><i></i><span>{html.escape(titolo)}</span></div>'
           f'<div class="corpo">{"".join(corpo)}</div></div></html>')
    dest = comune.RADICE / destinazione
    dest.parent.mkdir(parents=True, exist_ok=True)
    src = comune.RADICE / "assets" / "src" / dest.parent.name / (dest.stem + ".html")
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(doc, encoding="utf-8")
    r = subprocess.run(["node", str(RENDER), str(src), str(dest), "--larghezza-cm", str(larghezza_cm),
                        "--dpi", str(dpi)], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    return dest


def n(k: int) -> str:
    """Segnalino numerato da mettere in fondo a una riga."""
    return f'<span class="n">{k}</span>'
