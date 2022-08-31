vuosi = int(input('Anna vuosiluku: '))
if ((vuosi%400 == 0) or ((vuosi%4 == 0) and (vuosi%100 != 0))):
    print('Karkausvuosi.')

else:
    print('Ei ole karkausvuosi.')