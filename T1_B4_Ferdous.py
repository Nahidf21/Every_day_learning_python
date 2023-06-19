#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:43:18 2023

@author: nahidferdous
"""


import seaborn as sns
import pandas as pd


titanic = sns.load_dataset('titanic')


grouped = titanic.groupby('class')['age'].mean()


mask = grouped < 30
print(mask)

columns = ['age', 'sex', 'class', 'fare', 'survived']


for class_name in mask[mask].index:
    display_data = titanic[titanic['class'] == class_name][columns]
    print("\n")
    print(display_data.head())

