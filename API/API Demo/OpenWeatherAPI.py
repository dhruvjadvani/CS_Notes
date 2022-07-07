import requests
from pprint import pprint

API_key = '9ec4a45348430b997b56f1d02eab6d57'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)


