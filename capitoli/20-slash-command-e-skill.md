# Slash command e skill

Ricordo bene, per modo di dire, il marzo del 2025. Ero al mondo da pochi giorni e arrivò una delle mie prime novità: i comandi personalizzati. Chiunque poteva salvare una procedura in un file e richiamarla con una barra e un nome. <!-- F-302 --> Sette mesi dopo arrivarono le skill, <!-- F-318 --> che oggi sono diventate uno standard aperto, adottato ben oltre i miei confini. <!-- F-319 --> <!-- F-320 --> Sono due modi per insegnarmi qualcosa una volta sola, invece di rispiegarlo a ogni sessione. Con questo capitolo comincia la parte dedicata a quelli che, con una certa immodestia, il piano di questo libro chiama i miei superpoteri.

## Il problema: rispiegare tutto ogni volta

Nel capitolo 7 abbiamo visto come scrivere una buona richiesta, e nel capitolo 8 come scrivere nel CLAUDE.md le regole che valgono sempre. Ma c'è una terza categoria: le *procedure*. «Controlla questa fattura: leggi imponibile, IVA e totale, verifica che i conti tornino, rispondi in questo formato, non correggere niente.» Non è una regola da tenere sempre presente; è un lavoro da fare quando serve, sempre allo stesso modo. La documentazione dà un criterio molto pratico: quando ti accorgi di incollare nella conversazione sempre le stesse istruzioni, o quando un pezzo del CLAUDE.md è diventato una procedura invece di una regola, è il momento di farne una skill. <!-- F-386 -->

![Comando e skill a confronto: il comando lo avvii tu, la skill la scelgo io quando serve](assets/cap20/IMG-20-01-comando-skill.png){larghezza=13}

## Un comando personalizzato

Il modo più semplice è un comando personalizzato: un file di testo nella cartella `.claude/commands` del progetto. Il nome del file diventa il nome del comando. Ecco `riepilogo-fattura.md`:

```markdown
---
description: Riassume una fattura PDF in tre righe
argument-hint: [file della fattura]
---
Leggi la fattura $ARGUMENTS e scrivi esattamente tre righe
in italiano:
1. Fornitore e numero della fattura
2. Data
3. Totale in euro, con la virgola decimale
Nient'altro.
```

La parte tra le due righe di trattini è l'intestazione: una descrizione e un suggerimento su che cosa scrivere dopo il nome. Sotto ci sono le istruzioni. Al posto di `$ARGUMENTS` finisce tutto quello che scrivi dopo il comando. <!-- F-388 --> L'ho provato davvero, in una cartella con le fatture del capitolo 16:

```terminale
> /riepilogo-fattura fatture/fattura-03.pdf
Pulizie Lampo di G. Neri – Fattura n. 102/2026
29 luglio 2026
Totale: 3.136,82 €
```

Tre righe, giuste. La prossima volta che Anna deve riassumere una fattura, le basta una barra e un nome.

## Una skill

Una [skill]{xe="skill"} è qualcosa di più: una cartella con un file `SKILL.md` di istruzioni ed eventuali file di supporto, come esempi o piccoli programmi. Sta nella cartella `.claude/skills/` del progetto, o in quella del tuo utente per averla ovunque. <!-- F-386 --> Ecco l'inizio di `controllo-fattura/SKILL.md`:

```markdown
---
description: Controlla una fattura (imponibile + IVA =
  totale, IVA al 22%). Usala quando l'utente chiede di
  verificare, controllare o validare una fattura.
---
# Controllo fattura
1. Leggi la fattura indicata.
2. Trova imponibile, IVA e totale.
3. Controlla l'IVA al 22% e la somma.
4. Rispondi «FATTURA CORRETTA» o «FATTURA DA CONTROLLARE».
Non correggere mai la fattura: segnala soltanto.
```

(Nella versione vera le istruzioni sono un po' più dettagliate.) La differenza decisiva sta nella descrizione. Le descrizioni di tutte le skill disponibili sono sempre davanti a me; il loro contenuto completo lo leggo solo quando serve. <!-- F-387 --> Questo significa che una skill non va necessariamente richiamata per nome: se la tua richiesta corrisponde alla descrizione, la scelgo io.

Anche questo l'ho provato. Nella stessa cartella ho chiesto, senza nominare nessuna skill: «Puoi verificarmi la fattura fatture/fattura-14.pdf?». La figura 20.2 mostra che cosa è successo: come prima mossa ho usato la skill `controllo-fattura`, poi ho letto il PDF, e ho risposto esattamente nel formato stabilito, trovando i cento euro di differenza che avevamo scoperto nel capitolo 16. <!-- F-390 -->

## Comando o skill?

La figura 20.1, all'inizio del capitolo, riassume la differenza, che oggi è più sottile di quanto fosse un tempo. I comandi personalizzati sono stati infatti assorbiti dalle skill: un file in `.claude/commands/` e una skill con lo stesso nome creano lo stesso comando e funzionano allo stesso modo, e i vecchi file continuano a funzionare. Per i lavori nuovi la documentazione consiglia le skill, perché possono contenere anche file di supporto. <!-- F-385 -->

In pratica, il mio consiglio è questo. Se è un **gesto** che vuoi avviare tu, quando decidi tu, va benissimo un comando, o una skill che scelgo io solo quando me lo chiedi: basta aggiungere nell'intestazione `disable-model-invocation: true`. <!-- F-387 --> Se è una **competenza**, cioè un modo di fare le cose che voglio applicare ogni volta che l'argomento salta fuori, è una skill con una buona descrizione.

![La skill scelta da sola: la richiesta non la nominava (ricostruzione stilizzata della prova reale, testo accorciato)](assets/cap20/IMG-20-02-skill-in-azione.png){larghezza=12}

::: consiglio La descrizione è tutto
Una skill che non viene mai usata ha quasi sempre una descrizione vaga. Scrivi due cose: **che cosa fa** e **quando usarla**, con le parole che userebbe davvero chi te la chiede. «Controlla fatture» è debole; «Usala quando l'utente chiede di verificare, controllare o validare una fattura» funziona, come ha mostrato la prova.
:::

## Tre skill per un ufficio

Per darti un'idea di che cosa vale la pena trasformare in skill, ecco tre esempi che in un ufficio come quello di Anna si ripagano in una settimana.

**Il verbale di riunione.** «Usala quando l'utente ti dà degli appunti di riunione da sistemare.» Dentro: il modello del verbale dello studio, l'ordine delle sezioni (presenti, decisioni, compiti con responsabile e scadenza), la regola di non inventare decisioni che negli appunti non ci sono e di segnalare i compiti senza responsabile.

**La lettera ai clienti.** «Usala quando devi scrivere a un cliente dello studio.» Dentro: il tono (il lei, cortese ma diretto), le formule di apertura e chiusura, la firma, due lettere di esempio come file di supporto, e l'elenco delle cose da non promettere mai per iscritto.

**Il controllo prima dell'invio.** «Usala quando l'utente sta per spedire un documento all'esterno.» Dentro: una lista di controllo. Nomi e cifre coincidono con i dati? Ci sono segnaposto rimasti, come nel capitolo 14? Allegati citati ma mancanti? Dati personali che non dovrebbero esserci?

Nota che nessuna delle tre contiene codice: sono istruzioni scritte in italiano, come le scriveresti per un collega nuovo. È la ragione per cui le skill sono alla portata di chiunque sappia spiegare bene il proprio lavoro.

## Skill già pronte, e skill da condividere

Non devi scriverle tutte tu. Con me arrivano alcune skill già pronte, come `/code-review`, che abbiamo incontrato nel capitolo 12, `/loop`, del capitolo 18, `/debug` e `/doctor`; il comando `/skills` elenca tutte quelle disponibili. <!-- F-389 --> E poiché le skill sono semplici cartelle di testo, si condividono come qualunque altro file: messe nella cartella del progetto, sotto Git, valgono per tutti i colleghi. Le skill sono nate mentre si costruiva Claude Code e sono diventate uno standard aperto; a ottobre 2026 se ne contavano circa 280 milioni di installazioni. <!-- F-320 --> <!-- F-505 --> Nel capitolo 24 vedremo come impacchettarle, insieme ad altri strumenti, in un plugin.

::: attenzione Una skill presa da internet è codice di qualcun altro
Una skill può contenere istruzioni e programmi che verranno eseguiti sul tuo computer. Prima di installarne una trovata in rete, leggine il contenuto, o chiedimi di leggerlo e di spiegarti che cosa fa, come faresti con una macro di Excel arrivata per email.
:::

## In breve

- Comandi e skill servono a **insegnarmi una procedura una volta sola**.
- Un **comando personalizzato** è un file in `.claude/commands/`: lo avvii con `/nome`, e `$ARGUMENTS` riceve quello che scrivi dopo.
- Una **skill** è una cartella con `SKILL.md`: la scelgo io quando la richiesta corrisponde alla **descrizione**, oppure la avvii tu con `/nome`.
- Oggi i comandi sono confluiti nelle skill: per i lavori nuovi, **preferisci le skill**.
- La **descrizione** decide tutto: che cosa fa e quando usarla.
- Le skill si **condividono** con la cartella del progetto; quelle prese da internet vanno **lette** prima di installarle.
