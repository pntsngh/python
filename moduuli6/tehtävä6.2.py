import random


def heita_noppaa(lkm):
    return random.randint(1, lkm)

lkm = int(input('syötä tahkojen lukumäärä: '))
noppa = 0
while noppa != lkm:
    noppa = heita_noppaa(lkm)
    print(noppa)