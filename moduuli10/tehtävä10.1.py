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

h = Hissi(0, 5)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)