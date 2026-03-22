

class Bojovník:

    """
    Třída reprezentující bojovníka v aréně.
    """

    def __init__(self, jméno, život, útok, obrana, kostka):

        self._jméno = jméno
        self._život = život
        self._max_život = život
        self._útok = útok
        self._obrana = obrana
        self._kostka = kostka
        self._zpráva = ""

    def __str__(self):
        
        return f"{self._jméno}"
    
    def je_naživu(self) -> bool:

        """
        Funkce která kontroluje zda-li je bojovník naživu. Pokud fce vratí True bojobník je naživu, 
        pokud vrátí False bojovník zemřel.
        """

        return self._život > 0
    

    def grafické_zobrazení(self, aktuální, maximální) -> str:

        """
        Tato funkce zobrazuje graficky stav života bojovníka
        """
        
        dílků_celkem = 30

        počet_dílků = int((aktuální / maximální) * dílků_celkem)

        if počet_dílků == 0 and self.je_naživu():

            počet_dílků = 1

        return f"[{'*' * počet_dílků}{" " * (dílků_celkem - počet_dílků)}]"
    
    def grafické_zobrazení_životů(self):
        
        return f"Životy: {self.grafické_zobrazení(self._život,self._max_život)}"
    
    def braň_se(self, úder: int) -> None:

        """
        Tato fce odráží útok soupeře. Proměnná zranění je rozdíl mezi parametrem úder a součtem obrany bojovníka + hod kostkou.
        Pokud bojovník neodrazí útok, uberou se životy z proměnné self.život. 
        """

        zranění = úder - (self._obrana + self._kostka.hod())

        if zranění > 0:
            self._život -= zranění
            zpráva = f"{self._jméno} utrpěl zranění {zranění} HP." 

            if self._život <= 0:
                zpráva = f"{self._jméno} utrpěl zranění {zranění} HP a zemřel!"
                self._život = 0
        else:
            zpráva = f"{self._jméno} odrazil útok."
        self.nastav_zprávu(zpráva)            

    def útoč(self,soupeř):

        """
        Tato funkce útočí na soupeře. Parametr soupeř je objekt jiného bojovníka.
        Proměnná udeř je hodnota která představuje útok. Tato proměnná pak slouží jako parametr pro fci braň se.
        """

        udeř = self._útok + self._kostka.hod()
        zpráva = f"{self._jméno} útočí s úderem {udeř}."
        self.nastav_zprávu(zpráva)
        soupeř.braň_se(udeř)

    def nastav_zprávu(self, zpráva: str) -> None:

        self._zpráva = zpráva

    def vrať_zprávu_o_bojovníkovi(self) -> str:

        return self._zpráva



        



    
    
    
        
        