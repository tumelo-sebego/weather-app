import datetime as dt
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key', 'r').read()
CITY = 'Johannesburg'


def kelvin_to_celsious_fahrenheit(kelvin):
    
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32

    return celsius, fahrenheit

def kelvin_to_celsius(kelvin):

    return kelvin - 273.15
    
url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f'Temperature in {CITY}: {temp_celsius:.2f}')
print(f'Temperature in {CITY} feels like: {feels_like_celsius:.2f}')
print(f'Humidity in {CITY}: {humidity}%')
print(f'Wind speed in {CITY}: {wind_speed}km/h')
print(f'General Weather in {CITY}: {description}')
print(f'Sun rises in {CITY} at {sunrise_time} local time')
print(f'Sun sets in {CITY} at {sunset_time} local time')