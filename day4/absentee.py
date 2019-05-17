# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:56:01 2019

@author: User
"""


"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

with open("new.txt","wt") as rf:
    counter = 25
    while True:
        list1 = input("Enter students name: ").split(" ")
        if counter==1 and list1=="  ":
            break
        else:
            for line in list1 :
                rf.write(line +"\n")
                counter -= 1
with open("new.txt","rt")as rt:
    print(rt.readlines())