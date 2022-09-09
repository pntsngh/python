import random

oikeanumero = random.randint(1, 10)

while True:
    arvaus = int(input('Arvaa luku väliltä 1-10: '))
    if arvaus == oikeanumero:
        print('Oikein!')
        break
    elif arvaus < oikeanumero:
        print('Luku on isompi.')
    else:
        print('Luku on pienempi.')