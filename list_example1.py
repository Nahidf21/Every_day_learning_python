#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 02:45:46 2023

@author: nahidferdous
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:42:46 2023

@author: nahidferdous
"""

name_data=[]

  
def print_name():
    print("Here are teh names you entered.\n")
    for name in name_data:
        print(name)
    
def main():
    q="y"
    while q=="y":
        name= input("Enter a name: ")
        name_data.append(name)
        q= input("Do you want to add another name? \n y=yes, anything else= no: n")
    print_name()
        
main()       
