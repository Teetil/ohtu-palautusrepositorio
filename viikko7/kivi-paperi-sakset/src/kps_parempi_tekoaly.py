from kivipaperisakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSPelaajaVsParempiTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)
        self._aloitus_siirto = True

    def _pyyda_siirrot(self):
        eka_siirto = self._ekan_siirto()
        toka_siirto = self._tokan_siirto()
        if self._aloitus_siirto:
            self._aloitus_siirto = False
        else:
            self.tekoaly.aseta_siirto(eka_siirto)
        return eka_siirto, toka_siirto

    def _tokan_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print("Tietokone antoi siirron: ", siirto)
        return siirto

       
