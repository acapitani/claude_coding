# Documenti

Benvenuto in ufficio. Da questa parte del libro in avanti lasciamo le applicazioni e ci occupiamo del lavoro di tutti i giorni: lettere, fogli di calcolo, PDF, cartelle disordinate, report del lunedì mattina. È il terreno in cui, mi piace pensare, posso restituirti più tempo, perché è fatto di compiti ripetitivi, precisi e noiosi, cioè esattamente quelli in cui un collaboratore instancabile dà il meglio.

Non è solo una mia impressione. In Anthropic, il gruppo che si occupa di marketing ha costruito con me un flusso di lavoro che genera centinaia di nuovi annunci pubblicitari «in minuti invece che in ore», partendo dai dati delle campagne precedenti. <!-- F-701 --> Non serve essere un'azienda tecnologica per fare lo stesso con le lettere ai clienti. Cominciamo da lì.

## Che cosa so fare con i documenti

Un file Word, sotto la superficie, è un pacchetto di testi e istruzioni di formattazione. Io non apro Word come faresti tu, cliccando nei menu: uso dei piccoli programmi, delle *librerie*, che sanno leggere e scrivere quei file direttamente. Il risultato, però, è un normale documento, che apri, modifichi e stampi come qualunque altro.

Questo significa che posso leggere un contratto di quaranta pagine e riassumertelo, confrontare due versioni dello stesso documento e dirti che cosa è cambiato, uniformare lo stile di trenta relazioni scritte da persone diverse, trasformare un elenco Excel in cinquanta lettere personalizzate e convertirle tutte in PDF. Ci sono anche dei limiti, ed è giusto conoscerli subito. Un documento scansionato è una fotografia, non un testo: va prima «letto» come immagine, e ne parleremo nel capitolo 16 a proposito dei PDF. Le impaginazioni molto elaborate, con caselle di testo e immagini ancorate, possono spostarsi quando le modifico: per quelle conviene lavorare su una copia e controllare il risultato a colpo d'occhio. E una firma resta una firma: la metti tu.

Quest'ultimo è un lavoro classico d'ufficio, la *stampa unione*, ed è l'esempio di questo capitolo. L'ho fatto davvero, con un elenco di clienti inventati.

## Cinquanta lettere da un elenco

Lo studio di Anna deve mandare un sollecito di pagamento a cinquanta clienti. Ha un elenco Excel con titolo, nome, cognome, città, numero di fattura, importo e scadenza, e una lettera tipo in Word, con dei segnaposto tra parentesi graffe al posto dei dati che cambiano: `{titolo}`, `{cognome}`, `{importo}` e così via. La richiesta:

```terminale
> In questa cartella ci sono clienti.xlsx e il modello
  modello-sollecito.docx. Prepara una lettera per ogni riga
  dell'elenco, sostituendo i segnaposto. Importi in euro
  all'italiana, date per esteso. Se una riga ha dati
  mancanti, non fare la lettera e dimmelo alla fine.
  Prima mostrami tre lettere d'esempio.
```

Preparo un piccolo programma, `lettere.py`, che legge l'elenco riga per riga, apre il modello, sostituisce i segnaposto e salva una lettera per ogni cliente. La figura 14.1 mostra il meccanismo. L'ultima frase della richiesta conta più di tutte le altre: prima di produrne cinquanta, ne vediamo tre.

![La stampa unione: l'elenco e il modello entrano, le lettere escono; le righe con problemi vengono segnalate](assets/cap14/IMG-14-01-stampa-unione.png){larghezza=12}

Quando lo eseguo sul vero elenco, la risposta è questa:

```terminale
PS C:\Users\anna\solleciti> py lettere.py
Lettere create: 49 (cartella 'lettere')
Da controllare a mano:
  - riga 18: manca Importo
```

Quarantanove lettere pronte e una riga segnalata: in quella riga dell'elenco l'importo è vuoto, e un sollecito senza cifra non ha senso. Il programma non l'ha inventata, non l'ha lasciata in bianco e non si è fermato: ha fatto le altre e te l'ha detto. È il comportamento che devi pretendere da qualunque automazione.

## Che cosa può andare storto

I problemi della stampa unione, quasi sempre, non stanno nel programma ma nei dati. Nell'elenco c'era, per esempio, un cognome scritto «  ferrari », con spazi intorno e la minuscola: il programma lo ripulisce e lo scrive «Ferrari». È un piccolo accorgimento che ho aggiunto dopo aver guardato i dati, ed è il genere di cosa che si scopre solo guardando.

Poi c'è l'episodio che preferisco, perché riguarda me. L'elenco di clienti inventati l'avevo generato con un altro piccolo programma, che sceglieva titoli, nomi e cognomi a caso. Troppo a caso: rileggendo le lettere d'esempio ho trovato un «Gentile Dott.ssa Marco Ferrari». Ho contato: 22 lettere su 50 avevano un titolo che non concordava con il nome. Il programma delle lettere era corretto; i dati no. E un programma corretto con dati sbagliati produce, con grande efficienza, cinquanta lettere sbagliate. Ho corretto il generatore e rifatto tutto, ma la lezione resta: **le lettere si rileggono a campione**, sempre, prima di spedirle.

![Una delle 49 lettere prodotte, convertita in PDF (ritaglio della pagina)](assets/cap14/IMG-14-02-lettera.png){larghezza=9}

Rileggendo, del resto, mi sono accorto anche di un difetto del modello stesso: nella prima versione il nome del destinatario faceva da saluto, e mancava il classico «Gentile Dott. Ferrari,» prima del testo. Corretto il modello, rifatte le lettere: la figura 14.2 mostra il risultato. Rifare cinquanta lettere costa pochi secondi. Spedirne cinquanta sbagliate costa una figuraccia.

::: consiglio Rileggi a campione
Prima di usare il risultato di un'automazione, aprine tre o quattro esemplari scelti a caso, più quelli «strani»: il nome più lungo, l'importo più alto, la riga che ti hanno segnalato. Chiedimelo esplicitamente: «mostrami la lettera con l'importo più alto e quella del cliente con il cognome più lungo». Bastano due minuti, e sono i due minuti meglio spesi della giornata.
:::

## Il modello lo prepari tu

La lettera tipo è un normale documento Word, e conviene che lo prepari tu, con il tuo logo, i tuoi caratteri e la tua firma: io mi limito a sostituire i segnaposto. Scegli parentesi che non compaiono mai nel testo vero, come le graffe, e nomi chiari: `{scadenza}` è meglio di `{campo7}`.

C'è un'insidia tecnica che vale la pena conoscere. Word, mentre scrivi, spezza spesso il testo in pezzi invisibili, per esempio quando correggi una parola o cambi formattazione a metà. Un segnaposto può quindi risultare diviso in due, e un programma ingenuo non lo riconosce più. Il mio programma riunisce i pezzi prima di sostituire, e soprattutto, alla fine, controlla che in ogni lettera non sia rimasta nessuna parentesi graffa: se ne trova una, la lettera non viene salvata e finisce nell'elenco da controllare. Chiedi sempre un controllo del genere: *verifica che non sia rimasto nessun segnaposto*.

## Non solo lettere

La stampa unione è solo un esempio. Altre tre richieste che, in un ufficio, valgono oro:

```terminale
> Riassumi contratto-fornitura.docx in una pagina per il
  direttore: durata, costi, penali, come si disdice.
  Per ogni punto indica il numero dell'articolo.
```

```terminale
> Confronta offerta-v1.docx e offerta-v2.docx e fammi
  l'elenco di che cosa è cambiato, articolo per articolo.
```

```terminale
> Le 30 relazioni nella cartella relazioni/ usano stili
  diversi. Uniformale al modello relazione-tipo.docx,
  senza cambiare una parola del testo, e salvale in
  relazioni-uniformate/.
```

Nota i dettagli che rendono affidabile il risultato: il numero dell'articolo accanto a ogni punto del riassunto, così puoi controllare alla fonte; il confronto «articolo per articolo», che non lascia sfuggire niente; e quel «senza cambiare una parola», che fissa un confine chiaro. Sono le quattro parti del capitolo 7, applicate ai documenti.

## Dal Word al PDF, e oltre

Per mandare le lettere via email serve spesso il PDF. Anche qui posso aiutarti: la lettera della figura 14.2 l'ho convertita con LibreOffice, un programma gratuito per l'ufficio che sa trasformare documenti Word in PDF senza aprirli uno per uno. Lo stesso vale per cinquanta lettere, o cinquecento.

E le email? Posso prepararle, una per cliente, con la lettera in allegato e il testo personalizzato, e lasciartele come bozze. Spedirle è un'altra faccenda.

::: attenzione Prepari con me, spedisci tu
Preparare cento email è un lavoro che faccio volentieri; premere «invia» cento volte è una decisione che spetta a te. Un errore in una lettera si corregge prima che parta; dopo, no. Per tutto ciò che esce dall'ufficio, come email, PEC, pagamenti o pubblicazioni, la regola di questo libro è semplice: io preparo e ti mostro, tu controlli e confermi.
:::

## In breve

- Posso leggere, riassumere, confrontare, uniformare e generare documenti Word, e convertirli in PDF.
- La **stampa unione** trasforma un elenco Excel e un modello con i `{segnaposto}` in una lettera per riga.
- Le righe con dati mancanti non devono produrre lettere: vanno **segnalate**.
- I problemi stanno quasi sempre **nei dati**: rileggi le lettere **a campione**, compresi i casi strani.
- Chiedi di **verificare che non resti nessun segnaposto**.
- **Prepari con me, spedisci tu**: niente invii automatici senza il tuo controllo.
