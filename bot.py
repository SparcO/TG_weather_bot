import redis
import requests
import datetime
import json
# r = redis.StrictRedis(host='localhost', port=6379, db=1)

base_url = 'https://api.openweathermap.org/data/2.5/forecast?q=Moscow,RU&appid=c3770fdd3539a9da7aa3d7b408eba9de'

def get_weather():

    source_page = requests.get(base_url)
    city = source_page.json()
    for item in city["list"]:
        weather = item["weather"][0]
        print(f'ID: {weather["id"]}, {weather["main"]}, {weather["description"]}')

get_weather()