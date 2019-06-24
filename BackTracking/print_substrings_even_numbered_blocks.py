# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:50:28 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT SUBSTRINGS WITH EVEN-NUMBERED BLOCKS
print("BACK-TRACKINGPRINT SUBSTRINGS WITH EVEN-NUMBERED BLOCKS")
M = [0,0,0,0,0]

def apari(n,i):
    if(i==n):
        print(M)
    else:
        if(i+1<n):
            M[i] = 'a'
            M[i+1] = 'a'
            apari(n,i+2)
            M[i] = 'b'
            apari(n,i+1)
        else:
            M[i] = 'b'
            apari(n,i+1)
            
apari(5,0)