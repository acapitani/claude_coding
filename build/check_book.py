"""Controlli di qualità sul libro impaginato (PLAN.md §11). Da lanciare dopo update_indexes.py.

Uso:
    py build/check_book.py                      # controlli; l'intervallo di pagine è solo informativo
    py build/check_book.py --finale             # l'intervallo 160–200 diventa un errore bloccante
    py build/check_book.py --config book-prova.yaml

Scrive il resoconto anche in output/<nome>.report.txt. Esce con codice 1 se ci sono errori.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pymupdf
from docx import Document

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402

MAX_CAR_CODICE = 68   # oltre, la riga va a capo nel blocco di codice (Consolas 8,5 pt su 13 cm)
SEGNAPOSTO = re.compile(r"\b(TODO|TBD|FIXME|XXX)\b|\[FIGURA MANCANTE|\?\?\?")


def parole_markdown(testo: str) -> int:
    testo = re.sub(r"```.*?```", " ", testo, flags=re.S)          # blocchi di codice
    testo = re.sub(r"<!--.*?-->", " ", testo, flags=re.S)         # commenti
    testo = re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?", " ", testo)  # immagini (la didascalia conta poco)
    testo = re.sub(r"\{[^}]*\}", " ", testo)                      # attributi
    testo = re.sub(r"^:::.*$", " ", testo, flags=re.M)
    return len(re.findall(r"[\wÀ-ÿ’']+", testo))


def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="book.yaml")
    ap.add_argument("--finale", action="store_true")
    a = ap.parse_args()
    cfg = comune.carica_config(a.config)
    nome = comune.nome_output(cfg)
    errori, avvisi, info = [], [], []

    f_docx, f_pdf = comune.OUTPUT / f"{nome}.docx", comune.OUTPUT / f"{nome}.pdf"
    f_str, f_pag = comune.OUTPUT / f"{nome}.struttura.json", comune.OUTPUT / f"{nome}.pagine.json"
    for f in (f_docx, f_pdf, f_str, f_pag):
        if not f.exists():
            print(f"✘ manca {f.relative_to(comune.RADICE)}: lanciare prima update_indexes.py")
            sys.exit(1)
    struttura = json.loads(f_str.read_text(encoding="utf-8"))
    pagine = json.loads(f_pag.read_text(encoding="utf-8"))

    # 1. numero di pagine
    pdf = pymupdf.open(f_pdf)
    n = len(pdf)
    pmin, pmax = cfg["pagina"]["pagine_min"], cfg["pagina"]["pagine_max"]
    msg = f"pagine nel PDF: {n} (intervallo richiesto {pmin}–{pmax}, obiettivo {cfg['pagina'].get('pagine_obiettivo', '—')})"
    if pmin <= n <= pmax:
        info.append("✔ " + msg)
    elif a.finale:
        errori.append(msg)
    else:
        info.append("· " + msg + " — libro incompleto, verifica non bloccante")
    w = pdf[0].rect.width / 72 * 2.54
    h = pdf[0].rect.height / 72 * 2.54
    if abs(w - cfg["pagina"]["larghezza_cm"]) > 0.1 or abs(h - cfg["pagina"]["altezza_cm"]) > 0.1:
        errori.append(f"formato pagina {w:.1f}×{h:.1f} cm diverso da quello richiesto")

    # 2. metadati
    cp = Document(f_docx).core_properties
    if cp.author != cfg["metadati"]["autore"]:
        errori.append(f"autore nei metadati = {cp.author!r}")
    else:
        info.append(f"✔ autore nei metadati: {cp.author}")
    if cp.language != cfg["metadati"].get("lingua", "it-IT"):
        avvisi.append(f"lingua nei metadati = {cp.language!r}")

    # 3. figure e crediti
    crediti = (comune.RADICE / "assets" / "CREDITI.md").read_text(encoding="utf-8")
    for f in struttura["figure"]:
        if not (comune.RADICE / f["src"]).exists():
            errori.append(f"figura {f['numero']} mancante: {f['src']}")
        elif f"| {f['src']} |" not in crediti:
            errori.append(f"figura {f['numero']} senza voce in assets/CREDITI.md: {f['src']}")
    info.append(f"✔ figure: {len(struttura['figure'])}")

    # 4. fatti
    fatti = (comune.RADICE / "research" / "FATTI.md").read_text(encoding="utf-8")
    noti = set(re.findall(r"^\| (F-\d{3}) \|", fatti, flags=re.M))
    for m in struttura.get("fatti", []):
        if m not in noti:
            errori.append(f"rimando {m} assente da research/FATTI.md")
        elif re.search(rf"^\| {m} \|.*\| B \|", fatti, flags=re.M):
            avvisi.append(f"rimando {m}: fatto con affidabilità B")
    info.append(f"✔ rimandi ai fatti: {len(struttura.get('fatti', []))}")

    # 5. sorgenti: segnaposto, righe di codice lunghe, parole
    capitoli = [v for v in struttura["voci"] if v["livello"] in (1, 3)]
    fis = pagine.get("fisiche", {})
    righe_tab = []
    tot_parole = tot_pagine = 0
    for k, v in enumerate(capitoli):
        if not v.get("file"):
            continue
        testo = (comune.RADICE / v["file"]).read_text(encoding="utf-8")
        for i, riga in enumerate(testo.splitlines(), 1):
            if SEGNAPOSTO.search(riga):
                errori.append(f"{v['file']}:{i}: segnaposto o TODO")
        for blocco in re.findall(r"```[^\n]*\n(.*?)```", testo, flags=re.S):
            for riga in blocco.splitlines():
                if len(riga) > MAX_CAR_CODICE:
                    avvisi.append(f"{v['file']}: riga di codice di {len(riga)} caratteri (max {MAX_CAR_CODICE}): {riga[:40]}…")
        parole = parole_markdown(testo)
        inizio = fis.get(v["id"])
        succ = next((fis.get(c["id"]) for c in capitoli[k + 1:] if fis.get(c["id"]) is not None), n)
        npag = (succ - inizio) if inizio is not None else None
        righe_tab.append((v["etichetta"] or "", v["testo"][:38], parole, npag,
                          round(parole / npag) if npag else None))
        tot_parole += parole
        tot_pagine += npag or 0

    # resoconto
    out = [f"Controllo di {f_pdf.relative_to(comune.RADICE)}", ""]
    out += info
    out += ["", f"{'cap.':>11}  {'titolo':38}  {'parole':>7}  {'pagine':>6}  {'parole/p':>8}"]
    for et, tit, par, pg, pp in righe_tab:
        out.append(f"{et:>11}  {tit:38}  {par:>7}  {pg if pg is not None else '?':>6}  {pp if pp else '—':>8}")
    if tot_pagine:
        out.append(f"{'':>11}  {'TOTALE capitoli':38}  {tot_parole:>7}  {tot_pagine:>6}  {round(tot_parole / tot_pagine):>8}")
    out.append("")
    out += [f"! {x}" for x in avvisi]
    out += [f"✘ {x}" for x in errori]
    out.append("")
    out.append("ESITO: " + ("✘ ERRORI" if errori else ("✔ OK con avvisi" if avvisi else "✔ OK")))
    testo = "\n".join(out)
    print(testo)
    (comune.OUTPUT / f"{nome}.report.txt").write_text(testo, encoding="utf-8")
    sys.exit(1 if errori else 0)


if __name__ == "__main__":
    main()
