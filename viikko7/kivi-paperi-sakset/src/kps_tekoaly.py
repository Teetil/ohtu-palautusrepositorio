from kivipaperisakset import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSPelaajaVsTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()

    def _tokan_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print("Tietokone antoi siirron: ", siirto)
        return siirto

       
