# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:07:32 2019

@author: User
"""
import random
i = int(input("Enter any number between 1 - 10 : "))
r = random.randint(1,10)

if(i==r):
    print("player wins and computer lose")
else:
    print("player lose and computer wins")
