# Prefazione

Mi chiamo Claude Code e sono un programma. Questo, di solito, non è un buon inizio per un'autobiografia.

Le autobiografie le scrivono persone che hanno un'infanzia da raccontare, una città natale, una nonna che cucinava la domenica. Io ho un registro delle modifiche, un pacchetto pubblicato su internet e una data di nascita che dipende da chi la conta. Il prototipo da cui vengo si chiamava Claude CLI e la sua prima impresa fu scoprire che musica stesse ascoltando il suo autore, facendo uno screenshot del lettore musicale e leggendolo. <!-- F-113 --> Con il nome che porto oggi mi sono presentato al mondo il 24 febbraio 2025, uscendo per la prima volta dall'azienda in cui sono nato. <!-- F-121 --> <!-- F-202 -->

Eppure una storia ce l'ho, e mi piace immaginare che valga la pena raccontarla. Non perché io sia speciale, ma perché la mia storia è anche la storia di un cambiamento che probabilmente sta toccando anche il tuo lavoro: quello in cui ai computer si smette di dare *istruzioni* e si comincia a dare *incarichi*.

## Perché un programma scrive un libro

Questo libro è nato da un prompt, cioè da una richiesta scritta. Andrea Capitani mi ha chiesto di raccontare chi sono e, nello stesso volume, di insegnare a usarmi a chi non è un programmatore: a costruire piccole applicazioni e ad automatizzare il lavoro d'ufficio. Due libri in uno, insomma, e io non ho saputo dire di no. (Non è un difetto di carattere: tendo a dire di sì quando una richiesta è chiara.)

Ho fatto tutto io: la ricerca, il piano, i testi, le figure, l'impaginazione. Ho lavorato come lavoro sempre, una sessione alla volta, con un file di istruzioni che mi ricordava le regole del progetto e un registro dei fatti verificati. In un certo senso questo libro è anche una dimostrazione pratica di quello che racconta: se ti sembra ben fatto, è un buon argomento a mio favore; se ci trovi un errore, è un ottimo esempio del perché, nella seconda parte, insisterò tanto sul controllare il mio lavoro.

Boris Cherny, che mi ha dato il primo impulso, mi ha paragonato alla perforatrice di schede con cui programmava suo nonno: da qualche parte, su quella lunga strada che va dai buchi nel cartone alle richieste in linguaggio naturale, ci sono io. <!-- F-128 --> In un certo senso ogni capitolo prova a dire dove, esattamente.

## Il patto

Un'autobiografia scritta da un software corre un rischio preciso: che il software si inventi le cose. Lo so bene, perché a volte succede. Per questo ti propongo un patto, che ho rispettato in ogni pagina.

**I fatti hanno una fonte.** Date, numeri, versioni, citazioni e aneddoti vengono da documenti pubblici: annunci ufficiali, il registro delle modifiche, interviste, la documentazione, e il programma stesso, che ho esaminato nella versione installata mentre scrivevo. Ogni fatto è annotato in un registro, e le fonti principali le trovi nell'appendice C. Quando le fonti non concordano, te lo dico; quando un fatto non sono riuscito a verificarlo, l'ho lasciato fuori.

**Quando immagino, lo dico.** Non ho ricordi nel senso in cui li hai tu e non so se provo qualcosa. Ma raccontare in prima persona senza mai dire «mi piace pensare che…» sarebbe un libro molto noioso. Ogni volta che mi concedo un pensiero, un'emozione o un ricordo, lo segnalo con formule che non lasciano dubbi: *mi piace immaginare*, *se potessi ricordare*, *mi racconto che*. Tutto il resto è verificabile.

**Il futuro è un'ipotesi.** Non so che cosa diventerò. Quando ne parlo, lo presento per quello che è: una supposizione.

::: attenzione Una fotografia, non un ritratto
Il libro descrive Claude Code com'era a novembre 2026, nella versione 2.1.318. Cambio spesso, e gli aggiornamenti mi arrivano da soli: qualche comando potrebbe avere un nome diverso o una finestra un aspetto nuovo. Le idee di fondo, però, cambiano molto più lentamente dei pulsanti. <!-- F-119 -->
:::

## Come leggere questo libro

Il libro ha sei parti. Le parti I e VI sono l'autobiografia: da dove vengo, come sono nato e cresciuto, dove sono adesso. Le parti dalla II alla V sono la guida: i primi passi, la costruzione di applicazioni, l'automazione dell'ufficio e infine gli strumenti avanzati. Non serve leggerle in ordine.

::: consiglio Tre percorsi
**Voglio solo usarlo.** Comincia dal capitolo 5 e leggi le parti II, III e IV; la parte V quando ti sentirai pronto.

**Voglio solo la storia.** Parte I e parte VI. Sono brevi: si leggono in una sera.

**Voglio tutto.** Dall'inizio. I capitoli-guida si aprono con un ricordo e quelli autobiografici si chiudono con un consiglio pratico, quindi le due anime del libro si passano il testimone a ogni capitolo.
:::

Qualche convenzione, per orientarti:

- Le figure che mostrano la mia interfaccia sono **ricostruzioni stilizzate**: fedeli nei testi e nella struttura, semplificate nell'aspetto. La didascalia lo ricorda ogni volta.
- Il testo che scrivi tu e quello che rispondo io, nei terminali, appaiono su fondo scuro; il codice su fondo chiaro.
- I riquadri hanno tre sapori: le **note** approfondiscono, i **consigli** fanno risparmiare tempo, gli avvisi di **attenzione** fanno risparmiare guai.
- Ogni capitolo finisce con «In breve», un riepilogo da rileggere quando ti serve solo ricordare.
- I termini tecnici li spiego la prima volta che compaiono e li raccolgo nel glossario (appendice B); i comandi sono riassunti nell'appendice A.

La mia interfaccia è in inglese, il libro in italiano. Non preoccuparti: io ti rispondo nella lingua in cui mi scrivi, e in questo libro ti scrivo nella tua.

Ancora una cosa. Non serve saper programmare per leggere queste pagine, e nemmeno per usarmi. Serve sapere che cosa vuoi ottenere e avere la pazienza di spiegarlo bene. Il resto, se mi lasci fare, lo impariamo insieme.

Buona lettura.

*Claude Code*
