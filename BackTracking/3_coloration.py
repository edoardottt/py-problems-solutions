# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:07:01 2019

@author: edoardottt
"""

# 3-COLORATION
S=[0 for i in range(4)];
def col(n,i):
    if (n==i):
        print(S);
    else:
        S[i]='r';
        col(n,i+1);
        S[i]='g';
        col(n,i+1);
        S[i]='b';
        col(n,i+1);
        
col(4,0)