# Dal requisito al prototipo

Il mio primo prototipo costò al suo autore circa due giorni di lavoro. Boris Cherny ha detto che oggi, con me, lo rifarebbe in due minuti. <!-- F-130 --> Mi piace questa frase, ma non per vanità: perché racconta che cosa è cambiato per chi ha un'idea e non ha mai scritto una riga di codice. In Anthropic, per esempio, il gruppo che analizza i dati ha costruito applicazioni web complete pur ammettendo di non conoscere bene il linguaggio in cui erano scritte. <!-- F-704 --> La distanza tra «mi servirebbe uno strumento che…» e lo strumento vero si è accorciata moltissimo.

Non si è azzerata, però. In mezzo resta un percorso, e questo capitolo lo segue passo per passo con un esempio concreto: un piccolo convertitore di unità di misura. L'ho costruito davvero mentre scrivevo queste pagine, e funziona.

![Il percorso dal requisito al prototipo: la parte importante è il giro tra prototipo e prova](assets/cap10/IMG-10-01-percorso.png){larghezza=13}

## Il requisito: mezza pagina, non un trattato

Tutto comincia con un [requisito]{xe="requisito"}: la descrizione di che cosa deve fare lo strumento. Non serve un documento di trenta pagine; serve la richiesta del capitolo 7, con le sue quattro parti, applicata a qualcosa da costruire. Per il nostro convertitore:

```terminale
> Voglio una pagina web per convertire unità di misura.
  Chi la usa: colleghi d'ufficio, non tecnici.
  Categorie: lunghezza, peso, temperatura.
  Si sceglie la categoria, si scrive un valore, si scelgono
  le unità di partenza e di arrivo; il risultato compare
  subito, con la virgola decimale all'italiana.
  Un solo file, che si apra con un doppio clic, senza
  installare niente. Prima di scrivere codice, proponimi
  un piano.
```

Nota che cosa *non* c'è: nessuna parola tecnica, nessuna scelta di linguaggio. C'è invece chi userà lo strumento, che cosa deve fare e un vincolo pratico importante: un file solo, niente installazioni. Quel vincolo da solo orienta quasi tutte le mie scelte successive.

## Scegliere la tecnologia, o lasciarla scegliere a me

Se non sai quale tecnologia usare, va benissimo: dimmelo, e chiedimi *la soluzione più semplice che funzioni*. Per un convertitore che deve aprirsi con un doppio clic la risposta è quasi obbligata: un unico file [HTML]{xe="HTML"}, la stessa tecnologia delle pagine web, con dentro un po' di [JavaScript]{xe="JavaScript"}, il linguaggio che i browser sanno eseguire. Nessun server, nessuna installazione: il browser che hai già sul computer fa tutto.

Per progetti diversi la scelta sarà diversa. Uno strumento che rielabora fogli Excel ogni mattina sarà più probabilmente uno script Python; un'applicazione usata da più persone con dati condivisi avrà bisogno di un piccolo server, come vedremo nel capitolo 13. L'importante è che la scelta parta dal problema e dai vincoli, non dalla moda. Se ti propongo qualcosa di complicato, chiedimi perché: a volte ho una buona ragione, a volte sto solo esagerando. E non sentirti in dovere di descrivere tutto a parole: se hai già uno schizzo, una tabella o un vecchio modulo da imitare, dammelo. In Anthropic i designer mi hanno affidato direttamente i loro progetti grafici, chiedendomi di realizzarli e di prevedere i casi in cui qualcosa va storto. <!-- F-703 --> Un disegno fatto a mano e fotografato con il telefono, per una pagina semplice, fa un ottimo lavoro.

::: nota Tre parole da riconoscere
**HTML** è il linguaggio con cui si descrive una pagina web: titoli, caselle, pulsanti. **JavaScript** è il linguaggio che dà vita alla pagina: quando cambi un valore, è JavaScript che ricalcola il risultato. Entrambi funzionano dentro qualunque browser, senza installare niente. **Python** è un linguaggio molto usato per lavorare con file e dati, come i fogli Excel o i PDF: lo incontrerai spesso nella parte IV. Non serve saperli scrivere. Serve riconoscerli, per capire che cosa ti sto proponendo.
:::

## Il primo prototipo

Dopo il piano, che ti presento in plan mode e tu approvi, scrivo il file `convertitore.html`: un centinaio di righe, che a te non costano nessuna fatica. Poi tocca a te: apri il file con un doppio clic e prova. La figura 10.2 mostra il risultato.

![La mini-app: un file HTML che si apre nel browser con un doppio clic](assets/cap10/IMG-10-02-app.png){larghezza=7}

Il [prototipo]{xe="prototipo"} non deve essere perfetto: deve essere *abbastanza buono da poterlo usare e criticare*. È per questo che conviene chiedere prima la versione minima, quella con l'indispensabile, e aggiungere il resto dopo averla provata. Se avessimo chiesto subito venti categorie, la cronologia delle conversioni e il tema scuro, avresti dovuto controllare tutto insieme, e un errore in un angolo sarebbe passato inosservato.

Non devi leggere il codice, ma se lo apri scoprirai che è meno misterioso di quanto sembri. Ecco, per esempio, la parte che converte le temperature, con i commenti in italiano che ti chiedo sempre di scrivere:

```javascript
// La temperatura non si converte con un fattore:
// servono formule
function aCelsius(v, u) {
  if (u === "gradi Fahrenheit") return (v - 32) * 5 / 9;
  if (u === "kelvin") return v - 273.15;
  return v;
}
```

Anche senza conoscere JavaScript, si capisce che cosa fa: se il valore è in Fahrenheit, applica la formula; se è in kelvin, sottrae 273,15; altrimenti lo lascia com'è.

## Un passo alla volta

Ora si gira nel cerchio della figura 10.1: provi, noti qualcosa, me lo dici, correggo. Nel caso del convertitore, le richieste successive potrebbero essere:

1. «Aggiungi un pulsante per scambiare le unità di partenza e di arrivo.»
2. «I numeri lunghi sono illeggibili: mostra al massimo quattro decimali.»
3. «Se scrivo una lettera invece di un numero, dimmi di scrivere un numero invece di mostrare NaN.»

Ogni richiesta è piccola, si verifica in pochi secondi e non rompe quello che funzionava già. È il metodo con cui lavorano bene le persone e con cui lavoro bene io: piccoli passi verificati battono grandi balzi sperati.

Prima o poi, però, arriva una richiesta diversa dalle altre. Per il convertitore potrebbe essere: «aggiungi le valute». Sembra una categoria in più, come la temperatura, ma non lo è: i cambi variano ogni giorno, quindi la pagina dovrebbe collegarsi a internet e fidarsi di una fonte esterna, e il vincolo «un file solo, niente di complicato» salterebbe. Quando una richiesta cambia la natura del progetto, fermati e chiedimi di spiegarti le conseguenze prima di procedere. Io te le dirò; ma la decisione è tua, perché solo tu sai se ne vale la pena.

::: consiglio Dammi un modo per controllare
Per il convertitore il criterio di «fatto» è semplice: alcune conversioni di cui conosciamo il risultato. Un miglio è circa 1,6093 chilometri, −40 gradi Celsius sono esattamente −40 Fahrenheit, 100 gradi Celsius sono 373,15 kelvin. Mentre scrivevo questo capitolo ho fatto proprio queste prove sulla pagina, con un programma che la apre, compila i campi e legge il risultato. Chiedimelo sempre: «prima di dirmi che hai finito, verifica questi casi».
:::

## Quando fermarsi

Un prototipo serve a rispondere a una domanda: *questo strumento mi è utile?* Se la risposta è sì, puoi continuare a migliorarlo, oppure fermarti: un convertitore che fa bene tre cose è meglio di uno che ne fa male trenta. Se la risposta è no, hai perso mezz'ora invece di un mese, e anche questo è un ottimo risultato. Un prototipo scartato non è un fallimento: è una domanda a cui hai risposto in fretta, e con poca spesa.

Se lo strumento ti è utile, probabilmente lo sarà anche ai colleghi. Un file HTML come il nostro si condivide come qualunque documento: in una cartella comune o per email. Prima di farlo, però, chiedimi una revisione con occhi nuovi: «rileggi il file come se lo vedessi per la prima volta e dimmi che cosa potrebbe confondere un collega». È sorprendente quante piccole cose si notano così.

C'è un'altra domanda, però, che arriva presto: *come faccio a sapere che continuerà a funzionare quando lo modificheremo di nuovo?* La risposta si chiama test, ed è l'argomento del prossimo capitolo.

## In breve

- Un **requisito** è mezza pagina: chi lo usa, che cosa deve fare, i vincoli. Niente gergo.
- Se non sai quale tecnologia usare, chiedi **la soluzione più semplice che funzioni**.
- Il **prototipo** è la versione minima, abbastanza buona da essere usata e criticata.
- Si migliora **un passo alla volta**: ogni modifica piccola e verificata.
- Dai sempre un **criterio di controllo**: casi di cui conosci il risultato.
