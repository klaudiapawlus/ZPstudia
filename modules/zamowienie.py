from modules.pacjent import Pacjent
from modules.dietetyk import Dietetyk


class Zamowienie:

    def __init__(self, pacjent: Pacjent, data: str,
                 dieta: list, dietetyk: Dietetyk):
        self._pacjent = pacjent
        self._data = data
        self._dieta = dieta
        self._dietetyk = dietetyk

    @property
    def dietetyk(self) -> object:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value):
        self._dietetyk = value

    @property
    def pacjent(self) -> object:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value):
        self._pacjent = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def dieta(self) -> list:
        return self._dieta

    @dieta.setter
    def dieta(self, value):
        self._dieta = value

    def policz_cene(self):
        suma_cena: float = 0.0

        for dieta in self.dieta:
            suma_cena += dieta.cena

        return round(suma_cena, 2)

    def policz_kcal(self):
        suma_kcal: int = 0

        for dieta in self.dieta:
            suma_kcal += dieta.ilosckcal

        return suma_kcal

    def __str__(self):
        return f'{self.data} Suma kalorii {self.policz_kcal()}' \
               f'  Koszt całość: {self.policz_cene()}'
