class Property:
    def __init__(self,area:str,rooms: int,price:int, addres:str):
        self._area = area
        self._rooms=rooms
        self._price=price
        self._addres=addres

    @property
    def addres(self):
        return self._addres

    @addres.setter
    def addres(self, value):
        self._addres = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms= value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f'NIERUCOMOŚĆ: \n Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres}'


class House(Property):
    def __init__(self,area:str,rooms: int,price:int, addres:str,plot:int):
        super().__init__(area,rooms,price,addres)
        self._plot = plot

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value

    def __str__(self):
        return f'DOM: \n Działka:{self.plot} Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres} '

class Flat(Property):
    def __init__(self,area:str,rooms: int,price:int, addres:str,floor:int):
        super().__init__(area,rooms,price,addres)
        self._floor = floor

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value

    def __str__(self):
        return f'Mieszkanie: \n Piętro:{self.floor} Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres} '


nieruchomosc1=Property('132m2',3,30000,'Zielona 12')
dom1=House('123m2',5,234442,'Zielona 3',123)
mieszkanie1=Flat('223m2',2,124442,'Zielona 900/a',2)
print(nieruchomosc1)
print(dom1)
print(mieszkanie1)