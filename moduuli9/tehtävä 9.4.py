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

autot = []

for i in  range(10):
    auto = Auto(f'ABC-{i+1}', random.randint(100, 200))
    autot.append(auto)

tunti = 0

for a in autot:
    while a.matka < 10000:
        for a in autot:
            a.kiihdytä(random.randint(-10, 15))
        for a in autot:
            a.kulje(1)
        for i in autot:
            print(f'Auto: {i.rekkari} | Huippunopeus: {i.huippunopeus} | Nopeus: {i.nopeus} | Matka: {i.matka}')
        tunti += 1
        print(f'Aikaa kulunut {tunti} tuntia.')
