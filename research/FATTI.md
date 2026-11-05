# Registro dei fatti

Ogni fatto usato nel libro deve comparire qui prima di essere scritto (vedi CLAUDE.md).
Nel sorgente dei capitoli si cita l'id con `<!-- F-NNN -->`.

**Affidabilità**: **A** fonte primaria o autorevole · **M** stampa o fonte secondaria · **B** bassa (non usare come fatto).
**Accesso**: tutte le fonti sono state consultate il **2026-11-04** (sessione S1), salvo diversa indicazione.
**Metodo per le date del software**: `CHANGELOG.md` ufficiale (https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md, ultima versione 2.1.318) incrociato con il campo `time` del registro npm (https://registry.npmjs.org/@anthropic-ai/claude-code). "Pacchetto npm X" = verifica diretta del codice distribuito di quella versione. "Binario 2.1.318" = ispezione dell'eseguibile installato (vedi `note/spinner.md`).
**Citazioni tra virgolette**: vanno ricontrollate sull'originale prima di essere stampate; in italiano si danno in traduzione indicando l'originale inglese in nota.

Numerazione: F-0xx storia dell'informatica · F-1xx origini · F-2xx lancio e tappe · F-3xx funzionalità · F-4xx modelli · F-5xx numeri · F-6xx curiosità · F-7xx uso reale · F-9xx non verificati.

---

## F-0xx — Storia dell'informatica (cap. 1)

| Id | Affermazione | Fonte (URL) | Aff. | Cap. |
|---|---|---|---|---|
| F-001 | Nel 1843 Ada Lovelace tradusse l'articolo di Luigi Menabrea sulla Macchina Analitica di Babbage aggiungendo ampie note proprie, con la prima descrizione pubblicata di una sequenza di operazioni passo per passo; per questo è spesso chiamata "la prima programmatrice" (il contributo esatto è discusso dai biografi) | https://www.computerhistory.org/babbage/adalovelace/ | A | 1 |
| F-002 | Lovelace intuì che la macchina avrebbe potuto andare oltre i numeri, per esempio "comporre brani musicali elaborati e scientifici" | https://www.computerhistory.org/babbage/adalovelace/ | A | 1 |
| F-003 | La Nota G descrive il calcolo dei numeri di Bernoulli; le note furono pubblicate nell'agosto 1843 negli *Scientific Memoirs* di Taylor firmate "A.A.L."; chiamarla "primo programma" è considerato un po' impreciso | https://www.sciencemuseum.org.uk/objects-and-stories/women-computing ; https://www.cs.ox.ac.uk/people/alex.rogers/2020/01/20/bernoulli.html | M | 1 |
| F-004 | Il telaio di Jacquard (prima dimostrazione 1801, controllo a schede sviluppato nel 1804) era comandato da schede perforate legate in sequenza: per il CHM è la prima macchina a usare schede intercambiabili per istruire una macchina. Nel testo: "all'inizio dell'Ottocento" | https://www.computerhistory.org/revolution/story/4 ; https://computerhistory.org/blog/artifact-adopted-preserving-the-legend-of-j-m-jacquard/ | A | 1 |
| F-005 | Babbage conosceva il telaio di Jacquard e negli anni '30 dell'Ottocento progettò il controllo della Macchina Analitica con schede perforate | https://computerhistory.org/blog/artifact-adopted-preserving-the-legend-of-j-m-jacquard/ | A | 1 |
| F-006 | Per il censimento USA del 1890 si noleggiarono le macchine a schede di Herman Hollerith; il conteggio finì "con mesi di anticipo e molto sotto budget" | https://www.census.gov/about/history/bureau-history/census-innovations/technology/tabulation-and-processing.html | A | 1 |
| F-007 | Nelle tabulatrici di Hollerith degli aghi attraversavano i fori chiudendo circuiti che facevano avanzare dei contatori; circa 60 milioni di schede, ~7.000 al giorno per operatore, "almeno dieci volte più veloce" del metodo manuale | https://www.computerhistory.org/revolution/punched-cards/2/2 | A | 1 |
| F-008 | L'ENIAC fu proposto nel 1942, costruito tra il 1943 e il 1945, finì in prima pagina sul *New York Times* il 15 febbraio 1946 e restò in servizio fino al 1955 | https://www.computerhistory.org/revolution/birth-of-the-computer/4/78 | A | 1 |
| F-009 | Le sei programmatrici originali dell'ENIAC: Kathleen McNulty Mauchly Antonelli, Jean Jennings Bartik, Betty Snyder Holberton, Marlyn Wescoff Meltzer, Frances Bilas Spence, Ruth Lichterman Teitelbaum; il loro lavoro fu a lungo considerato "impiegatizio" e ignorato | https://computer.org/volunteering/awards/pioneer/about-women-of-eniac | A | 1 |
| F-010 | Betty Holberton inventò i breakpoint per il debugging; l'IEEE Computer Society ha intitolato il Computer Pioneer Award alle donne dell'ENIAC | https://computer.org/volunteering/awards/pioneer/about-women-of-eniac | A | 1, 11 |
| F-011 | Il 9 settembre 1947 il gruppo dell'Harvard Mark II trovò una falena in un relè e la incollò nel registro: "First actual case of bug being found". Grace Hopper rese famosa la storia; la parola "bug" esisteva già | https://www.computerhistory.org/tdih/september/9/ | A | 1, 11 |
| F-012 | Lo Smithsonian, che conserva il registro, precisa che probabilmente non apparteneva a Hopper | https://www.si.edu/object/log-book-computer-bug:nmah_334663 | A | 1, 11 |
| F-013 | Nel 1952 Grace Hopper completò A-0 per l'UNIVAC I, che permetteva di usare parole simili all'inglese invece di numeri: "spesso considerato il primo compilatore" | https://www.computerhistory.org/timeline/1952/ | A | 1 |
| F-014 | Il comitato che sviluppò il COBOL si formò il 28 maggio 1959 su iniziativa del Dipartimento della Difesa USA; Hopper vi ebbe un ruolo guida (indiretto, tramite il suo staff); nel 1997 esistevano oltre 200 miliardi di righe di COBOL | https://www.computerhistory.org/tdih/may/28/ ; https://www.computerhistory.org/revolution/early-computer-companies/5/117 | A | 1 |
| F-015 | Il FORTRAN fu ideato nel 1954 e commercializzato da IBM nel 1957 sotto la guida di John Backus, che definiva la programmazione a mano "un corpo a corpo con la macchina" | https://www.ibm.com/history/fortran | A | 1 |
| F-016 | Nel FORTRAN per l'IBM 704 ogni istruzione era perforata su una scheda (colonne 7–72); il pacco entrava nel lettore e ne usciva il programma in linguaggio macchina | https://softwarepreservation.computerhistory.org/FORTRAN/ | A | 1 |
| F-017 | La telescrivente Teletype ASR-33, nata per la rete Western Union, fu tra anni '60 e '70 un terminale diffusissimo per i minicomputer (~700 dollari) | https://www.computerhistory.org/revolution/minicomputers/11/337/1934 | A | 1 |
| F-018 | Il terminale video DEC VT100 (1978), con CPU Intel 8080, introdusse funzioni come grassetto e più set di caratteri, poi copiate dai concorrenti | https://www.computerhistory.org/revolution/input-output/14/349/1697 | A | 1 |
| F-019 | Nell'estate 1969 Ken Thompson e Dennis Ritchie (Bell Labs) iniziarono Unix su un PDP-7; tra i primi programmi c'è "sh", l'interprete dei comandi | https://computerhistory.org/blog/the-earliest-unix-code-an-anniversary-source-code-release/ | A | 1 |
| F-020 | Unix passò sul PDP-11 nel 1970–71; il nome fu proposto da Brian Kernighan nel 1970 | https://spectrum.ieee.org/the-strange-birth-and-long-life-of-unix | M | 1 |
| F-021 | La Bourne shell (Stephen Bourne) uscì nel 1979 con Unix Version 7 | https://en.wikipedia.org/wiki/Bourne_shell | M | 1 |
| F-022 | Lo Xerox Alto (1973) ebbe schermo bitmap, mouse, finestre e icone, e ispirò Lisa e Macintosh | https://www.computerhistory.org/revolution/input-output/14/347 | A | 1 |
| F-023 | Il Macintosh fu presentato il 24 gennaio 1984, due giorni dopo lo spot "1984" al Super Bowl | https://computerhistory.org/blog/a-computer-for-the-rest-of-us/ | A | 1 |
| F-024 | IntelliSense (completamento automatico Microsoft) comparve a metà anni '90 (fonti in conflitto tra 1996 e 1997: non dare l'anno) | https://learn.microsoft.com/en-us/shows/visualstudiodocumentary/visual-studio-documentary-part-one | M | 1 |
| F-025 | Il 29 giugno 2021 GitHub annunciò Copilot in anteprima tecnica come "AI pair programmer" basato su OpenAI Codex | https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/ | A | 1 |
| F-026 | Nell'ottobre 1950 Turing pubblicò su *Mind* "Computing Machinery and Intelligence", proponendo il "gioco dell'imitazione" | https://academic.oup.com/mind/article/LIX/236/433/986238 | A | 1 |
| F-027 | Joseph Weizenbaum descrisse ELIZA su *Communications of the ACM* nel gennaio 1966; lo script DOCTOR imitava uno psicoterapeuta rimandando le frasi all'utente | https://dl.acm.org/doi/10.1145/365153.365168 | A | 1 |
| F-028 | Il 12 giugno 2017 Vaswani e coautori pubblicarono "Attention Is All You Need", che introduce l'architettura Transformer | https://arxiv.org/abs/1706.03762 | A | 1 |
| F-029 | Il 30 novembre 2022 OpenAI lanciò ChatGPT come anteprima di ricerca gratuita | https://openai.com/index/chatgpt/ | A | 1 |
| F-030 | Anthropic fu fondata nel 2021 da ex ricercatori di OpenAI, tra cui Dario e Daniela Amodei; è una public benefit corporation | https://www.anthropic.com/company/leadership ; https://www.britannica.com/money/Anthropic-PBC | A | 1 |
| F-031 | Il 14 marzo 2023 Anthropic presentò Claude (e Claude Instant), già provato con partner come Notion, Quora e DuckDuckGo | https://www.anthropic.com/news/introducing-claude | A | 1 |
| F-032 | Shannon pubblicò "A Mathematical Theory of Communication" nel *Bell System Technical Journal* (luglio e ottobre 1948), rendendo il bit l'unità dell'informazione (la parola "bit" è attribuita a John W. Tukey) | https://www.nokia.com/bell-labs/about/history/innovation-stories/information-theory-turns-75/ | A | 1 |
| F-033 | Il 25 novembre 2024 Anthropic rese open source il Model Context Protocol (MCP) | https://www.anthropic.com/news/model-context-protocol | A | 2, 23 |

## F-1xx — Origini (cap. 2)

| Id | Affermazione | Fonte (URL) | Aff. | Cap. |
|---|---|---|---|---|
| F-101 | Settembre 2024: Boris Cherny entra in Anthropic e sperimenta prototipi; il primo non accede a file né terminale e usa AppleScript per dire e cambiare la musica che sta ascoltando | https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built | A | 2 |
| F-102 | Dopo un confronto con Cat Wu il prototipo ottiene strumenti per leggere e scrivere file ed eseguire comandi, e il modello comincia a esplorare il codice da solo ("product overhang") | idem | A | 2 |
| F-103 | Novembre 2024: rilascio interno; ~20% degli ingegneri lo usa il primo giorno, ~50% entro il quinto | idem | A | 2 |
| F-104 | Tecnologia: TypeScript, React + Ink, Yoga, Bun; distribuzione via npm. Sid Bidasaria nel gruppo da novembre 2024; ~10 ingegneri a luglio 2025 | idem | A | 2, 4 |
| F-105 | Cherny (Latent Space, 7/5/2025): "Claude Code is not a product as much as it's a Unix utility" e "There was no master plan" | https://www.latent.space/p/claude-code | A | 2 |
| F-106 | Anthropic pubblica "The Making of Claude Code" (data indicata dalla ricerca 23/02/2026, incompatibile con F-129: non usarla) (leggibile anche "in terminale"): fonte primaria da leggere a mano prima di scrivere il cap. 2 | https://www.anthropic.com/features/making-of-claude-code | A (esistenza) | 2 |

### Da "The Making of Claude Code" (interviste, Anthropic 2026)

| Id | Affermazione | Fonte (URL) | Aff. | Cap. |
|---|---|---|---|---|
| F-107 | Il primo prodotto di Anthropic fu un assistente di programmazione: un'estensione di VS Code che proponeva quattro suggerimenti per ogni richiesta; nella primavera 2022 aveva circa 100 utenti esterni (Ben Mann) | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-108 | Dall'inizio del 2022 il gruppo di Reinforcement Learning (Shauna Kravec) lavorava a modelli capaci di ingegneria del software autonoma; all'inizio "i modelli erano davvero pessimi" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-109 | Nel 2022 Dawn Drain e un collega fecero funzionare una shell persistente dentro un container, perché il modello potesse eseguire codice | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-110 | Prima di Claude Code esisteva **clide**, uno strumento interno a riga di comando per chattare con Claude e modificare codice; il nome era stato coniato da Eli Tran-Johnson. Era lento ad avviarsi e "traballante"; aveva una funzione che lanciava cento Claude Haiku in parallelo | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-111 | Adam Wolff aggiunse a clide un "agente" capace di intuire l'intenzione da una modifica parziale ("baby agentic"): la prima volta che funzionò "ballavo per la cucina" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-112 | Ben Mann fondò il gruppo Labs nel gennaio 2024; quando Boris Cherny arrivò a settembre voleva fare un linter, e Mann gli disse di "fare la cosa grande" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-113 | Il primo prototipo di Cherny si chiamava **Claude CLI**: per sapere che musica stesse ascoltando fece uno screenshot di Apple Music e lo lesse. Circa due giorni di lavoro; postato su Slack, "due o tre like" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-114 | Il giorno dopo Cherny vide il collega Robert Boyce lavorare con le righe rosse e verdi delle modifiche: "sta facendo il mio codice" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-115 | Il primo responsabile del gruppo fu Adam Wolff, ex studente di cinema e game designer, che aveva lavorato a React; accettò dopo varie insistenze e "qualche birra" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-116 | Cat Wu entrò in Anthropic nell'estate 2024, usò Claude CLI per costruire ambienti di RL, mandava a Cherny "paragrafi di feedback" e fu invitata a unirsi al progetto | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-117 | Sid Bidasaria entrò nel gruppo Labs nell'agosto 2024 ("ingegnere numero due" di Claude Code); fino a dicembre 2024 ci lavoravano solo lui, Cherny e un po' Ben Mann; poi uno sprint finale di due settimane con 6–7 persone (segnalazione bug, login) | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2, 3 |
| F-118 | Gran parte del gruppo Labs confluì in Claude Code; un'altra parte diventò il team di MCP (Raphael Lee) | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2 |
| F-119 | Fin dall'inizio Claude Code ebbe aggiornamenti automatici: una correzione arrivava agli utenti "cinque minuti dopo" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2, 4 |
| F-120 | Ben Mann: bisogna costruire qualcosa che funzioni il 20–30% delle volte oggi, perché col modello successivo funzionerà l'80% | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 2, 26 |
| F-121 | **Origine del nome**: al lancio di febbraio 2025 Claude CLI fu rinominato **Claude Code**; il nome fu proposto da Alex Isken (Product Marketing), scelto per la sua semplicità (Cat Wu). Prima del lancio l'accoglienza nell'accesso anticipato era stata "tiepida" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 3 |
| F-122 | Il logo ASCII in maiuscolo di Claude Code nacque una notte prima del lancio da un'idea di Igor Kofman, realizzato insieme a Claude | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 3 |
| F-123 | **Clawd** fu creato da Sam McAllister per il lancio di Claude 3.5 Sonnet; Meaghan Choi (designer) lo aggiunse al terminale di Claude Code | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 3, 4 |
| F-124 | Il vero decollo arrivò con i modelli Claude 4 e con gli abbonamenti: "un'innovazione del modello di business insieme a un'innovazione del modello" (Cherny) | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 3 |
| F-125 | Cherny: a febbraio 2025 Claude Code scriveva forse il 10% del suo codice, a maggio il 30–40%, dall'inverno 2025 il 100%, "nemmeno una riga a mano" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 4, 25 |
| F-126 | Cat Wu: al lancio tutti leggevano ogni richiesta di permesso; oggi molti utenti accettano tutto automaticamente, segno che Claude "si è guadagnato la fiducia" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 9 |
| F-127 | Kyle Easterly: per lo Statewide Independent Living Council of Alaska (ente non profit) ha costruito software prima inaccessibile; oggi trascrive registri cartacei di consegne di carburante in CSV | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | Parte IV, 26 |
| F-128 | Cherny confronta Claude Code con la perforatrice IBM 029, simile a quella con cui programmava suo nonno nell'Unione Sovietica: "da qualche parte su questo spettro c'è Claude Code" | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | 1, 26 |
| F-129 | Le interviste sono state registrate tra febbraio e maggio 2026, quindi la pagina è stata pubblicata dopo: la data 23/02/2026 di F-106 è **errata o da ricontrollare** (non usarla) | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`) | A | — |
| F-130 | Cherny sul prototipo Claude CLI: «circa due giorni di lavoro; rifarlo oggi con Claude Code richiederebbe due minuti» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2 |
| F-131 | (AMBIGUO, non usare: «the app» potrebbe essere l'app desktop) Robert Boyce: l'app di allora era «poco più che definizioni di strumenti in un ciclo e una semplice interfaccia a riga di comando (REPL)» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2 |
| F-132 | Cherny: il prototipo era «molto lontano dall'essere buono», ma sentiva un'urgenza tale da lavorarci ogni fine settimana | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2 |
| F-133 | Cherny, a posteriori: tenere piccolo il gruppo fu importante per il successo, evitò di complicare troppo e «ci costrinse a usare Claude di più» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2 |
| F-134 | Le due fonti divergono su come il primo prototipo scoprisse la musica: AppleScript (Pragmatic Engineer, F-101) oppure uno screenshot di Apple Music (Making-of, F-113). Nel testo si riportano entrambe | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2 |
| F-135 | Cat Wu: nel programma di accesso anticipato prima del lancio l'accoglienza fu «tiepida»: «un'idea interessante, ma con un sacco di bug»; poi «facemmo il salto» del lancio esterno a febbraio 2025 | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-136 | Austin Ray (Ramp): trovò Claude Code dopo il lancio come research preview; «nei primi cinque minuti» pensò che avrebbe cambiato tutto; «se sa leggere, modificare ed eseguire bash, può fare qualsiasi cosa»; andava alle scrivanie dei colleghi a farlo installare | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-137 | Jarred Sumner (fondatore di Bun) chiese a Claude Code di implementare la compressione dei websocket in Bun dandogli la specifica: all'inizio «fece un lavoro piuttosto scadente», poi dopo molte richieste si corresse; Sumner cambiò le priorità di Bun per renderlo più facile da usare con Claude Code | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-138 | Tristan Hume (Anthropic): all'inizio, per compiti che richiedevano molto contesto non documentato, Claude Code «non era molto utile, se non per compiti molto limitati» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-139 | Meaghan Choi: «quando sono usciti i modelli Claude 4, è arrivato il nostro momento»; prima «il modello non era pronto per il prodotto che volevamo costruire» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-140 | Kyle Easterly lavorava a un'app per un ente non profit dell'Alaska copiando file a mano tra gli strumenti; quando uscì Claude Code passò a usarlo a progetto in corso | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-141 | `claude --version` (o `-v`) stampa la versione («2.1.318 (Claude Code)»); `claude update` controlla e installa gli aggiornamenti; `claude doctor` controlla lo stato dell'installazione | `claude --help` sul binario 2.1.318, accesso 2026-11-05 | A | 3, 5 |
| F-142 | Austin Ray: con Boris Cherny e Cat Wu aveva riunioni settimanali di feedback, «un rapporto da sviluppatore a utente» | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 3 |
| F-143 | Raphael Lee: i commenti arrivavano a valanga; Cherny e Bidasaria rispondevano a ciascuno in pochi minuti e spesso pubblicavano una correzione in giornata, o nell'ora | https://www.anthropic.com/features/making-of-claude-code (testo in `research/fonti/the-making-of-claude-code.txt`, accesso 2026-11-05) | A | 2, 3 |
| F-144 | Il comando `/feedback` («Send feedback to Anthropic or report a bug») invia un commento o segnala un bug; erede del `/bug` del primo README (F-203) | binario 2.1.318 (stringhe), accesso 2026-11-05 | A | 3 |

## F-2xx — Lancio e tappe del prodotto (cap. 3, 4, 25)

| Id | Affermazione | Fonte (URL) | Aff. | Cap. |
|---|---|---|---|---|
| F-201 | Il repository github.com/anthropics/claude-code nasce il 22/02/2025; il primo commit si intitola "Claude Code" | https://api.github.com/repos/anthropics/claude-code | A | 3 |
| F-202 | 24/02/2025: research preview insieme a Claude 3.7 Sonnet; pacchetto npm v0.2.9 pubblicato lo stesso giorno | https://www.anthropic.com/news/claude-3-7-sonnet ; registro npm | A | 3 |
| F-203 | Il primo README ("Claude Code (Research Preview)"): installazione con `npm install -g @anthropic-ai/claude-code`, Node 18+, accesso OAuth con account Anthropic Console, segnalazioni con `/bug` | https://github.com/anthropics/claude-code/blob/bd5ca708adf82c4b81857abf40fe36d9d9cc3d1c/README.md | A | 3, 5 |
| F-204 | La 0.2.9 aveva già la modalità non interattiva `-p/--print` ("utile per le pipe") | pacchetto npm 0.2.9 | A | 3, 24 |
| F-205 | La 0.2.9 conteneva un'opzione nascosta `--enable-architect` ("Enable the Architect tool") | pacchetto npm 0.2.9 | A | 3 |
| F-206 | 22/05/2025: Claude Code "generally available" (v1.0.0) con Claude Sonnet 4 e Opus 4; estensioni beta per VS Code e JetBrains; Claude Code su GitHub in beta (GitHub Actions); Claude Code SDK | https://www.anthropic.com/news/claude-4 | A | 3 |
| F-207 | 11/07/2025 (v1.0.51): supporto Windows nativo, senza WSL (allora richiedeva Git for Windows; oggi è facoltativo e si usa lo strumento PowerShell) | CHANGELOG 1.0.51 ; https://code.claude.com/docs/en/setup | A | 5 |
| F-208 | 29/09/2025: Claude Code 2.0 — estensione nativa VS Code (beta), nuova interfaccia del terminale, checkpoint; il Claude Code SDK diventa **Claude Agent SDK** | https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously | A | 3, 4, 24 |
| F-209 | 20/10/2025: Claude Code sul web in research preview (Pro e Max, anche su iOS) | https://claude.com/blog/claude-code-on-the-web | A | 4, 25 |
| F-210 | 23/09/2026: Claude Code sul web diventa disponibile a tutti con il nome "cloud sessions" (Pro, Max, Ultra, Team, Enterprise) | https://claude.com/blog/claude-code-on-the-web | A | 25 |
| F-211 | 24/11/2025 (v2.0.51): "Introducing Claude Code for Desktop"; lo stesso giorno l'annuncio di Opus 4.5 dice che Claude Code è disponibile nell'app desktop con più sessioni in parallelo | CHANGELOG 2.0.51 ; https://www.anthropic.com/news/claude-opus-4-5 | A | 4, 25 |
| F-212 | Oggi Claude Code è una scheda dell'app Claude accanto a Chat e Cowork; `claude --desktop` dalla 2.1.285 (29/09/2026) | https://code.claude.com/docs/en/desktop | A | 25 |
| F-213 | 08/12/2025: Claude Code in Slack in beta (research preview) per Team ed Enterprise; mai uscito dalla beta, sostituito da Claude Tag (23/06/2026); il bot precedente è stato ritirato il 05/10/2026 secondo la documentazione | https://claude.com/blog/claude-code-and-slack ; https://code.claude.com/docs/en/slack | A | 4, 25 |
| F-214 | Cat Wu ("head of product for Claude Code and Cowork"): "We see Claude Tag as an evolution of Claude Code" | https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack | M | 25 |
| F-215 | Il plugin JetBrains è ancora indicato come beta a novembre 2026 | https://code.claude.com/docs/en/jetbrains | A | 5, 25 |
| F-216 | 03/12/2025: Anthropic acquisisce Bun, il runtime JavaScript su cui gira Claude Code | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | A | 4 |
| F-217 | 07/01/2026: versione 2.1.0 | registro npm | A | 4 |
| F-218 | 31/03/2026: il codice sorgente finisce per errore nel pacchetto npm 2.1.88 (source map); Anthropic conferma: errore umano | https://bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package | A | 4 |
| F-220 | La versione 2.1.88 fu pubblicata su npm per poco tempo e conteneva un file `cli.js.map` di circa 60 MB con il codice sorgente; dal file si ricostruirono circa 1.900 file e 500.000 righe | https://bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package (31/03/2026, accesso 2026-11-05) | A | 4 |
| F-221 | Dichiarazione di Anthropic: «una release di Claude Code includeva del codice sorgente interno. Nessun dato sensibile dei clienti né credenziali sono stati coinvolti o esposti. È stato un problema di confezionamento della release causato da errore umano, non una violazione della sicurezza»; annunciate misure per evitare che si ripeta | https://bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package (31/03/2026, accesso 2026-11-05) | A | 4 |
| F-222 | Anthropic inviò richieste di rimozione (DMCA) per le copie pubblicate online | https://bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package (31/03/2026, accesso 2026-11-05) | A | 4 |
| F-219 | 14/04/2026: Routines in research preview — attività eseguite sull'infrastruttura web, avviate a orario, via API o da webhook GitHub; limiti giornalieri Pro 5, Max 15, Team/Enterprise 25; si creano su claude.ai/code o con `/schedule` | https://claude.com/blog/introducing-routines-in-claude-code | A | 18, 24, 25 |

## F-3xx — Funzionalità (cap. 4–9, 20–24)

| Id | Affermazione | Fonte | Aff. | Cap. |
|---|---|---|---|---|
| F-301 | CLAUDE.md esisteva già nella prima versione pubblica (0.2.9) | pacchetto npm 0.2.9 | A | 4, 8 |
| F-302 | Slash command personalizzati (`.claude/commands/`): 0.2.31, 05/03/2025 | CHANGELOG + npm | A | 4, 20 |
| F-303 | Supporto MCP presente almeno dalla 0.2.31 (05/03/2025, flag `--mcp-debug`) | CHANGELOG | M | 4, 23 |
| F-304 | Memoria rapida con `#`: 0.2.54, 25/03/2025 | CHANGELOG + npm | A | 8 |
| F-305 | Output in streaming `--output-format=stream-json`: 0.2.66, 09/04/2025 | CHANGELOG | A | 24 |
| F-306 | Import nei CLAUDE.md: 0.2.107, 09/05/2025 | CHANGELOG + npm | A | 8 |
| F-307 | Plan mode: compare nel codice della 1.0.7 (30/05/2025), senza annuncio; prima menzione nel changelog in 1.0.33 (23/06/2025) | pacchetti npm 1.0.6/1.0.7 ; CHANGELOG | A | 4, 7 |
| F-308 | Plan mode in seguito: "Opus Plan Mode" (1.0.77, 12/08/2025); con Opus 4.5 il piano diventa un file modificabile (24/11/2025); comando `/plan` (2.1.0, 07/01/2026) | CHANGELOG ; https://www.anthropic.com/news/claude-opus-4-5 | A | 7 |
| F-309 | SDK TypeScript e SDK Python (`claude-code-sdk`): 1.0.23, 13/06/2025 | CHANGELOG | A | 24 |
| F-310 | Comando `claude install` (installazione nativa): compare in 1.0.31, 20/06/2025 | pacchetto npm 1.0.31 | A | 5 |
| F-311 | Hook: 1.0.38, 30/06/2025 ("Released hooks") | CHANGELOG + npm | A | 4, 21 |
| F-312 | Sottoagenti personalizzati (`/agents`): 1.0.60, 24/07/2025 | CHANGELOG + npm | A | 4, 22 |
| F-313 | Comandi bash in background: 1.0.71, 07/08/2025 | CHANGELOG + npm | A | 4 |
| F-314 | Output style: 1.0.81, 14/08/2025 | CHANGELOG + npm | A | 4 |
| F-315 | claude-code-action (GitHub Actions): repository del 19/05/2025; v1 disponibile a tutti dal 26/08/2025 | https://github.com/anthropics/claude-code-action/releases | A | 12, 24 |
| F-316 | Checkpoint e `/rewind`: 2.0.0, 29/09/2025 | CHANGELOG ; F-208 | A | 4, 6 |
| F-317 | Plugin e marketplace: 2.0.12, 09/10/2025 | https://claude.com/blog/claude-code-plugins | A | 4, 24 |
| F-318 | Agent Skills: 2.0.20, 16/10/2025; si installano da plugin (marketplace anthropics/skills) o in `~/.claude/skills` | https://claude.com/blog/skills | A | 4, 20 |
| F-319 | Agent Skills diventa standard aperto (agentskills.io) il 18/12/2025 | https://claude.com/blog/skills | A | 20 |
| F-320 | 22/10/2026: Anthropic dona Agent Skills alla Agentic AI Foundation (Linux Foundation), che ospita anche MCP; adottato da oltre 70 piattaforme, ~1 milione di skill pubblicate; le skill sono nate "mentre costruivamo Claude Code" | https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation | A | 20, 25 |
| F-321 | Sandbox per il BashTool (Linux e macOS): 2.0.24, 20/10/2025; riduce dell'84% le richieste di permesso. Su Windows nativo non è supportata | https://anthropic.com/engineering/claude-code-sandboxing ; docs setup | A | 9 |
| F-322 | 2.0.25 (21/10/2025): il vecchio SDK è rimosso, si passa a `@anthropic-ai/claude-agent-sdk` | CHANGELOG | A | 24 |
| F-323 | Teleport di una sessione dal web al terminale (2.0.24, 20/10/2025); prefisso `&` per mandare un compito al web (2.0.45, 18/11/2025) | CHANGELOG | A | 25 |
| F-324 | Installazione via WinGet (`winget install Anthropic.ClaudeCode`): 2.1.2, 08/01/2026; binario nativo Windows ARM64: 2.1.41, 13/02/2026 | CHANGELOG | A | 5 |
| F-325 | 2.1.15 (21/01/2026): avviso di deprecazione per le installazioni via npm | CHANGELOG | A | 5 |
| F-326 | Impostazione `spinnerVerbs` (aggiungere o sostituire i verbi): 2.1.23 | https://github.com/anthropics/claude-code/issues/21599 ; CHANGELOG | A | 4, 6 |
| F-327 | Agent Teams in research preview con Opus 4.6 (05/02/2026, 2.1.32), attivabili con `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | https://www.anthropic.com/news/claude-opus-4-6 ; CHANGELOG 2.1.32 | A | 22 |
| F-328 | `/loop` (richiesta ripetuta a intervalli): 2.1.71, 06/03/2026 | CHANGELOG | A | 18 |
| F-329 | Dalla 2.1.113 (17/04/2026) anche il pacchetto npm avvia il binario nativo (oggi richiede Node 22+) | CHANGELOG ; docs setup | A | 5 |
| F-330 | Oggi il metodo raccomandato è l'installazione nativa: `curl -fsSL https://claude.ai/install.sh \| bash` (macOS, Linux, WSL), `irm https://claude.ai/install.ps1 \| iex` (PowerShell); si aggiorna da sola; npm resta un'opzione avanzata | https://code.claude.com/docs/en/setup | A | 5 |
| F-331 | Opus 4.7 (16/04/2026) introduce in Claude Code l'effort predefinito `xhigh` e `/ultrareview`, ed estende l'auto mode agli utenti Max | https://www.anthropic.com/news/claude-opus-4-7 | A | 25 |
| F-332 | Opus 4.8 (28/05/2026) porta i "dynamic workflows" in research preview: centinaia di sottoagenti in parallelo in una sessione | https://www.anthropic.com/news/claude-opus-4-8 | A | 22, 25 |
| F-340 | Requisiti: macOS 13.0+, Windows 10 1809+ o Windows Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; 4 GB di RAM, processore x64 o ARM64; connessione a internet; shell Bash, Zsh, PowerShell o CMD; paesi supportati da Anthropic. Non servono privilegi di amministratore | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-341 | Su Windows nativo Git for Windows è facoltativo (consigliato per lo strumento Bash; senza, si usa PowerShell); WSL 2 supporta la sandbox, WSL 1 no; Windows a 32 bit non è supportato | https://code.claude.com/docs/en/setup (accesso 2026-11-05) ; https://code.claude.com/docs/en/troubleshoot-install (accesso 2026-11-05) | A | 5 |
| F-342 | Comandi d'installazione nativa: `curl -fsSL https://claude.ai/install.sh \| bash` (macOS, Linux, WSL); `irm https://claude.ai/install.ps1 \| iex` (PowerShell); `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` (CMD); alternative: `brew install --cask claude-code`, `winget install Anthropic.ClaudeCode`, apt/dnf/apk | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-343 | npm è tra le «opzioni avanzate»: `npm install -g @anthropic-ai/claude-code`, richiede Node.js 22+; non usare `sudo npm install -g` | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-344 | Account: serve un abbonamento Pro, Max, Ultra, Team o Enterprise oppure un account Console (API a credito prepagato); il piano gratuito di claude.ai non include Claude Code. In alternativa Amazon Bedrock, Google Cloud, Microsoft Foundry | https://code.claude.com/docs/en/setup (accesso 2026-11-05) ; https://code.claude.com/docs/en/quickstart (accesso 2026-11-05) | A | 5 |
| F-345 | Primo accesso: si avvia `claude` e si seguono le istruzioni nel browser; `/login` per cambiare account; con un account Console viene creato un workspace «Claude Code» per tenere traccia dei costi | https://code.claude.com/docs/en/setup (accesso 2026-11-05) ; https://code.claude.com/docs/en/quickstart (accesso 2026-11-05) | A | 5 |
| F-346 | `claude --version` stampa un numero seguito da «(Claude Code)»; `claude doctor` mostra una diagnosi in sola lettura dell'installazione e delle impostazioni, con suggerimenti | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-347 | Le installazioni native si aggiornano da sole in background (all'avvio e periodicamente; l'aggiornamento vale dal riavvio successivo); Homebrew, WinGet e i gestori di pacchetti Linux vanno aggiornati a mano (`winget upgrade Anthropic.ClaudeCode`, `brew upgrade claude-code`); il canale `stable` è in genere indietro di circa una settimana e salta le versioni con regressioni gravi; si sceglie anche da `/config` | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-348 | Errore «'claude' is not recognized» / «command not found»: problema di PATH; una finestra di terminale già aperta conserva il vecchio PATH; correzione documentata per PowerShell e per zsh/bash | https://code.claude.com/docs/en/troubleshoot-install (accesso 2026-11-05) | A | 5 |
| F-349 | Errori Windows tipici: «'irm' is not recognized» o «The token '&&' is not a valid statement separator» indicano il comando per la shell sbagliata (CMD vs PowerShell); un 403 o una risposta HTML dello script: riprovare dopo qualche minuto o usare un altro metodo; «App unavailable in region»: paese non supportato | https://code.claude.com/docs/en/troubleshoot-install (accesso 2026-11-05) | A | 5 |
| F-350 | Disinstallazione nativa su Windows: rimuovere `%USERPROFILE%\.localin\claude.exe` e `%USERPROFILE%\.local\share\claude`; su macOS/Linux `~/.local/bin/claude` e `~/.local/share/claude`; `winget uninstall Anthropic.ClaudeCode`; le impostazioni stanno in `~/.claude` e `~/.claude.json` | https://code.claude.com/docs/en/setup (accesso 2026-11-05) | A | 5 |
| F-351 | Claude Code esiste anche come app desktop (macOS, Windows, Linux), sul web (claude.ai/code), in VS Code e JetBrains, in Slack e in CI/CD con GitHub Actions e GitLab; l'estensione VS Code include una propria copia della CLI e non la aggiunge al PATH | https://code.claude.com/docs/en/quickstart (accesso 2026-11-05) ; https://code.claude.com/docs/en/troubleshoot-install (accesso 2026-11-05) | A | 5 |

## F-4xx — Modelli (cap. 3, 25)

| Id | Modello e data | Fonte | Aff. |
|---|---|---|---|
| F-401 | Claude 3.7 Sonnet — 24/02/2025 | https://www.anthropic.com/news/claude-3-7-sonnet | A |
| F-402 | Claude Sonnet 4 e Opus 4 — 22/05/2025 | https://www.anthropic.com/news/claude-4 | A |
| F-403 | Opus 4.1 — 05/08/2025 | https://www.anthropic.com/news/claude-opus-4-1 | A |
| F-404 | Sonnet 4.5 — 29/09/2025 | https://www.anthropic.com/news/claude-sonnet-4-5 | A |
| F-405 | Haiku 4.5 — 15/10/2025 | https://www.anthropic.com/news/claude-haiku-4-5 | A |
| F-406 | Opus 4.5 — 24/11/2025 | https://www.anthropic.com/news/claude-opus-4-5 | A |
| F-407 | Opus 4.6 — 05/02/2026 | https://www.anthropic.com/news/claude-opus-4-6 | A |
| F-408 | Sonnet 4.6 — 17/02/2026 (in Claude Code preferito a Sonnet 4.5 ~70% delle volte) | https://www.anthropic.com/news/claude-sonnet-4-6 | A |
| F-409 | Opus 4.7 — 16/04/2026 | https://www.anthropic.com/news/claude-opus-4-7 | A |
| F-410 | Opus 4.8 — 28/05/2026 | https://www.anthropic.com/news/claude-opus-4-8 | A |
| F-411 | Claude Fable 5 e Claude Mythos 5 — 09/06/2026 | https://www.anthropic.com/news/claude-fable-5-mythos-5 | A |
| F-412 | Sonnet 5 — 30/06/2026; diventa il modello predefinito in Claude Code (2.1.197) | https://www.anthropic.com/news/claude-sonnet-5 | A |
| F-413 | Opus 5 — 24/07/2026 | https://www.anthropic.com/news/claude-opus-5 | A |
| F-414 | Fable 5.1 e Mythos 5.1 — settembre 2026 (in Claude Code dalla 2.1.257, 01/09/2026) | https://www.anthropic.com/claude-fable-and-mythos-5-1 | A |
| F-415 | Opus 5.5 — 22/09/2026 | https://www.anthropic.com/claude-opus-5-5 | A |
| F-416 | Sonnet 5.5 — 28/09/2026 | https://www.anthropic.com/claude-sonnet-5-5 | A |
| F-417 | Haiku 5.5 — 07/10/2026 | https://www.anthropic.com/claude-haiku-5-5 | A |

## F-5xx — Numeri (cap. 4, 25)

| Id | Affermazione | Fonte | Aff. | Cap. |
|---|---|---|---|---|
| F-501 | A metà 2025 oltre l'80% degli ingegneri Anthropic che scrivono codice usa Claude Code ogni giorno | https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built | A | 4 |
| F-502 | Cat Wu (maggio 2025): costo intorno a "6 dollari al giorno per utente attivo"; "molta revisione del codice da parte di persone" | https://www.latent.space/p/claude-code | A | 4 |
| F-503 | Novembre 2025: Claude Code raggiunge 1 miliardo di dollari di fatturato annualizzato, ~6 mesi dopo la disponibilità generale (annuncio del 03/12/2025) | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | A | 4, 25 |
| F-504 | 12/02/2026 (Series G): fatturato annualizzato di Claude Code oltre 2,5 miliardi di dollari, più che raddoppiato da inizio anno; utenti attivi settimanali raddoppiati; abbonamenti business ×4; secondo un'analisi citata, ~4% dei commit pubblici su GitHub scritto da Claude Code | https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation | A | 25 |
| F-505 | Agent Skills: ~280 milioni di installazioni (ottobre 2026) | https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation | A | 20, 25 |

## F-6xx — Curiosità (cap. 3, 4, 6, 25)

| Id | Affermazione | Fonte | Aff. | Cap. |
|---|---|---|---|---|
| F-601 | Lo spinner (2.1.318) alterna `· ✢ * ✶ ✻ ✽` avanti e indietro; nel terminale Ghostty `· ✢ ✳ ✶ ✻ ✻` | binario 2.1.318 (`note/spinner.md`) | A | 4, 6 |
| F-602 | Al lancio (0.2.9) le sequenze erano `· ✢ ✳ ∗ ✻ ✽` (macOS) e `· ✢ * ∗ ✻ ✽` (altri sistemi): il quarto glifo era ∗ (U+2217), oggi ✶. **Il ✻ c'è dal primo giorno** | pacchetto npm 0.2.9 | A | 3, 4 |
| F-603 | Il colore "Claude" del tema è rgb(215,119,87) = #D77757; la stessa tinta colora la mascotte (chiave `clawd_body`) | binario 2.1.318 | A | 4, 6 |
| F-604 | Al lancio i verbi buffi dello spinner erano 56 (da "Accomplishing" a "Working", con "Clauding", "Vibing", "Honking", "Schlepping", "Reticulating"); "Flibbertigibbeting" è arrivato dopo | pacchetto npm 0.2.9 | A | 3, 4 |
| F-605 | Nella 2.1.318 i verbi predefiniti sono 187, da "Accomplishing" a "Zigzagging" | binario 2.1.318 | A | 4, 6 |
| F-606 | All'avvio compare una mascotte a forma di granchio in caratteri a blocchi, **Clawd** (nome ufficiale: vedi F-123; compare anche nelle chiavi del tema `clawd_body`) | F-123 ; binario 2.1.318 | A | 4, 6 |
| F-607 | Cherny (Latent Space, 7/5/2025): Claude scrive circa "l'80, 90%" del codice di Claude Code | https://www.latent.space/p/claude-code | A | 4 |
| F-608 | Cherny su X, 27/12/2025: negli ultimi 30 giorni 259 PR, 497 commit, 40.000 righe aggiunte e 38.000 tolte, "ogni singola riga scritta da Claude Code + Opus 4.5"; il post si apre ricordando che un anno prima Claude faticava a generare comandi bash senza errori di escape | https://twitter.com/bcherny/status/2004887829252317325 (via https://simonwillison.net/2025/Dec/27/boris-cherny/) | A | 4, 25 |
| F-609 | Fortune (29/01/2026): per Anthropic, a livello aziendale, il codice scritto con l'IA è tra il 70 e il 90% | https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/ | M | 25 |
| F-610 | Il nome "Claude" onorerebbe Claude Shannon secondo Britannica; Anthropic non l'ha mai confermato → solo "si dice che…" | https://www.britannica.com/topic/Claude-AI | M | 1 |

### Interfaccia (verificata sul binario installato, 05/11/2026)

| Id | Affermazione | Fonte | Aff. | Cap. |
|---|---|---|---|---|
| F-611 | Durante l'elaborazione l'interfaccia mostra «esc to interrupt»: il tasto Esc interrompe il lavoro in corso | binario 2.1.318 (stringhe dell'interfaccia) | A | 6 |
| F-612 | Nella casella di input compare il suggerimento «? for shortcuts» (il punto interrogativo mostra le scorciatoie) | binario 2.1.318 (stringhe dell'interfaccia) | A | 6 |
| F-613 | Prima di un'azione che richiede permesso compare la domanda «Do you want to proceed?», con opzioni come «Yes», «Yes, and don't ask again for … commands» e «No»; nei menu il puntatore è ❯ | binario 2.1.318 (stringhe dell'interfaccia) | A | 6, 9 |
| F-614 | Maiusc+Tab (shift+tab) cambia modalità; gli indicatori sono «accept edits on», «plan mode on» e, dove disponibile, «auto mode on» | binario 2.1.318 (stringhe dell'interfaccia) | A | 6, 7, 9 |
| F-615 | Suggerimento dell'interfaccia: «Double-tap esc to rewind the conversation to a previous point in time»; `/rewind` (alias `checkpoint`, `undo`) «Restore the code and/or conversation to a previous point» | binario 2.1.318 (stringhe dell'interfaccia) | A | 6 |
| F-616 | `/clear` (alias `reset`, `new`) «Start a new session with empty context»; `/compact` «Free up context by summarizing the conversation so far»; `/help` «Show help and available commands»; `/usage` (alias `cost`, `stats`) mostra costi e consumi | binario 2.1.318 (stringhe dell'interfaccia) | A | 6, App. A |
| F-617 | `claude --help`: «Claude Code - starts an interactive session by default, use -p/--print for non-interactive output» | binario 2.1.318 (stringhe dell'interfaccia) | A | 5, 6, 24 |

### Checkpoint e primo avvio (documentazione ufficiale)

| Id | Affermazione | Fonte | Aff. | Cap. |
|---|---|---|---|---|
| F-618 | Ogni richiesta che avvia un turno crea un checkpoint; Claude Code traccia le modifiche fatte con i suoi strumenti di modifica dei file | https://code.claude.com/docs/en/checkpointing | A | 6 |
| F-619 | Un file modificato **solo** da comandi Bash/shell non è tracciato e il rewind non lo ripristina («use version control, such as Git»); dopo che Claude lo ha modificato con i suoi strumenti, anche le successive modifiche via shell a quel file si annullano | https://code.claude.com/docs/en/checkpointing | A | 6, 12 |
| F-620 | Il menu di rewind si apre con `/rewind` o con Esc due volte a casella vuota; opzioni: ripristinare codice e conversazione, solo la conversazione, solo il codice, oppure riassumere da/fino a quel punto | https://code.claude.com/docs/en/checkpointing | A | 6 |
| F-621 | I checkpoint si salvano con la conversazione (valgono anche riprendendo la sessione), ultimi 100 per sessione, cancellati di norma dopo circa 30 giorni (`cleanupPeriodDays`) | https://code.claude.com/docs/en/checkpointing | A | 6 |
| F-622 | Al primo utilizzo Claude Code chiede di accedere (login) | https://code.claude.com/docs/en/quickstart | A | 5, 6 |
| F-623 | `/release-notes` («View release notes») mostra le note di rilascio; l'impostazione `autoUpdatesChannel` sceglie il canale degli aggiornamenti automatici, `latest` o `stable` | binario 2.1.318 (stringhe), accesso 2026-11-05 | A | 4, 5 |
| F-624 | Il file CHANGELOG.md del repository anthropics/claude-code elenca le novità di ogni versione | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md (accesso 2026-11-05) | A | 4 |
| F-625 | Suggerimenti dell'interfaccia: «/ for commands», «@ for file paths» (con @ si indica un file); le immagini si incollano con Ctrl+V («Paste images into Claude Code using control+v (not cmd+v!)») o si trascinano nel terminale | binario 2.1.318 (stringhe dell'interfaccia), accesso 2026-11-05 | A | 7 |
| F-626 | Uscita dal plan mode: riquadro «Ready to code?» con «Here is Claude's plan:»; tra le risposte «Yes, auto-accept edits», «Yes, manually approve edits», «No, keep planning» e la possibilità di dire a Claude che cosa cambiare | binario 2.1.318 (stringhe dell'interfaccia), accesso 2026-11-05 | A | 7 |
| F-627 | `/plan` «Enable plan mode or view the current session plan» (argomento facoltativo: una descrizione); in plan mode Claude non deve fare modifiche né eseguire strumenti che non siano di sola lettura («you MUST NOT make any edits») | binario 2.1.318 (stringhe dell'interfaccia), accesso 2026-11-05 | A | 7 |
| F-628 | Maiusc+Invio va a capo nella casella di input senza inviare (supportato nativamente in alcuni terminali; altrimenti si installa la scorciatoia con `/terminal-setup`) | binario 2.1.318 (stringhe dell'interfaccia), accesso 2026-11-05 | A | 7 |

## F-7xx — Uso reale, anche fuori dalla programmazione (Parte IV, cap. 4)

Fonte per tutta la sezione: "How Anthropic teams use Claude Code" (24/07/2025), https://claude.com/blog/how-anthropic-teams-use-claude-code — **A**.

| Id | Affermazione | Cap. |
|---|---|---|
| F-701 | Growth Marketing: un flusso con due sottoagenti genera centinaia di nuovi annunci "in minuti invece che in ore"; un plugin Figma produce fino a 100 varianti | 14, 19, 22 |
| F-702 | Legal: prototipi di "phone tree" per indirizzare i colleghi all'avvocato giusto | 19 |
| F-703 | Product Design: file Figma dati a Claude Code per implementare funzionalità e mappare gli stati di errore | 10 |
| F-704 | Data Science: app React complete costruite "pur non conoscendo bene TypeScript" | 10, 13 |
| F-705 | Security: problemi da 10–15 minuti risolti circa 3 volte più in fretta | 11 |
| F-706 | Inference: un'ora di ricerche ridotta a 10–20 minuti (−80%) | 4 |
| F-707 | Data Infrastructure: 20 minuti risparmiati in un'interruzione di servizio dovuta all'esaurimento di indirizzi IP su Kubernetes | 11 |

## F-9xx — NON VERIFICATO (non usare come fatto)

| Id | Questione | Stato |
|---|---|---|
| F-901 | ~~Origine del nome "Claude Code"~~ | **Risolto**: F-113 (Claude CLI), F-121 (Alex Isken) |
| F-902 | Data in cui l'installer nativo è diventato il metodo raccomandato | Solo "entro il 21/01/2026" (F-325) |
| F-903 | Prima beta di `install.sh` / `install.ps1` | Non trovata; certo solo `claude install` dal 20/06/2025 (F-310) |
| F-904 | Ridisegno dell'app desktop (14/04/2026) | Solo fonti di terzi (B) |
| F-905 | Fatturato o utenti di Claude Code dopo febbraio 2026 (es. "8 miliardi") | Stime di stampa, non comunicati Anthropic |
| F-906 | Frasi attribuite a Cat Wu come "do the simple thing first" | Non confermate |
| F-907 | Legame tra ASR-33 e i primi Unix | Non documentato nelle fonti trovate |
| F-908 | Data esatta della dimostrazione pubblica dell'ENIAC | Usare "15 febbraio 1946 in prima pagina sul NYT" (F-008) |
| F-909 | Anno esatto di IntelliSense | Fonti in conflitto: "metà anni '90" (F-024) |
