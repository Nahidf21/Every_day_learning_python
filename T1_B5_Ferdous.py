#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:53:31 2023

@author: nahidferdous
"""

# Print the tree branches
print(' ' * 12 + "★" )
for i in range(1, 12):
    print(' ' * (12 - i) + '*' * (2 * i + 1))

# Print the tree trunk
print(' ' * 8 + '| | | |')

# Print the tree base
for _ in range(4):
    print(' ' * 7 + "■■■■■■■■■■")