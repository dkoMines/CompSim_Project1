import random
import math
import sys
import numpy as np


# import matplotlib.pyplot as plt

# Returns a dictionary of what leads to i node. 
def make_Beta():
    b = {}
    for i in range(len(N_standard)):
        immediate_nodes = []
        for j in range(len(N_standard[i])):
            val = N_standard[i][j]
            if val < 0:
                for k in range(len(N_standard)):
                    if abs(val) == N_standard[k][j]:
                        immediate_nodes.append(k)
        b[i] = set(immediate_nodes)
    return b

def T(j):
    k = 0
    l = 0
    t_max = 0.0
    while l < len(Beta[j]):
        if N[j][k] < 0.0:
            i = 0
            while N[i][k] <= 0.0:
                i += 1
            if t_tab[i] is None:
                t_i = T(i)
                t_tab[i] = t_i
            t = t_tab[i] + abs(N[i][k])
            if t >= t_max:
                t_max = t
            l += 1
        k += 1
    t_tab[j] = t_max
    return t_max

# Takes the .net file and creates an n*m matrix. 
def max_beta(j):
    b = sorted([(t_tab[c], c) for c in Beta[j]])
    return b[-1][1]


def find_path(j):
    path = str(j+1)
    path += ","
    while True:
        max_node = max_beta(j)
        path += str(max_node+1)
        path += ","
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


def randomize_N(file_obj, _N):
    for i in range(len(_N)):
        for j in range(len(_N[i])):
            val = _N[i][j]
            if val < 0:
                for k in range(len(_N)):
                    if abs(val) == _N[k][j]:
                        rand = float(file_obj.readline())
                        val *= rand
                        _N[i][j] = val
                        _N[k][j] = -val
                        break


def write_output(filename, results):
    with open(filename, 'w') as f:
        for result in results:
            string = 'OUTPUT\t:'
            for arc in result[0]:
                string += arc + ','
            string = string[:-1] + ':'
            string += '\t' + str(result[1])
            f.write(f'{string:>10}\n')


# <<<<<<< HEAD
randoms = open('uniform-0-1-00.dat', 'r')
n = 30000
N_standard = createMatrix("san-leemis79.net")
target = len(N_standard) - 1
Beta = make_Beta()
paths_dict = {}
for i in range(7000):
    N = [[i for i in j] for j in N_standard]
    t_tab = [None for i in range(len(N))]
    t_tab[0] = 0.0
    randomize_N(randoms, N)

    t = T(target)
    path = find_path(target)
    path_str = path
    if path_str not in paths_dict.keys():
        paths_dict[path_str] = []
    paths_dict[path_str].append(t)
print('\n')
for k, v in paths_dict.items():
    print(k, len(v))
'''=======
N = createMatrix("san-leemis01.net")
Beta = make_Beta()
t_tab = [None for i in range(len(N))]
t_tab[0] = 0.0
terminalNode = len(N)-1


def runSimulation(n):
	dic = {}
	for i in range(n):
	    print("I = ", i)
	    print(T(terminalNode))
	    print(t_tab)
	    print(find_path(terminalNode))
	# 	T(terminalNode)
	# 	path_string = find_path(terminalNode)
	# 	if path_string not in dic.keys():
	# 		dic[path_string] = 1
	# 	else:
	# 		dic[path_string] = dic[path_string]+1
	# for k, c in dic.items():
	# 	print(k," : ",c)



def main():
    print(T(terminalNode))
    print(t_tab)
    print(find_path(terminalNode))
    # runSimulation(100000)



if __name__ == '__main__':
    main()
>>>>>>> 0ef447f0c73320c42dbe14f566cbf79974517125'''
