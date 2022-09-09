import random
lista = []
määrä = int(input('Montako noppaa heitetään?: '))

for luku in range(määrä):
    tulos = random.randint(1, 6)
    lista.append(tulos)
print('Silmäluvut: ', lista)
print('Silmälukujen summa: ', sum(lista))
