# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:31:40 2019

@author: User
"""

"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""
import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://aayushgupta:aayushgupta%40123@cluster0-shard-00-00-cqkyd.mongodb.net:27017,cluster0-shard-00-01-cqkyd.mongodb.net:27017,cluster0-shard-00-02-cqkyd.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.employee

def add_student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.employees.insert_one(
            {
            "name" : Student_Name,
            "age" : Student_Age,
            "roll_no" : Student_Roll_no,
            "branch" : Student_Branch
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.employees.find()
    for i in user:
        print (i)

add_student('aayush',20,1,'cse')
add_student('aakash',20,11,'me')
add_student('saurabh',20,2,'ee')
add_student('dhruvin',20,13,'cse')
add_student('bhavya',20,12,'IT')

fetch_all_student()