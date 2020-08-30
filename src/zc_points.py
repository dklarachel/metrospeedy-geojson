# get leftovers
import json
from zip_codes import nyc
from geojson import leftovers

with open('../geojson/ny.min.json', 'r') as file:
    data = json.load(file)

zip_codes = leftovers(
    data = data,
    zip_codes = nyc
)

# call api for coordinates 
import requests
from pprint import pprint

csv_data = []

# res = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=10008&rows=1")
# data = res.json()
# pprint(data)


for code in zip_codes:
    try:
        res = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q={}&rows=1".format(code))
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)
    data = res.json()
    print(data["records"][0]["geometry"]["coordinates"])
    long = data["records"][0]["geometry"]["coordinates"][0]
    lat = data["records"][0]["geometry"]["coordinates"][1]
    coord = {
        "zip code": code,
        "long": long,
        "lat": lat
    }
    csv_data.append(coord)

# write data to csv file
from csv_ops import write_data

write_data(
    file = "../coordinates.csv",
    fieldnames = ["zip code", "long", "lat"],
    data = csv_data
)

    

    
