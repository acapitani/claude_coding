# Glossario

I termini tecnici del libro, con il capitolo in cui compaiono per la prima volta. Le parole in inglese sono quelle che troverai nell'interfaccia e nella documentazione.

| Termine | Significato | Cap. |
|---|---|---|
| **Agent SDK** | Librerie Python e TypeScript per usare il motore di Claude Code nei propri programmi. | 24 |
| **Agent Teams** | Squadre sperimentali di istanze di Claude Code che si scambiano messaggi. | 22 |
| **agente** | Programma che porta avanti un incarico da solo, a passi: guarda, decide, agisce, verifica. | 1 |
| **allow / ask / deny** | Regole: permesso senza chiedere / chiedere sempre / vietato. | 9 |
| **$ARGUMENTS** | Segnaposto che riceve ciò che si scrive dopo il nome del comando. | 20 |
| **auto mode** | Modalità in cui un modello controllore verifica le azioni al posto delle richieste di permesso. | 9 |
| **branch** | Linea di lavoro parallela che si può unire o abbandonare. | 12 |
| **breakpoint** | Punto in cui si ferma un programma per esaminarne lo stato durante il debug. | 1 |
| **bug** | Difetto di un programma. | 1 |
| **caso limite** | Situazione ai margini (gennaio, campo vuoto, zero) dove si nascondono gli errori. | 13 |
| **changelog** | Registro delle modifiche: elenco delle novità di ogni versione. | 4 |
| **checkpoint** | Punto della conversazione a cui si può tornare con `/rewind`. | 6 |
| **Claude Tag** | Claude in Slack, erede di Claude Code in Slack. | 25 |
| **CLAUDE.md** | File di istruzioni che Claude Code legge all'inizio di ogni sessione. | 8 |
| **CLI** | Command-line interface: programma che si usa scrivendo comandi nel terminale. | 2 |
| **cloud sessions** | Sessioni di Claude Code che girano sui computer di Anthropic, avviate dal browser. | 25 |
| **CMD (Prompt dei comandi)** | La shell storica di Windows. | 5 |
| **codice di uscita** | Numero con cui un programma dice com'è andata; per gli hook 2 = blocca. | 21 |
| **comando personalizzato** | File in .claude/commands/ richiamato con /nome. | 20 |
| **commit** | Fotografia del lavoro salvata nel repository con una descrizione. | 3 |
| **compilatore** | Programma che traduce un testo leggibile da una persona nel linguaggio della macchina. | 1 |
| **connettore** | Server MCP aggiunto all'account claude.ai, disponibile anche in Claude Code. | 23 |
| **Console (Anthropic)** | Il sito per gli sviluppatori, con API e credito prepagato. | 5 |
| **container** | Ambiente isolato, una specie di piccolo computer dentro il computer. | 2 |
| **contesto** | Tutto ciò che Claude Code ha «davanti» mentre lavora: conversazione, file letti, istruzioni. | 6 |
| **criterio di «fatto»** | Il modo in cui si verifica che un lavoro è finito e corretto; funziona da test. | 7 |
| **CSV** | File di testo con dati in colonne separate da un simbolo, leggibile da Excel. | 13 |
| **database** | Archivio ordinato di dati, interrogabile da un programma. | 13 |
| **debug** | Caccia all'errore: riprodurre, isolare, capire, correggere, verificare. | 11 |
| **description (skill)** | Descrizione con cui Claude Code decide quando usare una skill. | 20 |
| **.env** | File in cui i programmi tengono di solito password e chiavi. | 9 |
| **espressione regolare** | Schema di ricerca nel testo (es. «un importo dopo la parola Totale»). | 16 |
| **evento (hook)** | Momento in cui un hook può scattare: PreToolUse, PostToolUse, Stop… | 21 |
| **EXIF** | Dati nascosti in una foto: fotocamera, impostazioni, data e ora di scatto. | 17 |
| **file batch (.bat)** | File di comandi che Windows esegue con un doppio clic o trascinandoci sopra una cartella. | 19 |
| **file per annullare** | Elenco delle modifiche fatte, che permette di tornare indietro. | 17 |
| **formula** | Istruzione di calcolo in una cella di un foglio, es. =SOMMA(B2:B13). | 15 |
| **Git** | Sistema che registra la storia delle versioni di un progetto. | 12 |
| **GitHub** | Servizio online che ospita repository e il lavoro di gruppo. | 12 |
| **.gitignore** | Elenco dei file che Git deve ignorare. | 12 |
| **Haiku** | Il modello più piccolo ed economico della famiglia Claude. | 22 |
| **headless** | Modalità senza interfaccia (`claude -p`): una richiesta, un risultato, poi Claude Code esce. | 24 |
| **Homebrew** | Gestore di programmi per macOS. | 5 |
| **hook** | Comando che Claude Code esegue sempre in un momento preciso della sessione; può anche bloccare un'azione. | 21 |
| **HTML** | Linguaggio con cui si descrive una pagina web. | 10 |
| **import (in CLAUDE.md)** | Riga @percorso che fa leggere anche un altro file. | 8 |
| **impronta (hash)** | Codice calcolato dal contenuto di un file, uguale solo per file identici. | 17 |
| **JavaScript** | Linguaggio che dà vita alle pagine web, eseguito dal browser. | 10 |
| **JSON Schema** | Descrizione di un formato di dati; con `--json-schema` Claude Code risponde in quel formato. | 24 |
| **LEGGIMI** | Foglio di istruzioni che accompagna uno strumento. | 19 |
| **LibreOffice** | Programma gratuito per l'ufficio; converte anche documenti in PDF. | 14 |
| **libreria** | Raccolta di funzioni pronte che un programma usa (es. per leggere file Word o Excel). | 14 |
| **libreria standard** | Gli strumenti che un linguaggio (es. Python) ha già di serie, senza installare altro. | 13 |
| **linter** | Programma che controlla il codice e segnala errori e problemi di stile. | 2 |
| **localhost** | Il nome con cui un computer chiama se stesso: una pagina «locale». | 13 |
| **/loop** | Ripete una richiesta a intervalli, finché la sessione è aperta. | 18 |
| **macro** | Piccolo programma dentro un file Office; può fare di tutto, da trattare con prudenza. | 15 |
| **Markdown** | Formato di testo semplice: # per i titoli, - per gli elenchi. | 8 |
| **marketplace** | Elenco di plugin (file marketplace.json) da cui aggiungerli e installarli. | 4 |
| **MCP (Model Context Protocol)** | Standard aperto con cui Claude Code si collega a strumenti e dati esterni. | 23 |
| **memoria automatica** | Note che Claude Code prende da solo tra una sessione e l'altra. | 8 |
| **merge** | Unione di un branch nella linea principale. | 12 |
| **messaggio d'errore (traceback)** | Resoconto di un errore; si legge dal basso. | 11 |
| **modalità di permesso** | Grado di autonomia di Claude Code: Plan, Manual, Accept edits, Auto, Bypass. | 9 |
| **modello linguistico** | Programma che ha imparato da molto testo a prevedere come continua una frase. | 1 |
| **npm** | Registro e gestore dei pacchetti JavaScript da cui si installano programmi. | 3 |
| **OCR** | Riconoscimento ottico dei caratteri: trasforma l'immagine di un testo in testo vero. | 16 |
| **PATH** | Elenco delle cartelle in cui il sistema cerca i programmi da avviare. | 5 |
| **PDF con testo / scansionato** | Il primo contiene il testo vero; il secondo è solo un'immagine della pagina. | 16 |
| **permesso** | Conferma richiesta prima di un'azione che modifica file o esegue comandi. | 6 |
| **plan mode** | Modalità in cui Claude Code legge e ragiona senza modificare nulla, poi presenta un piano da approvare. | 7 |
| **plugin** | Pacchetto di skill, sottoagenti, hook e server MCP che si installa con un solo comando. | 4 |
| **PowerShell** | La shell moderna di Windows. | 5 |
| **product overhang** | Quando un modello sa fare più di quanto i prodotti esistenti gli permettano. | 2 |
| **prompt** | La richiesta scritta che si dà a un modello o a Claude Code. | Pref. |
| **prompt injection** | Istruzioni nascoste in un contenuto per manipolare un assistente. | 9 |
| **prototipo** | La versione minima di uno strumento, abbastanza buona da essere usata e criticata. | 10 |
| **prova a secco** | Anteprima di un'operazione (per esempio una rinomina in blocco) prima di eseguirla davvero. | 7 |
| **pull request** | Proposta di unire un branch, da rivedere e approvare (su GitHub). | 12 |
| **Python** | Linguaggio molto usato per lavorare con file e dati. | 10 |
| **README** | File di istruzioni che accompagna un programma o un progetto. | 3 |
| **repository** | Archivio di un progetto con la storia di tutte le sue modifiche. | 3 |
| **requisito** | Descrizione di che cosa deve fare uno strumento: chi lo usa, che cosa fa, i vincoli. | 10 |
| **research preview** | Anteprima di ricerca: versione dichiaratamente sperimentale di un prodotto. | 3 |
| **revisione del codice** | Rilettura delle modifiche da parte di un'altra persona (o di Claude) prima di accettarle. | 12 |
| **rosso-verde** | Metodo: prima un test che fallisce, poi la correzione che lo fa passare. | 11 |
| **Routines** | Attività di Claude Code che girano sui server di Anthropic e partono da sole, a orario o a un segnale (/schedule). | 18 |
| **sandbox** | Recinto in cui i comandi girano isolati, con meno richieste di permesso. | 4 |
| **SDK** | Kit per gli sviluppatori: strumenti per costruire altri programmi. | 3 |
| **segnaposto** | Parola tra parentesi (es. {cognome}) che verrà sostituita con un dato. | 14 |
| **server MCP** | Programma, locale o in rete, che offre a Claude Code strumenti con nome e descrizione. | 23 |
| **sessione** | Una conversazione con Claude Code, dall'avvio all'uscita o a `/clear`. | 6 |
| **settings.json** | File delle impostazioni, comprese le regole di permesso. | 9 |
| **shell** | Interprete dei comandi: aspetta un comando, lo esegue, mostra il risultato. | 1 |
| **skill** | Cartella con un file SKILL.md di istruzioni (ed eventuali file di supporto) che Claude Code usa quando la richiesta corrisponde alla sua descrizione. | 4 |
| **slash command** | Comando breve che inizia con `/`, per esempio `/help`. | 6 |
| **soglia di segnalazione** | Variazione oltre la quale un report segnala qualcosa. | 18 |
| **SOMMA.PIÙ.SE (SUMIFS)** | Funzione che somma solo le righe che rispettano più condizioni. | 15 |
| **sottoagente** | Assistente con contesto, istruzioni e strumenti propri, a cui Claude Code affida una parte del lavoro. | 22 |
| **source map** | File che collega il codice distribuito al codice sorgente originale. | 4 |
| **spinner** | L'asterisco animato con il verbo in -ing che indica che Claude Code sta lavorando. | 6 |
| **SQLite** | Database completo contenuto in un solo file. | 13 |
| **stampa unione** | Un documento per ogni riga di un elenco, partendo da un modello con segnaposto. | 14 |
| **stdio** | Canale di testo (ingresso e uscita standard) con cui un server MCP locale comunica. | 23 |
| **strumento (tool)** | Azione che il programma intorno al modello esegue per lui: leggere, scrivere, eseguire comandi. | 2 |
| **terminale** | Finestra in cui si scrivono comandi testuali al computer. | 6 |
| **test** | Domanda di cui si conosce la risposta, controllata automaticamente da un programma. | 11 |
| **totale di controllo** | Totale calcolato in modo indipendente per verificare un risultato. | 15 |
| **Transformer** | Architettura dei modelli linguistici moderni (2017). | 1 |
| **Utilità di pianificazione** | Lo strumento di Windows che avvia programmi a orari stabiliti. | 18 |
| **versione (numero di)** | Numero in tre parti (es. 2.1.318): grandi svolte, tappe importanti, piccoli aggiornamenti. | 4 |
| **WinGet** | Gestore di programmi di Windows (installa e aggiorna da riga di comando). | 5 |
| **WSL** | Windows Subsystem for Linux: un Linux che gira dentro Windows. | 4 |
| **XML (fattura elettronica)** | Formato strutturato con cui viaggiano le fatture elettroniche in Italia. | 16 |
