while True:
    syote = float(input('syötä tuumat: '))
    sentit = syote * 2.54
    if syote < 0:
        break
    else:
        print(sentit, 'cm')
