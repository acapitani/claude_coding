# Lo spinner di Claude Code — verifica S1 (2026-11-04)

**Metodo.** Ispezione dell'eseguibile ufficiale installato su questa macchina
(`claude.exe`, `claude --version` → **2.1.318**, installer nativo), cercando le stringhe dello
spinner e del tema. È il pacchetto distribuito da Anthropic: **non** si usa la copia trapelata a marzo 2026.
Nel libro si descrivono i fatti osservati; **non si riproduce codice**.

## Glifi (versione 2.1.318)
| Terminale | Sequenza | Note |
|---|---|---|
| Tutti tranne Ghostty (Windows, macOS, Linux) | `· ✢ * ✶ ✻ ✽` | percorsa in avanti e poi all'indietro (6 + 6 fotogrammi) |
| Ghostty (`TERM=xterm-ghostty`) | `· ✢ ✳ ✶ ✻ ✻` | il ✽ è sostituito, probabilmente per un problema di resa |
| (definita ma non selezionata in 2.1.318) | `· ✢ ✳ ✶ ✻ ✽` | era la variante macOS nella versione 2.1.88 (fonte: analisi pubbliche del sorgente trapelato) |

Codici: · U+00B7, ✢ U+2722, ✳ U+2733, ✶ U+2736, **✻ U+273B** (TEARDROP-SPOKED ASTERISK), ✽ U+273D.
**✻ è presente in tutte le varianti** → glifo del titolo confermato.

## Colori (tema)
- `claude`: **rgb(215,119,87) = #D77757**, il colore "Claude" dei temi (testo dello spinner, accenti).
- `claudeShimmer` (alone, tema chiaro): rgb(245,149,117) = #F59575. Il valore rgb(235,159,127) compare anch'esso nel binario (tema scuro secondo la 2.1.88).
- `clawd_body`: **rgb(215,119,87)**. Il nome della chiave conferma che la mascotte si chiama "Clawd" anche nel codice ufficiale.
- `#D97757` compare solo in un'animazione SVG (contesto non chiaro): resta il "colore di marca" citato online, non confermato da una guida ufficiale.
→ **Colore di accento del libro: #D77757** (confermato).

## Verbi
- Elenco predefinito: **187 verbi**, da "Accomplishing" a "Zigzagging", tutti in inglese
  (es. Clauding, Combobulating, Flibbertigibbeting). Lista completa: `spinner-verbi-2.1.318.txt`.
- L'impostazione `spinnerVerbs` permette di aggiungere verbi o di sostituire l'elenco
  (issue https://github.com/anthropics/claude-code/issues/21599, introdotta in 2.1.23).
- Il numero cambia tra versioni: nel libro scrivere "quasi duecento" oppure "187 nella versione 2.1.318".

## Storia (dal pacchetto npm 0.2.9 del 24/02/2025, verifica dell'agente di ricerca S1)
- Sequenze al lancio: macOS `· ✢ ✳ ∗ ✻ ✽`, altri sistemi `· ✢ * ∗ ✻ ✽` (∗ = U+2217, poi sostituito da ✶).
- **Il ✻ c'è dal primo giorno.**
- Verbi al lancio: 56 (da "Accomplishing" a "Working"); "Flibbertigibbeting" è arrivato dopo.
