"""Figure del capitolo 25 «Dove sono adesso» (dati da FATTI.md).

25.1 Dove vivo: le superfici al novembre 2026 (F-210, F-212, F-213, F-215, F-219, F-351).
25.2 I modelli con cui ho lavorato, febbraio 2025 – ottobre 2026 (F-401…F-417).
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

def html_png(nome, corpo, css, larghezza=13):
    src = comune.RADICE / "assets/src/cap25" / f"{nome}.html"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text('<!doctype html><html lang="it"><meta charset="utf-8"><style>'
                   '* { box-sizing:border-box; margin:0; padding:0 } '
                   'body { background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.1cm }'
                   f'{css}</style>{corpo}</html>', encoding="utf-8")
    dest = comune.RADICE / "assets/cap25" / f"{nome}.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                        "--larghezza-cm", str(larghezza), "--dpi", "300"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


GRUPPI = [
    ("Sul tuo computer", [("terminale", "dove sono nato"), ("VS Code · JetBrains", "dentro l'editor (JetBrains in beta)"),
                          ("app Claude", "la scheda Code, accanto a Chat e Cowork")]),
    ("Nel cloud", [("sessioni nel browser", "le «cloud sessions», per tutti da settembre 2026"),
                   ("Routines", "attività che partono da sole, a orario o a un segnale"),
                   ("GitHub Actions · GitLab", "il lavoro sul codice condiviso")]),
    ("Dove si lavora insieme", [("Claude Tag in Slack", "l'erede di Claude Code in Slack")]),
]
colonne = "".join(
    f'<div class="g"><div class="t">{titolo}</div>' +
    "".join(f'<div class="c"><b>{n}</b><span>{s}</span></div>' for n, s in voci) + "</div>"
    for titolo, voci in GRUPPI)
html_png("IMG-25-01-superfici", f'<div class="io">Claude Code <span>· lo stesso motore, molte porte</span></div>'
         f'<div class="righe">{colonne}</div>', """
.io { margin:0 auto 0.3cm; width:7cm; text-align:center; padding:0.15cm; border:1.2pt solid #D77757; background:#FBF0EB;
      border-radius:0.2cm; font:bold 10pt Calibri } .io span { font-weight:normal; color:#6E6962 }
.righe { display:flex; gap:0.25cm }
.g { flex:1; border:0.8pt solid #B8B2A7; border-radius:0.2cm; padding:0.15cm }
.t { font:bold 8pt Calibri; color:#8C867D; text-align:center; margin-bottom:0.12cm; text-transform:uppercase; letter-spacing:0.03em }
.c { background:#F3F0EA; border:0.8pt solid #1F1E1D; border-radius:0.15cm; padding:0.1cm 0.15cm; margin-bottom:0.12cm; font-size:8.5pt; line-height:1.2 }
.c b { display:block } .c span { color:#6E6962; font-size:7.5pt }
""")

MODELLI = [  # (data, nome, famiglia)
    (date(2025, 2, 24), "3.7 Sonnet", "s"), (date(2025, 5, 22), "Sonnet 4 · Opus 4", "o"),
    (date(2025, 8, 5), "Opus 4.1", "o"), (date(2025, 9, 29), "Sonnet 4.5", "s"),
    (date(2025, 10, 15), "Haiku 4.5", "h"), (date(2025, 11, 24), "Opus 4.5", "o"),
    (date(2026, 2, 5), "Opus 4.6", "o"), (date(2026, 2, 17), "Sonnet 4.6", "s"),
    (date(2026, 4, 16), "Opus 4.7", "o"), (date(2026, 5, 28), "Opus 4.8", "o"),
    (date(2026, 6, 9), "Fable 5 · Mythos 5", "f"), (date(2026, 6, 30), "Sonnet 5", "s"),
    (date(2026, 7, 24), "Opus 5", "o"), (date(2026, 9, 1), "Fable · Mythos 5.1", "f"),
    (date(2026, 9, 22), "Opus 5.5", "o"), (date(2026, 9, 28), "Sonnet 5.5", "s"),
    (date(2026, 10, 7), "Haiku 5.5", "h"),
]
MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
def colonna(anno):
    righe = "".join(
        f'<div class="r {f}"><div class="d">{d.day} {MESI[d.month - 1]}</div><div class="p"><i></i></div>'
        f'<div class="n">{n}</div></div>' for d, n, f in MODELLI if d.year == anno)
    return f'<div class="col"><div class="anno">{anno}</div><div class="lista">{righe}</div></div>'

html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; color:#1F1E1D; padding:0.15cm 0.1cm }}
.tela {{ display:flex; gap:0.6cm; align-items:flex-start }}
.col {{ flex:1 }}
.anno {{ font:bold 10pt Calibri; color:#8C867D; margin:0 0 0.1cm 1.35cm }}
.lista {{ position:relative }}
.lista::before {{ content:""; position:absolute; left:1.62cm; top:0.25cm; bottom:0.25cm; border-left:1.2pt solid #B8B2A7 }}
.r {{ display:flex; align-items:center; height:0.5cm; font-size:8.5pt }}
.d {{ width:1.35cm; text-align:right; color:#6E6962 }}
.p {{ width:0.55cm; position:relative; height:100% }}
.p i {{ position:absolute; left:0.175cm; top:50%; width:0.18cm; height:0.18cm; margin-top:-0.09cm; border-radius:50%; background:#8C867D }}
.r.o .p i {{ background:#D77757 }} .r.o .n {{ color:#B5573A; font-weight:bold }}
.leg {{ margin-top:0.2cm; text-align:right; font-size:7.5pt; color:#6E6962 }}
.leg i {{ display:inline-block; width:0.18cm; height:0.18cm; border-radius:50%; margin:0 0.05cm 0 0.25cm; background:#8C867D; vertical-align:-0.02cm }}
.leg i.o {{ background:#D77757 }}
</style><div class="tela">{colonna(2025)}{colonna(2026)}</div>
<div class="leg"><i class="o"></i>Opus, i modelli più grandi <i></i>gli altri</div></html>"""
src = comune.RADICE / "assets/src/cap25/IMG-25-02-modelli.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src),
                    str(comune.RADICE / "assets/cap25/IMG-25-02-modelli.png"), "--larghezza-cm", "13", "--dpi", "300"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
print("ok")
