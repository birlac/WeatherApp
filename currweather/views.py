from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import sqlite3


def search(req):
    return render(req,'currweather/searchbar.html')


def find(req):
    conn = sqlite3.connect("city.db")   #making a connection to city.db
    c = conn.cursor()                   #allows us to execute sql commands
    search_str = req.GET["search"]
    query = 'SELECT * FROM citydB WHERE name LIKE '+"'"+search_str+'%'+"'"
    #args = search_str + '%'
    #print(query)
    c.execute(query)
    search_result = list(c.fetchall())
    return HttpResponse(search_result)

def zip(req):
    return render(req,'currweather/zip_weather.html')


def temp(req):
    zip_code = req.POST["zipcode"]
    source = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',us&appid=8822d04fc990a149594ad7f69d0912b6')
    data = json.loads(source.text)
    zip_temp = float(data['main']['temp'])-273.15
    zip_city = data['name']
    return HttpResponse(f'Temperature in {zip_city} is {zip_temp}')
# Create your views here.
