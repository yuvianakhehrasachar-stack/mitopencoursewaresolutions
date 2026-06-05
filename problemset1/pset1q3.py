#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:04:39 2026

@author: yuvianasachar
"""

annualsalary=10000
monthlysalary=10000/12
r=0.04
sar=0.07
costofhouse=int(input("What is the cost of your dreammmm house"))
downpayment=costofhouse*0.25
bestrate=None

low=0
high=10000

while low<=high:
    mid=(low+high)//2
    portion_saved=mid/10000
    current_savings=0
    months=0
    salary=annualsalary
    monthlysalary=annualsalary/12
    
    while months<36:
        current_savings+=monthlysalary*portion_saved
        current_savings+=current_savings*r/12
        
        months+=1
        
        if  months %6==0:
            salary*=(1+sar)
            monthlysalary=salary/12
    
        
    if abs(current_savings-downpayment)<=100:
          bestrate=portion_saved
          break
            
    elif current_savings<downpayment:
            
            low=mid+1
        
    else: 
            high=mid-1
        
if bestrate is None:
            
    print("Not possible")
            
else: print("Best rate is",bestrate)
            
            
        
    
        
        

        
        
        
        
    
