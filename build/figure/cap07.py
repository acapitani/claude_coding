"""Figure del capitolo 7 «Come parlarmi»."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402
from terminale import finto_terminale  # noqa: E402

# IMG-07-01 — anatomia di una buona richiesta
PARTI = [
    ("c", "Contesto", "In questa cartella ci sono gli estratti conto 2026 della ditta, uno per mese, in Excel."),
    ("o", "Obiettivo", "Voglio un unico file riepilogo.xlsx con un foglio per mese e un foglio «Totali»."),
    ("v", "Vincoli", "Non modificare i file originali. Le colonne sono le stesse in tutti i file."),
    ("f", "Fatto quando", "Il totale di ogni mese nel riepilogo coincide con quello del file originale."),
]
righe = "".join(f'<div class="r {k}"><div class="e">{t}</div><div class="x">{x}</div></div>' for k, t, x in PARTI)
html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:#fff; font-family:Calibri,sans-serif; padding:0.15cm }}
.box {{ border:0.8pt solid #6E6962; border-radius:0.15cm; padding:0.25cm 0.3cm; background:#FAF8F4 }}
.p {{ font:9pt Consolas, monospace; color:#8C867D; margin-bottom:0.15cm }}
.r {{ display:flex; align-items:stretch; margin:0.12cm 0 }}
.e {{ width:2.3cm; flex:none; font:bold 8.5pt Calibri; color:#fff; border-radius:0.1cm 0 0 0.1cm; padding:0.12cm 0.15cm;
      display:flex; align-items:center }}
.x {{ flex:1; font:9.5pt Cambria, Georgia, serif; color:#1F1E1D; padding:0.1cm 0.2cm; border-radius:0 0.1cm 0.1cm 0 }}
.c .e {{ background:#6E8CA6 }} .c .x {{ background:#EAF0F5 }}
.o .e {{ background:#D77757 }} .o .x {{ background:#FBF0EB }}
.v .e {{ background:#8A7F6E }} .v .x {{ background:#F1EEE8 }}
.f .e {{ background:#6B9B57 }} .f .x {{ background:#EDF4E9 }}
</style><div class="box"><div class="p">&gt; la tua richiesta</div>{righe}</div></html>"""
src = comune.RADICE / "assets/src/cap07/IMG-07-01-anatomia-richiesta.html"
src.parent.mkdir(parents=True, exist_ok=True)
src.write_text(html, encoding="utf-8")
dest = comune.RADICE / "assets/cap07/IMG-07-01-anatomia-richiesta.png"
dest.parent.mkdir(parents=True, exist_ok=True)
r = subprocess.run(["node", str(Path(__file__).parent / "render.mjs"), str(src), str(dest),
                    "--larghezza-cm", "12.5", "--dpi", "300"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr

# IMG-07-02 — il piano presentato in plan mode (testi dell'interfaccia 2.1.318, F-626)
finto_terminale([
    '<span class="t">&gt;</span> unisci gli estratti conto in un riepilogo (vedi sopra)',
    '',
    '<div class="box a"><span class="b">Ready to code?</span>\n\n'
    'Here is Claude\'s plan:\n'
    '  <span class="c">1. Leggo i 12 file e controllo che le colonne coincidano</span>\n'
    '  <span class="c">2. Creo riepilogo.xlsx: un foglio per mese</span>\n'
    '  <span class="c">3. Aggiungo il foglio «Totali» con le somme mensili</span>\n'
    '  <span class="c">4. Confronto ogni totale con il file originale</span>\n'
    '  <span class="t">  I file originali non vengono modificati.</span>\n\n'
    '<span class="sel"><span class="a">❯</span> 1. Yes, auto-accept edits</span>\n'
    '  2. Yes, manually approve edits\n'
    '  3. No, keep planning</div>',
    '  <span class="a">plan mode on</span>',
], "assets/cap07/IMG-07-02-plan-mode.png", titolo="estratti-2026 — claude", larghezza_cm=13)
print("ok")
