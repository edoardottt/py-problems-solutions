# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:56:02 2019

@author: edoardottt
"""

# BACK-TRACKING PRINT STRINGS WITH BLOCKS OF EVEN-NUMBERED 'A' AND 'B'
print("BACK-TRACKING PRINT STRINGS WITH BLOCKS OF EVEN-NUMBERED 'A' AND 'B'")
M = [0, 0, 0, 0, 0, 0]


def apari(n, i):
    if i == n:
        print(M)
    else:
        if i + 1 < n:
            M[i] = "a"
            M[i + 1] = "a"
            apari(n, i + 2)
            M[i] = "b"
            M[i + 1] = "b"
            apari(n, i + 2)


apari(6, 0)
