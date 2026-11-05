"""Rinomina le foto in AAAA-MM-GG_HHMMSS_luogo.jpg usando la data di scatto.

Uso:
  py rinomina.py foto            prova a secco: scrive piano.csv, non tocca niente
  py rinomina.py foto --esegui   rinomina davvero e scrive annulla.csv
  py rinomina.py --annulla       rimette tutti i nomi com'erano

Il luogo è il nome della sottocartella. Le foto senza data e i doppioni
non vengono toccati: finiscono nell'elenco da controllare.
"""
import csv
import hashlib
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image


def data_scatto(file):
    exif = Image.open(file).getexif()
    testo = exif.get_ifd(0x8769).get(0x9003) or exif.get(0x0132)     # DateTimeOriginal, DateTime
    return datetime.strptime(testo, "%Y:%m:%d %H:%M:%S") if testo else None


def impronta(file):
    return hashlib.sha256(file.read_bytes()).hexdigest()


def piano(radice):
    righe, problemi, visti, usati = [], [], {}, set()
    # le copie («IMG_4001 (1).jpg») dopo gli originali: così il doppione segnalato è la copia
    ordine = lambda f: (str(f.parent), " (" in f.name, f.name)
    for file in sorted(radice.rglob("*.jpg"), key=ordine):
        h = impronta(file)
        if h in visti:
            problemi.append(f"{file.relative_to(radice)}: doppione di {visti[h]}")
            continue
        visti[h] = file.relative_to(radice)
        quando = data_scatto(file)
        if quando is None:
            problemi.append(f"{file.relative_to(radice)}: nessuna data di scatto")
            continue
        luogo = file.parent.name.lower().replace(" ", "-")
        base = f"{quando:%Y-%m-%d_%H%M%S}_{luogo}"
        nuovo, k = f"{base}.jpg", 2
        while (file.parent / nuovo) in usati:                      # due scatti nello stesso secondo
            nuovo, k = f"{base}_{k}.jpg", k + 1
        usati.add(file.parent / nuovo)
        righe.append((str(file), str(file.parent / nuovo)))
    return righe, problemi


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--annulla" in sys.argv:
        with open("annulla.csv", encoding="utf-8") as f:
            coppie = list(csv.reader(f))[1:]
        for nuovo, vecchio in coppie:
            Path(nuovo).rename(vecchio)
        print(f"Ripristinati {len(coppie)} nomi originali.")
        return
    radice = Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "foto")
    righe, problemi = piano(radice)
    with open("piano.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nome attuale", "nuovo nome"])
        w.writerows(righe)
    if "--esegui" in sys.argv:
        for vecchio, nuovo in righe:
            if Path(nuovo).exists():
                raise SystemExit(f"Mi fermo: {nuovo} esiste già")
        with open("annulla.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nome attuale", "nome originale"])
            for vecchio, nuovo in righe:
                Path(vecchio).rename(nuovo)
                w.writerow([nuovo, vecchio])
        print(f"Rinominate {len(righe)} foto. Per tornare indietro: py rinomina.py --annulla")
    else:
        print(f"PROVA A SECCO: {len(righe)} foto da rinominare (vedi piano.csv). Nessun file toccato.")
        for vecchio, nuovo in righe[:3]:
            print(f"  {Path(vecchio).name}  ->  {Path(nuovo).name}")
    if problemi:
        print(f"Da controllare a mano ({len(problemi)}):")
        for p in problemi[:4]:
            print("  -", p)
        if len(problemi) > 4:
            print(f"  … e altre {len(problemi) - 4}")


if __name__ == "__main__":
    main()
