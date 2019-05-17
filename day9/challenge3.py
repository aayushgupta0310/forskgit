# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:01:58 2019

@author: User
"""

"""

Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""


from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://bidplus.gem.gov.in/bidlists"


a = []
b = []
c = []
d = []
e = []
f = []
browser = webdriver.Chrome("F:/forsk/chromedriver.exe")
browser.get(url)

sleep(2)

for i in range(1,11):
    a.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    b.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    c.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/strong').text)
    d.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]').text)
    e.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]').text)
    f.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]').text)


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()




import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://aayushgupta:aayushgupta%40123@cluster0-shard-00-00-cqkyd.mongodb.net:27017,cluster0-shard-00-01-cqkyd.mongodb.net:27017,cluster0-shard-00-02-cqkyd.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.employee

def add_student(a,b,c,d,e,f):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    for i in range(0,10):
        
        mydb.employees.insert_one(
            {
                 "BID NO":a[i],
                 "items":b[i],
                 "Quantity Required":c[i],
                 "Department Name And Address":d[i],
                 "Start date":e[i],
                 "End date":f[i]                 
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.employees.find()
    for i in user:
        print (i)

add_student(a,b,c,d,e,f)

fetch_all_student()
