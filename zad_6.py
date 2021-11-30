def zad6 (lista1:list,lista2: list ) -> list:
    lista3 = lista1 + lista2
    lista3=list(dict.fromkeys(lista3))


    return [l **3  for l in  lista3]


print (zad6([1,2,3,4],[6,6,5,9]))