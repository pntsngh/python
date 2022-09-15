lentokentät = {'EFHK':'Helsinki-Vantaan lentoasema',
               'ARN':'Tukholman kansainvälinen lentoasema',
               'ENGM':'Oslon lentokenttä'}

syöte = input('Mitä haluat tehdä?(hae/lisää/lopeta): ')
while syöte != 'lopeta':
    if syöte == 'hae':
        haku = input('Syötä ICAO: ')
        if haku in lentokentät:
            print({lentokentät[haku]})
        else:
            print('Lentokenttää ei löydy.')
        syöte = input('Mitä haluat tehdä?(hae/lisää/lopeta): ')

    elif syöte == 'lisää':
        koodi = input('Syötä uusi ICAO: ')
        nimi = input('Syötä uusi lentokenttä: ')
        lentokentät[koodi] = nimi
        syöte = input('Mitä haluat tehdä?(hae/lisää/lopeta): ')

print(lentokentät)