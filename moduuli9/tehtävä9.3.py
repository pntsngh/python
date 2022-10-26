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

auto = Auto('ABC-123', 142)
auto.matka = 2000
auto.kiihdytä(60)
auto.kulje(1.5)
print(f'Nopeus tällä hetkellä: {auto.nopeus}km/h ja kuljettu matka: {auto.matka}km')
