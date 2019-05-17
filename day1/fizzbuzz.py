# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:42:34 2019

@author: User
"""
i=0
while(i<=100):
    i=i+1
    if(i%3==0  and i%5==0):
        print("fizzbuzz")
        continue
    elif(i%3==0):
        print("fizz")
        continue
    elif(i%5==0):
        print("buzz")
        continue
    print(i)
    
    
