# Script riutilizzabili per non programmatori

In questa parte del libro abbiamo costruito cinque strumenti: le lettere da un elenco, l'unione degli estratti conto, le fatture PDF in Excel, la rinomina delle foto, il report settimanale. Funzionano tutti. Ma se per usarli bisogna aprire un terminale, ricordare il nome di un file e scrivere un comando, in un ufficio vero li userà una persona sola: quella che li ha fatti costruire. E il giorno in cui andrà in ferie, torneranno il copia e incolla e i pomeriggi persi.

Questo capitolo chiude la parte IV con il passo che trasforma un esperimento in un'abitudine dell'ufficio: rendere gli strumenti utilizzabili da tutti, anche da chi non ha mai visto un terminale. In Anthropic, per esempio, anche il gruppo legale ha costruito con me piccoli strumenti interni per indirizzare i colleghi verso l'avvocato giusto. <!-- F-702 --> Non serve essere programmatori per avere una cassetta degli attrezzi; serve che gli attrezzi abbiano un manico.

## Il manico: un doppio clic

Su Windows esiste da sempre un tipo di file fatto apposta per questo: il *[file batch]{xe="file batch"}*, con estensione `.bat`. È un elenco di comandi che Windows esegue quando ci fai doppio clic sopra, o quando ci trascini sopra una cartella. La richiesta:

```terminale
> Prepara una cartella «Cassetta degli attrezzi» con i
  cinque strumenti dei capitoli precedenti. Per ognuno un
  file .bat con un nome chiaro: si trascina sull'icona la
  cartella con i dati e lo strumento parte. Se manca
  qualcosa, deve dirlo in italiano. Aggiungi un LEGGIMI.
```

Il risultato è la cartella della figura 19.1: cinque strumenti numerati, un file di istruzioni e una sottocartella `strumenti` con i programmi veri, che nessuno ha bisogno di aprire.

![La cassetta degli attrezzi: si trascina la cartella dei dati sopra lo strumento (ricostruzione stilizzata)](assets/cap19/IMG-19-01-cassetta.png){larghezza=13}

Ecco com'è fatto uno di quei file. Non devi saperlo scrivere, ma è utile poterlo leggere:

```bat
@echo off
chcp 65001 >nul
rem Unisce gli estratti mensili in riepilogo.xlsx.
where py >nul 2>nul || (echo Manca Python: chiedi
  all'ufficio informatico di installarlo. & pause & exit /b)
if "%~1"=="" (echo Trascina sull'icona la cartella con
  gli estratti. & pause & exit /b)
cd /d "%~1"
py "%~dp0strumenti\unisci.py" estratti
pause
```

(Ho accorciato i messaggi e spezzato due righe per farle stare nella pagina: nel file vero ogni istruzione sta su una riga sola.) Tradotto: imposta la finestra perché mostri bene le lettere accentate; controlla che Python sia installato e, se manca, lo dice in italiano; se hai fatto doppio clic invece di trascinare una cartella, ti spiega che cosa fare; altrimenti entra nella cartella che hai trascinato ed esegue il programma; alla fine aspetta che tu prema un tasto, così la finestra non si chiude prima che tu abbia letto il risultato.

## Provati davvero

Ho provato i cinque strumenti come li userebbe un collega, trascinando su ciascuno la cartella dei dati del capitolo corrispondente. Le lettere: 49 create, una riga da controllare. Gli estratti: 229 movimenti uniti, saldo 155.000,16 €. Le fatture: 29 su 30, con la scansione segnalata. Le foto: la prova a secco, 380 nomi nuovi in un file. Il report: la settimana di fine ottobre, con il caffè di Modena in evidenza. E il caso più importante di tutti: il doppio clic su uno strumento *senza* cartella, che risponde «Trascina sull'icona di questo file la cartella che contiene la sottocartella estratti» e aspetta, invece di produrre un errore incomprensibile.

Una curiosità, a proposito di prove: la prima volta che ho cercato di lanciare un file batch dal mio ambiente di lavoro, Windows mi ha risposto che il comando non esisteva. Il file era giusto; ero io che lo chiamavo nel modo sbagliato, senza il percorso completo. Lo racconto perché è un buon promemoria: quando qualcosa «non funziona», prima di cambiare lo strumento conviene controllare come lo si sta usando.

## Le regole della cassetta

Non tutti gli strumenti meritano la stessa libertà. Nella cassetta ho seguito tre regole, che ti consiglio di tenere.

**Gli strumenti che leggono e creano file nuovi** stanno nella cassetta senza problemi: le lettere, l'unione, le fatture, il report. Nel peggiore dei casi producono un file sbagliato, che si butta.

**Gli strumenti che modificano o spostano file** entrano solo nella versione prudente. Per questo nella cassetta c'è «Rinomina foto (prova)», che prepara il piano senza toccare niente; la rinomina vera, con il suo file per annullare, resta a chi gestisce la cassetta.

**Nessuno strumento spedisce, paga o cancella.** Il report prepara l'email in bozza; le lettere restano nella cartella. Le azioni che escono dall'ufficio o che non si possono annullare restano decisioni di una persona.

::: consiglio Un LEGGIMI per chi non c'era
Ogni cassetta ha bisogno di un foglio di istruzioni scritto per il collega che arriverà tra un anno: che cosa fa ogni strumento, che cosa bisogna trascinarci sopra, che cosa produce, a chi rivolgersi. Chiedimelo sempre, in italiano semplice e senza gergo. È anche il miglior test dello strumento: se non si riesce a spiegarlo in tre righe, probabilmente è troppo complicato.
:::

## Quando la cassetta cresce

Una cassetta degli attrezzi ben fatta tende ad attirare richieste: «potresti aggiungere anche…». È un buon segno, ma conviene governarla. Tieni gli strumenti in una cartella condivisa con una sola copia, così una correzione arriva a tutti; mettila sotto Git, come nel capitolo 12, così ogni modifica è annotata e reversibile; e affidala a una persona che ne sia responsabile, anche se non è un programmatore. Con me accanto, quella persona può aggiungere uno strumento in un pomeriggio.

Esiste anche un modo per dare a me stesso degli «strumenti» da richiamare con un nome: sono i comandi personalizzati e le skill, e sono l'argomento del prossimo capitolo, che apre la parte dedicata ai miei superpoteri.

## In breve

- Uno strumento è davvero utile all'ufficio quando lo può usare **chiunque**, non solo chi l'ha fatto costruire.
- Su Windows bastano i **file .bat**: si trascina la cartella dei dati sull'icona e lo strumento parte.
- Ogni strumento deve **spiegare in italiano** che cosa manca e **aspettare** che tu abbia letto il risultato.
- Nella cassetta: liberamente gli strumenti che **creano file nuovi**; solo in **versione di prova** quelli che modificano; **mai** quelli che spediscono, pagano o cancellano.
- Un **LEGGIMI** semplice, una sola copia condivisa, **Git** e un responsabile.
