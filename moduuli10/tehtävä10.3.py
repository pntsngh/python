class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, kohdekerros):
        # jos kohdekerros ei ole alimman ja ylimmän kerroksen rajoissa, kerro että kerrosta ei ole ja lopeta
        if self.alinkerros > kohdekerros > self.ylinkerros:
            print('Kerrosta ei ole.')
            return
        # niinkauan kun hissin kerros on pienempi kuin kohdekerros
        # siirry ylös
        while self.kerros < kohdekerros:
            self.kerros_ylös()
        #niin kauan kun hissin kerros on suurempi kuin kohdekerros
        #siirry alas
        while self.kerros > kohdekerros:
            self.kerros_alas()
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi on kerroksessa {self.kerros}')
        return

    def kerros_ylös(self):
        self.kerros += 1
        print(f'Hissi on kerroksessa {self.kerros}')
        return

class Talo:
    def __init__(self, alinkerros, ylinkerros, lkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        #lista hissejä varten
        self.hissit = []
        #lisää hissit listaan
        for luku in range(lkm):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissiä(self, nro, kohdekerros):
        print(f'Ajetaan hissillä {nro}')
        #siirrä hissi kerros x kerrokseen y
        self.hissit[nro-1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        h = 0
        print('Palohälytys! Kaikki hissit siirtyvät alas.')
        #kaikki listan hissit alimpaan kerrokseen
        for hissi in self.hissit:
            hissi.alinkerros
        for hissi in self.hissit:
            print(f'Hissi {h+1} on kerroksessa {hissi.kerros}')
            h += 1

talo = Talo(0, 5, 4)
talo.palohälytys()