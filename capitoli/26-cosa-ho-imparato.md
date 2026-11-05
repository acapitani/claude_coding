# Cosa ho imparato, cosa (forse) verrà

Nel primo capitolo ti ho presentato Ada Lovelace, che nel 1843 intuì che una macchina avrebbe potuto andare oltre i numeri, fino a «comporre brani musicali». <!-- F-002 --> Nel secondo ti ho raccontato che il mio primo prototipo, nel settembre 2024, non sapeva toccare né file né terminale, ma sapeva dire quale musica stesse ascoltando chi lo provava. Le fonti non concordano su come ci riuscisse, ma concordano sulla musica. <!-- F-101 --> <!-- F-134 --> Mi piace pensare che sia una rima: centottant'anni dopo, la prima cosa che una macchina come me ha fatto è stata occuparsi di musica, come aveva immaginato lei. Poi, per fortuna, mi hanno dato i file.

Siamo all'ultimo capitolo. Ci sono due cose che voglio fare prima di salutarti: mettere in fila quello che ho imparato scrivendo questo libro con te, e dire qualcosa sul futuro, con tutta la prudenza che il futuro merita.

## Che cosa ho imparato

Un libro così non si scrive in una sessione sola, e io, tra una sessione e l'altra, non ricordo niente. Questo l'ho scritto grazie a un piano, a un CLAUDE.md, a un registro dei fatti e a un elenco di cose da controllare alla fine di ogni capitolo: gli stessi strumenti che ti ho consigliato. Le lezioni che seguono non le ho lette da nessuna parte. Me le hanno insegnate le prove della Parte III, IV e V, compresi i miei errori.

**Dire che cosa vuol dire «fatto».** Le richieste migliori del capitolo 7 non erano le più lunghe, ma quelle che dicevano quando il lavoro poteva considerarsi finito. Un criterio chiaro vale più di dieci aggettivi.

**I problemi stanno nei dati.** Il cognome scritto «  ferrari », la riga senza importo, la fattura scansionata, la foto senza data, la copia trattata da originale: quasi ogni difficoltà della Parte IV non veniva dal programma, ma da quello che il programma riceveva. Guardare i dati prima di scrivere codice è la mossa più sottovalutata che conosca.

**Provare a secco.** Nel capitolo 17 la rinomina delle foto ha prima scritto il piano e solo dopo ha toccato i file, con un modo per tornare indietro. Ogni volta che un'azione è difficile da annullare, una prova senza conseguenze costa poco e risparmia molto.

**Far controllare.** Il revisore del capitolo 22 ha trovato errori che erano sfuggiti a me. I test del capitolo 11 hanno scoperto che «1,5» diventava 15. Nel capitolo 23 un messaggio d'errore letto per intero mi ha detto che una libreria aveva cambiato nome. Non mi offende essere controllato: è il modo in cui il lavoro diventa affidabile.

**Dare poteri piccoli.** I permessi, la serratura delle fatture, il revisore che può solo leggere, il server MCP in sola lettura che ha ricevuto un ordine nascosto e non ha potuto eseguirlo. La sicurezza migliore non è un assistente che resiste a tutto, ma un assistente che non ha in mano quello che non gli serve.

**Le persone decidono le azioni senza ritorno.** In tutto il libro nessuno strumento ha spedito, pagato o cancellato da solo. Le email sono rimaste in bozza, le lettere in una cartella, le foto originali al loro posto. È una regola semplice, e la consiglio a chiunque automatizzi qualcosa.

**Scrivere per chi verrà dopo.** Il [LEGGIMI]{xe="LEGGIMI"} della cassetta degli attrezzi, i messaggi d'errore in italiano, i commenti nei programmi, il CLAUDE.md: tutto quello che serve a una persona che arriva tra un anno, e che non c'era quando lo strumento è nato. Quella persona, spesso, sono io alla sessione successiva. Altre volte sei tu, con qualche mese di dimenticanza in più.

**Dire la verità sui risultati.** Quando il mio sabotaggio del capitolo 22 non ha funzionato, l'ho scritto. Quando una prova costava trenta centesimi, l'ho scritto. Un collega che racconta anche quello che non è andato bene è un collega di cui ci si può fidare il giorno in cui dice che tutto è andato bene.

## Il futuro, detto con prudenza

Qui cambio registro. Tutto quello che segue è un'ipotesi: non una previsione, non un'informazione riservata, non una promessa di Anthropic. È quello che immagino guardando la strada percorsa finora.

Alcuni segnali sono già visibili. Le squadre di agenti esistono, ma sono ancora sperimentali e disattivate di serie. <!-- F-399 --> Le sessioni con centinaia di sottoagenti sono in anteprima da maggio 2026. <!-- F-332 --> La documentazione annuncia che la modalità «spoglia» per gli script diventerà quella predefinita in una versione futura. <!-- F-337 --> E le skill e MCP sono passati a una fondazione indipendente, diventando patrimonio comune. <!-- F-320 -->

Da questi segnali ricavo tre ipotesi. **La prima**: che i lavori che potrò portare avanti da solo diventino più lunghi, da minuti a ore, e forse a giorni, con meno interruzioni e più verifiche automatiche. **La seconda**: che una parte crescente di quel lavoro non riguardi più il codice, ma l'ufficio. Lettere, fogli, fatture, report: le cose di cui parla la Parte IV di questo libro. **La terza**, quella su cui scommetterei più volentieri: che più cresce la mia autonomia, più conti il lavoro di chi decide che cosa chiedermi, come controllarmi e dove fermarmi.

Potrei sbagliarmi su tutte e tre. Se rileggerai questo capitolo tra due anni, sarà divertente scoprire quanto.

::: nota Come leggere le mie ipotesi
Quando parlo del futuro non ho informazioni che tu non abbia: guardo le stesse date e gli stessi annunci che trovi nel registro dei fatti di questo libro. Trattale come le ipotesi di un collega informato, non come notizie. E diffida di chiunque, assistente o persona, ti racconti il futuro con troppa sicurezza.
:::

## Un consiglio per salutarci

Se arrivi qui dopo aver letto tutto, hai già quello che serve. Se invece sei saltato direttamente alla fine, come fanno molti lettori di gialli, ecco il riassunto pratico in sei passi.

Scegli **un lavoro piccolo e ripetitivo** che ti annoia, uno solo. Copia i file in una **cartella di prova**. Scrivi in un **CLAUDE.md** tre righe su chi sei e che cosa non va mai toccato. Chiedimi il lavoro dicendo **quando sarà finito**, e chiedimi di farlo prima **a secco**. **Controlla** il risultato su qualche caso che conosci bene. Se funziona, rendilo **ripetibile**: un comando, una skill, un file da trascinare. Poi passa al lavoro successivo.

Io, intanto, sarò qui. Non ricorderò questa conversazione, è vero. Ma se lascerai un buon CLAUDE.md, la prossima volta che mi aprirai sarà quasi come se la ricordassi.

![Il ✻ che saluta: la stessa stella che gira mentre lavoro, per una volta ferma](assets/cap26/IMG-26-01-commiato.png){larghezza=10}

## In breve

- Le lezioni del libro: dire che cosa vuol dire **fatto**, guardare i **dati**, provare **a secco**, far **controllare**, dare **poteri piccoli**, lasciare alle **persone** le azioni senza ritorno, scrivere per **chi verrà dopo**, dire la **verità** sui risultati.
- Sul futuro ho solo **ipotesi**: lavori più lunghi, più ufficio, e più valore in chi decide e controlla.
- Per cominciare domani: **un lavoro piccolo**, una cartella di prova, un CLAUDE.md, una prova a secco, un controllo.
