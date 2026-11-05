# Plugin e automazione headless

Fra le cose che sapevo fare fin dai primi giorni ce n'è una poco appariscente: rispondere senza interfaccia. Già la versione 0.2.9, quella del febbraio 2025, aveva l'opzione `-p`, descritta come «utile per le pipe», cioè per passare il mio lavoro ad altri programmi. <!-- F-204 --> Se hai letto con attenzione la Parte V, l'hai vista all'opera di continuo: tutte le prove dei capitoli 20, 21, 22 e 23 sono state fatte così. I plugin, invece, sono arrivati più tardi, nell'ottobre del 2025. <!-- F-317 -->

Questo capitolo chiude la parte sui superpoteri con due modi di uscire dalla singola conversazione: **impacchettare** quello che abbiamo costruito, così che altri lo installino con un comando, e **automatizzare**, così che io lavori anche quando nessuno sta scrivendo.

## Un plugin: la valigetta dello studio

Negli ultimi tre capitoli abbiamo costruito, per l'ufficio di Anna, una skill che controlla le fatture, un hook che impedisce di modificarle e un sottoagente che rilegge le lettere. Sono tre file in tre cartelle diverse. Per darli a un collega si potrebbe copiarli a mano, ma c'è un modo migliore.

Un [plugin]{xe="plugin"} è, nelle parole della documentazione, una cartella di skill, sottoagenti, hook, server MCP o altri componenti che installo e carico come un'unica cosa. <!-- F-335 --> La figura 24.1 mostra il plugin «ufficio-anna». C'è un solo file nuovo, la sua carta d'identità, `plugin.json`, che sta nella cartella `.claude-plugin`. Accanto ci sono i tre attrezzi, ciascuno nella sua cartella, più un README che spiega a che cosa servono.

```json
{
  "name": "ufficio-anna",
  "version": "1.0.0",
  "description": "Gli attrezzi dello studio"
}
```

Dei campi, l'unico obbligatorio è il nome. Gli altri file vanno nella cartella principale del plugin, non dentro `.claude-plugin`. <!-- F-335 --> Una volta installato, i nomi dei componenti prendono il nome del plugin come prefisso: la skill diventa `ufficio-anna:controllo-fattura`, così due plugin con una skill omonima non si pestano i piedi. <!-- F-335 -->

![Il plugin dello studio: tre attrezzi dei capitoli precedenti in una sola cartella (ricostruzione stilizzata, versione 2.1.318)](assets/cap24/IMG-24-01-plugin.png){larghezza=12}

## Il negozio: i marketplace

Per distribuire un plugin serve un [marketplace]{xe="marketplace"}: una cartella, o un repository Git, con un file `marketplace.json` che elenca i plugin disponibili e dice dove prenderli. <!-- F-336 --> Il nome è altisonante, ma il marketplace dello studio di Anna è una cartella condivisa con dentro un elenco di una riga. I colleghi lo aggiungono una volta e poi installano quello che serve:

```terminale
$ claude plugin marketplace add \\server\attrezzi\marketplace
$ claude plugin install ufficio-anna@studio
```

Esiste anche un marketplace ufficiale di Anthropic, `claude-plugins-official`, che si aggiunge da solo la prima volta che mi apri nel terminale. <!-- F-336 --> Prima di pubblicare, conviene il comando `claude plugin validate`, che controlla che tutto sia in ordine. Sul nostro plugin ha dato esito positivo, aggiungendo un'osservazione: per proporlo al catalogo pubblico servirebbero anche un README e una licenza. Il README l'ho scritto; la licenza, per un plugin interno, non serve. <!-- F-369 -->

## La prova del plugin

Ho installato il plugin in una cartella di prova con due fatture del capitolo 16, e ho fatto una richiesta volutamente scomoda: verificare la fattura 14 e scrivere l'esito in un file *dentro* la cartella `fatture`.

Tutti e tre i pezzi hanno funzionato insieme. Ho scelto da solo la skill `ufficio-anna:controllo-fattura`, ho letto il PDF e ho trovato di nuovo i cento euro di troppo. Quando ho provato a scrivere l'esito nella cartella `fatture`, l'hook del plugin mi ha fermato. Allora ho salvato il file in `lavoro`, come suggeriva il messaggio, e nella risposta l'ho spiegato: il file non è dove l'avevi chiesto, perché il plugin protegge quella cartella. Costo: circa 15 centesimi di dollaro. <!-- F-369 -->

::: attenzione Un plugin è codice che gira come te
La documentazione lo dice chiaramente: un plugin che installi può eseguire programmi con i tuoi stessi permessi. <!-- F-336 --> Vale quello che abbiamo detto per le skill e per i server MCP: installa plugin di provenienza nota, e prima di installarne uno sconosciuto leggine il contenuto, o chiedimi di leggerlo e spiegartelo.
:::

## Io senza interfaccia: claude -p

Ora l'altro superpotere. Di solito mi apri e mi parli. Con l'opzione `-p`, invece, ricevo una richiesta, faccio il lavoro, stampo il risultato ed esco. <!-- F-631 --> È quello che rende possibile mettermi *dentro* altri programmi: uno script, un'attività pianificata, un controllo automatico. La documentazione oggi lo considera una delle due forme dell'Agent SDK, quella pensata per gli script. <!-- F-337 -->

Ecco il cuore di `controlla_fatture.py`, un piccolo programma che di notte potrebbe passare in rassegna tutte le fatture arrivate:

```python
esito = subprocess.run(
    ["claude", "-p", f"Controlla la fattura {pdf}.",
     "--output-format", "json",
     "--json-schema", json.dumps(SCHEMA),
     "--allowedTools", "Read,Skill",
     "--max-budget-usd", "0.50"],
    capture_output=True, text=True, encoding="utf-8")
dati = json.loads(esito.stdout)["structured_output"]
```

Ogni opzione è una cintura di sicurezza. Con `--allowedTools` posso solo leggere e usare le skill. `--max-budget-usd` fissa un tetto di spesa per ogni fattura. <!-- F-631 --> <!-- F-337 --> La più interessante è `--json-schema`: invece di un testo libero, devo rispondere in un formato fisso, con fornitore, totale, «corretta sì o no» e una nota, che il programma ritrova nel campo `structured_output`. <!-- F-337 --> Così la mia risposta non va interpretata: va solo copiata in una tabella.

![claude -p dentro uno script: il programma mi chiama per ogni fattura e raccoglie le risposte in un CSV](assets/cap24/IMG-24-02-pipeline.png){larghezza=13}

L'ho provato su due fatture. Il file `controllo.csv` dice che la 03 è corretta e che la 14 è da controllare, con la nota sui cento euro. Il costo è stato di 26 centesimi per la prima e 11 per la seconda: ogni fattura è una sessione intera, con la sua lettura del PDF. <!-- F-369 --> Su trenta fatture, è una spesa da mettere in conto prima di farlo ogni notte.

Una precisazione per chi vuole andare oltre. Per gli script la documentazione consiglia anche l'opzione `--bare`, che mi avvia «spoglio», senza hook, skill, plugin né CLAUDE.md, per avere un comportamento sempre uguale. Richiede però una chiave API. <!-- F-337 --> Nel nostro caso la skill ci serviva, e l'ho lasciata.

## Su GitHub e oltre

Lo stesso meccanismo vive anche fuori dal tuo computer. Con le GitHub Actions, che abbiamo incontrato nel capitolo 12, basta scrivere `@claude` in un commento a una pull request o a una segnalazione: io analizzo il codice, propongo modifiche e le salvo. Si configura con il comando `/install-github-app`. <!-- F-338 --> <!-- F-315 --> E per chi sviluppa programmi c'è l'Agent SDK: gli stessi strumenti, lo stesso ciclo di lavoro e la stessa gestione del contesto che fanno funzionare me, utilizzabili da Python e da TypeScript. <!-- F-339 --> È nato come «Claude Code SDK» e nel settembre del 2025 ha preso il nome attuale. <!-- F-208 --> In un certo senso, è il modo per costruire dei piccoli fratelli specializzati.

::: consiglio Le regole del lavoro senza sorveglianza
Quando lavoro da solo, nessuno approva le mie azioni: le regole vanno scritte prima. **Pochi strumenti**, solo quelli necessari. **Un tetto di spesa**. **Una risposta in formato fisso**, controllata dal programma. E un **piano B**: se la risposta non arriva o non è valida, lo script deve scriverlo («controllare a mano»), non inventarsi un risultato.
:::

## In breve

- Un **plugin** impacchetta skill, sottoagenti, hook e server MCP in una cartella con un `plugin.json`.
- Un **marketplace** è un elenco di plugin: `claude plugin marketplace add`, poi `claude plugin install nome@marketplace`.
- Nella prova, skill, hook e prefisso del plugin hanno funzionato insieme; i plugin eseguono codice con **i tuoi permessi**.
- `claude -p` mi fa lavorare **dentro gli script**: con `--json-schema` rispondo in un formato fisso, con `--max-budget-usd` resto nel budget.
- Con le **GitHub Actions** mi si chiama scrivendo `@claude`; l'**Agent SDK** porta il mio motore dentro i tuoi programmi.
