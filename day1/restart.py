# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:52:39 2019

@author: User
"""
str1 = input("Enter any String : ")
b = str1.split('R',1)
c = b[1].replace("R","$")
print(b[0]+"R"+c)