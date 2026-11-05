# ufficio-anna

Gli attrezzi dello studio di Anna, in un solo pacchetto per Claude Code:

- **controllo-fattura** (skill): verifica che imponibile, IVA al 22% e totale di una fattura tornino; si attiva da sola quando chiedi di controllare una fattura, oppure con `/ufficio-anna:controllo-fattura`.
- **revisore-lettere** (sottoagente): rilegge le lettere prima della spedizione, in sola lettura, con un modello piccolo.
- **serratura delle fatture** (hook): impedisce di modificare i file nella cartella `fatture`.

Richiede Python (comando `py`) per l'hook. Installazione: `claude plugin marketplace add <cartella>` e poi `claude plugin install ufficio-anna@studio`.
