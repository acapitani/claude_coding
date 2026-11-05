"""Spese di casa — la pagina web. Avvio: py app.py, poi http://localhost:8000

Usa solo la libreria standard di Python: niente da installare.
"""
import html
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import spese

DB = spese.apri()
COLORI = ["#D77757", "#6E8CA6", "#8A7F6E", "#6B9B57", "#C9A227", "#B8B2A7"]


def grafico(totali):
    """Barre orizzontali in SVG: una per categoria."""
    if not totali:
        return "<p class='vuoto'>Nessuna spesa in questo mese.</p>"
    massimo = max(totali.values())
    righe = []
    for i, (cat, cent) in enumerate(totali.items()):
        y, larg = i * 34, 300 * cent / massimo
        colore = COLORI[spese.CATEGORIE.index(cat) % len(COLORI)]
        righe.append(
            f"<text x='0' y='{y + 20}'>{cat}</text>"
            f"<rect x='90' y='{y + 6}' width='{larg:.0f}' height='20' rx='3' fill='{colore}'/>"
            f"<text x='{98 + larg:.0f}' y='{y + 21}' class='val'>{spese.euro(cent)}</text>")
    return (f"<svg width='520' height='{len(totali) * 34}' role='img'"
            f" aria-label='Spese per categoria'>{''.join(righe)}</svg>")


def pagina(mese, messaggio=""):
    totali = spese.totali_per_categoria(DB, mese)
    voci = "".join(
        f"<tr><td>{d[8:]}/{d[5:7]}</td><td>{c}</td><td>{html.escape(t)}</td>"
        f"<td class='num'>{spese.euro(cent)}</td>"
        f"<td><form method='post' action='/elimina'><input type='hidden' name='id' value='{i}'>"
        f"<input type='hidden' name='mese' value='{mese}'><button title='Elimina'>×</button></form></td></tr>"
        for i, d, c, t, cent in spese.del_mese(DB, mese))
    opzioni = "".join(f"<option>{c}</option>" for c in spese.CATEGORIE)
    totale = spese.euro(sum(totali.values()))
    prima = spese.totale(DB, spese.mese_precedente(mese))
    confronto = f" (mese precedente: {spese.euro(prima)})" if prima else ""
    return f"""<!doctype html><html lang="it"><meta charset="utf-8">
<title>Spese di casa</title><style>
body {{ font-family: system-ui, sans-serif; background: #f4f1ea; margin: 0; color: #1f1e1d }}
main {{ max-width: 760px; margin: 24px auto; background: #fff; padding: 24px 32px;
        border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,.08) }}
h1 {{ margin: 0 0 4px }} .sotto {{ color: #777; margin: 0 0 18px }}
form.nuova {{ display: grid; grid-template-columns: 130px 120px 1fr 100px auto; gap: 8px; margin-bottom: 18px }}
input, select, button {{ font: inherit; padding: 6px; border: 1px solid #ccc; border-radius: 6px }}
button {{ background: #fff; cursor: pointer }} form.nuova button {{ background: #d77757; color: #fff; border: 0 }}
table {{ width: 100%; border-collapse: collapse; margin-top: 8px }}
td {{ padding: 6px 4px; border-bottom: 1px solid #eee }} td.num {{ text-align: right }}
td button {{ border: 0; color: #999 }} svg text {{ font-size: 14px }} svg .val {{ fill: #555 }}
.messaggio {{ background: #fbe9e5; padding: 8px 12px; border-radius: 6px }}
.mese {{ display: flex; gap: 8px; align-items: center; margin: 18px 0 8px }}
</style><main>
<h1>Spese di casa</h1><p class="sotto">Totale di {mese[5:]}/{mese[:4]}: <b>{totale}</b>{confronto}</p>
{f'<p class="messaggio">{html.escape(messaggio)}</p>' if messaggio else ''}
<form class="nuova" method="post" action="/aggiungi">
 <input type="date" name="data" value="{date.today().isoformat()}" required>
 <select name="categoria">{opzioni}</select>
 <input name="descrizione" placeholder="Descrizione" required>
 <input name="importo" placeholder="12,50" inputmode="decimal" required>
 <button>Aggiungi</button></form>
<form class="mese" method="get"><label>Mese</label><input type="month" name="mese" value="{mese}">
 <button>Mostra</button> <a href="/esporta?mese={mese}">Scarica CSV</a></form>
{grafico(totali)}
<table>{voci}</table></main></html>"""


class Gestore(BaseHTTPRequestHandler):
    def rispondi(self, corpo, tipo="text/html; charset=utf-8", codice=200):
        dati = corpo.encode("utf-8")
        self.send_response(codice)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(dati)))
        self.end_headers()
        self.wfile.write(dati)

    def torna(self, mese):
        self.send_response(303)
        self.send_header("Location", f"/?mese={mese}")
        self.end_headers()

    def do_GET(self):
        url = urlparse(self.path)
        mese = parse_qs(url.query).get("mese", [date.today().isoformat()[:7]])[0]
        if url.path == "/":
            self.rispondi(pagina(mese))
        elif url.path == "/esporta":
            self.rispondi(spese.esporta_csv(DB, mese), "text/csv; charset=utf-8")
        else:
            self.rispondi("Pagina non trovata", "text/plain; charset=utf-8", 404)

    def do_POST(self):
        lunghezza = int(self.headers.get("Content-Length", 0))
        campi = {k: v[0] for k, v in parse_qs(self.rfile.read(lunghezza).decode("utf-8")).items()}
        if self.path == "/aggiungi":
            try:
                spese.aggiungi(DB, campi.get("data", ""), campi.get("categoria", ""),
                               campi.get("descrizione", ""), campi.get("importo", ""))
            except ValueError as errore:
                self.rispondi(pagina(campi.get("data", "")[:7], f"Non ho salvato: {errore}"))
                return
            self.torna(campi["data"][:7])
        elif self.path == "/elimina":
            spese.elimina(DB, int(campi["id"]))
            self.torna(campi.get("mese", ""))


if __name__ == "__main__":
    print("Spese di casa: apri http://localhost:8000 (Ctrl+C per fermare)")
    HTTPServer(("localhost", 8000), Gestore).serve_forever()
