from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self._ostokset:
            lukumaara += ostos.lukumaara()
        return lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum([n.hinta() for n in self._ostokset])
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ost = next((n for n in self._ostokset if n.tuotteen_nimi() == lisattava.nimi()), None)
        if ost:
            ost.muuta_lukumaaraa(1)
            return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ost = next((n for n in self._ostokset if n.tuotteen_nimi() == poistettava.nimi()), None)
        if ost.lukumaara() > 1:
            ost.muuta_lukumaaraa(-1)
        else:
            self._ostokset.remove(ost)
        # poistaa tuotteen

    def tyhjenna(self):
        self._ostokset.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
