# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:53:19 2019

@author: User
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
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

import pandas as pd
from collections import OrderedDict

col_name = ["BID NO","items","Quantity Required","Department Name And Address","Start date","End date"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e,f]))
df = pd.DataFrame(col_data) 
df.to_csv("bid.csv")

