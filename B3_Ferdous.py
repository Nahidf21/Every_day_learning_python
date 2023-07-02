#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:40:40 2023

@author: nahidferdous
"""

##                      Question : B-3.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('tips.csv')

# Filter the data to include only male customers
male_tips = df[df['sex'] == 'Male']['tip']

# Generate a histogram
plt.hist(male_tips, bins=10, alpha=0.5, color='g')
plt.xlabel('Tip Amount')
plt.ylabel('Frequency')
plt.title('Histogram of Tip Amounts Given by Male Customers')
plt.grid(True)
plt.show()

# Calculate and print the mean and standard deviation
mean_tip = np.mean(male_tips)
std_dev_tip = np.std(male_tips)

print(f'Mean Tip Amount: {mean_tip}')
print(f'Standard Deviation of Tip Amounts: {std_dev_tip}')

## The histogram shows that the distribution of tip amounts for 
## male customers is somewhat normally distributed. However, 
## there is a slight right skew, which means that there are more 
## tips that are towards the higher end of the range. The mean 
## tip amount is $3.089 and the standard deviation is $1.48.