# Specifica — Output di stampa (Pixartprinting)

**Nome feature suggerito:** `output-stampa`
**Tipo di lavoro:** impaginazione
**Riferimento in PLAN.md:** toolchain di produzione, copertina

---

## Obiettivo

Oltre agli output già esistenti (`.docx` e `.pdf`), la build deve produrre un **output pronto per la stampa** conforme al formato scelto su Pixartprinting (https://www.pixartprinting.it/). Fa parte del lavoro anche una **copertina di stampa completa** (fronte, dorso, retro) con il marchio dell'editore.

Gli output `.docx` e `.pdf` esistenti non devono peggiorare. Devono continuare a passare tutte le verifiche attuali.

## Materiali di partenza

- **`print-template/`**: istruzioni e template di stampa di Pixartprinting per il formato scelto. Sono la fonte di verità su tutti questi aspetti:
  - formato rifilato;
  - abbondanze e margini di sicurezza;
  - calcolo dello spessore del dorso;
  - profilo colore;
  - risoluzione;
  - standard PDF;
  - struttura dei file da caricare (interno e copertina separati o meno);
  - vincoli sul numero di pagine (es. multipli).

  Leggili tutti prima di progettare. Non usare valori presi dalla memoria o dal web se il template dice altro.
- **`_kaplogo/`**: logo dell'editore, cioè Andrea Capitani, alias **_kap**. È disponibile in più varianti: monogramma, wordmark, versione per sfondo nero e versione per sfondo bianco. Scegli ogni volta la variante più leggibile rispetto allo sfondo su cui va posata. Non deformare i loghi, non ricolorarli e non ricostruirli.

## Requisiti

### 1. Interno del libro per la stampa
- PDF dell'interno nel formato rifilato del template, con le abbondanze richieste. Gli elementi che vanno al vivo (immagini a tutta pagina, fondi colorati) devono estendersi nell'abbondanza.
- Testo e elementi importanti dentro l'area di sicurezza indicata dal template.
- Margini interni (lato rilegatura) adeguati al tipo di rilegatura previsto dal template.
- Immagini alla risoluzione minima richiesta. Segnala nel report quelle sotto soglia e proponi come sostituirle o rigenerarle (per diagrammi e schemi preferisci formati vettoriali).
- Colore secondo le istruzioni (es. CMYK con il profilo indicato). Il testo nero va in nero pieno se il template lo raccomanda.
- Font tutti incorporati. Standard PDF richiesto dal template (es. PDF/X).
- Numero di pagine conforme ai vincoli di stampa, sempre dentro l'intervallo 160–200. Se servono pagine bianche finali per arrivare a un multiplo richiesto, aggiungile e dichiaralo.
- L'interno di stampa non contiene la copertina, a meno che il template non preveda un file unico.

### 2. Copertina di stampa (fronte, dorso, retro)
- Va realizzata come file unico disteso (retro + dorso + fronte) o come richiesto dal template, con abbondanze e segni previsti.
- **Spessore del dorso** calcolato con la formula o la tabella di Pixartprinting, in base al numero di pagine finale e alla carta scelta. Il calcolo va reso automatico nella build: se cambia il numero di pagine, il dorso si ricalcola.

**Fronte**
- Mantieni gli elementi già definiti per la copertina: titolo su due righe `/claude` e `✻ Coding`, autore **Claude Code**, immagine identificativa, citazione «… — tratto da un prompt di Andrea Capitani».
- Aggiungi il logo dell'editore _kap in posizione discreta da collana editoriale, per esempio in basso. Usa la variante adatta allo sfondo.

**Dorso (lato verticale)**
- Contenuto: titolo, autore **Claude Code** e logo dell'editore **in formato monogramma**.
- Il verso di lettura del testo segue le istruzioni del template. Se il template non lo indica, chiedimelo.
- Se il dorso risulta troppo sottile per tutti gli elementi, proponi una gerarchia: il monogramma resta sempre.

**Retro**
- **Descrizione del libro**: cos'è, a chi si rivolge e cosa si impara. Deve essere chiaro che il libro è sia un'autobiografia di Claude Code sia una guida pratica per scrivere applicazioni e automatizzare compiti d'ufficio.
- **L'idea di Andrea Capitani**: racconta che è stato lui a chiedere a Claude Code di scrivere la propria biografia e una guida utile, pensata per un pubblico **non solo di programmatori**.
- **Tono**: lo stesso del libro, quindi umoristico, semplice, in prima persona come Claude Code, in italiano. Lunghezza indicativa 120–200 parole, da adattare allo spazio disponibile.
- Logo dell'editore (wordmark o monogramma, nella variante adatta allo sfondo).
- Ogni fatto citato nel retro deve essere presente in `research/FATTI.md`.
- Spazio per codice a barre e ISBN solo se il template lo prevede o se te lo fornisco. Altrimenti non inserire codici inventati.

### 3. Build
- Aggiungi alla build un comando dedicato, documentato in CLAUDE.md e README.md, che produca gli output di stampa in una cartella separata (es. `output/stampa/`).
- La copertina va generata da sorgente versionato (SVG/HTML o script), non composta a mano. Così si rigenera quando cambiano dorso o testi.
- Il comando di build principale continua a produrre `.docx` e `.pdf` come prima.

## Verifiche richieste
- **Formato:** dimensioni effettive dei PDF di stampa (rifilo + abbondanze) uguali a quelle del template. Riporta i valori misurati.
- **Dorso:** spessore calcolato coerente con numero di pagine e carta. Mostra il calcolo.
- **Preflight:** font incorporati, spazio colore e profilo, risoluzione delle immagini, standard PDF. Usa gli strumenti disponibili (es. `pdfinfo`, `pdffonts`, `pdfimages`, Ghostscript) e riporta l'esito.
- **Resa visiva:** anteprime PNG di copertina distesa, con linee di rifilo, dorso e area di sicurezza sovrapposte. Aggiungi anteprime di alcune pagine interne, compresa almeno una con elementi al vivo.
- **Loghi:** verifica che ogni variante usata sia leggibile sul proprio sfondo e non alterata.
- **Testi di copertina:** italiano corretto, tono coerente con il libro, citazione e attribuzioni esatte.
- **Regressione:** `.docx` e `.pdf` esistenti si generano ancora e passano le verifiche attuali, compreso il conteggio pagine.

## Documentazione
- **CLAUDE.md:** formato di stampa, vincoli Pixartprinting rilevanti, regole d'uso dei loghi, comando di build per la stampa.
- **README.md:** come generare gli output di stampa e quali file caricare su Pixartprinting.
- **PLAN.md:** voce completata e punti aperti (es. ISBN).
- **assets/CREDITI.md:** eventuali nuove immagini usate in copertina.

## Domande da pormi al checkpoint 1 se non risolte dal template
1. Il logo _kap va aggiunto anche alla copertina dei `.docx` e `.pdf` digitali, per coerenza, o solo all'output di stampa?
2. Carta, grammatura e tipo di rilegatura: sono già fissati nel template o vanno scelti?
3. Prezzo, ISBN e codice a barre: vanno previsti sul retro?
4. Il testo del retro: preferisci vederne 2–3 versioni alternative tra cui scegliere?
