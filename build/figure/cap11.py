"""Figure del capitolo 11 «Test e debug».
L'uscita dei test è quella reale (research/note/test-cap11-prima.txt), eseguita sulla versione del cap. 10."""
from grafo import disegna
from terminale import finto_terminale

disegna("""
  rankdir=LR; nodesep=0.5; ranksep=0.7;
  rosso [label="Rosso\nscrivo un test\nche fallisce", fillcolor="#F9E3E3", color="#C0504D"];
  verde [label="Verde\ncorreggo il codice\nfinché passa", fillcolor="#EDF4E9", color="#6B9B57"];
  rifinisco [label="Rifinisco\nmigliorando, con\ni test sempre verdi"];
  rosso -> verde -> rifinisco;
  rifinisco -> rosso [label="  nuovo caso", constraint=false, color="#D77757", fontcolor="#D77757"];
""", "assets/cap11/IMG-11-02-rosso-verde.png")

finto_terminale([
    '<span class="a">$</span> node prova-convertitore.mjs convertitore.html',
    '<span class="v">✔</span> 1 miglia → chilometri: 1,6093 chilometri',
    '<span class="v">✔</span> 12 pollici → centimetri: 30,48 centimetri',
    '<span class="v">✔</span> 10 libbre → chilogrammi: 4,5359 chilogrammi',
    '<span class="v">✔</span> -40 gradi Celsius → gradi Fahrenheit: -40 …',
    '<span class="v">✔</span> 100 gradi Celsius → kelvin: 373,15 kelvin',
    '<span class="r">✘</span> 1,5 metri → centimetri: <span class="r">1500 centimetri</span>',
    '     <span class="t">(atteso: 150 centimetri)</span>',
    '<span class="r">✘</span> -10 kelvin → gradi Celsius: <span class="r">-283,15 gradi Celsius</span>',
    '     <span class="t">(atteso: Sotto lo zero assoluto: controlla il valore)</span>',
    '',
    '<span class="r b">2 test falliti</span>',
], "assets/cap11/IMG-11-01-test-falliti.png", titolo="esempi — test", larghezza_cm=13)
print("ok")
