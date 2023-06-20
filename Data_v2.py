#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 02:28:13 2023

@author: nahidferdous
"""
import pandas as pd
import matplotlib.pyplot as plt

## who to create multiple figure 
fig= plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

## data 
size=["S","M","L"]
store1=[10,20,30]
store2=[45,41,6]

#ax1.bar(size,store2)
ax2.pie(store1,labels=['A', 'B', 'C'],autopct='%1.1f%%')
ax2.set_title("Pie Chart")

ax1.bar(size,store2)
ax1.set_title("Bar Chart")
ax1.set_xlabel("bangladesh")
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=.4)
# Display the figure
plt.show()
                     