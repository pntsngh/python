N = 1000000
n = 0
toistot = 0
while toistot < N:
    #x ja y ovat liukulukuja (float)
    #arvo x väliltä -1 ja 1
    x = 0
    #arvo y väliltä -1 ja 1
    y = 0
    #osuuko x ja y ympyrän sisälle
    if (x * x + y * y < 1):
        n += 1

    pi = 4 * n / N
print(f'Piin likiarvo on {pi}')