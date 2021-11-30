class FirmaTransportowa:
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
        return f'Firma transportowa: {self.nazwa} Pod adresem: {self.miasto} {self.ulica} {self.kodpocztowy} nr kontaktowy {self.nrtel}'


Firma=FirmaTransportowa('Szybki Transport','Bielsko','Czerwona 12','43-300',1234545)




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


FirmaSpozywcza1=FirmaSpozywcza('Biedronka','Bielsko','Główna 32','43-300',23424545)

class Pojazd:
    def __init__(self,marka:str,model:str,rejestracja:str,przebieg:int,kolor:str):
        self._marka=marka
        self._model=model
        self._rejestracja=rejestracja
        self._przebieg=przebieg
        self._kolor=kolor

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
        return f'Pojazd: {self.marka} Pod adresem: {self.model} o numerze: {self.rejestracja } przebieg: {self.przebieg } w kolorze {self.kolor}'


pojazd1=Pojazd ('Opel','Astra','SB2345',20300,'Niebieski')


class Odcinek:
    def __init__(self,startmiasto:str,startulica:str,stopmiasto:str,stopulica:str,odlegloswkm:int):
        self._startmiasto=startmiasto
        self._startulica=startulica
        self._stopmiasto=stopmiasto
        self._stopulica=stopulica
        self._odlegloswkm=odlegloswkm

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
        self._startulica= value

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
        return f'Odcinek z: {self.startmiasto} ulica: {self.startulica } do  {self.stopmiasto } ulica: {self.stopulica } odległosc: {self.odlegloswkm }'


odcinek1=Odcinek('Bielsko','Zielona','Zywiec','Kasztanowa',12)
odcinek2=Odcinek('Cieszyn','Zielona','Bielsko','Kasztanowa',32)


class Kurs:
    def __init__(self,pojazd:object,komu:object,odcinki:list,kiedy:str,rodzaj:str):
        self._pojazd= pojazd
        self._komu = komu
        self._odcinki = odcinki
        self._kiedy= kiedy
        self._rodzaj = rodzaj

    @property
    def pojazd(self) ->object:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value):
        self._pojazd = value

    @property
    def komu(self)->object:
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
        self._rodzaj= value

    def __str__(self):
        return f'Kiedy {self.kiedy}  \n komu:{self.komu } \n {self.pojazd }  rodzaj:{self.rodzaj }'

    def markapoj(self):
        return (self.pojazd.marka)





kurs1=Kurs(pojazd1,FirmaSpozywcza1,[odcinek1,odcinek2],'20-01-2021','zywnosc')

print(kurs1)

print(kurs1.markapoj())
