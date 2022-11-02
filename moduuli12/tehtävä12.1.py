import requests

#Pyynnön malli: https://api.chucknorris.io/jokes/random
pyyntö = 'https://api.chucknorris.io/jokes/random'


vastaus = requests.get(pyyntö)
if vastaus.status_code==200:
    json_vastaus = vastaus.json()
    print(json_vastaus['value'])