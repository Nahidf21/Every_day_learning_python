#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:55:41 2023

@author: nahidferdous
"""
import matplotlib.pyplot as plt
import seaborn as sns

## load the dataset from the Seaborn 

irish= sns.load_dataset("iris")
titanic= sns.load_dataset("titanic")
tips= sns.load_dataset("tips")
flight=sns.load_dataset("flights")

## joint plot in Seaborn
sns.jointplot(x="sepal_length", y="petal_width", data=irish)
plt.suptitle("Joint Plot")
plt.show()


sns.jointplot(x="sepal_length", y="petal_width",data=irish,kind="kde")            
plt.suptitle("Joint Plot")
plt.show()

## Pairplot
sns.pairplot(irish)
plt.title("Iris Data : Pair Plot")
plt.show()

## if i want to change the color of the Pairplot then we can 
## add hue="species"

sns.pairplot(irish, hue="species", markers=["o","s","D"])
plt.title("Iris data Pair plot")
plt.show()











