import os as _os
import time as _time
import random as _random
from mag import Mág
from pyfiglet import figlet_format

class Aréna:

    """
    Třída reprezentující arénu v které bojovníci bojují.
    """

    def __init__(self, bojovník_1, bojovník_2, kostka):
        self.bojovník_1 = bojovník_1
        self.bojovník_2 = bojovník_2
        self.kostka = kostka

    def _vykresli_boj(self):
        self._vycisti_obrazovku()
        print(figlet_format("ARENA", font="slant"))
        print("O===[============================>")
        print()
        print()
        print(self._vypiš_bojovníka(self.bojovník_1))
        print()
        print(self._vypiš_bojovníka(self.bojovník_2))
        print()
      

    def _vycisti_obrazovku(self):

        """
        Funkce vyčistí terminál
        """

        _os.system("cls" if _os.name == "nt" else "clear")

    def _vypiš_zprávu(self, zpráva) -> None:

       print(zpráva)
       _time.sleep(2.75)

    def zápas(self):

        print("Vítejte v aréně!")
        print(f"Dnes se utkají {self.bojovník_1} a {self.bojovník_2}!")
        print(f"Zápas může začít!")
        _time.sleep(4)

        if _random.randint(0,1):
            self.bojovník_1, self.bojovník_2 = self.bojovník_2, self.bojovník_1

        while self.bojovník_1.je_naživu() and self.bojovník_2.je_naživu():

            self._vykresli_boj()
            self.bojovník_1.útoč(self.bojovník_2)
            self._vypiš_zprávu(self.bojovník_1.vrať_zprávu_o_bojovníkovi())
            self._vypiš_zprávu(self.bojovník_2.vrať_zprávu_o_bojovníkovi())
            if self.bojovník_2.je_naživu():
                self._vykresli_boj()
                self.bojovník_2.útoč(self.bojovník_1)
                self._vypiš_zprávu(self.bojovník_2.vrať_zprávu_o_bojovníkovi())
                self._vypiš_zprávu(self.bojovník_1.vrať_zprávu_o_bojovníkovi())

    def _vypiš_bojovníka(self, bojovník) -> str:

        """
        Toto fce graficky znazorňuje životy bojovníku a jejich manu.
        """

        if isinstance(bojovník, Mág):
            
            return f"{bojovník}\n{bojovník.grafická_mana_a_životy()}"

        else:
            
            return f"{bojovník}\n{bojovník.grafické_zobrazení_životů()}"
            
            







        


        


