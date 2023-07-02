#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:04:07 2023

@author: nahidferdous
"""

##                 B-2
## A. Import the necessary libraries and create a DataFrame:
    
import pandas as pd

data = {
    'State': ['CA', 'TX', 'FL', 'NY', 'IL', 'PA'],
    'TimeZone': ['PST', 'CST', 'EST', 'EST', 'CST', 'EST'],
    'Population': [39250, 27862, 20612, 19745, 12801, 12784],
    'Percentage': ['12%', '9%', '6%', '6%', '4%', '4%']
}

df = pd.DataFrame(data)

print("\n",df)

## B. Sort the data by time zone and state:

df = df.sort_values(['TimeZone', 'State'], ascending=(True, True))

print("\n",df)

## C. Add a new column for the real population:
df['RealPopulation'] = df['Population'] * 1000

print("\n",df)

## D. average_population = df['RealPopulation'].mean()

average_population = df['RealPopulation'].mean()
min_population = df['RealPopulation'].min()
max_population = df['RealPopulation'].max()

print('\nAverage population:', average_population)
print('Minimum population:', min_population)
print('Maximum population:', max_population)

## E. Calculate and display the group sum of population for each time zone:
group_sum = df.groupby('TimeZone')['RealPopulation'].sum()

print("\n",group_sum)

## F. Draw a bar plot to show the states’ populations:
import matplotlib.pyplot as plt

df.plot(kind='bar', x='State', y='Population', title='Population')
plt.ylabel('In Thousands')
plt.xlabel('State')
plt.show()

## G. Draw a pie plot to show the states’ populations:

import matplotlib.pyplot as plt

# Create a pie chart
plt.figure(figsize=(8,8)) # making the pie chart larger for better visualization
plt.pie(df['Population'], labels=df['State'])
plt.title('Population')
plt.show()


##                      Question : B-3.
print("\n")
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
