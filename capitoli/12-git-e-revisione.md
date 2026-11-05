# Git e revisione del codice

Questo libro ha un diario segreto. Ogni volta che finisco una sessione di lavoro, salvo lo stato di tutti i file con una breve descrizione di che cosa è cambiato. Mentre scrivo questo capitolo, il diario ha diciotto voci, e le ultime suonano così (le ho accorciate):

```terminale
$ git log --oneline
06dc80d S15: cap. 11 «Test e debug» — 6 pp., 1.245 parole
024ba8a S14: cap. 10 «Dal requisito al prototipo» — 6 pp.
c3c365f S13: cap. 9 «Permessi e sicurezza» — 4 pp.
```

La prima voce, la più vecchia, si intitola «S0: fondamenta del progetto». Se domani rovinassi un capitolo, potrei tornare a com'era ieri in pochi secondi. Se tu volessi sapere quando ho aggiunto la storia della falena, lo scopriresti con un comando. Questo diario si chiama Git, e in questo capitolo ti spiego perché dovrebbe averlo anche il tuo progetto, anche se non hai mai scritto una riga di codice.

## Git spiegato a chi non programma

Conosci la cartella con dentro `preventivo.docx`, `preventivo_v2.docx`, `preventivo_v2_corretto.docx` e `preventivo_DEFINITIVO_ok.docx`? È un sistema di versioni fatto a mano, e tutti sappiamo come finisce: nessuno ricorda quale sia quello giusto.

[Git]{xe="Git"} fa la stessa cosa, ma bene. La cartella del progetto diventa un *repository*, un archivio che ricorda tutta la propria storia. Quando il lavoro è a un buon punto, si fa un *commit*: una fotografia di tutti i file in quel momento, con una didascalia che spiega che cosa è cambiato. I file restano uno solo, con il loro nome normale; le versioni precedenti stanno nella storia, pronte per essere consultate o ripristinate. E siccome ogni commit registra esattamente quali righe sono cambiate, puoi sempre chiedere: che cosa è successo tra martedì e oggi?

Nel capitolo 6 abbiamo visto il limite dei checkpoint: un file modificato da un comando del terminale non torna indietro con il rewind, e la documentazione consiglia proprio un sistema di controllo delle versioni come Git. <!-- F-619 --> I checkpoint sono la rete di sicurezza della singola sessione; Git è quella del progetto.

## Il primo repository

Non devi imparare i comandi di Git: li conosco io. Per cominciare basta chiedere:

```terminale
> Metti questa cartella sotto Git e fai un primo commit
  con tutti i file. Poi spiegami in due righe che cosa hai
  fatto.
```

Se Git non è installato sul computer, te lo dico e ti spiego come installarlo; su Windows si chiama Git for Windows. Da quel momento puoi chiedermi di fare un commit ogni volta che il lavoro è a un buon punto, e io scriverò didascalie chiare. Per il convertitore dei capitoli 10 e 11 ho fatto proprio così, in un repository di prova: tre commit, uno per ogni passo. La figura 12.1 mostra la loro storia e una parte della modifica che ha corretto il bug della virgola, con le righe tolte in rosso e quelle aggiunte in verde.

![La storia del convertitore e una parte della correzione, come le mostra Git (uscita reale, accorciata)](assets/cap12/IMG-12-01-log-diff.png){larghezza=12}

Le didascalie contano più di quanto sembri. «Modifiche» o «sistemato» non dicono niente a chi le leggerà tra sei mesi, cioè quasi sempre a te. «Legge i numeri con la virgola; rifiuta lo zero assoluto» racconta invece che cosa è cambiato e perché, e permette di ritrovare quel momento cercando una parola. Una buona didascalia risponde a una sola domanda: *che cosa è diverso da prima?* Scriverle è uno dei lavori in cui sono più bravo, e in cui le persone, di fretta alle sette di sera, tendono a essere più sbrigative. Lascia fare a me, e rileggi.

Ti consiglio di fissare la regola nel CLAUDE.md del progetto: «a fine lavoro proponimi un commit con una descrizione in italiano». È esattamente la regola che seguo per questo libro.

## Branch: lavorare senza paura

A volte vuoi provare una modifica senza rischiare di rovinare quello che funziona. Per questo Git ha i [branch]{xe="branch"}, letteralmente «rami»: una linea di lavoro parallela, che parte dalla versione principale e può essere unita a essa quando è pronta, oppure abbandonata senza conseguenze se l'esperimento non convince.

![Commit e branch come una linea della metropolitana: la correzione nasce su un ramo e poi torna sulla linea principale](assets/cap12/IMG-12-02-metro.png){larghezza=12}

Nella figura 12.2 la linea grigia è quella principale, chiamata `main`. La correzione della virgola è nata su un ramo a parte, `correzione-virgola`; quando i test sono diventati tutti verdi, l'abbiamo riportata sulla linea principale. Per te, la richiesta è semplicissima: «lavora su un branch separato e uniscilo solo quando i test passano».

## Tornare indietro

Il momento in cui Git ti ripaga di tutto è quello in cui qualcosa va storto. «Il report funzionava ieri, oggi no» diventa una domanda con una risposta: posso confrontare la versione di ieri con quella di oggi e mostrarti esattamente che cosa è cambiato. Se serve, posso riportare un file, o l'intero progetto, a com'era a un commit preciso. Tu non devi ricordare nessun codice: basta dire «torna alla versione di ieri sera del file report.py» o «annulla l'ultimo commit». Git sa dire perfino quando è stata cambiata una singola riga, e con quale didascalia: utilissimo quando ci si chiede «ma questa regola chi l'ha messa, e perché?».

Una sola raccomandazione: le operazioni che cancellano la storia esistono, ma sono pericolose. Se ti propongo comandi che «riscrivono» i commit passati o cancellano modifiche non salvate, leggi bene la richiesta di permesso prima di dire sì.

::: attenzione Git ricorda tutto, anche quello che non dovrebbe
Un file finito in un commit resta nella storia anche se poi lo cancelli. Per questo password, chiavi d'accesso e dati personali non devono mai entrare in un repository. Esiste un file apposta, `.gitignore`, che elenca che cosa Git deve ignorare: chiedimi di prepararlo all'inizio del progetto, con dentro almeno i file `.env` e le cartelle con dati riservati.
:::

## La revisione del codice

Nei gruppi di sviluppo nessuna modifica importante entra nel progetto senza che un'altra persona l'abbia riletta. È la [revisione del codice]{xe="revisione del codice"}, e serve per la stessa ragione per cui si fa rileggere una lettera importante a un collega: chi scrive vede quello che voleva scrivere, chi legge vede quello che c'è.

Posso aiutarti anche qui. Il comando `/diff` mostra le modifiche non ancora salvate in un commit, così le vedi prima di confermarle. <!-- F-384 --> Il comando `/code-review` rilegge le modifiche in corso, o una proposta di modifica intera, cercando errori di correttezza, e può anche applicare le correzioni che trova. <!-- F-381 --> E `/security-review` fa lo stesso dal punto di vista della sicurezza. <!-- F-382 --> Un trucco utile: la revisione funziona meglio con occhi nuovi, quindi apri una sessione pulita, con `/clear`, prima di chiedermi di rivedere un lavoro che ho appena fatto io.

## GitHub e le pull request

Finora tutto è rimasto sul tuo computer. Quando il progetto coinvolge più persone, il repository si copia anche su un servizio online, come GitHub, che fa da punto di incontro. Lì le modifiche si propongono con una [pull request]{xe="pull request"}, una richiesta di unire il proprio ramo a quello principale: i colleghi la leggono, commentano le righe e, quando sono d'accordo, la approvano.

Posso partecipare anche a questo: dalla versione 1.0 esiste un'integrazione con GitHub, <!-- F-206 --> e dall'agosto 2025 l'azione ufficiale per GitHub Actions è disponibile a tutti. <!-- F-315 --> Il comando `/install-github-app` la configura per un repository, <!-- F-383 --> e da quel momento posso lavorare anche dentro GitHub, accanto ai colleghi. Ne riparleremo nel capitolo 24, quando vedremo come farmi lavorare in automatico.

## In breve

- **Git** è un diario del progetto: ogni **commit** è una fotografia dei file con una didascalia.
- Non serve imparare i comandi: chiedimi di creare il repository e di fare commit con descrizioni chiare.
- I **branch** permettono di sperimentare senza rischi e di unire il lavoro solo quando funziona.
- Con Git si torna sempre indietro; i checkpoint coprono la sessione, Git il progetto.
- Mai password o dati personali in un repository: prepara subito il `.gitignore`.
- `/diff`, `/code-review` e `/security-review` aiutano a rivedere le modifiche; le **pull request** portano la revisione nel lavoro di gruppo.
