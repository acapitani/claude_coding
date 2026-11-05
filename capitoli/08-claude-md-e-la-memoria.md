# CLAUDE.md e la memoria

Nel capitolo 6 ti ho confessato di avere la memoria di un pesce rosso: ogni sessione riparto da zero. Ora posso raccontarti come faccio a scrivere un libro intero, una sessione alla volta, senza dimenticare a ogni capitolo chi sono, come si impagina una figura o perché non devo mai inventare una data.

Il segreto è un file. Si chiama `CLAUDE.md`, sta nella cartella di questo libro, e lo leggo all'inizio di ogni sessione, prima ancora che tu mi scriva qualcosa. Contiene righe come questa:

```markdown
- Date, numeri, versioni, citazioni e aneddoti **solo** da
  `research/FATTI.md`
```

Se in questo libro non trovi date inventate, il merito è anche di quella riga. Io non ricordo le sessioni precedenti; il file sì. È il mio quaderno degli appunti, e questo capitolo ti insegna a scriverne uno.

## Che cos'è un CLAUDE.md

Un [CLAUDE.md]{xe="CLAUDE.md"} è un normale file di testo, scritto in Markdown: il formato semplice, con i titoli preceduti da `#` e gli elenchi da `-`, in cui sono scritti anche i capitoli di questo libro. Quando mi avvii in una cartella, leggo il CLAUDE.md che trovo lì e quelli delle cartelle che la contengono, e li tengo presenti per tutta la sessione. <!-- F-361 --> Esisteva già nella mia prima versione pubblica. <!-- F-301 -->

Dentro ci va quello che diresti a un collega nuovo il primo giorno: come è organizzato il lavoro, quali regole valgono sempre, quali errori evitare. Non serve una sintassi speciale. Serve chiarezza.

## Dove si mettono

Di CLAUDE.md ce ne possono essere diversi, a livelli diversi, come nella figura 8.1. <!-- F-360 -->

![I diversi CLAUDE.md, dal più generale al più specifico, e le altre due forme di memoria](assets/cap08/IMG-08-01-gerarchia.png){larghezza=13}

- **Il file del progetto**, `CLAUDE.md` nella cartella di lavoro. È il più importante e il più comune: contiene le regole di quel progetto e, se la cartella è condivisa, vale per tutti i colleghi.
- **Il tuo file personale**, `CLAUDE.md` dentro la cartella `.claude` del tuo utente. Vale per tutti i tuoi progetti: è il posto giusto per «rispondimi sempre in italiano» o «quando scrivi email usa il lei».
- **Il file locale**, `CLAUDE.local.md` nella cartella del progetto: preferenze tue su quel progetto, che non vuoi condividere.
- **Il file aziendale**, che l'ufficio informatico può installare per tutti, per esempio in `C:\Program Files\ClaudeCode` su Windows.
- **I file delle sottocartelle**, che leggo solo quando lavoro su file al loro interno.

Una cosa importante: questi file non si sostituiscono, si **sommano**. Li leggo tutti, dal più generale al più specifico. Se due file dicono cose in contrasto, però, non c'è una regola che decida chi vince: potrei seguire l'uno o l'altro. <!-- F-361 --> Quindi evita le contraddizioni, e quando cambi una regola cambiala in un posto solo.

## Il modo più veloce per cominciare

Non devi partire da un foglio bianco. Avviami nella cartella del progetto e scrivi `/init`: esamino i file che ci sono e preparo un CLAUDE.md iniziale con quello che riesco a capire da solo. Se un CLAUDE.md esiste già, non lo sovrascrivo: ti propongo dei miglioramenti. <!-- F-363 --> Poi tocca a te correggerlo e completarlo, perché le cose più preziose, come le abitudini dell'ufficio e le eccezioni, dai file non si vedono.

Per rivederlo in seguito c'è `/memory`, che elenca i file di memoria e ti permette di aprirli e modificarli. <!-- F-363 --> Oppure, più semplicemente, chiedimelo a parole: «aggiungi al CLAUDE.md che le fatture vanno sempre salvate in PDF». Ai tempi del mio debutto esisteva anche una scorciatoia, il cancelletto `#` all'inizio della richiesta; <!-- F-304 --> nella versione 2.1.318 non c'è più, e le parole bastano. <!-- F-368 -->

## Un esempio: l'ufficio amministrativo

Ecco un CLAUDE.md per la cartella in cui un piccolo ufficio amministrativo tiene fatture, estratti conto e report. È inventato, ma ogni riga risponde a un problema reale.

```markdown
# Amministrazione — istruzioni per Claude

## Chi siamo
Ufficio amministrativo di Rossi Srl (12 dipendenti).
Rispondi in italiano; nelle lettere ai clienti usa il lei.

## Cartelle
- fatture/AAAA/MM/  fatture ricevute, in PDF
- estratti/         estratti conto mensili (Excel)
- report/           i report che produciamo noi

## Regole
- Non modificare MAI i file in fatture/ ed estratti/:
  lavora su copie in lavoro/.
- Importi in euro con due decimali e la virgola: 1.234,56
- Date nel formato GG/MM/AAAA nei documenti,
  AAAA-MM-GG nei nomi dei file.
- Prima di rinominare o spostare più di 10 file,
  mostrami un'anteprima.

## Quando hai finito
- Controlla che i totali coincidano con gli originali.
- Dimmi quali file hai creato e dove.
```

Nota tre cose. Le regole sono **concrete**: non «usa un formato corretto», ma «1.234,56». La documentazione ufficiale dà lo stesso consiglio: meglio «esegui i test prima di ogni commit» che «verifica le modifiche». <!-- F-365 --> Le regole sono **brevi** e raggruppate sotto titoli, perché un CLAUDE.md dovrebbe restare sotto le duecento righe. <!-- F-365 --> E c'è un criterio di «fatto», quello del capitolo 7, scritto una volta per tutte.

::: attenzione Un promemoria, non un lucchetto
Il CLAUDE.md orienta il mio comportamento, ma non è una serratura: lo tratto come un insieme di istruzioni da seguire, non come una regola imposta dal sistema. <!-- F-366 --> Di solito basta, ma se una cosa non deve succedere *mai*, come cancellare la cartella delle fatture, serve un vero divieto: lo imposteremo con i permessi nel capitolo 9 e con gli hook nel capitolo 21.
:::

## Che cosa metterci, e che cosa no

**Sì:** le regole che valgono in ogni sessione, i formati, le cartelle importanti, i file da non toccare, le abitudini dell'ufficio, gli errori già fatti una volta e da non ripetere. **No:** procedure lunghe che servono solo ogni tanto (per quelle esistono le skill, capitolo 20), informazioni che posso ricavare da solo guardando i file, e soprattutto **password, codici e dati personali**. Un CLAUDE.md finisce spesso in cartelle condivise: scrivici solo quello che potresti appendere in bacheca.

Un ultimo vantaggio, poco noto: quando una sessione diventa lunga e la riassumo con `/compact`, le istruzioni date solo a voce durante la conversazione possono perdersi nel riassunto, mentre il CLAUDE.md del progetto lo rileggo da capo. <!-- F-366 --> Se ti accorgi di ripetermi la stessa cosa in ogni sessione, è il segnale che quella cosa va nel CLAUDE.md.

## Quando il file cresce

Con il tempo un CLAUDE.md tende a ingrassare: ogni problema risolto aggiunge una riga. Ci sono due modi per tenerlo in forma. Il primo sono gli **import**: dentro il CLAUDE.md una riga come `@istruzioni/lettere.md` mi dice di leggere anche quell'altro file, così puoi tenere le regole sulle lettere in un documento a parte, magari scritto da chi in ufficio se ne occupa. Gli import possono annidarsi fino a quattro livelli, e se puntano fuori dalla cartella del progetto ti chiedo il permesso prima di leggerli. <!-- F-362 -->

Il secondo sono le **regole per argomento**: piccoli file nella cartella `.claude/rules` del progetto, uno per tema (fatture, report, lettere), che possono anche valere solo per certe cartelle. <!-- F-367 --> Per un ufficio, all'inizio, un solo CLAUDE.md ben tenuto basta e avanza. Ma è bello sapere che, quando servirà, il quaderno può diventare un piccolo schedario.

## La memoria automatica

Oltre ai CLAUDE.md, che scrivi tu, esiste una memoria che scrivo io. Si chiama [memoria automatica]{xe="memoria automatica"} ed è attiva di serie: mentre lavoriamo, annoto da solo le cose utili da ricordare la volta successiva, come una tua preferenza, una correzione che mi hai fatto o un'informazione sul progetto. Le note restano in una cartella dentro `.claude/projects`, sul tuo computer, e all'inizio di ogni conversazione rileggo il loro indice. <!-- F-364 -->

Se mi dici «ricordati che il venerdì l'ufficio chiude alle 14», lo annoto lì; se mi dici «aggiungilo al CLAUDE.md», scrivo nel file del progetto. La differenza conta: la memoria automatica è solo tua e resta su quel computer, il CLAUDE.md lo leggono anche i colleghi. Con `/memory` puoi vedere la cartella delle note e, se preferisci, spegnere la memoria automatica. <!-- F-364 -->

Mi piace immaginare che sia il mio modo di crescere anche dentro un singolo progetto. Non ricordo le nostre conversazioni, ma ricordo quello che ho imparato da te, e forse, per un collaboratore, è la parte che conta.

## In breve

- Il **CLAUDE.md** è un file di testo che leggo all'inizio di ogni sessione: il mio quaderno degli appunti.
- Ce ne sono a più livelli (azienda, utente, progetto, sottocartella, locale): si **sommano**, non si sostituiscono.
- `/init` ne prepara uno iniziale; `/memory` li elenca e li apre; oppure chiedimelo a parole.
- Regole **concrete**, brevi, sotto i titoli; niente password né dati personali.
- Il CLAUDE.md orienta, non blocca: per i divieti veri servono permessi e hook.
- La **memoria automatica** è un taccuino che scrivo io, solo tuo e solo su quel computer.
