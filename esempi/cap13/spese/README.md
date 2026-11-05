# Spese di casa

Una piccola applicazione per annotare le spese di casa e vedere, mese per mese,
dove finiscono i soldi. Funziona sul tuo computer: i dati restano in un file,
`spese.db`, nella stessa cartella.

## Che cosa serve

Solo Python 3 (da https://www.python.org). Nessun altro programma da installare.

## Come si avvia

1. Apri il terminale in questa cartella.
2. Scrivi `py app.py` (su macOS e Linux: `python3 app.py`).
3. Apri il browser all'indirizzo http://localhost:8000
4. Per fermare l'applicazione, torna al terminale e premi Ctrl+C.

Vuoi provarla con dei dati inventati? Prima del passo 2 scrivi `py dati_esempio.py`.

## Come si usa

- **Aggiungere una spesa**: data, categoria, descrizione e importo (anche con la
  virgola: `12,50`), poi *Aggiungi*.
- **Cambiare mese**: scegli il mese e premi *Mostra*.
- **Eliminare una spesa**: la × in fondo alla riga.
- **Portare i dati in Excel**: *Scarica CSV* (separatore punto e virgola).

## Copie di sicurezza

Tutti i dati sono nel file `spese.db`: per farne una copia basta copiare quel file.

## Per chi vuole modificarla

- `spese.py` — i dati: salvataggio, totali, formato degli importi.
- `app.py` — la pagina web.
- `test_spese.py` — i test: `py -m unittest -v` (devono essere tutti OK).
