#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 23:32:21 2023

@author: nahidferdous
"""

import pandas as pd

data= pd.read_csv("vgsales.csv")
## lets creat a variable 
var1= data["Platform"]

## lets import matplotlib libray

import matplotlib.pyplot as plt
# lets visualize the veriable var1
var1.value_counts().plot.bar()
plt.show()

#lets plot a histogram

var1.value_counts().plot.hist(orientation="vertical")
plt.show()

#lets create another variable name var2
var2= data[["EU_Sales","JP_Sales"]]
var2.plot.area(stacked=False)
plt.show()

#lets create another variable name var2
var2= data[["EU_Sales","JP_Sales"]]
var2.plot.area(stacked=True)
plt.show()

## lets create pichart

var3= data["Platform"].head(200)
var3.value_counts().plot.pie(figsize=(10,10),title=" This is a Pi Chart")
plt.show()

















