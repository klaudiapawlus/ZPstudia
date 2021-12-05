from klasy import Property


class Flat(Property.Property):
    def __init__(self, area: str, rooms: int, price: int, addres: str, floor: int):
        super().__init__(area, rooms, price, addres)
        self._floor = floor

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value

    def __str__(self):
        return f'Mieszkanie: \n Piętro:{self.floor} Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres} '
