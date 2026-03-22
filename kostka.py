import random

class Kostka:

    """
    Trida reprezentujici hraci kostku
    """

    def __init__(self, pocet_sten):
        self._pocet_sten = pocet_sten

    def hod(self):

        """ Tato metoda simuluje hod kostkou."""

        return random.randint(1,self._pocet_sten)
    
    def vrat_pocet_sten(self) -> int:

        """
        Vratí počet stěn hrací kostky.
        """

        return self.pocet_sten
    
    def __str__(self):
        
        """Vrací textovou reprezentaci kostky."""

        return f"Kostka se {self._pocet_sten} stěnami."
    


    


    















