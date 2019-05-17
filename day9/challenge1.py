# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:09:14 2019

@author: User
"""


"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
conn = sqlite3.connect ( 'student.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO students VALUES ('aayush',20,1,'cse')")
c.execute("INSERT INTO students VALUES ('aakash',20,11,'me')")
c.execute("INSERT INTO students VALUES ('saurabh',20,2,'ee')")
c.execute("INSERT INTO students VALUES ('dhruvin',20,13,'cse')")
c.execute("INSERT INTO students VALUES ('bhavya',20,12,'IT')")


# STEP 3
c.execute("SELECT * FROM students")
# "SELECT * FROM employees WHERE last = 'Fernandes' "

# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")



