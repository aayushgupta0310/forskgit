# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:15:33 2019

@author: User
"""

"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
list1 = list(filter(lambda x:'height' in x,people))
list2 = dict(map(lambda x:x.values() ,list1))
dict_len = len(list2)
avg = reduce(lambda x,y:x+y,list2.values())
avg1 = avg/dict_len
print(avg1)