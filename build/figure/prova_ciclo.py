"""Figura di PROVA della toolchain (S2): il ciclo dell'agente."""
from grafo import disegna

disegna("""
  rankdir=LR;
  leggi [label="Leggo\n(file, errori)"];
  penso [label="Penso\n(un piano)"];
  agisco [label="Agisco\n(modifico, eseguo)", fillcolor="#FBF0EB", color="#D77757"];
  verifico [label="Verifico\n(test, output)"];
  leggi -> penso -> agisco -> verifico;
  verifico -> leggi [label="  se non va", constraint=false, color="#D77757", fontcolor="#D77757"];
""", "assets/_prova/IMG-00-01-ciclo.png")
