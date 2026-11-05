"""Impaginazione completa: costruisce il .docx, lo converte in PDF con LibreOffice, legge dal PDF
i numeri di pagina reali di titoli e voci analitiche, e ricostruisce finché i numeri sono stabili.

Uso:
    py build/update_indexes.py                       # libro (book.yaml)
    py build/update_indexes.py --config book-prova.yaml

Perché così e non con una macro LibreOffice: il .docx finale resta quello prodotto da python-docx
(nessun passaggio di salvataggio da LibreOffice che altererebbe gli stili), e l'indice contiene già
i numeri giusti anche aprendo il file con un visualizzatore che non aggiorna i campi.
In Word i campi restano aggiornabili (F9) se l'impaginazione di Word differisce da quella di LibreOffice.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).parent))
import build_book  # noqa: E402
import comune  # noqa: E402

PT_CM = 72 / 2.54
RE_ROMANO = re.compile(r"^[ivxlcdm]+$")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = s.replace("’", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def etichette_pagine(pdf: pymupdf.Document, cfg: dict) -> list[str | None]:
    """Numero stampato in ogni pagina, letto dal piè di pagina; le pagine senza numero
    (aperture di parte, pagine bianche) lo ricavano dalla pagina numerata più vicina."""
    m = cfg["pagina"]["margini_cm"]
    lette: list[str | None] = []
    for pagina in pdf:
        h = pagina.rect.height
        zona = pymupdf.Rect(0, h - m["inferiore"] * PT_CM, pagina.rect.width, h)
        parole = [w[4] for w in pagina.get_text("words", clip=zona)]
        etichetta = None
        for w in parole:
            if w.isdigit() or RE_ROMANO.match(w):
                etichetta = w
        lette.append(etichetta)
    risultato = list(lette)
    for i, e in enumerate(lette):
        if e is not None:
            continue
        # cerca la prossima pagina numerata dello stesso tipo
        for j in range(i + 1, len(lette)):
            if lette[j] is not None:
                if lette[j].isdigit() and int(lette[j]) - (j - i) >= 1:
                    risultato[i] = str(int(lette[j]) - (j - i))
                elif RE_ROMANO.match(lette[j]):
                    n = da_romano(lette[j]) - (j - i)
                    risultato[i] = a_romano(n) if n >= 1 else None
                break
    return risultato


def da_romano(s: str) -> int:
    val = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    tot = 0
    for a, b in zip(s, s[1:] + " "):
        tot += -val[a] if b != " " and val[a] < val[b] else val[a]
    return tot


def a_romano(n: int) -> str:
    out = ""
    for v, s in ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"),
                 (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out, n = out + s, n - v
    return out


def righe_per_dimensione(pagina) -> list[tuple[float, str]]:
    out = []
    for b in pagina.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            spans = l["spans"]
            if spans:
                out.append((max(s["size"] for s in spans), "".join(s["text"] for s in spans)))
    return out


def trova_voci(pdf, voci: list[dict], inizio: int) -> dict[str, int]:
    """Pagina fisica (0-based) di ogni voce, cercandole in ordine a partire da `inizio`."""
    trovate, cursore = {}, inizio
    cache = {}
    for v in voci:
        chiave = norm(v.get("cerca") or v["testo"])[:28]
        for p in range(cursore, len(pdf)):
            if p not in cache:
                cache[p] = righe_per_dimensione(pdf[p])
            righe = cache[p]
            # unisce righe consecutive della stessa dimensione (titoli su più righe)
            testo = " ".join(t for d, t in righe if abs(d - v["dimensione"]) < 1.2)
            if chiave and chiave in norm(testo):
                trovate[v["id"]] = p
                cursore = p
                break
        else:
            comune.avviso(f"voce non trovata nel PDF: {v['testo'][:50]}")
    return trovate


def trova_xe(pdf, xe: list[dict], pagina_voce: dict[str, int], voci: list[dict]) -> list[int | None]:
    # i capitoli (e le parti) delimitano la ricerca; i sottotitoli no
    inizi = sorted({pagina_voce[v["id"]] for v in voci if v["livello"] in (1, 3) and v["id"] in pagina_voce})
    risultato, cursori = [], {}
    for x in xe:
        p0 = pagina_voce.get(x["capitolo"])
        if p0 is None:
            risultato.append(None)
            continue
        dopo = [p for p in inizi if p > p0]
        p1 = dopo[0] if dopo else len(pdf)
        cur = cursori.get(x["capitolo"], p0)
        chiave = norm(x["testo"])
        trovata = None
        for p in range(cur, p1):
            testo = norm(pdf[p].get_text().replace("-\n", ""))
            if chiave and chiave in testo:
                trovata = p
                break
        if trovata is None:
            trovata = cur
        cursori[x["capitolo"]] = trovata
        risultato.append(trovata)
    return risultato


def calcola_bianche(pdf, sezioni: list[dict], bianche_attuali: set[str]) -> list[str]:
    """Decide prima di quali sezioni serve una pagina bianca perché inizino a destra.
    Misura la lunghezza di ogni sezione nel PDF (indipendente dalle pagine bianche, perché ogni
    sezione inizia comunque su una pagina nuova) e ricalcola le posizioni da capo."""
    inizi = trova_voci(pdf, sezioni, 0)
    if len(inizi) != len(sezioni):
        comune.avviso("non tutte le sezioni trovate nel PDF: pagine bianche invariate")
        return sorted(bianche_attuali)
    pos_inizio = [inizi[s["id"]] + 1 for s in sezioni]          # pagine fisiche, da 1
    lunghezze = []
    for k, s in enumerate(sezioni):
        fine = pos_inizio[k + 1] - (1 if sezioni[k + 1]["id"] in bianche_attuali else 0) if k + 1 < len(sezioni) else len(pdf) + 1
        lunghezze.append(fine - pos_inizio[k])
    pos = pos_inizio[0] - (1 if sezioni[0]["id"] in bianche_attuali else 0)
    nuove = []
    for s, lun in zip(sezioni, lunghezze):
        if s["recto"] and pos % 2 == 0:
            nuove.append(s["id"])
            pos += 1
        pos += lun
    return nuove


def impagina(cfg: dict, max_passaggi: int = 5) -> tuple[Path, Path, dict]:
    nome = comune.nome_output(cfg)
    f_pagine = comune.OUTPUT / f"{nome}.pagine.json"
    pagine = json.loads(f_pagine.read_text(encoding="utf-8")) if f_pagine.exists() else {}
    for passo in range(1, max_passaggi + 1):
        docx, struttura = build_book.costruisci(cfg, pagine)
        pdf_path = comune.docx_a_pdf(docx)
        with pymupdf.open(pdf_path) as pdf:
            etichette = etichette_pagine(pdf, cfg)
            # il filtro sulla dimensione del carattere esclude le righe dell'indice e le testatine,
            # quindi si può cercare dalla prima pagina
            fisiche = trova_voci(pdf, struttura["voci"], 0)
            fis_xe = trova_xe(pdf, struttura["xe"], fisiche, struttura["voci"])
            bianche = calcola_bianche(pdf, struttura["sezioni"], set(pagine.get("bianche", [])))
            nuove = {
                "bianche": bianche,
                "voci": {vid: etichette[p] for vid, p in fisiche.items()},
                "xe": [etichette[p] if p is not None else "—" for p in fis_xe],
                "pagine_totali": len(pdf),
                "fisiche": fisiche,
            }
        stabile = (nuove["voci"] == pagine.get("voci") and nuove["xe"] == pagine.get("xe")
                   and nuove["bianche"] == pagine.get("bianche", []))
        print(f"  passaggio {passo}: {nuove['pagine_totali']} pagine, indice {'stabile' if stabile else 'aggiornato'}")
        pagine = nuove
        f_pagine.write_text(json.dumps(pagine, ensure_ascii=False, indent=1), encoding="utf-8")
        if stabile:
            break
    else:
        comune.avviso("i numeri di pagina non si sono stabilizzati: controllare l'indice")
    (comune.OUTPUT / f"{nome}.struttura.json").write_text(
        json.dumps(struttura, ensure_ascii=False, indent=1), encoding="utf-8")
    return docx, pdf_path, pagine


def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser(description="Impagina il libro, aggiorna gli indici ed esporta il PDF")
    ap.add_argument("--config", default="book.yaml")
    a = ap.parse_args()
    cfg = comune.carica_config(a.config)
    docx, pdf, pagine = impagina(cfg)
    print(f"✔ {docx.relative_to(comune.RADICE)}  e  {pdf.relative_to(comune.RADICE)}: "
          f"{pagine['pagine_totali']} pagine")


if __name__ == "__main__":
    main()
