# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:09:42 2019

@author: edoardottt
"""

# TERNARY STRINGS (LENGTH = N) WITHOUT ADJACENT EQUAL VALUES PRINTER
S=[0,0,0];
def printer(n,i):
    if(i==n):
        print(S)
    else:
        if(i==0):
            for j in range(3):
                S[i]=j
                printer(n,i+1)
        else:
            for j in range(3):
                if(S[i-1]!=j):
                    S[i]=j
                    printer(n,i+1)
printer(3,0)