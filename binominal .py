#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:58:42 2023

@author: nahidferdous
"""

## binominal distribution 

import numpy as np
import random as r
import seaborn as sns

np.random.seed(1)
n,p =10, .5
## here p is the probability , n is the excepted value
s=np.random.binomial(n,p, 100)

print(s)
sns.countplot(x=s)

