import requests

TOKEN = '1b45f9439fa3392ab44de2921f3eb427'
city = input('Please enter city: ')
# city = 'Volgograd'
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={TOKEN}')
res = response.json()
# print(response.json())

main = res['weather'][0]['main']
description = res['weather'][0]['description']

temp = res['main']['temp']
humidity = res['main']['humidity']

wind = res['wind']['speed']

print(f'Your city: {city}\n{main} - {description}\ntemp: {temp}\nhumidity: {humidity}\nwind speed: {wind}')
