# Comandi rapidi

Un promemoria da tenere accanto alla tastiera. Comandi, scorciatoie e opzioni sono verificati sulla versione 2.1.318; le descrizioni originali, in inglese, sono quelle che vedrai nell'elenco che compare scrivendo `/`. <!-- F-616 --> <!-- F-634 --> Se un comando non c'è o ha cambiato nome, `/help` mostra quelli disponibili nella tua versione.

## Nella sessione

| Comando | A che cosa serve | Cap. |
|---|---|---|
| `/help` | Mostra l'aiuto e i comandi disponibili | 6 |
| `/clear` | Ricomincia da capo, con il contesto vuoto | 6 |
| `/compact` | Riassume la conversazione per liberare spazio | 6 |
| `/rewind` | Torna a un punto precedente (codice, conversazione o entrambi) | 6 |
| `/resume` | Riprende una conversazione precedente | — |
| `/context` | Mostra quanto contesto è occupato | — |
| `/usage` | Costi e consumi | 6 |
| `/status` | Versione, modello, account, connessione | — |
| `/model` | Sceglie il modello | 25 |
| `/config` | Apre le impostazioni | 5 |
| `/plan` | Attiva il plan mode | 7 |
| `/init` | Prepara un primo CLAUDE.md | 8 |
| `/memory` | Apre i file di memoria e le relative impostazioni | 8 |
| `/permissions` | Mostra e modifica le regole allow e deny | 9 |
| `/diff` | Mostra le modifiche non ancora salvate in un commit | 12 |
| `/code-review` | Revisione del codice; `/security-review` per la sicurezza | 12 |
| `/install-github-app` | Collega Claude Code alle GitHub Actions | 12, 24 |
| `/loop` | Ripete una richiesta a intervalli | 18 |
| `/schedule` | Crea e gestisce le Routines | 18 |
| `/skills` | Elenca le skill disponibili | 20 |
| `/hooks` | Mostra gli hook attivi | 21 |
| `/mcp` | Stato e accesso dei server MCP | 23 |
| `/plugin` | Gestisce plugin e marketplace | 24 |
| `/release-notes` | Le novità delle ultime versioni | 25 |
| `/feedback` | Invia un commento o segnala un problema | 3 |
| `/exit` | Esce | 6 |

<!-- F-615 --> <!-- F-616 --> <!-- F-627 --> <!-- F-363 --> <!-- F-381 --> <!-- F-382 --> <!-- F-383 --> <!-- F-384 --> <!-- F-629 --> <!-- F-630 --> <!-- F-389 --> <!-- F-623 --> <!-- F-144 -->

## Tasti e simboli

| Tasto | Effetto | Cap. |
|---|---|---|
| [Esc]{.tasto} | Interrompe il lavoro in corso | 6 |
| [Esc]{.tasto} due volte | Apre il menu per tornare indietro (a casella vuota) | 6 |
| [Maiusc+Tab]{.tasto} | Cambia modalità: normale, accept edits, plan, auto | 6, 9 |
| [Maiusc+Invio]{.tasto} | Va a capo senza inviare | 7 |
| [Ctrl+V]{.tasto} | Incolla un'immagine | 7 |
| `?` | Mostra le scorciatoie | 6 |
| `/` | Elenco dei comandi | 6 |
| `@` | Indica un file o un sottoagente | 7, 22 |

<!-- F-611 --> <!-- F-612 --> <!-- F-614 --> <!-- F-620 --> <!-- F-625 --> <!-- F-628 --> <!-- F-398 -->

## Dal terminale

| Comando | A che cosa serve | Cap. |
|---|---|---|
| `claude` | Avvia una sessione nella cartella corrente | 5 |
| `claude -c` | Riprende l'ultima conversazione | — |
| `claude -r` | Sceglie una conversazione da riprendere | — |
| `claude --version` | Mostra la versione | 3 |
| `claude update` | Cerca e installa gli aggiornamenti | 5 |
| `claude doctor` | Controlla l'installazione | 5 |
| `claude mcp add` | Collega un server MCP (`list`, `remove`) | 23 |
| `claude plugin install` | Installa un plugin (`marketplace add`, `validate`) | 24 |

<!-- F-141 --> <!-- F-634 --> <!-- F-353 --> <!-- F-336 -->

## Per gli script

| Opzione | A che cosa serve | Cap. |
|---|---|---|
| `-p "richiesta"` | Una risposta senza interfaccia, poi esce | 24 |
| `--allowedTools` | Gli unici strumenti permessi | 24 |
| `--output-format json` | Risposta in JSON, con costo e sessione | 24 |
| `--json-schema` | Risposta in un formato fisso | 24 |
| `--max-budget-usd` | Tetto di spesa in dollari | 24 |
| `--model` | Sceglie il modello (`opus`, `sonnet`, `fable`) | 25 |

<!-- F-631 --> <!-- F-337 --> <!-- F-633 -->

## File e cartelle

| Dove | Che cosa contiene | Cap. |
|---|---|---|
| `CLAUDE.md` | Le istruzioni del progetto | 8 |
| `.claude/settings.json` | Permessi e hook del progetto | 9, 21 |
| `.claude/skills/` | Le skill del progetto (anche in `~/.claude/skills/`) | 20 |
| `.claude/commands/` | I comandi personalizzati | 20 |
| `.claude/agents/` | I sottoagenti | 22 |
| `.mcp.json` | I server MCP condivisi del progetto | 23 |
