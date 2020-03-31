from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import sqlite3


def search(req):
    return render(req,'currweather/searchbar.html')


def find(req):
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    conn = sqlite3.connect("city.db")   #making a connection to city.db
    conn.row_factory = dict_factory
    c = conn.cursor()                   #allows us to execute sql commands
    search_str = req.GET["search"]
    query = 'SELECT * FROM city WHERE name LIKE '+"'"+search_str+'%'+"'"
    #args = search_str + '%'
    #print(query)
    c.execute(query)
    search_result = c.fetchall()
    context = {'search_result':search_result}
    conn.close()
    return render(req, 'currweather/search_list.html', context)

def current(req, city_id):
    source = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+str(city_id)+'&appid=8822d04fc990a149594ad7f69d0912b6')
    data = json.loads(source.text)
    return render(req, 'currweather/weather_info.html', {'data':data})

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
