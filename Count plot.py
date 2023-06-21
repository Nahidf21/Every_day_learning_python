#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:08:41 2023

@author: nahidferdous
"""
## Distribution and Visualizetions 

import numpy as np
import random as r

N=100
Xrange=[1,2,3,4]
p=[0.7,0.2,0.08,0.02]
u=np.array([])

for i in range(0,N):
    s=r.choices(Xrange, p,k=1)
    u = np.append(u,s)
    
import seaborn as sns
import matplotlib.pyplot as plt

## you need indicate x= data 
sns.countplot(x=u)



