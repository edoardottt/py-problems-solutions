# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:08:31 2019

@author: edoardottt
"""

# k-SUBSET GENERATOR
S = [0, 1, 2, 3, 4]


def ksott(n, i, k, x):
    if i == n:
        print(S)
    if x >= k - n + i + 1:
        S[i] = 0
        ksott(n, i + 1, k, x)
    if x < k:
        S[i] = 1
        ksott(n, i + 1, k, x + 1)


ksott(5, 0, 3, 0)
