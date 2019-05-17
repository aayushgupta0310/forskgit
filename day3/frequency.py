# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:10:55 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
str1 = input("Enter a string : ")
dic1 = {}
for i in str1:
    if i in dic1:
        dic1[i]=dic1[i]+1
    else:
        dic1[i]=1
print(dic1)