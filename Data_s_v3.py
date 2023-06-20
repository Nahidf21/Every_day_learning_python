#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:17:30 2023

@author: nahidferdous
"""
## 2D mixed data : plots: Barplot, Violin plot, Strip plot

import matplotlib.pyplot as plt
import seaborn as sns

## load the dataset from the Seaborn 

irish= sns.load_dataset("iris")
titanic= sns.load_dataset("titanic")
tips= sns.load_dataset("tips")
flight=sns.load_dataset("flights")

## barplot of 2d datas
sns.barplot(x="day",y="total_bill",data=tips)
plt.title("Total tips")
plt.show()

## Violinplot
sns.violinplot(x="day",y="total_bill", data=tips)
plt.title("Total tips - violinplot")
plt.show()

## change the background 

sns.set_style("whitegrid")
sns.violinplot(x="day",y="total_bill", data=tips)
plt.title("Total tips - violinplot")
plt.show()
















