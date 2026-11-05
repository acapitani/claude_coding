"""Spese di casa — la parte che gestisce i dati (database SQLite).

Tutte le funzioni ricevono una connessione al database, così i test
possono usare un database in memoria senza toccare quello vero.
"""
import sqlite3
from datetime import date

CATEGORIE = ["Casa", "Spesa", "Trasporti", "Salute", "Svago", "Altro"]


def apri(percorso="spese.db"):
    """Apre (o crea) il database e prepara la tabella delle spese."""
    db = sqlite3.connect(percorso)
    db.execute("""
        CREATE TABLE IF NOT EXISTS spese (
            id          INTEGER PRIMARY KEY,
            data        TEXT NOT NULL,      -- AAAA-MM-GG
            categoria   TEXT NOT NULL,
            descrizione TEXT NOT NULL,
            centesimi   INTEGER NOT NULL    -- importi in centesimi
        )""")
    return db


def leggi_importo(testo):
    """'12,50' o '1.234,5' -> centesimi (int). Errore se non è valido."""
    s = testo.strip().replace("€", "").strip()
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        euro = float(s)
    except ValueError:
        # il messaggio di Python è in inglese: ne diamo uno comprensibile
        raise ValueError(f"«{testo}» non è un importo valido (esempio: 12,50)")
    if euro <= 0:
        raise ValueError("L'importo deve essere positivo")
    return round(euro * 100)


def aggiungi(db, giorno, categoria, descrizione, importo):
    """Registra una spesa. 'importo' è un testo come '12,50'."""
    if categoria not in CATEGORIE:
        raise ValueError(f"Categoria sconosciuta: {categoria}")
    try:
        date.fromisoformat(giorno)        # controlla che la data esista
    except ValueError:
        raise ValueError(f"«{giorno}» non è una data valida")
    if not descrizione.strip():
        raise ValueError("Manca la descrizione")
    db.execute("INSERT INTO spese (data, categoria, descrizione, centesimi)"
               " VALUES (?, ?, ?, ?)",
               (giorno, categoria, descrizione.strip(), leggi_importo(importo)))
    db.commit()


def elimina(db, id_spesa):
    db.execute("DELETE FROM spese WHERE id = ?", (id_spesa,))
    db.commit()


def del_mese(db, mese):
    """Le spese di un mese ('AAAA-MM'), dalla più recente."""
    return db.execute("SELECT id, data, categoria, descrizione, centesimi"
                      " FROM spese WHERE substr(data, 1, 7) = ?"
                      " ORDER BY data DESC, id DESC", (mese,)).fetchall()


def totali_per_categoria(db, mese):
    """{categoria: centesimi} per il mese, solo le categorie con spese."""
    righe = db.execute("SELECT categoria, SUM(centesimi) FROM spese"
                       " WHERE substr(data, 1, 7) = ?"
                       " GROUP BY categoria", (mese,)).fetchall()
    return {c: t for c, t in sorted(righe, key=lambda r: -r[1])}


def mese_precedente(mese):
    """'2026-01' -> '2025-12'."""
    anno, m = int(mese[:4]), int(mese[5:7])
    return f"{anno - 1}-12" if m == 1 else f"{anno}-{m - 1:02d}"


def totale(db, mese):
    """Totale del mese in centesimi (0 se non ci sono spese)."""
    return sum(totali_per_categoria(db, mese).values())


def euro(centesimi):
    """1234567 -> '12.345,67 €' (formato italiano)."""
    intero, cent = divmod(centesimi, 100)
    migliaia = f"{intero:,}".replace(",", ".")
    return f"{migliaia},{cent:02d} €"


def esporta_csv(db, mese):
    """Il mese in formato CSV (separatore ';', come lo vuole Excel in italiano)."""
    righe = ["data;categoria;descrizione;importo"]
    for _, d, c, descr, cent in reversed(del_mese(db, mese)):
        importo = f"{cent // 100},{cent % 100:02d}"
        righe.append(f"{d};{c};{descr.replace(';', ',')};{importo}")
    return "\n".join(righe) + "\n"
