import math


def neliöhinta(säde, hinta):
    nh = hinta / (math.pi * säde**2 / 10000)
    return nh

r = float(input('säde: '))
h = float(input('hinta: '))
vastaus = neliöhinta(r, h)

r2 = float(input('säde: '))
h2 = float(input('hinta: '))
vastaus2 = neliöhinta(r2, h2)



print(vastaus)
print(vastaus2)