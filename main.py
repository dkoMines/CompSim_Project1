import random
import math
import sys
#import numpy as np
#import matplotlib.pyplot as plt


def make_Beta():
    b = {}
    for i in range(len(N)):
        immediate_nodes = []
        for j in range(len(N[i])):
            val = N[i][j]
            if val < 0:
                for k in range(len(N)):
                    if abs(val) == N[k][j]:
                        immediate_nodes.append(k)
        b[i] = set(immediate_nodes)
    return b


def has_negative(ls):
    for element in ls:
        if element < 0:
            return True
    return False


def T(j):
    if len(Beta[j]) == 0:
        return 0
    total_time = 0
    for node in Beta(j):
        total_time += abs(N[node][j]) + T(node)
    return total_time


def alg(j):
    k = 1
    l = 0
    t_max = 0.0
    while l < len(Beta[j]):
        if N[j][k] == -1:
            i = 1
            while N[i][k] != 1:
                i += 1
            t = T(i) + Y[i][j]
            if t >= t_max:
                t_max = t
            l += 1
        k += 1
    return t_max

