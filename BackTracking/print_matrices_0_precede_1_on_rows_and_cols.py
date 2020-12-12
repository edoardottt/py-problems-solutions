# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:45:04 2019

@author: edoardottt
"""

# BACK-TRACKING MATRICES WITH 0 PRECEDE THAT THE 1s ON ROWS AND COLS
print("BACK-TRACKING MATRICES WITH 0 THAT PRECEDE THE 1s ON ROWS AND COLS")

R = [False, False]
C = [False, False]
M = [[0, 0], [0, 0]]


def es4(n, i, j, R, C, M):
    if j == n:
        i += 1
        j = 0
        es4(n, i, j, R, C, M)
    if i == n:
        print(M)
    else:

        if R[i] == False and C[j] == False:
            M[i][j] = 0
            es4(n, i, j + 1, R, C, M)

            M[i][j] = 1
            C[j] = True
            R[i] = True
            es4(n, i, j + 1, R, C, M)

        else:
            M[i][j] = 1
            C[j] = True
            R[i] = True
            es4(n, i, j + 1, R, C, M)


es4(2, 0, 0, R, C, M)
