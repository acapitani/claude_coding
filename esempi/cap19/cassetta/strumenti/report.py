"""Report settimanale delle vendite: Word con tabella e grafico, più un'email in bozza.

Uso: py report.py [AAAA-MM-GG]   (lunedì della settimana; predefinito: la settimana scorsa)
Produce report/report-AAAA-MM-GG.docx e report/email-AAAA-MM-GG.eml (da aprire,
controllare e spedire a mano: il programma non invia niente).
"""
import csv
import sys
from collections import defaultdict
from datetime import date, timedelta
from email.message import EmailMessage
from pathlib import Path

import docx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                       # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH        # noqa: E402
from docx.shared import Cm, Pt                        # noqa: E402

SOGLIA = 25  # variazione percentuale da segnalare
SETTIMANE_MEDIA = 4  # confronto con la media delle settimane precedenti, non con una sola


def euro(x):
    return f"{x:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def perc(x):
    return f"{x:+.1f}%".replace(".", ",")


def leggi(file):
    with open(file, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            yield date.fromisoformat(r["data"]), r["negozio"], r["prodotto"], \
                float(r["incasso"].replace(",", "."))


def totali(righe, inizio):
    fine = inizio + timedelta(days=7)
    t = defaultdict(float)
    for d, negozio, prodotto, incasso in righe:
        if inizio <= d < fine:
            t[(negozio, prodotto)] += incasso
    return t


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) > 1:
        lunedi = date.fromisoformat(sys.argv[1])
    else:
        oggi = date.today()
        lunedi = oggi - timedelta(days=oggi.weekday() + 7)
    righe = list(leggi("vendite.csv"))
    ora, prima = totali(righe, lunedi), totali(righe, lunedi - timedelta(days=7))
    if not ora:
        raise SystemExit(f"Nessuna vendita nella settimana del {lunedi:%d/%m/%Y}: controlla il file dei dati.")
    negozi = sorted({n for n, _ in ora})
    per_negozio = {n: sum(v for (m, _), v in ora.items() if m == n) for n in negozi}
    per_negozio_prima = {n: sum(v for (m, _), v in prima.items() if m == n) for n in negozi}
    tot, tot_prima = sum(per_negozio.values()), sum(per_negozio_prima.values())

    # le variazioni importanti, prodotto per prodotto
    # Prima versione: confronto con la sola settimana prima e soglia 15% -> 6 segnalazioni,
    # quasi tutte rumore. Meglio la media delle ultime 4 settimane.
    storico = [totali(righe, lunedi - timedelta(days=7 * k)) for k in range(1, SETTIMANE_MEDIA + 1)]
    allarmi = []
    for (n, p), v in sorted(ora.items()):
        valori = [s[(n, p)] for s in storico if (n, p) in s]
        if len(valori) < SETTIMANE_MEDIA:
            continue
        media = sum(valori) / len(valori)
        if abs(v - media) / media * 100 >= SOGLIA:
            allarmi.append(f"{p} a {n}: {euro(v)} ({(v - media) / media * 100:+.0f}% "
                           f"rispetto alla media delle {SETTIMANE_MEDIA} settimane precedenti)")

    uscita = Path("report")
    uscita.mkdir(exist_ok=True)
    grafico = uscita / f"grafico-{lunedi}.png"
    fig, ax = plt.subplots(figsize=(6, 2.6), dpi=200)
    x = range(len(negozi))
    ax.bar([i - 0.2 for i in x], [per_negozio_prima[n] for n in negozi], 0.4, label="Settimana prima", color="#B8B2A7")
    ax.bar([i + 0.2 for i in x], [per_negozio[n] for n in negozi], 0.4, label="Questa settimana", color="#D77757")
    ax.set_xticks(list(x), negozi)
    ax.yaxis.set_major_formatter(lambda v, _: euro(v).replace(",00", ""))
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(grafico)

    doc = docx.Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10.5)
    domenica = lunedi + timedelta(days=6)
    doc.add_heading(f"Vendite della settimana {lunedi:%d/%m} – {domenica:%d/%m/%Y}", level=1)
    var = (tot - tot_prima) / tot_prima * 100
    doc.add_paragraph(f"Incasso totale: {euro(tot)} ({perc(var)} rispetto alla settimana precedente).")
    tab = doc.add_table(rows=1, cols=4)
    tab.style = "Light Grid Accent 1"
    for cella, testo in zip(tab.rows[0].cells, ["Negozio", "Questa settimana", "Settimana prima", "Variazione"]):
        cella.text = testo
    for n in negozi:
        c = tab.add_row().cells
        c[0].text, c[1].text, c[2].text = n, euro(per_negozio[n]), euro(per_negozio_prima[n])
        c[3].text = perc((per_negozio[n] - per_negozio_prima[n]) / per_negozio_prima[n] * 100)
        for k in (1, 2, 3):
            c[k].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    doc.add_paragraph()
    doc.add_picture(str(grafico), width=Cm(15))
    doc.add_heading("Da guardare", level=2)
    for a in allarmi or [f"Nessuna variazione superiore al {SOGLIA}%."]:
        doc.add_paragraph(a, style="List Bullet")
    nome_doc = uscita / f"report-{lunedi}.docx"
    doc.save(nome_doc)

    mail = EmailMessage()
    mail["Subject"] = f"Vendite settimana {lunedi:%d/%m} – {domenica:%d/%m}"
    mail["To"] = "direzione@example.com"
    mail["X-Unsent"] = "1"                          # Outlook la apre come bozza da spedire
    mail.set_content(f"Buongiorno,\n\nin allegato il report delle vendite della settimana. "
                     f"Incasso totale {euro(tot)} ({perc(var)}).\n" +
                     ("Da guardare:\n" + "\n".join(f"- {a}" for a in allarmi) + "\n" if allarmi else "") +
                     "\nCordiali saluti,\nAnna")
    mail.add_attachment(nome_doc.read_bytes(), maintype="application",
                        subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
                        filename=nome_doc.name)
    (uscita / f"email-{lunedi}.eml").write_bytes(bytes(mail))

    print(f"Settimana {lunedi:%d/%m} – {domenica:%d/%m}: incasso {euro(tot)} ({perc(var)})")
    for a in allarmi:
        print("  da guardare:", a)
    print(f"Creati {nome_doc} e la bozza email (non inviata)")


if __name__ == "__main__":
    main()
