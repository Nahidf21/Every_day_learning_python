#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:37:23 2023

@author: nahidferdous
"""

import numpy as np
import pandas as pd

df= pd.read_csv("Athlete.csv")
## Display the first 5 rows (including headers) of the data.

print(df.head(5))
print("\n")
## Create a NumPy array for the data. Show how many rows and columns there are 
## in the data.

array= df.values
rows, colomns =array.shape
print("Rows: ", rows)
print("Coloms: ", colomns)
print("\n")
## Overwrite the Year value of the 2nd row (that is, the athlete whose ID is 1)
## with 1993. Display only the Year column to check if the value has been 
## successfully changed

df.loc[1,"Year"]=1993

print(df["Year"].head())
print("\n")

## Deduct 10 from all athletes’ weights and show results.

df["Weight"]=df["Weight"]-10

print(df.head())

print("\n")
## Add a new column to the array to show the ratio of weight to height 
## of each athlete

df["ratio_weight_height"] = df["Weight"]/df["Height"]
print(df.head())








