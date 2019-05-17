# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:13:14 2019

@author: User
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
list1 = ('Monday', 'Wednesday', 'Thursday', 'Saturday')
list2 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
list1 = list(list1)
list2 = list(list2)
for day in list2:
    if day not in list1:
        list1.append(day)
print(list1)
        