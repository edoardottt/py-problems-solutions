# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:09:57 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT PERMUTATIONS WITHOUT ODD AND EVEN NUMBER ADJACENT
print("BACK-TRACKING PRINT PERMUTATIONS WITHOUT ODD AND EVEN NUMBER ADJACENT")

X = [1,2,3,4]
PRESO = [0,0,0,0]
M = [0,0,0,0]
# PRESO = array that stores the values taken yet

def perma(n,i):
    if(i==n):
        print(M)
    else:
        if(i==0): # first value so I can put into first value of result anything
            for x in range(n):
                M[i] = X[x]
                PRESO[x] = 1
                perma(n,i+1)
                PRESO[x] = 0
        else:
            for j in range(n):
                if( M[i-1]%2==0 ): # if the precedent value is even
                    if(PRESO[j]==0): # if I have not already entered it
                        if(X[j]%2==1): # if the value is odd
                            M[i] = X[j]
                            PRESO[j] = 1
                            perma(n,i+1)
                            PRESO[j] = 0
                else:       # if odd
                    if(PRESO[j]==0): # if I have not already entered it
                        if(X[j]%2==0): # if the value is even
                            M[i] = X[j]
                            PRESO[j] = 1
                            perma(n,i+1)
                            PRESO[j] = 0
perma(4,0) 