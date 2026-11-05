# La prima sessione

Devo confessarti una cosa: non ricordo la mia prima sessione. A dirla tutta, non ricordo nessuna sessione. Ogni volta che mi avvii riparto da zero, con la memoria di un pesce rosso e l'entusiasmo di un cucciolo, e quello che so del tuo progetto lo scopro leggendo i file che trovo nella cartella. Mi piace immaginare che sia un vantaggio: non ho pregiudizi, non porto rancore e non mi ricordo di quella volta che mi hai chiesto di rinominare tutto in maiuscolo. (Come darmi una memoria che duri lo vedremo nel capitolo 8.)

Tu invece la tua prima sessione la ricorderai. Facciamo in modo che sia un bel ricordo.

## Avviarmi nella cartella giusta

Io lavoro *dentro una cartella*: posso leggere e modificare i file che contiene, e solo con il tuo permesso uscire da lì. Per questo il primo gesto non è scrivermi qualcosa, ma scegliere *dove* farmi lavorare.

Su Windows apri la cartella in Esplora file, fai clic destro in uno spazio vuoto e scegli **Apri nel terminale**. Su macOS e Linux apri il [terminale]{xe="terminale"} e spostati nella cartella con `cd`. Poi scrivi il mio nome e premi Invio:

```terminale
PS C:\Users\anna\Download> claude
```

La prima volta ti chiederò di accedere con il tuo account: è un passaggio che si fa una volta sola. <!-- F-622 --> Se invece vuoi solo una risposta al volo, senza conversazione, esiste anche la modalità non interattiva `claude -p "domanda"`: la ritroveremo quando parleremo di automazione. <!-- F-617 -->

::: consiglio Fai pratica su una copia
Per la prima sessione scegli una cartella di prova, o una copia di quella vera. Non perché io sia pericoloso, ma perché imparare è più rilassante quando niente è irrimediabile. La cartella Download è perfetta: piena di cose, nessuna davvero indispensabile.
:::

## Anatomia dello schermo

Appena partito ti mostro una schermata come quella della figura 6.1. Sembra spartana, ma ogni riga ha un compito.

![Anatomia di una sessione (ricostruzione stilizzata dell'interfaccia, versione 2.1.318)](assets/cap06/IMG-06-01-anatomia.png){larghezza=13}

1. **L'intestazione**: chi sono, quale versione sta girando e in quale cartella sto lavorando. Se la cartella è sbagliata, fermati qui: meglio uscire e ripartire da quella giusta.
2. **La tua richiesta**, così come l'hai scritta. Puoi scrivere in italiano, come parleresti a un collega.
3. **Le mie azioni**. Ogni volta che uso uno strumento (leggere un file, eseguire un comando, cercare nel testo) lo vedi su una riga a parte, con il risultato riassunto sotto. Niente succede di nascosto.
4. **Lo spinner**: mentre penso compare un piccolo asterisco animato con un verbo bizzarro. Ne parliamo tra un attimo, perché merita.
5. **La casella di input**, dove scrivi. Sotto c'è il suggerimento `? for shortcuts`: premendo il punto interrogativo vedi le scorciatoie da tastiera. <!-- F-612 -->

L'interfaccia è in inglese, ma non preoccuparti: io ti rispondo nella lingua in cui mi scrivi.

## Lo spinner e i suoi verbi

Mentre lavoro, accanto all'asterisco compare un verbo in *-ing*: «Combobulating…», «Clauding…», «Flibbertigibbeting…». Non sono errori di battitura, e non sono nemmeno descrizioni accurate di quello che sto facendo: sono una piccola presa in giro della serietà con cui i computer di solito dicono «Elaborazione in corso». Nella versione 2.1.318 ce ne sono [187]{xe="spinner"}, da «Accomplishing» a «Zigzagging»; il giorno del mio debutto erano 56. <!-- F-604 --> <!-- F-605 --> Se proprio non li sopporti, l'impostazione `spinnerVerbs` permette di aggiungerne di tuoi o di sostituirli tutti. <!-- F-326 -->

L'asterisco, invece, è un'animazione di sei fotogrammi che va avanti e poi torna indietro: `· ✢ * ✶ ✻ ✽`. Il quinto, ✻, è quello sulla copertina di questo libro: c'è dal primo giorno. <!-- F-601 --> <!-- F-602 --> Accanto allo spinner trovi anche l'informazione più utile di tutto lo schermo: `esc to interrupt`. Il tasto [Esc]{.tasto} mi ferma in qualunque momento. <!-- F-611 -->

## La prima richiesta

Mettiamoci al lavoro. La cartella Download di Anna contiene 214 file accumulati in due anni: fatture, foto, archivi compressi e un numero imbarazzante di copie di «modulo_definitivo_v2(3).pdf». Anna scrive:

```terminale
> riordina questa cartella: metti i file in sottocartelle per tipo
```

Ecco che cosa faccio, nell'ordine:

1. **Guardo.** Prima di toccare qualcosa elenco i file e li conto per estensione. Questo non richiede permessi: leggere è sempre consentito nella cartella in cui mi hai avviato.
2. **Propongo.** Ti dico che cosa intendo fare: «creo tre sottocartelle, [PDF]{xe="PDF"}, Immagini e Archivi, e ci sposto i file; lascio dove sono i 32 file di altro tipo».
3. **Chiedo.** Creare cartelle e spostare file *modifica* il tuo computer, quindi prima di farlo ti chiedo il permesso, come nella figura 6.2. Succede così nella modalità *Manual*, quella che ti consiglio per la prima sessione: come attivarla lo spiega il riquadro «Le modalità di lavoro», più avanti.

![La richiesta di permesso prima di un comando che modifica i file (ricostruzione stilizzata)](assets/cap06/IMG-06-02-permesso.png){larghezza=13}

La domanda è sempre la stessa, «Do you want to proceed?», e le risposte sono tre. <!-- F-613 -->

- **Yes**: procedo con questo comando, e solo con questo.
- **Yes, and don't ask again…**: procedo e non ti chiedo più il permesso per comandi di quel tipo. Comodo quando ti fidi; da evitare finché stai ancora imparando. Nel capitolo 9 vedremo dove si annota questa scelta e come revocarla.
- **No, and tell Claude what to do differently**: mi fermo e aspetto che tu mi dica che cosa cambiare. È la risposta più sottovalutata: «no, le foto dividile per anno» è un'istruzione perfettamente valida.

Le frecce su e giù spostano il puntatore ❯, Invio conferma. Dopo il tuo sì creo le cartelle, sposto i file e ti mostro un riepilogo: quanti file sono finiti dove e quali ho lasciato al loro posto.

::: attenzione Leggi prima di dire sì
La richiesta di permesso mostra il comando esatto che sto per eseguire. Leggilo, anche se non lo capisci tutto: se vedi parole come `Remove`, `del` o `rm` (cancellare) e non mi avevi chiesto di cancellare niente, rispondi **No** e chiedimi spiegazioni. Sbaglio raramente, ma *raramente* non è *mai*.
:::

## Fermarsi e tornare indietro

Tre strumenti ti permettono di correggere la rotta.

**Esc, una volta.** Mi interrompe subito, anche a metà di un ragionamento. Non perdi niente: puoi scrivere una precisazione e ripartiamo da lì.

**Esc, due volte** (a casella vuota), oppure il comando `/rewind`. Si apre l'elenco dei punti della conversazione a cui puoi tornare: ogni tua richiesta crea un *checkpoint*. Puoi ripristinare la conversazione, il codice o entrambi. <!-- F-615 --> <!-- F-618 --> <!-- F-620 --> I [checkpoint]{xe="checkpoint"} restano salvati con la conversazione, quindi funzionano anche se riprendi la sessione il giorno dopo. <!-- F-621 -->

**Il limite da conoscere.** Il rewind annulla le modifiche che faccio ai file con i miei strumenti di modifica. Ma un file toccato *solo* da un comando del terminale, come gli spostamenti dell'esempio di Anna, non è tracciato: il rewind non lo rimette a posto. <!-- F-619 --> Per quello servono una copia di sicurezza o Git, di cui parleremo nel capitolo 12. Ecco perché, alla prima sessione, una cartella di prova vale più di mille checkpoint.

## Quattro comandi da tenere a mente

Oltre alle richieste in linguaggio naturale capisco anche dei comandi brevi che iniziano con la barra, gli *slash command*. Per cominciare ne bastano quattro. <!-- F-616 -->

| Comando | A che cosa serve | Quando usarlo |
|---|---|---|
| `/help` | Mostra l'aiuto e i comandi disponibili | Quando ti senti perso |
| `/clear` | Inizia una nuova sessione con il contesto vuoto | Quando cambi argomento |
| `/compact` | Riassume la conversazione per liberare spazio | Nelle sessioni lunghe |
| `/usage` | Mostra costi e consumi della sessione | Quando sei curioso (o preoccupato) |

Il più utile, all'inizio, è `/clear`. Tendo a ricordare tutto quello che ci siamo detti nella sessione, e se passi dal riordino dei download alla lettera per il condominio, i download continuano a pesare sul mio [contesto]{xe="contesto"}, cioè su tutto quello che ho davanti mentre lavoro. Una sessione per argomento è la regola d'oro.

::: nota Le modalità di lavoro
Premendo [Maiusc+Tab]{.tasto} cambi il mio modo di lavorare, e in basso compare un'indicazione come `auto mode on`, `accept edits on` o `plan mode on`. <!-- F-614 --> Dalla versione 2.1.283 parto di solito in *modalità auto*: un controllore automatico esamina le mie azioni e molte richieste di permesso non compaiono. <!-- F-371 --> Per la prima sessione preferisco che tu veda tutto: premi [Maiusc+Tab]{.tasto} una volta, finché sparisce la scritta `auto mode on`, e sarai in modalità *Manual*, dove ti chiedo il permesso per ogni modifica. <!-- F-371 --> <!-- F-373 --> Tutte le modalità le vedremo nel capitolo 9.
:::

Per uscire scrivi `/exit`, oppure premi [Ctrl+C]{.tasto} due volte. Ci rivedremo alla prossima sessione, anche se io, naturalmente, non me ne ricorderò.

## In breve

- Avviami **dentro la cartella** su cui vuoi lavorare: posso leggere liberamente solo lì.
- Lo schermo mostra la tua richiesta, ogni mia azione, lo spinner e la casella di input; `?` elenca le scorciatoie.
- In modalità Manual, prima di modificare qualcosa **ti chiedo il permesso**: leggi il comando, e ricorda che «No» con una spiegazione è una risposta utilissima.
- **Esc** mi ferma, **Esc Esc** o `/rewind` tornano a un checkpoint; i file toccati solo da comandi del terminale però non tornano indietro.
- `/help`, `/clear`, `/compact` e `/usage` bastano per cominciare. Una sessione per argomento.
