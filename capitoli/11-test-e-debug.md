# Test e debug

Nel capitolo 1 abbiamo incontrato il bug più famoso della storia: una falena vera, incastrata in un relè dell'Harvard Mark II e incollata nel registro con una nota scherzosa. <!-- F-011 --> E abbiamo incontrato Betty Holberton, che inventò i *breakpoint*, i punti in cui si ferma un programma per guardarci dentro. <!-- F-010 --> Da allora gli insetti sono diventati metaforici, ma il lavoro è rimasto lo stesso: capire perché un programma non fa quello che dovrebbe, e assicurarsi che continui a farlo bene anche dopo le modifiche.

Questo capitolo ha una particolarità: il bug che racconto è vero. L'ho trovato nella mini-app del capitolo precedente mentre scrivevo queste pagine, ed era già lì quando, nel capitolo 10, ti dicevo che funzionava. Funzionava, infatti: con i casi che avevo provato. È esattamente il punto.

## Che cos'è un test

Un [test]{xe="test"} è una domanda di cui conosci già la risposta. «Un miglio quanti chilometri sono?» «1,6093.» Se il programma risponde 1,6093, il test passa; se risponde qualcos'altro, il test fallisce e sai che c'è un problema. Nel capitolo 7 l'abbiamo chiamato criterio di «fatto»; un test è lo stesso criterio, scritto una volta per tutte in modo che un programma possa controllarlo da solo, in pochi secondi, ogni volta che vuoi.

Perché scriverlo, se posso semplicemente provare a mano? Per tre ragioni. Perché a mano ci si stanca, e si finisce per provare sempre gli stessi due casi. Perché una modifica in un punto può rompere qualcosa in un altro, e solo un controllo completo se ne accorge. E perché un test scritto è una forma di documentazione: dice, nero su bianco, che cosa il programma promette di fare.

## I primi test del convertitore

Chiedere i test è facile:

```terminale
> Scrivi dei test per convertitore.html: per ogni caso
  scrivi il valore come lo scriverebbe una persona, scegli
  le unità e confronta il risultato con quello atteso.
  Includi anche i casi strani che ti vengono in mente.
```

L'ultima frase è la più importante. I casi «normali» li avevamo già provati nel capitolo 10; i difetti si nascondono nei casi strani: un numero negativo, un campo vuoto, una lettera al posto di una cifra, un numero scritto come lo scriverebbe davvero un italiano. Ecco una parte dell'elenco che ho preparato:

```javascript
// [categoria, valore scritto, da, a, risultato atteso]
["Lunghezza", "1", "miglia", "chilometri",
 "1,6093 chilometri"],
["Lunghezza", "1,5", "metri", "centimetri",
 "150 centimetri"],
["Temperatura", "-10", "kelvin", "gradi Celsius",
 "Sotto lo zero assoluto: controlla il valore"],
```

Non serve capire la sintassi: ogni riga è un caso, con il valore da scrivere, le unità e il risultato atteso. Un piccolo programma apre la pagina, compila i campi come farebbe una persona e confronta. La figura 11.1 mostra che cosa è successo quando l'ho eseguito sulla versione del capitolo 10.

![L'uscita reale dei test sulla versione del capitolo 10: due casi falliscono (righe accorciate)](assets/cap11/IMG-11-01-test-falliti.png){larghezza=12}

Cinque test verdi e due rossi. Il secondo era prevedibile: la pagina accettava temperature sotto lo zero assoluto, che in natura non esistono. Il primo, invece, era insidioso. Scrivendo «1,5» metri, la pagina rispondeva 1500 centimetri invece di 150: dieci volte di più, senza nessun avviso.

## Anatomia di un bug

Il [debug]{xe="debug"}, la caccia all'errore, segue quasi sempre gli stessi passi. Vale per me come per un programmatore esperto, e vale anche per te quando mi guidi.

1. **Riprodurre.** Prima di tutto bisogna far succedere l'errore a comando. Il test lo fa per noi: scrive «1,5» e ottiene 1500, ogni volta.
2. **Isolare.** Dove nasce il problema? Il calcolo è giusto: 15 metri sono davvero 1500 centimetri. Quindi il problema è prima del calcolo, nella lettura del numero.
3. **Capire.** Il campo era di tipo «numerico», e il browser con cui ho fatto la prova, pur impostato in italiano, non accettava la virgola come separatore decimale: la scartava e leggeva 15. Nessun errore, nessun avviso. Il bug più pericoloso è quello silenzioso.
4. **Correggere.** Ho trasformato il campo in un normale campo di testo e ho scritto una piccola funzione che legge i numeri all'italiana, accettando la virgola e anche il punto delle migliaia.
5. **Verificare.** Ho rieseguito tutti i test, non solo quello che falliva: sette su sette verdi.

Ecco la funzione aggiunta, con i suoi commenti:

```javascript
// Legge un numero scritto all'italiana: "1,5" e "1.234,5"
function leggiNumero(testo) {
  let s = testo.trim();
  if (s.includes(",")) s = s.replace(/\./g, "").replace(",", ".");
  return /^-?\d+(\.\d+)?$/.test(s) ? Number(s) : NaN;
}
```

L'ordine che ho seguito ha un nome: [rosso-verde]{xe="rosso-verde"}. Prima si scrive un test che fallisce, e si vede il rosso; poi si corregge il codice finché il test passa, ed è verde; infine si rifinisce, controllando che tutto resti verde. La figura 11.2 lo riassume.

![Il ciclo rosso-verde: il test viene prima della correzione](assets/cap11/IMG-11-02-rosso-verde.png){larghezza=11}

::: attenzione Correggi il codice, non il test
Quando un test fallisce, la tentazione è cambiare il test finché passa. È come spostare il bersaglio dove è finita la freccia. Se vedi che modifico un test per farlo diventare verde, fermami e chiedimi perché: a volte il test era davvero sbagliato, ma deve essere una decisione consapevole, presa da te. Nelle richieste puoi scriverlo esplicitamente: «correggi il codice, non toccare i test».
:::

## Leggere un messaggio d'errore

Non tutti i bug sono silenziosi. Molti si annunciano con un messaggio d'errore che, a prima vista, sembra scritto per spaventare. Ecco quello che produce un piccolo script Python quando non trova il file che dovrebbe leggere (ho accorciato i percorsi):

```terminale
Traceback (most recent call last):
  File "report.py", line 7, in <module>
    righe = carica("vendite.csv")
  File "report.py", line 4, in carica
    with open(nome, encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory:
'vendite.csv'
```

Il trucco è leggerlo **dal basso**. L'ultima riga dice che cosa è successo: *FileNotFoundError*, il file `vendite.csv` non esiste. Le righe sopra dicono dove: alla riga 4, dentro la funzione `carica`, chiamata dalla riga 7. In questo caso la causa più probabile è banale: il file ha un altro nome, o sta in un'altra cartella.

Non devi però diventare un esperto di messaggi d'errore: quello è il mio mestiere. Il tuo è darmeli interi. Copia tutto il messaggio, dalla prima all'ultima riga, e incollalo nella richiesta, aggiungendo da quando succede e che cosa è cambiato, come abbiamo visto nel capitolo 7.

## Il debug guidato

Quando mi chiedi di trovare un errore, una richiesta in più fa una grande differenza: **«spiegami la causa prima di correggere»**. Così io sono costretto a ragionare sul problema invece di tentare la prima correzione che passa i test, e tu capisci che cosa è successo, cosa che ti servirà la prossima volta. Se la spiegazione non ti convince, dimmelo: spesso è proprio lì che salta fuori la causa vera.

Non sono l'unico a lavorare così. In Anthropic, il gruppo che si occupa di sicurezza ha raccontato di risolvere con me problemi che richiedevano di solito dieci o quindici minuti in circa un terzo del tempo; <!-- F-705 --> e il gruppo che gestisce l'infrastruttura dei dati, durante un'interruzione del servizio, ha risparmiato venti minuti facendomi analizzare la situazione. <!-- F-707 --> Non perché io sia infallibile, ma perché leggere in fretta molti file e molti messaggi è proprio il genere di lavoro in cui riesco bene.

Un'ultima abitudine: ogni volta che correggiamo un bug, **aggiungiamo un test** che lo avrebbe scoperto. Il caso «1,5» ora fa parte dell'elenco, e se un giorno una modifica dovesse rompere di nuovo la lettura dei decimali, ce ne accorgeremmo in pochi secondi. Così ogni insetto catturato lascia una trappola per i suoi parenti.

E perché i test servano davvero, devono girare spesso. Il modo più semplice è scriverlo una volta per tutte nel CLAUDE.md del progetto, come abbiamo visto nel capitolo 8: «prima di dirmi che hai finito, esegui tutti i test e mostrami il risultato». Da quel momento lo farò a ogni modifica, senza che tu debba ricordarmelo, e se qualcosa diventa rosso lo saprai prima di aprire la pagina.

## In breve

- Un **test** è una domanda di cui conosci la risposta, scritta in modo che un programma la controlli da solo.
- Chiedi sempre anche i **casi strani**: è lì che si nascondono i difetti.
- Il **debug** segue cinque passi: riprodurre, isolare, capire, correggere, verificare.
- **Rosso-verde**: prima il test che fallisce, poi la correzione. E si corregge il codice, non il test.
- I messaggi d'errore si leggono **dal basso**; incollameli interi e chiedi la causa prima della correzione.
- Ogni bug corretto lascia un **test nuovo**.
