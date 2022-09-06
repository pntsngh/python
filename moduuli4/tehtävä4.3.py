lista = []
while True:
    syöte = input('syötä luku: ')
    if syöte == '':
        break
    lista.append(syöte)
print('Pienin luku: ', min(lista))
print('Suurin luku: ', max(lista))