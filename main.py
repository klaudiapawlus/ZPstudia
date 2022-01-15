from modules.pacjent import Pacjent
from modules.dietetyk import Dietetyk
from modules.dieta import Dieta
from modules.zamowienie import Zamowienie

pacjent1 = Pacjent('Jan', 'Kowalski', '6123345', 'Zielona 12 Bielsko-Biala')
dietetyk1 = Dietetyk('Marian', 'Złoty', '6123345', 200)
dieta1 = Dieta('Wege', 1600, 4, 499.234)
dieta2 = Dieta('Bialkowa', 2600, 6, 700.234)
zamowienie1 = Zamowienie(pacjent1, '2020-10-11', [dieta1, dieta2], dietetyk1)
print(pacjent1)
print(dieta1)
print(dietetyk1)
print(zamowienie1)
