import random
import math
import sys
import numpy as np
import matplotlib.pyplot as plt


N = [[]]    # rows=nodes, cols=arcs
Beta = {}
Beta[2] = set()


def T(j):
    if None:
        return 0
    return T(j)

def Y(i, j):
    if None:
        return 0
    return Y(i, j)


def alg(j):
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


def write_output(filename, results):
    with open(filename, 'w') as f:
        for result in results:
            string = 'OUTPUT\t:'
            for arc in result[0]:
                string += arc + ','
            string = string[:-1]
            string += '\t' + str(result[1])
            f.write(f'{string:>10}\n')
