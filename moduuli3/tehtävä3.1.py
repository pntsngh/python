kalan_pituus = int(input('Anna kuhan pituus(cm): '))
puuttuu = 37 - kalan_pituus
if kalan_pituus>=37:
    print('Hieno kala! ')
else:
    print('Pistä takasi järveen. Mitasta puuttuu ' + str(puuttuu) + 'cm. ')