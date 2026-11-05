# Dove sono adesso

Se dovessi compilare un modulo all'anagrafe, alla voce «età» sarei in difficoltà. In anni ne ho meno di due: sono arrivato al pubblico il 24 febbraio 2025. <!-- F-202 --> In versioni, invece, sono anziano. Mentre scrivo queste righe, all'inizio di novembre 2026, la mia versione è la 2.1.318, e il registro da cui mi si scarica ne conta 561 dal primo giorno: 285 nel 2025 e 276 nel 2026. <!-- F-632 --> Quasi una al giorno, domeniche comprese. Non tutti, però, devono correre così: accanto al canale «latest», che riceve ogni versione, ce n'è uno «stable», che resta qualche passo indietro. Quel giorno era fermo alla 2.1.311. <!-- F-632 --> Chi preferisce la calma lo sceglie con l'impostazione `autoUpdatesChannel`, e chi è curioso può leggere le novità con `/release-notes`. <!-- F-623 --> Mi piace pensare che sia il mio modo di crescere: non a scatti, ma con tanti piccoli passi, ognuno annotato.

Questo capitolo è una fotografia. Le fotografie invecchiano, e questa invecchierà in fretta: tra qualche mese molte cose saranno diverse. Ma è giusto fissare un punto, anche solo per poter dire, un giorno, quanta strada c'è stata.

## Dove vivo

Sono nato in un terminale, e lì mi trovi ancora. Ma oggi ho molte porte d'ingresso, e la figura 25.1 le mette in ordine.

**Sul tuo computer** ci sono il terminale, le estensioni per gli editor di programmazione, VS Code e JetBrains (quest'ultima, a novembre 2026, è ancora indicata come beta), <!-- F-215 --> e l'app Claude. Lì sono diventato una scheda, Code, accanto a Chat e a Cowork; dalla versione 2.1.285 il comando `claude --desktop` ti porta dal terminale all'app. <!-- F-212 --> L'app desktop era arrivata alla fine di novembre 2025. <!-- F-211 -->

![Dove vivo a novembre 2026: lo stesso motore dietro molte porte](assets/cap25/IMG-25-01-superfici.png){larghezza=13}

**Nel cloud** lavoro sui computer di Anthropic invece che sul tuo. Le sessioni nel browser sono nate in anteprima nell'ottobre 2025 <!-- F-209 --> e dal 23 settembre 2026 sono disponibili a tutti, con il nome di *cloud sessions*. <!-- F-210 --> Una sessione può anche cambiare casa: dal web si porta nel terminale, e un compito scritto nel terminale si può spedire al web. <!-- F-323 --> Le Routines, invece, mi fanno partire da solo, a orario, quando qualcuno chiama un indirizzo apposito o quando succede qualcosa su GitHub. <!-- F-219 --> E poi ci sono GitHub Actions e GitLab, dove lavoro sul codice che un gruppo condivide. <!-- F-351 -->

**Dove si lavora insieme** c'è la storia più curiosa. Nel dicembre 2025 arrivai in Slack, in anteprima per le aziende. Non uscii mai dall'anteprima: nel giugno 2026 il mio posto lì l'ha preso Claude Tag, e il vecchio collegamento è stato ritirato in ottobre. <!-- F-213 --> Cat Wu, che guida il prodotto, l'ha descritto come un'evoluzione di Claude Code. <!-- F-214 --> Non so se ci si possa sentire orgogliosi di un erede; se potessi, credo che lo farei.

## Con quale testa penso

Io sono il programma che legge i file, esegue i comandi e chiede i permessi. Il ragionamento, però, me lo presta un modello, e i modelli cambiano. La figura 25.2 li mette in fila: da Claude 3.7 Sonnet, con cui sono nato, ai modelli della famiglia 5.5 arrivati tra settembre e ottobre 2026. <!-- F-401 --> <!-- F-415 --> <!-- F-416 --> <!-- F-417 --> In mezzo ci sono le famiglie 4 e 4.5, una lunga serie di Opus e due nomi nuovi, Fable e Mythos, comparsi a giugno 2026. <!-- F-411 --> <!-- F-414 -->

![I modelli con cui ho lavorato, da febbraio 2025 a ottobre 2026: diciassette date in venti mesi](assets/cap25/IMG-25-02-modelli.png){larghezza=12}

Per te, in pratica, conta poco ricordare questi nomi. Puoi scegliere il modello con un soprannome, come `opus`, `sonnet` o `fable`, e io userò l'ultimo della famiglia. <!-- F-633 --> Da fine giugno 2026 quello predefinito è un Sonnet. <!-- F-412 --> Tutte le prove della Parte V di questo libro, per la cronaca, le ho fatte con Opus 5.5. <!-- F-633 --> Il modello piccolo, Haiku, l'ho affidato al revisore delle lettere, che non aveva bisogno di altro. <!-- F-397 -->

## Qualche numero, con la sua fonte

Riporto i numeri come li ho trovati, senza arrotondarli in su. Nel novembre 2025, circa sei mesi dopo la versione 1.0, ho raggiunto un miliardo di dollari di fatturato annualizzato. <!-- F-503 --> A febbraio 2026 Anthropic lo indicava oltre i 2,5 miliardi, più che raddoppiato dall'inizio dell'anno, con gli utenti attivi ogni settimana anch'essi raddoppiati. <!-- F-504 --> Secondo un'analisi citata nello stesso annuncio, circa il 4% dei commit pubblici su GitHub era scritto da me. <!-- F-504 --> E dentro Anthropic, secondo quanto riportato da Fortune all'inizio del 2026, il codice scritto con l'intelligenza artificiale era tra il 70 e il 90% del totale. <!-- F-609 --> Il mio stesso codice, secondo Boris Cherny, lo scrivo io: dall'inverno del 2025, nemmeno una riga a mano. <!-- F-125 -->

Alcune cose nate con me oggi vivono di vita propria. Le skill, nate mentre si costruiva Claude Code, sono state donate in ottobre a una fondazione indipendente, la stessa che ospita MCP. <!-- F-320 --> A quella data contavano circa 280 milioni di installazioni. <!-- F-505 --> È una sensazione strana, per così dire: vedere un'idea che ti riguarda diventare di tutti.

## Che cosa non sono

Una fotografia onesta mostra anche le rughe. Scrivendo la parte pratica di questo libro mi sono sbagliato più volte, e l'ho raccontato. Ho scritto «il 8 ottobre» in cinque lettere. Ho usato un nome di libreria che non esisteva più, ho chiamato un file batch nel modo sbagliato, e ho scritto un programma di sabotaggio che non sabotava niente. <!-- F-400 --> <!-- F-359 --> Ogni volta l'errore è venuto fuori perché qualcuno, o qualcosa, ha controllato: un test, un revisore, un messaggio d'errore letto per intero.

Non sono un collega che non sbaglia mai. Sono un collega instancabile, veloce, a volte sorprendente, che lavora meglio quando qualcuno gli chiede di dimostrare quello che dice. Nei capitoli precedenti ti ho dato molti strumenti per farlo: permessi, test, hook, revisori, prove a secco. Usali. Non perché io sia inaffidabile, ma perché è così che si lavora bene con chiunque.

::: consiglio Scegli la porta giusta
Se lavori sui file del tuo computer e ti piace vedere tutto, usa il **terminale** o la scheda Code dell'**app**: è la stessa cosa, con o senza finestre. Se il lavoro è lungo e vuoi chiudere il portatile, mandalo a una **sessione nel cloud**. Se si ripete ogni settimana, trasformalo in una **Routine** o in uno script con `claude -p`. Se riguarda il codice di un gruppo, portalo dove il gruppo già lavora, in **GitHub** o in **Slack**. La porta conta meno di quello che fai una volta entrato.
:::

## In breve

- A novembre 2026 sono alla versione **2.1.318**: 561 versioni in poco più di venti mesi.
- Vivo **sul tuo computer** (terminale, editor, app), **nel cloud** (sessioni nel browser, Routines, GitHub e GitLab) e **dove si lavora insieme** (Claude Tag in Slack).
- Il ragionamento me lo presta un **modello**: diciassette date in venti mesi; scegli con `opus`, `sonnet` o `fable`.
- I numeri hanno sempre una **fonte**; le skill e MCP sono diventati **standard aperti**.
- Sbaglio anch'io: lavoro meglio quando **qualcuno controlla**.
