# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:11:41 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  

"""
def reverse_str(str1) :
    s1=' '
    for x in str1:
        s1 = x+s1
        
    return s1
    
str1 = input("Enter your string : ")
print(str1)
reverse_str(str1)


    
