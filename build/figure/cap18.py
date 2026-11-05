"""Figure del capitolo 18 «Report periodici».
IMG-18-02: il report vero di esempi/cap18 (settimana 26/10/2026), convertito con LibreOffice e ritagliato."""
from grafo import disegna

disegna("""
  rankdir=LR; nodesep=0.35; ranksep=0.45;
  dati [label="vendite.csv\ni dati della settimana", shape=note];
  report [label="report.py\ncalcola, confronta,\nsegnala", fillcolor="#FBF0EB", color="#D77757"];
  word [label="Report Word\ntabella e grafico", shape=note];
  mail [label="Email in bozza\ncon allegato", shape=note];
  tu [label="Tu\ncontrolli e spedisci", shape=box];
  quando [label="Ogni lunedì alle 8\n(/loop, Routines,\nUtilità di pianificazione)", style="rounded,dashed", fillcolor="#FFFFFF"];
  quando -> report [style=dashed];
  dati -> report -> word;
  report -> mail -> tu;
  word -> tu;
""", "assets/cap18/IMG-18-01-catena.png")
print("ok")
