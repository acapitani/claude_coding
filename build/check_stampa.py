"""Preflight degli esecutivi di stampa (output/stampa/) e anteprime con le guide.

Uso:  py build/check_stampa.py        (lo esegue anche build/build_stampa.py)

Controlla misure (e, se c'è, il confronto con il template locale in print-template/), dorso,
font incorporati, spazio colore (solo CMYK, OutputIntent Fogra 39, PDF/X), risoluzione delle
immagini, corpo minimo, spessore minimo dei tratti, testo dentro l'area sicura, copertina interna
bianca, assenza di cifratura e di annotazioni. Scrive output/stampa/preflight.txt e le anteprime
PNG in output/stampa/anteprime/ (rifilo, abbondanza, area sicura, pieghe e fasce della colla).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402

MM = 72 / 25.4
STAMPA = comune.OUTPUT / "stampa"
TEMPLATE = comune.RADICE / "print-template" / "print-template.pdf"


class Report:
    def __init__(self):
        self.righe: list[str] = []
        self.errori = 0
        self.avvisi = 0

    def ok(self, msg):
        self.righe.append(f"✔ {msg}")

    def avviso(self, msg):
        self.avvisi += 1
        self.righe.append(f"! {msg}")

    def errore(self, msg):
        self.errori += 1
        self.righe.append(f"✘ {msg}")

    def info(self, msg):
        self.righe.append(f"  {msg}")


def mm(v: float) -> float:
    return round(v / MM, 2)


def uguale(a: float, b: float, tol: float = 0.06) -> bool:
    return abs(a - b) <= tol


# ---------------------------------------------------------------- controlli
def misure(doc, s, info, rep: Report):
    w, h, b, d = s["w"], s["h"], s["b"], info["dorso_mm"]
    cop = (2 * b + 2 * w + d, 2 * b + h)
    pag = (w + 2 * b, h + 2 * b)
    attese = [cop, cop] + [pag] * info["pagine_interno"]
    if len(doc) != len(attese):
        rep.errore(f"pagine nel file unico: {len(doc)}, attese {len(attese)} (2 di copertina + {info['pagine_interno']})")
    sbagliate = [i + 1 for i, (p, (aw, ah)) in enumerate(zip(doc, attese))
                 if not (uguale(mm(p.rect.width), aw) and uguale(mm(p.rect.height), ah))]
    if sbagliate:
        rep.errore(f"misure diverse dall'atteso nelle pagine {sbagliate[:10]}")
    else:
        rep.ok(f"misure: copertina {mm(doc[0].rect.width)} × {mm(doc[0].rect.height)} mm (2 pagine), "
               f"interno {mm(doc[2].rect.width)} × {mm(doc[2].rect.height)} mm × {len(doc) - 2} "
               f"(rifilato {w} × {h} + {b} mm di abbondanza per lato)")
    trim_ok = all(uguale(mm(p.trimbox.width), (attese[i][0] - 2 * b)) for i, p in enumerate(doc))
    (rep.ok if trim_ok else rep.errore)(f"TrimBox e BleedBox impostate ({'coerenti' if trim_ok else 'NON coerenti'} con il rifilato)")


def confronto_template(doc, s, info, rep: Report):
    if not TEMPLATE.exists():
        rep.info("template locale assente (print-template/): confronto pagina per pagina saltato")
        return
    t = pymupdf.open(TEMPLATE)
    tpag = t[1:]                                   # la prima pagina del template sono le istruzioni
    if len(tpag) != len(doc):
        rep.errore(f"il template ha {len(tpag)} pagine (copertina + interno), il nostro file {len(doc)}")
    diverse = [i + 1 for i, (a, b) in enumerate(zip(tpag, doc))
               if not (uguale(mm(a.rect.width), mm(b.rect.width)) and uguale(mm(a.rect.height), mm(b.rect.height)))]
    pieghe = sorted({round(mm(g["rect"].x0), 2) for g in t[1].get_drawings() if g.get("dashes") and "[ 5 5 ]" in g["dashes"]}
                    | {round(mm(g["rect"].x1), 2) for g in t[1].get_drawings() if g.get("dashes") and "[ 5 5 ]" in g["dashes"]})
    dorso_t = round(pieghe[-1] - pieghe[0], 2) if len(pieghe) >= 2 else None
    if diverse:
        rep.errore(f"pagine con misure diverse dal template: {diverse[:10]}")
    else:
        rep.ok(f"confronto con il template: {len(tpag)} pagine, tutte con le stesse misure")
    if dorso_t is not None:
        (rep.ok if uguale(dorso_t, info["dorso_mm"]) else rep.errore)(
            f"dorso: template {dorso_t} mm (pieghe a {pieghe[0]} e {pieghe[-1]} mm), nostro {info['dorso_mm']} mm")


def dorso(s, info, rep: Report):
    n = info["pagine_interno"]
    rep.ok(f"dorso: {n} pagine = {n // 2} fogli × {s['spessore_foglio_mm']} mm = "
           f"{n / 2 * s['spessore_foglio_mm']:.3f} mm → {info['dorso_mm']} mm "
           f"(spessore calibrato sul template: {s['dorso_template_mm']} mm / {s['pagine_preventivo'] // 2} fogli)")
    if info["bianche_finali"]:
        rep.info(f"pagine bianche finali aggiunte per arrivare alle {s['pagine_preventivo']} del preventivo: "
                 f"{info['bianche_finali']}")


def font(doc, rep: Report):
    tutti, non_inc, tipo3 = {}, set(), set()
    for p in doc:
        for xref, ext, tipo, base, *_ in p.get_fonts(full=True):
            tutti[base] = tipo
            if ext in ("n/a", ""):
                non_inc.add(base)
            if tipo == "Type3":
                tipo3.add(base)
    nomi = sorted({re.sub(r"^[A-Z]{6}\+", "", f) for f in tutti})
    if non_inc:
        rep.errore(f"font NON incorporati: {sorted(non_inc)}")
    else:
        rep.ok(f"font: {len(tutti)} sottoinsiemi, tutti incorporati ({', '.join(nomi)})")
    if tipo3:
        rep.avviso(f"font Type 3 (glifi disegnati, non testo vero): {sorted(tipo3)[:6]}")


def colore(doc, rep: Report):
    rgb_obj, rgb_op = 0, 0
    for x in range(1, doc.xref_length()):
        try:
            o = doc.xref_object(x, compressed=False)
        except Exception:
            continue
        if "/DeviceRGB" in o or "/CalRGB" in o:
            rgb_obj += 1
        if doc.xref_is_stream(x) and "/N 3" in o and "/Subtype" not in o and "/Type" not in o:
            rgb_obj += 1                              # profilo ICC RGB
    for p in doc:
        for c in p.get_contents():
            flusso = doc.xref_stream(c) or b""
            rgb_op += len(re.findall(rb"(?<![\w/])(rg|RG)\s", flusso))
    # colore del testo interno: nero e grigi su una sola lastra (DeviceGray); niente scuri in
    # quadricromia. Si segue il colore di riempimento nei flussi (con q/Q) fino a ogni Tj/TJ.
    car = {"grigio, solo K": 0, "CMYK": 0, "CMYK scuro": 0}   # scuro = nero/grigio in quadricromia
    token = re.compile(rb"([\d.]+) g\b|([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+) k\b|\bq\b|\bQ\b|T[jJ]\b")
    interni = set()                                # flussi delle pagine interne (la copertina è disegno)
    for p in doc.pages(2, len(doc)):
        interni.update(p.get_contents())
        interni.update(x[0] for x in p.get_xobjects())
    for x in sorted(interni):
        if "/Subtype /Image" in doc.xref_object(x):
            continue
        try:
            dati = doc.xref_stream(x) or b""
        except Exception:
            continue
        if b"BT" not in dati:
            continue
        pila, colore_corr = [], ("g", 0.0)
        for m in token.finditer(dati):
            t = m.group(0)
            if m.group(1) is not None:
                colore_corr = ("g", float(m.group(1)))
            elif m.group(2) is not None:
                colore_corr = ("k", tuple(float(v) for v in m.group(2, 3, 4, 5)))
            elif t == b"q":
                pila.append(colore_corr)
            elif t == b"Q":
                colore_corr = pila.pop() if pila else colore_corr
            else:
                if colore_corr[0] == "g":
                    car["grigio, solo K"] += 1
                elif (colore_corr[1][3] > 0.5 and sum(colore_corr[1][:3]) > 0.3
                      and max(colore_corr[1][:3]) - min(colore_corr[1][:3]) < 0.15):   # scuro neutro
                    car["CMYK scuro"] += 1
                else:
                    car["CMYK"] += 1
    (rep.ok if car["CMYK scuro"] == 0 else rep.avviso)(
        "colore del testo interno (operazioni di testo): " + ", ".join(f"{k} {v}" for k, v in car.items())
        + ("" if car["CMYK scuro"] == 0 else " — testo scuro in quadricromia: rischio di registro"))
    (rep.ok if rgb_obj == rgb_op == 0 else rep.errore)(
        f"spazio colore: {'solo CMYK/grigio' if rgb_obj == rgb_op == 0 else f'{rgb_obj} oggetti e {rgb_op} operatori RGB'}")
    cat = doc.pdf_catalog()
    oi = doc.xref_get_key(cat, "OutputIntents")
    testo_oi = doc.xref_object(cat) + "".join(doc.xref_object(int(n)) for n in re.findall(r"(\d+) 0 R", oi[1]))
    (rep.ok if "FOGRA39" in testo_oi else rep.errore)(
        f"OutputIntent: {'FOGRA39 (Coated_Fogra39L_VIGC_300)' if 'FOGRA39' in testo_oi else 'assente'}")
    pdfx = doc.metadata.get("format", "")
    trailer = doc.pdf_trailer()
    info_x = re.search(r"/Info (\d+) 0 R", trailer)
    versione = ""
    if info_x:
        m = re.search(r"/GTS_PDFXVersion\s*\(([^)]*)\)", doc.xref_object(int(info_x.group(1))))
        versione = m.group(1) if m else ""
    (rep.ok if versione else rep.avviso)(f"standard: {versione or 'nessuna dichiarazione PDF/X'} ({pdfx})")


def immagini(doc, s, rep: Report):
    sotto = []
    for i, p in enumerate(doc):
        for img in p.get_images(full=True):
            xref, w = img[0], img[2]
            for r in p.get_image_rects(xref):
                if r.width < 2 * MM:                  # fili e sfumature minuscole
                    continue
                dpi = w / (r.width / 72)
                if dpi < s["risoluzione_min_dpi"] - 1:
                    sotto.append((i + 1, round(dpi), mm(r.width)))
    if sotto:
        rep.avviso(f"immagini sotto {s['risoluzione_min_dpi']} dpi effettivi: {len(sotto)} — "
                   + "; ".join(f"p. {p}: {d} dpi su {lw} mm" for p, d, lw in sotto[:8]))
    else:
        rep.ok(f"immagini: tutte ≥ {s['risoluzione_min_dpi']} dpi effettivi")


def testo_e_tratti(doc, s, rep: Report):
    b, area = s["abbondanza_mm"], s["area_sicura_mm"]
    minimo, dove = 99.0, None
    fuori, vicino_interno, vicino_esterno = [], 0, 0
    sottili = 0
    for i, p in enumerate(doc):
        t = p.trimbox
        sic = pymupdf.Rect(t.x0 + area * MM, t.y0 + area * MM, t.x1 - area * MM, t.y1 - area * MM)
        interna = i >= 2
        for blk in p.get_text("dict")["blocks"]:
            for ln in blk.get("lines", []):
                for sp in ln["spans"]:
                    if not sp["text"].strip():
                        continue
                    if sp["size"] < minimo:
                        minimo, dove = sp["size"], (i + 1, sp["text"][:20])
                    bb = pymupdf.Rect(sp["bbox"])
                    if not sic.contains(bb):
                        fuori.append((i + 1, sp["text"][:20]))
                    if interna:
                        # pagina interna n (da 1): dispari = destra, il lato interno è a sinistra
                        destra = (i - 2) % 2 == 0
                        da_interno = (bb.x0 - t.x0) if destra else (t.x1 - bb.x1)
                        da_esterno = (t.x1 - bb.x1) if destra else (bb.x0 - t.x0)
                        if da_interno < s["testi_consigliati_mm"]["interno"] * MM - 0.1:
                            vicino_interno += 1
                        if min(da_esterno, bb.y0 - t.y0, t.y1 - bb.y1) < s["testi_consigliati_mm"]["esterno"] * MM - 0.1:
                            vicino_esterno += 1
        for g in p.get_drawings():
            if g.get("type") in ("s", "fs") and g.get("width") and g["width"] < s["tratto_minimo_pt"] - 0.005:
                sottili += 1
    (rep.ok if minimo >= s["corpo_minimo_pt"] else rep.errore)(
        f"corpo minimo: {minimo:.2f} pt (p. {dove[0]}, «{dove[1]}»; soglia {s['corpo_minimo_pt']} pt)")
    (rep.ok if not fuori else rep.errore)(
        f"testo nell'area sicura ({area} mm dal taglio): "
        + ("tutto dentro" if not fuori else f"{len(fuori)} righe fuori, es. {fuori[:4]}"))
    (rep.ok if not vicino_interno and not vicino_esterno else rep.avviso)(
        f"margini consigliati (testi a {s['testi_consigliati_mm']['interno']} mm dal lato interno, "
        f"{s['testi_consigliati_mm']['esterno']} mm dagli altri): "
        + ("rispettati" if not vicino_interno and not vicino_esterno
           else f"{vicino_interno} righe più vicine al lato interno, {vicino_esterno} agli altri lati"))
    (rep.ok if not sottili else rep.avviso)(
        f"tratti: {'nessuno' if not sottili else sottili} sotto {s['tratto_minimo_pt']} pt")


def copertina_interna(doc, rep: Report):
    p = doc[1]
    vuota = not p.get_text().strip() and not p.get_images() and not p.get_drawings()
    (rep.ok if vuota else rep.errore)(
        "copertina interna: bianca (dorso e fasce per la colla liberi)" if vuota
        else "copertina interna NON bianca: dorso e fasce per la colla devono restare liberi")


def sicurezza(doc, rep: Report):
    annot = sum(len(list(p.annots())) for p in doc)
    (rep.ok if not doc.is_encrypted and not doc.needs_pass else rep.errore)("nessuna password né cifratura")
    (rep.ok if not annot else rep.avviso)(f"annotazioni e crocini: {annot or 'nessuno'}")


# ---------------------------------------------------------------- anteprime
def guide(img: Image.Image, dpi: int, larghezza_mm: float, altezza_mm: float, s, pieghe: list[float] = ()):
    k = dpi / 25.4
    d = ImageDraw.Draw(img)
    b, area = s["abbondanza_mm"], s["area_sicura_mm"]
    rett = lambda m, col, larg=2: d.rectangle([m * k, m * k, (larghezza_mm - m) * k, (altezza_mm - m) * k], outline=col, width=larg)
    rett(0.3, (0, 166, 80))                        # abbondanza (verde, come nel template)
    rett(b, (236, 0, 140))                         # taglio (magenta)
    rett(b + area, (237, 28, 36), 1)               # area sicura (rosso)
    for x in pieghe:                               # pieghe del dorso (tratteggio rosso)
        for y in range(0, int(altezza_mm * k), 12):
            d.line([x * k, y, x * k, y + 6], fill=(237, 28, 36), width=2)
    return img


def anteprime(s, info, rep: Report):
    dest = STAMPA / "anteprime"
    dest.mkdir(exist_ok=True)
    for vecchio in dest.glob("*.png"):
        vecchio.unlink()
    doc = pymupdf.open(STAMPA / "claude-coding-stampa.pdf")
    w, b, d = s["w"], s["b"], info["dorso_mm"]
    pieghe = [b + w, b + w + d]
    dpi = 110
    pix = doc[0].get_pixmap(dpi=dpi, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(dest / "copertina.png")
    guide(img.copy(), dpi, mm(doc[0].rect.width), mm(doc[0].rect.height), s, pieghe).save(dest / "copertina-guide.png")

    # pagine interne significative (numeri dell'interno, da 1)
    def cerca(testo):
        for i in range(2, len(doc)):
            if testo in doc[i].get_text():
                return i - 1
        return None
    foto = max(range(2, 40), key=lambda i: sum(r.width * r.height for x in doc[i].get_images()
                                                for r in doc[i].get_image_rects(x[0])))
    scelte = {"frontespizio": 1, "apertura-cap06": cerca("La prima sessione\nDevo"),
              "terminale-fig6-1": cerca("Figura 6.1"), "foto-cap01": foto - 1,
              "ultima-bianca": len(doc) - 2}
    for nome, n in scelte.items():
        if not n:
            continue
        p = doc[n + 1]
        pix = p.get_pixmap(dpi=dpi, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        guide(img, dpi, mm(p.rect.width), mm(p.rect.height), s).save(dest / f"interno-{n:03d}-{nome}.png")
    rep.info(f"anteprime in {dest.relative_to(comune.RADICE)}: copertina (con e senza guide), "
             f"pagine interne {sorted(n for n in scelte.values() if n)}")


# ---------------------------------------------------------------- principale
def controlla(cfg: dict | None = None) -> bool:
    cfg = cfg or comune.carica_config("book.yaml")
    from build_stampa import parametri
    s = parametri(cfg)
    info = json.loads((STAMPA / "stampa.json").read_text(encoding="utf-8"))
    rep = Report()
    rep.righe.append(f"Preflight di {(STAMPA / 'claude-coding-stampa.pdf').relative_to(comune.RADICE)}"
                     f" — {s['stampatore']}, {s['prodotto']}, A5\n")
    doc = pymupdf.open(STAMPA / "claude-coding-stampa.pdf")
    misure(doc, s, info, rep)
    confronto_template(doc, s, info, rep)
    dorso(s, info, rep)
    font(doc, rep)
    colore(doc, rep)
    immagini(doc, s, rep)
    testo_e_tratti(doc, s, rep)
    copertina_interna(doc, rep)
    sicurezza(doc, rep)
    for nome in ("copertina.pdf", "interno.pdf"):
        f = STAMPA / nome
        rep.info(f"{nome}: {len(pymupdf.open(f))} pagine, {f.stat().st_size // 1024} KB (alternativa a due file)")
    rep.info(f"retro: versione «{info['retro']}»")
    anteprime(s, info, rep)
    rep.righe.append(f"\n{'OK' if not rep.errori else 'ERRORI'}: {rep.errori} errori, {rep.avvisi} avvisi")
    testo = "\n".join(rep.righe)
    (STAMPA / "preflight.txt").write_text(testo + "\n", encoding="utf-8")
    print(testo)
    return rep.errori == 0


if __name__ == "__main__":
    comune.utf8_console()
    sys.exit(0 if controlla() else 1)
