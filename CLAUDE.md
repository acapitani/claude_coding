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

## Regole sulle immagini
- Ogni immagine sta in `assets/CREDITI.md` (id, file, fonte/URL, autore, licenza, uso) **prima** di essere inserita.
- Licenze ammesse: pubblico dominio, CC0, CC BY, CC BY-SA, unDraw. Licenza incerta = esclusa.
- Le figure generate hanno lo script sorgente in `assets/src/` o `build/figure/`.
- Formato: PNG 300 dpi, larghezza massima 13 cm, didascalia obbligatoria "Figura N.M – …".

## Cartelle e nomi
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
- Build:            `py build/build_book.py`
- Indici + PDF:     `py build/update_indexes.py`   (LibreOffice headless)
- Controlli:        `py build/check_book.py`       (pagine 160–200, metadati, crediti, fatti, TODO)
- Anteprime:        `py build/render_pages.py --sample 12`
- Una figura:       `py build/figure/<script>.py` oppure `node build/figure/render.mjs <file.html>`

## Checklist di fine capitolo
1. Lunghezza entro ±10% del budget di parole in PLAN.md §5.
2. Ogni fatto ha `<!-- F-NNN -->` e la voce esiste in FATTI.md.
3. Figure previste presenti, con didascalia e voce in CREDITI.md.
4. Almeno un box e il riepilogo "In breve"; nuovi termini nel glossario.
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
