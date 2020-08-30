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

# scrape coordinates from google maps
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from csv_ops import write_data

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get('https://maps.google.com')

def enter_search (search_query):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchboxinput"]')))
    search_field = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
    search_field.click()
    search_field.clear()
    search_field.send_keys(search_query)
    search_field.send_keys(Keys.RETURN)

def get_coordinates ():
    url = driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')
    return url 

enter_search("10702")
url = get_coordinates()
url = url.split('?center=')[1].split('&zoom=')[0].split('%2C') # extract coordinates
print(url)

# data = []

# for code in zip_codes:
#     enter_search(code)
#     WebDriverWait(driver, 30).until(EC.url_changes(driver.current_url))
#     url = get_coordinates() 
#     url = url.split('?center=')[1].split('&zoom=')[0].split('%2C') # extract coordinates
#     # if "maps/place" not in driver.current_url:
#     if len(url) > 2:
#         coord = {
#             "zip code": code,
#             "long": "N/A",
#             "lat": "N/A"
#         }
#         data.append(coord)
#     else:
#         coord = {
#             "zip code": code,
#             "long": float(url[0]),
#             "lat": float(url[1])
#         }
#         data.append(coord)
#     print(url)

# write_data(
#     file = "../coordinates.csv",
#     fieldnames = ["zip code", "long", "lat"],
#     data = data
# )

# if url does not contain 'maps/place', skip over or label it as ??
