# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:06:57 2019

@author: User
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
input_new = input("Enter numbers : ").split(",")
new_tuple = tuple(input_new)
print(input_new)
print(new_tuple)