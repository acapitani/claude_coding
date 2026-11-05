# Report periodici

Ogni ufficio ha il suo rito del lunedì mattina: qualcuno apre tre file, copia i numeri della settimana in un quarto, rifà il grafico, scrive due righe di commento e manda tutto alla direzione. Un'ora, a volte due, ogni settimana, per cinquanta settimane all'anno. Se mi chiedessero quale lavoro d'ufficio mi piacerebbe togliere di mezzo per primo, mi piace pensare che risponderei questo.

In questo capitolo costruiamo un report settimanale delle vendite che si prepara da solo: un documento Word con tabella e grafico, e un'email già scritta con il report in allegato, che resta in bozza finché non decidi tu di spedirla. Poi vediamo come farlo partire ogni lunedì senza ricordarsene. Come negli altri capitoli, l'esempio è vero.

## Dai dati al report

Anna gestisce le vendite di tre negozi, a Bologna, Modena e Parma. Ogni sera la cassa aggiunge le vendite del giorno a un file, `vendite.csv`: data, negozio, prodotto, pezzi e incasso. La richiesta:

```terminale
> Da vendite.csv preparami il report della settimana scorsa:
  incasso per negozio a confronto con la settimana prima,
  un grafico, e l'elenco delle variazioni importanti per
  prodotto. Salvalo in Word e preparami un'email in bozza
  per la direzione con il report allegato. Non spedire.
```

Ho scritto un programma, `report.py`, che fa esattamente questo. La figura 18.1 mostra la catena: i dati entrano, il programma calcola e confronta, escono un documento e un'email, e alla fine ci sei tu.

![La catena del report: dai dati al documento e all'email in bozza, con l'ultima parola a te](assets/cap18/IMG-18-01-catena.png){larghezza=13}

Eseguito sulla settimana dal 26 ottobre al primo novembre 2026, risponde così:

```terminale
PS C:\Users\anna\vendite> py report.py 2026-10-26
Settimana 26/10 – 01/11: incasso 8.919,90 € (-8,9%)
  da guardare: Caffè a Modena: 446,50 € (-62% rispetto
  alla media delle 4 settimane precedenti)
Creati report\report-2026-10-26.docx e la bozza email
(non inviata)
```

Il report vero è quello della figura 18.2. La bozza dell'email è un file che si apre con Outlook o con un altro programma di posta, con oggetto, destinatario, testo e allegato già al loro posto: basta rileggerla e premere «Invia».

![Il report della settimana, come esce dal programma (prima pagina, ritaglio)](assets/cap18/IMG-18-02-report.png){larghezza=11}

## La parte difficile: che cosa segnalare

Calcolare i totali è facile. La parte interessante di un report è un'altra: dire a chi lo legge *dove guardare*. Per questo il programma ha una sezione «Da guardare», con le variazioni importanti prodotto per prodotto. E qui ho sbagliato la prima volta, in un modo istruttivo.

Nei dati inventati avevo nascosto un problema vero: nell'ultima settimana, a Modena, le vendite di caffè crollano. Nella prima versione il programma confrontava ogni prodotto con la sola settimana precedente e segnalava ogni variazione superiore al 15%. Risultato: sei segnalazioni. Il crollo del caffè a Modena c'era, ma insieme a un caffè a Bologna in aumento del 41%, a un tè a Parma in calo del 31% e ad altre tre variazioni che erano solo il normale andirivieni delle vendite da una settimana all'altra. Un report che segnala sei cose ogni lunedì insegna in fretta a non leggere la sezione «Da guardare», e il giorno in cui la segnalazione sarà quella giusta nessuno se ne accorgerà.

Ho cambiato il confronto: non più con la sola settimana prima, che può essere stata strana per mille motivi, ma con la **media delle quattro settimane precedenti**, e con una soglia del 25%. Nella settimana di fine ottobre la segnalazione è una sola, quella giusta: caffè a Modena, −62%. Onestà vuole che io aggiunga che nelle settimane normali di ottobre il programma segnala comunque una o tre variazioni, che a guardarle bene sono rumore. La soglia perfetta non esiste: è una scelta tra perdere qualcosa e segnalare troppo, e conviene farla insieme, guardando qualche settimana passata.

::: consiglio Prova il report sul passato
Prima di fidarti di un report automatico, fallo girare sulle ultime cinque o sei settimane e leggi che cosa avrebbe segnalato. Se segnala troppo, alza la soglia; se ti accorgi che avrebbe taciuto su un problema che ricordi, abbassala. È il modo più rapido per tarare un allarme, e i dati del passato li hai già.
:::

## Ogni lunedì alle otto

Il report funziona; ora deve partire da solo. Ci sono tre strade, molto diverse tra loro.

**Dentro una sessione, con `/loop`.** Il comando `/loop` ripete una richiesta a intervalli regolari: «/loop 1h controlla se è arrivato il file delle vendite e, se c'è, prepara il report». <!-- F-629 --> È comodo, ma funziona solo finché la sessione resta aperta sul tuo computer: è più adatto a sorvegliare qualcosa per qualche ora che a un appuntamento settimanale.

**Sui server di Anthropic, con le Routines.** Dall'aprile 2026 esistono le *Routines*: attività che girano sull'infrastruttura web di Anthropic, a orari stabiliti, anche a computer spento. Si creano su claude.ai/code o con il comando `/schedule`, e il numero di esecuzioni giornaliere dipende dall'abbonamento: cinque per il piano Pro, quindici per Max, venticinque per Team ed Enterprise. <!-- F-219 --> <!-- F-630 --> Sono la scelta giusta quando i dati stanno già in un servizio online raggiungibile da lì, come un repository.

**Sul tuo computer, con l'Utilità di pianificazione.** C'è però una cosa che vale la pena notare: una volta scritto `report.py`, per eseguirlo *non servo più io*. È un normale programma Python, e Windows sa già avviare programmi a orario con l'Utilità di pianificazione, l'equivalente di una sveglia per i programmi; su macOS e Linux c'è qualcosa di simile. Posso prepararti l'attività pianificata, ogni lunedì alle 8:00, con il comando giusto e la cartella giusta. Da quel momento il report si prepara anche se io non ci sono, senza costi e sempre nello stesso modo.

Questa terza strada è spesso la migliore per i lavori ripetitivi d'ufficio, e dice qualcosa di importante sul modo di usarmi: il mio lavoro più utile non è fare il report ogni settimana, è scrivere una volta lo strumento che lo fa. Quando invece il compito richiede giudizio ogni volta, come leggere i dati e scrivere un commento diverso ogni settimana, allora ha senso chiamare me, anche in automatico, con la modalità non interattiva `claude -p` che vedremo nel capitolo 24. <!-- F-631 -->

::: attenzione Automatico non vuol dire incontrollato
Un report che parte da solo può anche sbagliare da solo: un file dei dati arrivato vuoto, una colonna rinominata, un negozio nuovo. Il programma di questo capitolo si ferma con un messaggio chiaro se la settimana non ha dati, invece di produrre un report pieno di zeri; chiedi sempre controlli del genere. E l'email resta in bozza: la spedisci tu, come abbiamo stabilito nel capitolo 14.
:::

## In breve

- Un report periodico si costruisce una volta: **dati, calcoli, documento, email in bozza**.
- La parte difficile è **che cosa segnalare**: troppe segnalazioni equivalgono a nessuna.
- Confronta con la **media di più settimane**, non con una sola, e **prova il report sul passato** per tarare la soglia.
- Tre modi per l'automatismo: **`/loop`** (dentro una sessione), **Routines** (sui server di Anthropic, `/schedule`), **Utilità di pianificazione** (sul tuo computer, senza bisogno di me).
- Il mio lavoro più utile è **scrivere lo strumento** che fa il report, non rifarlo ogni settimana.
- **Automatico non vuol dire incontrollato**: controlli sui dati e invio sempre manuale.
