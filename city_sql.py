# create json objects from gzip file
import gzip
import json

with gzip.open('city.list.json.gz','r') as f:       # gzip
    json_bytes = f.read()                           # bytes(i.e. UTF-8)
json_str = json_bytes.decode('utf-8')               # string(i.e. JSON)
data = json.loads(json_str)                         # data(list type)


#create db from city.list.json.gz file
import sqlite3
conn = sqlite3.connect("city.db")   #making a connection to city.db

c = conn.cursor()                   #allows us to execute sql commands

#execute the sql table

c.execute("""CREATE TABLE citydB (
            city_id integer,
            name text,
            country text
            )""")

count = 0
for d in data:
    try:
        c.execute("INSERT INTO citydB VALUES (:city_id, :name, :country)", {'city_id':d["id"], 'name':d["name"], 'country':d["country"]})
    except Exception as E:
        print('Error: ', E)
    else:    
        conn.commit()                      #commits the current transaction to make sure db is updated
        count += 1
    if count%1000 == 0:
        print(count)
conn.close() 
