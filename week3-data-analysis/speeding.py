'''
Author: Nathan Page
Desc: Analysis of the effectivenes of speed warning signs. Data read from csv file and visualized with matplotlib
Created: September 24, 2021
'''

from numpy import short
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

# Read data from csv file 
fname = input("Enter filename: ")

if len(fname) < 1:
    fname = "amis.csv"

datafrm = pd.read_csv(fname)   # Read csv data into a pandas DataFrame

speed_frame = datafrm['speed']  # extract speed column from data frame
period_frame = datafrm['period']

speed_list = speed_frame.tolist() #   and convert it to a list
period_list = period_frame.tolist()

pre_sign = list()
shortly_after = list()
long_time_after = list()

# extract list of speeds for each period (1,2, or 2) and store values in new lists
for speed,period in zip(speed_list,period_list):
    if period == 1: # 1: before sign was set up
        pre_sign.append(speed)
    elif period == 2:  # 2: shortly after sign 
        shortly_after.append(speed)
    elif period == 3:
        long_time_after.append(speed) # 3: a long time after sign
    else:
        continue

# calculate average/mean speed of each period
avg1 = sum(pre_sign)/len(pre_sign)
avg2 = sum(shortly_after)/len(shortly_after)
avg3 = sum(long_time_after)/len(long_time_after)

print(''' 
Average speed before sign {}
Average speed shortly after sign {}
Average speed a long time after sign {}
'''.format(avg1,avg2,avg3))

# Plot 1 
plt.hist(pre_sign, label="Before sign")
plt.subplot(131,label="Pre-Sign")
plt.ylabel("Number of drivers")
plt.xlabel("Speed (mph)")
plt.title("Before Sign")

# plot 2 
plt.hist(shortly_after)
plt.subplot(132, label="After sign")
plt.xlabel("Speed (mph)")
plt.title("Shortly After Sign")

# Plot 3
plt.hist(long_time_after)
plt.subplot(133, label="Long time after sign")
plt.xlabel("Speed (mph)")
plt.title("A Long Time After Sign")

plt.show()
