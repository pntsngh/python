def listanmuokkaus(lista):
    for luku in lista:
        if luku % 2 != 0:
            lista1.remove(luku)

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(lista1)
listanmuokkaus(lista1)
print(lista1)