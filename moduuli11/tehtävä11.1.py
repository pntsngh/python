class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi} Kirjoittaja: {self.kirjoittaja} Sivut: {self.sivut}')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi} Päätoimittaja: {self.päätoimittaja}')


kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
lehti = Lehti('Aku Ankka', 'Aki Hyyppä')

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()