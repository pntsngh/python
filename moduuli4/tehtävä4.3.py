lista = []
while True:
    syöte = input('syötä luku: ')
    if syöte == '':
        break
    lista.append(syöte)
print('Pienin luku: ', min(lista))
print('Suuin luku: ', max(lista))