
lista = [20, 10, 3, 12, 5]


def zad_b1(n):
    for number in range(len(n)):
        print(n[number]*2)


zad_b1(lista)


def zad_b2(n):
    numbers2 = [number * 2 for number in n]


zad_b2(lista)
