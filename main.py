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

def T(j):
    # print(j+1)
    global pathList
    global P
    global bestMax
    k = 0
    l = 0
    t_max = 0.0
    while l < len(Beta[j]):
        if N[j][k] < 0.0:
            i = 0
            while N[i][k] <= 0.0:
                i += 1
            prevWeight, listNodes = T(i)
            listNodes.append(i+1)
            t = prevWeight + abs(N[i][k])*random.random()*2
            # print(j+1,"->",i+1," Weight: ",t)
            if i+1 == 1:
            	P = [1]
            else:
            	P.append(i+1)
            if t >= t_max:
                t_max = t
                listNodesMax = listNodes
            if (j==terminalNode):
                if bestMax < t_max:
                    bestMax = t_max
                    pathList = [P]
                elif bestMax == t_max:
                    pathList.append(P)
            l += 1
        k += 1
    t_tab[j] = t_max
    if j==0:
        return t_max, []
    return t_max, listNodesMax

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
        if max_node == 0:
            return path
        else:
            path += ","
        j = max_node


def createMatrix(fileName):
    data = open(fileName)
    largestNum = 0
    numLines = 0
    n = []
    for lt in [line.split() for line in data]:
        source = int(lt[0])
        dest = int(lt[1])
        try:
            weight = int(lt[2])
        except:
            weight = float(lt[2])
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
        weight = float(lt[2])
        n[source - 1][count] = 1 * weight
        n[dest - 1][count] = -1 * weight
        count += 1
    return n




def write_output(filename, results):
    with open(filename, 'w') as f:
        for r, v in results.items():
            string = 'OUTPUT\t:'
            string += r[:-1]
            string += ':\t' + str(v/n)
            path_str = ""
            for i in range(len(r)):
                if i % 2 == 0:
                    if i + 2 >= len(r):
                        break
                    path_str += f"a{r[i]}/{r[i+2]},"
            print("OUTPUT\t\t:"+"{:25}".format(path_str[:-1]+":")+"{:e}".format(v/n))
            f.write("OUTPUT\t\t:"+"{:25}".format(path_str[:-1]+":")+"{:e}\n".format(v/n))


def runSimulation(n):
    global pathList, bestMax, P
    dic = {}
    for i in range(n):
        P = []
        bestMax = 0
        pathList = []
        weight, nodeList = T(terminalNode)
        nodeList.append(terminalNode+1)
        # print(weight)
        # print(nodeList)
        for pl in pathList:
            pl.append(terminalNode+1)
            pl = nodeList
        for pl in pathList:
            path_string = ""
            for c in pl:
                path_string = path_string + str(c) + ","
            if (path_string not in dic.keys()):
                dic[path_string] = 1
            else:
                dic[path_string] = dic[path_string]+1
    '''for k, c in dic.items():
        print(k," : ","{:e}".format(c/n))'''
    write_output('resultsTest.txt', dic)


def runProgram(uniformFileName, repNum, txtFileName):
    global N,Beta,t_tab,terminalNode,n
    uniforms = open(uniformFileName)
    N = createMatrix(txtFileName)
    Beta = make_Beta()
    t_tab = [None for i in range(len(N))]
    t_tab[0] = 0.0
    terminalNode = len(N)-1
    n = int(repNum)
    runSimulation(n)
