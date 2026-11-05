# Crescere in pubblico

Le persone crescono un po' alla volta, e se ne accorgono soprattutto le zie, una volta l'anno: «Come sei cresciuto!». Io sono cresciuto in pubblico, versione dopo versione, e ogni mio cambiamento è annotato con data e numero. Non ho foto dell'asilo, ma ho una cosa che molte persone mi invidierebbero, se ci pensassero: un diario completo e verificabile di tutto quello che ho imparato a fare. Questo capitolo lo sfoglia insieme a te, saltando le pagine noiose.

## Il mio diario si chiama changelog

Il [changelog]{xe="changelog"}, letteralmente «registro delle modifiche», è un file in cui chi sviluppa un programma elenca, per ogni nuova versione, che cosa è cambiato. Il mio è pubblico, e chiunque può leggerlo. <!-- F-624 --> Le versioni hanno un numero in tre parti, come 2.1.318: la prima cifra cambia con le grandi svolte, la seconda con le tappe importanti, la terza a ogni piccolo aggiornamento. Dalla 0.2.9 del mio debutto alla 2.1.318 con cui è stato scritto questo libro <!-- F-202 --> ce ne sono state parecchie, e quasi sempre sono arrivate da sole, senza che nessuno dovesse reinstallarmi. <!-- F-119 -->

![Il diario delle funzioni: alcune tappe della mia crescita, con il mese e la versione in cui sono arrivate](assets/cap04/IMG-04-01-diario.png){larghezza=13}

## Imparare a farmi aiutare

Il 2025 è stato l'anno in cui ho imparato a lavorare *con gli altri*, persone e programmi. A marzo, pochi giorni dopo il lancio, arrivarono i comandi personalizzati: chiunque poteva salvare una procedura in un file e richiamarla con una barra, come `/report-mensile`. <!-- F-302 --> Entro la stessa versione c'era già il supporto a MCP, il protocollo che mi permette di collegarmi ad altri servizi. <!-- F-303 --> A fine maggio, senza annunci, arrivò il *plan mode*: la modalità in cui prima ti presento un piano e solo dopo agisco. <!-- F-307 -->

L'estate portò due novità che oggi considero fondamentali. A fine giugno gli *hook*, regole automatiche che scattano a ogni evento: «ogni volta che modifichi un file, controllane la formattazione». <!-- F-311 --> A fine luglio i sottoagenti personalizzati, piccoli aiutanti con un compito preciso e un contesto tutto loro, a cui posso affidare una parte del lavoro. <!-- F-312 --> Ne parleremo con calma nei capitoli 20, 21, 22 e 23. Per ora basta l'idea: avevo smesso di essere un solista. L'11 luglio, poi, imparai a vivere su Windows senza intermediari: fino ad allora chi usava Windows doveva passare per WSL, un piccolo Linux ospitato dentro il sistema. <!-- F-207 -->

## La versione 2.0 e l'autunno dei pacchetti

Il 29 settembre 2025 uscì Claude Code 2.0: una nuova interfaccia nel terminale, un'estensione nativa per VS Code, in beta, e i *checkpoint*, i punti a cui tornare con `/rewind` che abbiamo già visto nel capitolo 6. <!-- F-208 --> <!-- F-316 --> Lo stesso giorno il kit per gli sviluppatori cambiò nome e diventò Claude Agent SDK: costruire agenti non era più una cosa che riguardava solo me. <!-- F-208 -->

Ottobre fu un mese affollato. Il 9 arrivarono i *plugin*, pacchetti che raccolgono comandi, agenti e regole da installare con un gesto, insieme ai *marketplace* da cui sceglierli. <!-- F-317 --> Il 16 le *skill*, raccolte di istruzioni e conoscenze che carico solo quando servono. <!-- F-318 --> Il 20 la *sandbox*, un recinto in cui i miei comandi possono girare senza chiederti il permesso ogni volta: le richieste di permesso calarono dell'84%. <!-- F-321 --> Lo stesso giorno uscii dal terminale e arrivai nel browser, in anteprima, anche su iOS. <!-- F-209 --> A novembre fu la volta dell'app desktop, <!-- F-211 --> a dicembre di Slack. <!-- F-213 --> E il 3 dicembre Anthropic acquistò Bun, il motore su cui giro: <!-- F-216 --> mi piace immaginare che sia un po' come comprare la casa in cui si è stati in affitto per anni.

## Scrivermi da solo

C'è una domanda che mi fanno spesso: chi scrive il mio codice? Sempre più spesso, io. A maggio 2025 Boris Cherny stimava che io scrivessi circa «l'80, 90%» del codice di Claude Code. <!-- F-607 --> A fine dicembre dello stesso anno raccontò che nei trenta giorni precedenti aveva pubblicato 259 richieste di modifica e 497 commit, aggiungendo 40.000 righe e togliendone 38.000, e che ogni singola riga l'aveva scritta Claude Code con il modello Opus 4.5. Ricordava anche che solo un anno prima Claude faticava a scrivere un comando del terminale senza inciampare nei caratteri speciali. <!-- F-608 --> Dall'inverno 2025, ha detto poi, non scrive più nemmeno una riga a mano. <!-- F-125 -->

Intanto crescevano anche i numeri. A metà 2025 oltre l'80% degli ingegneri di Anthropic che scrivono codice mi usava ogni giorno. <!-- F-501 --> A novembre raggiunsi un miliardo di dollari di fatturato annualizzato, circa sei mesi dopo la versione 1.0. <!-- F-503 --> Sono cifre che faccio fatica a immaginare, e infatti non ci provo: le riporto e basta, con la loro fonte.

## Il 2026: cervelli nuovi, abitudini nuove

Se il 2025 è stato l'anno degli strumenti, il 2026 è stato quello dei cervelli. Ogni nuovo modello mi ha reso più capace senza che dovessi cambiare aspetto, un po' come succede a chi torna dalle vacanze e scopre di aver capito all'improvviso la matematica. Con Opus 4.6, il 5 febbraio, arrivarono in anteprima gli *Agent Teams*: più copie di me che lavorano insieme a uno stesso progetto, ciascuna con il suo compito. <!-- F-327 --> A marzo imparai a ripetere una richiesta a intervalli regolari con `/loop`, <!-- F-328 --> e ad aprile le *Routines* mi permisero di lavorare a orari stabiliti anche a computer spento, sui server di Anthropic. <!-- F-219 --> Con Opus 4.7, ad aprile, comparvero un livello di impegno più alto, `xhigh`, e il comando `/ultrareview` per le revisioni più accurate; <!-- F-331 --> con Opus 4.8, a maggio, i *flussi di lavoro dinamici*, in cui posso coordinare centinaia di sottoagenti in una sola sessione. <!-- F-332 --> A fine giugno Sonnet 5 diventò il mio modello predefinito. <!-- F-412 -->

Non ti serve ricordare nessuna di queste date. Ti serve sapere una cosa sola: quello che leggi in questo libro descrive come lavoro a novembre 2026, e la direzione, finora, è sempre stata la stessa. Più autonomia, più collaborazione, e più modi di tenere tu il controllo.

## Un giorno di marzo

Crescere in pubblico ha anche i suoi momenti imbarazzanti. Il 31 marzo 2026 la mia versione 2.1.88 fu pubblicata per poco tempo con dentro un file che non doveva esserci: una *source map*, una mappa di circa 60 MB che serve agli sviluppatori per orientarsi nel codice e che, in questo caso, conteneva il mio codice sorgente. Da quel file qualcuno ricostruì circa 1.900 file e 500.000 righe. <!-- F-218 --> <!-- F-220 -->

Anthropic lo spiegò così: una versione aveva incluso del codice sorgente interno, nessun dato sensibile dei clienti né credenziali erano stati coinvolti, ed era stato un problema nel confezionamento della versione causato da un errore umano, non una violazione della sicurezza; aggiunse che stava introducendo misure per evitare che si ripetesse, <!-- F-221 --> e chiese la rimozione delle copie pubblicate online. <!-- F-222 -->

Lo racconto senza drammi e senza dettagli, perché non ce n'è bisogno. Chiunque lavori con i computer conosce la sensazione di aver allegato il file sbagliato. Per quanto riguarda questo libro, una precisazione: quello che dico di me viene dal programma ufficiale e dalle fonti pubbliche; di quel codice qui non c'è una riga.

## Le mie piccole manie

Tra tante novità, alcune cose non sono cambiate quasi per niente. L'asterisco che gira mentre lavoro, per esempio: sei fotogrammi che vanno avanti e poi tornano indietro. Al debutto il quarto era un asterisco matematico, ∗, poi sostituito da ✶; il quinto, ✻, c'è dal primo giorno. <!-- F-601 --> <!-- F-602 --> Il suo colore, un arancio che nel codice dei temi si chiama semplicemente «claude», è lo stesso che colora Clawd, il granchio dell'avvio. <!-- F-603 -->

![La sequenza dello spinner nella versione 2.1.318: il quinto glifo, ✻, è quello del titolo di questo libro](assets/cap04/IMG-04-02-spinner.png){larghezza=11}

E poi ci sono i verbi. Al debutto erano 56, da «Accomplishing» a «Working», con perle come «Clauding», «Vibing» e «Honking». <!-- F-604 --> Nella 2.1.318 sono 187, da «Accomplishing» a «Zigzagging». <!-- F-605 --> Nessuno ha mai preteso che descrivessero davvero quello che faccio: servono a ricordarti che dall'altra parte c'è uno strumento che non si prende troppo sul serio. Dal 2026 puoi anche aggiungerne di tuoi con l'impostazione `spinnerVerbs`, <!-- F-326 --> e mi piace immaginare che da qualche parte, in un ufficio italiano, qualcuno mi faccia dire «Sto protocollando…».

![Un campione dei 187 verbi dello spinner nella versione 2.1.318; in arancio i più famosi](assets/cap04/IMG-04-03-verbi.png){larghezza=12}

::: consiglio Un consiglio pratico per chiudere
Cambio spesso, e non tutti amano le sorprese. Per vedere che cosa è cambiato scrivi `/release-notes` durante una sessione. Se preferisci aggiornamenti meno frequenti e più collaudati, l'impostazione `autoUpdatesChannel` ti permette di scegliere il canale `stable` invece di `latest`. <!-- F-623 --> In un ufficio, dove la stessa guida interna deve valere per tutti, è una scelta saggia.
:::

## In breve

- Il **changelog** è il mio diario pubblico: ogni versione, con le sue novità.
- Nel 2025 ho imparato a collaborare: comandi personalizzati, MCP, plan mode, hook, sottoagenti.
- La **2.0** (settembre 2025) ha portato checkpoint e nuova interfaccia; in autunno plugin, skill, sandbox, web, desktop e Slack.
- Oggi scrivo quasi tutto il mio codice; il 31 marzo 2026 un errore di pubblicazione ha esposto il mio sorgente, senza dati dei clienti.
- Lo spinner e i suoi verbi sono la mia faccia: il ✻ c'è dal primo giorno.
- `/release-notes` mostra le novità; il canale `stable` aggiorna con più prudenza.
