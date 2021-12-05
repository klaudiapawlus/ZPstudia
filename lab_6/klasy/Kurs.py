
class Kurs:
    def __init__(self, pojazd: object, komu: object, odcinki: list, kiedy: str, rodzaj: str):
        self._pojazd = pojazd
        self._komu = komu
        self._odcinki = odcinki
        self._kiedy = kiedy
        self._rodzaj = rodzaj

    @property
    def pojazd(self) -> object:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value):
        self._pojazd = value

    @property
    def komu(self) -> object:
        return self._komu

    @komu.setter
    def komu(self, value):
        self._komu = value

    @property
    def odcinki(self):
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value):
        self._odcinki = value

    @property
    def kiedy(self):
        return self._kiedy

    @kiedy.setter
    def kiedy(self, value):
        self._kiedy = value

    @property
    def rodzaj(self):
        return self._rodzaj

    @rodzaj.setter
    def rodzaj(self, value):
        self._rodzaj = value

    def __str__(self):
        return f'Kiedy {self.kiedy}  \n komu:{self.komu} \n {self.pojazd}  rodzaj:{self.rodzaj}'

    def markapoj(self):
        return (self.pojazd.marka)


