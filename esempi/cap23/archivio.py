"""Server MCP «archivio»: risponde a domande sui clienti e sulle fatture aperte.

Legge archivio.xlsx e non modifica niente. Si collega a Claude Code con:
    claude mcp add archivio -- py archivio.py
"""
from pathlib import Path
from openpyxl import load_workbook
from mcp.server.mcpserver import MCPServer   # SDK mcp 2.x

FILE = Path(__file__).parent / "archivio.xlsx"
server = MCPServer("archivio")


def righe():
    foglio = load_workbook(FILE, data_only=True).active
    intestazioni = [c.value for c in foglio[1]]
    for valori in foglio.iter_rows(min_row=2, values_only=True):
        r = dict(zip(intestazioni, valori))
        if r.get("Scadenza"):
            r["Scadenza"] = r["Scadenza"].date().isoformat()
        yield r


@server.tool()
def cerca_cliente(testo: str) -> list[dict]:
    """Cerca i clienti il cui nome, cognome o città contiene il testo."""
    t = testo.lower()
    return [r for r in righe()
            if t in f"{r['Nome']} {r['Cognome']} {r['Città']}".lower()]


@server.tool()
def fatture_scadute(al_giorno: str) -> dict:
    """Fatture con scadenza precedente alla data (AAAA-MM-GG) e totale."""
    scadute = [r for r in righe()
               if r["Importo"] and r["Scadenza"] and r["Scadenza"] < al_giorno]
    totale = round(sum(r["Importo"] for r in scadute), 2)
    return {"numero": len(scadute), "totale_euro": totale, "fatture": scadute}


if __name__ == "__main__":
    server.run()          # comunica con Claude Code attraverso stdin/stdout
