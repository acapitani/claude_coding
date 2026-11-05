"""Prepara 30 fatture PDF inventate di tre fornitori, ognuno con il suo stile,
più i casi difficili: una fattura con un totale sbagliato e una scansionata."""
import random
from datetime import date, timedelta
from pathlib import Path

import pymupdf

random.seed(16)
FORNITORI = [
    {"nome": "Cartoleria Europa Srl", "piva": "01234560987", "num": "Fattura n. {n}",
     "data": "Data: {d:%d/%m/%Y}", "tot": "Totale documento"},
    {"nome": "TecnoService S.p.A.", "piva": "09876540321", "num": "DOCUMENTO N° TS-{n}",
     "data": "del {d:%d.%m.%Y}", "tot": "TOTALE DA PAGARE"},
    {"nome": "Pulizie Lampo di G. Neri", "piva": "05555550123", "num": "Fatt. {n}/2026",
     "data": "Bologna, {gg} {mese} 2026", "tot": "Totale fattura €"},
]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
        "settembre", "ottobre", "novembre", "dicembre"]


def euro(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


cartella = Path("fatture")
cartella.mkdir(exist_ok=True)
for i in range(30):
    f = FORNITORI[i % 3]
    d = date(2026, 1, 1) + timedelta(days=random.randint(0, 300))
    imponibile = round(random.uniform(60, 3000), 2)
    iva = round(imponibile * 0.22, 2)
    totale = round(imponibile + iva, 2)
    if i == 13:
        totale = round(totale + 100, 2)          # errore nella fattura: totale che non torna
    doc = pymupdf.open()
    p = doc.new_page(width=595, height=842)
    y = 60
    def riga(testo, size=11, x=60, bold=False):
        global y
        p.insert_text((x, y), testo, fontsize=size, fontname="hebo" if bold else "helv")
        y += size + 9
    riga(f["nome"], 16, bold=True)
    riga(f"P. IVA {f['piva']}", 9)
    y += 20
    riga(f["num"].format(n=100 + i), 12, bold=True)
    riga(f["data"].format(d=d, gg=d.day, mese=MESI[d.month - 1]))
    y += 10
    riga("Spett.le Studio Amministrativo Bianchi - Via Roma 12, Bologna", 10)
    y += 25
    riga("Descrizione", 10, bold=True)
    riga(random.choice(["Materiale di cancelleria", "Assistenza informatica", "Pulizia uffici",
                        "Toner e carta", "Manutenzione stampanti"]), 10)
    y += 20
    riga(f"Imponibile          {euro(imponibile)}", 10)
    riga(f"IVA 22%             {euro(iva)}", 10)
    riga(f"{f['tot']}   {euro(totale)}", 12, bold=True)
    nome = cartella / f"fattura-{i + 1:02d}.pdf"
    if i == 22:
        # la scansione: la pagina diventa un'immagine leggermente storta, senza testo
        pix = p.get_pixmap(dpi=150, colorspace=pymupdf.csGRAY)
        scan = pymupdf.open()
        sp = scan.new_page(width=595, height=842)
        sp.insert_image(sp.rect, pixmap=pix, rotate=0)
        scan.save(nome, deflate=True, garbage=3)
    else:
        doc.save(nome)
print("create 30 fatture in", cartella)
