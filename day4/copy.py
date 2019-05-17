# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:08:01 2019

@author: User
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
with open ("aayush.txt", "rt") as rf :
  with open ("b.txt", "wt") as wf :
    for line in rf :
      wf.write ( line)