#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:10:51 2023

@author: nahidferdous
"""

import car as c 
import account as ac

def main():
    
    while True:
        
        select= input("What you want to select, Car or Bookstore : ")
        if select == "car":
            make= input("Enter the car company name: ")
            model= input("Enter the car Model name: ")
            horse_power= input("Enter the car horse_power : ")
            p=c.Car(make, model, horse_power)
            p.prints()
        elif select=="bookstore":
            bal= int(input("Enter your account balance : "))
            p1=ac.Account(bal)
            add= int(input("Add money : "))
            p1.add_money(add)
            cash=int(input("How much you want to cash"))
            p1.cash_money(cash)
            p1.print_bal()
        
        x= input("yes or no")
        if x== "no":
            break
       
main()