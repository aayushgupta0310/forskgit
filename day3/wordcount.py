# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:16:42 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
set1 = 0
count2 = 0
count1 = 0
count = 0
file_name = input("Enter file name : ")
with open(file_name,'rt') as file1:
    for item in file1.readlines():
        count = count + len(item)
        count1 = count1 + len(item.split(" "))
        count2 = count2 + len(item.split("/n"))
        set1 = len(set(item.split(" "))) +set1
        
        
print(count)   
print(count1)
print(count2)  
print(set1)
print(count3)   