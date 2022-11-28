import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_ostoskorin_hinta_yhden_tuotteen_jälkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        kaakao = Tuote("Kaakao", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaakao)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_jalkeen_hinta_summa_oikein(self):
        maito = Tuote("Maito", 3)
        kaakao = Tuote("Kaakao", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaakao)
        self.assertEqual(self.kori.hinta(), 7)
    
    def test_kahden_saman_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_jalkeen_hinta_summa_oikein(self):
        peruna = Tuote("Peruna", 7)
        self.kori.lisaa_tuote(peruna)
        self.kori.lisaa_tuote(peruna)
        self.assertEqual(self.kori.hinta(), 14)