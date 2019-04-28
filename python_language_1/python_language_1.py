# -*- coding: utf-8 -*-
import csv
import json
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt


def canToInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def rainDict(filename):
    '''
    extracts data from csv file and stores to dictionary
    '''
    year_dict = defaultdict(list)
    with open(filename,'rt') as f:
        reader = csv.reader(f)
        for year, _, value  in reader:
            if not canToInt(year):
                continue # skipping first line
            year_dict[year].append(value)
    return year_dict


def plotYear(filename, year, colour="blue"):
    '''
    produces plot of daily rainfalls for a year 
    '''
    with open(filename, 'r') as openfile:
        data = json.load(openfile)
        
    # generating x and y axis data
    y_axis = [float(val) for val in data[str(year)]]
    x_axis = np.arange(1, len(y_axis)+1)
    
    # creating plot
    plt.plot(x_axis, y_axis, color=colour)
    plt.title(f" rainfall in {year}")
    plt.xlabel("day of the year")
    plt.ylabel("daily rainfall (mm/day)")
    plt.savefig('year_rain.png')
    plt.close()
    return

def plotMeanFall(filename, start_year, end_year):
    '''
    produces plot of mean daily rainfall for each year in a given interval
    '''
    with open(filename, 'r') as openfile:
        data = json.load(openfile)
        
    x_axis = np.arange(start_year, end_year+1)
    
    # generating y_axis data
    y_axis = np.zeros(x_axis.size)
    for i in range(x_axis.size):
         year_fall = np.array([float(val) for val in data[str(x_axis[i])]])
         y_axis[i] = np.mean(year_fall)
         
    # creating plot
    plt.bar(x_axis, y_axis)
    plt.title(f"average rainfalls between {start_year} and {end_year}")
    plt.xlabel("year")
    plt.ylabel("mean rainfall (mm/day)")
    plt.savefig('mean_fall.png')
    plt.close()
    return


def valueCorrector(value):
    '''
    applies correction formula to rainfall value
    '''
    return value * 1.2 ** np.sqrt(2)

def correctedYear1(filename, year):
    '''
    corrects all data for a year using a for loop
    pro: more explicit
    con: proper n00b method
    '''
    with open(filename, 'r') as openfile:
        data = json.load(openfile)
    corrected_vals = []
    for val in data[str(year)]:
        corrected_vals.append(valueCorrector(float(val)))
    return corrected_vals
    
def correctedYear2(filename, year):
    '''
    corrects all data for a year using a list comprehension
    pro: one line
    con: more likely to make a mistake
    '''
    with open(filename, 'r') as openfile:
        data = json.load(openfile)
    corrected_vals = [valueCorrector(float(val)) for val in data[str(year)]]
    return corrected_vals
    
# import csv file, store to dict
rain_data = "python_language_1_data.csv"
rain_dict = rainDict(rain_data)

# store dictionary to json file
json_file = "python_language_1_data.json" 
with open(json_file, 'w') as outfile:
    json.dump(rain_dict, outfile, indent=4)

# produce rainfall plots
plotYear(json_file, 1998)
plotMeanFall(json_file, 1988, 2000)

# rainfall data corrections using two methods
newVals1 = correctedYear1(json_file, 2006)
newVals2 = correctedYear2(json_file, 2006)

# check that methods produce same results
for val1, val2 in zip(newVals1, newVals2):
    if val1 != val2:
        print("hol' up")
