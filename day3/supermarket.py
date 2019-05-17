# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:25:14 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
item_dic = { }
while True:
    item_input=input("Enter the item_name and net_price :").lower()
    if item_input == "exit":
        for product, price in item_dic.keys,item_dic.values :
            print(product,price)
        break
    else:
        item_detail=item_input.split(" ")
        if len(item_detail)==2:
            if item_detail[0] not in item_dic:
                item_dic[item_detail[0]]=int(item_detail[1])
            else:
                item_dic[item_detail[0]]=item_dic[item_detail[0]]+int(item_detail[1])
        else:
            if item_detail[0]+" "+item_detail[1] not in item_dic:
                item_dic[item_detail[0]+" "+item_detail[1]]=int(item_detail[2])
            else:
                item_dic[item_detail[0]+" "+item_detail[1]]=item_dic[item_detail[0]+" "+item_detail[1]]+int(item_detail[2])
                
                
        
