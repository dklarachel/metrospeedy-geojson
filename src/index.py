import json
from pprint import pprint
import time

from geojson import *

from zip_codes import all_zc

for x in all_zc:
    with open('../geojson/{}.min.json'.format(x["state"]), 'r') as file:
        data = json.load(file)

    print('\n', '---- {} ----'.format(x["str"]))
    print('len of data features: {}'.format(len(data['features'])))

    edit_geojson(
        data = data,
        zip_codes = x["list"],
        write_file = "../geojson/{}_zc.geojson".format(x["str"])
    )

    if leftovers(data = data, zip_codes = x["list"]):
        write_points(
            leftovers = leftovers(data = data, zip_codes = x["list"]),
            area = x["str"]
        )
        merge_geojson(
            merged_file = "../geojson/{}_zc.geojson".format(x["str"]),
            files_to_combine = [
                "../geojson/{}_zc.geojson".format(x["str"]),
                "../geojson/{}_points.geojson".format(x["str"])
            ]
        )

    

# merge_geojson(
#     merged_file = "../geojson/metrospeedy.geojson",
#     files_to_combine = ["../geojson/nj_zc.geojson", "../geojson/ny_zc.geojson"]
# )
# print('\n', 'all done!')



# with open('../geojson/nj.min.json', 'r') as file:
#     data = json.load(file)

# print('len of data features: {}'.format(len(data['features'])))

# leftovers(
#     data = data,
#     zip_codes = nj
# )

# edit_geojson(
#     data = data,
#     zip_codes = nj,
#     write_file = "../nj_zc.geojson"
# )




