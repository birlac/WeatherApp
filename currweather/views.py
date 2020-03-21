from django.shortcuts import render
from django.http import HttpResponse
import json
import requests


def hello(req):
    return HttpResponse('Weather Today..')

def zip(req):
    return render(req,'currweather/zip_weather.html')


def temp(req):
    zip_code = req.POST["zipcode"]
    source = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',us&appid=8822d04fc990a149594ad7f69d0912b6')
    data = json.loads(source.text)
    zip_temp = data['main']['temp']
    zip_city = data['name']
    return HttpResponse(f'Temperature in {zip_city} is {zip_temp}')
# Create your views here.
