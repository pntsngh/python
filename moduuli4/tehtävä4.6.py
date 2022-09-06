import math

N = 1000000
n = 0
toistot = 0

while toistot < N:
    import random

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x * x + y * y < 1):
        n += 1
        toistot += 1

    else:
        toistot += 1
piin_likiarvo_pisteillä = 4 * n / N
print('Piin likiarvo pisteillä: ', piin_likiarvo_pisteillä)
print('Piin likiarvo: ', math.pi)