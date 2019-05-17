# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:07:13 2019

@author: User
"""


"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
str1 = input("Enter city name:")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+str1
url3 = "&appid=53c3c30bc51ed9dfd9147481c9916411"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content
jsondata = response.json()
print(jsondata)

print("longitude: ",jsondata['coord']['lon'])
print("latitude:",jsondata['coord']['lat'])
print("weather: ",jsondata['weather'][0]['description'])
print("wind speed :",jsondata['wind']['speed'])
print("sunrise: ",jsondata['sys']['sunrise'])
print("sunset:",jsondata['sys']['sunset'])