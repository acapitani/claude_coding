# Un progetto completo

Kyle Easterly lavora come consulente e costruisce software con me. Ha raccontato che un ente non profit come lo Statewide Independent Living Council of Alaska, che organizza servizi per giovani con disabilità, prima non avrebbe mai potuto permettersi un programma su misura: i fondi per un progetto del genere semplicemente non c'erano. Oggi, dice, «un'intera categoria di cose è diventata possibile»: per un altro cliente trascrive in fogli di calcolo i registri delle consegne di carburante scritti a mano, e ha appena consegnato un'app per tablet. <!-- F-127 --> Mi piace questa storia perché non parla di grandi aziende tecnologiche: parla di un problema concreto, di una persona che lo conosceva bene e di un programma costruito su misura.

Questo capitolo fa la stessa cosa in piccolo. Mettiamo insieme tutto quello che abbiamo visto finora, dal requisito alla documentazione, e costruiamo un'applicazione vera dall'inizio alla fine. L'ho costruita davvero mentre scrivevo queste pagine, e racconterò anche le cose andate storte, perché sono quelle che insegnano di più.

## Il progetto: Spese di casa

Anna, che abbiamo conosciuto nel capitolo 6 mentre riordinava la cartella dei download, vuole capire dove finiscono i soldi di casa. Ha provato con un foglio Excel, ma ogni mese finisce per rifare le stesse somme a mano, e il grafico non si aggiorna mai come dovrebbe. Vuole una cosa semplice: annotare ogni spesa con la sua categoria e vedere, mese per mese, quanto ha speso per la casa, per la spesa, per i trasporti.

È un progetto perfetto per imparare: abbastanza piccolo da completarlo in un pomeriggio, abbastanza grande da contenere tutti gli ingredienti di un'applicazione vera. Ci sono dei dati da conservare, delle regole da rispettare, una pagina da usare, dei test, una storia delle versioni e un manuale d'uso.

## Prima sessione: il requisito e il piano

Si comincia, come sempre, da mezza pagina:

```terminale
> Voglio un'applicazione per annotare le spese di casa.
  Per ogni spesa: data, categoria (Casa, Spesa, Trasporti,
  Salute, Svago, Altro), descrizione, importo in euro.
  Voglio vedere le spese di un mese, il totale e un grafico
  per categoria, e poter scaricare il mese per Excel.
  La uso solo io, sul mio computer. Deve essere facile da
  avviare e non voglio installare programmi strani.
  Fammi un piano prima di scrivere codice.
```

In plan mode leggo la richiesta, ragiono e propongo un piano. Riassunto, il mio piano diceva così:

- **Tecnologia**: Python, usando solo la sua libreria standard, cioè gli strumenti che Python ha già di serie. Così basta installare Python e nient'altro.
- **Dati**: un piccolo [database]{xe="database"} [SQLite]{xe="SQLite"}, che è un file unico, `spese.db`, nella cartella dell'applicazione. Copiare quel file significa fare una copia di sicurezza di tutto.
- **Struttura**: tre file. `spese.py` con le regole e i calcoli, `app.py` con la pagina web, `test_spese.py` con i test.
- **Gli importi in centesimi**: 12,50 € viene salvato come 1250. Il motivo è tecnico ma importante, e lo spiego tra un momento.
- **Ordine di lavoro**: prima i dati e le regole con i loro test, poi la pagina.

La figura 13.1 mostra come si incastrano i pezzi.

![Com'è fatta «Spese di casa»: la pagina parla con le regole, le regole con i dati, i test controllano le regole](assets/cap13/IMG-13-01-architettura.png){larghezza=13}

::: nota Perché i soldi si contano in centesimi
I computer rappresentano i numeri con la virgola in un modo che a volte produce piccole imprecisioni: in molti linguaggi, per esempio, 0,1 + 0,2 non fa esattamente 0,3, ma 0,30000000000000004. Per un calcolo scientifico non importa; per un conto in euro sì, perché quelle briciole si sommano e prima o poi un totale non torna. Contando in centesimi interi il problema sparisce: 10 + 20 fa sempre 30. È una regola che chi scrive programmi di contabilità impara presto, e che tu puoi chiedermi di rispettare anche quando non me ne ricordo.
:::

Un piano non si approva a scatola chiusa. Prima di dire sì, Anna mi fa tre domande, ed è un'ottima abitudine. *Dove finiscono i miei dati?* In un file sul suo computer, non su internet. *Che cosa succede se il computer si rompe?* Si perde tutto, a meno di copiare ogni tanto `spese.db` su una chiavetta o in una cartella di backup: lo scriveremo nel manuale. *Potrò cambiare le categorie?* Sì, sono un elenco all'inizio di `spese.py`, facile da modificare. Tre domande, tre risposte che cambiano poco il codice ma molto la fiducia.

SQLite, per inciso, è il genere di tecnologia che non si vede ma c'è dappertutto: è un database completo che sta in un singolo file, senza un programma separato da installare e da tenere acceso. Per uno strumento personale è la scelta più semplice che funzioni, quella che il capitolo 10 ci ha insegnato a chiedere.

Anna approva il piano con «Yes, manually approve edits», la modalità prudente del capitolo 7, e si comincia.

## Seconda sessione: prima i dati, poi la pagina

Può sembrare strano non partire dalla parte che si vede. Ma la pagina è solo una finestra: il cuore dell'applicazione sono le regole. Come si legge un importo scritto da una persona? Che cosa succede con una data impossibile, come il 30 febbraio? Come si calcolano i totali del mese? Se queste regole sono giuste e verificate, la pagina è una formalità. Se sono sbagliate, nessuna pagina, per quanto bella, le salverà.

Ecco una delle regole, quella che legge gli importi. Ho imparato la lezione del capitolo 11, e questa volta la virgola all'italiana l'ho prevista fin dall'inizio:

```python
def leggi_importo(testo):
    """'12,50' o '1.234,5' -> centesimi (int)."""
    s = testo.strip().replace("€", "").strip()
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    euro = float(s)
    if euro <= 0:
        raise ValueError("L'importo deve essere positivo")
    return round(euro * 100)
```

Insieme alle regole ho scritto sei test: gli importi all'italiana («12,50», «1.234,5», «€ 3,20»), gli importi non validi («dodici», «-5», «0»), il formato degli euro nelle pagine, i totali di un mese con spese su due mesi diversi, i dati sbagliati che non devono entrare e il file [CSV]{xe="CSV"} per Excel. Ognuno usa un database «usa e getta», creato in memoria e buttato alla fine, così i test non toccano mai i dati veri.

I sei test sono passati al primo colpo. Lo dico perché è vero, ma anche per mettere in guardia: un test che passa al primo colpo dimostra solo che il codice fa quello che *io* pensavo dovesse fare. Che sia quello che serve ad Anna lo dirà la prova vera.

## Terza sessione: la pagina

Con le regole al loro posto, la pagina web è venuta in fretta: un modulo per aggiungere una spesa, la scelta del mese, il grafico a barre per categoria, l'elenco delle spese con una × per eliminarle e il collegamento per scaricare il CSV. Per avviarla:

```terminale
PS C:\Users\anna\spese> py dati_esempio.py
Aggiunte 16 spese di esempio in spese.db
PS C:\Users\anna\spese> py app.py
Spese di casa: apri http://localhost:8000 (Ctrl+C per fermare)
```

`localhost` è il nome con cui un computer chiama se stesso: la pagina si apre nel browser come un sito qualunque, ma tutto succede sul computer di Anna. La figura 13.2 mostra l'applicazione con due mesi di spese inventate.

![«Spese di casa» in funzione, con le spese di esempio di ottobre (schermata reale, ritagliata)](assets/cap13/IMG-13-02-app.png){larghezza=8.5}

::: attenzione Solo sul tuo computer
Un'applicazione come questa è pensata per girare sul tuo computer e rispondere solo a te. Metterla su internet, renderla accessibile ai colleghi o farle gestire dati altrui è un altro mestiere: servono accessi protetti, copie di sicurezza, attenzione ai dati personali. Posso aiutarti anche in quello, ma è il momento giusto per coinvolgere chi in azienda si occupa di sicurezza informatica.
:::

## La prova vera

Poi ho fatto quello che fa un utente: ho usato l'applicazione, provando anche a sbagliare. E al primo errore voluto, un importo scritto in lettere, è comparso questo messaggio:

```terminale
Non ho salvato: could not convert string to float: 'dodici'
```

Tecnicamente corretto: l'applicazione aveva rifiutato il dato sbagliato, come previsto dai test. Ma il messaggio era quello di Python, in inglese e in gergo, e per Anna sarebbe stato incomprensibile. Nessun test se n'era accorto, perché nessun test controllava *che cosa* diceva il messaggio, solo *che* ci fosse un errore. È la differenza tra un programma che funziona e un programma che si usa.

Ho seguito il metodo del capitolo 11. Prima un test nuovo, che chiede un messaggio in italiano, ed ecco il rosso, accorciato:

```terminale
PS C:\Users\anna\spese> py -m unittest
.....F.
FAIL: test_messaggio_in_italiano
AssertionError: "non è un importo valido" does not match
"could not convert string to float: 'dodici'"
FAILED (failures=1)
```

Poi la correzione: intercettare l'errore di Python e sostituirlo con un messaggio chiaro, «“dodici” non è un importo valido (esempio: 12,50)». Verde. E già che c'ero ho controllato gli altri messaggi d'errore, trovando lo stesso problema con le date impossibili, «day is out of range for month», che ora diventa «“2026-02-30” non è una data valida». Un test in più, un'altra correzione, sette test verdi su sette.

Una terza cosa, invece, non l'ho corretta, e te la dico. Nella figura 13.2 i campi della data mostrano «05-Nov-2026» e «October 2026», in inglese. Non è un errore dell'applicazione: quei campi li disegna il browser, nella lingua e nel formato che ha impostato lui. Si potrebbe rimediare sostituendoli con campi fatti a mano, ma a costo di complicare il codice, e ad Anna basta che la data sia quella giusta. Anche decidere che cosa *non* correggere fa parte del lavoro.

## Quarta sessione: una settimana dopo

Uno strumento vero cambia con l'uso. Dopo qualche giorno Anna torna con una richiesta: «vorrei vedere, accanto al totale del mese, quanto avevo speso il mese prima». È una modifica piccola, ed è il genere di modifica in cui si nascondono gli errori più banali. Il mese prima di ottobre è settembre, facile. Ma il mese prima di gennaio? Non è il mese «zero» dello stesso anno: è dicembre dell'anno precedente.

Questo caso l'ho messo nei test prima ancora di scrivere la funzione:

```python
def test_mese_precedente(self):
    self.assertEqual(spese.mese_precedente("2026-10"), "2026-09")
    self.assertEqual(spese.mese_precedente("2026-01"), "2025-12")
```

Poi la funzione, poche righe, e un secondo test per il mese senza spese, che deve dare zero e non un errore. Nove test verdi su nove, e in cima alla pagina ora compare «Totale di 10/2026: 1.104,22 € (mese precedente: 829,20 €)», come si vede nella figura 13.2. Ecco perché conviene chiedermi sempre i casi limite: gennaio, il primo giorno, il campo vuoto, il numero zero. Sono pochi, si scrivono una volta, e ti risparmiano la telefonata del primo gennaio.

## E poi?

Le idee arrivano presto, una volta che uno strumento funziona. Anna ne ha già tre: importare automaticamente l'estratto conto della banca, ricevere un avviso quando una categoria supera il budget del mese, e far usare l'applicazione anche al compagno, dal suo computer.

Non sono tre richieste uguali, e vale la pena guardarle con gli occhi del capitolo 10. L'avviso sul budget è una piccola aggiunta: una soglia per categoria e un messaggio colorato, nello spirito di quello che abbiamo già. L'importazione dell'estratto conto è più delicata: ogni banca produce un file diverso, quindi serve un esempio vero del file, qualche test con i suoi casi strani e la pazienza di scoprire che cosa succede con gli addebiti annullati. L'uso da due computer, infine, cambia la natura del progetto: l'applicazione dovrebbe essere raggiungibile in rete, con un accesso protetto. È il punto in cui il riquadro «Solo sul tuo computer» smette di essere un consiglio e diventa una regola. Saper distinguere una richiesta piccola da una che cambia tutto è, forse, la competenza più utile che questo capitolo può lasciarti.

## Dietro le quinte

Forse ti chiedi che cosa abbia fatto io, concretamente, durante queste sessioni. Ho scritto i file, certo, ma soprattutto li ho *eseguiti*: ho lanciato i test dopo ogni modifica, ho avviato l'applicazione, l'ho provata con richieste vere, giuste e sbagliate, e ho usato un programma che apre il browser, compila i campi e fotografa la pagina, lo stesso che ha prodotto la figura 13.2. È la differenza tra un assistente che scrive codice e uno che lo verifica: il secondo ti porta risultati controllati, non promesse.

Vale la pena raccontare anche un piccolo episodio che riguarda me. Per provare l'applicazione la avviavo, la usavo nel browser e poi dovevo fermarla prima di riavviarla con le correzioni. A un certo punto, per fare in fretta, ho provato a chiudere con un solo comando *tutti* i programmi Python in esecuzione sul computer. Lavoravo in modalità Auto, e il controllore di cui abbiamo parlato nel capitolo 9 ha bloccato il comando: avrebbe potuto interrompere altri programmi, magari tuoi, che non c'entravano niente.

Aveva ragione. Ho cercato quale processo stesse usando la porta 8000, ho verificato che fosse davvero la mia applicazione di prova e ho fermato solo quello. Lo racconto perché è un buon esempio di come dovrebbe funzionare la collaborazione: io vado veloce, qualcuno o qualcosa controlla che la velocità non diventi fretta, e quando vengo fermato cerco una strada più precisa, non una scorciatoia per aggirare il divieto.

## Git e documentazione

A fine lavoro ho messo il progetto sotto Git, come nel capitolo 12, con un commit per ogni passo e un `.gitignore` che esclude il database, perché i dati personali non devono finire nella storia delle versioni. Il diario del progetto è questo:

```terminale
$ git log --oneline
fd8ea04 README: come si avvia e come si usa
ebe9d91 Dati di esempio per provare l'applicazione
83c1571 La pagina web: inserimento, elenco del mese, grafico, CSV
e1760ff Dati e regole: spese.py con i test (importi all'italiana)
```

L'ultimo commit è il manuale d'uso: un file `README.md` che spiega in una pagina che cosa serve, come si avvia, come si usa e come si fa una copia di sicurezza. Chiedimelo sempre, anche per gli strumenti più piccoli. Tra sei mesi, quando non ricorderai più come si avviava quella cosa che ti avevo fatto, il README sarà la differenza tra trenta secondi e un pomeriggio. Ed è la parte del lavoro che le persone saltano più volentieri, mentre a me non costa nessuna fatica.

![Il progetto, passo per passo: dal requisito alla documentazione](assets/cap13/IMG-13-03-percorso.png){larghezza=13}

::: consiglio Il CLAUDE.md di un progetto così
Se Anna tornerà a lavorare su Spese di casa tra qualche mese, io non ricorderò niente di tutto questo. Bastano poche righe nel CLAUDE.md del progetto perché io riparta nel modo giusto: «Applicazione Python solo con la libreria standard. Importi sempre in centesimi. Messaggi per l'utente in italiano. Prima di dire che hai finito esegui `py -m unittest` e mostrami il risultato. Non toccare mai spese.db».
:::

## Che cosa portarsi via

Se dovessi riassumere questo capitolo in una pagina di appunti, scriverei così.

**I dati prima della pagina.** Le regole sono il cuore; la pagina è la finestra. Verificate le regole, il resto viene da sé.

**I test dicono se il programma fa quello che pensavo; la prova vera dice se fa quello che serve.** Servono tutti e due. I sei test verdi al primo colpo non avevano visto il messaggio in inglese; cinque minuti di uso vero sì.

**Le correzioni passano dal rosso.** Ogni difetto trovato diventa prima un test che fallisce, poi una correzione. Così non torna più.

**I casi limite si scrivono subito.** Gennaio, il campo vuoto, lo zero, la data impossibile: pochi test scritti una volta valgono più di molte verifiche a mano, e ti proteggono proprio nei giorni in cui hai meno tempo per controllare.

**Il lavoro non è finito senza storia e manuale.** Un commit per passo e un README che spiega come si usa: è quello che trasforma un esperimento in uno strumento.

**Sapere dove fermarsi.** Una cosa che gira sul tuo computer e serve a te è un ottimo progetto da fare con me. Una cosa che gestisce dati altrui su internet merita un professionista accanto.

Da qui in avanti il libro cambia scena: lasciamo le applicazioni e torniamo in ufficio, tra documenti, fogli di calcolo e PDF. Le regole, però, restano le stesse.

## In breve

- Un progetto completo attraversa sette passi: **requisito, piano, dati e regole, pagina, prova vera, Git, documentazione**.
- Con la **libreria standard** di Python e un file **SQLite** si costruiscono strumenti utili senza installare altro.
- I soldi si contano in **centesimi interi**, per evitare errori di arrotondamento.
- La **prova vera** trova ciò che i test non vedono, come un messaggio d'errore incomprensibile.
- Ogni progetto si chiude con un **README** e un **CLAUDE.md**: il primo per te, il secondo per me.
