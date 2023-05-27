#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 02:22:31 2023

@author: nahidferdous
"""
def salary(sell,commision1,adv_pay):
    
    pay= (sell*commision1)-adv_pay
    
    
    return pay


def commisions(sell):
    if sell < 10000:
        commision= 10/100
    elif sell >= 10000 and sell <= 14999:
        commision= 12/100
    elif sell >= 15000 and sell <= 17999:
        commision= 14/100
    elif sell >= 18000 and sell <= 21999:
        commision= 16/100
    elif sell >= 22000 :
        commision= 18/100
    
    return commision
        
        
def main():
    
    Total_sell= int (input("Whats your total sell in this month: "))
    Adv_ammount= int(input("How mauch you get in advance: "))
    
    
    print( " ------- Your final salary is :  -------  \n ")
    
    if salary(Total_sell, commisions(Total_sell), Adv_ammount)>=0: 
        print(f"You salary is {salary(Total_sell, commisions(Total_sell), Adv_ammount)} \n ---- You dont have any due ---- ")
    else: 
        print(" ------ You dont have any salaty ------")
        print("---- You need to pay your due ----")
        print(f"--- your due is {abs(salary(Total_sell, commisions(Total_sell), Adv_ammount))}")
        
main()
    
    


