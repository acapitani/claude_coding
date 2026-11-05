"""Figure del capitolo 20 «Slash command e skill»."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402
from terminale import finto_terminale  # noqa: E402

html = """<!doctype html><html lang="it"><meta charset="utf-8"><style>
* { box-sizing:border-box; margin:0; padding:0 }
body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm; display:flex; gap:0.3cm }
.c { flex:1; border:0.8pt solid #D9D4CB; border-radius:0.15cm; background:#FAF8F4; padding:0.2cm 0.25cm; font-size:8pt; line-height:1.35 }
.c.s { border-color:#D77757; background:#FBF0EB }
h { display:block; font-size:11pt; font-weight:bold; margin-bottom:0.05cm }
.c.s h { color:#D77757 }
code { font:7pt Consolas,monospace; color:#6E6962; display:block; margin-bottom:0.12cm }
.r { margin:0.07cm 0 } .r b { display:inline-block; width:1.75cm; color:#6E6962; font-weight:normal }
.es { margin-top:0.12cm; font:7.5pt Consolas,monospace; background:#1F1E1D; color:#F0EEE6; border-radius:0.08cm; padding:0.08cm 0.12cm }
.es i { color:#D77757; font-style:normal }
</style>
<div class="c"><h>Comando</h><code>.claude/commands/riepilogo-fattura.md</code>
<div class="r"><b>Chi lo avvia</b>tu, scrivendo il nome</div>
<div class="r"><b>Che cos'è</b>un solo file di istruzioni</div>
<div class="r"><b>Argomenti</b>sì, con <i>$ARGUMENTS</i></div>
<div class="r"><b>Ideale per</b>gesti che ripeti spesso</div>
<div class="es"><i>&gt;</i> /riepilogo-fattura fattura-03.pdf</div></div>
<div class="c s"><h>Skill</h><code>.claude/skills/controllo-fattura/SKILL.md</code>
<div class="r"><b>Chi la avvia</b>io, quando serve; o tu con /nome</div>
<div class="r"><b>Che cos'è</b>una cartella: istruzioni e file di supporto</div>
<div class="r"><b>Come la scelgo</b>dalla <i>description</i></div>
<div class="r"><b>Ideale per</b>procedure e competenze</div>
<div class="es"><i>&gt;</i> puoi verificarmi la fattura 14?</div></div>
</html>"""
src = comune.RADICE / "assets/src/cap20/IMG-20-01-comando-skill.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
(comune.RADICE / "assets/cap20").mkdir(exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap20/IMG-20-01-comando-skill.png"), "--larghezza-cm", "13", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr

# IMG-20-02 — la skill scelta da sola (dalla prova reale, research/note/skill-cap20.txt; testo accorciato)
finto_terminale([
    '<span class="t">&gt;</span> Puoi verificarmi la fattura fatture/fattura-14.pdf?',
    '',
    '<span class="v">●</span> <span class="b">Skill</span>(controllo-fattura)',
    '<span class="v">●</span> <span class="b">Read</span>(fatture/fattura-14.pdf)',
    '',
    '<span class="c">●</span> <span class="b">FATTURA DA CONTROLLARE</span>',
    '  Imponibile 189,38 €   IVA 22% 41,66 €  <span class="v">✔</span>',
    '  Totale in fattura <span class="r">331,04 €</span>, calcolato 231,04 €  <span class="r">✘</span>',
    '  <span class="b">Differenza: 100,00 € in più.</span> Va chiarito con',
    '  il fornitore prima di pagare.',
], "assets/cap20/IMG-20-02-skill-in-azione.png", titolo="ufficio — claude", larghezza_cm=13)
print("ok")
