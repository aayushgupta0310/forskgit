# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:50:50 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

list1 = input("Enter values :").split(" ")
list1.sort()
a = len(list1)
print(a)
print(int(list1[a-1]))
sum = 0
if(a<3):
    print("Enter 3 or more than 3 values")
else:
    for x in range(int(list1[1]),int(list1[a-1])):
        print(x)
        sum = int(x) + sum
    print(sum)
        
        
