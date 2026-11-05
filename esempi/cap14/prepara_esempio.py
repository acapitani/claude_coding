"""Prepara i file d'esempio del capitolo 14: un elenco Excel di 50 clienti
inventati (con due righe difettose, come succede davvero) e un modello Word."""
import random
from datetime import date, timedelta

import docx
from docx.shared import Pt
from openpyxl import Workbook

random.seed(14)
NOMI = ["Giulia", "Marco", "Francesca", "Luca", "Sara", "Andrea", "Chiara", "Paolo",
        "Elena", "Davide", "Martina", "Stefano", "Valentina", "Matteo", "Laura"]
COGNOMI = ["Rossi", "Bianchi", "Ferrari", "Esposito", "Romano", "Colombo", "Ricci",
           "Marino", "Greco", "Bruno", "Gallo", "Conti", "De Luca", "Costa", "Fontana"]
CITTA = ["Milano", "Torino", "Bologna", "Firenze", "Roma", "Napoli", "Bari", "Verona"]

wb = Workbook()
ws = wb.active
ws.title = "Clienti"
ws.append(["Titolo", "Nome", "Cognome", "Città", "Fattura", "Importo", "Scadenza"])
for i in range(50):
    nome = random.choice(NOMI)
    # Prima versione: titolo a caso -> «Dott.ssa Marco» in 22 lettere su 50.
    # Il titolo deve concordare con il nome.
    maschile = nome in {"Marco", "Luca", "Paolo", "Andrea", "Davide", "Stefano", "Matteo"}
    titolo = random.choice(["Sig.", "Dott."] if maschile else ["Sig.ra", "Dott.ssa"])
    scad = date(2026, 10, 1) + timedelta(days=random.randint(0, 30))
    ws.append([titolo, nome, random.choice(COGNOMI), random.choice(CITTA),
               f"2026/{300 + i}", round(random.uniform(80, 2400), 2), scad])
ws["F18"] = None            # una riga senza importo
ws["C33"] = "  ferrari "    # un cognome scritto male
wb.save("clienti.xlsx")

d = docx.Document()
d.styles["Normal"].font.name = "Calibri"
d.styles["Normal"].font.size = Pt(11)
for testo in ["Studio Amministrativo Bianchi", "Via Roma 12, 40121 Bologna", "",
              "Bologna, {oggi}", "", "{titolo} {nome} {cognome}", "{citta}", "",
              "Oggetto: sollecito di pagamento della fattura n. {fattura}", "",
              "Gentile {titolo} {cognome},",
              "ci risulta ancora da saldare la fattura n. {fattura} di {importo}, "
              "scaduta il {scadenza}. Le chiediamo cortesemente di provvedere entro "
              "quindici giorni dal ricevimento di questa lettera.",
              "Se ha già effettuato il pagamento, la preghiamo di non tenere conto di questo "
              "avviso e di scusarci per il disturbo.", "", "Cordiali saluti,", "",
              "Anna Bianchi"]:
    d.add_paragraph(testo)
d.save("modello-sollecito.docx")
print("creati clienti.xlsx e modello-sollecito.docx")
