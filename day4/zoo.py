# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:44:23 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
with open("zoo.csv")as zoo_csv:
    csv_reader = csv.reader(zoo_csv,delimiter=",")
    elephant = 0
    elephant_list = []
    tiger = 0
    tiger_list =[]
    lion = 0
    lion_list = []
    zebra = 0
    zebra_list = []
    kangaroo = 0
    kangaroo_list = []
    for row in csv_reader:
        print(row)
        if row[0]=="elephant":
            elephant = elephant+int(row[2])
            elephant_list.append(row[1])
        elif row[0]=="tiger":
            tiger = tiger+int(row[2])
            tiger_list.append(row[1])
        elif row[0]=="lion":
            lion = lion+int(row[2])
            lion_list.append(row[1])
        elif row[0]=="zebra":
            zebra = zebra+int(row[2])
            zebra_list.append(row[1])
        elif row[0]=="kangaroo":
            kangaroo = kangaroo+int(row[2])
            kangaroo_list.append(row[1])
        else:
            pass
    print("water by elephant :",elephant,elephant_list)
    print("water by tiger :",tiger,tiger_list)
    print("water by lion :",lion,lion_list)
    print("water by zebra :",zebra,zebra_list)
    print("water by kangaroo :",kangaroo,kangaroo_list)
    print("Total water needed to all animals : ",elephant+lion+tiger+zebra+kangaroo)        