# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:53:00 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
list1 = input("Enter 3 values for small bricks , big bricks and target value : ").split(" ")
print(list1)
a = list1[0]
b = list1[1]
c = list1[2]
total = int(a)*1 + int(b)*5
if(total >= int(c)):
    print("TRUE")
else:
    print("FALSE")    