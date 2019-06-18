# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:20:45 2019

@author: edoardottt
"""

#NON-DECREASING SEQUENCES (LENGTH = N ) COUNTER
T=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
for i in range(1,4):
    T[0][i]=1
for i in range(10):
    T[i][0]=0
for i in range(10):
    T[i][1]=i+1
    for i in range(10):
        for j in range(1,4):
            T[i][j]=T[i-1][j]+T[i][j-1]