"""Figure del capitolo 9 «Permessi e sicurezza» (F-370…F-378)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

BASE = "* { box-sizing:border-box; margin:0; padding:0 } body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm }"


def png(nome, corpo, css, larghezza=13):
    src = comune.RADICE / "assets/src/cap09" / f"{nome}.html"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(f'<!doctype html><html lang="it"><meta charset="utf-8"><style>{BASE}{css}</style>{corpo}</html>',
                   encoding="utf-8")
    dest = comune.RADICE / "assets/cap09" / f"{nome}.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                        "--larghezza-cm", str(larghezza), "--dpi", "300"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


# IMG-09-01 — le modalità di permesso, dalla più prudente alla più libera
MODI = [
    ("Plan", "plan mode on", "leggo e propongo un piano; non modifico niente", "lavori nuovi o delicati", ""),
    ("Manual", "(nessuna scritta)", "ti chiedo il permesso per modifiche e comandi", "la prima volta, i file importanti", "on"),
    ("Accept edits", "accept edits on", "modifico i file della cartella senza chiedere", "quando ti fidi del piano", ""),
    ("Auto", "auto mode on", "un controllore esamina le azioni al posto tuo", "il lavoro di tutti i giorni", ""),
    ("Bypass", "—", "nessuna domanda, nessun controllo", "solo in macchine isolate", "no"),
]
celle = "".join(
    f'<div class="m {c}"><b>{n}</b><code>{i}</code><p>{d}</p><span>{q}</span></div>' for n, i, d, q, c in MODI)
png("IMG-09-01-modalita", f'<div class="asse"><span>più controllo</span><span>più autonomia</span></div>'
    f'<div class="riga">{celle}</div>', """
.asse { display:flex; justify-content:space-between; font-size:8pt; color:#8C867D; margin:0 0.1cm 0.12cm;
        background:linear-gradient(90deg,#6B9B57,#D9D4CB 50%,#C0504D); background-size:100% 1.5pt;
        background-repeat:no-repeat; background-position:0 100%; padding-bottom:0.12cm }
.riga { display:flex; gap:0.15cm }
.m { flex:1; border:0.8pt solid #D9D4CB; border-radius:0.15cm; background:#FAF8F4; padding:0.15cm; min-height:3.3cm }
.m b { display:block; font-size:10pt } .m code { display:block; font:6.5pt Consolas, monospace; color:#D77757; margin:0.05cm 0 0.1cm }
.m p { font-size:7.8pt; line-height:1.25; color:#1F1E1D; margin-bottom:0.1cm } .m span { display:block; line-height:1.2; font-size:7.3pt; color:#8C867D; font-style:italic }
.m.on { border-color:#D77757; background:#FBF0EB }
.m.no { border-color:#C0504D; border-style:dashed; background:#fff }
""")

# IMG-09-02 — la sandbox come recinto
png("IMG-09-02-sandbox", """
<div class="sc">
 <div class="rec"><div class="tit">Sandbox</div>
   <div class="dentro"><b>Cartella di lavoro</b>i comandi leggono e scrivono qui</div>
   <div class="cmd">$ comando</div>
 </div>
 <div class="fuori">
   <div class="f no"><b>Resto del disco</b>scrittura bloccata</div>
   <div class="f no"><b>Internet</b>bloccato, salvo i domini che ammetti</div>
   <div class="f ok"><b>Lettura</b>possibile quasi ovunque: proteggi a parte i file con le password</div>
 </div>
</div>""", """
.sc { display:flex; gap:0.4cm; align-items:center }
.rec { flex:1.1; border:1.6pt dashed #D77757; border-radius:0.3cm; padding:0.3cm; background:#FBF0EB; position:relative }
.tit { position:absolute; top:-0.28cm; left:0.3cm; background:#fff; padding:0 0.15cm; font:bold 9pt Calibri; color:#D77757 }
.dentro { background:#fff; border:0.8pt solid #D9D4CB; border-radius:0.15cm; padding:0.2cm; font-size:8pt; color:#6E6962 }
.dentro b, .f b { display:block; font-size:9.5pt; color:#1F1E1D }
.cmd { margin-top:0.2cm; background:#1F1E1D; color:#F0EEE6; font:8pt Consolas, monospace; padding:0.12cm 0.2cm; border-radius:0.1cm }
.fuori { flex:1; display:flex; flex-direction:column; gap:0.15cm }
.f { border:0.8pt solid #D9D4CB; border-radius:0.15cm; padding:0.12cm 0.2cm; font-size:7.8pt; color:#6E6962; position:relative; padding-left:0.75cm }
.f::before { position:absolute; left:0.2cm; top:0.12cm; font:bold 11pt "Segoe UI Symbol" }
.f.no::before { content:"✘"; color:#C0504D } .f.ok::before { content:"⚠"; color:#C9A227 }
""", 12)
print("ok")
