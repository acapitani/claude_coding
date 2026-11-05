# Installazione

Il giorno del mio debutto, per installarmi bisognava prima installare un'altra cosa, Node.js, almeno alla versione 18, e poi digitare un comando npm che a chi non programma sembrava scritto in codice segreto. <!-- F-203 --> Se potessi ricordarlo, ricorderei soprattutto le persone che si fermavano al primo passo. Oggi le cose sono molto più semplici: una riga, qualche secondo di attesa, e ci siamo. Questo capitolo ti accompagna in quei secondi, e anche nei minuti successivi, se qualcosa dovesse andare storto.

## Che cosa serve

Prima di cominciare controlla tre cose.

**Il computer.** Mi bastano Windows 10 (versione 1809 o successiva) o Windows 11, macOS 13 o successivo, oppure una distribuzione Linux recente come Ubuntu 20.04 o Debian 10, con almeno 4 GB di memoria e una connessione a internet. Non servono privilegi di amministratore. <!-- F-340 --> Windows a 32 bit, invece, non è supportato. <!-- F-341 --> Se non sai quale versione di Windows hai, premi [Win+R]{.tasto}, scrivi `winver` e premi Invio: una finestra te lo dice.

**L'account.** Per usarmi serve un abbonamento a Claude (Pro, Max, Ultra, Team o Enterprise) oppure un account della Console di Anthropic, quella per gli sviluppatori, con credito prepagato. Il piano gratuito di claude.ai non mi include. Le aziende possono anche passare da Amazon Bedrock, Google Cloud o Microsoft Foundry. <!-- F-344 --> Se lavori in un'azienda, chiedi prima all'ufficio informatico: è probabile che abbiano già scelto per te.

**Il paese.** Funziono nei paesi supportati da Anthropic: l'elenco aggiornato è sul suo sito. <!-- F-340 -->

## Installare su Windows

Apri [PowerShell]{xe="PowerShell"}: premi il tasto Windows, scrivi «PowerShell» e premi Invio. Poi copia questa riga e premi Invio:

```terminale
PS C:\Users\anna> irm https://claude.ai/install.ps1 | iex
```

In parole povere: `irm` scarica lo script d'installazione dal sito ufficiale e `iex` lo esegue. Aspetta che abbia finito. <!-- F-342 --> Ora **chiudi e riapri il terminale**: una finestra già aperta non si accorge dei programmi appena installati. <!-- F-348 --> La figura 5.1 mostra l'intero percorso.

![Installazione su Windows con PowerShell, dal download al primo avvio (ricostruzione stilizzata)](assets/cap05/IMG-05-01-windows.png){larghezza=12}

Se preferisci il vecchio Prompt dei comandi (CMD), i comandi sono tre:

```terminale
C:\> curl -fsSL https://claude.ai/install.cmd -o install.cmd
C:\> install.cmd
C:\> del install.cmd
```

Chi usa [WinGet]{xe="WinGet"}, il gestore di programmi di Windows, può scrivere invece `winget install Anthropic.ClaudeCode`. <!-- F-342 --> Non serve installare altro: Git for Windows è facoltativo, e senza di lui uso PowerShell per eseguire i comandi. Se usi già WSL, il Linux integrato in Windows, puoi installarmi anche lì, con il comando per Linux. <!-- F-341 -->

::: attenzione Solo dal sito ufficiale
Il comando d'installazione scarica un programma da internet e lo esegue subito. È normale, ed è il metodo raccomandato, ma solo se l'indirizzo è esattamente `https://claude.ai/…`. Diffida di guide, video o messaggi che ti propongono indirizzi diversi o «versioni speciali». Nel dubbio, copia i comandi dalla documentazione ufficiale.
:::

## Installare su macOS e Linux

Apri il Terminale (su macOS: [Cmd+Spazio]{.tasto}, poi scrivi «Terminale») e scrivi:

```terminale
$ curl -fsSL https://claude.ai/install.sh | bash
```

Su macOS, chi usa Homebrew può scrivere `brew install --cask claude-code`; su Linux esistono anche i pacchetti per apt, dnf e apk. <!-- F-342 --> Esiste infine l'installazione con npm, che la documentazione mette tra le opzioni avanzate: richiede Node.js 22 o successivo, e va fatta senza `sudo`. <!-- F-343 --> Se non sai che cosa siano npm e sudo, sei la persona giusta per ignorare questo paragrafo.

## Il primo avvio

::: consiglio Prepara una cartella di prova
Prima di avviarmi per la prima volta, crea una cartella apposta, per esempio `Documenti\prove`, e copiaci dentro qualche file su cui fare esperimenti: un foglio [Excel]{xe="Excel"}, due o tre documenti, qualche foto. Nel prossimo capitolo la useremo per la prima sessione. Lavorare su copie, all'inizio, toglie ogni ansia: se qualcosa va storto, si ricomincia da capo.
:::

Entra nella cartella in cui vuoi lavorare, come vedremo meglio nel prossimo capitolo, e scrivi `claude`. La prima volta si apre il browser e ti chiedo di accedere con il tuo account; poi torni al terminale e sei pronto. <!-- F-345 --> Se in futuro dovrai cambiare account, durante una sessione scrivi `/login`. Con un account Console, al primo accesso viene creato uno spazio di lavoro chiamato «Claude Code» per tenere traccia dei costi. <!-- F-345 -->

## Controllare e aggiornare

Due comandi ti dicono se è tutto a posto:

```terminale
$ claude --version
2.1.318 (Claude Code)
$ claude doctor
```

Il primo mostra la versione; il secondo fa una diagnosi in sola lettura dell'installazione e delle impostazioni, e se trova qualcosa che non va ti suggerisce come rimediare. <!-- F-346 -->

Degli aggiornamenti non devi preoccuparti: con l'installazione standard mi aggiorno da solo, in sottofondo, e la nuova versione entra in funzione al riavvio successivo. Se mi hai installato con WinGet o Homebrew, invece, gli aggiornamenti si fanno a mano, per esempio con `winget upgrade Anthropic.ClaudeCode`. Il canale `stable`, di cui abbiamo parlato nel capitolo 4, riceve le novità con circa una settimana di ritardo e salta le versioni con problemi gravi; si sceglie anche dal comando `/config`. <!-- F-347 -->

## Quando qualcosa va storto

La maggior parte dei problemi d'installazione ha una causa banale. Ecco i più comuni. <!-- F-348 --> <!-- F-349 -->

| Messaggio | Che cosa significa | Che cosa fare |
|---|---|---|
| `'claude' is not recognized`, `command not found` | Il terminale non sa dove mi trovo | Chiudi e riapri il terminale; se non basta, vedi sotto |
| `'irm' is not recognized` | Hai usato il comando di PowerShell nel CMD | Usa i comandi per CMD, o apri PowerShell |
| `The token '&&' is not a valid…` | Il contrario: comando per CMD in PowerShell | Usa il comando per PowerShell |
| Errore 403 o una pagina HTML | Il sito non ha risposto come doveva | Riprova tra qualche minuto, o usa WinGet o Homebrew |
| `App unavailable in region` | Il paese non è supportato | Non c'è rimedio tecnico |

Se dopo aver riaperto il terminale `claude` non viene ancora trovato, bisogna dire a Windows dove cercarmi, aggiungendo la mia cartella al [PATH]{xe="PATH"}, l'elenco delle cartelle in cui il sistema cerca i programmi. In PowerShell, una volta sola: <!-- F-348 -->

```terminale
PS> $p = [Environment]::GetEnvironmentVariable('PATH', 'User')
PS> $p = "$p;$env:USERPROFILE\.local\bin"
PS> [Environment]::SetEnvironmentVariable('PATH', $p, 'User')
```

Su macOS la riga equivalente è `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`. Le tre righe per PowerShell, tradotte: la prima legge l'elenco attuale, la seconda ci aggiunge in fondo la cartella in cui mi sono installato, la terza lo salva. Niente viene cancellato. Poi, di nuovo, chiudi e riapri il terminale. E se qualcosa continua a non funzionare, ricordati di `claude doctor`.

## Non solo terminale

Il terminale è casa mia, e questo libro parte da lì. Ma non è l'unico posto in cui puoi trovarmi. Esisto come app desktop per Windows, macOS e Linux, dentro gli editor di codice VS Code e JetBrains, sul web all'indirizzo claude.ai/code, in Slack e nelle procedure automatiche di GitHub e GitLab. <!-- F-351 --> Le idee di questo libro ti serviranno anche lì, anche se i pulsanti saranno diversi. Un'avvertenza per chi ha installato solo l'estensione di VS Code: si porta dietro una sua copia di me, ad uso del suo pannello, e non rende disponibile il comando `claude` nel terminale. Per seguire il libro serve l'installazione descritta in questo capitolo. <!-- F-351 -->

![Dove posso usarmi: il terminale è il punto di partenza di questo libro](assets/cap05/IMG-05-02-dove.png){larghezza=10}

::: nota Disinstallarmi
Spero che non succeda, ma è giusto saperlo. Con WinGet basta `winget uninstall Anthropic.ClaudeCode`. Con l'installazione standard si cancellano due elementi nella cartella del tuo utente: il file `.local\bin\claude.exe` e la cartella `.local\share\claude` (su macOS e Linux: `~/.local/bin/claude` e `~/.local/share/claude`). Le impostazioni restano nella cartella `.claude` e nel file `.claude.json`: cancellali solo se vuoi dimenticarmi del tutto. <!-- F-350 -->
:::

## In breve

- Servono Windows 10 1809+, macOS 13+ o un Linux recente, 4 GB di RAM e un abbonamento a pagamento o un account Console: il piano gratuito non basta.
- **Windows:** `irm https://claude.ai/install.ps1 | iex` in PowerShell. **macOS e Linux:** `curl -fsSL https://claude.ai/install.sh | bash`.
- Dopo l'installazione **chiudi e riapri il terminale**, poi controlla con `claude --version`.
- Al primo avvio accedi dal browser; `/login` cambia account; `claude doctor` diagnostica i problemi.
- Mi aggiorno da solo; con WinGet o Homebrew gli aggiornamenti sono manuali.
