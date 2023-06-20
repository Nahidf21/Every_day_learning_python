#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:49:48 2023

@author: nahidferdous
"""
## multiple figure with title
import matplotlib.pyplot as plt

prince=[150,200,230]
size=["S","L","M"]

fig= plt.figure()

ar1= fig.add_subplot(1,2,1)
ar2= fig.add_subplot(1,2,2)

ar1.set_title("Pi Chart")
ar1.pie(prince,labels=size,autopct='%1.1f%%')
ar2.set_title("Bar Chart")
ar2.bar(size,prince)

plt.subplots_adjust(wspace=.4)
plt.suptitle("The Charts")
plt.show()

