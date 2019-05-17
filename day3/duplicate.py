# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:43:39 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""
lst1 = input("Enter your list : ").split(" ")
set1 = set(lst1)
lst2 = list(set1)
print(lst2)