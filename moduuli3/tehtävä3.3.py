sukupuoli = input('Sukupuoli: ')
hemogl = int(input('Hemoglobiini(g/l): '))
if sukupuoli=='mies' and 134<=hemogl<=195:
    print('Normaali hemoglobiini. ')
elif sukupuoli=='mies' and hemogl<134:
    print('Alhainen hemoglobiini. ')
elif sukupuoli=='mies' and hemogl>195:
    print('Korkea hemoglobiini. ')
elif sukupuoli=='nainen' and 117<=hemogl<=175:
    print('Normaali hemoglobiini. ')
elif sukupuoli=='nainen' and hemogl<117:
    print('Alhainen hemioglobiini.')
elif sukupuoli=='nainen' and hemogl>175:
    print('Korkea hemoglobiini. ')
else:
    print('*_*')