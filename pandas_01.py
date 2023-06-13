#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:40:13 2023

@author: nahidferdous
"""

import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(0,15 ).reshape(5,3), 
                index=["Texas","Ohio","Wisconsin","Colorado","Utah"],
                columns=["c1","c2","c3"])
df

## now we creat a missing value = nan colum in our datafream. 

df['c4']=np.nan
df

## now we create a new row using loc function. and used arange function to fill 
## the row.

df.loc["New Maxico"] = np.arange(15,19)
df

df.loc["Texas","c4"]=20 
df 
df.loc["Oklahom"]=np.nan
df
df["c5"]=np.nan
df
## Missing Data - Duplicate Data 
## Dropping enties from an axis using drop() function 



