# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:22:23 2019

@author: User
"""

ass1 = int(input("Enter assigment 1 marks : "))
ass2 = int(input("Enter assigment 2 marks : "))
ass3 = int(input("Enter assigment 3 marks : "))
exam1 = int(input("Enter exam 1 marks : "))
exam2 = int(input("Enter exam 2 marks : "))
ws = (ass1+ass2+ass3) *0.1 + (exam1+exam2) *0.35
print("weighted score is {} ".format(ws))