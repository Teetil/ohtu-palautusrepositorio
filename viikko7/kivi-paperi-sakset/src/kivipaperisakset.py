from tuomari import Tuomari


class KiviPaperiSakset:
    def __init__(self) -> None:
        self._tuomari = Tuomari()

    def pelaa(self):
        siirto1, siirto2 = self._pyyda_siirrot()
        while self._ok_siirto(siirto1) and self._ok_siirto(siirto2):
            self._tuomari.kirjaa_siirto(siirto1, siirto2)
            print(self._tuomari)
            siirto1, siirto2 = self._pyyda_siirrot()
        print("Game over!")
        print(self._tuomari)

    
    def _pyyda_siirrot(self):
        return self._ekan_siirto(), self._tokan_siirto()

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    def _tokan_siirto(self):
        return 0
    
    def _ok_siirto(self, siirto : str):
        return siirto in ["k", "p", "s"]