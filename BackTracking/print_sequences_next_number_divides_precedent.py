# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:53:13 2019

@author: edoardottt
"""

# BACK-TRACKING PRINT SEQUENCES WITH NEXT NUMBER THAT DIVIDES THE PRECEDENT AND VALUES 1<= I <= M
print(
    "BACK-TRACKING PRINT SEQUENCES WITH NEXT NUMBER THAT DIVIDES THE PRECEDENT AND VALUES 1<= I <= M"
)


M = [0, 0, 0]


def seqlec(n, i, m):
    if i == n:
        print(M)
    else:
        if i == 0:
            for j in range(1, m + 1):
                M[i] = j
                seqlec(n, i + 1, m)
        else:
            for j in range(1, m + 1):
                if M[i - 1] % j == 0:
                    M[i] = j
                    seqlec(n, i + 1, m)


seqlec(3, 0, 4)
