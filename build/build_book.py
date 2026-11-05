"""Assembla il libro: legge book.yaml e i capitoli Markdown e scrive output/<nome>.docx.

Uso:
    py build/build_book.py                    # libro completo (book.yaml)
    py build/build_book.py --config book-prova.yaml

Le pagine dell'indice generale e dell'indice analitico vengono dall'ultima impaginazione
(output/<nome>.pagine.json, scritto da update_indexes.py). Per numeri corretti usare
update_indexes.py, che ricostruisce il documento finché i numeri di pagina sono stabili.

Convenzioni Markdown (vedi CLAUDE.md):
    # Titolo del capitolo           (primo H1 = titolo; H2 nell'indice, H3 no)
    ::: nota|consiglio|attenzione [Titolo]   …   :::
    ```terminale  … ```             finto terminale;  ```python … ```  blocco di codice
    ![Didascalia](assets/capNN/IMG-NN-MM-x.png){larghezza=10}
    [testo]{xe="voce d'indice"}     voce dell'indice analitico
    [Ctrl+C]{.tasto}                tasto
    <!-- F-NNN -->                  rimando a research/FATTI.md (invisibile)
    ---                             separatore ✻
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from markdown_it import MarkdownIt
from mdit_py_plugins.attrs import attrs_plugin
from mdit_py_plugins.container import container_plugin
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import comune  # noqa: E402
import stili  # noqa: E402
from stili import elemento, inserisci  # noqa: E402

ROMANI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
TWIP_CM = 567


def crea_md() -> MarkdownIt:
    md = MarkdownIt("commonmark", {"typographer": True, "quotes": "«»“”"})
    md.enable(["table", "replacements", "smartquotes", "strikethrough"])
    for nome in ("nota", "consiglio", "attenzione"):
        md.use(container_plugin, name=nome)
    md.use(attrs_plugin, spans=True)
    return md


def testo_piano(inline_token) -> str:
    out = []
    for c in inline_token.children or []:
        if c.type in ("text", "code_inline"):
            out.append(c.content)
        elif c.type in ("softbreak", "hardbreak"):
            out.append(" ")
    return "".join(out).strip()


def segmenta(testo: str):
    """Divide il testo in pezzi (normale / glifo speciale)."""
    if not testo:
        return
    corrente, speciale = testo[0], testo[0] in stili.GLIFI_SPECIALI
    for ch in testo[1:]:
        s = ch in stili.GLIFI_SPECIALI
        if s == speciale:
            corrente += ch
        else:
            yield corrente, speciale
            corrente, speciale = ch, s
    yield corrente, speciale


def trova_chiusura(tokens, i: int) -> int:
    """Indice del token di chiusura che corrisponde all'apertura in posizione i."""
    tipo_apre = tokens[i].type
    tipo_chiude = tipo_apre.replace("_open", "_close")
    livello = 0
    for j in range(i, len(tokens)):
        if tokens[j].type == tipo_apre:
            livello += 1
        elif tokens[j].type == tipo_chiude:
            livello -= 1
            if livello == 0:
                return j
    raise ValueError(f"Chiusura non trovata per {tipo_apre}")


# --- Campi Word ----------------------------------------------------------------
def _fld(run, tipo: str):
    run._r.append(elemento("w:fldChar", **{"w:fldCharType": tipo}))


def campo(par, istruzione: str, cache: str = "1"):
    r = par.add_run(); _fld(r, "begin")
    r = par.add_run()
    it = elemento("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {istruzione} "
    r._r.append(it)
    r = par.add_run(); _fld(r, "separate")
    r = par.add_run(cache)
    r2 = par.add_run(); _fld(r2, "end")
    return r


def campo_xe(par, voce: str):
    r = par.add_run(); _fld(r, "begin")
    r = par.add_run()
    it = elemento("w:instrText"); it.set(qn("xml:space"), "preserve")
    it.text = ' XE "' + voce.replace('"', "'") + '" '
    r._r.append(it)
    r = par.add_run(); _fld(r, "end")


# --- Tabelle di servizio ---------------------------------------------------------
def bordi_tabella(tabella, bordi: dict):
    """bordi: lato -> (val, spessore_ottavi_di_punto, colore) oppure None per nessun bordo."""
    tblpr = tabella._tbl.tblPr
    tb = elemento("w:tblBorders")
    for lato in ("top", "left", "bottom", "right", "insideH", "insideV"):
        v = bordi.get(lato)
        if v is None:
            tb.append(elemento(f"w:{lato}", **{"w:val": "nil"}))
        else:
            tb.append(elemento(f"w:{lato}", **{"w:val": v[0], "w:sz": v[1], "w:space": 0, "w:color": v[2]}))
    inserisci(tblpr, tb)


def larghezza_tabella(tabella, cm: float, colonne_cm: list[float] | None = None):
    tblpr = tabella._tbl.tblPr
    inserisci(tblpr, elemento("w:tblW", **{"w:w": int(cm * TWIP_CM), "w:type": "dxa"}))
    inserisci(tblpr, elemento("w:tblLayout", **{"w:type": "fixed"}))
    colonne_cm = colonne_cm or [cm]
    grid = tabella._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), colonne_cm):
        gc.set(qn("w:w"), str(int(w * TWIP_CM)))
    for riga in tabella.rows:
        for cella, w in zip(riga.cells, colonne_cm):
            cella.width = Cm(w)


def margini_cella(tabella, sopra=0.12, sinistra=0.3, sotto=0.12, destra=0.3):
    m = elemento("w:tblCellMar")
    for lato, v in (("top", sopra), ("left", sinistra), ("bottom", sotto), ("right", destra)):
        m.append(elemento(f"w:{lato}", **{"w:w": int(v * TWIP_CM), "w:type": "dxa"}))
    inserisci(tabella._tbl.tblPr, m)


def sfondo_cella(cella, colore: str):
    stili.ombreggia(cella._tc.get_or_add_tcPr(), colore)


class Costruttore:
    def __init__(self, cfg: dict, pagine: dict | None = None):
        self.cfg = cfg
        self.meta = cfg["metadati"]
        self.pagine = pagine or {}
        self.doc = Document()
        stili.crea_stili(self.doc)
        stili.imposta_impostazioni_documento(self.doc)
        self.md = crea_md()
        self.voci: list[dict] = []      # voci dell'indice generale
        self.xe: list[dict] = []        # voci dell'indice analitico
        self.figure: list[dict] = []
        self.marcatori_fatti: list[str] = []
        self.sezioni_usate = 0
        self.etichetta = ""
        self.n_fig = 0
        self.voce_capitolo = None
        self.primo_arabo = True
        self.a_capo = False  # True: gli a capo del sorgente restano a capo (dedica, poesie)
        self.sezioni_reg: list[dict] = []
        self.bianche = set(self.pagine.get("bianche", []))
        self._formato_corrente = "lowerRoman"
        self.cartella = comune.RADICE / cfg.get("cartella_capitoli", "capitoli")
        self.crediti = self._leggi_crediti()

    # ---------------- sezioni, testatine, piè di pagina ----------------
    def nuova_sezione(self, inizio=WD_SECTION.NEW_PAGE, formato="decimal", riparti=None,
                      testatina=None, piede="numerato", prima_diversa=False, centra=False, colonne=1,
                      margini=None, firma=None, recto=False):
        """`firma` = (testo, dimensione in pt) con cui update_indexes.py ritrova nel PDF la prima pagina
        della sezione; `recto` = la sezione deve iniziare su pagina dispari (a destra).
        Le pagine bianche per mandare a destra capitoli e parti le decide update_indexes.py misurando
        il PDF (LibreOffice gestisce male le interruzioni "pagina dispari" con testatine diverse)."""
        if firma:
            sid = f"s{len(self.sezioni_reg) + 1:02d}"
            self.sezioni_reg.append({"id": sid, "testo": firma[0], "cerca": firma[0],
                                     "dimensione": firma[1], "recto": recto})
            if sid in self.bianche:
                self.nuova_sezione(formato=self._formato_corrente, piede=None)
                self.doc.add_paragraph()
        self._formato_corrente = formato
        pg = self.cfg["pagina"]
        if self.sezioni_usate == 0:
            sez = self.doc.sections[0]
        else:
            sez = self.doc.add_section(inizio)
        self.sezioni_usate += 1
        sez.page_width, sez.page_height = Cm(pg["larghezza_cm"]), Cm(pg["altezza_cm"])
        m = margini or pg["margini_cm"]
        sez.left_margin, sez.right_margin = Cm(m["interno"]), Cm(m["esterno"])
        sez.top_margin, sez.bottom_margin = Cm(m["superiore"]), Cm(m["inferiore"])
        sez.header_distance, sez.footer_distance = Cm(m.get("testatina", 1.0)), Cm(m.get("piede", 1.2))
        sp = sez._sectPr
        pn = elemento("w:pgNumType", **{"w:fmt": formato})
        if riparti is not None:
            pn.set(qn("w:start"), str(riparti))
        inserisci(sp, pn)
        for vecchio in sp.findall(qn("w:vAlign")):
            sp.remove(vecchio)
        if centra:
            inserisci(sp, elemento("w:vAlign", **{"w:val": "center"}))
        for vecchio in sp.findall(qn("w:cols")):
            sp.remove(vecchio)
        inserisci(sp, elemento("w:cols", **{"w:num": colonne, "w:space": int(0.8 * TWIP_CM)}))
        # Sempre "prima pagina diversa": LibreOffice, se una sezione è preceduta da una pagina bianca
        # inserita automaticamente, applica male l'impostazione. Se la prima pagina non deve essere
        # diversa, le si dà lo stesso contenuto delle altre.
        sez.different_first_page_header_footer = True

        for hf in (sez.header, sez.even_page_header, sez.first_page_header,
                   sez.footer, sez.even_page_footer, sez.first_page_footer):
            hf.is_linked_to_previous = False
            for p in hf.paragraphs[1:]:
                p._p.getparent().remove(p._p)
            p0 = hf.paragraphs[0]
            for r in list(p0.runs):
                r._r.getparent().remove(r._r)

        if testatina:
            dispari, pari = testatina
            self._testatina(sez.header.paragraphs[0], dispari, WD_ALIGN_PARAGRAPH.RIGHT)
            self._testatina(sez.even_page_header.paragraphs[0], pari, WD_ALIGN_PARAGRAPH.LEFT)
            if not prima_diversa:
                self._testatina(sez.first_page_header.paragraphs[0], dispari, WD_ALIGN_PARAGRAPH.RIGHT)
        if piede == "numerato":
            self._piede(sez.footer.paragraphs[0], WD_ALIGN_PARAGRAPH.RIGHT, dispari=True)
            self._piede(sez.even_page_footer.paragraphs[0], WD_ALIGN_PARAGRAPH.LEFT, dispari=False)
            if prima_diversa:
                self._piede(sez.first_page_footer.paragraphs[0], WD_ALIGN_PARAGRAPH.CENTER, solo_numero=True)
            else:
                self._piede(sez.first_page_footer.paragraphs[0], WD_ALIGN_PARAGRAPH.RIGHT, dispari=True)
        elif piede == "centrato":
            for f in (sez.footer, sez.even_page_footer, sez.first_page_footer):
                self._piede(f.paragraphs[0], WD_ALIGN_PARAGRAPH.CENTER, solo_numero=True)
        return sez

    def _testatina(self, p, testo, allinea):
        p.style = "Libro Testatina"
        p.alignment = allinea
        self.testo(p, testo)
        stili.bordo_paragrafo(p._p.get_or_add_pPr(), "bottom", "C9C3BA", 4, 4)

    def _piede(self, p, allinea, dispari=True, solo_numero=False):
        p.style = "Libro Piede"
        p.alignment = allinea
        autore = self.meta["autore"]
        if solo_numero:
            campo(p, "PAGE")
        elif dispari:
            p.add_run(f"{autore}   ")
            r = campo(p, "PAGE"); r.bold = True
        else:
            r = campo(p, "PAGE"); r.bold = True
            p.add_run(f"   {autore}")

    # ---------------- testo e inline ----------------
    def testo(self, par, testo, bold=None, italic=None, stile_car=None, colore=None, mono=False,
              size=None, strike=None):
        ultimo = None
        for pezzo, speciale in segmenta(testo):
            r = par.add_run(pezzo)
            if stile_car:
                r.style = stile_car
            if bold:
                r.bold = True
            if italic:
                r.italic = True
            if strike:
                r.font.strike = True
            if colore is not None:
                r.font.color.rgb = colore
            if size:
                r.font.size = Pt(size)
            if speciale:
                stili.imposta_font(r._r.get_or_add_rPr(),
                                   stili.FONT_SIMBOLI_MONO if (mono or stile_car) else stili.FONT_SIMBOLI)
            ultimo = r
        return ultimo

    def inline(self, par, figli, colore=None, bold=False, italic=False):
        n_bold = n_it = n_strike = 0
        span_stack = []
        for t in figli or []:
            ty = t.type
            if ty == "text":
                self.testo(par, t.content, bold or n_bold > 0, italic or n_it > 0, colore=colore,
                           strike=n_strike > 0)
                for s in span_stack:
                    s["testo"] += t.content
            elif ty == "strong_open":
                n_bold += 1
            elif ty == "strong_close":
                n_bold -= 1
            elif ty == "em_open":
                n_it += 1
            elif ty == "em_close":
                n_it -= 1
            elif ty == "s_open":
                n_strike += 1
            elif ty == "s_close":
                n_strike -= 1
            elif ty == "code_inline":
                self.testo(par, t.content, stile_car="Libro Codice in linea")
                for s in span_stack:
                    s["testo"] += t.content
            elif ty == "softbreak":
                if self.a_capo:
                    par.add_run().add_break()
                else:
                    par.add_run(" ")
            elif ty == "hardbreak":
                par.add_run().add_break()
            elif ty == "span_open":
                classi = (t.attrs.get("class") or "").split()
                span_stack.append({"xe": t.attrs.get("xe"), "tasto": "tasto" in classi, "testo": ""})
                if "tasto" in classi:
                    # i tasti si rendono come codice: il testo arriva nei token successivi
                    span_stack[-1]["par_runs"] = len(par.runs)
            elif ty == "span_close":
                s = span_stack.pop()
                if s.get("tasto"):
                    for r in par.runs[s["par_runs"]:]:
                        r.style = "Libro Codice in linea"
                        r.bold = True
                if s["xe"]:
                    campo_xe(par, s["xe"])
                    self.xe.append({"voce": s["xe"], "testo": s["testo"].strip(),
                                    "capitolo": self.voce_capitolo})
            elif ty == "html_inline":
                self._marcatori(t.content)
            elif ty == "image":
                comune.avviso(f"immagine in mezzo al testo ignorata: {t.attrs.get('src')}")
            # link_open/link_close: si rende solo il testo

    def _marcatori(self, html: str):
        self.marcatori_fatti.extend(re.findall(r"F-\d{3}", html))

    # ---------------- blocchi ----------------
    def blocchi(self, tokens, target, stile="Libro Corpo"):
        i = 0
        liste: list[dict] = []
        while i < len(tokens):
            t = tokens[i]
            ty = t.type
            if ty == "heading_open":
                self.titoletto(target, int(t.tag[1]), tokens[i + 1])
                i += 3
            elif ty == "paragraph_open":
                inl = tokens[i + 1]
                figli = [c for c in (inl.children or []) if not (c.type == "text" and not c.content.strip())]
                if len(figli) == 1 and figli[0].type == "image" and not liste:
                    self.figura(target, figli[0])
                else:
                    p = target.add_paragraph(style=self._stile_lista(liste) if liste else stile)
                    if liste and liste[-1].get("num_id") is not None:
                        self._applica_numerazione(p, liste[-1]["num_id"], len(liste) - 1)
                    if liste and liste[-1]["primo_par_fatto"]:
                        # secondo paragrafo dello stesso punto: niente pallino
                        p.style = stile
                        p.paragraph_format.left_indent = Cm(0.63 * len(liste))
                    if liste:
                        liste[-1]["primo_par_fatto"] = True
                    self.inline(p, inl.children)
                i += 3
            elif ty in ("bullet_list_open", "ordered_list_open"):
                ordinata = ty == "ordered_list_open"
                d = {"ordinata": ordinata, "primo_par_fatto": False, "num_id": None}
                if ordinata:
                    d["num_id"] = self._nuova_numerazione("List Number" if not liste else "List Number 2")
                liste.append(d)
                i += 1
            elif ty in ("bullet_list_close", "ordered_list_close"):
                liste.pop()
                i += 1
            elif ty == "list_item_open":
                if liste:
                    liste[-1]["primo_par_fatto"] = False
                i += 1
            elif ty == "list_item_close":
                i += 1
            elif ty in ("fence", "code_block"):
                self.codice(target, (t.info or "").strip(), t.content)
                i += 1
            elif ty.startswith("container_") and ty.endswith("_open"):
                j = trova_chiusura(tokens, i)
                tipo = ty[len("container_"):-len("_open")]
                titolo = t.info.strip()[len(tipo):].strip()
                self.box(target, tipo, titolo, tokens[i + 1:j])
                i = j + 1
            elif ty == "blockquote_open":
                j = trova_chiusura(tokens, i)
                self.blocchi(tokens[i + 1:j], target, "Libro Citazione")
                i = j + 1
            elif ty == "table_open":
                j = trova_chiusura(tokens, i)
                self.tabella(target, tokens[i:j + 1])
                i = j + 1
            elif ty == "hr":
                p = target.add_paragraph(style="Libro Separatore")
                self.testo(p, "✻")
                i += 1
            elif ty == "html_block":
                self._marcatori(t.content)
                i += 1
            else:
                i += 1

    def _stile_lista(self, liste):
        prof = min(len(liste), 2)
        base = "List Number" if liste[-1]["ordinata"] else "List Bullet"
        return base if prof == 1 else f"{base} 2"

    def _nuova_numerazione(self, nome_stile):
        try:
            stile = self.doc.styles[nome_stile]
            num_id = stile.element.pPr.numPr.numId.val
            numbering = self.doc.part.numbering_part.element
            num = next(n for n in numbering.num_lst if n.numId == num_id)
            nuovo = numbering.add_num(num.abstractNumId.val)
            ovr = nuovo.add_lvlOverride(ilvl=0)
            ovr.add_startOverride(1)
            return nuovo.numId
        except Exception as e:  # pragma: no cover
            comune.avviso(f"numerazione elenco non ripartita ({e})")
            return None

    @staticmethod
    def _applica_numerazione(p, num_id, livello):
        numpr = p._p.get_or_add_pPr().get_or_add_numPr()
        numpr.get_or_add_ilvl().val = 0
        numpr.get_or_add_numId().val = num_id

    def titoletto(self, target, livello, inl):
        if livello == 1:
            livello = 2  # un secondo H1 nel capitolo diventa H2
        p = target.add_paragraph(style=f"Heading {min(livello, 3)}")
        self.inline(p, inl.children)
        if livello == 2:
            self._voce(2, testo_piano(inl), 13.5)

    def _voce(self, livello, testo, dimensione, etichetta="", cerca=None):
        """`testo` è quello mostrato nell'indice; `cerca` (se diverso) quello da trovare nel PDF."""
        vid = f"v{len(self.voci) + 1:03d}"
        self.voci.append({"id": vid, "livello": livello, "testo": testo, "dimensione": dimensione,
                          "etichetta": etichetta, "cerca": cerca or testo})
        return vid

    def figura(self, target, img):
        src = img.attrs.get("src", "")
        alt = "".join(c.content for c in (img.children or [])) or img.content
        larg = min(float(img.attrs.get("larghezza", 12)), stili.LARGHEZZA_TESTO_CM)
        alt_max = float(img.attrs.get("altezza_max", 11))
        self.n_fig += 1
        numero = f"{self.etichetta}.{self.n_fig}" if self.etichetta else str(self.n_fig)
        percorso = comune.RADICE / src
        p = target.add_paragraph(style="Libro Figura")
        if percorso.exists():
            with Image.open(percorso) as im:
                w, h = im.size
            if larg * h / w > alt_max:
                larg = alt_max * w / h
            p.add_run().add_picture(str(percorso), width=Cm(larg))
        else:
            comune.avviso(f"figura mancante: {src}")
            self.testo(p, f"[FIGURA MANCANTE: {src}]", bold=True, colore=RGBColor(0xC0, 0, 0))
        c = target.add_paragraph(style="Libro Didascalia")
        r = c.add_run(f"Figura {numero} – ")
        r.bold = True
        r.italic = False
        self.testo(c, alt)
        self.figure.append({"numero": numero, "src": src, "didascalia": alt, "capitolo": self.voce_capitolo})

    def codice(self, target, info, contenuto):
        terminale = (info.split() or [""])[0].lower() in ("terminale", "terminal", "console")
        tab = target.add_table(rows=1, cols=1)
        tab.alignment = WD_TABLE_ALIGNMENT.CENTER
        larghezza_tabella(tab, stili.LARGHEZZA_TESTO_CM)
        margini_cella(tab, 0.15, 0.3, 0.15, 0.3)
        cella = tab.cell(0, 0)
        if terminale:
            bordi_tabella(tab, {})
            sfondo_cella(cella, stili.FONDO_TERMINALE)
        else:
            bordi_tabella(tab, {"left": ("single", 18, stili.ACCENTO_HEX)})
            sfondo_cella(cella, stili.FONDO_CODICE)
        righe = contenuto.rstrip("\n").replace("\t", "    ").split("\n")
        for k, riga in enumerate(righe):
            p = cella.paragraphs[0] if k == 0 else cella.add_paragraph()
            p.style = "Libro Terminale" if terminale else "Libro Codice"
            if terminale:
                self._riga_terminale(p, riga)
            else:
                s = riga.lstrip()
                commento = s.startswith(("#", "//", "--", "REM ", "::"))
                self.testo(p, riga or " ", italic=commento or None,
                           colore=stili.GRIGIO if commento else None, mono=True)
        self._spazio(target)

    def _riga_terminale(self, p, riga):
        m = re.match(r"^(\$ |> |❯ |PS [^>]*> )(.*)$", riga)
        if m:
            self.testo(p, m.group(1), colore=stili.ACCENTO, bold=True, mono=True)
            self.testo(p, m.group(2), mono=True)
            return
        if riga.lstrip().startswith("#"):
            self.testo(p, riga, colore=stili.GRIGIO_CHIARO, italic=True, mono=True)
            return
        for pezzo, speciale in segmenta(riga or " "):
            self.testo(p, pezzo, colore=stili.ACCENTO if speciale else None, mono=True)

    def _spazio(self, target, pt=5):
        p = target.add_paragraph(style="Normal")
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run()
        r.font.size = Pt(pt)
        # il paragrafo vuoto deve avere la dimensione del font nel suo segno di paragrafo
        rpr = p._p.get_or_add_pPr()
        prpr = rpr.find(qn("w:rPr"))
        if prpr is None:
            prpr = inserisci(rpr, elemento("w:rPr"))
        inserisci(prpr, elemento("w:sz", **{"w:val": pt * 2}))

    def box(self, target, tipo, titolo, interni):
        if tipo not in stili.TITOLO_BOX:
            comune.avviso(f"tipo di box sconosciuto: {tipo}")
            tipo = "nota"
        tab = target.add_table(rows=1, cols=1)
        tab.alignment = WD_TABLE_ALIGNMENT.CENTER
        larghezza_tabella(tab, stili.LARGHEZZA_TESTO_CM)
        margini_cella(tab, 0.2, 0.35, 0.15, 0.35)
        bordi_tabella(tab, {"left": ("single", 24, stili.BORDO_BOX[tipo])})
        cella = tab.cell(0, 0)
        sfondo_cella(cella, stili.FONDO_BOX[tipo])
        p = cella.paragraphs[0]
        p.style = f"Box {stili.TITOLO_BOX[tipo]} Titolo"
        self.testo(p, stili.ICONA_BOX[tipo] + "  ")
        self.testo(p, titolo or stili.TITOLO_BOX[tipo])
        self.blocchi(interni, cella, "Box Testo")
        ultimo = cella.paragraphs[-1]
        ultimo.paragraph_format.space_after = Pt(0)
        self._spazio(target)

    def tabella(self, target, toks):
        righe, intest, allinea = [], [], []
        corrente = None
        in_head = False
        for t in toks:
            if t.type == "thead_open":
                in_head = True
            elif t.type == "thead_close":
                in_head = False
            elif t.type == "tr_open":
                corrente = []
            elif t.type in ("th_open", "td_open"):
                stile_attr = t.attrs.get("style", "") if t.attrs else ""
                if len(righe) == 0:
                    allinea.append("right" if "right" in stile_attr else "center" if "center" in stile_attr else "left")
            elif t.type == "inline" and corrente is not None:
                corrente.append(t)
            elif t.type == "tr_close":
                righe.append(corrente)
                intest.append(in_head)
        n = max(len(r) for r in righe)
        lun = [max(1, max(len(testo_piano(r[c])) if c < len(r) else 0 for r in righe)) for c in range(n)]
        lun = [min(max(x, 6), 60) for x in lun]
        tot = sum(lun)
        larghezze = [stili.LARGHEZZA_TESTO_CM * x / tot for x in lun]
        tab = target.add_table(rows=len(righe), cols=n)
        tab.alignment = WD_TABLE_ALIGNMENT.CENTER
        larghezza_tabella(tab, stili.LARGHEZZA_TESTO_CM, larghezze)
        margini_cella(tab, 0.05, 0.12, 0.05, 0.12)
        bordi_tabella(tab, {"top": ("single", 8, "1F1E1D"), "bottom": ("single", 8, "1F1E1D"),
                            "insideH": ("single", 2, "C9C3BA")})
        for ri, (riga, testa) in enumerate(zip(righe, intest)):
            if testa:
                trpr = tab.rows[ri]._tr.get_or_add_trPr()
                inserisci(trpr, elemento("w:tblHeader"))
            for ci in range(n):
                cella = tab.cell(ri, ci)
                p = cella.paragraphs[0]
                p.style = "Libro Tabella Intestazione" if testa else "Libro Tabella"
                p.alignment = {"left": WD_ALIGN_PARAGRAPH.LEFT, "center": WD_ALIGN_PARAGRAPH.CENTER,
                               "right": WD_ALIGN_PARAGRAPH.RIGHT}[allinea[ci] if ci < len(allinea) else "left"]
                if testa:
                    sfondo_cella(cella, "EDE8E0")
                if ci < len(riga):
                    self.inline(p, riga[ci].children)
        self._spazio(target, 6)

    # ---------------- parti del libro ----------------
    def copertina(self, percorso):
        self.nuova_sezione(piede=None, formato="lowerRoman", riparti=1,
                           margini={"interno": 0, "esterno": 0, "superiore": 0, "inferiore": 0,
                                    "testatina": 0, "piede": 0})
        p = self.doc.paragraphs[0] if self.doc.paragraphs else self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        file = comune.RADICE / percorso if percorso else None
        if file and file.exists():
            pg = self.cfg["pagina"]
            # un soffio meno dell'altezza piena: evita che l'immagine spinga una pagina vuota
            p.add_run().add_picture(str(file), width=Cm(pg["larghezza_cm"]), height=Cm(pg["altezza_cm"] - 0.05))
        else:
            comune.avviso("copertina non ancora presente (sessione S3): segnaposto")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(250)
            self.testo(p, "[ COPERTINA — sessione S3 ]", bold=True, colore=stili.GRIGIO)

    def frontespizio(self):
        righe = self.meta.get("titolo_righe", [self.meta["titolo"]])
        self.nuova_sezione(piede=None, formato="lowerRoman", centra=True, firma=(righe[0], 30), recto=True)
        for k, riga in enumerate(righe):
            p = self.doc.add_paragraph(style="Libro Frontespizio Titolo")
            if k == 0:
                p.paragraph_format.space_before = Cm(6)  # LibreOffice ignora la centratura verticale
            for pezzo, speciale in segmenta(riga):
                r = p.add_run(pezzo)
                if speciale:
                    r.font.color.rgb = stili.ACCENTO
        p = self.doc.add_paragraph(style="Libro Frontespizio Autore")
        self.testo(p, self.meta["autore"])
        if self.meta.get("citazione_copertina"):
            p = self.doc.add_paragraph(style="Libro Citazione")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(30)
            self.testo(p, self.meta["citazione_copertina"])

    def pagina_semplice(self, percorso, stile, inizio=WD_SECTION.ODD_PAGE, centra=False):
        """Colophon, dedica: nessuna testatina, nessun numero, nessuna voce d'indice."""
        tokens = self.md.parse(percorso.read_text(encoding="utf-8"))
        # niente titolo visibile
        if tokens and tokens[0].type == "heading_open":
            tokens = tokens[3:]
        primo = next((t for t in tokens if t.type == "inline"), None)
        firma = (testo_piano(primo)[:30], self.doc.styles[stile].font.size.pt) if primo else None
        self.nuova_sezione(piede=None, formato="lowerRoman", centra=centra, firma=firma,
                           recto=(inizio == WD_SECTION.ODD_PAGE))
        n_prima = len(self.doc.paragraphs)
        self.a_capo = True
        self.blocchi(tokens, self.doc, stile)
        self.a_capo = False
        if centra and len(self.doc.paragraphs) > n_prima:
            self.doc.paragraphs[n_prima].paragraph_format.space_before = Cm(5)

    def indice_generale(self):
        self.nuova_sezione(piede="centrato", formato="lowerRoman", firma=("Indice", 24), recto=True)
        p = self.doc.add_paragraph(style="Libro Titolo Indice")
        p.add_run("Indice")
        self._segnaposto_indice = self.doc.add_paragraph(style="Normal")

    def capitolo(self, percorso, tipo, numero=None, preliminare=False):
        testo = percorso.read_text(encoding="utf-8")
        tokens = self.md.parse(testo)
        titolo_tok = None
        for k, t in enumerate(tokens):
            if t.type == "heading_open" and t.tag == "h1":
                titolo_tok = tokens[k + 1]
                tokens = tokens[:k] + tokens[k + 3:]
                break
        titolo = testo_piano(titolo_tok) if titolo_tok else percorso.stem
        if tipo == "capitolo":
            etichetta, self.etichetta = f"Capitolo {numero}", str(numero)
            voce_testo, intest = titolo, f"{numero} · {titolo}"
        elif tipo == "appendice":
            etichetta, self.etichetta = f"Appendice {numero}", str(numero)
            voce_testo, intest = titolo, f"Appendice {numero} · {titolo}"
        else:
            etichetta, self.etichetta = "", ""
            voce_testo, intest = titolo, titolo
        titolo_libro = self.meta["titolo"]
        riparti = None
        if not preliminare and self.primo_arabo:
            riparti, self.primo_arabo = 1, False
        self.nuova_sezione(formato="lowerRoman" if preliminare else "decimal", riparti=riparti,
                           testatina=(intest, titolo_libro), prima_diversa=True, firma=(titolo, 24), recto=True)
        self.n_fig = 0
        p_et = self.doc.add_paragraph(style="Libro Etichetta Capitolo")
        if etichetta:
            p_et.add_run(etichetta)
        p = self.doc.add_paragraph(style="Heading 1")
        if titolo_tok:
            self.inline(p, titolo_tok.children)
        else:
            p.add_run(titolo)
        self.voce_capitolo = self._voce(1, voce_testo, 24, etichetta=str(numero) if tipo == "capitolo"
                                        else (f"Appendice {numero}" if tipo == "appendice" else ""))
        self.voci[-1]["file"] = percorso.relative_to(comune.RADICE).as_posix()
        self.blocchi(tokens, self.doc)

    def parte(self, n, titolo, percorso):
        riparti = None
        if self.primo_arabo:
            riparti, self.primo_arabo = 1, False
        self.nuova_sezione(formato="decimal", riparti=riparti, piede=None, centra=True,
                           firma=(titolo, 30), recto=True)
        p = self.doc.add_paragraph(style="Libro Etichetta Parte")
        p.paragraph_format.space_before = Cm(5)  # LibreOffice ignora la centratura verticale
        p.add_run(f"Parte {ROMANI[n - 1]}")
        p = self.doc.add_paragraph(style="Titolo Parte")
        self.testo(p, titolo)
        if percorso and percorso.exists():
            tokens = self.md.parse(percorso.read_text(encoding="utf-8"))
            if tokens and tokens[0].type == "heading_open":
                tokens = tokens[3:]
            self.blocchi(tokens, self.doc, "Libro Introduzione Parte")
        self.voce_capitolo = self._voce(3, f"Parte {ROMANI[n - 1]} – {titolo}", 30, cerca=titolo)

    def crediti_immagini(self, lettera):
        self.nuova_sezione(testatina=(f"Appendice {lettera} · Crediti delle immagini", self.meta["titolo"]),
                           prima_diversa=True, firma=("Crediti delle immagini", 24), recto=True)
        self.etichetta, self.n_fig = lettera, 0
        p = self.doc.add_paragraph(style="Libro Etichetta Capitolo"); p.add_run(f"Appendice {lettera}")
        p = self.doc.add_paragraph(style="Heading 1"); p.add_run("Crediti delle immagini")
        self.voce_capitolo = self._voce(1, "Crediti delle immagini", 24, etichetta=f"Appendice {lettera}")
        p = self.doc.add_paragraph(style="Libro Corpo")
        p.add_run("Le illustrazioni senza indicazione di fonte sono originali, realizzate dall'autore per questo "
                  "libro. Per le altre si riportano autore e licenza.")
        esterne = []
        for f in self.figure:
            info = self.crediti.get(Path(f["src"]).as_posix())
            if info and not info["licenza"].lower().startswith("originale"):
                esterne.append((f, info))
        if not esterne:
            self.doc.add_paragraph(style="Libro Corpo").add_run("Nessuna immagine esterna.")
        for f, info in esterne:
            p = self.doc.add_paragraph(style="Libro Colophon")
            r = p.add_run(f"Figura {f['numero']}"); r.bold = True
            self.testo(p, f" – {info['autore']}. {info['licenza']}. Fonte: {info['fonte']}")
        mancanti = [f["src"] for f in self.figure if Path(f["src"]).as_posix() not in self.crediti]
        for m in mancanti:
            comune.avviso(f"figura senza voce in assets/CREDITI.md: {m}")

    def indice_analitico(self):
        self.nuova_sezione(testatina=("Indice analitico", self.meta["titolo"]), prima_diversa=True,
                           firma=("Indice analitico", 24), recto=True)
        p = self.doc.add_paragraph(style="Libro Etichetta Capitolo")
        p = self.doc.add_paragraph(style="Heading 1"); p.add_run("Indice analitico")
        self.voce_capitolo = self._voce(1, "Indice analitico", 24)
        # il contenuto (su due colonne) va in una sezione continua
        self.nuova_sezione(inizio=WD_SECTION.CONTINUOUS, testatina=("Indice analitico", self.meta["titolo"]),
                           colonne=2)
        self._segnaposto_analitico = self.doc.add_paragraph(style="Normal")

    def _leggi_crediti(self):
        crediti = {}
        f = comune.RADICE / "assets" / "CREDITI.md"
        if not f.exists():
            return crediti
        for riga in f.read_text(encoding="utf-8").splitlines():
            if not riga.startswith("| IMG") and not riga.startswith("| COVER"):
                continue
            celle = [c.strip() for c in riga.strip().strip("|").split("|")]
            if len(celle) >= 5:
                crediti[celle[1]] = {"id": celle[0], "fonte": celle[2], "autore": celle[3], "licenza": celle[4]}
        return crediti

    # ---------------- indici (riempiti alla fine) ----------------
    def _riempi_indice(self):
        if not hasattr(self, "_segnaposto_indice"):
            return
        ancora = self._segnaposto_indice
        livelli = self.cfg.get("indice_livelli", 2)
        voci = [v for v in self.voci if v["livello"] in (1, 3) or v["livello"] <= livelli]
        paragrafi = []
        for v in voci:
            stile = {1: "toc 1", 2: "toc 2", 3: "toc 3"}[v["livello"]]
            p = self.doc.add_paragraph(style=stile)
            if v["livello"] == 1 and v["etichetta"] and v["etichetta"].isdigit():
                r = p.add_run(f"{v['etichetta']}  "); r.font.color.rgb = stili.ACCENTO
            elif v["livello"] == 1 and v["etichetta"]:
                r = p.add_run(f"{v['etichetta']} · "); r.font.color.rgb = stili.ACCENTO
            self.testo(p, v["testo"])
            p.add_run("\t" + str(self.pagine.get("voci", {}).get(v["id"], "—")))
            paragrafi.append(p)
        if not paragrafi:
            return
        # campo TOC: inizio nel primo paragrafo, fine nell'ultimo (il risultato è già calcolato)
        primo, ultimo = paragrafi[0], paragrafi[-1]
        runs_inizio = []
        for tipo, testo in (("begin", None), (None, ' TOC \\o "1-2" \\u '), ("separate", None)):
            r = primo.add_run()
            if tipo:
                _fld(r, tipo)
            else:
                it = elemento("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = testo
                r._r.append(it)
            runs_inizio.append(r)
        ppr = primo._p.pPr
        for r in reversed(runs_inizio):
            r._r.getparent().remove(r._r)
            ppr.addnext(r._r)
        _fld(ultimo.add_run(), "end")
        for p in paragrafi:
            ancora._p.addprevious(p._p)
        ancora._p.getparent().remove(ancora._p)

    def _riempi_analitico(self):
        if not hasattr(self, "_segnaposto_analitico"):
            return
        ancora = self._segnaposto_analitico
        pagine_xe = self.pagine.get("xe", [])
        per_voce: dict[str, list] = {}
        for k, x in enumerate(self.xe):
            pg = pagine_xe[k] if k < len(pagine_xe) else "—"
            per_voce.setdefault(x["voce"], [])
            if pg not in per_voce[x["voce"]]:
                per_voce[x["voce"]].append(pg)
        lettera = None
        nuovi = []
        for voce in sorted(per_voce, key=lambda s: s.lower().lstrip("/.-_")):
            iniziale = voce.lstrip("/.-_")[:1].upper()
            if iniziale != lettera:
                lettera = iniziale
                p = self.doc.add_paragraph(style="Libro Indice Lettera"); p.add_run(lettera)
                nuovi.append(p)
            p = self.doc.add_paragraph(style="Libro Indice Analitico")
            self.testo(p, voce)
            p.add_run(", " + ", ".join(str(x) for x in per_voce[voce]))
            nuovi.append(p)
        if not nuovi:
            p = self.doc.add_paragraph(style="Libro Corpo"); p.add_run("(nessuna voce)")
            nuovi.append(p)
        for p in nuovi:
            ancora._p.addprevious(p._p)
        ancora._p.getparent().remove(ancora._p)

    # ---------------- orchestrazione ----------------
    def file_capitolo(self, voce: str) -> Path | None:
        p = Path(voce)
        cand = [comune.RADICE / p] if p.suffix == ".md" else [self.cartella / f"{voce}.md"]
        for c in cand:
            if c.exists():
                return c
        comune.avviso(f"sorgente non ancora scritto, saltato: {voce}")
        return None

    def costruisci(self) -> dict:
        cfg = self.cfg
        self.copertina(cfg.get("copertina"))
        for voce in cfg.get("preliminari", []):
            if voce == "frontespizio":
                self.frontespizio()
            elif voce == "indice":
                self.indice_generale()
            else:
                f = self.file_capitolo(voce)
                if not f:
                    continue
                if "colophon" in f.stem:
                    self.pagina_semplice(f, "Libro Colophon", inizio=WD_SECTION.NEW_PAGE)
                    # colophon in fondo alla pagina pari: si allinea in basso con spazio sopra
                elif "dedica" in f.stem:
                    self.pagina_semplice(f, "Libro Dedica", centra=True)
                else:
                    self.capitolo(f, "preliminare", preliminare=True)
        n_cap = 0
        for k, parte in enumerate(cfg.get("parti", []), start=1):
            apertura = comune.RADICE / parte["apertura"] if parte.get("apertura") else None
            self.parte(k, parte["titolo"], apertura)
            for slug in parte.get("capitoli", []):
                n_cap += 1
                f = self.file_capitolo(slug)
                if f:
                    self.capitolo(f, "capitolo", n_cap)
        lettera = 0
        for voce in cfg.get("appendici", []):
            if voce == "indice-analitico":
                self.indice_analitico()
            elif voce == "crediti":
                self.crediti_immagini("ABCDEFGHIJ"[lettera]); lettera += 1
            else:
                f = self.file_capitolo(voce)
                if f:
                    self.capitolo(f, "appendice", "ABCDEFGHIJ"[lettera])
                lettera += 1
        self._riempi_indice()
        self._riempi_analitico()
        self._metadati()
        return {"voci": self.voci, "xe": self.xe, "figure": self.figure, "sezioni": self.sezioni_reg,
                "fatti": sorted(set(self.marcatori_fatti))}

    def _metadati(self):
        cp = self.doc.core_properties
        cp.author = self.meta["autore"]
        cp.last_modified_by = self.meta["autore"]
        cp.title = self.meta["titolo"].replace("\n", " ")
        cp.subject = self.meta.get("soggetto", "")
        cp.keywords = ", ".join(self.meta.get("parole_chiave", []))
        cp.language = self.meta.get("lingua", "it-IT")
        cp.comments = self.meta.get("citazione_copertina", "")


def costruisci(cfg: dict, pagine: dict | None = None, destinazione: Path | None = None) -> tuple[Path, dict]:
    c = Costruttore(cfg, pagine)
    struttura = c.costruisci()
    comune.OUTPUT.mkdir(exist_ok=True)
    destinazione = destinazione or comune.OUTPUT / f"{comune.nome_output(cfg)}.docx"
    c.doc.save(destinazione)
    return destinazione, struttura


def main():
    comune.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--config", default="book.yaml")
    a = ap.parse_args()
    cfg = comune.carica_config(a.config)
    f_pagine = comune.OUTPUT / f"{comune.nome_output(cfg)}.pagine.json"
    pagine = json.loads(f_pagine.read_text(encoding="utf-8")) if f_pagine.exists() else None
    docx, struttura = costruisci(cfg, pagine)
    (comune.OUTPUT / f"{comune.nome_output(cfg)}.struttura.json").write_text(
        json.dumps(struttura, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✔ {docx.relative_to(comune.RADICE)}  ({len(struttura['voci'])} voci d'indice, "
          f"{len(struttura['figure'])} figure, {len(struttura['xe'])} voci analitiche)")


if __name__ == "__main__":
    main()
