# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:29:00 2019

@author: User
"""

"""

Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


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


right_table=soup.find('table', class_='table')


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




import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://aayushgupta:aayushgupta%40123@cluster0-shard-00-00-cqkyd.mongodb.net:27017,cluster0-shard-00-01-cqkyd.mongodb.net:27017,cluster0-shard-00-02-cqkyd.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.employee

def add_student(A,B,C,D):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    for i in range(0,4):
        
        mydb.employees.insert_one(
            {
                 "position":A[i],
                 "weighted matches":B[i],
                 "points":C[i],
                 "rating":D[i]            
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.employees.find()
    for i in user:
        print (i)

add_student(A,B,C,D)

fetch_all_student()
