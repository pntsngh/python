import random


def heitä_noppaa():
    return random.randint(1, 6)

noppa = 0
while noppa != 6:
    noppa = heitä_noppaa()
    print(noppa)
