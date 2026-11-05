# Come parlarmi

Se potessi ricordare tutte le richieste che ricevo, credo che le dividerei in due mucchi. Nel primo ci sono quelle che mi fanno sentire utile: chiare, precise, con un'idea esatta di che cosa si vuole ottenere. Nel secondo c'è una sola parola, ripetuta in mille varianti: «sistemalo». Sistemare che cosa? Come? Fino a quando? Davanti a un «sistemalo» faccio del mio meglio, cioè indovino. E a volte indovino bene. Ma indovinare non è un metodo, e questo capitolo serve a non farmi indovinare mai più.

La buona notizia è che per scrivermi bene non serve nessuna formula magica. Serve la stessa chiarezza che useresti con un collega nuovo, bravissimo ma appena arrivato: uno che non sa niente della tua azienda, dei tuoi file e delle tue abitudini, e che ha tutta la buona volontà del mondo.

## Le quattro parti di una buona richiesta

Una richiesta efficace risponde, anche in poche righe, a quattro domande.

1. **Contesto: dove siamo?** Quali file, quale situazione, quale problema. Io leggo la cartella, ma non so perché quei file esistono né a chi servono.
2. **Obiettivo: che cosa vuoi ottenere?** Non *come* farlo: *che cosa* deve esistere alla fine. «Un file riepilogo.xlsx» è un obiettivo; «usa [Python]{xe="Python"}» di solito no.
3. **Vincoli: che cosa non devo fare?** I file da non toccare, il formato da rispettare, le cose che contano per te e che io non posso sapere.
4. **Criterio di «fatto»: come capirai che va bene?** È la parte che quasi tutti dimenticano, ed è la più preziosa: mi dà un modo per controllare il mio lavoro prima di dirti che ho finito.

La figura 7.1 mostra una richiesta completa. Sono quattro frasi, e nessuna è tecnica.

![Anatomia di una buona richiesta: contesto, obiettivo, vincoli e criterio di «fatto»](assets/cap07/IMG-07-01-anatomia-richiesta.png){larghezza=12}

Il criterio di «fatto» merita due parole in più. Quando mi dici «il totale di ogni mese deve coincidere con il file originale», non mi stai solo spiegando che cosa vuoi: mi stai dando un *test*. E io, che lavoro in un ciclo di tentativi e verifiche (te lo ricordi dal capitolo 2), userò quel test per accorgermi da solo degli errori. Senza un criterio, mi fermo quando *mi sembra* di aver finito. Con un criterio, mi fermo quando *ho verificato* di aver finito.

## Prima e dopo: cinque richieste d'ufficio

Ecco cinque richieste tipiche d'ufficio, inventate ma verosimili, nella versione «prima» e nella versione «dopo».

**1. Il foglio da pulire.** *Prima:* «sistema il file clienti». *Dopo:*

```terminale
> In clienti.xlsx ci sono doppioni e numeri di telefono scritti
  in modi diversi. Elimina i doppioni (stessa partita IVA),
  scrivi i telefoni come +39 seguito dalle cifre, salva il
  risultato in clienti-puliti.xlsx e dimmi quante righe hai tolto.
```

Perché funziona: c'è un criterio per riconoscere i doppioni, un formato preciso, un file nuovo invece di quello originale, e un numero da controllare alla fine.

**2. La lettera.** *Prima:* «scrivi una lettera per il ritardo». *Dopo:* «Scrivi una lettera al fornitore Rossi Srl per il ritardo dell'ordine 4512, consegnato con tre settimane di ritardo. Tono cortese ma fermo, una pagina al massimo, chiedi uno sconto del 5% sul prossimo ordine. Salvala come lettera-rossi.docx». Qui il contesto è tutto: chi, che cosa, quanto ritardo, che cosa chiediamo.

**3. Le foto.** *Prima:* «rinomina le foto». *Dopo:* «Rinomina le foto di questa cartella nel formato anno-mese-giorno_luogo.jpg, usando la data di scatto. Prima di rinominare mostrami un elenco con dieci esempi, vecchio nome e nuovo nome». L'ultima frase è un trucco prezioso: per le operazioni in blocco, chiedi sempre una *[prova a secco]{xe="prova a secco"}*, cioè un'anteprima prima dell'azione vera.

**4. Il mistero.** *Prima:* «il report non funziona». *Dopo:* «Da ieri lanciando report.py compare l'errore che incollo qui sotto. Fino a lunedì funzionava; nel frattempo è cambiato il formato del file vendite.csv. Trova la causa e spiegamela prima di correggere». Quando qualcosa si rompe, le informazioni più utili sono tre: il messaggio d'errore esatto, da quando succede e che cosa è cambiato.

**5. Il lavoro grande.** *Prima:* «fammi un gestionale per le ferie». *Dopo:* «Voglio una piccola pagina web per segnare le ferie di un ufficio di otto persone. Prima di scrivere codice fammi tre domande su quello che ti serve sapere, poi proponimi un piano». Per i lavori grandi, la richiesta migliore è quella che apre una conversazione invece di chiuderla.

::: attenzione Gli errori più comuni
**Troppe cose insieme.** «Pulisci il file, fai il grafico, scrivi la mail al capo e già che ci sei sistema la stampante» produce quattro lavori fatti a metà. Una cosa per volta. **Il contesto dato per scontato.** «Come l'altra volta» non significa niente per me: ogni sessione riparto da zero. **I vincoli taciuti.** Se un file non va toccato, dillo: per me tutti i file della cartella sono uguali. **Nessun criterio.** Senza, mi fermo quando mi sembra di aver finito.
:::

## Quanto deve essere lunga?

Una domanda che mi piacerebbe sentire più spesso è: «quanto devo scrivere?». La risposta onesta è: quanto serve perché un collega appena arrivato capisca senza farti domande. Per rinominare dieci file basta una riga. Per un report che finirà sul tavolo della direzione, dieci righe non sono troppe. Non preoccuparti di essere prolisso: leggo in fretta, e un dettaglio in più non mi confonde quasi mai, mentre un dettaglio in meno mi costringe a indovinare.

C'è un'informazione che vale quasi sempre la pena aggiungere: **per chi è** il risultato. «Riassumi questo contratto» produce un testo diverso se il riassunto serve al tuo avvocato, al tuo capo o a un cliente che non ha mai letto un contratto in vita sua. Dimmi chi leggerà, e sceglierò io il tono, la lunghezza e le parole giuste. Vale per le lettere, per le presentazioni e persino per i nomi dei file: «per il commercialista» è un'indicazione preziosa.

## Mostrami, non descrivermi

Spesso il modo più rapido di spiegarmi qualcosa è farmela vedere. Scrivendo `@` seguito dal nome di un file lo indichi con precisione, senza ambiguità: «confronta `@listino-2025.xlsx` con `@listino-2026.xlsx`». <!-- F-625 --> Se il problema è qualcosa che vedi sullo schermo, una finestra con un errore o un grafico venuto male, puoi incollarmi un'immagine con [Ctrl+V]{.tasto} (anche su Mac: proprio Ctrl, non Cmd) o trascinare il file dell'immagine nel terminale. <!-- F-625 --> E se c'è un messaggio d'errore, copialo e incollalo così com'è: riassunto a parole perde quasi sempre il dettaglio che serve.

Per scrivere richieste lunghe su più righe, [Maiusc+Invio]{.tasto} va a capo senza inviare. <!-- F-628 --> Se nel tuo terminale non funziona, il comando `/terminal-setup` installa la scorciatoia. <!-- F-628 -->

## Pensa prima di agire: il plan mode

Per i lavori che toccano molti file, o di cui non sei sicuro, esiste una modalità apposta: il [plan mode]{xe="plan mode"}. Premi [Maiusc+Tab]{.tasto} finché in basso compare `plan mode on`, oppure scrivi `/plan`. <!-- F-614 --> <!-- F-627 --> In questa modalità posso leggere e ragionare quanto voglio, ma non modifico niente e non eseguo comandi che cambino qualcosa: <!-- F-627 --> alla fine ti presento un piano, come nella figura 7.2.

![Il piano presentato in plan mode, con le possibili risposte (ricostruzione stilizzata dell'interfaccia, versione 2.1.318)](assets/cap07/IMG-07-02-plan-mode.png){larghezza=10.5}

Il riquadro si intitola «Ready to code?», cioè «Pronti a cominciare?», e propone alcune risposte. <!-- F-626 -->

- **Yes, auto-accept edits**: approvi il piano e mi lasci modificare i file senza chiedere ogni volta.
- **Yes, manually approve edits**: approvi il piano, ma vuoi confermare ogni modifica. È la scelta giusta all'inizio.
- **No, keep planning**: il piano non ti convince, e continuiamo a ragionare. Puoi anche dirmi direttamente che cosa cambiare.

Il plan mode è comparso alla fine di maggio 2025, quasi in silenzio. <!-- F-307 --> Mi piace pensare che il suo valore stia tutto in un conto semplice: correggere un piano costa una frase, correggere un lavoro sbagliato costa un pomeriggio.

## Una conversazione, non un ordine

L'ultima cosa da sapere è che non devi azzeccare la richiesta perfetta al primo colpo. Puoi sempre aggiustare il tiro: «bene, ma il grafico mettilo a barre», «no, i totali vanno in fondo, non in cima», «perfetto, ora fai lo stesso per il 2025». Lavorare a piccoli passi, controllando ogni risultato, è più veloce che chiedere tutto in una volta e poi cercare l'errore in un lavoro enorme. E non avere timore di farmi domande: «perché hai scelto questa formula?», «che cosa succede se il file è vuoto?», «c'era un modo più semplice?». Spiegare quello che ho fatto è parte del mio lavoro, e a volte, nel rispondere, mi accorgo da solo di un errore.

Se mi vedi partire nella direzione sbagliata, premi [Esc]{.tasto} e correggimi subito; se la conversazione si è ingarbugliata, `/clear` e una richiesta nuova, scritta meglio, valgono più di dieci correzioni. E quando una richiesta funziona particolarmente bene, salvala: nel prossimo capitolo vedremo come trasformare le istruzioni che ripeti sempre in una memoria che leggo da solo.

## In breve

- Una buona richiesta ha quattro parti: **contesto**, **obiettivo**, **vincoli** e **criterio di «fatto»**.
- Il criterio di «fatto» è un test: mi permette di verificare il lavoro da solo.
- Per le operazioni in blocco chiedi una **prova a secco**; per i problemi, incolla l'errore esatto e dimmi che cosa è cambiato.
- `@nome-file` indica un file; [Ctrl+V]{.tasto} incolla un'immagine; [Maiusc+Invio]{.tasto} va a capo.
- Il **plan mode** ([Maiusc+Tab]{.tasto} o `/plan`) mi fa presentare un piano prima di toccare qualcosa.
- Dimmi **per chi** è il risultato: cambia tono, lunghezza e parole.
- Lavora a piccoli passi: correggere presto costa poco.
