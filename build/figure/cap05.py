"""Figure del capitolo 5 «Installazione» (comandi da FATTI.md F-342…F-351)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402
from terminale import finto_terminale  # noqa: E402

# IMG-05-01 — installazione su Windows (PowerShell)
finto_terminale([
    '<span class="t"># 1. installa (una riga sola)</span>',
    r'<span class="a">PS C:\Users\anna&gt;</span> irm https://claude.ai/install.ps1 | iex',
    '<span class="t">   … l\'installatore scarica e configura …</span>',
    '',
    '<span class="t"># 2. chiudi e riapri il terminale, poi controlla</span>',
    r'<span class="a">PS C:\Users\anna&gt;</span> claude --version',
    '2.1.318 (Claude Code)',
    '',
    '<span class="t"># 3. entra nella cartella di lavoro e avviami</span>',
    r'<span class="a">PS C:\Users\anna&gt;</span> cd Documenti\prove',
    r'<span class="a">PS C:\Users\anna\Documenti\prove&gt;</span> claude',
], "assets/cap05/IMG-05-01-windows.png", titolo="Windows PowerShell", larghezza_cm=13)

# IMG-05-02 — dove posso usarmi
SUPERFICI = [
    ("Terminale", "Windows, macOS, Linux", "il mio ambiente naturale: questo libro parte da qui", True),
    ("App desktop", "Windows, macOS, Linux", "Claude Code senza terminale, con finestre e pulsanti", False),
    ("Editor di codice", "VS Code, JetBrains", "un pannello accanto ai file che stai modificando", False),
    ("Web", "claude.ai/code", "sessioni nel browser, sui server di Anthropic", False),
    ("Lavoro di squadra", "Slack, GitHub Actions, GitLab", "mi chiamano i colleghi o le procedure automatiche", False),
]
celle = "".join(f'<div class="s{" on" if on else ""}"><b>{t}</b><span class="d">{d}</span><span>{x}</span></div>'
                for t, d, x, on in SUPERFICI)
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.15cm }}
.centro {{ text-align:center; margin-bottom:0.3cm }}
.centro div {{ display:inline-block; background:#1F1E1D; color:#F0EEE6; border-radius:0.2cm; padding:0.2cm 0.5cm;
               font:bold 11pt "DejaVu Sans Mono" }}
.centro i {{ color:#D77757; font-style:normal }}
.griglia {{ display:grid; grid-template-columns:1fr 1fr; gap:0.22cm }}
.s {{ border:0.8pt solid #D9D4CB; background:#FAF8F4; border-radius:0.15cm; padding:0.18cm 0.25cm; font-size:8pt; line-height:1.3 }}
.s b {{ display:block; font-size:10pt }} .s .d {{ display:block; color:#D77757; font-weight:bold }}
.s span {{ color:#6E6962 }}
.s.on {{ grid-column:span 2; border-color:#D77757; background:#FBF0EB }}
</style><div class="centro"><div><i>✻</i> Claude Code</div></div><div class="griglia">{celle}</div></html>"""
src = comune.RADICE / "assets/src/cap05/IMG-05-02-dove.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap05/IMG-05-02-dove.png"), "--larghezza-cm", "12", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
