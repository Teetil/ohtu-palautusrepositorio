from kivipaperisakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()

    def _tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")     

       
