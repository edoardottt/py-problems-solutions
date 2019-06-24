# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:49:38 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT NOT DECREASING TERNARY SUBSTRINGS 
print("BACK-TRACKING PRINT NOT DECREASING TERNARY SUBSTRINGS ")
X = [1,2,3,1,2,3]
M = [0,0,0,0,0,0]

def eserc(n,i,pu,pd,u,d,t):
    if(i==n):
        if(u and d and t):
            print(M)
    else:
        if(X[i]==1):
            if(pu):
                M[i] = 1
                eserc(n,i+1,True,True,True,d,t)
                M[i] = '-'
                eserc(n,i+1,pu,pd,u,d,t)
            else:
                M[i] = '-'
                eserc(n,i+1,False,pd,u,d,t)
        else:
            if(X[i]==2):
                if(pd):
                    M[i] = 2
                    eserc(n,i+1,False,True,u,True,t)
                    M[i] = '-'
                    eserc(n,i+1,False,pd,u,d,t)
                else:
                    M[i] = '-'
                    eserc(n,i+1,pu,pd,u,d,t)
            else:
                M[i] = 3
                eserc(n,i+1,False,False,u,d,True)
                M[i] = '-'
                eserc(n,i+1,pu,pd,u,d,t)
                
eserc(6,0,True,False,False,False,False)