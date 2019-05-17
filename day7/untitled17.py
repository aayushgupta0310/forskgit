# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:40:13 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests
number = input("Enter amount in USD:")
response = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=5ceb3a3a354e2bde0d52")
response.content
jsondata = response.json()
print(number*jsondata['USD_INR'])