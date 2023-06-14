#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:45:59 2023

@author: nahidferdous
"""
## Import pandas and NumPy packages.

import numpy as np
import pandas as pd

## Create a list that contains "id" and a dictionary containing 
## other sets of data, such as "name," "score," "attempt," and "pass/fail." 

id=np.array(["a","b","c","d","e","f","g","h","i","j"])

elements= {"name": ["Yuan","David","Margaret","Daniel",
                    "Gina","Catherine","Chris","Jacki",
                    "Ethan","Murfhy"],
           "score":[12.5,9,16.5,"N/A",9,20,14.5,"N/A",
                    8,19],
           "attempt":[1,3,2,3,2,3,1,1,2,1],
           "pass/fail":["Yes","No","Yes","No","No","Yes",
                        "Yes","No","No","Yes"]}

## Create a data frame by taking the dictionary and the list (as the index)
## you created in b)

df= pd.DataFrame(elements,index=id)
df=df.rename_axis('id')

print(df)

## Select and display the 'name' and 'score' columns of the records (rows) 
## of 1, 3, 5, and 6 from the data frame. 

name_score_col= df.iloc[[1,3,5,6],[0,1]]
print(name_score_col)

## Select and display the rows where the number of attempts is greater than 2.
## Then, select and display the rows where the score is missing (‘N/A’). 
## Also, display the records that hold both conditions.

attempts_gre_2= df[df['attempt']>2]
print(attempts_gre_2)

df_with_na= df[df["score"]=="N/A"]
print(df_with_na)

both_conditions =  df[(df["score"] == "N/A") & (df['attempt']>2) ]
print(both_conditions)

## Append the new record "k" to the data frame with the given values of each 
## column as name: 'Song,' score: '15.5', attempt: '1', and pass/fail: 'yes.' 
## After appending the new record, delete the record of 'h' from the data 
## frame. 
row_k=["Song",15.5,1,"Yes"]
df_k = df.loc["k"]=row_k
print(df)
df_del_h=df.drop("h", axis=0 ,inplace=True)
print(df)

## Replace values of 'yes' and 'no' in 'pass/fail' column with 'pass' and 
## 'fail' and display new the data frame.
df["pass/fail"]=df["pass/fail"].replace({"Yes":"Pass","No":"Fail"})
print(df)

