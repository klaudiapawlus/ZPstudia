from lab6 import FirmaTransportowa
from lab6 import Pojazd
from lab6 import FirmaSpozywcza
from lab6 import Odcinek
from lab6 import Kurs

FirmaSpozywcza1 = FirmaSpozywcza.FirmaSpozywcza('Biedronka', 'Bielsko', 'Główna 32', '43-300', 23424545)
Firma = FirmaTransportowa.FirmaTransportowa('Szybki Transport', 'Bielsko', 'Czerwona 12', '43-300', 1234545)

odcinek1 = Odcinek.Odcinek('Bielsko', 'Zielona', 'Zywiec', 'Kasztanowa', 12)
odcinek2 = Odcinek.Odcinek('Cieszyn', 'Zielona', 'Bielsko', 'Kasztanowa', 32)
pojazd1 = Pojazd.Pojazd('Opel', 'Astra', 'SB2345', 20300, 'Niebieski')

kurs1 = Kurs.Kurs(pojazd1, FirmaSpozywcza1, [odcinek1, odcinek2], '20-01-2021', 'zywnosc')
print(kurs1)
print(kurs1.markapoj())
