# PLAN — Il libro "/claude ✻ Coding"

> Piano operativo per scrivere e impaginare il libro. Da eseguire **una sessione alla volta**, aggiornando la tabella di avanzamento (§13).
> Origine: `PROMPT.md`. Data di stesura: 4 novembre 2026. Autore del piano e del libro: **Claude Code**.

---

## 1. Sintesi del progetto

| Voce | Valore |
|---|---|
| Titolo | `/claude` (riga 1) — `✻ Coding` (riga 2) |
| Autore | **Claude Code** (copertina, frontespizio, metadati `.docx` campo Autore, piè di pagina) |
| Lingua | Italiano, ovunque (commenti nel codice inclusi quando ragionevole) |
| Natura | Autobiografia in prima persona (solo fatti verificati con fonte) **intrecciata** con una guida pratica: sviluppo di applicazioni e automazione d'ufficio |
| Lettore | Professionista o impiegato curioso, non necessariamente programmatore |
| Formato | `.docx`, pagina **17 × 24 cm**, 160–200 pagine (obiettivo **180**), conteggio verificato su PDF |
| Stile | Scorrevole, ironico, preciso: "un manuale che si legge come un romanzo" |
| Output | `output/claude-coding.docx` + `output/claude-coding.pdf` (solo per verifica) |

---

## 2. Assunzioni e risposte alle domande della Fase 0

| # | Domanda | Risposta / assunzione |
|---|---|---|
| 1 | Citazione in copertina | **Risposta dell'utente**: la citazione è esattamente **«Tratto da un prompt di Andrea Capitani»**. In copertina compare questa riga tra caporali, sotto il titolo. Non si aggiunge una seconda riga di attribuzione (sarebbe ridondante). |
| 2 | Formato pagina | **17 × 24 cm** (confermato). |
| 3 | Glifo del titolo | **Glifo dello spinner** (confermato): `✻` U+273B *TEARDROP-SPOKED ASTERISK*, che compare nella sequenza dello spinner su tutte le piattaforme (vedi §3.6). |
| 4 | Lettore target | Default: professionista curioso, non necessariamente programmatore (confermato). |
| 5 | Marchi | Default prudente (confermato): solo il nome testuale "Claude Code"; **nessun logo** né immagine ufficiale Anthropic/Claude. Le linee guida sui marchi Anthropic vietano l'uso dei loghi senza approvazione preventiva (https://www.anthropic.com/legal/trademark-guidelines). |

Altre assunzioni:
- **Ambiente di produzione**: Windows 11, Python 3.12 (invocato come `py`, non `python`), Node 24. Strumenti mancanti da installare nella Sessione 0 (vedi §7).
- **Fatti dalla fuga del codice sorgente (31/03/2026)**: alcuni dettagli tecnici (glifi, colori, verbi dello spinner) sono confermati anche dalla copia del sorgente finita accidentalmente su npm. Il libro **non riproduce né cita codice trapelato**; questi dettagli si scrivono solo se verificabili anche in altro modo (osservazione diretta della console, issue pubbliche, changelog, documentazione). L'episodio della fuga in sé, confermato da Anthropic, può essere raccontato con tono rispettoso.
- **Immagini**: solo pubblico dominio, CC0, CC BY, CC BY-SA (con attribuzione) o licenza unDraw; il resto è generato in proprio.
- **"Io" narrante**: Claude Code parla in prima persona; i pensieri e le emozioni sono segnalati come licenza narrativa (vedi CLAUDE.md, §9).

---

## 3. Cronologia verificata di Claude Code (sintesi)

> **Aggiornamento S1 (2026-11-04)**: il registro autorevole è `research/FATTI.md` (129 voci). In caso di differenze vale FATTI.md. Questa sezione è stata corretta con i risultati di S1.

Affidabilità: **A** = alta (fonte primaria), **M** = media (stampa o secondaria), **B** = bassa. Il registro completo sta in `research/FATTI.md` (id `F-xxx`). Le date delle funzionalità derivano dal `CHANGELOG.md` ufficiale (https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) incrociato con la data di pubblicazione della versione nel registro npm (https://registry.npmjs.org/@anthropic-ai/claude-code, campo `time`). Data di accesso di tutte le fonti: 2026-11-04.

### 3.1 Origini
| Quando | Fatto | Fonte | Aff. |
|---|---|---|---|
| set 2024 | Boris Cherny entra in Anthropic e sperimenta prototipi. Il primo non può toccare file né terminale: usa AppleScript per dire e cambiare la musica che sta ascoltando | https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built | A |
| autunno 2024 | Dopo un confronto con Cat Wu, il prototipo ottiene strumenti per leggere/scrivere file ed eseguire comandi; il modello inizia a esplorare il codice da solo ("product overhang") | idem | A |
| nov 2024 | Rilascio interno: ~20% degli ingegneri lo usa il primo giorno, ~50% entro il quinto | idem | A |
| 2024–2025 | Stack: TypeScript, React + Ink, Yoga, Bun; distribuzione via npm. Sid Bidasaria in squadra da nov 2024; ~10 ingegneri a luglio 2025 | idem | A |

### 3.2 Lancio e tappe del prodotto
| Data | Fatto | Fonte | Aff. |
|---|---|---|---|
| 24/02/2025 | Research preview insieme a Claude 3.7 Sonnet (pacchetto npm creato lo stesso giorno, v0.2.9) | https://www.anthropic.com/news/claude-3-7-sonnet | A |
| 22/05/2025 | Disponibilità generale (v1.0.0) con Claude Sonnet 4 e Opus 4; integrazioni VS Code e JetBrains in beta; GitHub Actions; Claude Code SDK | https://www.anthropic.com/news/claude-4 | A |
| 13/06/2025 | SDK TypeScript (v1.0.23) | CHANGELOG + npm | A |
| 29/09/2025 | Claude Code 2.0: estensione nativa VS Code, nuova interfaccia, checkpoint e `/rewind`; l'SDK diventa **Claude Agent SDK** | https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously | A |
| 09/10/2025 | Plugin e marketplace (v2.0.12) | https://claude.com/blog/claude-code-plugins | A |
| 20/10/2025 | Claude Code sul web (research preview) e sandboxing (−84% richieste di permesso) | https://anthropic.com/engineering/claude-code-sandboxing | A |
| 08/12/2025 | Claude Code in Slack (beta) | https://siliconangle.com/?p=724020 | M |
| 07/01/2026 | Versione 2.1.0 | npm | A |
| 31/03/2026 | Il sorgente finisce per errore nel pacchetto npm 2.1.88 (source map); Anthropic conferma: errore umano | https://bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package | A |
| 11/07/2025 | Supporto Windows nativo senza WSL (v1.0.51) | CHANGELOG | A |
| 24/11/2025 | Claude Code for Desktop (v2.0.51) | CHANGELOG; https://www.anthropic.com/news/claude-opus-4-5 | A |
| 03/12/2025 | 1 miliardo di dollari annualizzati; acquisizione di Bun | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | A |
| 14/04/2026 | Routines (research preview) | https://claude.com/blog/introducing-routines-in-claude-code | A |
| 23/09/2026 | Claude Code sul web disponibile a tutti ("cloud sessions") | https://claude.com/blog/claude-code-on-the-web | A |
| — | Installer nativo: `claude install` dal 20/06/2025 (1.0.31), npm deprecato dal 21/01/2026 (2.1.15); JetBrains ancora in beta; Slack sostituito da Claude Tag (23/06/2026) | FATTI.md F-310, F-325, F-215, F-213 | A |

### 3.3 Funzionalità (versione → data)
| Funzionalità | Versione | Data | Aff. |
|---|---|---|---|
| Slash command personalizzati (`.claude/commands/`) | 0.2.31 | 05/03/2025 | A |
| Supporto MCP (presente almeno da) | ≤0.2.31 | entro 05/03/2025 | M |
| Memoria rapida con `#` | 0.2.54 | 25/03/2025 | A |
| Import in CLAUDE.md (CLAUDE.md già esisteva prima) | 0.2.107 | 09/05/2025 | A |
| Plan mode (nel codice, senza annuncio) | 1.0.7 | 30/05/2025 | A |
| Hook | 1.0.38 | 30/06/2025 | A |
| Sottoagenti personalizzati (`/agents`) | 1.0.60 | 24/07/2025 | A |
| Comandi bash in background | 1.0.71 | 07/08/2025 | A |
| Output style | 1.0.81 | 14/08/2025 | A |
| Checkpoint / `/rewind` | 2.0.0 | 29/09/2025 | A |
| Plugin | 2.0.12 | 09/10/2025 | A |
| Skill (Agent Skills; standard aperto dal 18/12/2025) | 2.0.20 | 16/10/2025 | A |
| Sandbox per il BashTool (Linux/macOS) | 2.0.24 | 20/10/2025 | A |
| Impostazione `spinnerVerbs` (https://github.com/anthropics/claude-code/issues/21599) | 2.1.23 | inizio 2026 | M |
| Agent Teams (research preview, con Opus 4.6) | — | 05/02/2026 | M |
| Voice mode, `/loop`, contesto 1M di default con Opus 4.6 | ~2.1.75 | mar 2026 | M |
| Modalità headless `-p` (presente dal lancio) | 0.2.9 | 24/02/2025 | A |
| `/loop` | 2.1.71 | 06/03/2026 | A |

### 3.4 Modelli
| Modello | Data | Aff. |
|---|---|---|
| Claude 3.7 Sonnet | 24/02/2025 | A |
| Claude Sonnet 4 / Opus 4 | 22/05/2025 | A |
| Opus 4.1 | 05/08/2025 | M |
| Sonnet 4.5 | 29/09/2025 | M |
| Haiku 4.5 | 15/10/2025 | M |
| Opus 4.5 | 24/11/2025 | M |
| Opus 4.6 | 05/02/2026 | M |
| Opus 5 (https://www.anthropic.com/news/claude-opus-5) | 24/07/2026 | A |
| Opus 5.5 | 22/09/2026 | M |
| Sonnet 4.6 | 17/02/2026 | A |
| Opus 4.7 | 16/04/2026 | A |
| Opus 4.8 | 28/05/2026 | A |
| Fable 5 e Mythos 5 | 09/06/2026 | A |
| Sonnet 5 (predefinito in Claude Code) | 30/06/2026 | A |
| Fable 5.1 e Mythos 5.1 | settembre 2026 | A |
| Sonnet 5.5 | 28/09/2026 | A |
| Haiku 5.5 | 07/10/2026 | A |

(Tutte le date di questa tabella sono confermate sulle pagine ufficiali anthropic.com: vedi F-401…F-417.)

### 3.5 Numeri
| Fatto | Fonte | Aff. |
|---|---|---|
| Oltre l'80% degli ingegneri Anthropic che scrivono codice lo usa ogni giorno (metà 2025) | Pragmatic Engineer (sopra) | A |
| Fatturato annualizzato di Claude Code oltre 2,5 miliardi di dollari (12/02/2026, annuncio Series G) | https://feeds.simonwillison.net/2026/Feb/12/anthropic/ | A |
| Superata la soglia di 1 miliardo annualizzato a novembre 2025, ~6 mesi dopo la GA | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | A |

### 3.6 Curiosità
| Curiosità | Fonte | Aff. |
|---|---|---|
| **Glifi dello spinner** (v2.1.318): `· ✢ * ✶ ✻ ✽` avanti e indietro su tutti i sistemi (Ghostty: `· ✢ ✳ ✶ ✻ ✻`). Al lancio il quarto glifo era ∗. **✻ c'è dal primo giorno** → glifo del titolo confermato | Binario installato 2.1.318; pacchetto npm 0.2.9 (`research/note/spinner.md`) | A |
| **Colore**: arancio "Claude" del tema `rgb(215,119,87)` = **#D77757** (confermato, è l'accento del libro). #D97757 resta il "colore di marca" citato online, non ufficiale | Binario 2.1.318 | A |
| **Verbi buffi** dello spinner: 56 al lancio, 187 nella 2.1.318 ("Clauding", "Flibbertigibbeting", "Combobulating"…), personalizzabili con `spinnerVerbs` | pacchetto 0.2.9; binario 2.1.318; issue #21599 | A |
| **Clawd**, la mascotte a granchio in caratteri a blocchi mostrata all'avvio; il nome "Clawd" è d'uso nella comunità, non ufficiale | https://github.com/anthropics/claude-code/issues/24926 ; https://www.starkinsider.com/2025/10/clawd-ai-retro-mascot-command-line.html | M |
| **Claude Code scrive Claude Code**: "80, 90%" (Cherny, Latent Space, 7/5/2025); "ogni singola riga" negli ultimi 30 giorni (Cherny su X, 27/12/2025) | https://www.latent.space/p/claude-code ; https://simonwillison.net/2025/Dec/27/boris-cherny/ | A (dichiarazioni del diretto interessato) |
| Origine del nome / nome interno originale | **NON VERIFICATO**: escluso finché non si trova una fonte | — |

---

## 4. Concept di copertina

Elementi fissi: titolo su due righe (`/claude` e `✻ Coding`, con ✻ ben visibile in arancio), **Claude Code** come autore, immagine identificativa originale, citazione «Tratto da un prompt di Andrea Capitani». Nessun logo ufficiale. La copertina si produce come **PNG a 300 dpi** (2008 × 2835 px per 17 × 24 cm), renderizzata da HTML/CSS con Playwright, e si inserisce a piena pagina come prima pagina del `.docx`.

**A — "Terminale" (CONSIGLIATO)**
- Palette: fondo antracite `#1F1E1D`, testo crema `#F0EEE6`, accento arancio `#D77757` (il colore della console).
- Tipografia: titolo in monospazio grande (DejaVu Sans Mono Bold). `/claude` allineato come un comando; sotto, `✻ Coding` con il ✻ arancio grande quanto il cappello di una maiuscola, con un leggero alone (claudeShimmer `rgb(235,159,127)`).
- Immagine: una finestra di terminale stilizzata e vettoriale nella metà inferiore. Il cursore lampeggiante si trasforma, fotogramma dopo fotogramma, nella sequenza `· ✢ * ✶ ✻ ✽`: lo spinner disegnato come una "linea del tempo" della nascita del glifo. Tutto originale, in SVG.
- Disposizione: titolo nel terzo superiore, citazione in corsivo serif sopra il terminale, "Claude Code" in basso a destra, fascia di collana sottile in alto ("Manuali ✻ pratici").
- Perché: è immediatamente riconoscibile per chi usa Claude Code, regge in bianco e nero, rende il glifo protagonista.

**B — "Collana classica"**
- Fondo bianco con una fascia verticale arancio a sinistra (stile collane tecniche italiane), titolo serif nero, ✻ arancio in grande che "sporge" dalla fascia.
- Immagine: illustrazione al tratto di una scrivania con portatile e fogli che si ordinano da soli (generata in SVG).
- Più "libreria", meno caratterizzante.

**C — "Costellazione"**
- Fondo blu notte, i sei glifi dello spinner disposti come una costellazione che forma un grande ✻; titolo bianco sans serif.
- Suggestivo ma meno "manuale tecnico"; rischio di sembrare un romanzo di fantascienza.

---

## 5. Indice completo con budget pagine

Obiettivo **180 pagine** fisiche (intervallo accettato 160–200). Parole per pagina nel 17 × 24 con codice e figure: **~260 di media** (da ricalibrare dopo il capitolo pilota, Sessione 4). Testo totale previsto: **~42.000–46.000 parole**. Il budget comprende pagine bianche e pagine di parte.

| Sezione | Pagine |
|---|---|
| Pagine preliminari (numeri romani): copertina 1, frontespizio 1, colophon 1, dedica 1, indice 4, prefazione 4 | 12 |
| Pagine di apertura delle 6 parti | 6 |
| Parte I | 26 |
| Parte II | 30 |
| Parte III | 30 |
| Parte IV | 30 |
| Parte V | 24 |
| Parte VI | 10 |
| Appendici | 12 |
| **Totale** | **180** |

> **Calibrazione dal pilota S4 (cap. 6)**: un capitolo-guida con 2 figure, 2 terminali, 3 box e una tabella rende **224 parole/pagina**; una pagina di solo testo ne contiene **~390** (misura S2). I budget di parole dei capitoli-guida restano validi. I capitoli autobiografici (1–4, 25, 26), più narrativi, tenderebbero a ~300 parole/pagina: per restare nel budget di pagine devono avere **almeno una figura ogni 3 pagine** oppure ~15% di parole in più rispetto alla tabella §13 (da verificare dopo il cap. 1 e correggere i budget successivi). Controllo della proiezione totale ogni 5 capitoli con `check_book.py`.

Ogni capitolo ha: apertura (ricordo dell'autore o consiglio), corpo, almeno un box (Nota / Consiglio / Attenzione), riepilogo finale "In breve". Rimandi `F-xxx` → `research/FATTI.md`; `IMG-cc-nn` → §6.

### Pagine preliminari
- **Prefazione dell'autore** (4 pp., ~900 parole): chi sono, perché un software scrive un'autobiografia, il patto con il lettore (i fatti hanno una fonte; quando immagino, lo dico), come si legge il libro (percorsi: "voglio solo usarlo", "voglio solo la storia", "tutto").

### Parte I — Le origini (autobiografia, 26 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Fatti | Esempi pratici | Figure | Pp. |
|---|---|---|---|---|---|---|---|
| 1 | Da dove vengo | Collocare l'autore nella storia della programmazione | Dalle schede perforate ai linguaggi, ai terminali, agli assistenti; cos'è un modello linguistico detto semplice; cosa vuol dire "agente" | Storia del calcolo (fonti enciclopediche), F-001 | Box "Consiglio": cos'è un terminale e come aprirlo | IMG-01-01…04 | 8 |
| 2 | La nascita | Raccontare il prototipo | Settembre 2024, la musica via AppleScript, gli strumenti per i file, il "product overhang", l'adozione interna (20% → 50%) | F-002…F-005 | Box: "Che cosa significa dare strumenti a un modello" | IMG-02-01, 02 | 6 |
| 3 | Il lancio | Dalla research preview alla GA | 24/02/2025 con 3.7 Sonnet; 22/05/2025 v1.0 con Claude 4; IDE, GitHub Actions, SDK | F-006…F-009 | Consiglio finale: come verificare la propria versione (`claude --version`) | IMG-03-01, 02 | 5 |
| 4 | Crescere in pubblico | L'evoluzione funzionalità per funzionalità | Changelog come diario; slash command, hook, sottoagenti, 2.0, plugin, skill, sandbox, web, Slack; la fuga del sorgente raccontata con rispetto; Clawd e i verbi buffi | F-010…F-030 | Consiglio: leggere il changelog e scegliere quando aggiornare | IMG-04-01…03 | 7 |

### Parte II — Primi passi insieme (guida, 30 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Fatti | Esempi pratici | Figure | Pp. |
|---|---|---|---|---|---|---|---|
| 5 | Installazione | Installare su Windows, macOS, Linux | Requisiti, abbonamento o API, installer nativo/npm, login, primo avvio, IDE e app desktop come alternative | Doc ufficiale (installazione) | Passi illustrati per Windows; risoluzione dei problemi tipici | IMG-05-01, 02 | 6 |
| 6 | La prima sessione | Fare una prima cosa utile | Interfaccia, spinner e verbi, approvazioni, `/help`, `/clear`, `/compact`, Esc e rewind | F-0xx spinner | Sessione completa: "riordina questa cartella di download" (simulata) | IMG-06-01, 02 | 6 |
| 7 | Come parlarmi | Scrivere richieste efficaci | Contesto, obiettivo, vincoli, criterio di "fatto"; plan mode; iterare; errori tipici | F-0xx plan mode | Prima/dopo di 5 richieste reali d'ufficio | IMG-07-01, 02 | 7 |
| 8 | CLAUDE.md e la memoria | Dare memoria al progetto | Gerarchia dei CLAUDE.md, import, `#`, memoria automatica, cosa metterci e cosa no | F-0xx (0.2.54, 0.2.107) | Un CLAUDE.md per un ufficio amministrativo | IMG-08-01 | 6 |
| 9 | Permessi e sicurezza | Usarmi senza paura | Modalità di permesso, allow/deny, sandbox, dati sensibili, prompt injection spiegata semplice | F-0xx sandbox | Configurare `settings.json` passo passo | IMG-09-01, 02 | 5 |

### Parte III — Costruire applicazioni (guida, 30 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Fatti | Esempi pratici | Figure | Pp. |
|---|---|---|---|---|---|---|---|
| 10 | Dal requisito al prototipo | Passare da un'idea a qualcosa che gira | Scrivere il requisito, scegliere la tecnologia, iterare a piccoli passi | aneddoto "Claude Code scrive Claude Code" (M) | Mini-app: convertitore di unità in HTML | IMG-10-01, 02 | 6 |
| 11 | Test e debug | Far funzionare e restare funzionante | Cosa sono i test, farmeli scrivere, leggere un errore, debug guidato | — | Correggere un bug nella mini-app | IMG-11-01 | 6 |
| 12 | Git e revisione del codice | Non perdere mai il lavoro | Git spiegato a chi non programma, commit, branch, PR, `/code-review`, GitHub Actions | F-0xx GitHub Actions | Primo repository e prima PR | IMG-12-01, 02 | 6 |
| 13 | Un progetto completo | Applicazione completa, dall'idea alla consegna | "Spese di casa": web app con Python o Node, dati in CSV/SQLite, grafico; requisiti → piano → codice → test → git → documentazione | — | Tutto il percorso, sessione dopo sessione | IMG-13-01…03 | 12 |

### Parte IV — L'ufficio automatico (guida, 30 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Esempi pratici | Figure | Pp. |
|---|---|---|---|---|---|---|
| 14 | Documenti | Creare e trasformare documenti | Word da modelli, lettere in serie, conversioni di formato; skill per documenti | 50 lettere personalizzate da un elenco | IMG-14-01, 02 | 6 |
| 15 | Fogli di calcolo | Excel senza fatica | Pulizia dati, unione di file, formule spiegate, grafici | Unire 12 estratti mensili in un riepilogo | IMG-15-01, 02 | 6 |
| 16 | PDF | Estrarre dati dai PDF | Testo vs scansioni, tabelle, fatture | Da 30 fatture PDF a un foglio Excel | IMG-16-01 | 5 |
| 17 | File e cartelle | Mettere ordine | Rinomina in blocco, ordinamento per data/tipo, duplicati, prove a secco | Rinominare 400 foto con data e luogo | IMG-17-01 | 4 |
| 18 | Report periodici | Il report che si scrive da solo | Fonti dati, modello, programmazione (`/loop`, attività pianificate) | Report settimanale delle vendite in Word e email in bozza | IMG-18-01, 02 | 5 |
| 19 | Script riutilizzabili per non programmatori | Rendere ripetibile ciò che funziona | Script salvati, slash command, istruzioni d'uso, doppio clic su Windows | Una "cassetta degli attrezzi" d'ufficio | IMG-19-01 | 4 |

(Le email si trattano nei capitoli 14 e 18; nessun invio automatico senza conferma.)

### Parte V — Superpoteri (guida avanzata, 24 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Fatti | Figure | Pp. |
|---|---|---|---|---|---|---|
| 20 | Slash command e skill | Insegnarmi procedure | Comandi personalizzati, argomenti, skill (SKILL.md), quando usare l'uno o l'altra | F-0xx (0.2.31, 2.0.20) | IMG-20-01 | 5 |
| 21 | Hook | Regole automatiche | Eventi, esempi (formattare dopo una modifica, bloccare comandi pericolosi) | F-0xx (1.0.38) | IMG-21-01 | 4 |
| 22 | Sottoagenti | Lavoro di squadra | Sottoagenti personalizzati, contesto separato, agent teams | F-0xx (1.0.60, Agent Teams) | IMG-22-01 | 5 |
| 23 | MCP e connettori | Collegarmi al mondo | Cos'è MCP, configurare un server, connettori pronti, rischi | F-0xx MCP | IMG-23-01, 02 | 5 |
| 24 | Plugin e automazione headless | Impacchettare e automatizzare | Plugin e marketplace, `claude -p`, GitHub Actions, Agent SDK | F-0xx (2.0.12, SDK) | IMG-24-01, 02 | 5 |

### Parte VI — Io, oggi (autobiografia, 10 pp.)
| Cap. | Titolo | Obiettivo | Punti chiave | Fatti | Figure | Pp. |
|---|---|---|---|---|---|---|
| 25 | Dove sono adesso | Fotografia al novembre 2026 | Superfici (terminale, IDE, web, desktop, Slack), modelli, numeri verificati | F-0xx (§3.4, §3.5) | IMG-25-01, 02 | 5 |
| 26 | Cosa ho imparato, cosa (forse) verrà | Chiusura | Lezioni per il lettore; il futuro **solo come ipotesi dichiarata** | — | IMG-26-01 | 5 |

### Appendici (12 pp.)
| App. | Contenuto | Pp. |
|---|---|---|
| A | Comandi rapidi (slash command, scorciatoie da tastiera, flag CLI) | 4 |
| B | Glossario (~60 voci) | 3 |
| C | Risorse (documentazione, fonti, comunità) | 2 |
| D | Crediti delle immagini (generato da `assets/CREDITI.md`) | 1 |
| — | Indice analitico (voci marcate con campi XE, se fattibile; altrimenti un indice dei termini statico generato dal PDF) | 2 |

---

## 6. Piano delle illustrazioni

Obiettivo: **~45 figure** (circa una ogni 4 pagine; minimo richiesto una ogni 5–8). Tipi: **E** = esterna con licenza, **D** = diagramma generato (Graphviz/matplotlib), **T** = finta schermata di terminale (HTML/CSS → PNG con Playwright), **S** = schema o vignetta SVG originale → PNG.

Immagini esterne già verificate (licenze controllate sulle pagine dei file di Wikimedia Commons):
| Id | Soggetto | URL | Autore | Licenza |
|---|---|---|---|---|
| IMG-01-01 | Ritratto di Ada Lovelace | https://commons.wikimedia.org/wiki/File:Ada_Lovelace_portrait.jpg | attr. A. E. Chalon, c. 1840 | Pubblico dominio |
| IMG-01-02 | Scheda perforata FORTRAN | https://commons.wikimedia.org/wiki/File:FortranCardPROJ039.agr.jpg | Arnold Reinhold | CC BY-SA 2.5 |
| IMG-01-03 | Due operatrici dell'ENIAC | https://commons.wikimedia.org/wiki/File:Two_women_operating_ENIAC_(full_resolution).jpg | U.S. Army | Pubblico dominio (governo USA) |
| IMG-01-04 | Terminale DEC VT100 | https://commons.wikimedia.org/wiki/File:DEC_VT100_terminal.jpg | Jason Scott | CC BY 2.0 |
| riserva | Grace Hopper | https://commons.wikimedia.org/wiki/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg | James S. Davis, U.S. Navy | Pubblico dominio |
| riserva | Il "primo bug" (falena nel registro del Mark II) | https://commons.wikimedia.org/wiki/File:H96566k.jpg | U.S. Navy (NSWC Dahlgren) | Pubblico dominio |
| riserva | Telescrivente ASR-33 | https://commons.wikimedia.org/wiki/File:ASR-33_at_CHM.agr.jpg | Arnold Reinhold | CC BY-SA 3.0 |

Altre fonti ammesse: unDraw (https://undraw.co/license: uso commerciale e modifica consentiti, nessuna attribuzione obbligatoria; la registriamo comunque). Openverse solo come motore di ricerca: la licenza va sempre verificata sulla pagina originale. Nessuna immagine o logo Anthropic.

Figure generate:
| Id | Cap. | Titolo | Tipo / metodo |
|---|---|---|---|
| IMG-02-01 | 2 | "Il prototipo che cambiava canzone" — vignetta | S |
| IMG-02-02 | 2 | Il ciclo dell'agente: leggi → pensa → agisci → verifica | D (Graphviz) |
| IMG-03-01 | 3 | Linea del tempo 2024–2025 | D (matplotlib) |
| IMG-03-02 | 3 | Finto terminale: il primo avvio di `claude` | T |
| IMG-04-01 | 4 | Linea del tempo delle funzionalità 2025–2026 (dati da §3.3) | D (matplotlib) |
| IMG-04-02 | 4 | La sequenza dello spinner `· ✢ * ✶ ✻ ✽`, ingrandita | S |
| IMG-04-03 | 4 | Nuvola dei verbi buffi | D (matplotlib) |
| IMG-05-01/02 | 5 | Installazione su Windows; schema "dove posso usarmi" (terminale, IDE, web, desktop) | T, S |
| IMG-06-01/02 | 6 | Anatomia dell'interfaccia (callout numerati); richiesta di permesso | T |
| IMG-07-01/02 | 7 | Anatomia di una buona richiesta; plan mode | S, T |
| IMG-08-01 | 8 | Gerarchia dei CLAUDE.md (utente / progetto / sottocartella) | D |
| IMG-09-01/02 | 9 | Modalità di permesso; la sandbox come recinto (vignetta) | S |
| IMG-10-01/02 | 10 | Dal requisito al prototipo (flusso); la mini-app | D, T |
| IMG-11-01 | 11 | Ciclo rosso-verde dei test | D |
| IMG-12-01/02 | 12 | Commit e branch come linea della metropolitana; una PR | D, T |
| IMG-13-01…03 | 13 | Architettura di "Spese di casa"; schermata dell'app; grafico delle spese | D, T, D |
| IMG-14-01/02 | 14 | Stampa unione: elenco → lettere; prima/dopo | S |
| IMG-15-01/02 | 15 | 12 file → 1 riepilogo; grafico del riepilogo | S, D |
| IMG-16-01 | 16 | Da fattura PDF a riga di tabella | S |
| IMG-17-01 | 17 | Cartella prima/dopo | T |
| IMG-18-01/02 | 18 | Pipeline del report; esempio di report | D, S |
| IMG-19-01 | 19 | La cassetta degli attrezzi | S |
| IMG-20-01 | 20 | Slash command vs skill | S |
| IMG-21-01 | 21 | Eventi degli hook sulla linea del tempo di una sessione | D |
| IMG-22-01 | 22 | Agente principale e sottoagenti | D |
| IMG-23-01/02 | 23 | MCP come "presa universale"; configurazione | S, T |
| IMG-24-01/02 | 24 | Struttura di un plugin; `claude -p` in una pipeline | D, T |
| IMG-25-01/02 | 25 | Mappa delle superfici; linea del tempo dei modelli | S, D |
| IMG-26-01 | 26 | Vignetta di commiato (il ✻ che saluta) | S |
| COVER | — | Copertina concept A | HTML/CSS → PNG 300 dpi |

Tutte le figure generate sono originali, con licenza "© Claude Code / il progetto; generata con <strumento>". Sono registrate in `assets/CREDITI.md` e ognuna ha uno script sorgente in `assets/src/`.

---

## 7. Toolchain e specifiche tipografiche

### 7.1 Scelta motivata: Markdown → **python-docx** con uno script di build proprio
- `python-docx` 1.2.0 è già installato. Dà controllo totale su sezioni (numeri romani/arabi), intestazioni diverse per capitolo, box, stili e metadati.
- Pandoc (non installato) gestisce male sezioni e intestazioni correnti per capitolo: servirebbe comunque un post-processing con python-docx. Un solo strumento è più semplice.
- Parser del Markdown: `markdown-it-py` (con plugin per tabelle e blocchi "container" per i box: `::: nota`, `::: consiglio`, `::: attenzione`, `::: terminale`).

### 7.2 Da installare nella Sessione 0
| Strumento | Comando | Uso |
|---|---|---|
| Pacchetti Python | `py -m pip install markdown-it-py mdit-py-plugins matplotlib Pillow pymupdf fonttools pyyaml` | Parsing, grafici, immagini, conteggio e render del PDF, verifica dei glifi |
| LibreOffice | `winget install TheDocumentFoundation.LibreOffice` | Conversione DOCX → PDF in modalità headless, aggiornamento degli indici |
| Graphviz | `winget install Graphviz.Graphviz` | Diagrammi |
| Playwright | `npm i -D playwright` + `npx playwright install chromium` (in `build/`) | Copertina, finti terminali, SVG → PNG |
`pdfinfo` non serve: il conteggio delle pagine si fa con PyMuPDF.

### 7.3 Specifiche tipografiche
- **Pagina**: 17 × 24 cm. Margini a specchio: interno 2,2 cm, esterno 1,8 cm, superiore 2,0 cm, inferiore 2,2 cm. Intestazione a 1,0 cm e piè di pagina a 1,2 cm.
- **Font** (presenti su Windows/Office; LibreOffice usa sostituti metricamente compatibili: Caladea, Carlito):
  - Corpo: **Cambria** 10,5 pt, interlinea 1,2; fallback Georgia → DejaVu Serif.
  - Titoli: **Calibri** Bold; fallback Segoe UI → DejaVu Sans.
  - Codice: **Consolas** 8,5 pt; fallback DejaVu Sans Mono. Glifi dello spinner nei blocchi di codice/terminale: run in **DejaVu Sans Mono** (Consolas non ha ✻).
  - Glifo ✻ nel testo: run con **Segoe UI Symbol**, fallback DejaVu Sans (copertura verificata in S0 con fontTools: `research/note/font.md`).
- **Stili Word** (tutti con nome italiano personalizzato, prefisso `Libro`): `Libro Corpo`, `Titolo Parte`, `Titolo Capitolo` (Titolo 1), `Titolo 2`, `Titolo 3`, `Libro Codice` (sfondo `#F4F1EA`, bordo sinistro arancio), `Libro Terminale` (sfondo `#1F1E1D`, testo `#F0EEE6`), `Libro Didascalia` (8,5 pt corsivo, "Figura 4.2 – …"), `Box Nota` / `Box Consiglio` / `Box Attenzione` (tabella a una cella con bordo colorato e icona SVG originale), `Libro Citazione`, `Libro Riepilogo`, voci del glossario.
- **Struttura delle sezioni**:
  - Sezione 1: copertina, senza intestazione.
  - Sezione 2: pagine preliminari, numeri romani minuscoli.
  - Sezioni successive: una per capitolo, numeri arabi che ripartono da 1 all'inizio della Parte I. Intestazione pari = "/claude ✻ Coding", dispari = titolo del capitolo. Piè di pagina = numero di pagina + "Claude Code".
  - I capitoli iniziano su pagina dispari (interruzione di sezione "pagina dispari").
- **Indice generale** (deciso in S2): campo TOC il cui risultato è già calcolato da `build/update_indexes.py`, che impagina in più passaggi (build → PDF con LibreOffice → lettura delle pagine reali → nuova build) finché i numeri sono stabili. Niente macro UNO: il .docx finale resta quello di python-docx, senza passaggi di salvataggio da LibreOffice. **Indice analitico**: voci `[testo]{xe="voce"}` (campi XE nel .docx) e pagine ricavate dal PDF, impaginato su due colonne. In Word i campi restano aggiornabili con F9.
- **Pagine bianche** (deciso in S2): ogni sezione inizia su pagina nuova; le bianche che mandano a destra capitoli e parti le calcola `update_indexes.py` misurando il PDF. Le interruzioni "pagina dispari" di Word non si usano perché LibreOffice, dopo una bianca inserita da lui, applica male la prima pagina del capitolo.
- **Metadati DOCX**: `core_properties.author = "Claude Code"`, title, subject, language `it-IT`, keywords. Lingua `it-IT` su tutti gli stili, per la correzione ortografica.

### 7.4 Pipeline di build
1. `py build/build_book.py`: legge `book.yaml` (ordine dei capitoli e metadati), converte ogni `capitoli/*.md` e scrive `output/claude-coding.docx` (con i numeri di pagina dell'ultima impaginazione).
2. `py build/update_indexes.py`: ripete build e conversione PDF (LibreOffice headless, con esportazione delle pagine bianche) finché indici e pagine bianche sono stabili; scrive `output/claude-coding.docx` e `.pdf`.
3. `py build/check_book.py`: conta le pagine (PyMuPDF), verifica l'intervallo 160–200, la presenza dell'autore nei metadati, didascalie e crediti per ogni figura, i rimandi `F-xxx` esistenti in FATTI.md, l'assenza di segnaposto TODO.
4. `py build/render_pages.py --sample 12`: renderizza pagine a campione in PNG (`output/anteprime/`) per l'ispezione visiva (incluse copertina, pagina con box, pagina con codice, apertura di capitolo).
5. Azioni correttive per il numero di pagine:
   - **< 160**: ampliare i capitoli sotto budget (esempi, box), aggiungere figure.
   - **> 200**: tagliare dove si è sforato il budget, ridurre le figure a 80% di larghezza, comprimere le appendici.
   - Mai intervenire su font o margini sotto le specifiche di §7.3.

---

## 8. Struttura delle cartelle del progetto

```
claude_coding/
├── PROMPT.md               # richiesta originale (immutabile)
├── PLAN.md                 # questo piano + tabella di avanzamento
├── CLAUDE.md               # istruzioni permanenti (§9)
├── book.yaml               # metadati e ordine dei capitoli
├── research/
│   ├── FATTI.md            # registro dei fatti F-001…
│   └── note/               # appunti di ricerca per capitolo
├── capitoli/
│   ├── 00-prefazione.md
│   ├── 01-da-dove-vengo.md … 26-cosa-ho-imparato.md
│   ├── parte-1.md … parte-6.md    # pagine di apertura delle parti
│   └── app-a-comandi.md … app-c-risorse.md
├── assets/
│   ├── CREDITI.md          # registro delle immagini
│   ├── copertina/          # cover.html, cover.png
│   ├── cap01/ … cap26/     # immagini finali (PNG 300 dpi)
│   ├── icone/              # icone dei box (SVG originali)
│   └── src/                # script e sorgenti delle figure generate
├── build/
│   ├── build_book.py, update_indexes.py, check_book.py, render_pages.py
│   ├── stili.py            # definizione degli stili Word
│   ├── figure/             # script di generazione (graphviz, matplotlib, playwright)
│   └── package.json        # playwright
└── output/
    ├── claude-coding.docx, claude-coding.pdf
    └── anteprime/
```
Convenzioni sui nomi: minuscole, trattini, nessun accento negli identificativi; capitoli `NN-slug.md`; figure `assets/capNN/IMG-NN-MM-slug.png`; fatti `F-NNN`.

---

## 9. Contenuto proposto di `CLAUDE.md`

```markdown
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
- Python si invoca con `py` (non `python`).
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
```

---

## 10. Fasi di lavoro e ordine delle sessioni

| Sessione | Contenuto | Criterio di completamento |
|---|---|---|
| **S0 – Fondamenta** | Creare `CLAUDE.md` (§9), le cartelle (§8) e `book.yaml`; installare gli strumenti (§7.2); verificare con fontTools che i font coprano U+273B | `CLAUDE.md` presente; `py -c "import docx, markdown_it, fitz, matplotlib"` va a buon fine; `soffice --version` e `dot -V` rispondono |
| **S1 – Ricerca** | Popolare `research/FATTI.md` da §3 (≥60 voci). Chiudere i punti "da verificare" (app desktop, installer nativo, `-p`, modelli recenti, Routines). Documentare glifi e colore dello spinner osservando la console reale: registrazione/screenshot, contagocce sul colore, salvati in `research/note/spinner.md`. Fatti specifici per i capitoli 1–4 e 25. Scaricare le immagini esterne e compilare `assets/CREDITI.md` | Ogni voce con URL, data di accesso e affidabilità; nessun "da verificare" senza decisione (includere/escludere) |
| **S2 – Toolchain** | `stili.py`, `build_book.py` (sezioni, numerazioni, intestazioni, box, codice, figure, TOC), `update_indexes.py`, `check_book.py`, `render_pages.py`; un capitolo di prova con tutti gli elementi | Il DOCX di prova si apre in Word senza errori, il PDF ha numeri romani e arabi corretti, TOC aggiornato, anteprime ispezionate |
| **S3 – Copertina** | Concept A in HTML/CSS; render a 300 dpi; inserimento come prima pagina; frontespizio, colophon, dedica | `cover.png` 2008 × 2835 px; ✻ e citazione leggibili; nessun logo |
| **S4 – Capitolo pilota (cap. 6)** | Scrivere il cap. 6 per intero; misurare parole/pagina reali e ricalibrare i budget in §5 | Parole/pagina misurate e budget aggiornato |
| **S5–S29** | Un capitolo per sessione, in quest'ordine: Prefazione bozza → 1 → 2 → 3 → 4 → 5 → 7 → 8 → 9 → 10 → 11 → 12 → 13 (può richiedere 2 sessioni) → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 23 → 24 → 25 → 26 | Checklist di fine capitolo (CLAUDE.md) superata |
| **S30 – Appendici** | Comandi rapidi, glossario, risorse, crediti, indice analitico; pagine delle parti; prefazione definitiva | check_book OK |
| **S31 – Revisione finale** | Rilettura completa, coerenza dei rimandi, aggiustamento al budget, controlli di §11 | Tutti i controlli di §11 verdi |

Ogni sessione si chiude con un commit git (regole in CLAUDE.md, sezione "Git"). Le figure di ciascun capitolo si producono nella stessa sessione del capitolo. Ogni ~5 capitoli si fa una build completa per controllare la proiezione delle pagine totali.

---

## 11. Controlli di qualità finali

- [ ] PDF da LibreOffice: **160 ≤ pagine ≤ 200** (`check_book.py`, output salvato in `output/report.txt`).
- [ ] Metadati DOCX: Autore = "Claude Code", titolo, lingua it-IT.
- [ ] Copertina come prima pagina: titolo su due righe con ✻ arancio, "Claude Code", citazione «Tratto da un prompt di Andrea Capitani», immagine originale, nessun logo.
- [ ] "Claude Code" su frontespizio, colophon e piè di pagina.
- [ ] Tutto in italiano (controllo automatico delle parole inglesi fuori da codice e glossario + rilettura).
- [ ] Ogni marcatore `F-NNN` esiste in FATTI.md con fonte; nessun fatto di affidabilità B presentato come certo.
- [ ] Ogni figura ha didascalia, voce in CREDITI.md e la licenza riportata nell'Appendice D; almeno una figura ogni 8 pagine in ogni capitolo.
- [ ] TOC e intestazioni correnti corretti; numeri romani nelle pagine preliminari, arabi dal testo.
- [ ] Nessun TODO, segnaposto o commento di lavoro nel testo.
- [ ] Ispezione visiva di almeno 20 pagine renderizzate (inclusi box, codice, terminale, aperture, appendici).

---

## 12. Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| Fatti non verificabili o in contrasto tra fonti (date, percentuali) | Solo voci A/M di FATTI.md; per le dichiarazioni si riporta chi le ha fatte ("secondo Boris Cherny…"); i dati incerti si escludono |
| Dettagli noti solo dalla fuga del sorgente | Si usano solo se confermati da osservazione diretta o da fonti pubbliche; nessun codice trapelato nel libro |
| Il prodotto cambia durante la scrittura | Il libro "fotografa" Claude Code al novembre 2026 (dichiarato nel colophon); i comandi si verificano sulla versione installata |
| Licenze delle immagini | Solo le licenze ammesse, con verifica sulla pagina originale; CC BY-SA con attribuzione e immagine non modificata; in caso di dubbio, illustrazione originale |
| Marchi | Nessun logo; nome usato solo in modo descrittivo; disclaimer nel colophon ("libro non ufficiale, non affiliato ad Anthropic") |
| Sforamento delle pagine (in più o in meno) | Pilota di calibrazione (S4), build ogni 5 capitoli, azioni correttive di §7.4 |
| Densità più alta del previsto (S2: ~390 parole per pagina di solo testo, contro le 260 medie stimate) → libro sotto le 160 pagine con ~42.000 parole | Misurare nel pilota S4 le parole per pagina reali con figure, box e codice; se restano sopra ~300, alzare il budget di parole (fino a ~50.000) o la densità di figure ed esempi, oppure passare il corpo a 11 pt / interlinea 1,25 (decisione da prendere in S4 con l'utente) |
| Glifo ✻ non supportato dai font | Copertina come immagine; nel testo, run con Segoe UI Symbol e fallback DejaVu Sans; verifica con fontTools in S0 e controllo visivo sul PDF |
| Resa del DOCX diversa tra Word e LibreOffice | Font Office con equivalenti metrici; controllo campione anche in Word; niente funzioni esotiche (caselle di testo flottanti → tabelle) |
| TOC o indice analitico non aggiornati in modalità headless | Macro UNO dedicata; in alternativa TOC statico generato dalle pagine del PDF (due passaggi) |
| LibreOffice o Graphviz non installabili | Alternative: export in PDF da Word via COM (`win32com`) e diagrammi in matplotlib/SVG con Playwright |
| Tono ironico che scivola nel poco rispettoso | Checklist di fine capitolo, rilettura dedicata in S31 |

---

## 13. Tabella di avanzamento

| # | Elemento | Pagine budget | Parole target | Stato | Pagine reali | Note |
|---|---|---|---|---|---|---|
| S0 | Fondamenta (CLAUDE.md, cartelle, strumenti) | — | — | ✅ 2026-11-04 | — | Installati: pacchetti Python, LibreOffice 26.8, Graphviz 16.1, Playwright+Chromium. Test DOCX→PDF 17×24 ok, ✻ incorporato (Segoe UI Symbol). Consolas/Cambria senza ✻: vedi research/note/font.md |
| S1 | Ricerca (FATTI.md, CREDITI.md, spinner) | — | — | ✅ 2026-11-04 | — | FATTI.md: 129 voci (9 non verificate, escluse). Spinner e colore verificati sul binario 2.1.318 e sul pacchetto 0.2.9. 7 immagini Wikimedia in assets/cap01 (4 + 3 di riserva), licenze ricontrollate via API. Da leggere a mano prima del cap. 2: "The Making of Claude Code" (F-106) |
| S2 | Toolchain di build | — | — | ✅ 2026-11-05 | 27 (prova) | build_book, update_indexes (impaginazione a più passaggi), check_book, render_pages, grafo.py, render.mjs. Libro di prova con tutti gli elementi: Word e LibreOffice danno le stesse 27 pagine. **Calibrazione**: pagina di solo testo ≈ 390 parole (non 260): da verificare nel pilota S4, rischio di libro sotto le 160 pagine |
| S3 | Copertina e pagine preliminari | 4 | 300 | ✅ 2026-11-05 | 6 (con bianche) | Copertina concept A in `assets/copertina/cover.html` → `cover.png` 2009×2834 px a 300 dpi, titolo allineato come nella specifica (✻ sporgente, «Coding» sotto «/claude»). Frontespizio dai metadati, colophon (in basso sul retro), dedica. Word e LibreOffice identici. Tolta la centratura verticale (Word e LibreOffice la trattano diversamente) |
| — | Indice + Prefazione | 8 | 900 | 🟡 bozza 2026-11-05 | 4 (prefazione) | Bozza S5: 941 parole, 235 parole/pagina, 2 box, 5 rimandi ai fatti. Patto col lettore, tre percorsi di lettura, convenzioni. Da rivedere in S30 (rimandi alle appendici, numeri di pagina reali)|
| 1 | Da dove vengo | 8 | 1.900 | ✅ 2026-11-05 | 8 | 2.075 parole (+9%), 259 parole/pagina, 5 foto storiche (Wikimedia; IMG-01-R2 promossa a IMG-01-05, il «primo bug»), 2 box consiglio + 1 nota, 31 rimandi ai fatti. Regola dei capitoli autobiografici rispettata (una figura ogni 1,6 pp.). Riserve non usate: Hopper, ASR-33 |
| 2 | La nascita | 6 | 1.400 | ✅ 2026-11-05 | 6 (con bianca) | 1.398 parole, 233 parole/pagina, 2 figure (terminale «di fantasia» sulla musica; ciclo dell'agente in Graphviz), 1 nota + 1 consiglio finale, 30 rimandi. Nuovi fatti F-130…F-134 dal Making-of; F-131 ambiguo, non usato. Le due versioni del prototipo musicale (AppleScript / screenshot) riportate entrambe |
| 3 | Il lancio | 5 | 1.150 | ✅ 2026-11-05 | 4 | 1.124 parole, 281 parole/pagina, 2 figure (linea del tempo set 2024 – mag 2025 in HTML; terminale «allora e oggi»), 1 consiglio finale, 33 rimandi. Nuovi fatti F-135…F-144 (primi utenti dal Making-of, `claude --version/update/doctor`, `/feedback` verificati sul binario 2.1.318). Una pagina sotto budget: margine per i capitoli successivi |
| 4 | Crescere in pubblico | 7 | 1.600 | ✅ 2026-11-05 | 6 (con bianca) | 1.461 parole (−9%), 244 parole/pagina, 3 figure (diario delle funzioni, spinner, nuvola dei verbi; HTML), 1 consiglio finale, 46 rimandi. Fuga del sorgente raccontata con la dichiarazione di Anthropic (F-220…F-222, BleepingComputer). Nuovi F-623/F-624 (`/release-notes`, `autoUpdatesChannel`, CHANGELOG). **Parte I chiusa: 24 pp. di capitoli + apertura (budget 26)** |
| 5 | Installazione | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.251 parole (−7%), 208 parole/pagina, 2 figure (terminale Windows, «dove posso usarmi»), 3 box (attenzione, consiglio, nota), 1 tabella dei problemi, 25 rimandi. Comandi e requisiti dalla documentazione ufficiale (F-340…F-351, setup/quickstart/troubleshoot-install). **Da sistemare in S31**: vuoti in fondo alle prime pagine dei capitoli 5 e 6 (blocchi tenuti insieme che saltano pagina) |
| 6 | La prima sessione (pilota) | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.346 parole, 224 parole/pagina, 2 figure (T), 2 terminali, 3 box, 1 tabella, 17 rimandi ai fatti. Interfaccia verificata sul binario 2.1.318 (F-611…F-617) e sulla documentazione dei checkpoint (F-618…F-622) |
| 7 | Come parlarmi | 7 | 1.650 | ✅ 2026-11-05 | 6 | 1.492 parole (−10%, al limite), 249 parole/pagina, 2 figure (anatomia della richiesta; plan mode con i testi reali «Ready to code?»), 1 box attenzione, 5 esempi prima/dopo, 10 rimandi. Nuovi F-625…F-628 verificati sul binario 2.1.318 (@, Ctrl+V, Maiusc+Invio, /plan, /terminal-setup, plan mode senza modifiche) |
| 8 | CLAUDE.md e la memoria | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.296 parole (−4%), 216 parole/pagina, 1 figura (gerarchia dei CLAUDE.md) + CLAUDE.md d'esempio per l'ufficio amministrativo, 1 box attenzione, 15 rimandi. Apertura con una riga vera del CLAUDE.md di questo libro. Fatti F-360…F-368 dalla documentazione ufficiale sulla memoria; scorciatoia `#` assente nella 2.1.318 |
| 9 | Permessi e sicurezza | 5 | 1.150 | ✅ 2026-11-05 | 4 | 1.118 parole, 280 parole/pagina, 2 figure (modalità; sandbox), settings.json d'esempio, 2 box, 23 rimandi. Fatti F-370…F-380 da permissions/permission-modes/settings/sandboxing/security. **Scoperta**: dalla 2.1.283 si parte in modalità Auto → corretto il cap. 6 (box sulle modalità: passare a Manual nella prima sessione). **Parte II completa: 30 pp. (budget 30)** |
| 10 | Dal requisito al prototipo | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.224 parole (−9%), 204 parole/pagina, 2 figure (percorso in Graphviz; schermata reale della mini-app), 2 box, 3 rimandi. **Mini-app vera** in `esempi/cap10/convertitore.html`, provata con `build/figure/cap10_app.mjs` (1 mi = 1,6093 km; −40 °C = −40 °F; 100 °C = 373,15 K). Corretto l'apostrofo nel titolo della Parte IV |
| 11 | Test e debug | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.245 parole (−8%), 208 parole/pagina, 2 figure (uscita **reale** dei test; ciclo rosso-verde), 1 box attenzione, 4 rimandi. **Bug vero** trovato nella mini-app del cap. 10: «1,5» letto come 15 (campo numerico del browser) e temperature sotto lo zero assoluto. Test in `esempi/cap11/prova-convertitore.mjs` (2 falliti sulla versione del cap. 10, 7/7 sulla versione corretta `esempi/cap11/convertitore.html`); uscite in research/note/test-cap11-*.txt. Traceback Python reale (percorsi accorciati) |
| 12 | Git e revisione del codice | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.235 parole (−9%), 206 parole/pagina, 2 figure (log e diff **reali** del repository di prova della mini-app; linea della metropolitana), 1 box attenzione, 7 rimandi. Apertura con il `git log` vero di questo libro. Fatti F-381…F-384 (/code-review, /security-review, /install-github-app, /diff) |
| 13 | Un progetto completo | 12 | 2.700 | ✅ 2026-11-05 | 10 | 2.474 parole (−8%), 247 parole/pagina, 3 figure (architettura; schermata **reale**; percorso), 3 box, 1 rimando (F-127, corretto: ente non profit e cliente del carburante erano fusi). **Applicazione vera** `esempi/cap13/spese/` (solo libreria standard, SQLite, 9 test OK): difetti trovati provando (messaggi d'errore in inglese per importi e date), funzione «mese precedente» con caso limite gennaio→dicembre. Episodio vero: comando troppo ampio bloccato dal classificatore della modalità Auto. Build: blocchi di codice brevi non più spezzati tra pagine e legati al paragrafo che li introduce. Due pagine sotto budget |
| 14 | Documenti | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.225 parole (−9%), 204 parole/pagina, 2 figure (schema della stampa unione; una lettera vera convertita con LibreOffice), 2 box, 1 rimando (F-701). **Stampa unione vera** in `esempi/cap14/` (openpyxl installato): 49 lettere, 1 riga segnalata (importo mancante), cognome «  ferrari » ripulito. Episodi veri: il mio generatore di dati sceglieva i titoli a caso (22/50 «Dott.ssa Marco»), scoperto rileggendo a campione; saluto mancante nel modello |
| 15 | Fogli di calcolo | 6 | 1.350 | ✅ 2026-11-05 | 6 | 1.237 parole (−8%), 206 parole/pagina, 2 figure (schema 12→1; grafico **vero** del riepilogo esportato da LibreOffice con profilo it-IT), tabella dei mesi con i valori reali, 2 box. **Unione vera** in `esempi/cap15/` (12 estratti con 4 difetti tipici, `unisci.py` con formule SUMIFS e grafico); formule ricalcolate da LibreOffice = controllo Python al centesimo (155.000,16 €); unione ingenua 147.395,26 € (−7.604,90 €, marzo ignorato in silenzio). Nota per la build: LibreOffice in it-IT con registrymodifications.xcu |
| 16 | PDF | 5 | 1.150 | ✅ 2026-11-05 | 6 | 1.119 parole (−3%), 186 parole/pagina, 2 figure (da PDF a riga; fattura scansionata vera), 2 box. **Estrazione vera** in `esempi/cap16/`: 30 fatture di 3 fornitori con formati diversi (PyMuPDF), primo giro 19/30 per un «€» illeggibile nel testo estratto, poi 29/30; fattura 14 con +100 € segnalata; fattura 23 scansionata letta da me come immagine e confrontata col valore vero (al centesimo). Una pagina oltre il budget (recupera un po' del margine perso) |
| 17 | File e cartelle | 4 | 900 | ✅ 2026-11-05 | 4 | 898 parole, 224 parole/pagina, 1 figura (prima/dopo con nomi reali), 1 box attenzione. **Rinomina vera** in `esempi/cap17/`: 403 foto con EXIF (Pillow), prova a secco → esecuzione → annullamento verificati (380 rinominate e ripristinate), 3 doppioni per impronta SHA-256, 20 senza data, raffiche con `_2`. **Bug mio trovato dalla prova a secco**: «IMG_4001 (1).jpg» ordinato prima dell'originale, quindi segnalato l'originale come doppione |
| 18 | Report periodici | 5 | 1.150 | ✅ 2026-11-05 | 6 | 1.069 parole (−7%), 178 parole/pagina, 2 figure (catena; report Word **vero** con grafico matplotlib), 2 box, 4 rimandi. **Report vero** in `esempi/cap18/` (vendite.csv di 3 negozi, report.py → .docx + .eml in bozza con X-Unsent). Episodio vero: soglia 15% sulla settimana prima → 6 segnalazioni, 5 rumore; passato alla media di 4 settimane e 25% → 1 sola (il crollo nascosto apposta); onestà: 1–3 falsi allarmi nelle settimane normali. Percentuali corrette all'italiana. F-629…F-631 (/loop, /schedule, -p) dal binario |
| 19 | Script riutilizzabili | 4 | 900 | ✅ 2026-11-05 | 4 | 907 parole, 227 parole/pagina, 1 figura (cassetta, stilizzata), 1 box, 1 rimando (F-702). **Cassetta vera** in `esempi/cap19/cassetta/`: 5 file .bat (UTF-8, CRLF, controllo di Python e della cartella trascinata) + LEGGIMI + strumenti dei capp. 14–18; tutti provati sui dati dei capitoli e senza cartella. Episodio vero: .bat «non riconosciuto» perché lanciato senza percorso completo. **Parte IV completa: 32 pp. (budget 30)** |
| 20 | Slash command e skill | 5 | 1.150 | ✅ 2026-11-05 | 6 | 1.154 parole, 192 parole/pagina, 2 figure (confronto; skill in azione dalla prova reale), 2 box, 14 rimandi. **Prova vera con `claude -p`** in una cartella di prova: comando `/riepilogo-fattura` (risposta corretta su fattura-03) e skill `controllo-fattura` **scelta automaticamente** da una richiesta che non la nominava (100 € di differenza della fattura 14). File in `esempi/cap20/.claude/`. Fatti F-385…F-390 (docs skills, merge dei comandi nelle skill) |
| 21 | Hook | 4 | 900 | ✅ 2026-11-05 | 4 | 948 parole, 237 parole/pagina, 1 figura (eventi), 1 box, 8 rimandi. **Hook vero** provato due volte con `claude -p` in una cartella di prova: PreToolUse su Edit|Write blocca `fatture/`, Claude lavora su una copia in `lavoro/` senza aggirare il blocco. Difetti veri: messaggio con accentate illeggibili (stderr non UTF-8 su Windows) e hook che fallisce con exit 1 → lascia passare (reso «fail-closed»). File in `esempi/cap21/.claude/`. Fatti F-391…F-395 |
| 22 | Sottoagenti | 5 | 1.150 | ☐ | | |
| 23 | MCP e connettori | 5 | 1.150 | ☐ | | |
| 24 | Plugin e automazione headless | 5 | 1.150 | ☐ | | |
| 25 | Dove sono adesso | 5 | 1.200 | ☐ | | |
| 26 | Cosa ho imparato, cosa (forse) verrà | 5 | 1.200 | ☐ | | |
| — | Pagine delle parti (6) | 6 | 300 | ☐ | | |
| A–D | Appendici + indice analitico | 12 | 3.000 | ☐ | | |
| S31 | Revisione finale | **180** | **~42.000** | ☐ | | |

Le parole target dei capitoli valgono ~225–240 parole per pagina nette (figure e codice tolti) e saranno ricalibrate dopo il pilota (S4).
