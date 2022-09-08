lista = []

syöte = input('syötä luku: ')
while syöte != '':
    lista.append(syöte)
    syöte = input('syötä luku: ')

lista.sort(reverse=True)
print(lista[0:5])
