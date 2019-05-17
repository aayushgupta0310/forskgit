# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:27:35 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
str1 = input("Enter a string : ")
output_directory = {'Digits':0,'Letters':0}
for x in str1:
    if x.isdigit()==True:
        output_directory['Digits']+=1
    elif x.isalpha()==True:
        output_directory['Letters']+=1
    else:
        continue
print(output_directory)