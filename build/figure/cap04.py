"""Figure del capitolo 4 «Crescere in pubblico» (date e numeri da FATTI.md)."""
import random
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

RENDER = Path(__file__).resolve().parent / "render.mjs"
BASE = "* { box-sizing:border-box; margin:0; padding:0 } body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D }"


def html_png(nome: str, corpo: str, css: str, larghezza: float, altezza: float | None = None):
    src = comune.RADICE / "assets/src/cap04" / f"{nome}.html"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(f'<!doctype html><html lang="it"><meta charset="utf-8"><style>{BASE}{css}</style>{corpo}</html>',
                   encoding="utf-8")
    dest = comune.RADICE / "assets/cap04" / f"{nome}.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["node", str(RENDER), str(src), str(dest), "--larghezza-cm", str(larghezza), "--dpi", "300"]
    if altezza:
        cmd += ["--altezza-cm", str(altezza)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


# IMG-04-01 — il diario delle funzioni (F-302…F-328, F-208…F-219)
DIARIO = [
    ("mar 2025", "0.2.31", "Comandi personalizzati", "le proprie procedure in .claude/commands/"),
    ("giu 2025", "1.0.38", "Hook", "regole che scattano da sole a ogni evento"),
    ("lug 2025", "1.0.60", "Sottoagenti", "aiutanti con un compito e un contesto propri"),
    ("set 2025", "2.0.0", "Claude Code 2.0", "nuova interfaccia, checkpoint e /rewind"),
    ("ott 2025", "2.0.12", "Plugin", "pacchetti di comandi, agenti e hook da installare"),
    ("ott 2025", "2.0.20", "Skill", "procedure e conoscenze caricate quando servono"),
    ("ott 2025", "2.0.24", "Sandbox e web", "un recinto per i comandi; sessioni nel browser"),
    ("gen 2026", "2.1.0", "Versione 2.1", "l'inizio di una lunga serie"),
    ("feb 2026", "2.1.32", "Agent Teams", "più istanze che collaborano (anteprima)"),
    ("mar 2026", "2.1.71", "/loop", "una richiesta ripetuta a intervalli"),
    ("apr 2026", "—", "Routines", "attività pianificate che girano sul web"),
]
righe = "".join(
    f'<div class="r"><div class="d">{d}</div><div class="p"><i></i></div>'
    f'<div class="v">{v}</div><div class="t"><b>{t}</b> <span>{s}</span></div></div>'
    for d, v, t, s in DIARIO)
html_png("IMG-04-01-diario", f'<div class="lista">{righe}</div>', """
.lista { padding:0.15cm 0.1cm; position:relative }
.lista::before { content:""; position:absolute; left:1.72cm; top:0.35cm; bottom:0.35cm; border-left:1.2pt solid #B8B2A7 }
.r { display:flex; align-items:center; height:0.62cm; font-size:8.5pt }
.d { width:1.45cm; text-align:right; color:#6E6962; font-weight:bold }
.p { width:0.55cm; position:relative; height:100% }
.p i { position:absolute; left:0.165cm; top:50%; width:0.2cm; height:0.2cm; margin-top:-0.1cm; border-radius:50%; background:#D77757 }
.v { width:1.2cm; font:7.5pt Consolas, monospace; color:#8C867D }
.t b { color:#1F1E1D } .t span { color:#6E6962 }
""", 13)

# IMG-04-02 — lo spinner ingrandito (F-601, F-602)
GLIFI = [("·", "U+00B7"), ("✢", "U+2722"), ("*", "U+002A"), ("✶", "U+2736"), ("✻", "U+273B"), ("✽", "U+273D")]
celle = "".join(f'<div class="c{" on" if g == "✻" else ""}"><div class="g">{g}</div><div class="u">{u}</div></div>'
                for g, u in GLIFI)
html_png("IMG-04-02-spinner", f'<div class="riga">{celle}</div>'
         '<div class="freccia">avanti → → → → →&#8195;poi indietro ← ← ← ← ←</div>', """
body { padding:0.2cm 0.3cm }
.riga { display:flex; justify-content:space-between }
.c { width:1.75cm; height:2.2cm; border:0.8pt solid #D9D4CB; border-radius:0.15cm; background:#FAF8F4; text-align:center }
.c .g { font:bold 30pt/1.55cm "DejaVu Sans Mono"; color:#6E6962; height:1.6cm }
.c .u { font:7pt Consolas, monospace; color:#8C867D }
.c.on { border-color:#D77757; background:#FBF0EB } .c.on .g { color:#D77757 }
.freccia { margin-top:0.25cm; text-align:center; font-size:8.5pt; color:#8C867D; letter-spacing:0.03em }
""", 12)

# IMG-04-03 — la nuvola dei verbi (F-605): un campione dei 187, con i più famosi in evidenza
verbi = (comune.RADICE / "research/note/spinner-verbi-2.1.318.txt").read_text(encoding="utf-8").split()
STELLE = {"Clauding", "Combobulating", "Flibbertigibbeting", "Moonwalking", "Pontificating", "Discombobulating",
          "Reticulating", "Schlepping", "Honking", "Vibing", "Zigzagging", "Accomplishing"}
random.seed(4)
campione = sorted(set(random.sample(verbi, 70)) | (STELLE & set(verbi)))
random.shuffle(campione)
parole = "".join(
    f'<span class="{"s" if v in STELLE else "n" + str(random.randint(1, 3))}">{v}</span>' for v in campione)
html_png("IMG-04-03-verbi", f'<div class="nuvola">{parole}</div>', """
.nuvola { display:flex; flex-wrap:wrap; justify-content:center; align-items:baseline; gap:0.05cm 0.28cm; padding:0.2cm }
span { font-family:Calibri, sans-serif; white-space:nowrap }
.n1 { font-size:7.5pt; color:#B8B2A7 } .n2 { font-size:9pt; color:#8C867D } .n3 { font-size:10.5pt; color:#6E6962 }
.s { font-size:13pt; font-weight:bold; color:#D77757 }
""", 13)
print("ok")
