#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 03:08:17 2023

@author: nahidferdous
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set the number of random numbers
num_samples = 100

# Generate random numbers uniformly distributed between 0 and 15
random_numbers = np.random.uniform(0, 15, num_samples)

# Create a histogram
plt.hist(random_numbers, bins='auto', alpha=0.7)
plt.title('Histogram of Generated Waiting Times')
plt.xlabel('Waiting Time')
plt.ylabel('Frequency')
plt.show()

# Perform Kolmogorov-Smirnov test
d, p_value = stats.kstest(random_numbers, 'uniform', args=(0, 15))

# Print the p-value
print("p-value: ", p_value)

#In this context, the null hypothesis is that the 
#generated numbers do follow a uniform distribution. 
#Given that our p-value is above 0.05, we do not have 
#enough evidence to reject the null hypothesis. 
#Therefore, based on this test, we can conclude 
#that the distribution of expected waiting times 
#appears to be uniform.