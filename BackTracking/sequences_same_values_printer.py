# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:22:08 2019

@author: edoardottt
"""

#SEQUENCES (LENGTH = N WITH ONLY SAME VALUES) PRINTER
T=[3,1,9,9,3]
S=[0,0,0,0,0]
def st_sott(n,i,x):
    if(i==n):
        print(S)
    else:
        if(T[i]==T[x]):
            S[i]=T[x]
            st_sott(n,i+1,x)
            x=x+1
            S[i]='-'
            st_sott(n,i+1,x)
            x=x+1
        else:
            S[i]='-'
            st_sott(n,i+1,x)
            x=x+1
st_sott(5,0,0)