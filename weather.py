import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()
def get_curent_weather():
    print('\n*** Get Current Weather conditions ***\n')
    city =input("\n Please enter a city name:\n")

    requests_url=f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    #print(requests_url)
    weather_data=requests.get(requests_url).json()
    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\n The temp is {weather_data['main']["temp"]:.2f}')
    #pprint(weather_data)
get_curent_weather()