from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Salasana1',
         autocommit=True
         )



app = Flask(__name__)
@app.route('/kenttä/<icao>')
def haeLentokenttä(icao):
    tuple = (icao,)
    sql = '''SELECT name, municipality FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    #(f'Nimi: {tulos[0]}, Kunta: {tulos[1]}')

    vastaus = {
        'Name' : tulos[0],
        'Municipality' : tulos[1],
        'ICAO' : icao
    }

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)