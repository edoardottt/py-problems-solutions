# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:15:00 2019

@author: edoardottt
"""

# BACK-TRACKING PRINT MATRICES WITHOUT '1' VALUE ADJACENT
print("BACK-TRACKING PRINT MATRICES WITHOUT '1' VALUE ADJACENT")
# i = row index
# j = col index
M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def matrice(n, i, j):
    if i == n:  # if I finish the rows, print it
        print(M)
    elif j == n:  # instead, if I finish a row, new line
        i = i + 1
        j = 0
        matrice(n, i, j)
    elif i == 0 and j == 0:  # first cell
        M[i][j] = 1
        matrice(n, i, j + 1)
        M[i][j] = 0
        matrice(n, i, j + 1)
    elif i == 0:  # first row
        if M[0][j - 1] == 0:  # check if the precedent on the same row is 0
            M[i][j] = 1
            matrice(n, i, j + 1)
            M[i][j] = 0
            matrice(n, i, j + 1)
        else:
            M[i][j] = 0
            matrice(n, i, j + 1)
    elif j == 0:  # first column
        if (
            M[i - 1][j] == 0 and M[i - 1][j + 1] == 0
        ):  # check if the adjacents inserted yet are equal to 0
            M[i][j] = 1
            matrice(n, i, j + 1)
            M[i][j] = 0
            matrice(n, i, j + 1)
        else:
            M[i][j] = 0
            matrice(n, i, j + 1)
    elif j == n - 1:  # last column
        if (
            M[i][j - 1] == 0 and M[i - 1][j - 1] == 0 and M[i - 1][j] == 0
        ):  # check if the adjacents inserted yet are equal to 0
            M[i][j] = 1
            matrice(n, i, j + 1)
            M[i][j] = 0
            matrice(n, i, j + 1)
        else:
            M[i][j] = 0
            matrice(n, i, j + 1)
    else:  # else, I'm in the middle of matrix
        if (
            M[i][j - 1] == 0
            and M[i - 1][j - 1] == 0
            and M[i - 1][j] == 0
            and M[i - 1][j + 1] == 0
        ):  # check if the adjacents inserted yet are equal to 0
            M[i][j] = 1
            matrice(n, i, j + 1)
            M[i][j] = 0
            matrice(n, i, j + 1)
        else:
            M[i][j] = 0
            matrice(n, i, j + 1)


matrice(3, 0, 0)
