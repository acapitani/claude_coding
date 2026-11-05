# PDF

Il PDF è il formato della fiducia: quello che vedi è quello che stampi, su qualunque computer. Proprio per questo è anche il formato più scomodo per chi deve riutilizzare i dati. Chiunque abbia ricopiato a mano in Excel i numeri di una pila di fatture sa di che cosa parlo: il PDF è fatto per essere guardato, non per essere letto da un programma.

Questo capitolo racconta come tirar fuori i dati dai PDF. L'esempio, ancora una volta, l'ho fatto davvero: trenta fatture, tre fornitori, un foglio Excel.

## Due tipi di PDF

La prima cosa da sapere è che esistono due tipi di PDF molto diversi, anche se a colpo d'occhio sembrano identici.

**I PDF con il testo.** Sono quelli prodotti da un programma: una fattura generata da un gestionale, un documento esportato da Word. Dentro c'è il testo vero, con le sue lettere e i suoi numeri. Se riesci a selezionare una parola con il mouse e a copiarla, sei in questo caso. Leggerli è facile e preciso.

**I PDF scansionati.** Sono fotografie di un foglio di carta, passate da uno scanner o da un telefono. Dentro non c'è testo, solo un'immagine. Se provi a selezionare una parola, selezioni l'intera pagina. Per un programma qualunque, questa pagina è vuota.

Io posso leggere entrambi, ma in modi diversi: i primi estraendo il testo, i secondi guardando l'immagine, come guardo uno screenshot che mi incolli nella conversazione.

## Trenta fatture, un foglio Excel

Lo studio di Anna ha ricevuto trenta fatture PDF da tre fornitori: una cartoleria, un'azienda di assistenza informatica, un'impresa di pulizie. Il commercialista vuole un elenco in Excel con fornitore, numero, data, imponibile, IVA e totale. Le fatture le ho inventate io, con un piccolo programma, ma rispettando una caratteristica delle fatture vere: ogni fornitore ha il suo modo di scriverle. Uno scrive «Fattura n. 101» e la data come «14/03/2026»; un altro «DOCUMENTO N° TS-119» e la data «del 15.03.2026»; il terzo «Fatt. 102/2026» e la data in lettere, «Bologna, 29 luglio 2026». Tra le trenta, ne ho nascoste due difficili: una con un errore nei conti e una scansionata.

```terminale
> Nella cartella fatture/ ci sono 30 fatture PDF. Fammi un
  foglio Excel con fornitore, numero, data, imponibile, IVA
  e totale. Per ogni fattura controlla che imponibile più
  IVA dia il totale. Se una fattura non si legge o i conti
  non tornano, non indovinare: dimmelo.
```

Il programma che ho scritto, `estrai.py`, legge il testo di ogni PDF e cerca i dati vicino alle parole che li annunciano: il numero dopo «Fattura n.» o «Fatt.», gli importi dopo «Imponibile», «IVA» e «Totale». La figura 16.1 mostra il procedimento su una fattura.

![Da fattura PDF a riga di tabella: il programma cerca i dati vicino alle parole che li annunciano, poi controlla i conti](assets/cap16/IMG-16-01-da-pdf-a-riga.png){larghezza=12}

## Il primo tentativo

Ecco il risultato del primo tentativo:

```terminale
Fatture lette: 19 su 30  ->  fatture.xlsx
  - fattura-23.pdf: è una scansione (nessun testo)
  - fattura-03.pdf: non trovo totale
  - fattura-06.pdf: non trovo totale
  ...
  - fattura-14.pdf: imponibile + IVA = 231.04, ma il
    totale è 331.04
```

Diciannove su trenta. Undici problemi, e dieci con lo stesso sintomo: «non trovo totale», in tutte le fatture dell'impresa di pulizie. Per capire, ho guardato il testo che usciva davvero da una di quelle fatture. La riga del totale era «Totale fattura» seguita da un carattere illeggibile e poi dalla cifra: il simbolo dell'euro, scritto con un carattere che l'estrazione del testo non sapeva rappresentare. Il mio programma cercava «Totale fattura €», con il simbolo, e non lo trovava mai.

È il genere di sorpresa che i PDF riservano spesso: quello che vedi sulla pagina e quello che c'è dentro il file non sempre coincidono. Ho reso la ricerca più tollerante, accettando qualunque simbolo tra l'etichetta e la cifra, e ho rilanciato:

```terminale
Fatture lette: 29 su 30  ->  fatture.xlsx
Totale delle fatture lette: 54.382,42 €
  - fattura-23.pdf: è una scansione (nessun testo):
    da leggere come immagine
  - fattura-14.pdf: imponibile + IVA = 231.04, ma il
    totale è 331.04
```

Ventinove su trenta, e le due segnalazioni rimaste sono esattamente le due trappole che avevo nascosto.

## La fattura con i conti sbagliati

La fattura 14 dichiara un totale di 331,04 €, ma imponibile e IVA sommano 231,04 €: cento euro di differenza. Un programma che si limitasse a copiare il totale l'avrebbe messo nel foglio senza battere ciglio. Il controllo «imponibile più IVA uguale al totale» costa una riga di codice e, in questo caso, vale cento euro. Nella realtà, un errore del genere va segnalato al fornitore, non corretto da te: il programma lo mette nell'elenco, ma la fattura resta com'è e la decisione è tua.

::: attenzione Non indovinare
Nella richiesta c'era una frase importante: «se una fattura non si legge o i conti non tornano, non indovinare». Un dato mancante è un problema visibile; un dato inventato è un problema invisibile, che emerge mesi dopo. Chiedi sempre che le eccezioni vengano segnalate, mai riempite.
:::

## La scansione

Resta la fattura 23, quella scansionata. Per il programma è una pagina vuota: nessun testo da estrarre. Per me no. L'ho trasformata in un'immagine, la figura 16.2, e l'ho letta come leggerei una fotografia: TecnoService S.p.A., documento TS-122 del 15 marzo 2026, imponibile 2.138,82 €, IVA 470,54 €, totale 2.609,36 €. Ho poi confrontato la mia lettura con i valori che il programma generatore aveva usato per creare quella fattura: coincidevano al centesimo.

![La fattura scansionata: per un programma è un'immagine senza testo, per me è un documento da leggere](assets/cap16/IMG-16-02-scansione.png){larghezza=8.5}

Due avvertenze, però. Questa scansione è nitida e dritta, perché l'ho prodotta io; quelle vere sono spesso storte, macchiate, fotografate di sbieco. Più la scansione è brutta, più è probabile che io sbagli una cifra, e un 3 scambiato per un 8 in un importo non fa rumore. Per le scansioni, quindi, il controllo dei conti è ancora più importante, e conviene ricontrollare a mano almeno gli importi. Se le scansioni sono tante, inoltre, ci sono programmi specializzati nel riconoscimento del testo, chiamati OCR, che possono trasformarle in PDF con il testo: posso aiutarti a usarli, e poi tornare al metodo di prima.

::: consiglio Chiedi i PDF giusti
Il modo migliore per leggere bene un PDF è non doverlo leggere affatto. Molti fornitori possono mandare i dati in un formato più comodo, come un CSV o un Excel, e in Italia le fatture elettroniche viaggiano già in un formato strutturato, l'XML, che si legge senza nessuna interpretazione. Prima di automatizzare la lettura di cento PDF, chiedi a chi te li manda se esiste un'alternativa.
:::

## Altri lavori con i PDF

Le fatture sono l'esempio più comune, ma non l'unico. Posso unire più PDF in uno solo o separarne le pagine, riassumere un documento lungo, cercare in una cartella di contratti tutti quelli che contengono una certa clausola, estrarre le tabelle da un rapporto per portarle in Excel. Per tutte queste richieste vale lo stesso principio di questo capitolo: dimmi che cosa ti serve, chiedimi di segnalare quello che non riesco a leggere, e controlla a campione il risultato.

## In breve

- Ci sono PDF **con il testo** (si seleziona una parola) e PDF **scansionati** (sono immagini).
- Dai PDF con il testo i dati si estraggono cercandoli vicino alle **parole che li annunciano**.
- Quello che vedi e quello che c'è nel file possono differire: nell'esempio, un simbolo dell'euro illeggibile.
- **Controlla i conti**: imponibile più IVA deve fare il totale; le eccezioni si **segnalano, non si indovinano**.
- Le scansioni posso leggerle come immagini, ma vanno **ricontrollate**; per grandi quantità servono strumenti OCR.
- Quando puoi, chiedi i dati in un **formato strutturato** (CSV, Excel, XML della fattura elettronica).
