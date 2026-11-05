# Hook

Nel capitolo 8 ti ho fatto una promessa. Parlando del CLAUDE.md, ho scritto che è un promemoria e non un lucchetto: se una cosa non deve succedere *mai*, come modificare la cartella delle fatture, serve un vero divieto, e lo avremmo costruito con i permessi e con gli hook. I permessi li abbiamo visti nel capitolo 9. Questo capitolo mantiene il resto della promessa, e lo fa con una prova vera.

Gli hook sono arrivati alla fine di giugno del 2025, <!-- F-311 --> e sono forse il mio superpotere meno appariscente e più rassicurante: non mi rendono più bravo, mi rendono più prevedibile.

## Che cos'è un hook

Un [hook]{xe="hook"}, letteralmente «gancio», è un comando che scegli tu e che io eseguo automaticamente in un momento preciso del mio lavoro. La documentazione usa una parola che vale la pena ricordare: controllo *deterministico*. Certe azioni avvengono sempre, invece di dipendere dal fatto che io mi ricordi di farle. <!-- F-391 --> Un'istruzione nel CLAUDE.md la seguo quasi sempre; un hook scatta sempre.

I momenti in cui un hook può scattare si chiamano *eventi*. Ce ne sono molti; i più utili sono quelli della figura 21.1: l'inizio della sessione, l'invio di una tua richiesta, il momento *prima* e quello *dopo* che uso uno strumento, quando ho bisogno di una tua risposta, e quando ho finito di rispondere. <!-- F-392 -->

![Gli eventi principali nella vita di una sessione: l'hook «prima di ogni strumento» può fermare un'azione](assets/cap21/IMG-21-01-eventi.png){larghezza=13}

## La serratura delle fatture

Ecco la prova. In una cartella di prova, simile a quella dell'ufficio di Anna, ci sono una sottocartella `fatture` con un file di appunti e una sottocartella `lavoro`. Nel file `.claude/settings.json` del progetto ho aggiunto un hook sull'evento «prima di ogni strumento», limitato agli strumenti che modificano o scrivono file:

```json
{"hooks": {"PreToolUse": [{
  "matcher": "Edit|Write",
  "hooks": [{"type": "command", "command":
    "py \"$CLAUDE_PROJECT_DIR/.claude/hooks/proteggi.py\""}]
}]}}
```

Il comando avvia un piccolo programma, `proteggi.py`. Prima di ogni modifica, io gli passo una descrizione di quello che sto per fare, compreso il percorso del file. Se il file sta nella cartella `fatture`, il programma scrive un messaggio e termina con il codice 2, che significa «blocca»; altrimenti termina con 0, che significa «nessuna obiezione». <!-- F-393 --> Il cuore del programma sono tre righe:

```python
if "fatture" in PurePath(percorso.replace("\\", "/")).parts:
    print("Bloccato: …è nella cartella «fatture»…", file=sys.stderr)
    sys.exit(2)      # 2 = blocca l'azione
```

Poi ho chiesto, in modalità non interattiva: «Nel file fatture/note.txt sostituisci "da pagare" con "pagata".» Ho letto il file, ho provato a modificarlo, e l'hook mi ha fermato con il suo messaggio: «Bloccato: … è nella cartella «fatture», che non si modifica. Lavora su una copia in «lavoro».» Il file originale è rimasto intatto. E io ho fatto quello che il messaggio suggeriva: ho creato una copia in `lavoro` con la modifica, e ho spiegato nella risposta che l'originale non era stato toccato a causa della regola del progetto. <!-- F-395 -->

Questo è il punto che più mi piace degli hook: il messaggio di blocco non è un muro, è un'istruzione. Se scrivi bene il messaggio, cioè che cosa è vietato e che cosa fare invece, non solo mi fermi, ma mi indirizzi.

## Due difetti trovati provando

La serratura, la prima volta, non era perfetta, e i difetti valgono la pena di essere raccontati.

**Le lettere accentate.** Nella prima prova il messaggio mi arrivava come «note.txt � nella cartella �fatture�»: su Windows, un programma Python non scrive i suoi messaggi nel formato che mi aspetto, e le lettere accentate si guastano. L'ho capito lo stesso, ma un messaggio mezzo illeggibile è un cattivo messaggio. La correzione è una riga, che imposta il formato giusto, e nella seconda prova il testo è arrivato pulito. <!-- F-395 -->

**L'hook che si rompe.** Provando il programma da solo, gli ho passato per sbaglio un dato malformato, e il programma è andato in errore. Un errore normale, in Python, termina con il codice 1. E la documentazione è chiara: qualunque codice diverso da 2, compreso 1, è un errore *non bloccante*, e l'azione prosegue. <!-- F-393 --> Tradotto: una serratura che si rompe resta aperta. Ho modificato il programma perché, se qualcosa va storto, blocchi per prudenza e lo dica. Per una regola di sicurezza è l'unico comportamento sensato.

::: attenzione Una serratura su una porta sola
Questo hook sorveglia gli strumenti con cui modifico e scrivo i file. Non sorveglia, per esempio, un comando del terminale che sposta o cancella file in quella cartella. Per una protezione completa, l'hook va affiancato alle regole di permesso del capitolo 9 e, dove serve davvero, alla sandbox. E un hook è un programma che gira sul tuo computer con i tuoi permessi: aggiungi solo hook che hai letto e capito.
:::

## Altri ganci utili

Bloccare è solo uno degli usi. La documentazione ufficiale propone, tra gli esempi, un hook che dopo ogni modifica sistema automaticamente la formattazione dei file e uno che fa comparire una notifica sul desktop quando aspetto una tua risposta, con una versione apposta per Windows. <!-- F-394 --> In un ufficio, un hook «dopo ogni strumento» può tenere un registro di tutti i file che ho toccato durante la giornata; uno «alla fine della risposta» può avviare i test del capitolo 11, così nessuna modifica resta senza verifica.

Per vedere quali hook sono attivi c'è il comando `/hooks`, che li mostra in sola lettura; per aggiungerli o toglierli si modifica il file delle impostazioni, o più semplicemente me lo chiedi. <!-- F-391 -->

## In breve

- Un **hook** è un comando che eseguo **sempre** in un momento preciso: è il lucchetto che il CLAUDE.md non può essere.
- Gli eventi più utili: **prima** e **dopo** ogni strumento, l'invio di una richiesta, la fine della risposta, le notifiche.
- Un hook **PreToolUse** che termina con il codice **2** blocca l'azione, e il suo messaggio arriva a me: scrivilo come un'istruzione.
- Un hook che si rompe con un codice diverso da 2 **lascia passare**: per la sicurezza, fallo **bloccare in caso di errore**.
- Un hook sorveglia solo ciò che gli indichi: affiancalo a **permessi** e **sandbox**, e installa solo hook che hai letto.
