# how to read json api using urllib or requests modules
import json
from urllib.request import urlopen
import requests


#using urllib
with urlopen("http://api.openweathermap.org/data/2.5/weather?zip=91367,us&appid=8822d04fc990a149594ad7f69d0912b6") as response:
    source = response.read()
data=json.loads(source)
print(json.dumps(data, indent=2))

#using requests
source = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=,us&appid=8822d04fc990a149594ad7f69d0912b6')
print(type(source.text))
data = json.loads(source.text)
print(json.dumps(data, indent=2))

