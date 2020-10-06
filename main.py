import random
import math
import sys
#import numpy as np
#import matplotlib.pyplot as plt


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
		n[source][count] = 1*weight
		n[dest][count] = -1*weight
		count += 1
	for i in n:
		print(i)





createMatrix("san-leemis79.net")
