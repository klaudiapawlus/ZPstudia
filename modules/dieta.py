class Dieta:

    def __init__(self, nazwa: str, ilosckcal: int, iloscposilkow: int, cena:float):
        self._nazwa=nazwa
        self._ilosckcal=ilosckcal
        self._iloscposilkow= iloscposilkow
        self._cena=cena

    @property
    def nazwa(self) -> str:
        return self._nazwa
    #
    # @imie.setter
    # def imie(self, value):
    #     self._imie = value
    @property
    def ilosckcal(self) -> int:
        return self._ilosckcal

    @property
    def iloscposilkow(self) -> int:
        return self._iloscposilkow
    @property
    def cena(self) ->float:
        return self._cena

    def __str__(self):
        return f'Dieta: {self.nazwa} Ilosc kalorii: {self.ilosckcal} ilość posiłków: {self.iloscposilkow} Cena:{self.cena}'

