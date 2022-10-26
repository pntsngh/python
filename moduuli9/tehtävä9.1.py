class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto = Auto('ABC-123', 142)

print(f' Auton rekisterinumero: {auto.rekisteri} \n Huippunopeus: {auto.huippunopeus} \n Nopeus tällä hetkellä: {auto.nopeus} \n Kuljettu matka: {auto.matka}')