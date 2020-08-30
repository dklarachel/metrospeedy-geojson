import json
from pprint import pprint
import time

from zip_codes import ny_zc, nj
print('len of ny_zc: {}'.format(len(ny_zc)))

with open('../geojson/ny.min.json', 'r') as file:
    data = json.load(file)

print('len of data features: {}'.format(len(data['features'])))

# make list from zip codes in geojson file that are in the nyc_zc list 
ny_in_data = []
for feature in data['features']:
    if feature["properties"]["ZCTA5CE10"] in ny_zc:
        ny_in_data.append(feature["properties"]["ZCTA5CE10"])

# check which zip codes were not in this geojson file
not_in_file = []
for x in ny_zc:
    if x not in ny_in_data:
        not_in_file.append(x)

print('len of zip codes in data: {}'.format(len(ny_in_data)))
print('len of zip codes not in data: {}'.format(len(not_in_file)))

counter = 0
for feature in data['features'].copy():
    if feature["properties"]["ZCTA5CE10"] not in ny_zc:
        data['features'].remove(feature)
        counter += 1

with open('../metrospeedy_zip_codes.geojson', 'w') as file:
    json.dump(data, file, indent=2)