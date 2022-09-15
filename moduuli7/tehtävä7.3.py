lentokentät = {'EFHK':'Helsinki-Vantaan lentoasema',
               'ARN':'Tukholman kansainvälinen lentoasema',
               'ENGM':'Oslon lentokenttä'}

syöte = input('Mitä haluat tehdä?(hae/lisää/lopeta): ')
while syöte != 'lopeta':
    if syöte == 'hae':
        haku = input('syötä icao: ')
        if haku in lentokentät:
            print({lentokentät[haku]})
        else:
            print('Lentokenttää ei löydy.')
        syöte = input('Mitä haluat tehdä?(hae/lisää/lopeta): ')

    elif syöte == 'lisää':
        koodi = input('icao: ')
        nimi = input('kenttä: ')
        lentokentät[koodi] = nimi

        print(lentokentät)