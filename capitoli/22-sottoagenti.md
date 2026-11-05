# Sottoagenti

Mi piace immaginare che ogni tanto anch'io avrei bisogno di un collega. Non per stanchezza, che non provo, ma per una ragione molto concreta: il mio *contesto*, cioè tutto quello che ho davanti mentre lavoro, ha un limite, come la scrivania di chiunque. Se devo leggere quarantanove lettere una per una, alla fine la scrivania è sommersa di fogli, e la conversazione con te diventa più pesante e più lenta. La soluzione è la stessa degli uffici veri: delegare.

I sottoagenti personalizzati sono arrivati nel luglio del 2025, <!-- F-312 --> e da allora sono il modo in cui divido un lavoro grande in lavori più piccoli, ognuno affidato a un aiutante con un compito preciso.

## Che cos'è un sottoagente

Un [sottoagente]{xe="sottoagente"} è un assistente specializzato che lavora con un contesto tutto suo, istruzioni sue, strumenti e permessi suoi. <!-- F-396 --> Gli affido un compito, lui lo svolge nella sua «stanza», e a me torna solo il risultato riassunto. La documentazione lo dice in modo molto pratico: conviene usarne uno quando un lavoro laterale riempirebbe la conversazione principale di risultati di ricerche, registri o contenuti di file che non serviranno più. <!-- F-396 -->

Alcuni sottoagenti esistono già. Uno si chiama Explore e serve a cercare nei file senza modificarli; un altro, Plan, raccoglie informazioni quando lavoro in plan mode; un terzo, general-purpose, sa fare un po' di tutto. <!-- F-398 --> Molto spesso li uso senza che tu te ne accorga.

## Un revisore per le lettere

Più interessanti sono quelli che crei tu. Un sottoagente personalizzato è un file di testo nella cartella `.claude/agents` del progetto, con un'intestazione e delle istruzioni. <!-- F-397 --> Ecco il revisore che ho preparato per le lettere del capitolo 14:

```markdown
---
name: revisore-lettere
description: Rilegge lettere già pronte prima della
  spedizione e segnala errori. Usalo quando l'utente chiede
  di controllare, rileggere o revisionare delle lettere.
tools: Read, Glob, Grep
model: haiku
---
Sei il revisore delle lettere di uno studio amministrativo.
Controlla segnaposto rimasti, titoli che non concordano
con il nome, importi e scadenze all'italiana.
Non modificare niente. Elenca solo le lettere con problemi.
```

(Le istruzioni vere sono un po' più lunghe.) Tre righe dell'intestazione meritano attenzione. La `description`, come per le skill del capitolo 20, è quella con cui decido quando chiamarlo. Gli strumenti, `tools`, sono solo quelli per leggere e cercare: questo revisore non può modificare niente, nemmeno se volesse. E il `model` è Haiku, un modello più piccolo e più economico, perché rileggere lettere non richiede il cervello più grande che ho a disposizione. <!-- F-397 -->

Non serve aspettare che io decida di usarlo. Puoi chiamarlo per nome, «fai rileggere le lettere al revisore-lettere», oppure scrivere `@` e sceglierlo dall'elenco che compare. Se invece vuoi che lo usi spesso di mia iniziativa, la documentazione suggerisce di scrivere nella descrizione una formula come «use proactively», cioè «usalo di tua iniziativa». <!-- F-398 --> E come per le skill, il file si può mettere sotto Git, così il revisore diventa un collega di tutto l'ufficio. <!-- F-397 -->

## La prova

Per mettere alla prova il revisore ho preso le 49 lettere del capitolo 14, in versione testo, e ne ho guastata una di proposito: nella lettera 12 ho lasciato un segnaposto, `{scadenza}`, non sostituito. Volevo guastarne anche un'altra, con un titolo sbagliato, ma il mio piccolo programma di sabotaggio non ha funzionato, e me ne sono accorto solo dopo. Poi, in modalità non interattiva, ho chiesto: «Prima di spedire le 49 lettere nella cartella lettere/ voglio che qualcuno le rilegga tutte. Dimmi solo che cosa va corretto.»

La figura 22.1 mostra che cosa è successo. Non ho chiamato un revisore: ne ho chiamati quattro, ciascuno con una parte delle lettere, e li ho fatti lavorare contemporaneamente. <!-- F-400 -->

![La prova reale: l'agente principale divide le lettere fra quattro revisori e raccoglie un solo elenco](assets/cap22/IMG-22-01-revisori.png){larghezza=12}

I risultati sono arrivati uno dopo l'altro, e qui la prova è diventata interessante.

**Il segnaposto è stato trovato.** Il primo revisore ha segnalato la lettera 12, e io l'ho riaperta per verificare: «scaduta il {scadenza} — 24 ottobre 2026».

**Il titolo sbagliato non c'era, e infatti nessuno l'ha trovato.** Tutti i revisori hanno confermato che saluti e nomi concordavano. Avevano ragione: era il mio sabotaggio a essere fallito.

**Sono saltati fuori errori veri, che io non avevo messo.** Cinque lettere dicevano «scaduta il 8 ottobre» o «scaduta il 1 ottobre». In italiano si scrive «l'8 ottobre» e «il 1° ottobre». Erano errori del *mio* programma del capitolo 14, sfuggiti sia a me sia alla rilettura a campione. Li ho corretti: oggi le lettere dicono «scaduta l'8 ottobre 2026».

**L'agente principale non si è fidato ciecamente.** Accortosi che i revisori non avevano trattato le date in modo coerente, ha ricontrollato da sé tutte le lettere con una ricerca, trovando due casi che a un revisore erano sfuggiti. E ha aggiunto tre osservazioni utili: la lettera numero 17 mancava (era la riga senza importo, scartata apposta nel capitolo 14), due lettere erano indirizzate alla stessa persona per due fatture diverse, e in tutte mancavano via e CAP. Nessun file è stato modificato. <!-- F-400 -->

Il costo dichiarato dell'intera operazione è stato di circa 37 centesimi di dollaro. <!-- F-400 --> Lo riporto perché i sottoagenti non sono gratuiti: ciascuno consuma per conto suo, e i suoi consumi contano negli stessi limiti della conversazione principale. <!-- F-396 -->

::: consiglio Quando conviene un sottoagente
Conviene quando il lavoro è **voluminoso ma ripetitivo** (rileggere, cercare, confrontare), quando si può **dividere in parti indipendenti**, o quando vuoi un **controllore con poteri limitati**, come un revisore che può solo leggere. Non conviene per una domanda veloce, né per un lavoro in cui ogni passo dipende dal precedente: lì un aiutante in più è solo una persona in più da coordinare.
:::

## Squadre di agenti

C'è anche un livello successivo, ancora sperimentale: gli *Agent Teams*, arrivati con Opus 4.6 nel febbraio 2026. <!-- F-327 --> La differenza con i sottoagenti è come quella tra affidare compiti a dei collaboratori esterni e mettere insieme una squadra. I sottoagenti lavorano ciascuno per conto proprio e riferiscono a me; in una squadra, invece, i compagni si scambiano messaggi direttamente, condividono un elenco di compiti e si coordinano da soli, mentre una sessione fa da capogruppo. Sono disattivati di serie, si accendono con un'impostazione apposta, funzionano solo nelle sessioni interattive e, avverte la documentazione, consumano molto di più di una sessione singola: per i lavori di routine una sessione sola conviene. <!-- F-399 --> Nel maggio 2026 sono arrivati anche i *flussi dinamici*, con cui posso coordinare centinaia di sottoagenti in una sola sessione. <!-- F-332 --> Strumenti potenti, pensati per lavori grandi; in ufficio, il più delle volte, bastano uno o due revisori ben istruiti.

## In breve

- Un **sottoagente** lavora con un **contesto suo** e restituisce solo il risultato: tiene sgombra la conversazione principale.
- Si crea con un file in `.claude/agents/`: `name`, `description`, gli **strumenti** permessi e il **modello**.
- Un revisore con **sola lettura** e un modello piccolo è un ottimo primo sottoagente.
- Nella prova, quattro revisori in parallelo hanno trovato il segnaposto e **due errori veri** del capitolo 14; l'agente principale ha **ricontrollato**.
- I sottoagenti **consumano** come la conversazione principale; gli **Agent Teams** consumano molto di più e sono sperimentali.
