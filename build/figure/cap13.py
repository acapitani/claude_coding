"""Figure del capitolo 13 «Un progetto completo».
IMG-13-02 (schermata) con: py esempi/cap13/spese/app.py (dati di esempio) + node build/figure/cap13_app.mjs, ritagliata."""
from grafo import disegna

# IMG-13-01 — com'è fatta «Spese di casa»
disegna("""
  rankdir=LR; nodesep=0.4; ranksep=0.6;
  tu [label="Tu\nnel browser", shape=box];
  app [label="app.py\nla pagina web", fillcolor="#FBF0EB", color="#D77757"];
  spese [label="spese.py\nregole e calcoli"];
  db [label="spese.db\ni dati (SQLite)", shape=cylinder];
  csv [label="CSV\nper Excel", shape=note];
  test [label="test_spese.py\ni test", style="rounded,dashed", fillcolor="#FFFFFF"];
  tu -> app [label=" localhost:8000", dir=both];
  app -> spese -> db;
  app -> csv;
  test -> spese [style=dashed, label=" controlla"];
""", "assets/cap13/IMG-13-01-architettura.png")

# IMG-13-03 — il progetto, sessione dopo sessione
disegna("""
  rankdir=TB; nodesep=0.35; ranksep=0.35;
  node [width=1.6];
  r [label="1. Requisito\n(mezza pagina)"];
  p [label="2. Piano\n(plan mode)"];
  d [label="3. Dati e regole\nspese.py + test"];
  a [label="4. La pagina\napp.py"];
  v [label="5. Prova vera\ne correzioni", fillcolor="#FBF0EB", color="#D77757"];
  g [label="6. Git\nun commit per passo"];
  doc [label="7. Documentazione\nREADME.md"];
  {rank=same; r; p; d; a}
  {rank=same; doc; g; v}
  r -> p -> d -> a;
  a -> v;
  g -> v [dir=back];
  doc -> g [dir=back];
""", "assets/cap13/IMG-13-03-percorso.png")
print("ok")
