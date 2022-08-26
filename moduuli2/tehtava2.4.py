kokonaisluku1_str = input('anna ensimmäinen kokonaisluku: ')
kokonaisluku2_str = input('anna toinen kokonaisluku: ')
kokonaisluku3_str = input('anna kolmas kokonaisluku: ')
kok1 = float(kokonaisluku1_str)
kok2 = float(kokonaisluku2_str)
kok3 = float(kokonaisluku3_str)

summa = kok1 + kok2 + kok3
tulo = kok1 * kok2 * kok3
keskiarvo = summa / 3

print('summa: ' + str(summa))
print('tulo: ' + str(tulo))
print('keskiarvo: ' + str(keskiarvo))