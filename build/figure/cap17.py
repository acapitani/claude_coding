"""Figura del capitolo 17 «File e cartelle»: la cartella prima e dopo (nomi reali da esempi/cap17/piano.csv)."""
from terminale import finto_terminale

finto_terminale([
    '<span class="t"># prima: i nomi della fotocamera</span>',
    r'Firenze\IMG_4141.jpg',
    r'Firenze\IMG_4142.jpg',
    r'Firenze\IMG_4143.jpg',
    r'Roma\IMG_4004.jpg',
    r'Roma\IMG_4001 (1).jpg   <span class="r">← doppione: non toccato</span>',
    r'Senza nome\IMG-2026-WA0361.jpg   <span class="r">← senza data: non toccato</span>',
    '',
    '<span class="t"># dopo: data e ora di scatto, poi il luogo</span>',
    r'Firenze\<span class="v">2026-08-17_122100_firenze.jpg</span>',
    r'Firenze\<span class="v">2026-08-16_143200_firenze.jpg</span>',
    r'Firenze\<span class="v">2026-08-17_110200_firenze.jpg</span>',
    r'Roma\<span class="v">2026-08-16_173300_roma_2.jpg</span>   <span class="t">← stesso secondo</span>',
], "assets/cap17/IMG-17-01-prima-dopo.png", titolo="foto — prima e dopo", larghezza_cm=13)
print("ok")
