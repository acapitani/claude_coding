"""Figure del capitolo 14 «Documenti».
IMG-14-02: una lettera vera prodotta da esempi/cap14/lettere.py, convertita in PDF con LibreOffice e ritagliata."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

html = """<!doctype html><html lang="it"><meta charset="utf-8"><style>
* { box-sizing:border-box; margin:0; padding:0 }
body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm; display:flex; align-items:center; gap:0.25cm }
.col { display:flex; flex-direction:column; gap:0.25cm }
.c { border:0.8pt solid #D9D4CB; border-radius:0.15cm; background:#FAF8F4; padding:0.15cm 0.2cm; font-size:8pt; width:3.6cm }
.c b { display:block; font-size:9.5pt; margin-bottom:0.08cm }
table { border-collapse:collapse; font-size:6.8pt; width:100% } td { border:0.5pt solid #D9D4CB; padding:0.02cm 0.06cm }
tr:first-child td { background:#E8E3DA; font-weight:bold }
.seg { color:#D77757; font-family:Consolas,monospace; font-size:7.5pt }
.freccia { font-size:18pt; color:#8C867D }
.motore { width:2.6cm; text-align:center; background:#1F1E1D; color:#F0EEE6; border-radius:0.15cm; padding:0.25cm 0.15cm; font-size:8pt }
.motore b { display:block; font:bold 9pt Consolas,monospace; color:#D77757; margin-bottom:0.05cm }
.pila { position:relative; width:3.2cm; height:2.6cm }
.foglio { position:absolute; width:2.4cm; height:2.0cm; background:#fff; border:0.8pt solid #B8B2A7; border-radius:0.08cm }
.ok { margin-top:0.15cm; font-size:8pt } .ok b { color:#6B9B57 } .no b { color:#C0504D }
</style>
<div class="col">
 <div class="c"><b>Elenco (Excel)</b><table><tr><td>Nome</td><td>Cognome</td><td>Importo</td></tr>
 <tr><td>Andrea</td><td>Ferrari</td><td>595,77</td></tr><tr><td>Giulia</td><td>Rossi</td><td>1.210,40</td></tr><tr><td>…</td><td>…</td><td>…</td></tr></table></div>
 <div class="c"><b>Modello (Word)</b>Gentile <span class="seg">{titolo} {cognome}</span>, ci risulta da saldare la fattura <span class="seg">{fattura}</span> di <span class="seg">{importo}</span>…</div>
</div>
<div class="freccia">→</div>
<div class="motore"><b>lettere.py</b>una riga,<br>una lettera;<br>controlla i dati</div>
<div class="freccia">→</div>
<div>
 <div class="pila">""" + "".join(f'<div class="foglio" style="left:{i*0.15}cm; top:{i*0.12}cm"></div>' for i in range(5)) + """</div>
 <div class="ok"><b>49 lettere</b> pronte</div><div class="ok no"><b>1 riga</b> da controllare</div>
</div></html>"""
src = comune.RADICE / "assets/src/cap14/IMG-14-01-stampa-unione.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap14/IMG-14-01-stampa-unione.png"),
                    "--larghezza-cm", "13", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
