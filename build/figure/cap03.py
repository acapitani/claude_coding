"""Figure del capitolo 3 «Il lancio»."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402
from terminale import finto_terminale

# IMG-03-01 — linea del tempo settembre 2024 – maggio 2025 (date da FATTI.md)
EVENTI = [  # (posizione in mesi da set 2024, data, titolo, dettaglio, evidenziato)
    (0.0, "set 2024", "Claude CLI", "il prototipo della musica", False),
    (2.0, "nov 2024", "Rilascio interno", "metà degli ingegneri in 5 giorni", False),
    (5.8, "24 feb 2025", "Research preview", "v0.2.9, con Claude 3.7 Sonnet", True),
    (8.7, "22 mag 2025", "Versione 1.0", "con Claude Sonnet 4 e Opus 4", True),
]
MESI = ["set", "ott", "nov", "dic", "gen", "feb", "mar", "apr", "mag"]
L = 12.6  # cm utili
def x(m): return 0.3 + m / 8.9 * L

tacche = "".join(f'<div class="m" style="left:{x(i):.2f}cm">{s}</div>' for i, s in enumerate(MESI))
anni = (f'<div class="anno" style="left:{x(0):.2f}cm">2024</div>'
        f'<div class="anno" style="left:{x(4):.2f}cm">2025</div>')
ev = ""
for i, (m, d, t, det, ev_on) in enumerate(EVENTI):
    alto = i % 2 == 0
    cls = "e su" if alto else "e giu"
    ev += (f'<div class="{cls}{" on" if ev_on else ""}" style="left:{x(m):.2f}cm">'
           f'<i></i><div class="t"><b>{t}</b><span class="d">{d}</span><span>{det}</span></div></div>')
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ width:13cm; height:5.0cm; background:#fff; position:relative; font-family:Calibri,sans-serif; color:#1F1E1D }}
.asse {{ position:absolute; left:0.2cm; right:0.2cm; top:2.2cm; height:0; border-top:1.2pt solid #6E6962 }}
.m {{ position:absolute; top:2.32cm; transform:translateX(-50%); font-size:7pt; color:#8C867D }}
.m::before {{ content:""; position:absolute; left:50%; top:-0.17cm; height:0.12cm; border-left:0.6pt solid #8C867D }}
.anno {{ position:absolute; top:2.65cm; font-size:7.5pt; font-weight:bold; color:#6E6962 }}
.e {{ position:absolute; top:2.2cm; width:0 }}
.e i {{ position:absolute; left:-0.11cm; top:-0.11cm; width:0.22cm; height:0.22cm; border-radius:50%; background:#6E6962 }}
.e.on i {{ background:#D77757; width:0.3cm; height:0.3cm; left:-0.15cm; top:-0.15cm }}
.e::after {{ content:""; position:absolute; left:0; border-left:0.6pt dashed #B8B2A7 }}
.e.su::after {{ bottom:0.12cm; height:0.55cm }}
.e.giu::after {{ top:0.12cm; height:1.1cm }}
.e.lontano::after {{ height:1.75cm }}
.t {{ position:absolute; left:-0.1cm; width:3.3cm; font-size:7.5pt; line-height:1.25 }}
.e.su .t {{ bottom:0.7cm }}
.e.giu .t {{ top:1.25cm }}
.e.lontano .t {{ top:1.9cm }}
.t b {{ display:block; font-size:8.5pt }}
.t .d {{ display:block; color:#D77757; font-weight:bold }}
.t span {{ display:block; color:#6E6962 }}
.e.on .t b {{ color:#D77757 }}
.e:last-child .t {{ left:auto; right:-0.1cm; text-align:right }}
</style><div class="asse"></div>{tacche}{anni}{ev}</html>"""
src = comune.RADICE / "assets/src/cap03/IMG-03-01-linea-tempo.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
dest = comune.RADICE / "assets/cap03/IMG-03-01-linea-tempo.png"
dest.parent.mkdir(parents=True, exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                    "--larghezza-cm", "13", "--altezza-cm", "5.0", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr

# IMG-03-02 — allora e oggi: l'installazione del primo README e la versione usata per il libro
finto_terminale([
    '<span class="t"># febbraio 2025, dal primo README</span>',
    '<span class="a">$</span> npm install -g @anthropic-ai/claude-code',
    '',
    '<span class="t"># novembre 2026, mentre scrivevo questo libro</span>',
    '<span class="a">$</span> claude --version',
    '2.1.318 (Claude Code)',
    '<span class="a">$</span> claude update',
], "assets/cap03/IMG-03-02-allora-oggi.png", titolo="terminale", larghezza_cm=11)
print("ok")
