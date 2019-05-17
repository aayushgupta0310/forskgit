# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:18:39 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
output=[]
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowel = list('aeiou')
for x in range(0,len(state_name)):
    list2 = list(state_name[x].lower())
    for i in list2:
        if i in vowel:
            list2.remove(i)
    output.append("".join(list2))
print(output)    
        