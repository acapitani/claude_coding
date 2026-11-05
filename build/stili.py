"""Stili Word e utilità di formattazione per il libro (PLAN.md §7.3)."""
from __future__ import annotations

from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# --- Palette -----------------------------------------------------------------
ACCENTO = RGBColor(0xD7, 0x77, 0x57)      # arancio "Claude" della console (#D77757)
ACCENTO_HEX = "D77757"
INCHIOSTRO = RGBColor(0x1F, 0x1E, 0x1D)
GRIGIO = RGBColor(0x6B, 0x66, 0x60)
GRIGIO_CHIARO = RGBColor(0x9A, 0x94, 0x8C)
CREMA = RGBColor(0xF0, 0xEE, 0xE6)
FONDO_CODICE = "F4F1EA"
FONDO_TERMINALE = "1F1E1D"
FONDO_BOX = {"nota": "EEF1F4", "consiglio": "FBF0EB", "attenzione": "FBEFEF"}
BORDO_BOX = {"nota": "6A8CAF", "consiglio": ACCENTO_HEX, "attenzione": "B54A4A"}
ICONA_BOX = {"nota": "✎", "consiglio": "✻", "attenzione": "⚠"}
TITOLO_BOX = {"nota": "Nota", "consiglio": "Consiglio", "attenzione": "Attenzione"}

# --- Font (vedi research/note/font.md) ---------------------------------------
FONT_CORPO = "Cambria"
FONT_TITOLI = "Calibri"
FONT_CODICE = "Consolas"
FONT_SIMBOLI = "Segoe UI Symbol"        # ha ✻ ✢ ✳ ✶ ✽ ⚠ ✎ ✔ ✘ ❯
FONT_SIMBOLI_MONO = "DejaVu Sans Mono"  # idem, a spaziatura fissa
# Caratteri assenti in Cambria/Calibri/Consolas: vanno in un run con font dei simboli.
GLIFI_SPECIALI = set("✢✳✶✻✽∗⚠✎✔✘❯")

LARGHEZZA_TESTO_CM = 13.0
LINGUA = "it-IT"


# --- Utilità XML ---------------------------------------------------------------
# Word esige che i figli di pPr/rPr/tcPr/tblPr/sectPr rispettino l'ordine dello schema OOXML.
ORDINE = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr",
            "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
            "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
            "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
            "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
            "sectPr", "pPrChange"],
    "rPr": ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike", "outline",
            "shadow", "emboss", "imprint", "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing",
            "w", "kern", "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd", "fitText",
            "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar",
             "textDirection", "tcFitText", "vAlign", "hideMark"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize", "tblStyleColBandSize",
              "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook"],
    "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore", "wAfter", "cantSplit", "trHeight",
             "tblHeader", "tblCellSpacing", "jc", "hidden"],
    "sectPr": ["headerReference", "footerReference", "footnotePr", "endnotePr", "type", "pgSz", "pgMar",
               "paperSrc", "pgBorders", "lnNumType", "pgNumType", "cols", "formProt", "vAlign", "noEndnote",
               "titlePg", "textDirection", "bidi", "rtlGutter", "docGrid", "printerSettings", "sectPrChange"],
}


def inserisci(genitore, elemento, sostituisci: bool = True):
    """Inserisce `elemento` in `genitore` rispettando l'ordine dello schema; se `sostituisci`,
    rimuove prima un eventuale figlio con lo stesso tag."""
    nome_gen = genitore.tag.split("}")[1]
    nome_el = elemento.tag.split("}")[1]
    ordine = ORDINE[nome_gen]
    if sostituisci:
        for vecchio in genitore.findall(elemento.tag):
            genitore.remove(vecchio)
    dopo = set(ordine[ordine.index(nome_el) + 1:])
    for figlio in genitore:
        if figlio.tag.split("}")[1] in dopo:
            figlio.addprevious(elemento)
            return elemento
    genitore.append(elemento)
    return elemento


def elemento(tag: str, **attrs):
    el = OxmlElement(tag)
    for k, v in attrs.items():
        el.set(qn(k), str(v))
    return el


def imposta_font(rpr_owner, nome: str) -> None:
    """Imposta il font su tutte e quattro le classi di caratteri (ascii, hAnsi, cs, eastAsia)."""
    rpr = rpr_owner.get_or_add_rPr() if hasattr(rpr_owner, "get_or_add_rPr") else rpr_owner
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = inserisci(rpr, OxmlElement("w:rFonts"))
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), nome)


def no_sillabazione(stile) -> None:
    inserisci(stile.element.get_or_add_pPr(), elemento("w:suppressAutoHyphens"))


def font_stile(stile, nome: str, size: float | None = None, colore: RGBColor | None = None,
               bold: bool | None = None, italic: bool | None = None) -> None:
    stile.font.name = nome
    imposta_font(stile.element.get_or_add_rPr(), nome)
    if size:
        stile.font.size = Pt(size)
    if colore is not None:
        stile.font.color.rgb = colore
    if bold is not None:
        stile.font.bold = bold
    if italic is not None:
        stile.font.italic = italic


def ombreggia(elemento_pr, colore_hex: str) -> None:
    """Aggiunge <w:shd> a un pPr, rPr, tcPr o tblPr."""
    inserisci(elemento_pr, elemento("w:shd", **{"w:val": "clear", "w:color": "auto", "w:fill": colore_hex}))


def bordo_paragrafo(ppr, lato: str = "bottom", colore: str = "9A948C", spessore: int = 4, spazio: int = 1) -> None:
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = inserisci(ppr, OxmlElement("w:pBdr"))
    pbdr.append(elemento(f"w:{lato}", **{"w:val": "single", "w:sz": spessore, "w:space": spazio, "w:color": colore}))


def livello_struttura(stile, livello: int) -> None:
    inserisci(stile.element.get_or_add_pPr(), elemento("w:outlineLvl", **{"w:val": livello}))


def _stile(doc, nome: str, tipo=WD_STYLE_TYPE.PARAGRAPH, base: str | None = None):
    stili = doc.styles
    try:
        s = stili[nome]
    except KeyError:
        s = stili.add_style(nome, tipo)
    if base:
        s.base_style = stili[base]
    return s


def _para(s, prima=0, dopo=0, interlinea=None, allinea=None, rientro_sx=None, mantieni_succ=None):
    pf = s.paragraph_format
    pf.space_before = Pt(prima)
    pf.space_after = Pt(dopo)
    if interlinea is not None:
        pf.line_spacing = interlinea
    if allinea is not None:
        pf.alignment = allinea
    if rientro_sx is not None:
        pf.left_indent = Cm(rientro_sx)
    if mantieni_succ is not None:
        pf.keep_with_next = mantieni_succ


# --- Definizione degli stili ---------------------------------------------------
def crea_stili(doc) -> None:
    st = doc.styles

    # Lingua e font predefiniti del documento (docDefaults)
    rpr_default = doc.styles.element.find(qn("w:docDefaults")).find(qn("w:rPrDefault")).find(qn("w:rPr"))
    lang = rpr_default.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr_default.append(lang)
    for a in ("w:val", "w:eastAsia", "w:bidi"):
        lang.set(qn(a), LINGUA)
    imposta_font(rpr_default, FONT_CORPO)

    normal = st["Normal"]
    font_stile(normal, FONT_CORPO, 10.5, INCHIOSTRO)
    _para(normal, 0, 4, 1.2, WD_ALIGN_PARAGRAPH.JUSTIFY)
    normal.paragraph_format.widow_control = True

    corpo = _stile(doc, "Libro Corpo", base="Normal")

    # Titoli (Heading 1-3 servono al campo TOC)
    h1 = st["Heading 1"]
    font_stile(h1, FONT_TITOLI, 24, INCHIOSTRO, bold=True, italic=False)
    _para(h1, 0, 24, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)
    h2 = st["Heading 2"]
    font_stile(h2, FONT_TITOLI, 13.5, INCHIOSTRO, bold=True, italic=False)
    _para(h2, 14, 5, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)
    h3 = st["Heading 3"]
    font_stile(h3, FONT_TITOLI, 11, ACCENTO, bold=True, italic=False)
    _para(h3, 10, 3, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)

    et = _stile(doc, "Libro Etichetta Capitolo")
    font_stile(et, FONT_TITOLI, 11, ACCENTO, bold=True)
    et.font.all_caps = True
    _para(et, 60, 6, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)

    parte_et = _stile(doc, "Libro Etichetta Parte")
    font_stile(parte_et, FONT_TITOLI, 14, ACCENTO, bold=True)
    parte_et.font.all_caps = True
    _para(parte_et, 0, 8, 1.0, WD_ALIGN_PARAGRAPH.CENTER, mantieni_succ=True)

    parte = _stile(doc, "Titolo Parte")
    font_stile(parte, FONT_TITOLI, 30, INCHIOSTRO, bold=True)
    _para(parte, 0, 18, 1.0, WD_ALIGN_PARAGRAPH.CENTER)
    livello_struttura(parte, 0)

    parte_intro = _stile(doc, "Libro Introduzione Parte", base="Normal")
    font_stile(parte_intro, FONT_CORPO, 11, GRIGIO, italic=True)
    _para(parte_intro, 0, 6, 1.25, WD_ALIGN_PARAGRAPH.CENTER, rientro_sx=1.0)
    parte_intro.paragraph_format.right_indent = Cm(1.0)

    # Codice e terminale (dentro tabelle a una cella)
    cod = _stile(doc, "Libro Codice")
    font_stile(cod, FONT_CODICE, 8.5, INCHIOSTRO)
    _para(cod, 0, 0, 1.0, WD_ALIGN_PARAGRAPH.LEFT)
    term = _stile(doc, "Libro Terminale")
    font_stile(term, FONT_CODICE, 8.5, CREMA)
    _para(term, 0, 0, 1.0, WD_ALIGN_PARAGRAPH.LEFT)

    cod_in = _stile(doc, "Libro Codice in linea", WD_STYLE_TYPE.CHARACTER)
    font_stile(cod_in, FONT_CODICE, 9.5, RGBColor(0x8A, 0x3E, 0x26))

    # Box
    for tipo in ("nota", "consiglio", "attenzione"):
        tb = _stile(doc, f"Box {TITOLO_BOX[tipo]} Titolo")
        font_stile(tb, FONT_TITOLI, 10, RGBColor.from_string(BORDO_BOX[tipo]), bold=True)
        _para(tb, 0, 3, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)
    tbx = _stile(doc, "Box Testo", base="Normal")
    font_stile(tbx, FONT_CORPO, 9.5, INCHIOSTRO)
    _para(tbx, 0, 3, 1.15, WD_ALIGN_PARAGRAPH.LEFT)

    # Figure e didascalie
    fig = _stile(doc, "Libro Figura", base="Normal")
    _para(fig, 8, 3, 1.0, WD_ALIGN_PARAGRAPH.CENTER, mantieni_succ=True)
    did = _stile(doc, "Libro Didascalia", base="Normal")
    font_stile(did, FONT_CORPO, 8.5, GRIGIO, italic=True)
    _para(did, 0, 10, 1.1, WD_ALIGN_PARAGRAPH.CENTER)

    # Citazioni ed epigrafi
    cit = _stile(doc, "Libro Citazione", base="Normal")
    font_stile(cit, FONT_CORPO, 10, GRIGIO, italic=True)
    _para(cit, 4, 6, 1.2, WD_ALIGN_PARAGRAPH.LEFT, rientro_sx=1.0)
    cit.paragraph_format.right_indent = Cm(1.0)

    sep = _stile(doc, "Libro Separatore", base="Normal")
    font_stile(sep, FONT_SIMBOLI, 11, ACCENTO)
    _para(sep, 8, 8, 1.0, WD_ALIGN_PARAGRAPH.CENTER)

    # Tabelle
    tab = _stile(doc, "Libro Tabella", base="Normal")
    font_stile(tab, FONT_CORPO, 9, INCHIOSTRO)
    _para(tab, 1, 1, 1.05, WD_ALIGN_PARAGRAPH.LEFT)
    tabh = _stile(doc, "Libro Tabella Intestazione", base="Libro Tabella")
    font_stile(tabh, FONT_TITOLI, 9, INCHIOSTRO, bold=True)

    # Elenchi
    for nome in ("List Bullet", "List Bullet 2", "List Number", "List Number 2"):
        s = st[nome]
        s.base_style = normal
        _para(s, 0, 2, 1.2, WD_ALIGN_PARAGRAPH.LEFT)

    # Intestazioni e piè di pagina
    tes = _stile(doc, "Libro Testatina", base="Normal")
    font_stile(tes, FONT_TITOLI, 8.5, GRIGIO)
    tes.font.small_caps = True
    _para(tes, 0, 0, 1.0)
    pie = _stile(doc, "Libro Piede", base="Normal")
    font_stile(pie, FONT_TITOLI, 8.5, GRIGIO)
    _para(pie, 0, 0, 1.0)

    # Indice generale
    titolo_ind = _stile(doc, "Libro Titolo Indice", base="Normal")
    font_stile(titolo_ind, FONT_TITOLI, 24, INCHIOSTRO, bold=True)
    _para(titolo_ind, 60, 24, 1.0, WD_ALIGN_PARAGRAPH.LEFT)
    for livello, (size, bold, prima, rientro) in {1: (10.5, True, 7, 0), 2: (9.5, False, 0, 0.6), 3: (10.5, True, 12, 0)}.items():
        nome = f"toc {livello}"
        s = _stile(doc, nome, base="Normal")
        font_stile(s, FONT_TITOLI if livello != 2 else FONT_CORPO, size, INCHIOSTRO, bold=bold)
        _para(s, prima, 1, 1.1, WD_ALIGN_PARAGRAPH.LEFT, rientro_sx=rientro)
        s.paragraph_format.tab_stops.add_tab_stop(Cm(LARGHEZZA_TESTO_CM), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    # toc 3 = voci di Parte nell'indice
    st["toc 3"].font.all_caps = True
    st["toc 3"].font.color.rgb = ACCENTO

    # Indice analitico
    ia = _stile(doc, "Libro Indice Analitico", base="Normal")
    font_stile(ia, FONT_CORPO, 8.5, INCHIOSTRO)
    _para(ia, 0, 0, 1.05, WD_ALIGN_PARAGRAPH.LEFT, rientro_sx=0.4)
    ia.paragraph_format.first_line_indent = Cm(-0.4)
    ial = _stile(doc, "Libro Indice Lettera", base="Normal")
    font_stile(ial, FONT_TITOLI, 10, ACCENTO, bold=True)
    _para(ial, 6, 2, 1.0, WD_ALIGN_PARAGRAPH.LEFT, mantieni_succ=True)

    # Pagine preliminari
    fr_t = _stile(doc, "Libro Frontespizio Titolo", base="Normal")
    font_stile(fr_t, FONT_SIMBOLI_MONO, 30, INCHIOSTRO, bold=True)
    _para(fr_t, 0, 0, 1.0, WD_ALIGN_PARAGRAPH.CENTER)
    fr_a = _stile(doc, "Libro Frontespizio Autore", base="Normal")
    font_stile(fr_a, FONT_TITOLI, 14, GRIGIO)
    _para(fr_a, 30, 6, 1.0, WD_ALIGN_PARAGRAPH.CENTER)
    col = _stile(doc, "Libro Colophon", base="Normal")
    font_stile(col, FONT_CORPO, 8, GRIGIO)
    _para(col, 0, 4, 1.15, WD_ALIGN_PARAGRAPH.LEFT)
    ded = _stile(doc, "Libro Dedica", base="Normal")
    font_stile(ded, FONT_CORPO, 11, INCHIOSTRO, italic=True)
    _para(ded, 0, 6, 1.3, WD_ALIGN_PARAGRAPH.RIGHT)

    # Niente sillabazione nei titoli e negli elementi di servizio
    for nome in ("Heading 1", "Heading 2", "Heading 3", "Libro Etichetta Capitolo", "Libro Etichetta Parte",
                 "Titolo Parte", "toc 1", "toc 2", "toc 3", "Libro Titolo Indice", "Libro Frontespizio Titolo",
                 "Libro Frontespizio Autore", "Libro Testatina", "Libro Piede", "Libro Didascalia",
                 "Libro Codice", "Libro Terminale", "Libro Tabella", "Libro Tabella Intestazione",
                 "Box Nota Titolo", "Box Consiglio Titolo", "Box Attenzione Titolo", "Libro Indice Analitico"):
        no_sillabazione(st[nome])


def imposta_impostazioni_documento(doc) -> None:
    """Pagine pari/dispari diverse, margini a specchio, sillabazione automatica."""
    settings = doc.settings.element

    def aggiungi(tag, **attrs):
        if settings.find(qn(tag)) is None:
            el = OxmlElement(tag)
            for k, v in attrs.items():
                el.set(qn(k), v)
            settings.append(el)

    doc.settings.odd_and_even_pages_header_footer = True
    aggiungi("w:mirrorMargins")
    aggiungi("w:autoHyphenation")
    aggiungi("w:consecutiveHyphenLimit", **{"w:val": "2"})
    # L'ordine degli elementi in settings.xml conta per Word: riordiniamo quelli aggiunti
    _riordina_settings(settings)


_ORDINE_SETTINGS = [
    "w:writeProtection", "w:view", "w:zoom", "w:removePersonalInformation", "w:removeDateAndTime",
    "w:doNotDisplayPageBoundaries", "w:displayBackgroundShape", "w:printPostScriptOverText",
    "w:printFractionalCharacterWidth", "w:printFormsData", "w:embedTrueTypeFonts", "w:embedSystemFonts",
    "w:saveSubsetFonts", "w:saveFormsData", "w:mirrorMargins", "w:alignBordersAndEdges",
    "w:bordersDoNotSurroundHeader", "w:bordersDoNotSurroundFooter", "w:gutterAtTop", "w:hideSpellingErrors",
    "w:hideGrammaticalErrors", "w:activeWritingStyle", "w:proofState", "w:formsDesign", "w:attachedTemplate",
    "w:linkStyles", "w:stylePaneFormatFilter", "w:stylePaneSortMethod", "w:documentType", "w:mailMerge",
    "w:revisionView", "w:trackRevisions", "w:doNotTrackMoves", "w:doNotTrackFormatting", "w:documentProtection",
    "w:autoFormatOverride", "w:styleLockTheme", "w:styleLockQFSet", "w:defaultTabStop", "w:autoHyphenation",
    "w:consecutiveHyphenLimit", "w:hyphenationZone", "w:doNotHyphenateCaps", "w:showEnvelope",
    "w:summaryLength", "w:clickAndTypeStyle", "w:defaultTableStyle", "w:evenAndOddHeaders",
]


def _riordina_settings(settings) -> None:
    pos = {t: i for i, t in enumerate(_ORDINE_SETTINGS)}
    figli = list(settings)
    noti = [c for c in figli if c.tag in {qn(t) for t in pos}]
    noti.sort(key=lambda c: pos[next(t for t in pos if qn(t) == c.tag)])
    altri = [c for c in figli if c not in noti]
    for c in figli:
        settings.remove(c)
    for c in noti + altri:
        settings.append(c)
