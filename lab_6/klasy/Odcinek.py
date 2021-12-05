class Odcinek:
    def __init__(self, startmiasto: str, startulica: str, stopmiasto: str, stopulica: str, odlegloswkm: int):
        self._startmiasto = startmiasto
        self._startulica = startulica
        self._stopmiasto = stopmiasto
        self._stopulica = stopulica
        self._odlegloswkm = odlegloswkm

    @property
    def startmiasto(self):
        return self._startmiasto

    @startmiasto.setter
    def startmiasto(self, value):
        self._startmiasto = value

    @property
    def startulica(self):
        return self._startulica

    @startulica.setter
    def startulica(self, value):
        self._startulica = value

    @property
    def stopmiasto(self):
        return self._stopmiasto

    @stopmiasto.setter
    def stopmiasto(self, value):
        self._stopmiasto = value

    @property
    def startmiasto(self):
        return self._startmiasto

    @startmiasto.setter
    def startmiasto(self, value):
        self._startmiasto = value

    @property
    def stopulica(self):
        return self._stopulica

    @stopulica.setter
    def stopulica(self, value):
        self._stopulica = value

    @property
    def odlegloswkm(self):
        return self._odlegloswkm

    @odlegloswkm.setter
    def odlegloswkm(self, value):
        self._odlegloswkm = value

    def __str__(self):
        return f'Odcinek z: {self.startmiasto} ulica: {self.startulica} do  {self.stopmiasto} ulica: {self.stopulica} odległosc: {self.odlegloswkm}'

