import mysql.connector

def haeLentokenttä(icao):
    tuple = (icao,)
    sql = '''SELECT name, municipality FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    print(f'Nimi: {tulos[0]}, Kunta: {tulos[1]}')

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Salasana1',
         autocommit=True
         )
syöte = input('icao: ')
kenttä = haeLentokenttä(syöte)


