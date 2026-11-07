"""Produce gli esecutivi di stampa per Pixartprinting in output/stampa/.

Uso (dalla radice del progetto):
    py build/build_stampa.py                     # impagina la variante di stampa e genera tutto
    py build/build_stampa.py --salta-impaginazione   # riusa output/claude-coding-stampa.pdf
    py build/build_stampa.py --retro 1           # usa un'altra versione del retro (retro.json)

Passi:
 1. variante «stampa» del libro (book.yaml → varianti.stampa): nero puro, testatina più grande;
 2. interno A5: le pagine dal frontespizio in poi, ridotte da 17 × 24 a 14,8 × 21 cm
    (vettoriale, font intatti) su pagine con 3 mm di abbondanza, più le bianche fino alle
    pagine del preventivo;
 3. copertina distesa (assets/copertina/cover-stampa.html → PDF vettoriale con Playwright),
    dorso calcolato dal numero di pagine, più la copertina interna bianca (brossura fresata);
 4. conversione in CMYK Fogra 39 con Ghostscript (PDF/X-4); nero e grigi neutri dell'interno
    passano prima da RGB a grigio, così vanno sulla sola lastra del nero;
 5. preflight (build/check_stampa.py) e anteprime.

Uscite: output/stampa/claude-coding-stampa.pdf (file unico nell'ordine del template: copertina
esterna, copertina interna, interno — è quello da caricare), copertina.pdf e interno.pdf
(alternativa a due file), preflight.txt, anteprime/.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402

MM = 72 / 25.4                      # punti PDF per millimetro
STAMPA = comune.OUTPUT / "stampa"
TMP = STAMPA / "tmp"
LARGHEZZA_DIGITALE_MM = 170         # il libro digitale è 17 × 24 cm
ALTEZZA_DIGITALE_MM = 240


# ---------------------------------------------------------------- parametri
def parametri(cfg: dict) -> dict:
    s = dict(cfg["stampa"])
    s["w"], s["h"] = s["rifilato_mm"]
    s["b"] = s["abbondanza_mm"]
    s["scala"] = s["w"] / LARGHEZZA_DIGITALE_MM
    return s


def dorso_mm(pagine: int, s: dict) -> float:
    """Spessore del dorso: fogli × spessore del foglio (calibrato sul template del preventivo)."""
    return round(pagine / 2 * s["spessore_foglio_mm"], 1)


# ---------------------------------------------------------------- 1. variante di stampa
def impagina_variante() -> Path:
    import update_indexes
    cfg = comune.carica_config("book.yaml", "stampa")
    _, pdf, pagine = update_indexes.impagina(cfg)
    print(f"✔ variante di stampa: {pdf.relative_to(comune.RADICE)} ({pagine['pagine_totali']} pagine)")
    return pdf


# ---------------------------------------------------------------- 2. interno A5
COLORE_RGB = re.compile(rb"(?<![\d.])([\d.]+) ([\d.]+) ([\d.]+) (rg|RG)(?=\s)")


def grigi_in_k(doc: pymupdf.Document) -> int:
    """LibreOffice scrive il nero e i grigi in RGB («0 0 0 rg»): convertiti con il profilo ICC
    diventerebbero quadricromia, a rischio di registro sul testo piccolo. Il nero puro e i grigi
    neutri di tono medio (testatine, didascalie, filetti) si riscrivono come grigio («g»), che
    Ghostscript lascia in DeviceGray: in stampa vanno sulla sola lastra del nero. Restano a colori
    i fondi scuri (#1F1E1D dei terminali: meglio un nero ricco sulle grandi aree) e i colori chiari."""
    def sostituisci(m):
        r, g, b = (float(x) for x in m.group(1, 2, 3))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        neutro = max(r, g, b) - min(r, g, b) <= 0.05
        if (r == g == b == 0) or (neutro and 0.2 <= lum <= 0.85):
            op = b"g" if m.group(4) == b"rg" else b"G"
            return b"%.4f " % lum + op if lum else b"0 " + op
        return m.group(0)

    n = 0
    for xref in range(1, doc.xref_length()):
        if not doc.xref_is_stream(xref) or "/Subtype /Image" in doc.xref_object(xref):
            continue
        try:
            dati = doc.xref_stream(xref)
        except Exception:
            continue
        if not dati or (b" rg" not in dati and b" RG" not in dati):
            continue
        nuovi = COLORE_RGB.sub(sostituisci, dati)
        if nuovi != dati:
            n += len(COLORE_RGB.findall(dati)) - len(COLORE_RGB.findall(nuovi))
            doc.update_stream(xref, nuovi)
    return n


def interno_a5(sorgente: Path, s: dict) -> tuple[Path, int, int]:
    src = pymupdf.open(sorgente)
    neri = grigi_in_k(src)
    w, h, b = s["w"], s["h"], s["b"]
    W, H = (w + 2 * b) * MM, (h + 2 * b) * MM
    alto = ALTEZZA_DIGITALE_MM * s["scala"]                 # 208,9 mm: si centra nel rifilo di 210
    dest = pymupdf.Rect(b * MM, (b + (h - alto) / 2) * MM, (b + w) * MM, (b + (h + alto) / 2) * MM)
    out = pymupdf.open()
    for i in range(s["prima_pagina_pdf"] - 1, len(src)):
        p = out.new_page(width=W, height=H)
        p.show_pdf_page(dest, src, i)
    contenuto = len(out)
    while len(out) < s["pagine_preventivo"]:
        out.new_page(width=W, height=H)
    bianche = len(out) - contenuto
    if len(out) > s["pagine_preventivo"]:
        comune.avviso(f"l'interno ha {len(out)} pagine, il preventivo {s['pagine_preventivo']}: "
                      "rifare il preventivo e scaricare il nuovo template")
    if len(out) % 2:
        out.new_page(width=W, height=H)
    rifilo = pymupdf.Rect(b * MM, b * MM, (b + w) * MM, (b + h) * MM)
    for p in out:
        p.set_trimbox(rifilo)
        p.set_bleedbox(p.rect)
    f = TMP / "interno-rgb.pdf"
    out.save(f, garbage=3, deflate=True)
    print(f"✔ interno A5: {contenuto} pagine dal PDF 17×24 (dalla {s['prima_pagina_pdf']}ª) "
          f"+ {bianche} bianche = {len(out)} pagine, riduzione {s['scala']:.4f}")
    print(f"✔ nero e grigi neutri → solo K: {neri} impostazioni di colore riscritte da RGB a grigio")
    return f, len(out), bianche


# ---------------------------------------------------------------- 3. copertina
def testo_retro(s: dict, scelta: int | None) -> dict:
    r = json.loads((comune.RADICE / s["retro"]).read_text(encoding="utf-8"))
    v = r["versioni"][r["scelta"] if scelta is None else scelta]
    return {"titolo": v["titolo"], "paragrafi": v["paragrafi"], "nome": v["nome"]}


def copertina(s: dict, dorso: float, retro: dict, uscita: Path) -> Path:
    w, h, b = s["w"], s["h"], s["b"]
    largo, alto = 2 * b + 2 * w + dorso, 2 * b + h
    query = urllib.parse.urlencode({
        "w": w, "h": h, "b": b, "dorso": dorso,
        "retro": json.dumps({"titolo": retro["titolo"], "paragrafi": retro["paragrafi"]}, ensure_ascii=False),
    })
    grezzo = TMP / "copertina-chromium.pdf"
    r = subprocess.run(["node", str(comune.RADICE / "build" / "figure" / "render.mjs"),
                        str(comune.RADICE / s["copertina"]), str(grezzo),
                        "--larghezza-cm", f"{largo / 10:.3f}", "--altezza-cm", f"{alto / 10:.3f}",
                        "--query", query],
                       capture_output=True, text=True, encoding="utf-8", cwd=comune.RADICE / "build")
    if r.returncode != 0:
        raise RuntimeError(f"render della copertina fallito:\n{r.stdout}\n{r.stderr}")
    doc = pymupdf.open(grezzo)
    if len(doc) > 1:
        doc.delete_pages(range(1, len(doc)))
    p = doc[0]
    # Chromium arrotonda la pagina al pixel: si riporta la MediaBox alla misura esatta,
    # tenendo l'angolo in alto a sinistra (le coordinate della MediaBox partono dal basso)
    H0 = p.mediabox.height
    p.set_mediabox(pymupdf.Rect(0, H0 - alto * MM, largo * MM, H0))
    p.set_trimbox(pymupdf.Rect(b * MM, b * MM, (largo - b) * MM, (alto - b) * MM))
    p.set_bleedbox(p.rect)
    # copertina interna: bianca (brossura fresata: niente stampa sulla 2ª e 3ª di copertina,
    # dorso e fasce per la colla restano comunque bianchi)
    q = doc.new_page(width=largo * MM, height=alto * MM)
    q.set_trimbox(pymupdf.Rect(b * MM, b * MM, (largo - b) * MM, (alto - b) * MM))
    q.set_bleedbox(q.rect)
    doc.save(uscita, garbage=3, deflate=True)
    return uscita


# ---------------------------------------------------------------- 4. CMYK (Ghostscript)
def pdfx_def(s: dict) -> Path:
    icc = (comune.RADICE / s["profilo_icc"]).as_posix()
    titolo = "<" + ("﻿" + "/claude ✻ Coding").encode("utf-16-be").hex().upper() + ">"
    testo = f"""%!PS
% Generato da build/build_stampa.py: OutputIntent Fogra 39 per PDF/X-4 (da lib/PDFX_def.ps di Ghostscript)
[ /GTS_PDFXVersion (PDF/X-4) /Title {titolo} /Trapped /False /DOCINFO pdfmark
/ICCProfile ({icc}) def
[/_objdef {{icc_PDFX}} /type /stream /OBJ pdfmark
[{{icc_PDFX}} << /N 4 >> /PUT pdfmark
[{{icc_PDFX}} ICCProfile (r) file /PUT pdfmark
[/_objdef {{OutputIntent_PDFX}} /type /dict /OBJ pdfmark
[{{OutputIntent_PDFX}} <<
  /Type /OutputIntent /S /GTS_PDFX
  /OutputCondition (Offset commercial printing, coated paper, FOGRA39)
  /Info (Coated_Fogra39L_VIGC_300)
  /OutputConditionIdentifier (FOGRA39)
  /RegistryName (http://www.color.org)
  /DestOutputProfile {{icc_PDFX}}
>> /PUT pdfmark
[{{Catalog}} <</OutputIntents [ {{OutputIntent_PDFX}} ]>> /PUT pdfmark
"""
    f = TMP / "PDFX_def.ps"
    f.write_text(testo, encoding="ascii")
    return f


def in_cmyk(ingresso: Path, uscita: Path, s: dict) -> Path:
    icc = comune.RADICE / s["profilo_icc"]
    if not icc.exists():
        raise SystemExit(f"manca il profilo colore {icc} (vedi README, «Edizione a stampa»)")
    if not comune.GS.exists():
        raise SystemExit(f"manca Ghostscript in {comune.GS} (vedi README)")
    defs = pdfx_def(s)
    cmd = [str(comune.GS), "-dBATCH", "-dNOPAUSE", "-dQUIET", "-dSAFER",
           f"--permit-file-read={icc.as_posix()}",
           "-sDEVICE=pdfwrite", "-dPDFX=4", "-dPDFSETTINGS=/prepress", "-dCompatibilityLevel=1.6",
           "-sColorConversionStrategy=CMYK", "-sProcessColorModel=DeviceCMYK",
           f"-sOutputICCProfile={icc.as_posix()}", "-dRenderIntent=1",
           "-dEmbedAllFonts=true", "-dSubsetFonts=true",
           "-dAutoRotatePages=/None", "-dDownsampleColorImages=false",
           "-dDownsampleGrayImages=false", "-dDownsampleMonoImages=false",
           "-dUseTrimBox=false",
           f"-sOutputFile={uscita}", str(defs), str(ingresso)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not uscita.exists():
        raise RuntimeError(f"Ghostscript non è riuscito a convertire {ingresso.name}:\n{r.stdout}\n{r.stderr}")
    # Ghostscript conserva TrimBox e BleedBox (il preflight le ricontrolla); si sistemano i metadati
    out = pymupdf.open(uscita)
    out.set_metadata({**out.metadata, "title": "/claude ✻ Coding", "author": "Claude Code",
                      "subject": "Esecutivo di stampa (Pixartprinting)"})
    out.save(uscita, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    return uscita


# ---------------------------------------------------------------- principale
def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser(description="Esecutivi di stampa per Pixartprinting")
    ap.add_argument("--salta-impaginazione", action="store_true",
                    help="riusa output/claude-coding-stampa.pdf senza rifare l'impaginazione")
    ap.add_argument("--retro", type=int, help="indice della versione del retro (predefinito: `scelta` in retro.json)")
    ap.add_argument("--senza-preflight", action="store_true")
    a = ap.parse_args()

    cfg = comune.carica_config("book.yaml")
    s = parametri(cfg)
    TMP.mkdir(parents=True, exist_ok=True)

    variante = comune.OUTPUT / "claude-coding-stampa.pdf"
    if not a.salta_impaginazione or not variante.exists():
        variante = impagina_variante()

    interno, n_pagine, bianche = interno_a5(variante, s)
    dorso = dorso_mm(n_pagine, s)
    print(f"✔ dorso: {n_pagine} pagine = {n_pagine // 2} fogli × {s['spessore_foglio_mm']} mm "
          f"= {n_pagine / 2 * s['spessore_foglio_mm']:.3f} → {dorso} mm "
          f"(template del preventivo: {s['dorso_template_mm']} mm)")
    if abs(dorso - s["dorso_template_mm"]) > 0.05:
        comune.avviso("il dorso non coincide con il template: rifare il preventivo e scaricare il nuovo template")

    retro = testo_retro(s, a.retro)
    cop = copertina(s, dorso, retro, TMP / "copertina-rgb.pdf")
    print(f"✔ copertina distesa: retro «{retro['nome']}», dorso {dorso} mm")

    unico = pymupdf.open(cop)
    unico.insert_pdf(pymupdf.open(interno))
    f_unico = TMP / "unico-rgb.pdf"
    unico.save(f_unico, garbage=3, deflate=True)

    risultati = {}
    for nome, sorgente in (("claude-coding-stampa.pdf", f_unico), ("copertina.pdf", cop), ("interno.pdf", interno)):
        risultati[nome] = in_cmyk(sorgente, STAMPA / nome, s)
        print(f"✔ CMYK Fogra 39 (PDF/X-4): {risultati[nome].relative_to(comune.RADICE)}")

    info = {"pagine_interno": n_pagine, "bianche_finali": bianche, "dorso_mm": dorso,
            "retro": retro["nome"], "variante": str(variante.relative_to(comune.RADICE))}
    (STAMPA / "stampa.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")

    ok = True
    if not a.senza_preflight:
        import check_stampa
        ok = check_stampa.controlla(cfg)
    anteprime_retro(s, dorso)
    sys.exit(0 if ok else 1)


def anteprime_retro(s: dict, dorso: float) -> None:
    """Una copertina (RGB, solo anteprima) per ogni versione del retro, per scegliere quella da usare."""
    dest = STAMPA / "anteprime" / "retro"
    dest.mkdir(parents=True, exist_ok=True)
    versioni = json.loads((comune.RADICE / s["retro"]).read_text(encoding="utf-8"))["versioni"]
    for i, v in enumerate(versioni):
        f = copertina(s, dorso, {"titolo": v["titolo"], "paragrafi": v["paragrafi"], "nome": v["nome"]},
                      TMP / f"retro-{i}.pdf")
        p = pymupdf.open(f)[0]
        clip = pymupdf.Rect(0, 0, (s["b"] + s["w"]) * MM, p.rect.height)   # solo la 4ª di copertina
        nome = v["nome"].split(" — ")[0]
        p.get_pixmap(dpi=130, clip=clip, alpha=False).save(dest / f"retro-{i}-{nome}.png")
    print(f"✔ anteprime del retro: {len(versioni)} versioni in {dest.relative_to(comune.RADICE)}")


if __name__ == "__main__":
    main()
