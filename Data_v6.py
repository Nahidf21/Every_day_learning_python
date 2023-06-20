#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:10:12 2023

@author: nahidferdous
"""

## How to add text in the plot

import matplotlib.pyplot as plt

data=[1,2,3,4]
lab=["a","b","c","d"]

fig=plt.figure()

ax1= fig.add_subplot(1,2,1)

ax1.set_title("This an Example")
ax1.set_xlabel("Lab")
ax1.set_ylabel("Data")
ax1.bar(lab,data)

## now we add a text 
ax1.text(.5,3.8, "This is the text")

ax2= fig.add_subplot(1,2,2)
ax2.set_title("This an Example")
ax2.set_xlabel("Lab")
ax2.set_ylabel("Data")
ax2.bar(lab,data)

## now we add a text 
ax2.text(.5,3.8, "This is the text")

## here we create space between two charte
plt.subplots_adjust(wspace=.4)
plt.suptitle("The Charts")

## lets create legend 
ax2.legend(["Data2"],loc="upper left")
ax1.legend(["Data1"],loc="upper left")
plt.show()