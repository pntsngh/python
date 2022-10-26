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

auto1 = Auto('ABC-1', random.randint(100, 200))
autot.append(auto1)
auto2 = Auto('ABC-2', random.randint(100, 200))
autot.append(auto2)
auto3 = Auto('ABC-3', random.randint(100, 200))
autot.append(auto3)
auto4 = Auto('ABC-4', random.randint(100, 200))
autot.append(auto4)
auto5 = Auto('ABC-5', random.randint(100, 200))
autot.append(auto5)
auto6 = Auto('ABC-6', random.randint(100, 200))
autot.append(auto6)

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
