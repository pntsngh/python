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

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, tankin_koko):
        self.tankin_koko = tankin_koko
        super().__init__(rekkari, huippunopeus)

s_auto = Sähköauto('ABC-15', 180, 52.5)
p_auto = Polttomoottoriauto('ACD-123', 165, 32.3)
s_auto.nopeus = 120
p_auto.nopeus = 132
s_auto.kulje(3)
p_auto.kulje(3)
print(f'Sähköauton matkamittari: {s_auto.matka}km')
print(f'Polttomoottoriauton matkamittari: {p_auto.matka}km')