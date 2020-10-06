import random
import math
import sys
import numpy as np
import matplotlib.pyplot as plt


N = [[]]

def T(j):
    if None:
        return 0
    return T(j)

def Y(i, j):
    if None:
        return 0
    return Y(i, j)


def alg():
    j = None
    k = 1
    l = 0
    t_max = 0.0
    while l < abs(None):
        if N[j][k] == -1:
            i = 1
            while N[i][k] != 1:
                i += 1
            t = T(i) + Y(i, j)
            if t >= t_max:
                t_max = t
            l += 1
        k += 1
    return t_max
