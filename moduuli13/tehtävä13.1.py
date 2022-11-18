from flask import Flask

def testaus(luku):
    if luku < 2:
        return False
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            return False
    return True

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    testi = testaus(luku)

    vastaus = {
        'Number' : luku,
        'isPrime' : testi
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)