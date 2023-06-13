#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 01:02:34 2023

@author: nahidferdous
"""

## white space characters remove:
    
import seaborn as sns
import pandas as pd

titanic= sns.load_dataset("titanic")
df= titanic[["age","sex","class","fare","survived"]]
print(" number of passengers are : ", format(len(df)))

## lets use groupby() function and apply this in "class" columns

groupbys= df.groupby("class")