nimet = set()

syöte = input('Syötä nimi: ')
nimet.add(syöte)
print('Uusi nimi.')

while syöte != '':
    nimet.add(syöte)
    syöte = input('Syötä uusi nimi: ')
    if syöte in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')

print(nimet)