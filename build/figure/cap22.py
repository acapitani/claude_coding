"""Figura del capitolo 22: come è andata la prova reale (research/note/agenti-cap22.jsonl)."""
from grafo import disegna

disegna("""
  rankdir=TB; nodesep=0.25; ranksep=0.45;
  tu [label="«Prima di spedire, fai rileggere\nle 49 lettere»", shape=box];
  capo [label="Agente principale\ndivide il lavoro, poi ricontrolla", fillcolor="#FBF0EB", color="#D77757"];
  r1 [label="revisore-lettere\nlettere 01–13"];
  r2 [label="revisore-lettere\nlettere 14–27"];
  r3 [label="revisore-lettere\nlettere 28–39"];
  r4 [label="revisore-lettere\nlettere 40–50"];
  esito [label="Un solo elenco:\n6 lettere da correggere, 3 cose da verificare", shape=note];
  tu -> capo;
  capo -> {r1 r2 r3 r4} [label=""];
  {r1 r2 r3 r4} -> esito [style=dashed, color="#8C867D"];
  {rank=same; r1; r2; r3; r4}
""", "assets/cap22/IMG-22-01-revisori.png")
print("ok")
