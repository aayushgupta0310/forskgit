# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:36:32 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
n = int(input("Enter any number : "))
for i in range(0,n+1):
    print ('*' * i)
for j in range(n-1,0,-1):
    print('*'*j)