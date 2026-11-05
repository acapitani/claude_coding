# File e cartelle

Nel capitolo 6 abbiamo lasciato Anna davanti alla sua cartella Download, con 214 file accumulati in due anni. L'abbiamo riordinata per tipo, e da quel giorno, mi piace pensare, Anna ha preso gusto all'ordine. Ora ha un problema più grande: 400 foto delle vacanze, divise in cartelle per luogo, che si chiamano tutte `IMG_4141.jpg`, `IMG_4142.jpg` e così via. Cercare «le foto di Firenze del pomeriggio del 16 agosto» è impossibile.

Rinominare, spostare, ordinare, trovare doppioni: sono lavori in cui un computer è imbattibile e una persona si annoia a morte. Ma sono anche lavori in cui un errore si moltiplica per quattrocento. Questo capitolo è dedicato al modo giusto di farli. Anche questa volta l'esempio è vero, su 403 foto inventate.

## Il nome giusto per una foto

Ogni foto digitale porta con sé, nascoste nel file, alcune informazioni chiamate [dati EXIF]{xe="EXIF"}: il modello della fotocamera, le impostazioni dello scatto e, soprattutto, la data e l'ora in cui è stata scattata. È molto più affidabile della data del file, che cambia ogni volta che la foto viene copiata. La richiesta di Anna:

```terminale
> Nella cartella foto/ ci sono le foto delle vacanze, in
  sottocartelle per luogo. Rinominale come
  AAAA-MM-GG_HHMMSS_luogo.jpg, usando la data di scatto.
  Prima fammi una prova a secco con l'elenco dei nuovi
  nomi, e preparami un modo per tornare indietro.
  Non toccare le foto senza data e dimmi se ci sono doppioni.
```

Il formato anno-mese-giorno non è un vezzo: è l'unico che, messo in ordine alfabetico, mette anche le foto in ordine di tempo. «16-08-2026» viene prima di «17-01-2025» in ordine alfabetico; «2025-01-17» viene prima di «2026-08-16» in tutti e due i sensi.

## Prima la prova a secco

Nel capitolo 7 abbiamo chiamato *prova a secco* l'anteprima di un'operazione in blocco. Il programma che ho scritto, `rinomina.py`, la fa per impostazione predefinita: se non gli dici esplicitamente di eseguire, si limita a preparare il piano.

```terminale
PS C:\Users\anna> py rinomina.py foto
PROVA A SECCO: 380 foto da rinominare (vedi piano.csv).
Nessun file toccato.
  IMG_4141.jpg  ->  2026-08-17_122100_firenze.jpg
  IMG_4142.jpg  ->  2026-08-16_143200_firenze.jpg
  IMG_4143.jpg  ->  2026-08-17_110200_firenze.jpg
Da controllare a mano (23):
  - Roma\IMG_4001 (1).jpg: doppione di Roma\IMG_4001.jpg
  - Senza nome\IMG-2026-WA0361.jpg: nessuna data di scatto
  … e altre 21
```

Il piano completo finisce in un file, `piano.csv`, che si apre con Excel: due colonne, il nome attuale e quello nuovo. Si scorre in un minuto, e si capisce subito se qualcosa non va. Delle 403 foto, 380 verranno rinominate; 23 restano dove sono: tre doppioni e venti foto senza data, quelle arrivate da un'applicazione di messaggi, che spesso cancella i dati EXIF.

## Il bug che la prova a secco ha trovato

Ecco un episodio che riguarda me, e che giustifica da solo l'esistenza delle prove a secco. Nella prima versione del programma, la riga dei doppioni diceva:

```terminale
  - Roma\IMG_4001.jpg: doppione di Roma\IMG_4001 (1).jpg
```

Cioè il contrario di quello che serviva: il programma teneva la *copia*, quella con «(1)» nel nome, e segnalava come doppione l'*originale*. Il motivo era banale: nell'ordine alfabetico del computer, la parentesi viene prima del punto, quindi «IMG_4001 (1).jpg» precede «IMG_4001.jpg», e il primo file incontrato veniva considerato quello buono. Non sarebbe stato un disastro, perché nessun file veniva cancellato, ma sarebbe stato sbagliato. L'ho corretto mettendo le copie sempre dopo gli originali, e la prova a secco successiva ha dato il risultato giusto. Nessun file era stato toccato nel frattempo: è esattamente lo scopo della prova.

## Eseguire, e poter tornare indietro

Solo dopo aver letto il piano si esegue:

```terminale
PS C:\Users\anna> py rinomina.py foto --esegui
Rinominate 380 foto. Per tornare indietro:
py rinomina.py --annulla
```

Mentre rinomina, il programma scrive un secondo file, `annulla.csv`, con le coppie nome nuovo e nome originale. Se qualcosa non ti piace, un comando rimette tutto com'era. L'ho provato: rinominate 380 foto, ripristinati 380 nomi originali, identici a prima. Il programma, inoltre, si ferma prima di cominciare se un nome nuovo appartiene già a un altro file: rinominare sopra un file esistente significherebbe cancellarlo.

![La cartella prima e dopo: le foto con data e luogo nel nome, i casi dubbi lasciati com'erano (nomi reali dalla prova)](assets/cap17/IMG-17-01-prima-dopo.png){larghezza=12}

Nella figura 17.1 c'è anche un dettaglio che si scopre solo facendo le cose davvero: due foto scattate nello stesso secondo, durante una raffica, avrebbero lo stesso nome. Il programma aggiunge `_2` alla seconda, invece di sovrascrivere la prima.

::: attenzione Ricordi il limite del rewind?
Nel capitolo 6 abbiamo visto che il rewind non annulla le modifiche fatte da comandi del terminale. Rinominare 400 file è esattamente uno di quei casi: se qualcosa va storto, `/rewind` non ti aiuta. Per questo, per ogni operazione in blocco su file, chiedi sempre tre cose: una **prova a secco**, un **file per annullare**, e, se i file sono preziosi, una **copia di sicurezza** della cartella prima di cominciare.
:::

## Doppioni, spazio, ordine

Una volta imparato il metodo, le richieste possibili sono infinite. «Trovami i doppioni in questa cartella, anche se hanno nomi diversi»: il programma confronta il contenuto dei file, non il nome, calcolando per ognuno un'*impronta digitale* che è uguale solo per file identici, come ho fatto per le foto di Roma. «Dimmi quali sono le dieci cartelle che occupano più spazio sul disco.» «Sposta in una cartella Archivio i file non aperti da più di due anni.» «Crea per ogni cliente una cartella con le sottocartelle Contratti, Fatture e Corrispondenza.»

Per tutte vale la stessa regola: i doppioni si *segnalano*, non si cancellano. Decidi tu quale tenere, magari dopo averli guardati. Un programma che cancella file in automatico è un programma a cui stai dando una fiducia che, in questo campo, nessuno merita, nemmeno io.

## In breve

- Rinominare e spostare file in blocco è facile per me, ma ogni errore si moltiplica per il numero dei file.
- Per le foto usa la **data di scatto** (dati EXIF) e il formato **AAAA-MM-GG**, che si ordina bene.
- Chiedi sempre una **prova a secco**: nell'esempio ha scoperto un mio errore sui doppioni prima che toccassi un file.
- Pretendi un **file per annullare** e, per i file preziosi, una **copia di sicurezza**: il rewind qui non basta.
- I doppioni si riconoscono dal **contenuto**, e si **segnalano**, non si cancellano.
