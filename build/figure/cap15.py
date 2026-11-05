"""Figure del capitolo 15 «Fogli di calcolo».
IMG-15-02: il grafico vero di esempi/cap15/riepilogo.xlsx, esportato in PDF con LibreOffice (profilo it-IT) e ritagliato."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
DIFETTI = {"mar": "importi come testo", "mag": "colonne in altro ordine", "ago": "riga doppia",
           "nov": "date come testo"}
fogli = "".join(
    f'<div class="f{" x" if m in DIFETTI else ""}"><b>2026-{i:02d}</b><span>{DIFETTI.get(m, "")}</span></div>'
    for i, m in enumerate(MESI, start=1))
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm; display:flex; align-items:center; gap:0.25cm }}
.griglia {{ display:grid; grid-template-columns:repeat(3, 1.55cm); gap:0.12cm }}
.f {{ height:1.05cm; border:0.8pt solid #B8B2A7; border-radius:0.08cm; background:#F1F6EE; padding:0.06cm 0.08cm;
      font-size:6.3pt; line-height:1.15; position:relative }}
.f b {{ display:block; font-size:7.5pt }} .f span {{ color:#C0504D }}
.f::after {{ content:"xlsx"; position:absolute; right:0.06cm; bottom:0.04cm; font-size:5.5pt; color:#8C867D }}
.f.x {{ border-color:#C0504D; background:#FBEDEC }}
.freccia {{ font-size:18pt; color:#8C867D }}
.motore {{ width:2.5cm; text-align:center; background:#1F1E1D; color:#F0EEE6; border-radius:0.15cm; padding:0.25cm 0.15cm; font-size:8pt }}
.motore b {{ display:block; font:bold 9pt Consolas,monospace; color:#D77757; margin-bottom:0.05cm }}
.esito {{ border:0.8pt solid #6B9B57; border-radius:0.12cm; padding:0.15cm 0.2cm; width:3.4cm; font-size:8pt; background:#F1F6EE }}
.esito b {{ display:block; font-size:9.5pt; margin-bottom:0.06cm }}
.esito div {{ margin:0.04cm 0 }}
</style>
<div class="griglia">{fogli}</div><div class="freccia">→</div>
<div class="motore"><b>unisci.py</b>legge, ripulisce,<br>segnala, unisce</div>
<div class="freccia">→</div>
<div class="esito"><b>riepilogo.xlsx</b><div>▸ Movimenti: 229 righe</div><div>▸ Mesi: formule SOMMA.PIÙ.SE</div><div>▸ grafico entrate/uscite</div></div>
</html>"""
src = comune.RADICE / "assets/src/cap15/IMG-15-01-unione.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap15/IMG-15-01-unione.png"),
                    "--larghezza-cm", "13", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
