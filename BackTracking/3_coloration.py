# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:07:01 2019

@author: edoardottt
"""

# 3-COLORATION
cols = ["r", "g", "b"]
S = ["-" for i in range(4)]


def col(n, i):
    if n == i:
        print(S)
    elif i == 0:
        for j in range(3):
            S[i] = cols[j]
            col(n, i + 1)
    else:
        for j in range(3):
            if S[i - 1] != cols[j]:
                S[i] = cols[j]
                col(n, i + 1)


col(4, 0)
