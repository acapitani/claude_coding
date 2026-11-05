"""Diagrammi Graphviz con lo stile del libro → PNG a 300 dpi.

Uso da script:   from grafo import disegna;  disegna(SORGENTE_DOT, "assets/cap02/IMG-02-02-ciclo.png")
Uso da riga di comando:   py build/figure/grafo.py sorgente.dot assets/capNN/IMG-....png
Nel sorgente basta scrivere i nodi e gli archi: lo stile (font, colori) viene aggiunto qui.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import comune  # noqa: E402

STILE = """
  graph [fontname="Calibri", fontsize=12, bgcolor="white", pad=0.25, nodesep=0.45, ranksep=0.5, dpi=300];
  node  [fontname="Calibri", fontsize=12, shape=box, style="rounded,filled", fillcolor="#F4F1EA",
         color="#1F1E1D", penwidth=1.2, margin="0.18,0.10"];
  edge  [fontname="Calibri", fontsize=10, color="#6B6660", penwidth=1.2, arrowsize=0.8];
"""


def disegna(sorgente: str, destinazione: str | Path) -> Path:
    """`sorgente` è il corpo di un digraph (senza 'digraph {' … '}'), oppure un digraph completo."""
    s = sorgente.strip()
    if not s.startswith(("digraph", "graph")):
        s = "digraph G {\n" + STILE + s + "\n}"
    else:
        s = s.replace("{", "{\n" + STILE, 1)
    dest = Path(destinazione)
    if not dest.is_absolute():
        dest = comune.RADICE / dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run([str(comune.DOT), "-Tpng", "-o", str(dest)], input=s.encode("utf-8"), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace"))
    return dest


if __name__ == "__main__":
    comune.utf8_console()
    print(disegna(Path(sys.argv[1]).read_text(encoding="utf-8"), sys.argv[2]))
