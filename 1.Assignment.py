#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:50:02 2023

@author: nahidferdous
"""

def h_m_S_calculetion (seconds):
    hours_1 =seconds/(60*60)
    hours= int(hours_1)
    
    minutes_1=(seconds - (hours* 3600))/60
    minutes= int(minutes_1)
    
    second= (minutes_1*60 - minutes*60) 
    
    return hours, minutes, second

def main():
    seconds= float(input("Enter a number of seconds : "))
    x,y,z= h_m_S_calculetion (seconds)
    print("Here is the time in Hours, Minutes, and Seconds:")
    print("Hours:", format(x,".1f"))
    print("Minutes:", format(y,".1f"))
    print("Seconds:", format(z,".1f"))

main()