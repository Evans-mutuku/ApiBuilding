from django.shortcuts import render
from django.http import HttpResponse

import requests

from .models import cities

def weather_app(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9f05ee2fa8d2c49c9464b1811efc71ee'
    weather_data = []

cities_list = cities.objects.all()

for city in cities_list:
    get_weather = requests.get(url.format(city)).json()

    print(get_weather)

    return render(request,'weather/weather_page.html')