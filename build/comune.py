"""Funzioni e costanti condivise dagli script di build del libro "/claude ✻ Coding"."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

RADICE = Path(__file__).resolve().parent.parent
OUTPUT = RADICE / "output"
SOFFICE = Path(r"C:\Program Files\LibreOffice\program\soffice.com")
DOT = Path(r"C:\Program Files\Graphviz\bin\dot.exe")
GS = Path(r"C:\Program Files\gs\gs10.08.0\bin\gswin64c.exe")    # Ghostscript: solo per la stampa

def utf8_console() -> None:
    """La console di Windows usa cp1252: senza questo, stampare ✻ manda in errore lo script."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except AttributeError:
            pass


def _fondi(base: dict, sopra: dict) -> dict:
    """Unisce `sopra` in `base`, ricorsivamente sui dizionari."""
    for k, v in sopra.items():
        base[k] = _fondi(dict(base[k]), v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return base


def carica_config(percorso: str | Path = "book.yaml", variante: str | None = None) -> dict:
    """Legge book.yaml. Con `variante` (es. "stampa") applica gli override di `varianti.<nome>`."""
    p = Path(percorso)
    if not p.is_absolute():
        p = RADICE / p
    with open(p, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if variante:
        varianti = cfg.get("varianti", {})
        if variante not in varianti:
            raise SystemExit(f"variante «{variante}» assente in {p.name}")
        cfg = _fondi(cfg, varianti[variante])
    cfg["_percorso"] = p
    cfg["_variante"] = variante
    return cfg


def nome_output(cfg: dict) -> str:
    return cfg.get("output", "claude-coding")


def docx_a_pdf(docx: Path, cartella: Path | None = None) -> Path:
    """Converte un .docx in PDF con LibreOffice headless, con un profilo utente isolato
    (così non interferisce con un LibreOffice eventualmente aperto)."""
    cartella = cartella or docx.parent
    profilo = Path(tempfile.gettempdir()) / "lo_profilo_claude_coding"
    cmd = [
        str(SOFFICE),
        f"-env:UserInstallation=file:///{profilo.as_posix()}",
        "--headless", "--norestore",
        # IsSkipEmptyPages=false: esporta anche le pagine bianche inserite dalle interruzioni
        # "pagina dispari", altrimenti il PDF avrebbe meno pagine del libro stampato
        "--convert-to", 'pdf:writer_pdf_Export:{"IsSkipEmptyPages":{"type":"boolean","value":"false"}}',
        "--outdir", str(cartella), str(docx),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    pdf = cartella / (docx.stem + ".pdf")
    if r.returncode != 0 or not pdf.exists():
        raise RuntimeError(f"Conversione PDF fallita:\n{r.stdout}\n{r.stderr}")
    return pdf


def avviso(msg: str) -> None:
    print(f"  ! {msg}")
