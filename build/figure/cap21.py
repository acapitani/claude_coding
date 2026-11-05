"""Figura del capitolo 21 «Hook»: gli eventi sulla linea del tempo di una sessione (F-392)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

EVENTI = [("SessionStart", "inizia la sessione", ""), ("UserPromptSubmit", "scrivi una richiesta", ""),
          ("PreToolUse", "prima di ogni strumento", "on"), ("PostToolUse", "dopo ogni strumento", ""),
          ("Notification", "ti serve una risposta", ""), ("Stop", "ho finito di rispondere", "")]
celle = "".join(f'<div class="e {c}"><i></i><b>{n}</b><span>{d}</span></div>' for n, d, c in EVENTI)
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.15cm 0.1cm }}
.linea {{ position:relative; display:flex; justify-content:space-between }}
.linea::before {{ content:""; position:absolute; left:0.3cm; right:0.3cm; top:0.16cm; border-top:1.2pt solid #B8B2A7 }}
.e {{ width:2.05cm; text-align:center; position:relative; font-size:7.3pt; line-height:1.25 }}
.e i {{ display:block; margin:0 auto 0.12cm; width:0.32cm; height:0.32cm; border-radius:50%; background:#fff; border:1.4pt solid #8C867D }}
.e b {{ display:block; font:bold 7.3pt Consolas,monospace; margin-bottom:0.04cm }}
.e span {{ color:#6E6962 }}
.e.on i {{ background:#D77757; border-color:#D77757 }} .e.on b {{ color:#D77757 }}
.giro {{ margin:0.25cm 0 0 4.1cm; width:4.6cm; border:1pt dashed #D77757; border-radius:0.15cm; padding:0.12cm 0.18cm; font-size:7.5pt; background:#FBF0EB }}
.giro b {{ color:#D77757 }}
</style><div class="linea">{celle}</div>
<div class="giro"><b>PreToolUse + exit 2</b> = l'azione non parte. Il messaggio dell'hook arriva a me, e cerco un'altra strada.</div></html>"""
src = comune.RADICE / "assets/src/cap21/IMG-21-01-eventi.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
(comune.RADICE / "assets/cap21").mkdir(exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap21/IMG-21-01-eventi.png"), "--larghezza-cm", "13", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
