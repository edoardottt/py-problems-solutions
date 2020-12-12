# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:18:44 2019

@author: edoardottt
"""

# SEQUENCES WITH DISTINGUISHED NUMBERS (FROM 1 TO 2N) PRINTER
S = [0, 0]


def stseqd(n, i):
    if i == n:
        print(S)
    else:
        if i == 0:
            for j in range(1, (2 * n) + 1):
                S[i] = j
                stseqd(n, i + 1)
        else:
            for j in range(1, (2 * n) + 1):
                if S[i - 1] != j:
                    S[i] = j
                    stseqd(n, i + 1)


stseqd(2, 0)
