# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:25:14 2019

@author: edoardottt
"""

# SEQUENCES (WITH ELEMENT 1 AT LEAST DISTANCE K) PRINTER
S = [0, 0, 0, 0, 0]


def sott(n, i, k, c, h):
    if i == n:
        print(S)
    else:
        if i == 0:
            S[i] = 0
            sott(n, i + 1, k, c, False)
            S[i] = 1
            sott(n, i + 1, k, c, True)
        else:
            if h == False:
                S[i] = 0
                sott(n, i + 1, k, c, False)
                S[i] = 1
                sott(n, i + 1, k, 0, True)
            else:
                if c < k:
                    S[i] = 0
                    sott(n, i + 1, k, c + 1, True)
                else:
                    S[i] = 0
                    sott(n, i + 1, k, c + 1, True)
                    S[i] = 1
                    sott(n, i + 1, k, 0, True)


sott(5, 0, 2, 0, False)
