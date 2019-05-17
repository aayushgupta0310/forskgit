# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:07:21 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

def f(x):
    return x==x[::-1] and x>0


list1 = input("Enter integers : ").split(" ")
y = list(filter(f,list1))
any(y)
