# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:16:10 2019

@author: edoardottt
"""

# INCREASING SEQUENCES (FROM 1 TO 2N) PRINTER
S = [0, 0]


def stseq(n, i):
    if i == n:
        print(S)
    else:
        if i == 0 and n == 1:
            for j in range(1, (2 * n) + 1):
                S[i] = j
                stseq(n, i + 1)
        else:
            if i == 0:
                for j in range(1, (2 * n) + 1):
                    S[i] = j
                    stseq(n, i + 1)
            else:
                for j in range(1, (2 * n) + 1):
                    if S[i - 1] < j:
                        S[i] = j
                        stseq(n, i + 1)


stseq(2, 0)
