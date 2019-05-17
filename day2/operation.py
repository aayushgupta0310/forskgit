# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:07:25 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed    
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

def Add(list1):
    add  = 0
    for x in list1:
        add = add + int(x)
    return add
def Multiply(list1):
    mul = 1
    for x in list1:
        mul = mul * int(x)
    return mul
def Largest(list1):
    lar = list1[0]
    for x in list1:
        if(int(x)>int(lar)):
            lar=x
    return lar
def Smallest(list1):
    small = list1[0]
    for x in list1:
        if(int(x)<int(small)):
            small = x
    return small
        
def Sorting(list1):
    list1.sort()
    return list1
def Print(list1):
    print("Addition is: {}".format(Add(list1)))
    print("Multiply is: {}".format(Multiply(list1)))
    print("Largest is: {}".format(Largest(list1)))
    print("Smallest is: {}".format(Smallest(list1)))
    print("Sorted list is: {}".format(Sorting(list1)))


list1 = input("Enter values :").split(" ")
Print(list1)
    
