import requests


hakusana = input('Enter the city: ')

#Pyynnön malli: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
pyyntö = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid=edf46da6bef8a85442fcb8aaa8b1119f&units=metric'

vastaus = requests.get(pyyntö)
if vastaus.status_code==200:
    json_vastaus = vastaus.json()
    print(f"Temperature: {json_vastaus['main']['temp']} celsius")
    print(f"Weather: {json_vastaus['weather'][0]['description']}")
else:
    print('Haku epäonnistui')

