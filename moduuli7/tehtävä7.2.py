nimet = set()

syöte = input('Syötä nimi: ')
nimet.add(syöte)

while syöte != '':
    nimet.add(syöte)
    syöte = input('Syötä uusi nimi: ')
    if syöte in nimet:
        print('Nimi on jo listassa.')

print(nimet)