# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:03:25 2019

@author: edoardottt
"""

# STRINGS COUNT (LENGTH = N) WITHOUT TWO CONSECUTIVES ZERO
print("Dynamic Programming - STRINGS COUNT (LENGTH = N) WITHOUT TWO CONSECUTIVES ZERO")


def es(n, k):

    T = [0 for i in range(n + 1)]

    T[1] = k

    T[2] = (k ** 2) - 1

    for i in range(3, n + 1):

        T[i] = (k - 1) * (T[i - 1] + T[i - 2])

    print(T[n])


es(3, 3)
