'''
Author: Nathan Page
Desc: Analysis of the effectivenes of speed warning signs. Data read from csv file and visualized with matplotlib
Created: September 24, 2021
'''


import pandas as pd
from pandas.core.frame import DataFrame

# Read data from csv file 
fname = input("Enter filename: ")

if len(fname) < 1:
    fname = "amis.csv"

data = pd.read_csv(fname)   # Read data into a pandas DataFrame

print(type(data))
print(data)
