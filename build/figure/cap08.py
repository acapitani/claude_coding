"""Figura del capitolo 8 «CLAUDE.md e la memoria» (F-360, F-361, F-364)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

LIV = [
    ("Azienda", r"C:\Program Files\ClaudeCode\CLAUDE.md", "regole decise dall'ufficio informatico, per tutti"),
    ("Tu", "~/.claude/CLAUDE.md", "le tue preferenze, in tutti i progetti"),
    ("Progetto", "Contabilita/CLAUDE.md", "le regole del progetto, condivise con i colleghi"),
    ("Sottocartella", "Contabilita/fatture/CLAUDE.md", "letto quando lavoro lì dentro"),
]
annidati = ""
for i, (t, f, d) in reversed(list(enumerate(LIV))):
    annidati = (f'<div class="l l{i}"><div class="h"><b>{t}</b><code>{f}</code></div>'
                f'<div class="d">{d}</div>{annidati}</div>')
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm; display:flex; gap:0.3cm }}
.col {{ flex:1 }}
.l {{ border:0.9pt solid #B8B2A7; border-radius:0.15cm; padding:0.15cm 0.2cm 0.2cm; margin-top:0.12cm }}
.l0 {{ background:#F4F1EA; margin-top:0 }} .l1 {{ background:#F9F7F2 }} .l2 {{ background:#FBF0EB; border-color:#D77757 }}
.l3 {{ background:#fff }}
.h {{ display:flex; justify-content:space-between; align-items:baseline; gap:0.2cm }}
.h b {{ font-size:9.5pt }} code {{ font:7pt Consolas, monospace; color:#8C867D }}
.l2 > .h b {{ color:#D77757 }}
.d {{ font-size:7.8pt; color:#6E6962 }}
.lato {{ width:4.5cm; flex:none; display:flex; flex-direction:column; gap:0.25cm }}
.n {{ border:0.9pt dashed #B8B2A7; border-radius:0.15cm; padding:0.15cm 0.2cm; font-size:7.8pt; color:#6E6962 }}
.n b {{ display:block; font-size:9pt; color:#1F1E1D }} .n code {{ display:block; margin:0.04cm 0 }}
.freccia {{ font-size:7.5pt; color:#8C867D; text-align:center; margin-top:0.12cm }}
</style><div class="col">{annidati}<div class="freccia">si leggono tutti, dal più generale al più specifico, e si sommano</div></div>
<div class="lato">
<div class="n"><b>Solo per te, solo qui</b><code>CLAUDE.local.md</code>appunti personali sul progetto, non condivisi</div>
<div class="n"><b>Memoria automatica</b><code>~/.claude/projects/…/memory/</code>le note che prendo da solo tra una sessione e l'altra</div>
</div></html>"""
src = comune.RADICE / "assets/src/cap08/IMG-08-01-gerarchia.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
dest = comune.RADICE / "assets/cap08/IMG-08-01-gerarchia.png"
dest.parent.mkdir(parents=True, exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                    "--larghezza-cm", "13", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
