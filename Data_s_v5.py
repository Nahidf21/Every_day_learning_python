#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:45:36 2023

@author: nahidferdous
"""

## Heatmap
import matplotlib.pyplot as plt
import seaborn as sns

## load the dataset from the Seaborn 

irish= sns.load_dataset("iris")
titanic= sns.load_dataset("titanic")
tips= sns.load_dataset("tips")
flight=sns.load_dataset("flights")

## Heatmap

dflights= flight.pivot("month","year","passengers")
sns.heatmap(dflights)
plt.title("Heatmap")
plt.show()