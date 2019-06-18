# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:07:40 2019

@author: edoardottt
"""

# PERMUTATIONS PRINTER
S=[0,0,0,0,0];
PRESO=[0,0,0,0,0];
def perm(n,i):
    if (i==n):
        print(S);
    for j in range(4):
        if (PRESO[j]==0):
            S[i]=j;
            PRESO[j]=1;
            perm(n,i+1);
            PRESO[j]=0;
                
perm(4,0)