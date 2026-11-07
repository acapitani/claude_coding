# Piano — Output di stampa Pixartprinting (`pixartprinting`)

**Specifica:** `_specs/spec-print.md` · **Modello di processo:** `spec-template.md`
**Tipo:** impaginazione · **Branch:** `pixartprinting` (da `master`, come richiesto; il modello dice `fb/<nome>`) · **Piano salvato in:** `_plans/pixartprinting.md` (fase 3)

## Contesto

Il libro esiste in digitale (`output/claude-coding.docx` / `.pdf`, 17 × 24 cm, 194 pp., `check_book --finale` OK).
Ora serve un esecutivo da caricare su Pixartprinting, con copertina distesa (fronte, dorso, retro) e logo dell'editore _kap.
Gli output digitali non devono cambiare.

### Cosa dicono template e istruzioni (`print-template/`, locale, non versionato)
| Voce | Valore misurato |
|---|---|
| Prodotto | Libro con copertina flessibile, **A5 14,8 × 21 cm**, brossura fresata (il template ha la pagina «inside cover») |
| File | **PDF unico**: istruzioni (da eliminare) → copertina esterna → copertina interna → 196 pagine interne. Ammessi anche due PDF separati (copertina / interno) |
| Interno | pagina 154 × 216 mm = 148 × 210 + **3 mm di abbondanza** per lato; area sicura a 5 mm dal taglio; consigliati testi a 15 mm dal lato interno e 10 mm dagli esterni |
| Copertina | 313,2 × 216 mm = 3 + 148 (4ª) + **11,2 dorso** + 148 (1ª) + 3; pieghe a x = 151,0 e 162,2 mm; area sicura a 5 mm |
| Copertina interna | per la fresata, dorso + 3 mm per lato **bianchi** (colla) |
| Colore | **CMYK Fogra 39** (l'RGB verrebbe convertito con un profilo standard) |
| Altro | 300 dpi; nessun crocino o segno di taglio; scala 1:1; nessuna password; font incorporati e non convertiti in curve; corpo minimo 6 pt; tracciati ≥ 0,25 pt; niente sovrastampa. Nessuna indicazione su ISBN o codice a barre, né sul verso del dorso |

### Decisioni prese con te (checkpoint 1, domande)
1. **Formato:** il PDF 17 × 24 si **riduce in A5** (fattore 148/170 = 0,8706). L'impaginazione resta quella verificata. Il corpo passa da 10,5 a 9,1 pt. Margini dopo la riduzione: interno 19,2 mm (≥ 15), esterno 15,7 mm (≥ 10).
2. **Pagine:** l'interno è di 192 pp. (le pp. 3–194 del PDF, senza copertina e relativo retro). Aggiungo **4 bianche finali** per arrivare alle **196** del preventivo; il dorso resta 11,2 mm. La parità si conserva: la prima pagina interna, il frontespizio, è di destra.
3. **Interno a colori**, convertito in CMYK Fogra 39, con il testo nero in solo K.
4. **Dorso** leggibile **dall'alto verso il basso**.
5. **Loghi:** mi mandi **versioni trasparenti** (SVG o PNG) in `_kaplogo/`. Quelle attuali hanno uno sfondo pieno. Finché non arrivano uso le attuali solo per le prove: il commit finale della copertina aspetta i file nuovi.
6. Logo **solo nella copertina di stampa**: la copertina digitale non cambia.
7. **Retro:** tre versioni del testo da scegliere al checkpoint 2.
8. **ISBN e codice a barre:** non li inserisco. Il template non li prevede e non me li hai forniti. Resta un punto aperto in PLAN.md.

### Problemi trovati nel PDF attuale (da correggere nella variante di stampa)
- **Testatine in maiuscoletto a 6,8 pt** (1.477 caratteri): ridotte all'87% diventano 5,9 pt, sotto il minimo di 6 pt.
- **Testo in #1F1E1D, non in nero puro** (249.000 caratteri): convertito in CMYK diventerebbe un nero in quadricromia, a rischio di problemi di registro a 9 pt.
- **Testatina a 1,0 cm dal bordo**: ridotta diventa 8,7 mm. È dentro l'area sicura (5 mm), ma sotto i 10 mm consigliati.
- Il resto è in regola. Le immagini sono tutte ≥ 300 dpi effettivi anche dopo la riduzione. Nell'interno **non ci sono elementi al vivo**: l'unico al vivo è la copertina.

## Approccio

Una **variante di stampa** del `.docx` serve solo a sistemare i problemi sopra. Il PDF 17 × 24 che ne esce viene ridotto in A5 con PyMuPDF, in modo vettoriale e senza toccare i font. La copertina è un **HTML parametrico** che si stampa in PDF vettoriale con Playwright. Ghostscript converte tutto in **CMYK Fogra 39**. Un controllo automatico di preflight produce un report e le anteprime.

### Passi (ognuno con il suo criterio di completamento)

1. **Prerequisiti**
   - Installare Ghostscript (`winget install ArtifexSoftware.GhostScript`) e aggiungere `GS` in `build/comune.py`, accanto a `SOFFICE`/`DOT`.
   - Scaricare il profilo Fogra 39 (ECI *ISOcoated_v2*, FOGRA39L, da eci.org) in `build/icc/`, aggiunta a `.gitignore` perché è un file di terzi.
   - *Fatto quando* `gswin64c -v` risponde e il profilo si apre.
2. **Parametri di stampa in `book.yaml`**
   - Nuova sezione `stampa:` con: formato rifilato, abbondanza, area sicura, margini consigliati, fascia per la colla, pagine del preventivo (196), dorso del template (11,2), spessore per foglio calibrato (11,2 / 98 = 0,11429 mm), profilo ICC, verso del dorso.
   - Nuova sezione `varianti: stampa:` con `output: claude-coding-stampa`, inchiostro `#000000`, testatina 9 pt (maiuscoletto 7,2 pt, cioè 6,3 pt dopo la riduzione) a 1,2 cm (10,4 mm dopo la riduzione).
   - Il dorso si calcola sempre come `pagine/2 × spessore_foglio`. Se il template locale c'è, il valore si confronta con le pieghe misurate nel template, e se le pagine non coincidono con il preventivo compare un avviso.
3. **Variante nella build**
   - `comune.carica_config(percorso, variante=None)` applica gli override della variante.
   - `stili.py` legge il colore dell'inchiostro dalla configurazione; oggi è la costante `INCHIOSTRO` usata in `font_stile`.
   - `build_book.py` legge dimensione e distanza della testatina dalla configurazione (`_testatina`, `header_distance` riga 212).
   - `update_indexes.py` e `build_book.py` accettano `--variante stampa`.
   - *Fatto quando* senza `--variante` il `.docx`/`.pdf` digitale resta identico (stesso testo pagina per pagina, 194 pp.) e la variante ha le stesse 194 pagine con le stesse etichette.
4. **Interno A5**, in `build/build_stampa.py`
   - Prende le pp. 3–194 della variante.
   - Mette ogni pagina, ridotta di 0,8706, su una pagina di 154 × 216 mm, centrata nel rifilo, con `show_pdf_page` di PyMuPDF (vettoriale).
   - Aggiunge 4 bianche e imposta TrimBox e BleedBox.
5. **Copertina**: `assets/copertina/cover-stampa.html` (sorgente versionato), parametrizzata via query string (dorso, misure, testo del retro scelto).
   - **Fronte:** riusa `cover.html` in un iframe ridotto, così il disegno non si duplica e la copertina digitale resta intatta. Il fondo prosegue nell'abbondanza. Il wordmark _kap va in basso a sinistra, in linea con «Claude Code», nella variante adatta al fondo scuro.
   - **Dorso:** «/claude ✻ Coding» · «Claude Code» · monogramma _kap al piede. Testo ruotato dall'alto verso il basso, almeno 1,5 mm dalle pieghe.
   - **Retro:** testo di 120–200 parole in prima persona: cos'è il libro, a chi serve, cosa insegna, e l'idea di Andrea Capitani di un pubblico non solo di programmatori. Poi il wordmark _kap. Le tre versioni stanno in `assets/copertina/retro.json`, ognuna con i suoi `F-NNN`, più il campo `scelta`.
   - **Copertina interna:** pagina bianca della stessa misura, senza stampa sulla 2ª e 3ª di copertina, come richiede la fresata.
   - Stampa con `render.mjs`, a cui si aggiunge un'opzione `--pdf` (Playwright `page.pdf`, misure in mm, `printBackground`).
6. **CMYK e assemblaggio**
   - Ghostscript `pdfwrite` con `-sColorConversionStrategy=CMYK`, `-sOutputICCProfile=<Fogra39>`, `-dBlackText` (testo nero puro → solo K), font incorporati, `/prepress`. Si punta a PDF/X-3 con OutputIntent Fogra 39; se Ghostscript non lo regge, PDF CMYK con OutputIntent, e lo dichiaro.
   - File in `output/stampa/`:
     - `claude-coding-stampa.pdf`: file unico nell'ordine del template, **quello da caricare**;
     - `copertina.pdf` e `interno.pdf`: alternativa a due file;
     - `preflight.txt` e `anteprime/`.
   - Comando unico: `py build/build_stampa.py`, che rifà anche l'impaginazione della variante.
7. **Preflight automatico**: `build/check_stampa.py`, eseguito anche da `build_stampa.py`. Solo PyMuPDF, più Ghostscript dove serve. Controlla:
   - misure di ogni pagina, e il confronto pagina per pagina con il template locale se c'è;
   - il calcolo del dorso, mostrato per intero;
   - font tutti incorporati, nessuno di tipo Type 3 o convertito in curve;
   - nessuno spazio colore RGB, OutputIntent presente;
   - immagini ≥ 300 dpi effettivi;
   - corpo minimo ≥ 6 pt e tracciati ≥ 0,25 pt;
   - testo dentro l'area sicura, con interno 15 mm ed esterno 10 mm come avvisi;
   - fascia della colla bianca;
   - nessuna cifratura e nessuna annotazione o crocino.
   - Anteprime PNG: copertina distesa con rifilo, abbondanza, area sicura, pieghe e fasce della colla sovrapposti. Pagine interne: frontespizio, apertura di capitolo, pagina con terminale, foto del cap. 1, ultima pagina bianca. Le tre versioni del retro.
8. **Testi del retro.** Scrivo tre versioni con taglio diverso, solo con fatti di FATTI.md, e le rileggo.

### Verifiche (fase 5)
- **Regressione:**
  - `py build/update_indexes.py` e `py build/check_book.py --finale`: 194 pp. e tutto verde;
  - `cover.png` invariata (hash);
  - testo del PDF digitale uguale a quello di prima, pagina per pagina.
- **Stampa:** `py build/build_stampa.py` e `preflight.txt` tutto verde. Il report riporta:
  - le misure misurate: interno 154,0 × 216,0 mm × 196, copertina 313,2 × 216,0 mm;
  - il calcolo del dorso: 98 fogli × 0,11429 = 11,2 mm;
  - font, colore, dpi e corpo minimo.
- **A occhio:** anteprime della copertina con le guide, alcune pagine interne al 100% per giudicare la leggibilità a 9,1 pt, loghi leggibili e non alterati.
- **Testi:** italiano, tono, citazione «Tratto da un prompt di Andrea Capitani» esatta; ogni fatto del retro presente in FATTI.md.

### Documentazione (fase 6)
- **CLAUDE.md:** sezione «Stampa»: formato A5 ottenuto per riduzione, vincoli Pixartprinting, regole sui loghi, comando, variante di stampa.
- **README.md:**
  - prerequisiti: Ghostscript e profilo ICC;
  - il comando `build_stampa.py`;
  - quale file caricare e dove scaricare il template;
  - fronte con logo nella tabella delle licenze (il logo resta escluso).
- **PLAN.md:** nuova riga in §13 e punti aperti: ISBN, loghi trasparenti, nuovo preventivo se cambiano le pagine.
- **assets/CREDITI.md:** voci per la copertina di stampa e per l'uso dei loghi _kap.
- **FATTI.md:** solo se il retro richiede fatti nuovi.
- **Glossario:** non serve.

### Commit sul branch `pixartprinting`
Uno per passo: piano → parametri e variante → interno A5 → copertina → CMYK e preflight → documentazione.
Al checkpoint 2: merge `--no-ff` su `master`, nuova build e nuove verifiche. Nessun push.

### Rischi
| Rischio | Mitigazione |
|---|---|
| Corpo a 9,1 pt più piccolo del previsto | Anteprima al 100% al checkpoint 2. Se non piace, l'alternativa è il preventivo 17 × 24 |
| Ghostscript rasterizza trasparenze e ombre della copertina | Appiattimento a ≥ 300 dpi; controllo nel preflight e a occhio |
| Licenza del profilo ICC | Resta locale e non versionato; il README dice dove scaricarlo |
| Il numero di pagine cambia in futuro | Il dorso si ricalcola; avviso di rifare il preventivo e scaricare il nuovo template |
| Loghi trasparenti in ritardo | La copertina si sviluppa con i PNG attuali; consegna bloccata finché non arrivano |
| Testatina spostata a 1,2 cm | Sta nel margine superiore di 2,0 cm e non cambia il corpo; lo verifico con lo stesso numero di pagine e le stesse etichette |

## Stato (2026-11-07)

Passi 1–8 completati sul branch `pixartprinting`. Preflight: 0 errori, 1 avviso.

### Scostamenti dal piano
- **Profilo colore:** il download ECI (*ISOcoated_v2*) non è più raggiungibile; si usa
  `Coated_Fogra39L_VIGC_300.icc` dal registro ICC (color.org): caratterizzazione FOGRA39, TAC 300%.
- **Ghostscript** non è su winget: installato dalle release firmate di Artifex (10.08.0).
- **Nero solo K:** `-dBlackText` di Ghostscript porta a nero *tutto* il testo (anche quello chiaro della
  copertina), quindi non si usa. Prima della conversione, nero e grigi neutri RGB dell'interno vengono
  riscritti come DeviceGray, che resta sulla sola lastra del nero.
- **Filetti delle tabelle:** 0,25 pt diventavano 0,218 pt dopo la riduzione; nella variante sono 0,375 pt.
- **cover.html:** con la modalità `?stampa=1` niente trama a righe (Chromium la rasterizzava a 22 dpi) e
  numeri dello spinner a 7 pt. Senza parametro la resa è identica pixel per pixel.
- **Avviso residuo:** le due sfumature di fondo della copertina, lisce e quasi impercettibili, sono
  rasterizzate da Chromium a 45 dpi.

### Punti aperti
- Retro: scelta la versione B «Il prompt» (campo `scelta` = 1 in `assets/copertina/retro.json`).
- ISBN e codice a barre: non previsti.
- Merge su `master` al checkpoint 2.
