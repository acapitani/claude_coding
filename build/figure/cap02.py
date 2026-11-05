"""Figure del capitolo 2 «La nascita»."""
from grafo import disegna
from terminale import finto_terminale

# IMG-02-01 — il prototipo e la musica (ricostruzione di fantasia: i testi originali non sono documentati)
finto_terminale([
    '<span class="t">&gt;</span> che musica sto ascoltando?',
    '',
    '<span class="c">●</span> Non posso sentirla, ma posso guardare lo schermo.',
    '<span class="v">●</span> <span class="b">Screenshot</span>(lettore musicale)',
    '  <span class="t">⎿  immagine acquisita</span>',
    '',
    '<span class="c">●</span> Stai ascoltando <span class="a">♪ …</span>',
    '  <span class="t">(il titolo, purtroppo, la storia non lo ricorda)</span>',
], "assets/cap02/IMG-02-01-musica.png", titolo="settembre 2024 — Claude CLI", larghezza_cm=11)

# IMG-02-02 — il ciclo dell'agente
disegna("""
  rankdir=TB; nodesep=1.2; ranksep=0.7;
  guardo [label="Guardo\n(file, errori)"];
  decido [label="Decido\n(un piano)"];
  agisco [label="Agisco\n(modifico, eseguo)", fillcolor="#FBF0EB", color="#D77757"];
  verifico [label="Verifico\n(risultato, test)"];
  {rank=same; guardo -> decido;}
  {rank=same; verifico -> agisco [dir=back];}
  decido -> agisco;
  guardo -> verifico [dir=back, xlabel="se non va  ", color="#D77757", fontcolor="#D77757"];
""", "assets/cap02/IMG-02-02-ciclo-agente.png")
print("ok")
