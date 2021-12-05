from klasy import Property


class House(Property.Property):
    def __init__(self, area: str, rooms: int, price: int, addres: str, plot: int):
        super().__init__(area, rooms, price, addres)
        self._plot = plot

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value

    def __str__(self):
        return f'DOM: \n Działka:{self.plot} Powierzchnia: {self.area} Pokoje:{self.rooms} cena:{self.price} adres: {self.addres} '
