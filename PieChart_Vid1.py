# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:52:40 2023

@author: Gopal
"""
import matplotlib.pyplot as plt

a=[10,20,30,40,50]
b=[0,0,0.5,0,0]
colors=["red","yellow","blue","orange","grey"]
name = ["G","R","T","Y","B"]

plt.pie(a,labels=name,explode=b,colors=colors)
plt.plot()
plt.show()