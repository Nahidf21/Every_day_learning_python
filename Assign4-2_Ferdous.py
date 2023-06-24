#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 02:55:10 2023

@author: nahidferdous
"""

import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Display the first five observations
print(titanic.head())

import matplotlib.pyplot as plt

# Group by class, embarked town and survived or not
grouped = titanic.groupby(['class', 'embark_town', 'survived']).size().reset_index(name='counts')


plt.figure(figsize=(10,6))
sns.barplot(x='class', y='counts', hue='embark_town', data=grouped[grouped['survived'] == 1])
plt.title('Survivors by Class and Embarked Town')
plt.show()


# Load Iris dataset
iris = sns.load_dataset('iris')

# Display pairwise relationships
sns.pairplot(iris)
plt.show()

# Display pairwise relationships with different plots for diagonal and non-diagonal comparisons
sns.pairplot(iris, diag_kind='hist',  kind='reg')
plt.show()
