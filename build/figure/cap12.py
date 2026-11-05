"""Figure del capitolo 12 «Git e revisione del codice».
I commit e il diff sono quelli reali del repository di prova della mini-app (research/note/git-cap12.txt)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402
from terminale import finto_terminale  # noqa: E402

# IMG-12-01 — commit e branch come una linea della metropolitana
html = """<!doctype html><html lang="it"><meta charset="utf-8"><style>
* { box-sizing:border-box; margin:0; padding:0 } body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D }
svg text { font-family:Calibri,sans-serif }
</style>
<svg xmlns="http://www.w3.org/2000/svg" width="13cm" height="5.4cm" viewBox="0 0 1300 540">
 <line x1="80" y1="170" x2="1220" y2="170" stroke="#6E6962" stroke-width="10" stroke-linecap="round"/>
 <path d="M520 170 C 600 170, 600 380, 700 380 L 860 380 C 960 380, 960 170, 1040 170" fill="none"
       stroke="#D77757" stroke-width="10" stroke-linecap="round"/>
 <g font-size="26">
  <circle cx="160" cy="170" r="24" fill="#fff" stroke="#6E6962" stroke-width="8"/>
  <text x="160" y="100" text-anchor="middle" font-weight="bold">b6a1ea0</text>
  <text x="160" y="240" text-anchor="middle">Prima versione</text><text x="160" y="272" text-anchor="middle">del convertitore</text>
  <circle cx="460" cy="170" r="24" fill="#fff" stroke="#6E6962" stroke-width="8"/>
  <text x="460" y="100" text-anchor="middle" font-weight="bold">ff4711b</text>
  <text x="400" y="240" text-anchor="middle">Aggiunti i test</text>
  <circle cx="780" cy="380" r="24" fill="#fff" stroke="#D77757" stroke-width="8"/>
  <text x="780" y="455" text-anchor="middle" font-weight="bold" fill="#D77757">38d5578</text>
  <text x="780" y="488" text-anchor="middle">Legge i numeri con la virgola</text>
  <circle cx="1120" cy="170" r="28" fill="#D77757" stroke="#6E6962" stroke-width="8"/>
  <text x="1120" y="100" text-anchor="middle" font-weight="bold">main</text>
  <text x="1120" y="240" text-anchor="middle">correzione unita</text>
 </g>
 <text x="40" y="40" font-size="24" fill="#6E6962">linea principale: main</text>
 <text x="590" y="390" font-size="24" fill="#D77757" text-anchor="end">branch: correzione-virgola</text>
</svg></html>"""
src = comune.RADICE / "assets/src/cap12/IMG-12-02-metro.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
dest = comune.RADICE / "assets/cap12/IMG-12-02-metro.png"
dest.parent.mkdir(parents=True, exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                    "--larghezza-cm", "13", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr

# IMG-12-02 — la storia e una modifica, come le mostra git (uscita reale, accorciata)
finto_terminale([
    '<span class="a">$</span> git log --oneline',
    '<span class="a">38d5578</span> Legge i numeri con la virgola; rifiuta lo zero assoluto',
    '<span class="a">ff4711b</span> Aggiunti i test con sette casi noti',
    '<span class="a">b6a1ea0</span> Prima versione del convertitore di unità',
    '',
    '<span class="a">$</span> git show 38d5578',
    '<span class="t"> convertitore.html | 19 ++++++++++++++++---</span>',
    '<span class="r">-  &lt;input id="valore" type="number" value="1" step="any"&gt;</span>',
    '<span class="v">+  &lt;input id="valore" type="text" inputmode="decimal" value="1"&gt;</span>',
    '<span class="r">-  const v = parseFloat($("valore").value);</span>',
    '<span class="v">+  const v = leggiNumero($("valore").value);</span>',
    '<span class="t">   …</span>',
], "assets/cap12/IMG-12-01-log-diff.png", titolo="convertitore — git", larghezza_cm=13)
print("ok")
