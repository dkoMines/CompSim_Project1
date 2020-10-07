import random
import math
import sys


# import numpy as np
# import matplotlib.pyplot as plt

# Returns a dictionary of what leads to i node. 
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

<<<<<<< HEAD
# TODO:: Probably remove this.
def has_negative(ls):
    for element in ls:
        if element < 0:
            return True
    return False

=======
>>>>>>> 5b3e70ca9d3a451f5d589e80b5a22bbfeb7e9bf6

def T(j):
    k = 0
    l = 0
    t_max = 0.0
    while l < len(Beta[j]):
        if N[j][k] < 0:
            i = 0
            while N[i][k] < 1:
                i += 1
            t = T(i) + abs(N[i][k])
            if t >= t_max:
                t_max = t
            l += 1
        k += 1
    return t_max

# Takes the .net file and creates an n*m matrix. 
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


def main():
    print(T(5))


if __name__ == '__main__':
    main()
