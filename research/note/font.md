# Copertura dei glifi dello spinner nei font (verifica S0, 2026-11-04, fontTools)

| Font | ✻ U+273B | ✢ | ✶ | ✽ | ✳ | · |
|---|---|---|---|---|---|---|
| Segoe UI Symbol (seguisym.ttf) | sì | sì | sì | sì | sì | sì |
| DejaVu Sans (tutti gli stili tranne ExtraLight) | sì | sì | sì | sì | sì | sì |
| DejaVu Sans Mono / Mono Bold | sì | sì | sì | sì | sì | sì |
| DejaVu Sans Mono Oblique / BoldOblique | no | no | no | no | no | sì |
| Consolas (tutti gli stili) | no | no | sì | no | no | sì |
| Cambria, Calibri, Georgia, Segoe UI, DejaVu Serif | no | no | no | no | no | sì |

Conseguenze per l'impaginazione:
- Nel testo corrente il glifo ✻ va in un run con font **Segoe UI Symbol** (fallback DejaVu Sans).
- Nei blocchi di codice e terminale (Consolas) i glifi dello spinner vanno in un run con **DejaVu Sans Mono**,
  oppure lo stile `Libro Terminale` usa direttamente DejaVu Sans Mono (non in corsivo).
- La copertina è un'immagine: nessun problema di font.
