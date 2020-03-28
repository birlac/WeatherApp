# create json objects from gzip file
import gzip
import json

with gzip.open('city.list.json.gz','r') as f:       # gzip
    json_bytes = f.read()                           # bytes(i.e. UTF-8)
json_str = json_bytes.decode('utf-8')               # string(i.e. JSON)
data = json.loads(json_str)                         # data
        
print(data[0]["id"])                                      #testing
print(json.dumps(data[200000], indent=2))
print(len(data))



