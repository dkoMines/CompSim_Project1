import random
import math
import sys


# import numpy as np
# import matplotlib.pyplot as plt


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


def T(j):
    k = 0
    l = 0
    t_max = 0.0
    i_max = None
    while l < len(Beta[j]):
        if N[j][k] < 0:
            i = 0
            while N[i][k] < 1:
                i += 1
            if t_tab[i] is None:
                t_i = T(i)
                t_tab[i] = t_i
            t = t_tab[i] + abs(N[i][k])
            if t >= t_max:
                t_max = t
                i_max = i
            l += 1
        k += 1
    print(j, i_max)
    return t_max


def max_beta(j):
    b = sorted([(t_tab[c], c) for c in Beta[j]])
    return b[-1][1]


def find_path(j):
    path = [j]
    while True:
        max_node = max_beta(j)
        path.append(max_node)
        if max_node == 0:
            return path
        j = max_node


def createMatrix(fileName):
    data = open(fileName)
    largestNum = 0
    numLines = 0
    n = []
    for lt in [line.split() for line in data]:
        source = int(lt[0])
        dest = int(lt[1])
        weight = int(lt[2])
        numLines += 1
        if largestNum < dest:
            largestNum = dest
    for i in range(largestNum):
        l = []
        for j in range(numLines):
            l.append(0)
        n.append(l)
    count = 0
    data = open(fileName)
    for lt in [line.split() for line in data]:
        source = int(lt[0])
        dest = int(lt[1])
        weight = int(lt[2])
        n[source - 1][count] = 1 * weight
        n[dest - 1][count] = -1 * weight
        count += 1
    return n


def write_output(filename, results):
    with open(filename, 'w') as f:
        for result in results:
            string = 'OUTPUT\t:'
            for arc in result[0]:
                string += arc + ','
            string = string[:-1] + ':'
            string += '\t' + str(result[1])
            f.write(f'{string:>10}\n')


N = createMatrix("san-leemis79.net")
Beta = make_Beta()
t_tab = [None for i in range(len(N))]
t_tab[0] = 0.0


def main():
    print(T(5))
    print(t_tab)
    print(find_path(5))


if __name__ == '__main__':
    main()
