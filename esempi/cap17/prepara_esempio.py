"""Prepara la cartella foto/ con 400 foto inventate (immagini minuscole con data di
scatto EXIF), in sottocartelle per luogo, con i difetti delle cartelle vere:
foto senza data (inoltrate da app di messaggi), doppioni, scatti nello stesso secondo."""
import random
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from PIL import Image

random.seed(17)
LUOGHI = {"Roma": 140, "Firenze": 120, "Lago di Garda": 100, "Senza nome": 40}
radice = Path("foto")
shutil.rmtree(radice, ignore_errors=True)
n = 0
for luogo, quante in LUOGHI.items():
    cartella = radice / luogo
    cartella.mkdir(parents=True)
    inizio = datetime(2026, random.randint(4, 9), random.randint(1, 20), 9, 0, 0)
    for i in range(quante):
        n += 1
        scatto = inizio + timedelta(days=random.randint(0, 3), minutes=random.randint(0, 600))
        if i % 25 == 3:                                   # raffica: stesso secondo della precedente
            scatto = ultimo
        ultimo = scatto
        img = Image.new("RGB", (32, 24), tuple(random.randint(0, 255) for _ in range(3)))
        exif = Image.Exif()
        if not (luogo == "Senza nome" and i % 2 == 0):    # metà delle «Senza nome» non ha data
            exif[0x0132] = scatto.strftime("%Y:%m:%d %H:%M:%S")          # DateTime
            exif.get_ifd(0x8769)[0x9003] = scatto.strftime("%Y:%m:%d %H:%M:%S")  # DateTimeOriginal
        nome = f"IMG_{4000 + n}.jpg" if luogo != "Senza nome" else f"IMG-2026-WA{n:04d}.jpg"
        img.save(cartella / nome, exif=exif, quality=60)
# doppioni: tre foto copiate con un altro nome
for src in random.sample(sorted((radice / "Roma").glob("*.jpg")), 3):
    shutil.copy2(src, src.with_name(src.stem + " (1).jpg"))
print("create", sum(1 for _ in radice.rglob("*.jpg")), "foto in", radice)
