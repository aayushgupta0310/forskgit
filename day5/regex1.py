# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:41:40 2019

@author: User
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re
str1 = input("Enter your String: ").split(" ")
str(str1)
for val in str1:
    if re.findall(r'[+-.]?[0-9]\.[0-9]+',val):
        print('True')
    else:
        print('False')