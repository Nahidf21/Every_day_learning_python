#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:35:13 2023

@author: nahidferdous
"""

import numpy as np
import random as r
import seaborn as sns

## normal distribution 
from scipy.stats import norm
N=100

## here mean value is 10 and std is 1
x=norm(10,1)
s1=x.rvs(N)
sns.distplot(s1,hist=True)

## this graph is not looks like normal distribution 
## lets check using scipy.stats packages 

from scipy.stats import shapiro 
shapiro(s1)

##when N=100 , output : ShapiroResult(statistic=0.9919200539588928,
                     ##  pvalue=0.8154038786888123)
##The Shapiro-Wilk test result you provided indicates that 
##the test statistic is approximately 0.992 and the p-value is 
##approximately 0.815.

##Since the p-value (0.815) is greater than the commonly used 
##significance level of 0.05, we fail to reject the null hypothesis.
##This means that there is not enough evidence to conclude 
##that the sample deviates significantly from a normal distribution.

##In other words, based on the Shapiro-Wilk test, we can consider 
##the generated samples (s1) to be approximately normally distributed.


## lets use Truncnorm
from scipy.stats import truncnorm 
N=100
## here upper bound is 100, lower bound is 0
lower,upper =0,100
## mean 70 and standard division 10
mu,sigma=70, 10
x= truncnorm((lower-mu)/sigma,(upper-mu)/sigma,loc=mu,scale=sigma)
s3=x.rvs(N)
sns.distplot(s3)


## The gamma distribution
from scipy.stats import gamma
N=100
s4=gamma.rvs(a=2,size=N)
sns.distplot(s4)


