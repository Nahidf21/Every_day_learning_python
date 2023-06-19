#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:35:42 2023

@author: nahidferdous
"""

# Initialize an empty list to store the numbers
numbers = []

# Ask the user to enter 10 numbers
for i in range(10):
    num = float(input(f"Enter a number {i+1} of 10: "))
    numbers.append(num)

# Calculate the minimum, maximum, total, and average of the numbers
minimum = min(numbers)
maximum = max(numbers)
total = sum(numbers)
average = total / len(numbers)

# Print the results
print(f"The lowest number is {minimum}")
print(f"The highest number is {maximum}")
print(f"The total of the numbers is {total}")
print(f"The average of the numbers is {average}")
