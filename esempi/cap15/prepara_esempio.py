"""Prepara 12 estratti conto mensili inventati (estratti/2026-01.xlsx … 2026-12.xlsx),
con i difetti tipici dei file veri: colonne in ordine diverso, importi scritti
come testo, una riga ripetuta, una data scritta come testo."""
import random
from datetime import date
from pathlib import Path

from openpyxl import Workbook

random.seed(15)
VOCI = [  # (descrizione, importo minimo, massimo, peso): positivi = entrate
    ("Vendite", 200, 3500, 5), ("Incasso fattura", 800, 6000, 3),
    ("Affitto ufficio", -1200, -1200, 0), ("Stipendi", -2800, -2200, 0),
    ("Utenze", -380, -90, 2), ("Fornitore materiali", -2500, -150, 4),
    ("Spese bancarie", -25, -2, 2)]
cartella = Path("estratti")
cartella.mkdir(exist_ok=True)
for mese in range(1, 13):
    wb = Workbook()
    ws = wb.active
    ws.title = "Movimenti"
    intest = ["Data", "Descrizione", "Importo"]
    if mese == 5:                       # maggio: colonne in un altro ordine
        intest = ["Descrizione", "Data", "Importo"]
    ws.append(intest)
    righe = [[date(2026, mese, 1), "Affitto ufficio", -1200.0],
             [date(2026, mese, 27), "Stipendi", round(random.uniform(-2800, -2200), 2)]]
    variabili = [v for v in VOCI if v[3] > 0]
    for _ in range(random.randint(14, 20)):
        voce, minimo, massimo, _ = random.choices(variabili, [v[3] for v in variabili])[0]
        importo = round(random.uniform(minimo, massimo), 2)
        righe.append([date(2026, mese, random.randint(1, 28)), voce, importo])
    righe.sort()
    if mese == 8:                       # agosto: una riga copiata due volte
        righe.insert(5, list(righe[4]))
    for g, v, imp in righe:
        if mese == 3:                   # marzo: importi esportati come testo, con la virgola
            imp = f"{imp:.2f}".replace(".", ",")
        if mese == 11 and v == "Utenze":  # novembre: una data scritta come testo
            g = g.strftime("%d/%m/%Y")
        ws.append([v, g, imp] if mese == 5 else [g, v, imp])
    wb.save(cartella / f"2026-{mese:02d}.xlsx")
print("creati 12 estratti in", cartella)
