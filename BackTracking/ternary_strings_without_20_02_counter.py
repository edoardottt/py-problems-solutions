# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:14:07 2019

@author: edoardottt
"""

# TERNARY STRINGS(WITHOUT '02' AND '20') COUNTER
S = [0, 0, 0]


def conta(n, i):
    if i == n:
        print(S)
    else:
        if i == 0:
            S[i] = 0
            conta(n, i + 1)
            S[i] = 1
            conta(n, i + 1)
            S[i] = 2
            conta(n, i + 1)
        else:
            if S[i - 1] == 1:
                S[i] = 0
                conta(n, i + 1)
                S[i] = 1
                conta(n, i + 1)
                S[i] = 2
                conta(n, i + 1)
            else:
                if S[i - 1] == 2:
                    S[i] = 1
                    conta(n, i + 1)
                    S[i] = 2
                    conta(n, i + 1)
                else:
                    if S[i - 1] == 0:
                        S[i] = 1
                        conta(n, i + 1)
                        S[i] = 0
                        conta(n, i + 1)


conta(3, 0)
