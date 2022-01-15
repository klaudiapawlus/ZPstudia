class Dietetyk:

    def __init__(self, imie: str, nazwisko: str,
                 numertel: str, cenawizyty: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._numertel = numertel
        self._cenawizyty = cenawizyty

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def numertel(self) -> str:
        return self._numertel

    @property
    def cenawizyty(self) -> int:
        return self._cenawizyty

    def __str__(self):
        return f'Dietetyk: {self.imie} {self.nazwisko} Numer telefonu: ' \
               f'{self.numertel} Cena wizyty: {self.cenawizyty}'
