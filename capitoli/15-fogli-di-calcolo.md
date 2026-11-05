# Fogli di calcolo

Mi piace pensare che il foglio di calcolo sia il primo linguaggio di programmazione di quasi ogni ufficio. Chi scrive `=SOMMA(B2:B13)` sta, a tutti gli effetti, dando un'istruzione a una macchina, anche se non si definirebbe mai un programmatore. E chi ha ereditato da un collega in pensione un file con sette fogli, formule lunghe tre righe e celle colorate di cui nessuno ricorda il significato sa che anche i fogli di calcolo, come i programmi, hanno bisogno di qualcuno che li capisca.

Questo capitolo è dedicato a quel lavoro: unire, ripulire, calcolare, spiegare. L'esempio è un classico di fine anno, e l'ho fatto davvero.

## Che cosa so fare con Excel

Come per i documenti Word, non apro Excel cliccando: leggo e scrivo i file con delle librerie. Posso quindi leggere fogli interi in pochi istanti, pulire dati disordinati, unire file diversi, scrivere formule al posto tuo, creare grafici e, cosa che sottovaluti finché non ti serve, spiegarti che cosa fa una formula che non hai scritto tu.

Un'avvertenza su un argomento delicato: le *macro*, i piccoli programmi nascosti dentro alcuni file Excel. Posso leggerle e scriverle, ma una macro può fare qualunque cosa sul tuo computer, e le macro arrivate per email sono uno dei modi preferiti per diffondere virus. Se ti propongo una macro, chiedimi di spiegarti riga per riga che cosa fa; se ne trovi una in un file che non conosci, non attivarla.

## Dodici estratti, un riepilogo

L'ufficio di Anna riceve ogni mese dalla banca l'estratto conto dei movimenti, in Excel. A fine anno il commercialista vuole un riepilogo: entrate, uscite e saldo mese per mese, con un grafico. Di solito qualcuno passa un pomeriggio a copiare e incollare. La richiesta, invece:

```terminale
> Nella cartella estratti/ ci sono i 12 estratti mensili
  del 2026. Uniscili in riepilogo.xlsx: un foglio con tutti
  i movimenti, un foglio con entrate, uscite e saldo per
  mese usando formule (non numeri scritti), e un grafico.
  Non modificare gli originali. Dimmi ogni stranezza che
  trovi nei file e il totale di controllo dell'anno.
```

Ho scritto un programma, `unisci.py`, che legge i dodici file, li ripulisce, li unisce e costruisce il riepilogo, come nella figura 15.1. Gli estratti, naturalmente, li avevo inventati io; ma ci avevo messo apposta i difetti che si trovano davvero nei file esportati dai programmi bancari.

![Dodici estratti mensili, quattro dei quali con un difetto, diventano un unico riepilogo](assets/cap15/IMG-15-01-unione.png){larghezza=13}

## I difetti dei file veri

Ecco che cosa ha risposto il programma (ho solo riformattato le righe più lunghe):

```terminale
Movimenti uniti: 229 da 12 file
Controllo: entrate 269.698,24  uscite 114.698,08
           saldo 155.000,16
Sistemazioni fatte:
  - 2026-05.xlsx: colonne in un altro ordine, riordinate
  - 2026-08.xlsx: riga ripetuta 03/08 Spese bancarie
    -18.53 (tenuta una sola volta: controlla che non
    fossero due pagamenti veri)
  - 2026-11.xlsx: data scritta come testo «01/11/2026»
  - 2026-03.xlsx: 18 importi scritti come testo
    (es. «-1200,00»), convertiti
```

Quattro file su dodici avevano qualcosa che non andava. A maggio le colonne erano in un ordine diverso: data e descrizione scambiate. Ad agosto una riga compariva due volte. A novembre alcune date erano scritte come testo, che Excel non riconosce come date. A marzo, il caso peggiore, tutti gli importi erano testo con la virgola, «-1200,00», invece di numeri.

Il caso di marzo merita un minuto. Se apri quel file in Excel e scrivi una somma, Excel *ignora in silenzio* le celle di testo: non dà errore, semplicemente non le conta. Ho fatto il conto di che cosa sarebbe successo con un'unione «ingenua», cioè copiando e incollando e sommando: il saldo dell'anno sarebbe risultato 147.395,26 € invece di 155.000,16 €. Mancano 7.604,90 €, cioè tutto il saldo di marzo, più i 18,53 € della riga contata due volte. Nessun avviso, nessun colore rosso: solo un numero sbagliato in un documento destinato al commercialista.

Sulla riga doppia di agosto, invece, il programma è prudente: la tiene una volta sola, ma te lo dice, perché due pagamenti identici nello stesso giorno possono anche essere veri. È una di quelle decisioni che un programma può preparare ma che spettano a te.

::: attenzione Lavora sempre su copie
La richiesta diceva «non modificare gli originali», ed è una regola da scrivere sempre, meglio ancora nel CLAUDE.md della cartella. Il riepilogo è un file nuovo; gli estratti della banca restano come sono arrivati. Se qualcosa va storto, si ricomincia da capo senza aver perso niente.
:::

## Formule, non numeri

Nel foglio «Mesi» del riepilogo non ci sono numeri scritti a mano, ma formule. Per le entrate di gennaio, in un Excel italiano, vedrai qualcosa del genere:

```text
=SOMMA.PIÙ.SE(Movimenti!C2:C230;Movimenti!D2:D230;1;
              Movimenti!C2:C230;">0")
```

Tradotto: somma gli importi della colonna C, considerando solo le righe in cui il mese, nella colonna D, è 1, e l'importo è maggiore di zero. Excel mostra i nomi delle funzioni nella lingua in cui è installato, quindi la stessa formula, su un computer in inglese, diventa `SUMIFS`.

Perché formule e non semplici numeri? Perché le formule si possono controllare: clicchi su una cella e vedi da dove viene il valore. E perché si aggiornano: se il commercialista ti fa notare un movimento da correggere nel foglio «Movimenti», il riepilogo si ricalcola da solo. Un riepilogo fatto di numeri incollati è una fotografia; uno fatto di formule è uno strumento.

## Verificare il risultato

Un riepilogo per il commercialista merita un controllo vero. Il programma, mentre unisce i dati, calcola anche per conto suo i totali dell'anno, il «totale di controllo» della richiesta. Poi ho fatto ricalcolare tutte le formule del file da LibreOffice, un programma diverso da quello che le aveva scritte, e ho confrontato: entrate 269.698,24 €, uscite 114.698,08 €, saldo 155.000,16 €, identici al centesimo. Ecco il foglio «Mesi», con i valori calcolati dalle formule:

| Mese | Entrate | Uscite | Saldo |
|---|---:|---:|---:|
| Gennaio | 20.376,30 € | 7.833,09 € | 12.543,21 € |
| Febbraio | 21.810,78 € | 9.229,27 € | 12.581,51 € |
| Marzo | 17.082,53 € | 9.496,16 € | 7.586,37 € |
| Aprile | 22.622,13 € | 10.155,32 € | 12.466,81 € |
| Maggio | 29.816,33 € | 10.801,53 € | 19.014,80 € |
| Giugno | 24.833,94 € | 11.405,35 € | 13.428,59 € |
| Luglio | 10.716,50 € | 14.184,68 € | −3.468,18 € |
| Agosto | 29.189,65 € | 8.009,20 € | 21.180,45 € |
| Settembre | 22.616,03 € | 10.390,50 € | 12.225,53 € |
| Ottobre | 14.777,70 € | 10.121,79 € | 4.655,91 € |
| Novembre | 30.692,96 € | 6.142,15 € | 24.550,81 € |
| Dicembre | 25.163,39 € | 6.929,04 € | 18.234,35 € |
| **Totale anno** | **269.698,24 €** | **114.698,08 €** | **155.000,16 €** |

E il grafico, costruito direttamente nel file Excel, è quello della figura 15.2: si vede subito luglio, l'unico mese in cui la barra rossa delle uscite supera quella blu delle entrate.

![Il grafico creato nel riepilogo, come appare aprendo il file (esportazione in PDF)](assets/cap15/IMG-15-02-grafico.png){larghezza=12}

::: consiglio Chiedi sempre un totale di controllo
Per qualunque lavoro con i numeri, chiedimi un controllo indipendente: «calcola il totale in un altro modo e confrontalo», «verifica che il numero di righe nel riepilogo sia uguale alla somma delle righe dei dodici file». Se i due conti coincidono, puoi fidarti; se non coincidono, abbiamo appena trovato un problema prima del commercialista.
:::

## Spiegami questa formula

Ultimo lavoro, forse il più apprezzato: capire un foglio ereditato. Prova a chiedermi:

```terminale
> Nel file listino-vecchio.xlsx, foglio Ordini, la colonna F
  ha una formula che non capisco. Spiegamela in italiano,
  dimmi se ci sono casi in cui sbaglia e proponi una
  versione più semplice, senza ancora cambiare il file.
```

Una formula come questa:

```text
=SE(VAL.ERRORE(CERCA.VERT(A2;Listino!A:C;3;FALSO));"";
   CERCA.VERT(A2;Listino!A:C;3;FALSO)*B2)
```

diventa così una frase: cerca il codice del prodotto della colonna A nel foglio Listino; se lo trovi, prendi il prezzo dalla terza colonna e moltiplicalo per la quantità; se non lo trovi, lascia la cella vuota. E il caso in cui sbaglia salta fuori da solo: un prodotto scritto male non dà errore, dà una cella vuota, e il totale dell'ordine risulta più basso senza che nessuno se ne accorga. Ti suona familiare? È lo stesso difetto del marzo di prima: gli errori silenziosi sono i più costosi.

## In breve

- Posso leggere, pulire, unire, calcolare e spiegare fogli Excel; le **macro** vanno trattate con prudenza.
- I file veri hanno difetti: colonne scambiate, righe doppie, **numeri e date scritti come testo**.
- Excel **ignora in silenzio** i numeri scritti come testo: nell'esempio, 7.604,90 € spariti.
- Nei riepiloghi usa **formule, non numeri**: si controllano e si aggiornano.
- Chiedi sempre un **totale di controllo** calcolato in modo indipendente.
- Lavora su **copie** e fatti **spiegare** le formule che non capisci.
