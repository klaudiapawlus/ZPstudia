class Pojazd:
    def __init__(self, marka: str, model: str, rejestracja: str, przebieg: int, kolor: str):
        self._marka = marka
        self._model = model
        self._rejestracja = rejestracja
        self._przebieg = przebieg
        self._kolor = kolor

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, value):
        self._marka = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def rejestracja(self):
        return self._rejestracja

    @rejestracja.setter
    def rejestracja(self, value):
        self._rejestracja = value

    @property
    def przebieg(self):
        return self._przebieg

    @przebieg.setter
    def przebieg(self, value):
        self._przebieg = value

    @property
    def kolor(self):
        return self._kolor

    @kolor.setter
    def kolor(self, value):
        self._kolor = value

    def __str__(self):
        return f'Pojazd: {self.marka} Pod adresem: {self.model} o numerze: {self.rejestracja} przebieg: {self.przebieg} w kolorze {self.kolor}'

