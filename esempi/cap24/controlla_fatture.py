"""Controllo notturno delle fatture con Claude Code in modalità non interattiva.

Uso: py controlla_fatture.py [cartella]   (predefinita: fatture)
Per ogni PDF chiede a Claude Code un esito in un formato fisso (JSON Schema)
e scrive controllo.csv. Claude può solo leggere: niente modifiche, niente rete.
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

SCHEMA = {
    "type": "object",
    "properties": {
        "fornitore": {"type": "string"},
        "totale_euro": {"type": "number"},
        "corretta": {"type": "boolean"},
        "nota": {"type": "string"},
    },
    "required": ["fornitore", "totale_euro", "corretta", "nota"],
}

cartella = Path(sys.argv[1] if len(sys.argv) > 1 else "fatture")
righe = []
for pdf in sorted(cartella.glob("*.pdf")):
    esito = subprocess.run(
        ["claude", "-p", f"Controlla la fattura {pdf.as_posix()}.",
         "--output-format", "json", "--json-schema", json.dumps(SCHEMA),
         "--allowedTools", "Read,Skill", "--max-budget-usd", "0.50"],
        capture_output=True, text=True, encoding="utf-8")
    try:
        risposta = json.loads(esito.stdout)
        dati = risposta["structured_output"]
        costo = risposta.get("total_cost_usd", 0)
    except (json.JSONDecodeError, KeyError, TypeError):
        dati = {"fornitore": "?", "totale_euro": "", "corretta": "",
                "nota": "nessuna risposta valida: controllare a mano"}
        costo = 0
    righe.append({"file": pdf.name, **dati, "costo_usd": round(costo, 3)})
    print(pdf.name, "OK" if dati.get("corretta") else "DA CONTROLLARE")

with open("controllo.csv", "w", newline="", encoding="utf-8-sig") as f:
    scrittore = csv.DictWriter(f, fieldnames=righe[0].keys(), delimiter=";")
    scrittore.writeheader()
    scrittore.writerows(righe)
print(f"{len(righe)} fatture controllate: vedi controllo.csv")
