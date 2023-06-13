#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:54:00 2023

@author: nahidferdous
"""

import pandas as pd

parsed = pd.read_csv("31.csv")

parsed

## we can change the data stracture differently 

parsed2 = pd.read_csv("31.csv", index_col= ["key1","key2"])
parsed2

## How to combining data sets
## pandas.concat = stacks together objects along an axis
## pandas.merge = marges dataframes based on keys 

df1= pd.DataFrame({"a":['a0','a1','a2','a3'],
                   "b":['b0','b1','b2','b3'],
                   "c":['c0','c1','c2','c3']},
                  index=[0,1,2,3])

df2= pd.DataFrame({"a":['a0','a1','a2','a3'],
                   "b":['b0','b1','b2','b3'],
                   "c":['c0','c1','c2','c3'],
                   "d":['d0','d1','d2','d3']},
                  index=[2,3,4,5])

## lets use concat to add two datafream

result1= pd.concat([df1,df2])

## lets use concat with axis=1 

result2= pd.concat([df1,df2],axis=1)    

## lets add join= 'inner' in concat() function 

result3= pd.concat([df1,df2], axis=1, join="inner")   

##_______________###
## marging data 

df3= pd.DataFrame({"a":['a0','a1','a2','a3'],
                   "b":['b0','b1','b2','b3'],
                   "c":['c0','c1','c2','c3']},
                  index=[0,1,2,3])

df4= pd.DataFrame({"a":['a0','a1','a2','a3'],
                   "b":['b0','b1','b2','b3'],
                   "c":['c0','c1','c2','c3'],
                   "d":['d0','d1','d2','d3']},
                  index=[2,3,4,5])   
    
marge_df= pd.merge(df3, df4)
