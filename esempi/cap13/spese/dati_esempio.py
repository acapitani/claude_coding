"""Riempie spese.db con due mesi di spese inventate, per provare l'applicazione."""
import spese

ESEMPIO = [
    ("2026-09-01", "Casa", "Affitto", "650"),
    ("2026-09-04", "Spesa", "Supermercato", "71,10"),
    ("2026-09-15", "Casa", "Bolletta gas", "41,80"),
    ("2026-09-22", "Spesa", "Supermercato", "66,30"),
    ("2026-10-01", "Casa", "Affitto", "650"),
    ("2026-10-02", "Spesa", "Supermercato", "62,40"),
    ("2026-10-05", "Trasporti", "Abbonamento autobus", "35"),
    ("2026-10-07", "Salute", "Farmacia", "18,90"),
    ("2026-10-09", "Spesa", "Mercato rionale", "23,15"),
    ("2026-10-12", "Svago", "Cinema", "16"),
    ("2026-10-14", "Casa", "Bolletta luce", "74,32"),
    ("2026-10-16", "Spesa", "Supermercato", "58,75"),
    ("2026-10-20", "Trasporti", "Benzina", "50"),
    ("2026-10-23", "Svago", "Pizzeria", "38,50"),
    ("2026-10-26", "Spesa", "Supermercato", "47,20"),
    ("2026-10-28", "Altro", "Regalo compleanno", "30"),
]

if __name__ == "__main__":
    db = spese.apri()
    for riga in ESEMPIO:
        spese.aggiungi(db, *riga)
    print(f"Aggiunte {len(ESEMPIO)} spese di esempio in spese.db")
