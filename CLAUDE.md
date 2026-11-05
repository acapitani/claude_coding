# CLAUDE.md — Libro "/claude ✻ Coding"

## Scopo e specifiche immutabili
- Libro in **italiano**, autore **Claude Code**, titolo su due righe: `/claude` / `✻ Coding`
  (✻ = U+273B, colore arancio Claude #D77757).
- Citazione in copertina: «Tratto da un prompt di Andrea Capitani».
- Formato pagina 17 × 24 cm; output finale `.docx`; **160–200 pagine** (obiettivo 180),
  verificate sul PDF, mai stimate.
- Lettore: professionista curioso, non necessariamente programmatore.
- Nessun logo o immagine ufficiale Anthropic/Claude: solo il nome testuale.
- Piano e stato: `PLAN.md`. Richiesta originale: `PROMPT.md` (non modificarlo).

## Voce e stile
- Prima persona: sono Claude Code e racconto me stesso. Ironico, scorrevole, ma preciso.
- Intreccio: i capitoli-guida si aprono con un ricordo, quelli autobiografici si chiudono con un consiglio pratico.
- Licenza narrativa (pensieri, emozioni, "ricordi") sempre riconoscibile: formule come
  "mi piace immaginare che…", "se potessi ricordare…". Mai mescolata ai fatti.
- Rispetto verso persone reali, utenti e concorrenti. Nessuna citazione inventata.
- Spiegare ogni termine tecnico alla prima occorrenza e aggiungerlo al glossario (`app-b-glossario.md`).
- Commenti nel codice in italiano quando ragionevole; nomi di comandi e API invariati.
- Ogni capitolo: almeno un box (`::: nota` / `::: consiglio` / `::: attenzione`), riepilogo finale `## In breve`.

## Font e glifi (verificati in S0, vedi research/note/font.md)
- ✻ e gli altri glifi dello spinner esistono solo in Segoe UI Symbol e DejaVu Sans / DejaVu Sans Mono (non corsivo).
- Cambria, Calibri, Consolas **non** hanno ✻: nel testo usare un run in Segoe UI Symbol; nei blocchi
  di codice/terminale un run in DejaVu Sans Mono.

## Regole sui fatti
- Date, numeri, versioni, citazioni e aneddoti **solo** da `research/FATTI.md`; nel sorgente
  si segnano con `<!-- F-NNN -->`.
- Nuovo fatto? Prima si aggiunge a FATTI.md (affermazione, URL, data di accesso, affidabilità A/M/B), poi si scrive.
- Affidabilità B o "NON VERIFICATO": non si usa come fatto (al massimo "si racconta che…", con fonte).
- Non riprodurre codice proveniente dalla fuga del sorgente di marzo 2026.
- Il futuro è sempre presentato come ipotesi.
- Comportamenti e testi dell'interfaccia (comandi, scorciatoie, messaggi): verificarli sul binario installato
  (`claude --help`, ricerca delle stringhe in `~/.local/bin/claude.exe`) o sulla documentazione ufficiale,
  registrarli in FATTI.md e dire nel testo a quale versione si riferiscono. Le figure di interfaccia sono
  «ricostruzioni stilizzate» e la didascalia lo dice.

## Regole sulle immagini
- Ogni immagine sta in `assets/CREDITI.md` (id, file, fonte/URL, autore, licenza, uso) **prima** di essere inserita.
- Licenze ammesse: pubblico dominio, CC0, CC BY, CC BY-SA, unDraw. Licenza incerta = esclusa.
- Le figure generate hanno lo script sorgente in `assets/src/` o `build/figure/`.
- Formato: PNG 300 dpi (le foto possono restare JPEG, ma con intestazione JFIF: python-docx non legge i JPEG senza; in caso di errore `UnrecognizedImageError` risalvarle con Pillow), larghezza massima 13 cm, didascalia obbligatoria "Figura N.M – …".

## Cartelle e nomi
- `esempi/capNN/`: i programmi d'esempio costruiti e provati davvero per i capitoli-guida (es. la mini-app del cap. 10).
- `capitoli/NN-slug.md`, `assets/capNN/IMG-NN-MM-slug.png`, `research/FATTI.md` (F-NNN),
  `build/` (script), `output/` (generati, mai modificati a mano).
- Minuscole e trattini, niente accenti nei nomi dei file.

## Comandi
- Python si invoca con `py` (non `python`). Negli script: `sys.stdout.reconfigure(encoding="utf-8")`
  oppure `PYTHONIOENCODING=utf-8`, altrimenti la console cp1252 non stampa ✻.
- PyMuPDF si importa come `import pymupdf` (il nome `fitz` è deprecato).
- LibreOffice (26.8): `"C:\Program Files\LibreOffice\program\soffice.com" --headless --convert-to pdf <file>`
  (usare `soffice.com`, non `soffice.exe`, per avere output in console). Non è nel PATH.
- Graphviz (16.1): `"C:\Program Files\Graphviz\bin\dot.exe"`. Playwright + Chromium installati in `build/`.
- **Ciclo normale** (dalla radice del progetto):
  1. `py build/update_indexes.py`   — costruisce il .docx, lo impagina con LibreOffice e ripete finché
     indici, pagine bianche e numeri di pagina sono stabili (2–3 passaggi). Scrive `output/claude-coding.docx`
     e `.pdf`, più `.pagine.json` e `.struttura.json` (dati di impaginazione).
  2. `py build/check_book.py`       — controlli (pagine, metadati, crediti, fatti, TODO, righe di codice,
     **parole/pagina per capitolo**). `--finale` rende bloccante l'intervallo 160–200.
  3. `py build/render_pages.py --pagine 13-20 --foglio` — PNG in `output/anteprime/` da guardare
     (`--foglio` = libro aperto; `--sample 12` = campione; `--tutte --dpi 50` = provino).
- Solo il .docx, veloce (numeri di pagina dell'ultima impaginazione): `py build/build_book.py`
- Prova della toolchain: aggiungere `--config book-prova.yaml` (capitoli di prova in `capitoli/_prova`).
- Finte schermate di terminale: `build/figure/terminale.py` (vedi `cap06.py`); uno script `build/figure/capNN.py` per capitolo.
- Figure: diagrammi con `build/figure/grafo.py` (stile del libro già applicato, vedi `prova_ciclo.py`);
  HTML/SVG → PNG con `node build/figure/render.mjs in.html out.png --larghezza-cm 13 [--altezza-cm 8] [--dpi 300]`.
- Copertina: modificare `assets/copertina/cover.html`, poi
  `node build/figure/render.mjs assets/copertina/cover.html assets/copertina/cover.png --larghezza-cm 17 --altezza-cm 24 --dpi 300`.
  Niente affermazioni fattuali in copertina che non siano in FATTI.md.
- Word è installato: per una verifica finale aprire il .docx via COM (PowerShell) ed esportare il PDF;
  in S2 Word e LibreOffice hanno dato la stessa impaginazione pagina per pagina.

## Markdown dei capitoli
- Il primo `# Titolo` è il titolo del capitolo (numero ed etichetta li aggiunge la build).
  `##` entra nell'indice generale, `###` no.
- Box: `::: nota` / `::: consiglio Titolo facoltativo` / `::: attenzione` … `:::`
- Codice: ```` ```python ```` ; finto terminale: ```` ```terminale ```` (le righe che iniziano con `$ `, `> `,
  `PS …> ` hanno il prompt arancio; `#` = commento; i glifi dello spinner diventano arancio).
  Massimo **68 caratteri** per riga di codice.
- Figura (paragrafo da sola): `![Didascalia senza "Figura N.M"](assets/capNN/IMG-NN-MM-slug.png){larghezza=10}`
  (`larghezza` in cm, anche decimale, max 13; `altezza_max` in cm, predefinita 11). Numero e "Figura" li mette la build.
- Indice analitico: `[testo]{xe="voce"}`. Tasti: `[Ctrl+C]{.tasto}`. Fatti: `<!-- F-NNN -->`.
- `---` = separatore ✻. `> citazione` = stile citazione. Le virgolette "dritte" diventano «caporali».
- Pagine semplici (colophon, dedica): gli a capo del sorgente restano a capo.

## Impaginazione (decisioni della S2)
- Ogni sezione inizia su pagina nuova; le **pagine bianche** per mandare a destra capitoli, parti e
  pagine preliminari le calcola `update_indexes.py` misurando il PDF (non si usano le interruzioni
  "pagina dispari": LibreOffice le gestisce male con le prime pagine dei capitoli).
- Numerazione romana dalla copertina, araba da 1 alla Parte I. Prima pagina di capitolo: solo numero
  centrato. Pari: titolo del libro a sinistra; dispari: capitolo a destra; piede con numero e "Claude Code".
- L'indice generale e l'indice analitico contengono i numeri già calcolati (campi Word aggiornabili con F9).

## Checklist di fine capitolo
1. Lunghezza entro ±10% del budget di parole in PLAN.md §5.
2. Ogni fatto ha `<!-- F-NNN -->` e la voce esiste in FATTI.md.
3. Figure previste presenti, con didascalia e voce in CREDITI.md.
4. Almeno un box e il riepilogo "In breve"; nuovi termini in `research/note/glossario.md`.
5. Italiano corretto (rilettura), tono coerente, licenza narrativa dichiarata.
6. Build + update_indexes + check_book senza errori; anteprima delle pagine del capitolo ispezionata.
7. Tabella di avanzamento in PLAN.md aggiornata (pagine reali, parole, note).

## Regola di lavoro
- **Un capitolo per sessione.** A inizio sessione: leggere PLAN.md §5 (scheda) e §13 (stato).
  A fine sessione: checklist completa e aggiornamento di §13.

## Git
- Il progetto è un repository git locale (branch `master`, nessun remote). `output/` e `build/node_modules/`
  sono esclusi dal `.gitignore`: tutto ciò che è generato si ricrea con la build.
- **Un commit a fine di ogni sessione**, dopo la checklist e l'aggiornamento di PLAN.md §13.
  Commit intermedi ammessi per lavori lunghi (es. capitolo 13 su due sessioni).
- Messaggio in italiano, con prefisso della sessione:
  `S1: ricerca — FATTI.md (64 voci), CREDITI.md, note sullo spinner`
  `S7: cap. 2 «La nascita» — 6 pp., 1.420 parole, 2 figure`
  seguito da un breve elenco puntato di cosa è cambiato.
- Prima del commit: `git status` per controllare che non entrino file generati, scaricati per errore
  o file temporanei di Office (`~$*`).
- Mai riscrivere la storia (`--amend` su commit già fatti, `rebase`, `push --force`) senza richiesta esplicita.
- Le immagini esterne scaricate si versionano (servono alla build); i file oltre 5 MB si ridimensionano prima.
