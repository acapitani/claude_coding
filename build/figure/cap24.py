"""Figure del capitolo 24 «Plugin e automazione headless».

24.1 La struttura del plugin ufficio-anna (esempi/cap24/marketplace, F-335, F-336).
24.2 claude -p dentro uno script: il controllo notturno delle fatture (F-337, F-369).
"""
from grafo import disegna
from terminale import finto_terminale

finto_terminale([
    'marketplace/                 <span class="t"># il «negozio» dello studio</span>',
    '├─ .claude-plugin/marketplace.json   <span class="t"># elenco dei plugin</span>',
    '└─ <span class="a">ufficio-anna/</span>             <span class="t"># il plugin</span>',
    '   ├─ .claude-plugin/plugin.json     <span class="t"># nome, versione</span>',
    '   ├─ README.md',
    '   ├─ skills/controllo-fattura/SKILL.md   <span class="t"># cap. 20</span>',
    '   ├─ hooks/hooks.json, proteggi.py      <span class="t"># cap. 21</span>',
    '   └─ agents/revisore-lettere.md         <span class="t"># cap. 22</span>',
    '',
    '<span class="a">$</span> claude plugin install ufficio-anna@studio',
    '<span class="v">✔</span> Successfully installed plugin: ufficio-anna@studio',
], "assets/cap24/IMG-24-01-plugin.png", titolo="un plugin per lo studio", larghezza_cm=13)

disegna("""
  rankdir=LR; nodesep=0.25; ranksep=0.4;
  pdf [label="fatture/*.pdf", shape=folder];
  script [label="controlla_fatture.py\nper ogni fattura…"];
  claude [label="claude -p\nsola lettura, tetto di spesa,\nrisposta in formato fisso", fillcolor="#FBF0EB", color="#D77757"];
  csv [label="controllo.csv\n03 corretta · 14 da controllare", shape=note];
  pdf -> script -> claude;
  claude -> script [label=" JSON", style=dashed, color="#8C867D", fontcolor="#6E6962"];
  script -> csv;
""", "assets/cap24/IMG-24-02-pipeline.png")
print("ok")
