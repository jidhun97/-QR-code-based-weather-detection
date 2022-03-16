import requests
from QR import cityname


api_key = '082893c8eb2bf0a0bc66d7a720a040d2'
#user_input = input("enter the city name: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp1 = weather_data.json()['main']['temp']
