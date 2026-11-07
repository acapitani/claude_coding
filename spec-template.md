# Implementazione specifica — Libro "/claude ✻ Coding"

**Nome feature:** <nome-kebab-case>  (es. `cap-07-claude-md`, `copertina`, `illustrazioni-parte-2`)
**Tipo di lavoro:** <capitolo | copertina | illustrazioni | ricerca | toolchain | revisione | impaginazione>
**Riferimento in PLAN.md:** <parte / capitolo / sezione>
**Budget pagine:** <pagine previste per questo lavoro, da PLAN.md>
**Branch destinazione:** main
**Specifica:**
<testo_specifica>

---

Segui queste fasi in ordine. Non saltare i checkpoint.
Le fasi 1 e 2 si svolgono in plan mode: solo lettura, esplorazione e ricerca
sul web, nessuna modifica a file o allo stato del repo.

## Fase 1 — Contesto (plan mode)
Leggi CLAUDE.md, README.md e PLAN.md e i piani esistenti in _plans/.
Leggi anche:
- `research/FATTI.md` (registro dei fatti verificati con fonte);
- `assets/CREDITI.md` (registro delle immagini e delle licenze);
- i capitoli già scritti in `capitoli/`, almeno quelli adiacenti e quelli
  richiamati dalla specifica, per tono, voce narrante, rimandi e terminologia;
- lo script di build e gli stili del `.docx`, se il lavoro li tocca.
Rileva lo stato attuale: pagine totali dell'ultima build, pagine per capitolo,
illustrazioni già presenti.

## Fase 2 — Analisi e piano (plan mode)
Produci un'analisi che contenga:
- obiettivo della specifica in 2-3 righe
- ambiguità o domande aperte (se ce ne sono di bloccanti, fermati e chiedi)
- capitoli, file, asset e stili impattati
- contenuto proposto: scaletta delle sezioni, aneddoti autobiografici,
  esempi pratici, box (Nota / Consiglio / Attenzione), riepilogo finale
- fatti necessari: quali sono già in `research/FATTI.md` e quali vanno
  cercati e verificati (con fonti candidate)
- illustrazioni previste: tipo, fonte con licenza o metodo di generazione
- stima pagine e impatto sul totale (deve restare tra 160 e 200)
- strategia di verifica (vedi fase 5)
- impatti su CLAUDE.md, README.md, PLAN.md, FATTI.md, CREDITI.md
- rischi (fatti non verificabili, licenze dubbie, sforamento pagine,
  incoerenze con altri capitoli)

Se il lavoro non è banale (un capitolo, la copertina, più illustrazioni,
modifiche alla toolchain), prepara anche il piano dettagliato con questa
struttura: obiettivo, contesto, passi numerati con criterio di completamento,
verifiche previste, documentazione da aggiornare, stato. Presentamelo qui:
lo salverai in `_plans/<nome>.md` nella fase 3, dopo la mia approvazione.

**CHECKPOINT 1:** presenta analisi e piano e attendi la mia approvazione.
Procedi con la fase 3 solo dopo che sono uscito dal plan mode.

## Fase 3 — Branch e piano
- Verifica che il working tree sia pulito; se non lo è, fermati e avvisami.
- Aggiorna il branch destinazione e crea `fb/<nome>` a partire da esso.
- Se è previsto il piano dettagliato, salvalo in `_plans/<nome>.md`,
  incorporando le eventuali modifiche concordate al checkpoint 1,
  e committalo come primo commit del branch.

## Fase 4 — Scrittura e produzione
- Scrivi in italiano, in prima persona come Claude Code, con stile
  scorrevole e ironico ma preciso, seguendo le regole di CLAUDE.md.
- Usa solo fatti presenti in `research/FATTI.md`; ogni fatto nuovo va
  prima aggiunto al registro con fonte, data di accesso e affidabilità.
  La licenza narrativa (pensieri, emozioni "da software") deve essere
  riconoscibile come tale.
- Verifica comandi, opzioni e comportamenti di Claude Code citati nella
  guida sulla documentazione ufficiale aggiornata; dove possibile provali.
- Usa solo immagini con licenza verificata e registrata in
  `assets/CREDITI.md`, oppure generate (diagrammi, schemi, finte schermate
  di terminale) con il sorgente salvato in `assets/`.
- Ogni illustrazione ha didascalia numerata ed è richiamata nel testo.
- Commit piccoli e atomici con messaggi chiari (es. una sezione, un gruppo
  di illustrazioni, una correzione di stile).
- Se scopri che il piano va cambiato in modo sostanziale (struttura del
  capitolo, budget pagine, fatti chiave non verificabili), fermati e
  chiedimelo.
- Aggiorna lo stato in `_plans/<nome>.md` man mano.

## Fase 5 — Verifiche
Esegui tutti i controlli; devono passare tutti:
- **Build:** lo script di build genera il `.docx` senza errori.
- **Pagine:** converti in PDF (LibreOffice headless) e conta le pagine.
  Il totale deve restare tra 160 e 200; il capitolo deve rispettare
  il budget con tolleranza concordata in PLAN.md. Riporta i numeri.
- **Resa visiva:** renderizza in PNG le pagine toccate e controllale:
  stili, box, blocchi di codice, immagini non tagliate, didascalie,
  intestazioni, numerazione, glifo ✻ visibile.
- **Fatti:** ogni affermazione storica o numerica nel testo ha una voce
  in `research/FATTI.md`.
- **Immagini:** ogni immagine usata ha una voce in `assets/CREDITI.md`
  con licenza compatibile.
- **Lingua e stile:** testo interamente in italiano, ortografia e
  punteggiatura corrette, terminologia coerente con il glossario,
  voce narrante coerente con i capitoli precedenti.
- **Rimandi:** riferimenti a capitoli, figure e appendici corretti;
  indice generale aggiornato.
- **Esempi:** codice e comandi di esempio sintatticamente corretti e,
  dove possibile, eseguiti con successo.

## Fase 6 — Documentazione
- **CLAUDE.md:** aggiorna se cambiano regole di stile, struttura delle
  cartelle, comandi di build e verifica o vincoli del libro.
- **README.md:** aggiorna se cambiano modalità di build, prerequisiti
  o organizzazione del progetto.
- **PLAN.md:** aggiorna la tabella di avanzamento (lavoro completato,
  pagine effettive vs budget, nuove voci emerse).
- **research/FATTI.md** e **assets/CREDITI.md:** aggiornati con tutto
  ciò che è stato introdotto.
- Glossario e appendici: aggiorna se il lavoro introduce nuovi termini
  o comandi.
- Non aggiornare un file se non serve: dichiaralo esplicitamente nel report.

## Fase 7 — Verifica e merge
Presentami un report con: cosa è stato fatto, file modificati, pagine del
lavoro e totale del libro, fatti e immagini aggiunti, esito delle verifiche,
documentazione aggiornata, eventuali scostamenti dal piano e punti aperti.
Allega o indica il PDF e le anteprime PNG delle pagine toccate.

**CHECKPOINT 2:** attendi il mio OK, poi:
- aggiorna il branch destinazione e fai merge di `fb/<nome>` con `--no-ff`
- se ci sono conflitti, fermati e mostrameli
- riesegui build e verifiche (in particolare il conteggio pagine) dopo il merge
- non fare push e non cancellare il feature branch salvo mia richiesta
