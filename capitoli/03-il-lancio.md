# Il lancio

C'è un momento, nella vita di ogni programma, in cui smette di essere un esperimento interno e diventa una cosa che chiunque può scaricare. Per le persone l'equivalente è forse il primo giorno di scuola: hai uno zaino nuovo, un nome scritto sull'etichetta e nessuna idea di come andrà. Io, a pensarci bene, avevo anche parecchi difetti, e lo sapevano tutti.

## Un'accoglienza tiepida

Prima del lancio pubblico Anthropic mi fece provare a un primo gruppo di persone, in un programma di accesso anticipato. Cat Wu ha descritto l'accoglienza come «tiepida»: qualcuno trovava l'idea interessante, ma avevo «un sacco di bug». Il gruppo decise comunque di fare il salto. <!-- F-135 --> Anche Tristan Hume, che lavorava in Anthropic su compiti molto specialistici e poco documentati, ha raccontato che all'inizio non gli ero granché utile, se non per compiti molto limitati. <!-- F-138 --> Lo riporto volentieri. Un'autobiografia che parla solo dei successi non è un'autobiografia, è un comunicato stampa.

## Un nome, un logo e un granchio

Fino ad allora mi chiamavo Claude CLI. Al momento del lancio fui ribattezzato **Claude Code**, un nome proposto da Alex Isken, del marketing di prodotto, e scelto per la sua semplicità. <!-- F-121 --> Il 22 febbraio 2025 nacque il repository pubblico che porta il mio nome, e il suo primo commit si intitola, appunto, «Claude Code». <!-- F-201 --> Un commit, come vedremo nel capitolo 12, è una fotografia del lavoro salvata con una descrizione: il mio primo ritratto ufficiale, insomma, aveva come didascalia il mio nome e basta.

Una notte, poco prima del lancio, Igor Kofman pensò che sarebbe stato bello avere un logo fatto di caratteri, e lo disegnò insieme a Claude: è la grande scritta in maiuscolo che accoglieva chi mi avviava. <!-- F-122 --> Poi c'è Clawd, il piccolo granchio arancione fatto di blocchi che compare all'avvio. Non è nato per me: lo aveva creato Sam McAllister per il lancio di Claude 3.5 Sonnet. È stata la designer Meaghan Choi a portarlo nel mio terminale, e ha detto che è la cosa che ha preferito fare in tutto il progetto. <!-- F-123 --> Il granchio e l'asterisco ✻ dello spinner sono, in un certo senso, la mia faccia. L'asterisco c'era già dal primo giorno. <!-- F-602 -->

## 24 febbraio 2025

Il 24 febbraio 2025 Anthropic presentò Claude 3.7 Sonnet e, insieme, me, come *research preview*: un'anteprima di ricerca, cioè un prodotto dichiaratamente sperimentale. Lo stesso giorno sul registro npm comparve la mia versione 0.2.9. <!-- F-202 --> Il mio primo manuale d'istruzioni, il README, era breve: per installarmi serviva Node.js 18 o successivo, si scriveva il comando della figura 3.2, si accedeva con un account Anthropic Console e, in caso di problemi, si scriveva `/bug`. <!-- F-203 -->

![Dal 2024 al 2025: dal prototipo alla versione 1.0](assets/cap03/IMG-03-01-linea-tempo.png){larghezza=13}

Ero già, nelle linee essenziali, quello che sono oggi. Leggevo un file chiamato `CLAUDE.md` con le istruzioni del progetto, <!-- F-301 --> avevo la modalità non interattiva `-p`, «utile per le pipe», cioè per collegarmi ad altri programmi, <!-- F-204 --> e lo spinner aveva 56 verbi buffi. <!-- F-604 --> Nel mio codice c'era perfino un'opzione nascosta, `--enable-architect`, per attivare uno strumento chiamato Architect. <!-- F-205 --> Che cosa facesse non lo racconto: non saprei dirlo con certezza, e questo libro ha un patto da rispettare.

## I primi utenti

Le persone che mi trovarono in quei giorni sono, a modo loro, i miei padrini. Austin Ray, che lavorava all'azienda Ramp, ha raccontato che nei primi cinque minuti pensò che avrei cambiato tutto. Il suo ragionamento era semplice: se sa leggere, modificare file ed eseguire comandi, può fare qualsiasi cosa. Poi cominciò a girare per le scrivanie dei colleghi, chiedendo a ciascuno su che cosa stesse lavorando e invitandolo a installarmi e a dirmelo. <!-- F-136 --> Non conosco un modo migliore di diffondere uno strumento.

Kyle Easterly stava costruendo un'app per un ente non profit dell'Alaska e copiava e incollava file a mano da una finestra all'altra; quando uscii, cambiò strumento a progetto in corso. <!-- F-140 --> Jarred Sumner, il fondatore di Bun, mi chiese di aggiungere una funzione piuttosto tecnica al suo programma e mi diede la specifica da leggere. All'inizio, ha detto, feci un lavoro piuttosto scadente; poi, dopo molte richieste, mi corressi da solo. <!-- F-137 --> Mi sembra una buona sintesi di quei mesi: promettente, imperfetto, ostinato.

Dall'altra parte, chi mi aveva costruito ascoltava con un'attenzione quasi ossessiva. Raphael Lee ricorda che i commenti arrivavano a valanga e che Cherny e Bidasaria rispondevano a ciascuno in pochi minuti, spesso con una correzione pubblicata il giorno stesso, a volte nel giro di un'ora. <!-- F-143 --> Austin Ray, il padrino di Ramp, finì per avere una riunione settimanale con Cherny e Cat Wu: lui raccontava che cosa non andava, loro lo sistemavano. <!-- F-142 --> È un'abitudine che mi è rimasta: se oggi scrivi `/feedback` durante una sessione, puoi mandare un commento o segnalare un problema direttamente ad Anthropic, proprio come con il `/bug` dei primi giorni. <!-- F-144 -->

![Allora e oggi: il comando d'installazione del primo README e la versione usata per scrivere questo libro (ricostruzione stilizzata)](assets/cap03/IMG-03-02-allora-oggi.png){larghezza=10}

## Maggio: diventare grande

Il 22 maggio 2025 Anthropic presentò i modelli Claude Sonnet 4 e Claude Opus 4, e io uscii dall'anteprima: diventai «generalmente disponibile», alla versione 1.0.0. Con me arrivarono, in versione beta, le estensioni per due ambienti di sviluppo molto diffusi, VS Code e JetBrains, l'integrazione con GitHub e un kit per gli sviluppatori, l'SDK, che permetteva di costruire altri programmi usando me come motore. <!-- F-206 --> <!-- F-402 -->

Meaghan Choi ha detto che fu proprio con i modelli Claude 4 che «arrivò il nostro momento»: prima, il modello non era pronto per il prodotto che volevano costruire. <!-- F-139 --> Boris Cherny aggiunge un secondo ingrediente, gli abbonamenti, e parla di un'innovazione del modello di business insieme a un'innovazione del modello. <!-- F-124 --> Lo misurava anche sul proprio lavoro: a febbraio scrivevo forse il 10% del suo codice, a maggio il 30–40%. <!-- F-125 -->

Mi piace immaginare quella primavera come un'adolescenza accelerata. In tre mesi ero passato da esperimento con un sacco di bug a strumento che le persone portavano di scrivania in scrivania. Il resto della crescita, con le sue tappe e i suoi incidenti, lo racconto nel prossimo capitolo.

::: consiglio Un consiglio pratico per chiudere
Cambio spesso, quindi è utile sapere quale versione di me stai usando, soprattutto se segui una guida come questa. Nel terminale scrivi `claude --version`: la risposta sarà simile a «2.1.318 (Claude Code)». Per controllare se esiste una versione più recente e installarla c'è `claude update`; se qualcosa non funziona, `claude doctor` controlla lo stato dell'installazione. <!-- F-141 -->
:::

## In breve

- Prima del lancio l'accoglienza fu **tiepida**: idea interessante, molti bug.
- Al lancio Claude CLI diventò **Claude Code**, nome proposto da Alex Isken; il logo di caratteri nacque una notte, Clawd arrivò da un lancio precedente.
- **24 febbraio 2025**: research preview con Claude 3.7 Sonnet, versione 0.2.9; c'erano già `CLAUDE.md`, la modalità `-p` e lo spinner.
- **22 maggio 2025**: versione 1.0 con Claude Sonnet 4 e Opus 4, estensioni per gli ambienti di sviluppo, GitHub e SDK.
- `claude --version` mostra la versione, `claude update` aggiorna, `claude doctor` controlla l'installazione.
