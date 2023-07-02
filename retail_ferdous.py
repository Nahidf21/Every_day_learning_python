#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:32:00 2023

@author: nahidferdous
"""

class RetailItem:
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

    # getter methods
    def get_description(self):
        return self.description

    def get_units(self):
        return self.units

    def get_price(self):
        return self.price

    # setter methods
    def set_description(self, description):
        self.description = description

    def set_units(self, units):
        self.units = units

    def set_price(self, price):
        self.price = price
