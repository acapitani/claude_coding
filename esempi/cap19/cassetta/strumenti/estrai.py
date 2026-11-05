"""Da una cartella di fatture PDF a un foglio Excel.

Uso: py estrai.py [cartella_fatture]
Per ogni fattura: fornitore, numero, data, imponibile, IVA, totale.
Controlla che imponibile + IVA = totale; le scansioni (PDF senza testo)
vengono segnalate a parte, da leggere come immagini.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

import pymupdf
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

MESI = {m: i for i, m in enumerate(["gennaio", "febbraio", "marzo", "aprile", "maggio",
        "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"], 1)}
IMPORTO = r"([\d.]+,\d{2})"


def numero(testo):                          # "1.234,56" -> 1234.56
    return float(testo.replace(".", "").replace(",", "."))


def cerca(schema, testo):
    m = re.search(schema, testo)
    return m.group(1) if m else None


def leggi_data(testo):
    if m := re.search(r"(\d{2})[/.](\d{2})[/.](\d{4})", testo):        # 14/03/2026, 14.03.2026
        return datetime(int(m[3]), int(m[2]), int(m[1])).date()
    if m := re.search(r"(\d{1,2}) (" + "|".join(MESI) + r") (\d{4})", testo):  # 3 marzo 2026
        return datetime(int(m[3]), MESI[m[2]], int(m[1])).date()
    return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    cartella = Path(sys.argv[1] if len(sys.argv) > 1 else "fatture")
    righe, scansioni, problemi = [], [], []
    for pdf in sorted(cartella.glob("*.pdf")):
        testo = "".join(pagina.get_text() for pagina in pymupdf.open(pdf))
        if len(testo.strip()) < 20:             # niente testo: è un'immagine
            scansioni.append(pdf.name)
            continue
        dati = {
            "file": pdf.name,
            "fornitore": testo.strip().splitlines()[0],
            "numero": cerca(r"(?:Fattura n\.|DOCUMENTO N°|Fatt\.)\s*([\w/-]+)", testo),
            "data": leggi_data(testo),
            "imponibile": cerca(r"Imponibile\s+" + IMPORTO, testo),
            "iva": cerca(r"IVA \d+%\s+" + IMPORTO, testo),
            "totale": cerca(r"(?:Totale documento|TOTALE DA PAGARE|Totale fattura)\W+" + IMPORTO, testo),
            # \W+: tra etichetta e cifra può esserci di tutto (spazi, «€», o un carattere illeggibile)
        }
        mancanti = [k for k, v in dati.items() if v is None]
        if mancanti:
            problemi.append(f"{pdf.name}: non trovo {', '.join(mancanti)}")
            continue
        for k in ("imponibile", "iva", "totale"):
            dati[k] = numero(dati[k])
        if abs(dati["imponibile"] + dati["iva"] - dati["totale"]) > 0.01:
            problemi.append(f"{pdf.name}: imponibile + IVA = "
                            f"{dati['imponibile'] + dati['iva']:.2f}, ma il totale è {dati['totale']:.2f}")
        righe.append(dati)

    wb = Workbook()
    ws = wb.active
    ws.title = "Fatture"
    colonne = ["file", "fornitore", "numero", "data", "imponibile", "iva", "totale"]
    ws.append([c.capitalize() for c in colonne])
    for d in sorted(righe, key=lambda r: r["data"]):
        ws.append([d[c] for c in colonne])
    for cella in ws[1]:
        cella.font = Font(bold=True)
        cella.fill = PatternFill("solid", fgColor="F4F1EA")
    for c, larghezza in zip("ABCDEFG", (14, 28, 12, 12, 13, 11, 13)):
        ws.column_dimensions[c].width = larghezza
    for riga in ws.iter_rows(min_row=2):
        riga[3].number_format = "DD/MM/YYYY"
        for cella in riga[4:]:
            cella.number_format = '#,##0.00 "€"'
    wb.save("fatture.xlsx")

    print(f"Fatture lette: {len(righe)} su {len(list(cartella.glob('*.pdf')))}  ->  fatture.xlsx")
    totale = sum(d["totale"] for d in righe)
    print("Totale delle fatture lette:", f"{totale:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
    for s in scansioni:
        print(f"  - {s}: è una scansione (nessun testo): da leggere come immagine")
    for p in problemi:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
