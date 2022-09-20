import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Salasana1',
         autocommit=True
         )


def haeLentokenttä(icao,):
    tuple = (icao,)
    sql = '''SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    print(tulos)
    lista.append(tulos)

lista = []

syöte1 = input('icao: ')
haeLentokenttä(syöte1)

syöte2 = input('icao: ')
haeLentokenttä(syöte2)
print(lista)
print(distance.distance(lista[0], lista[1]))