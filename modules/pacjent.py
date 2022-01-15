class Pacjent:

    def __init__(self, imie: str, nazwisko: str, numertel: str, adres: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._numertel = numertel
        self._adres = adres

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
    def adres(self) -> str:
        return self._adres

    def __str__(self):
        return f'Pacjent: {self.imie} {self.nazwisko}'
