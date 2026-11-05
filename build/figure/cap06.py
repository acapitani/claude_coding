"""Figure del capitolo 6 «La prima sessione» (ricostruzioni stilizzate dell'interfaccia 2.1.318)."""
from terminale import finto_terminale, n

# IMG-06-01 — anatomia dello schermo, con segnalini numerati
finto_terminale([
    '<span class="a b">✻</span> <span class="b">Claude Code</span> <span class="t">v2.1.318</span>' + n(1),
    r'  <span class="t">C:\Users\anna\Download</span>',
    '',
    '<span class="t">&gt;</span> riordina questa cartella: metti i file in sottocartelle per tipo' + n(2),
    '',
    '<span class="c">●</span> Guardo che cosa c\'è nella cartella.',
    '<span class="v">●</span> <span class="b">PowerShell</span>(Get-ChildItem | Group-Object Extension)' + n(3),
    '  <span class="t">⎿  214 file: 98 .pdf, 61 .jpg, 23 .zip, 32 altri</span>',
    '',
    '<span class="a">✻ Combobulating…</span> <span class="t">(esc to interrupt)</span>' + n(4),
    '<div class="box">&gt; <span style="background:#F0EEE6"> </span>' + n(5) + '</div>',
    '  <span class="t">? for shortcuts</span>',
], "assets/cap06/IMG-06-01-anatomia.png", titolo="Download — claude")

# IMG-06-02 — la richiesta di permesso
finto_terminale([
    '<span class="v">●</span> <span class="b">PowerShell</span>(New-Item -ItemType Directory PDF, Immagini, Archivi)',
    '<div class="box a"><span class="b">PowerShell command</span>\n\n'
    '  New-Item -ItemType Directory PDF, Immagini, Archivi\n'
    '  <span class="t">Crea tre sottocartelle in cui spostare i file</span>\n\n'
    '<span class="b">Do you want to proceed?</span>\n'
    '<span class="sel"><span class="a">❯</span> 1. Yes</span>\n'
    '  2. Yes, and don\'t ask again for New-Item commands\n'
    '  3. No, and tell Claude what to do differently <span class="t">(esc)</span></div>',
], "assets/cap06/IMG-06-02-permesso.png", titolo="Download — claude")
print("ok")
