
class FirmaSpozywcza:
    def __init__(self,nazwa:str,miasto:str,ulica:str,kodpocztowy:str,nrtel:int):
        self._nazwa=nazwa
        self._miasto=miasto
        self._ulica=ulica
        self._kodpocztowy=kodpocztowy
        self._nrtel=nrtel

    @property
    def nazwa(self):
         return self._nazwa

    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value

    @property
    def miasto(self):
        return self._miasto

    @miasto.setter
    def miasto(self, value):
        self._miasto = value

    @property
    def ulica(self):
        return self._ulica

    @ulica.setter
    def ulica(self, value):
        self._ulica= value

    @property
    def kodpocztowy(self):
        return self._kodpocztowy

    @kodpocztowy.setter
    def kodpocztowy(self, value):
        self._kodpocztowy = value

    @property
    def nrtel(self):
        return self._nrtel

    @nrtel.setter
    def nrtel(self, value):
        self._nrtel = value

    def __str__(self):
        return f'Firma Spozywcza: {self.nazwa} Pod adresem: {self.miasto} {self.ulica} {self.kodpocztowy} nr kontaktowy {self.nrtel}'

