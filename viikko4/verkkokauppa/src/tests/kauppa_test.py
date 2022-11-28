import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_arvoilla(self):
            self.viitegeneraattori_mock.uusi.return_value = 42

            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10

            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)

            self.varasto_mock.saldo.side_effect = varasto_saldo
            self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")

            self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)


    def test_lisataan_kaksi_eri_tuotetta(self):
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 4
            elif tuote_id == 2:
                return 6
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 2)
            elif tuote_id == 2:
                return Tuote(2, "kaakao", 3)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("janne", "11111")

        self.pankki_mock.tilisiirto.assert_called_with('janne', 42, '11111', '33333-44455', 5)

    def test_lisätään_kaksi_eri_samaa(self):
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 7
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "kookosmaito", 3)

        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("petteri", "12121")

        self.pankki_mock.tilisiirto.assert_called_with('petteri', 42, '12121', '33333-44455', 6) 


    def test_lisätään_kaksi_eri_tuotetta_loppu(self):
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 4
            elif tuote_id == 2:
                return 0
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "cashew", 1)
            elif tuote_id == 2:
                return Tuote(2, "suklaa", 4)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("ukko", "12321")

        self.pankki_mock.tilisiirto.assert_called_with('ukko', 42, '12321', '33333-44455', 1)

    def test_aloita_asiointi_nollautuu(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 41]

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 6
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "minttukrokantti", 5)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("ukko", "12321")
        self.pankki_mock.tilisiirto.assert_called_with('ukko', 42, '12321', '33333-44455', 5)


        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("nooa", "54321")
        self.pankki_mock.tilisiirto.assert_called_with('nooa', 41, '54321', '33333-44455', 10)

    def test_poista_korista(self):
        self.viitegeneraattori_mock.uusi.return_value = 42
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 6
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "perunasäkki", 5)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("daniel", "00100")
        self.pankki_mock.tilisiirto.assert_called_with('daniel', 42, '00100', '33333-44455', 5)

