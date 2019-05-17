# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:18:45 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
list1 = ()
dict1 = []
with open("romeo.txt","rt") as romeo:
    for line in romeo:
        list1 = line.split(" ")
       
        
