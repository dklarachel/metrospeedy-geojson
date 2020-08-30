import json
import csv

def leftovers (data, zip_codes):
    '''returns list of zip codes that were not in geojson file'''
    # make list from zip codes in geojson file that are in the zip_codes list 
    in_data = []
    for feature in data['features']:
        if feature["properties"]["ZCTA5CE10"] in zip_codes:
            in_data.append(feature["properties"]["ZCTA5CE10"])

    # check which zip codes were not in this geojson file
    not_in_file = []
    for x in zip_codes:
        if x not in in_data:
            not_in_file.append(x)

    print('len of zip codes in data: {}'.format(len(in_data)))
    print('len of zip codes not in data: {}'.format(len(not_in_file)))
    
    if not_in_file == 0:
        return False
    else:
        return not_in_file

def edit_geojson (data, zip_codes, write_file):
    '''delete certain lines from data, write to write_file'''
    # remove items 
    counter = 0
    for feature in data['features'].copy():
        if feature["properties"]["ZCTA5CE10"] not in zip_codes:
            data['features'].remove(feature)
            counter += 1
    print('removed items: {}'.format(counter))

    # write edited json to new file
    with open(write_file, 'w') as file:
        json.dump(data, file, indent=2)

def merge_geojson (merged_file, files_to_combine):
    '''takes files_to_combine as list, merges data in merged_file'''
    for index, file in enumerate(files_to_combine):
        with open(file, 'r') as read_file:
            if index == 0:
                data1 = json.load(read_file)
            else:
                data2 = json.load(read_file)

    data1["features"] += data2["features"]

    # write merged data to new file
    with open(merged_file, 'w') as write_file:
        json.dump(data1, write_file, indent=2)

def write_points (leftovers, area):
    geopoints = []
    print("leftovers: {}".format(leftovers))

    with open('../coordinates.csv', mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        # row_count = 0
        for row in reader:
            if (row["zip code"] in leftovers):
                point = [float(row["long"]), float(row["lat"])]
                print(point)
                geopoints.append(point)
            #row_count += 1

    data = {
        "type": "FeatureCollection",
        "features": []
    }

    # print("len of leftovers: {}".format(len(leftovers)))
    # print("len of geopoints: {}".format(len(geopoints)))

    for index, zc in enumerate(leftovers):
        coord_feature = {
            "type": "Feature",
            "properties": {
                "ZCTA5CE10": str(zc)
            },
            "geometry": {
                "type": "Point",
                "coordinates": geopoints[index]
            }
        }

        data["features"].append(coord_feature)

    with open("../geojson/{}_points.geojson".format(area), mode="w") as write_file:
        json.dump(data, write_file, indent=2)
        
