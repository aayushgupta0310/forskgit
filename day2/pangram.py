# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:12:08 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
str1 = input("Enter the String : ")
str2 = ("abcdefghijklmnopqrstuvwxyz")
a = len(str1)
count =0 
if(a<26):
    print("it is not pangram")
else:
    for i in range(0,26):
        if str2[i] in str1:
            count = count+1
    if(count==26):
        print("it is pangram")
    else:
        print("not a pangram")

                
            
                



