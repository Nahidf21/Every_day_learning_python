#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 01:13:21 2023

@author: nahidferdous
"""
import pandas as pd
import matplotlib.pyplot as plt

data_dic= {"CityA_High":[38,50,60,71,78,79,75,67,56,44,37,33],
           "CityA_Low":[24,35,42,53,60,62,57,47,38,28,22,19],
           "CityB_High":[55,63,75,84,94,93,91,83,76,67,59,54],
           "CityB_Low":[28,36,48,59,67,69,65,56,46,37,30,26]}
df=pd.DataFrame(data_dic)

## Draw line plots for City A to display 
## how high temperature and low temperature change over a year.

plt.plot(df["CityA_High"], marker='x', linestyle='-', color='red', label='High Temperature')
plt.plot(df["CityA_Low"], marker='x', linestyle='-', color='blue', label='Low Temperature')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.title("Temperature change over a year")
plt.legend()
plt.show()


## Draw bar plots for City A to show the comparison of 
## high temperature and low temperature of the year.

x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
            'Sep', 'Oct', 'Nov', 'Dec']
x = range(len(x_labels))
plt.bar(x,df["CityA_High"], label='High Temperature')
plt.bar(x,df["CityA_Low"], label='Low Temperature')
plt.xticks(x, x_labels)
plt.ylabel('Temperature (°C)')
plt.title('City A Temperature Comparison')
plt.legend()
plt.show()

## Draw a scatter plot to show the correlation between 
## the two cities’ monthly high temperatures and the correlation 
## between their monthly low temperatures.

plt.scatter(df["CityA_High"], df["CityB_High"], color='red', 
            label='High Temperatures')
plt.scatter(df["CityA_Low"], df["CityB_Low"], color='green', 
            label='Low Temperatures')
plt.xlabel('City A Temperature (°C)')
plt.ylabel('City B Temperature (°C)')
plt.title('Correlation between Monthly Temperatures')
plt.legend()
plt.show()







