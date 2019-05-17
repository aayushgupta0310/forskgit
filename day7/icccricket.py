# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:11:27 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())
right_table=soup.find('table', class_='table')

print (right_table)
source = requests.get(wiki).text


#Generate lists
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    
    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["position","weighted matches","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")