#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 03:30:03 2023

@author: nahidferdous
"""

class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, hourly_rate):
        Employee.__init__(self,name, id_number)
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate
        self.shift_type = "Day Shift" if shift_number == 1 else "Night Shift" if shift_number == 2 else "Invalid Shift"

    def display_info(self):
        print("\nProduction Worker Information:")
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Shift: {self.shift_type}")
        print(f"Hourly Pay Rate: $ {self.hourly_rate:.2f}")

def main():
    name = input("Enter your name: ")
    id_number = int(input("Enter your ID number: "))
    shift_number = int(input("Enter the shift number: "))
    hourly_rate = float(input("Enter your hourly rate: "))
    
    worker = ProductionWorker(name, id_number, shift_number, hourly_rate)
    worker.display_info()

main()
