"""Prepara vendite.csv: le vendite giornaliere inventate di tre negozi, settembre-ottobre 2026."""
import csv
import random
from datetime import date, timedelta

random.seed(18)
NEGOZI = {"Bologna": 1.0, "Modena": 0.7, "Parma": 0.55}
PRODOTTI = {"Caffè": 9.5, "Tè": 6.0, "Biscotti": 4.2, "Cioccolato": 3.8}
with open("vendite.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["data", "negozio", "prodotto", "pezzi", "incasso"])
    giorno = date(2026, 9, 7)
    while giorno <= date(2026, 11, 1):
        if giorno.weekday() < 6:                    # domenica chiuso
            for negozio, peso in NEGOZI.items():
                for prodotto, prezzo in PRODOTTI.items():
                    pezzi = max(0, round(random.gauss(30, 9) * peso * (1.25 if giorno.weekday() == 5 else 1)))
                    if negozio == "Modena" and giorno >= date(2026, 10, 26) and prodotto == "Caffè":
                        pezzi = round(pezzi * 0.4)  # ultima settimana: crollo del caffè a Modena
                    w.writerow([giorno.isoformat(), negozio, prodotto, pezzi,
                                f"{pezzi * prezzo:.2f}".replace(".", ",")])
        giorno += timedelta(days=1)
print("creato vendite.csv")
