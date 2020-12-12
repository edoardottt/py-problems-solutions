# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:00:39 2019

@author: edoardottt
"""

# DYNAMIC PROGRAMMING PRINT STRICTLY GROWING SUBSEQUENCE WITH MAX LENGTH
print("DYNAMIC PROGRAMMING PRINT STRICTLY GROWING SUBSEQUENCE WITH MAX LENGTH")
lista = [5, 1, 8, 4, 1, 8, 6, 3, 7, 3, 2]
T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# i = row index
# j = col index
def e(n):
    T[0] = 1
    for i in range(1, n):
        T[i] = 1
        actualmax = 1
        for j in range(1, i + 1):
            k = i - j
            if lista[k] < lista[i]:
                if T[k] + 1 > actualmax:
                    actualmax = T[k] + 1
        T[i] = actualmax
    print(max(T))
    print("list result values")
    b = max(T)
    for i in range(n):
        if T[i] == b:
            c = i
    print(lista[c])

    b = lista[c]
    maxx = max(T)
    c -= 1
    while c > 0:
        if lista[c] < b and T[c] == maxx - 1:
            maxx = T[c]

            print(lista[c])
        c -= 1


e(9)
