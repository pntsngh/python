num = int(input('Syötä luku: '))
if num > 1:
    for i in range(2, num):
        if num%i == 0:
            print('Luku ei ole alkuluku.')
            break
        else:
            print('Luku on alkuluku.')
else:
    print('Luku ei ole alkuluku.')