#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:51:15 2023

@author: nahidferdous
"""

import retail_ferdous as bf

def main():
    prod1 = bf.RetailItem("Jacket", 12, "$249.99")
    prod2 = bf.RetailItem("Designer Jeans", 30, "$199.99")
    prod3 = bf.RetailItem("Shirt", 45, "$49.99")

    # Print out the data for each product
    for i, prod in enumerate([prod1, prod2, prod3], start=1):
        print(f"Product {i}:")
        print(f"Description: {prod.get_description()}")
        print(f"Units in inventory: {prod.get_units()}")
        print(f"Price: {prod.get_price()}")
        print()
        
if __name__ == "__main__":
    main()