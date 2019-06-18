# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:12:09 2019

@author: edoardottt
"""

#MATRICES (DIAGONAL = 0 && WITH COLONS = |1|<|0|) PRINTER
C=[0,0,0]
M=[[0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]]
def stmatr(n,i,j,C):
    if(j==n):
        j=0;i=i+1;
    if(i==n):
        print(M)
    else:
        if(i==j):
            M[i][j]=0
            stmatr(n,i,j+1,C)
        else:
            if((C[j]+1)<n-(C[j]+1)):
                M[i][j]=0
                stmatr(n,i,j+1,C)
                M[i][j]=1
                C[j]=C[j]+1
                stmatr(n,i,j+1,C)
                C[j]=C[j]-1
            else:
                M[i][j]=0
                stmatr(n,i,j+1,C)
stmatr(3,0,0,C)