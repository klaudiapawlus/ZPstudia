def zad5 (lista:list,l1: int ) -> bool:
    for i in range(len(lista)):
        if(lista[i]==l1):
            return True
    return False



print (zad5([1,2,3,4],6))