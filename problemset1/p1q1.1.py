#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:06:01 2026

@author: yuvianasachar
"""

#Questions from User
yearly_salary=float(input("What is your yearly salary?"))
portion_saved=float(input("What portion of your monthly salary do you wish to save?"))
cost_of_dream_home=float(input('What is the cost of your dream home?'))

#Variables
amount_saved=float(0)
r=float(0.05)
down_payment=float(cost_of_dream_home*.25)
monthlysalary=float(yearly_salary/12)
month=int(0)




while amount_saved<down_payment:
    amount_saved+=amount_saved*0.05/12
    amount_saved+=portion_saved*monthlysalary
    
    month+=1
    
   
    
print(month)
   
    
