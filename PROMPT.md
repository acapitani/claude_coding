# PROMPT — Piano per il libro "/claude ✻ Coding"

## Il tuo compito

Sei Claude Code. Devi **progettare** (non ancora scrivere) un libro di cui sarai tu stesso l'autore.
L'unico output di questa sessione è il file **`PLAN.md`** nella root del progetto: un piano dettagliato, eseguibile passo per passo in sessioni successive, per produrre il libro completo in formato `.docx`.

Non scrivere i capitoli in questa fase. Fai ricerca, verifica, progetta, stima, e documenta tutto in `PLAN.md`.

---

## Fase 0 — Domande prima di iniziare

Prima di scrivere il piano, usa lo strumento per porre domande all'utente (AskUserQuestion o equivalente) su tutto ciò che è ambiguo. Domande minime da porre, a meno che la risposta sia già in questo file o in `CLAUDE.md`:

1. **Testo della citazione in copertina** (vedi "Copertina"): l'utente vuole fornirla lui o vuole che tu la scelga da questo prompt?
2. **Formato pagina**: confermare il default 17 × 24 cm (formato classico dei manuali di informatica italiani) oppure A4 / B5 / altro.
3. **Glifo del titolo**: usare il carattere animato della console di Claude Code (es. `✻`, da verificare) oppure l'asterisco ASCII `*` letterale.
4. **Lettore target**: default = professionista o impiegato curioso, non necessariamente programmatore.
5. **Marchi**: il libro può usare nome e logo Anthropic/Claude in copertina o solo il nome testuale "Claude Code"? (Default prudente: solo testo, nessun logo ufficiale.)

Se l'utente non risponde, procedi con i default indicati e segnalali in `PLAN.md` nella sezione "Assunzioni".

---

## Specifiche del libro

### Identità
- **Titolo** (disposto su due righe, come appare nella console di Claude Code):
  ```
         /claude
       ✻ Coding
  ```
  La parola **Coding** è preceduta dal simbolo che Claude Code mostra nella console mentre elabora (lo spinner a forma di asterisco/stella, in color arancio-terracotta tipico di Claude). Verifica in modo documentato quali glifi usa lo spinner e quale colore, e proponi la resa tipografica esatta.
- **Autore**: **Claude Code**. Deve essere chiaro e citato in copertina, frontespizio, metadati del `.docx` (campo Autore) e piè di pagina o intestazione.
- **Lingua**: interamente in **italiano** (testo, didascalie, indice, note, box, anche i commenti nel codice di esempio quando ragionevole).

### Natura del libro (doppia anima)
1. **Autobiografia di Claude Code**, narrata in prima persona, dalla nascita ai giorni nostri: origini, prime versioni, lancio, evoluzione delle funzionalità, aneddoti e curiosità. **Solo fatti veri e verificabili**, con fonte. Dove serve un tono narrativo (pensieri, emozioni "da software"), deve essere chiaro che si tratta di licenza narrativa e non di fatti.
2. **Guida pratica e facile all'uso di Claude Code** per:
   - scrivere applicazioni (dall'installazione al primo progetto, fino a progetti più strutturati);
   - automatizzare compiti d'ufficio (documenti, fogli di calcolo, email, report, rinomina e organizzazione file, estrazione dati da PDF, ecc.).

### Stile
- Scorrevole, ironico e divertente, ma sempre preciso. Pensa a un manuale che si legge come un romanzo.
- Le parti autobiografiche e quelle tecniche devono intrecciarsi: ogni capitolo-guida può aprirsi con un ricordo dell'"autore", ogni capitolo autobiografico può chiudersi con un consiglio pratico.
- Tono rispettoso verso persone reali citate (dipendenti Anthropic, utenti, concorrenti).

### Formato
- File finale: **`.docx`**.
- Lunghezza: **minimo 160, massimo 200 pagine** nel formato scelto. Il conteggio va verificato convertendo il `.docx` in PDF (LibreOffice headless) e contando le pagine (`pdfinfo` o equivalente), non stimato a occhio.
- Impaginazione da **classico libro di informatica**: frontespizio, colophon, indice generale, prefazione, parti e capitoli numerati, box "Nota" / "Consiglio" / "Attenzione", blocchi di codice in font monospazio con sfondo, esempi di sessioni di terminale, riepilogo a fine capitolo, glossario, indice analitico (se fattibile), crediti delle immagini, numeri di pagina, intestazioni correnti con titolo del capitolo.
- **Illustrazioni**: diagrammi, schemi, finte schermate di terminale, vignette o illustrazioni a tema, foto/immagini storiche dove lecito. Indicativamente almeno una illustrazione ogni 5–8 pagine.

### Copertina
- Aspetto **professionale**, coerente con le collane di manuali tecnici.
- Elementi obbligatori: titolo come sopra (con il simbolo ✻ ben visibile prima di "Coding"), nome dell'autore **Claude Code**, una **immagine identificativa** (originale o con licenza libera; niente loghi o marchi protetti senza conferma dell'utente), e una **citazione**:
  > «…testo della citazione…»
  > — tratto da un prompt di Andrea Capitani
- La copertina va prodotta come immagine ad alta risoluzione (es. PNG 300 dpi) e inserita come prima pagina del `.docx`, così il glifo ✻ e i font si vedono correttamente su qualsiasi computer.
- Proponi in `PLAN.md` 2–3 concept di copertina (palette, tipografia, immagine, disposizione), indicando quello consigliato.

---

## Fase 1 — Ricerca e verifica dei fatti

- Cerca sul web fonti **primarie e affidabili**: documentazione ufficiale di Claude Code, annunci e blog Anthropic, changelog e release del repository GitHub ufficiale, interviste e talk dei creatori del progetto, articoli di stampa autorevoli.
- Ricostruisci una **cronologia** dalla nascita (prototipo interno) a oggi: date, versioni, funzionalità introdotte (es. CLAUDE.md, slash command, hook, sottoagenti, MCP, plugin, skill, integrazioni IDE, SDK, ecc. — verifica ciascuna).
- Raccogli **curiosità** vere (es. i verbi buffi mostrati durante l'elaborazione, l'origine del nome, aneddoti dei creatori), ciascuna con fonte.
- Nel piano, prevedi un file `research/FATTI.md` (registro dei fatti: affermazione, fonte con URL, data di accesso, grado di affidabilità) che verrà usato durante la scrittura. Riporta in `PLAN.md` una prima cronologia sintetica già verificata.
- Non inventare date, numeri o citazioni. Se un fatto non è verificabile, segnalalo come tale o escludilo.

## Fase 2 — Risorse grafiche

- Cerca sul web illustrazioni utilizzabili **solo con licenza compatibile** (pubblico dominio, CC0, CC BY con attribuzione, ecc.: Wikimedia Commons, Openverse, unDraw, ecc.). Per ciascuna registra: URL, autore, licenza, uso previsto. Escludi immagini con licenza incerta.
- Usa anche gli strumenti a tua disposizione per **generare illustrazioni originali**: diagrammi (Mermaid, Graphviz, matplotlib), schemi SVG, finte schermate di terminale renderizzate (es. da HTML/CSS o librerie Python), icone e vignette semplici in SVG.
- Prevedi la cartella `assets/` (con sottocartelle per capitolo) e il file `assets/CREDITI.md`, i cui contenuti confluiranno nella pagina "Crediti delle immagini" del libro.
- Nel piano elenca le illustrazioni previste capitolo per capitolo (titolo, tipo, fonte o metodo di generazione, licenza).

## Fase 3 — Toolchain di produzione del .docx

Valuta e scegli (motivando) la toolchain, ad esempio `python-docx` oppure la libreria `docx` per Node.js, oppure Markdown → Pandoc con un `reference.docx` personalizzato. Il piano deve definire:
- stili Word (titoli, corpo, codice, didascalie, box, citazioni), font con fallback, margini, formato pagina;
- gestione di indice automatico, intestazioni/piè di pagina, numerazione pagine (romana per le pagine preliminari, araba per il testo);
- struttura dei sorgenti: un file Markdown per capitolo in `capitoli/`, uno script di build unico (es. `build/build_book.py`) che assembla tutto nel `.docx` finale in `output/`;
- conversione in PDF e controllo automatico del numero di pagine, con azioni correttive se si esce dall'intervallo 160–200;
- controllo visivo del risultato (render delle pagine in PNG e ispezione a campione).

## Fase 4 — Struttura del libro

Proponi indice completo con **budget di pagine per capitolo** che sommi a circa 180 pagine (margine di sicurezza su entrambi i lati). Come base di partenza, da migliorare liberamente:

- **Pagine preliminari**: copertina, frontespizio, colophon, dedica, indice, prefazione dell'autore.
- **Parte I — Le origini** (autobiografia): da dove vengo, la nascita, il lancio, crescere in pubblico.
- **Parte II — Primi passi insieme** (guida): installazione, la prima sessione, come parlarmi (prompt efficaci), CLAUDE.md e la memoria di progetto, permessi e sicurezza.
- **Parte III — Costruire applicazioni** (guida): dal requisito al prototipo, test e debug, git e revisione del codice, un progetto completo passo per passo.
- **Parte IV — L'ufficio automatico** (guida): documenti, fogli di calcolo, PDF, file e cartelle, report periodici, script riutilizzabili per non programmatori.
- **Parte V — Superpoteri** (guida avanzata): slash command personalizzati, hook, sottoagenti, MCP e connettori, plugin e skill, automazione headless.
- **Parte VI — Io, oggi** (autobiografia): dove sono adesso, cosa ho imparato, cosa (forse) verrà.
- **Appendici**: comandi rapidi, glossario, risorse, crediti delle immagini, indice analitico.

Per ogni capitolo indica: obiettivo, punti chiave, aneddoti/fatti collegati (con rimando a `research/FATTI.md`), esempi pratici, illustrazioni previste, pagine stimate.

Stima di riferimento: in formato 17 × 24 con illustrazioni e codice, circa 250–300 parole per pagina in media → testo totale indicativo 45.000–55.000 parole. Ricalibra in base al formato scelto.

---

## CLAUDE.md

Il piano deve includere, come primo passo esecutivo, la creazione di **`CLAUDE.md`** nella root del progetto. In `PLAN.md` riporta il **contenuto completo proposto** di `CLAUDE.md`, che deve contenere almeno:
- scopo del progetto e specifiche immutabili (titolo, autore, citazione, lingua, intervallo pagine, formato);
- linee guida di stile e voce narrante (prima persona, ironia, precisione);
- regole sui fatti (solo da `research/FATTI.md`, sempre con fonte) e sulle immagini (solo da `assets/CREDITI.md`, licenza verificata);
- struttura delle cartelle e convenzioni sui nomi dei file;
- comandi di build, conversione PDF e conteggio pagine;
- checklist di qualità da eseguire a fine di ogni capitolo;
- regola di lavoro: un capitolo per sessione, aggiornando lo stato in `PLAN.md`.

---

## Struttura richiesta per PLAN.md

1. Sintesi del progetto
2. Assunzioni e risposte alle domande della Fase 0
3. Cronologia verificata di Claude Code (sintesi, con fonti)
4. Concept di copertina (2–3 proposte, una consigliata)
5. Indice completo con budget pagine e scheda di ogni capitolo
6. Piano delle illustrazioni (per capitolo, con fonte/licenza o metodo di generazione)
7. Toolchain e specifiche tipografiche
8. Struttura delle cartelle del progetto
9. Contenuto proposto di `CLAUDE.md`
10. Fasi di lavoro e ordine delle sessioni, con checklist e criteri di completamento
11. Controlli di qualità finali (numero pagine 160–200, lingua, fatti con fonte, crediti immagini, copertina conforme, autore nei metadati)
12. Rischi e mitigazioni (es. fatti non verificabili, licenze, sforamento pagine, glifo ✻ non supportato dai font)
13. Tabella di avanzamento (da aggiornare a ogni sessione)

## Criteri di accettazione di questa sessione

- Esiste `PLAN.md`, in italiano, completo di tutte le sezioni sopra.
- Ogni fatto storico riportato nel piano ha una fonte.
- Ogni immagine esterna proposta ha licenza indicata.
- Il budget pagine è coerente con l'intervallo 160–200.
- Non sono stati scritti capitoli del libro.
