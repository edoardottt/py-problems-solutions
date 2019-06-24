# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:52:30 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT PERMUTATIONS
print("BACK-TRACKING PRINT PERMUTATIONS")

X = [0,1,2,3]
PRESO = [0,0,0,0]
M = [0,0,0,0]

def perm(n,i):
    if(i==n):
        print(M)
    else:
        for j in range(n):
            if(PRESO[j]==0):
                M[i] = X[j]
                PRESO[j] = 1
                perm(n,i+1)
                PRESO[j]=0
                
perm(4,0)