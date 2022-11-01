import random

class Auto:

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.tunnit = tunnit
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for a in autot:
            a.kiihdytä(random.randint(-10, 15))
            a.kulje(1)

    def tulosta_tilanne(self):
        for a in autot:
            print(f'Auto: {a.rekkari} | Huippunopeus: {a.huippunopeus} | Nopeus: {a.nopeus} | Matka: {a.matka}')

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.matka >= self.pituus:
                return True

autot = []

for i in range(10):
    auto = Auto(f'ABC-{i+1}', random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

tunti = 0

kisa = True
while kisa:
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()
        print(f'Aikaa kulunut {tunti} tuntia.')
    kilpailu.kilpailu_ohi()
    if kilpailu.kilpailu_ohi():
        kisa = False
        kilpailu.tulosta_tilanne()
        print(f'Aikaa kulunut {tunti} tuntia.')


