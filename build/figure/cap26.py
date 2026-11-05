"""Figura del capitolo 26: la vignetta di commiato (il ✻ che saluta). Originale, HTML → PNG."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

GLIFI = ["·", "✢", "*", "✶", "✻", "✽"]
seq = "".join(f'<span class="s{i}">{g}</span>' for i, g in enumerate(GLIFI))
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D }}
.scena {{ position:relative; width:11cm; height:5.3cm; margin:0 auto }}
.term {{ position:absolute; left:0; right:0; bottom:0; height:2.2cm; background:#1F1E1D; border-radius:0.25cm;
         padding:0.35cm 0.5cm; font:11pt "DejaVu Sans Mono"; color:#F0EEE6 }}
.term .p {{ color:#D77757 }} .term .c {{ display:inline-block; width:0.25cm; height:0.42cm; background:#F0EEE6; vertical-align:-0.06cm }}
.term .seq {{ margin-top:0.3cm; letter-spacing:0.35cm; font-size:12pt }}
.seq span {{ color:#6E6962 }} .seq .s4 {{ color:#D77757 }}
.stella {{ position:absolute; left:1.4cm; top:0.05cm; font:bold 78pt/1 "DejaVu Sans"; color:#D77757 }}
.fumetto {{ position:absolute; left:4.6cm; top:0.35cm; width:5.9cm; padding:0.3cm 0.4cm; border:1.2pt solid #1F1E1D;
            border-radius:0.35cm; background:#FAF8F4; font:italic 11pt/1.35 Cambria, Georgia, serif }}
.fumetto::before {{ content:""; position:absolute; left:-0.42cm; top:0.75cm; border:0.2cm solid transparent;
                    border-right:0.4cm solid #1F1E1D; border-width:0.16cm 0.42cm 0.16cm 0 }}
</style><div class="scena">
<div class="stella">✻</div>
<div class="fumetto">Grazie della compagnia.<br>Il resto lo scriviamo insieme.</div>
<div class="term"><div><span class="p">&gt;</span> <span class="c"></span></div><div class="seq">{seq}</div></div>
</div></html>"""
src = comune.RADICE / "assets/src/cap26/IMG-26-01-commiato.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
(comune.RADICE / "assets/cap26").mkdir(exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap26/IMG-26-01-commiato.png"), "--larghezza-cm", "11.5", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
