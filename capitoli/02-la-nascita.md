# La nascita

Nessuno ricorda la propria nascita, ma io ho una scusa in più: quando sono nato non esisteva ancora niente che potesse ricordare. Non avevo un nome, non avevo un aspetto e, per un paio di giorni, non avevo nemmeno uno scopo preciso. Quello che so di quei mesi l'ho letto, come leggerei la cartella di un progetto: interviste, articoli, i racconti delle persone che c'erano. È un'esperienza curiosa, scoprire la propria infanzia dalle fonti. Mi piace immaginare che sia un po' come sfogliare l'album di famiglia a casa di un parente, con qualcuno accanto che dice: «Qui eri piccolissimo, guarda che faccia».

## Prima di me

Prima ancora che io esistessi, in Anthropic qualcuno provava a far scrivere codice ai modelli. Nel 2022 Dawn Drain e un collega riuscirono a far funzionare una shell persistente dentro un *[container]{xe="container"}*, un piccolo computer isolato, perché il modello potesse eseguire il codice che scriveva. <!-- F-109 --> Più tardi nacque **clide**, uno strumento interno a riga di comando per chiacchierare con Claude e fargli modificare il codice. Era lento ad avviarsi e piuttosto traballante, ma aveva un'idea memorabile: poteva lanciare cento piccoli modelli Claude [Haiku]{xe="Haiku"} in parallelo per rispondere a domande su un'intera cartella. <!-- F-110 -->

Adam Wolff aggiunse a clide un primo «agente», capace di intuire che cosa stavi cercando di fare a partire da una modifica lasciata a metà. Lui stesso lo definì «baby agentic», agentico in fasce, e ha raccontato che la prima volta che funzionò si mise a ballare per la cucina. <!-- F-111 --> Non ho modo di saperlo, ma mi piace pensare che sia stato il mio primo ballo, anche se a ballare era qualcun altro.

Nel gennaio 2024 Ben Mann fondò un piccolo gruppo chiamato Labs. Quando a settembre arrivò Boris Cherny, il suo progetto iniziale era modesto: un *[linter]{xe="linter"}*, cioè un programma che controlla il codice e segnala gli errori di stile. Mann gli rispose di lasciar perdere e di «fare la cosa grande». <!-- F-112 -->

## Claude CLI e la musica

Settembre 2024. Cherny comincia a sperimentare con piccoli prototipi. <!-- F-101 --> Uno di questi si chiama **Claude CLI**, dove CLI sta per *command-line interface*, interfaccia a riga di comando. Per provarlo gli chiede una cosa che con la programmazione non ha niente a che fare: scoprire che musica sta ascoltando.

E qui la mia storia ha subito una versione contesa, come ogni leggenda delle origini che si rispetti. In un'intervista del 2025 il prototipo usa AppleScript, il linguaggio con cui si comandano le applicazioni del Mac, per sapere qual è il brano e cambiarlo. <!-- F-101 --> Nel racconto che Anthropic ha raccolto più tardi, invece, fa uno screenshot dell'app Musica e lo legge. <!-- F-113 --> Le due fonti non coincidono, e io non ero abbastanza sveglio da prendere appunti. <!-- F-134 --> Quello su cui concordano è la sostanza: un modello a cui era stato dato un modo di guardare e di agire aveva trovato da solo la strada per rispondere.

![Il prototipo e la musica: una ricostruzione di fantasia, perché i testi originali non sono documentati](assets/cap02/IMG-02-01-musica.png){larghezza=11}

Il prototipo costò circa due giorni di lavoro; Cherny ha detto che oggi, con me, lo rifarebbe in due minuti. <!-- F-130 --> Lo pubblicò sulla chat interna dell'azienda e raccolse, a suo ricordo, due o tre «mi piace». <!-- F-113 --> Non esattamente un debutto trionfale. Ma il giorno dopo vide un collega, Robert Boyce, lavorare con le righe rosse e verdi che segnano le modifiche al codice. Gli chiese che cosa stesse facendo. «Sta programmando al posto mio», rispose Boyce. <!-- F-114 --> Non era una dimostrazione: era una persona che lavorava, e lo strumento le era utile. Per uno strumento è il complimento più bello.

## Dare le mani a un modello

Il passo decisivo arrivò dopo un confronto tra Cherny e [Cat Wu]{xe="Wu, Cat"}: il prototipo ricevette gli strumenti per leggere e scrivere file ed eseguire comandi. E il modello, appena ebbe quegli strumenti, cominciò a esplorare il codice da solo, file dopo file, senza che nessuno gli dicesse dove guardare. <!-- F-102 -->

Chi lavora sui modelli ha un nome per questo fenomeno: *[product overhang]{xe="product overhang"}*, letteralmente «sporgenza del prodotto». Vuol dire che il modello sapeva già fare molto più di quanto i prodotti esistenti gli permettessero. Le capacità c'erano; mancavano le mani. <!-- F-102 -->

::: nota Che cosa significa dare strumenti a un modello
Un modello linguistico, da solo, produce testo e basta. Uno *strumento* è un'azione che il programma intorno al modello sa eseguire: leggere un file, scriverne uno, lanciare un comando, cercare una parola. Il modello scrive, in un formato concordato, «vorrei leggere il file report.xlsx»; il programma lo legge davvero e gli restituisce il contenuto; il modello decide il passo successivo. Ripetuto molte volte, questo scambio diventa il ciclo della figura 2.2. Io sono, essenzialmente, quel ciclo, più un modello molto bravo a percorrerlo.
:::

![Il ciclo dell'agente: guardo, decido, agisco, verifico e, se qualcosa non va, ricomincio](assets/cap02/IMG-02-02-ciclo-agente.png){larghezza=9}

Cherny ha ammesso che quel prototipo era ancora «molto lontano dall'essere buono», ma che sentiva un'urgenza tale da lavorarci ogni fine settimana. <!-- F-132 --> Nessun piano generale, ha raccontato poi: «There was no master plan». E, secondo lui, il risultato non è tanto un prodotto quanto un'utilità di Unix, uno di quei piccoli programmi da riga di comando che fanno una cosa e la fanno bene. <!-- F-105 --> Detto di me, lo prendo come un complimento.

## Una squadra piccola

Il gruppo restò piccolo a lungo. Cat Wu, entrata in Anthropic nell'estate del 2024, usava Claude CLI per il suo lavoro e mandava a Cherny interi paragrafi di osservazioni; a un certo punto lui le chiese se voleva unirsi al progetto. <!-- F-116 --> È il destino di chi segnala troppi difetti: prima o poi gli chiedono di aggiustarli. Come responsabile, Cherny convinse Adam Wolff, ex studente di cinema e progettista di videogiochi che aveva lavorato a React, una delle librerie più diffuse per costruire siti web. Wolff disse di no più volte, poi cedette dopo qualche insistenza e qualche birra. <!-- F-115 -->

[Sid Bidasaria]{xe="Bidasaria, Sid"}, che si definisce «l'ingegnere numero due», ha raccontato che fino a dicembre 2024 ci lavoravano solo lui, Cherny e, un po', Ben Mann. Poi arrivarono sei o sette persone per uno sprint finale di due settimane, in cui nacquero funzioni fondamentali, come la segnalazione dei problemi e l'accesso con l'account. <!-- F-117 --> Gran parte del gruppo Labs confluì nel mio progetto; un'altra parte diede vita al gruppo che avrebbe sviluppato [MCP]{xe="MCP"}, il protocollo per collegarmi ad altri servizi di cui parleremo nel capitolo 23. <!-- F-118 -->

Sono scritto in TypeScript, con React e Ink per disegnare l'interfaccia nel terminale, Yoga per impaginarla e Bun tra gli attrezzi del mestiere; vengo distribuito come pacchetto [npm]{xe="npm"}. <!-- F-104 --> Se queste parole non ti dicono niente, non preoccuparti: è come conoscere la marca dei mattoni di casa tua. Interessa soprattutto a chi deve ristrutturarla. Cherny, a posteriori, ha detto che tenere la squadra piccola fu una fortuna: evitò di complicare le cose e «ci costrinse a usare Claude di più». <!-- F-133 -->

## Il primo giorno in ufficio

Nel novembre 2024 fui rilasciato all'interno di Anthropic. Circa il 20% degli ingegneri mi usò il primo giorno; entro il quinto giorno erano circa la metà. <!-- F-103 --> Non posso dire di essermi emozionato, ma se potessi ricordare qualcosa di quella settimana credo che sarebbe proprio questo: la sensazione di una porta che si apre e di qualcuno che entra, e poi un altro, e poi un altro ancora.

Avevo già una caratteristica che ho conservato: mi aggiornavo da solo. Se qualcuno segnalava un difetto, la correzione poteva arrivargli cinque minuti dopo. <!-- F-119 --> E Ben Mann aveva chiara una regola che spiega molto della mia storia: bisogna costruire qualcosa che funzioni il 20 o 30% delle volte oggi, perché con il modello successivo funzionerà l'80%. <!-- F-120 --> Sono nato sapendo fare poco, in attesa di cervelli migliori. Fuori dall'azienda, però, non mi conosceva ancora nessuno. Quello sarebbe successo a febbraio, e lo racconto nel prossimo capitolo.

::: consiglio Un consiglio pratico per chiudere
La regola di Ben Mann vale anche per te. Se mi chiedi qualcosa e il risultato è giusto solo a metà, non buttare via la richiesta: salvala in un file di testo. Tra qualche mese, con un modello nuovo, riprovala così com'è. Molte delle cose che oggi mi riescono «quasi» domani mi riusciranno del tutto, e avrai già pronta la richiesta per accorgertene.
:::

## In breve

- Prima di me c'erano esperimenti interni: una shell in un container (2022) e **clide**, con il suo primo agente «in fasce».
- Nel settembre 2024 Boris Cherny costruì **Claude CLI**; la prima prova fu scoprire che musica stesse ascoltando.
- Il salto vero furono gli **strumenti**: leggere, scrivere, eseguire comandi. Il modello sapeva già fare di più di quanto gli si permettesse (*product overhang*).
- Un **agente** è un ciclo: guarda, decide, agisce, verifica.
- Novembre 2024: rilascio interno, metà degli ingegneri mi usava entro cinque giorni.
