# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:24:00 2019

@author: edoardottt
"""

# NON_DECREASING SEQUENCES (WITH |1|<=|0|) PRINTER
S = [0, 1, 0, 1]
M = [0, 0, 0, 0]


def ess(n, i, k, j, p):
    if i == n:
        print(M)
    else:
        if S[i] == 1:
            if j + 1 <= k:
                M[i] = 1
                ess(n, i + 1, k, j + 1, False)
                M[i] = "-"
                ess(n, i + 1, k, j, True)
            else:
                M[i] = "-"
                ess(n, i + 1, k, j, True)
        else:
            if S[i] == 0:
                if p == True:
                    M[i] = 0
                    ess(n, i + 1, k + 1, j, True)
                    M[i] = "-"
                    ess(n, i + 1, k, j, True)
                else:
                    M[i] = "-"
                    ess(n, i + 1, k, j, True)


ess(4, 0, 0, 0, True)
