while True:
    syote = float(input('syötä tuumat: '))
    sentit = syote * 2.51
    if syote < 0:
        break
    else:
        print(sentit, 'cm')
