#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:06:02 2023

@author: nahidferdous
"""

import seaborn as sns 
import numpy as np
import pandas as pd

## how to load data set using seaborn 

df= sns.load_dataset('titanic')
df.head()
df.info()
## lets use isnull() function to see the meesing data.

df.head().isnull()

## dropna().info() this two function give us the infor 
## -metion about the drop nan data. for row 

df.dropna(axis=0).info()

## check nan value for columns using dropna() function 
df.dropna(axis=1).info()

## handle indivedual columns missing values
df_age= df.dropna(subset=["age"])
print(len(df_age))

df_embarked= df_age.dropna(subset=["embarked"])
df_embarked.info()
## lets check is there any missing value avilabel or not ? 
print(df_embarked["embarked"].isnull().sum())
print(df_age["age"].isnull().sum())

## lets fill the missing value using fillna() function using
## mean value 
mean_age= df["age"].mean()
mean_age

df["age"].fillna(mean_age,inplace=True)
df.head(20)

df["embark_town"].fillna(method="ffill", inplace= True)
df.info()

df["deck"].isnull().sum()
mode_deck= df["deck"].mode()
mode_deck
df["deck"].fillna(method='ffill',inplace=True)
df.isnull().info()
print(df.isnull().sum())



