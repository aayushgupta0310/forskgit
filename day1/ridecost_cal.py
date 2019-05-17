# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:06:57 2019

@author: User
"""

dis=float(input("Total distance travelled to and fro : "))
dis = dis*2
cod=float(input("cost of diseal per liter : "))
vfa=float(input("vehicle fuel average  : "))
tavg = dis/vfa
cost = tavg*cod
print("cost of driving per day is:{}".format(cost))
