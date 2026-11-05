"""Test di Spese di casa. Avvio: py -m unittest -v"""
import sqlite3
import unittest

import spese


class TestSpese(unittest.TestCase):
    def setUp(self):
        self.db = spese.apri(":memory:")      # database usa e getta

    def test_importi_all_italiana(self):
        self.assertEqual(spese.leggi_importo("12,50"), 1250)
        self.assertEqual(spese.leggi_importo("1.234,5"), 123450)
        self.assertEqual(spese.leggi_importo("8"), 800)
        self.assertEqual(spese.leggi_importo("€ 3,20"), 320)

    def test_importi_non_validi(self):
        for sbagliato in ["", "dodici", "-5", "0"]:
            with self.assertRaises(ValueError):
                spese.leggi_importo(sbagliato)

    def test_messaggio_in_italiano(self):
        with self.assertRaisesRegex(ValueError, "non è un importo valido"):
            spese.leggi_importo("dodici")
        with self.assertRaisesRegex(ValueError, "non è una data valida"):
            spese.aggiungi(self.db, "2026-02-30", "Casa", "Affitto", "650")

    def test_formato_euro(self):
        self.assertEqual(spese.euro(123456), "1.234,56 €")
        self.assertEqual(spese.euro(5), "0,05 €")

    def test_totali_del_mese(self):
        spese.aggiungi(self.db, "2026-10-03", "Spesa", "Supermercato", "45,30")
        spese.aggiungi(self.db, "2026-10-15", "Spesa", "Mercato", "12,70")
        spese.aggiungi(self.db, "2026-10-20", "Casa", "Bolletta luce", "80")
        spese.aggiungi(self.db, "2026-11-01", "Casa", "Affitto", "650")
        self.assertEqual(spese.totali_per_categoria(self.db, "2026-10"),
                         {"Casa": 8000, "Spesa": 5800})

    def test_dati_sbagliati_non_entrano(self):
        with self.assertRaises(ValueError):
            spese.aggiungi(self.db, "2026-02-30", "Casa", "Data impossibile", "10")
        with self.assertRaises(ValueError):
            spese.aggiungi(self.db, "2026-10-01", "Vacanze", "Categoria strana", "10")
        self.assertEqual(spese.del_mese(self.db, "2026-10"), [])

    def test_csv_per_excel(self):
        spese.aggiungi(self.db, "2026-10-03", "Spesa", "Pane; latte", "4,5")
        self.assertEqual(spese.esporta_csv(self.db, "2026-10"),
                         "data;categoria;descrizione;importo\n"
                         "2026-10-03;Spesa;Pane, latte;4,50\n")


if __name__ == "__main__":
    unittest.main()
