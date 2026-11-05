"""Figura del capitolo 19: la cassetta degli attrezzi (ricostruzione stilizzata di una cartella di Windows)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

VOCI = [("1 - Lettere da elenco", "bat"), ("2 - Unisci estratti", "bat"), ("3 - Fatture PDF in Excel", "bat"),
        ("4 - Rinomina foto (prova)", "bat"), ("5 - Report settimanale", "bat"), ("LEGGIMI", "txt"),
        ("strumenti", "dir")]
ICONE = {"bat": "⚙", "txt": "≡", "dir": "▰"}
righe = "".join(f'<div class="v{" sel" if i == 1 else ""}"><i class="{t}">{ICONE[t]}</i>{n}<span>{ {"bat":"File batch","txt":"Documento di testo","dir":"Cartella"}[t]}</span></div>'
                for i, (n, t) in enumerate(VOCI))
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:"Segoe UI",Calibri,sans-serif; color:#1F1E1D; padding:0.15cm; display:flex; gap:0.35cm; align-items:center }}
.fin {{ width:8.2cm; border:0.8pt solid #B8B2A7; border-radius:0.15cm; overflow:hidden; box-shadow:0 0.08cm 0.25cm rgba(0,0,0,.12) }}
.barra {{ background:#F4F1EA; padding:0.12cm 0.25cm; font-size:7.5pt; color:#6E6962; border-bottom:0.6pt solid #D9D4CB }}
.v {{ display:flex; align-items:center; gap:0.18cm; padding:0.1cm 0.25cm; font-size:8pt }}
.v span {{ margin-left:auto; color:#8C867D; font-size:7pt }}
.v i {{ font-style:normal; width:0.42cm; text-align:center; font-family:"Segoe UI Symbol" }}
i.bat {{ color:#6E8CA6 }} i.txt {{ color:#8C867D }} i.dir {{ color:#C9A227 }}
.sel {{ background:#FBF0EB; outline:0.8pt dashed #D77757 }}
.lato {{ font-size:8pt; width:3.9cm; line-height:1.35 }}
.cartella {{ display:inline-block; background:#FFF5D6; border:0.8pt solid #C9A227; border-radius:0.08cm; padding:0.1cm 0.2cm; font-size:8pt; margin-bottom:0.15cm }}
.freccia {{ color:#D77757; font-size:16pt; line-height:1 }}
.lato b {{ color:#D77757 }}
</style>
<div class="fin"><div class="barra">Cassetta degli attrezzi</div>{righe}</div>
<div class="lato"><div class="cartella"><span style="color:#C9A227">▰</span> Estratti 2026</div><div class="freccia">⤺</div>
<b>Trascina</b> la cartella dei dati sopra lo strumento: si apre una finestra che dice che cosa ha fatto, e i risultati compaiono come file nuovi.</div>
</html>"""
src = comune.RADICE / "assets/src/cap19/IMG-19-01-cassetta.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
(comune.RADICE / "assets/cap19").mkdir(exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap19/IMG-19-01-cassetta.png"), "--larghezza-cm", "13", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
