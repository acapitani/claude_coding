"""Unisce gli estratti mensili in un unico riepilogo.xlsx con formule e grafico.

Uso: py unisci.py [cartella_estratti]
Fogli prodotti:  Movimenti (tutte le righe, ripulite)
                 Mesi      (entrate, uscite e saldo per mese, con FORMULE)
"""
import sys
from datetime import date, datetime
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill

MESI = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
        "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
EURO = '#,##0.00 "€";[Red]-#,##0.00 "€"'


def leggi_data(valore):
    if isinstance(valore, datetime):
        return valore.date()
    if isinstance(valore, date):
        return valore
    return datetime.strptime(str(valore).strip(), "%d/%m/%Y").date()   # "14/11/2026"


def leggi_importo(valore):
    if isinstance(valore, (int, float)):
        return float(valore)
    s = str(valore).strip().replace(".", "").replace(",", ".")        # "1.234,56"
    return float(s)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    cartella = Path(sys.argv[1] if len(sys.argv) > 1 else "estratti")
    movimenti, note, testo_imp = [], [], {}
    for file in sorted(cartella.glob("*.xlsx")):
        foglio = load_workbook(file, data_only=True).active
        intest = [str(c.value).strip().lower() for c in foglio[1]]
        if intest != ["data", "descrizione", "importo"]:
            note.append(f"{file.name}: colonne nell'ordine {intest}, riordinate")
        col = {nome: intest.index(nome) for nome in ("data", "descrizione", "importo")}
        visti = set()
        for riga in foglio.iter_rows(min_row=2, values_only=True):
            if all(v is None for v in riga):
                continue
            grezzo_data, grezzo_imp = riga[col["data"]], riga[col["importo"]]
            m = (leggi_data(grezzo_data), str(riga[col["descrizione"]]).strip(),
                 leggi_importo(grezzo_imp))
            if isinstance(grezzo_imp, str):
                testo_imp.setdefault(file.name, []).append(grezzo_imp)
            if isinstance(grezzo_data, str):
                note.append(f"{file.name}: data scritta come testo «{grezzo_data}»")
            if m in visti:
                note.append(f"{file.name}: riga ripetuta {m[0]:%d/%m} {m[1]} {m[2]:.2f}"
                            " (tenuta una sola volta: controlla che non fossero due pagamenti veri)")
                continue
            visti.add(m)
            movimenti.append(m)
    for nome, esempi in testo_imp.items():
        note.append(f"{nome}: {len(esempi)} importi scritti come testo (es. «{esempi[0]}»), convertiti")
    movimenti.sort()

    wb = Workbook()
    ws = wb.active
    ws.title = "Movimenti"
    ws.append(["Data", "Descrizione", "Importo", "Mese"])
    for d, descr, imp in movimenti:
        ws.append([d, descr, imp, d.month])
    for cella in ws["C"][1:]:
        cella.number_format = EURO
    for cella in ws["A"][1:]:
        cella.number_format = "DD/MM/YYYY"

    riep = wb.create_sheet("Mesi")
    riep.append(["Mese", "Entrate", "Uscite", "Saldo"])
    n = len(movimenti) + 1
    for i, nome in enumerate(MESI, start=1):
        r = i + 1
        riep.append([
            nome,
            f'=SUMIFS(Movimenti!$C$2:$C${n},Movimenti!$D$2:$D${n},{i},Movimenti!$C$2:$C${n},">0")',
            f'=-SUMIFS(Movimenti!$C$2:$C${n},Movimenti!$D$2:$D${n},{i},Movimenti!$C$2:$C${n},"<0")',
            f"=B{r}-C{r}",
        ])
    riep.append(["Totale anno", "=SUM(B2:B13)", "=SUM(C2:C13)", "=SUM(D2:D13)"])
    for riga in riep.iter_rows(min_row=2, min_col=2, max_col=4):
        for cella in riga:
            cella.number_format = EURO
    for foglio in (ws, riep):
        for cella in foglio[1]:
            cella.font = Font(bold=True)
            cella.fill = PatternFill("solid", fgColor="F4F1EA")
        foglio.column_dimensions["A"].width = 14
        foglio.column_dimensions["B"].width = 22
        foglio.column_dimensions["C"].width = 16
        foglio.column_dimensions["D"].width = 16
    riep["A14"].font = Font(bold=True)

    grafico = BarChart()
    grafico.title = "Entrate e uscite 2026"
    grafico.y_axis.title = "euro"
    grafico.add_data(Reference(riep, min_col=2, max_col=3, min_row=1, max_row=13), titles_from_data=True)
    grafico.set_categories(Reference(riep, min_col=1, min_row=2, max_row=13))
    grafico.width, grafico.height = 22, 11
    riep.add_chart(grafico, "F2")
    riep.page_setup.orientation = "landscape"          # in stampa: tabella e grafico
    riep.page_setup.fitToWidth = 1                       # sulla stessa pagina
    riep.page_setup.fitToHeight = 1
    riep.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save("riepilogo.xlsx")

    entrate = sum(i for _, _, i in movimenti if i > 0)
    uscite = -sum(i for _, _, i in movimenti if i < 0)
    print(f"Movimenti uniti: {len(movimenti)} da {len(list(cartella.glob('*.xlsx')))} file")
    print(f"Controllo: entrate {entrate:,.2f}  uscite {uscite:,.2f}  saldo {entrate - uscite:,.2f}"
          .replace(",", "X").replace(".", ",").replace("X", "."))
    print("Sistemazioni fatte:")
    for nota in dict.fromkeys(note):         # senza ripetizioni
        print("  -", nota)


if __name__ == "__main__":
    main()
