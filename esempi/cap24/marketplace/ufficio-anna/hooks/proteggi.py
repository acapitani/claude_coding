"""Hook PreToolUse: nessuna modifica ai file della cartella «fatture»."""
import json
import sys
from pathlib import PurePath

sys.stderr.reconfigure(encoding="utf-8")   # su Windows, altrimenti «è» arriva illeggibile

try:
    dati = json.load(sys.stdin)
    percorso = dati.get("tool_input", {}).get("file_path", "")
except Exception as errore:
    # Un hook che si rompe con il codice 1 NON blocca: meglio bloccare e dirlo.
    print(f"Hook di protezione non funzionante ({errore}): blocco per prudenza.", file=sys.stderr)
    sys.exit(2)

if "fatture" in PurePath(percorso.replace("\\", "/")).parts:
    print(f"Bloccato: {percorso} è nella cartella «fatture», che non si modifica. "
          "Lavora su una copia in «lavoro».", file=sys.stderr)
    sys.exit(2)      # 2 = blocca l'azione; il messaggio arriva a Claude
sys.exit(0)          # 0 = nessuna obiezione
