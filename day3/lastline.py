# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:38:09 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

file_name = input("Enter the file name : ")
with open(file_name,"rt") as file_open:
    content = file_open.readlines()
    print(content[-1])