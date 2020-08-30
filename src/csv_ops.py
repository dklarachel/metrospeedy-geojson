import csv
import pprint

from random import random
from random import randint

def write_data (file, fieldnames, data):
    ''' fieldnames parameter is a list, data parameter is a list of dictionaries , each list item is a row'''
    with open(file, mode="a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)

def write_data_from_list (file, fieldnames, list):
    '''
    write data from a list of lists to a column
    each list is a column
    '''
    with open(file, mode="w") as csv_file:
        writer = csv.writer(csv_file, lineterminator = '\n')
        for sub_list in list:
            writer.writerow(sub_list)



        

    
