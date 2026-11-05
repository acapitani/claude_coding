"""Figure del capitolo 23 «MCP e connettori».

23.1 MCP come «presa universale» (F-352, F-353, F-358).
23.2 La configurazione reale del server «archivio» (research/note/mcp-cap23-list.txt;
     i connettori dell'account sono omessi).
"""
from grafo import disegna
from terminale import finto_terminale

disegna("""
  rankdir=LR; nodesep=0.22; ranksep=0.55;
  io [label="Claude Code", fillcolor="#FBF0EB", color="#D77757"];
  mcp [label="MCP\nuna sola «presa»,\nun solo linguaggio", shape=box, style="rounded,filled", fillcolor="#1F1E1D", fontcolor="#F0EEE6", color="#1F1E1D"];
  a [label="archivio clienti\nun programma sul tuo computer (stdio)"];
  b [label="database dell'ufficio"];
  c [label="servizio in rete\n(HTTP: posta, documenti, ticket)"];
  d [label="connettori aggiunti in claude.ai"];
  io -> mcp [dir=both, color="#D77757", penwidth=1.6];
  mcp -> {a b c d} [dir=both, color="#8C867D"];
""", "assets/cap23/IMG-23-01-presa.png")

finto_terminale([
    '<span class="a">$</span> claude mcp add archivio -- py archivio.py',
    'Added stdio MCP server archivio with command:',
    '  py archivio.py to local config',
    '',
    '<span class="a">$</span> claude mcp list',
    'Checking MCP server health…',
    '<span class="t"># (altri server dell\'account omessi)</span>',
    'archivio: py archivio.py - <span class="v">✔ Connected</span>',
    '',
    '<span class="a">$</span> claude',
    '<span class="a">&gt;</span> Quanto devo ancora incassare dalle fatture scadute',
    '  prima del 15 ottobre 2026?',
    '<span class="t">  archivio · fatture_scadute (al_giorno: "2026-10-15")</span>',
    '  Devi ancora incassare <span class="c">€ 33.074,19</span>, su 29 fatture.',
], "assets/cap23/IMG-23-02-configurazione.png", titolo="claude — un server MCP", larghezza_cm=13)
print("ok")
