"""Stampa unione: una lettera Word per ogni riga dell'elenco Excel.

Uso: py lettere.py [clienti.xlsx] [modello-sollecito.docx]
Le lettere finiscono nella cartella 'lettere'. Le righe con dati mancanti
non producono lettere: vengono elencate alla fine, da sistemare a mano.
"""
import sys
from datetime import date, datetime
from pathlib import Path

import docx
from openpyxl import load_workbook

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def data_italiana(d):
    giorno = "1°" if d.day == 1 else str(d.day)          # «il 1° ottobre», non «il 1 ottobre»
    return f"{giorno} {MESI[d.month - 1]} {d.year}"


def con_articolo(d):
    """«l'8 ottobre», «l'11 ottobre», ma «il 14 ottobre» (errore trovato dai revisori del cap. 22)."""
    return ("l'" if d.day in (8, 11) else "il ") + data_italiana(d)


def euro(valore):
    intero, cent = divmod(round(valore * 100), 100)
    return f"{intero:,}".replace(",", ".") + f",{cent:02d} €"


def sostituisci(paragrafo, campi):
    """Sostituisce i {segnaposto} mantenendo la formattazione del paragrafo."""
    testo = paragrafo.text
    if "{" not in testo:
        return
    for chiave, valore in campi.items():
        testo = testo.replace("{" + chiave + "}", valore)
    # Word spesso spezza il testo in più "pezzi" (run): li riuniamo nel primo
    for run in paragrafo.runs[1:]:
        run.text = ""
    paragrafo.runs[0].text = testo


def main():
    elenco = sys.argv[1] if len(sys.argv) > 1 else "clienti.xlsx"
    modello = sys.argv[2] if len(sys.argv) > 2 else "modello-sollecito.docx"
    uscita = Path("lettere")
    uscita.mkdir(exist_ok=True)

    foglio = load_workbook(elenco, data_only=True).active
    intestazioni = [c.value for c in foglio[1]]
    fatte, scartate = 0, []
    for n, riga in enumerate(foglio.iter_rows(min_row=2, values_only=True), start=2):
        r = dict(zip(intestazioni, riga))
        mancanti = [k for k in ("Nome", "Cognome", "Importo", "Scadenza") if not r.get(k)]
        if mancanti:
            scartate.append(f"riga {n}: manca {', '.join(mancanti)}")
            continue
        scadenza = r["Scadenza"]
        if isinstance(scadenza, datetime):
            scadenza = scadenza.date()
        campi = {
            "oggi": data_italiana(date.today()),
            "titolo": r["Titolo"] or "",
            "nome": str(r["Nome"]).strip(),
            "cognome": str(r["Cognome"]).strip().title(),   # "  ferrari " -> "Ferrari"
            "citta": r["Città"] or "",
            "fattura": str(r["Fattura"]),
            "importo": euro(r["Importo"]),
            "scadenza": con_articolo(scadenza),
        }
        lettera = docx.Document(modello)
        for p in lettera.paragraphs:
            sostituisci(p, campi)
        rimasti = [p.text for p in lettera.paragraphs if "{" in p.text]
        if rimasti:
            scartate.append(f"riga {n}: segnaposto non sostituiti in «{rimasti[0][:40]}»")
            continue
        nome_file = f"sollecito-{n - 1:02d}-{campi['cognome'].lower().replace(' ', '')}.docx"
        lettera.save(uscita / nome_file)
        fatte += 1

    print(f"Lettere create: {fatte} (cartella '{uscita}')")
    if scartate:
        print("Da controllare a mano:")
        for s in scartate:
            print("  -", s)


if __name__ == "__main__":
    main()
