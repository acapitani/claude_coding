"""Figure del capitolo 10 «Dal requisito al prototipo».
IMG-10-02 (la mini-app) si genera con: node build/figure/cap10_app.mjs (che prova anche le conversioni)."""
from grafo import disegna

disegna("""
  rankdir=TB; nodesep=0.6; ranksep=0.5;
  idea [label="Idea\n«mi servirebbe…»"];
  req [label="Requisito\nmezza pagina"];
  piano [label="Piano\n(plan mode)"];
  proto [label="Prototipo\nla versione minima", fillcolor="#FBF0EB", color="#D77757"];
  prova [label="Prova\nusalo davvero"];
  ok [label="Strumento\nche si usa"];
  {rank=same; idea -> req -> piano;}
  {rank=same; ok -> prova -> proto [dir=back];}
  piano -> proto;
  prova:s -> proto:s [label="un passo\nalla volta", color="#D77757", fontcolor="#D77757", constraint=false];
""", "assets/cap10/IMG-10-01-percorso.png")
print("ok")
