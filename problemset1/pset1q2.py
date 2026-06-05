#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:18:42 2026

@author: yuvianasachar
"""

#questions
total_cost=float(input('What is the cost of your dream home?'))
annual_salary=float(input('What is your annual salary?'))
portion_saved=float(input('How much of your monthly salary do you wish to save for a down payment (please enter in decimal form)?'))
semirate=float(input("semi annual rate pls"))

#variables
r=float(0.04)
monthly_salary=float(annual_salary/12)
monthly_saving=float(monthly_salary*portion_saved)
current_savings=0
portion_down_payment=float((total_cost)*0.25)
months=float(0)


while current_savings<portion_down_payment:
    current_savings+=current_savings*r/12
    current_savings+=monthly_saving
    months+=1
    
    if months %6==0 and months !=0:
        annual_salary*=(1+semirate)
        monthly_salary = annual_salary / 12
        monthly_saving = monthly_salary * portion_saved
       

print(months)   
 
    






    
        
    
 
 