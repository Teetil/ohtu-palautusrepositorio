from kps_parempi_tekoaly import KPSPelaajaVsParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSPelaajaVsTekoaly

class GameStarter:

    @staticmethod
    def start_game(gamemode : str):
        if gamemode.endswith("a"):
            KPSPelaajaVsPelaaja().pelaa()
        elif gamemode.endswith("b"):
            KPSPelaajaVsTekoaly().pelaa()
        elif gamemode.endswith("c"):
            KPSPelaajaVsParempiTekoaly().pelaa()
        else:
            return False
    