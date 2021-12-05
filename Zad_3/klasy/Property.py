class Property:
    def __init__(self, area: str, rooms: int, price: int, addres: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._addres = addres

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
        self._rooms = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f'NIERUCOMOŚĆ: \n Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres}'
