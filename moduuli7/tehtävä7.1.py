vuodenajat = ('talvi','talvi','kevät','kevät','kevät','kesä','kesä','kesä','syksy',
              'syksy','syksy','talvi')
kuukausi = int(input('Syötä kuukauden numero: '))
vuodenaika = vuodenajat[kuukausi-1]

if kuukausi < 1:
    print('eioo')

else:
    print(f'Vuodenaika on {vuodenaika}.')

