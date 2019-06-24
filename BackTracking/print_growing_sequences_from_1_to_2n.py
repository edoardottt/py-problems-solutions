# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:47:23 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT GROWING SEQUENCES WITH NUMBERS FROM 1 TO 2N
print("BACK-TRACKING PRINT GROWING SEQUENCES WITH NUMBERS FROM 1 TO 2N")
S=[0,0];
def esss(n,i):
    if(i==n):
        print(S)
    else:
        if(i==0):
            for j in range(1,(2*n)+1):
                S[i]=j
                esss(n,i+1)
        else:
            for j in range(1,(2*n)+1):
                if(S[i-1]<j):
                    S[i]=j
                    esss(n,i+1)
esss(2,0)