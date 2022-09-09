tunnus = ''
salasana = ''
toistot = 5
yritykset = 0

while not (tunnus == 'python' and salasana == 'rules') and yritykset < toistot:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    yritykset += 1

if(yritykset >= 5):
    print('Pääsy evätty')
else:
    print('Tervetuloa')