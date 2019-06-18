# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:06:04 2019

@author: edoardottt
"""

# BINARY STRINGS GENERATOR
S=[0 for i in range(4)];
def gen(n,i):
    
    if (n==i):
        print(S);
    else:
        S[i]=0;
        gen(n,i+1);
        S[i]=1;
        gen(n,i+1);

gen(4,0)