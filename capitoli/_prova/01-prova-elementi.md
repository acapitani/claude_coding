# Tutti gli elementi in un capitolo

<!-- F-101 -->
Questo capitolo di prova contiene **ogni elemento** previsto dalla toolchain: testo *corsivo*, **grassetto**, `codice in linea`, il glifo ✻ in mezzo a una frase, virgolette "dritte" che devono diventare caporali, puntini... e trattini -- tutto in italiano. Il tasto [Esc]{.tasto} interrompe, il [terminale]{xe="terminale"} attende, e lo [spinner]{xe="spinner"} gira: `· ✢ * ✶ ✻ ✽`.

## Elenchi

Un elenco puntato:

- primo punto, con un [prompt]{xe="prompt"};
- secondo punto, con un sottoelenco:
  - sottopunto A;
  - sottopunto B;
- terzo punto.

Due elenchi numerati, per verificare che la numerazione riparta:

1. installa;
2. avvia;
3. chiedi.

Secondo elenco:

1. leggi;
2. rileggi.

## Box

::: nota
Una nota semplice, con `codice` e un secondo paragrafo.

Il secondo paragrafo della nota.
:::

::: consiglio Scrivi richieste precise
Dì che cosa vuoi, perché lo vuoi e come capirai che è fatto. Il [CLAUDE.md]{xe="CLAUDE.md"} aiuta.
:::

::: attenzione
Non incollare password o dati personali nelle richieste.
:::

## Codice e terminale

Un blocco di codice Python:

```python
# Rinomina le foto aggiungendo la data (commento in italiano)
from pathlib import Path

for foto in Path("foto").glob("*.jpg"):
    nuovo = foto.with_name(f"2026-11-05_{foto.name}")
    foto.rename(nuovo)  # attenzione: nessuna conferma!
```

Una finta sessione di terminale:

```terminale
$ claude
✻ Combobulating… (esc per interrompere)
> riordina la cartella Download per tipo di file
● Ho trovato 214 file. Creo le cartelle Documenti, Immagini, Archivi.
# riga di commento nel terminale
PS C:\Users\anna> claude --version
2.1.318 (Claude Code)
```

## Figure

![Il ciclo dell'agente: leggo, penso, agisco, verifico](assets/_prova/IMG-00-01-ciclo.png){larghezza=13}

Una foto storica alta, che deve essere ridotta in altezza:

![Ada Lovelace in un ritratto attribuito ad Alfred Edward Chalon (circa 1840)](assets/cap01/IMG-01-01-ada-lovelace.jpg){larghezza=8 altezza_max=9}

![Una figura che non esiste ancora](assets/_prova/non-esiste.png)

## Tabelle

| Versione | Data | Novità |
|---|:---:|---|
| 0.2.9 | 24/02/2025 | Research preview |
| 1.0.0 | 22/05/2025 | Disponibilità generale |
| 2.0.0 | 29/09/2025 | Checkpoint e `/rewind` |

## Citazioni e separatori

> «Claude Code is not a product as much as it's a Unix utility.»
> — Boris Cherny

---

### Un titolo di terzo livello

Non entra nell'indice generale, ma resta visibile nel testo.

## In breve

- Ogni elemento ha uno stile.
- Ogni figura ha una didascalia.
- Ogni fatto ha una fonte.
