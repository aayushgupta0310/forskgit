# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:38:31 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""


lst1 = input("Enter numbers for list 1 : ").split(" ")
lst2 = input("Enter numbers for list 2 : ").split(" ")
set1 = set(lst1)
set2 = set(lst2)
set3 = set1.intersection(set2)
print(set3)