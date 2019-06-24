# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:48:30 2019

@author: edoardottt
"""

#BACK-TRACKING PRINT SUBSTRINGS NOT DECREASING WITH AT LEAST A ZERO AND A ONE
print("BACK-TRACKING PRINT SUBSTRINGS NOT DECREASING WITH AT LEAST A ZERO AND A ONE")

X=[0,1,0,1]
S=[0,0,0,0]
def ess3(n,i,z,u,p):
    if(i==n and z!=0 and u!=0):
        print(S)
    else:
        if(i<n):
            if(X[i]==0):
                if(p):
                    S[i]=0
                    ess3(n,i+1,z+1,u,True)
                    S[i]='-'
                    ess3(n,i+1,z,u,True)
                else:
                    S[i]='-'
                    ess3(n,i+1,z,u,p)
            else:
                if (z!=0):
                    S[i]=1
                    ess3(n,i+1,z,u+1,False)
                    S[i]='-'
                    ess3(n,i+1,z,u,p)
                else:
                    S[i]='-'
                    ess3(n,i+1,z,u,p)

ess3(4,0,0,0,True)