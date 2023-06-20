#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:49:15 2023

@author: nahidferdous
"""
## Seaborn 1st 
## Seaborn :
## Is a visualizetion package based on Matplotlib
## Adds featuers such as color themes and statistical charts
## Plot of real distributions 
## 1. rugplot  2.kdeplot 3.distplot

import matplotlib.pyplot as plt
import seaborn as sns

## load the dataset from the Seaborn 

irish= sns.load_dataset("iris")
titanic= sns.load_dataset("titanic")
tips= sns.load_dataset("tips")
flight=sns.load_dataset("flights")


#x=irish["petal_length"]
x=irish.petal_length.values

## or x=irish.petal_length.values  both are same

sns.rugplot(x)
plt.title("Rug Plot for petal_length In Irish data")
plt.xlabel("Patal Length")
plt.show()

## kernel Density Plot

sns.kdeplot(x)
plt.title("Kernel Density Plot")
plt.xlabel("petal_length")
plt.show()

## the Dist plot 

sns.distplot(x)
plt.title("The Dist Plot")
plt.xlabel("The dist plot")
plt.show()

## count plot is only for DataFreame

sns.countplot(x="class",data=titanic)
plt.title("Number of Pasengers for each class of the Titanic")
plt.show()

sns.countplot(x="day", data=tips)
plt.title("Number of tips given by day of the week")
plt.show()