import json
from urllib.request import urlopen
import requests
'''
with urlopen("http://api.openweathermap.org/data/2.5/weather?zip=91367,us&appid=8822d04fc990a149594ad7f69d0912b6") as response:
    source = response.read()
data=json.loads(source)
print(json.dumps(data, indent=2))
'''

source = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=91367,us&appid=8822d04fc990a149594ad7f69d0912b6')
print(type(source.text))
data = json.loads(source.text)
#print(json.dumps(data, indent=2))

print(data['name'])

