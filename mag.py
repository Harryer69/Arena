from bojovnik import Bojovník


class Mág(Bojovník):

    """
    Třída reprezentující magického bojovníka.
    """

    def __init__(self, jméno, život, útok, obrana, kostka, mana, magický_útok):
        super().__init__(jméno, život, útok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magický_útok = magický_útok

    def útoč(self,soupeř):

        """
        Tato funkce útočí na soupeře. Parametr soupeř je objekt jiného bojovníka.
        Proměnná udeř je hodnota která představuje útok. Tato proměnná pak slouží jako parametr pro fci braň se.
        """

        if self._mana < self._max_mana:
            self._mana += 10
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().útoč(soupeř)

            
        else:
            udeř = self._magický_útok + self._kostka.hod()
            zpráva = f"{self._jméno} útočí s magií za {udeř} HP."
            self.nastav_zprávu(zpráva)
            self._mana = 0
            soupeř.braň_se(udeř)

    def grafická_mana_a_životy(self) -> str:

        return f"Mana: {self.grafické_zobrazení(self._mana, self._max_mana)}\n{self.grafické_zobrazení_životů()}"
        