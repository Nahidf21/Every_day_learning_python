#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:05:52 2023

@author: nahidferdous
"""

## How can we controle the axes

import matplotlib.pyplot as plt

size=["s","m","l"]
mark=[1,4,9]

fig=plt.figure()
ax1= fig.add_axes([0,0,1,1])
ax1.bar(size,mark)
ax1.set_title("Bar Chart")
plt.show()


fig=plt.figure()
ax2= fig.add_axes([0,0,1,.5])
ax2.bar(size,mark)
ax2.set_title("Bar Chart")
plt.show()