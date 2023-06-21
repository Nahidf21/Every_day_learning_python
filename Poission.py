#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:28:58 2023

@author: nahidferdous
"""
## poisson distributions

import numpy as np
import random as r
import seaborn as sns

from scipy.stats import poisson
N=100
## here 10 is the mean of the poisson distribution 
y=poisson(10)
s=y.rvs(N)
sns.countplot(x=s)

