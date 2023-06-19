#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:33:26 2023

@author: nahidferdous
"""

# Initial tuition cost
tuition = 5333

# Percentage increase each year
increase = 0.03

# Calculate and display the tuition for the next 5 years
for i in range(1, 6):
    tuition = tuition + (tuition * increase)
    print(f"The tuition cost in year {i} will be: ${tuition:.2f}")