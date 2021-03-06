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
    global P, nextRandom
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
            t = prevWeight + abs(N_R[i][k])
            if t >= t_max:
                t_max = t
                listNodesMax = listNodes
            if (j==terminalNode):
                newL = [t,listNodes]
                P.append(newL)
            l += 1
        k += 1
    t_tab[j] = t_max
    if j==0:
        return t_max, []
    return t_max, listNodesMax

# Takes the .net file and creates an n*m matrix. 

def createMatrix(fileName):
    try:
        data = open(fileName)
    except:
        print("Description File not found")
        exit(1)
    largestNum = 0
    numLines = 0
    n = []
    for lt in [line.split() for line in data]:
        source = int(lt[0])
        dest = int(lt[1])
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
            rs = r.split(',')
            for i in range(len(rs)):
                if i == len(rs)-2:
                    break
                path_str += f"a{rs[i]}/{rs[i+1]},"
            print("OUTPUT\t\t:"+"{:25}".format(path_str[:-1]+": ")+"{:.5e}".format(v/n))
            f.write("OUTPUT\t\t:"+"{:25}".format(path_str[:-1]+": ")+"{:.5e}\n".format(v/n))


def runSimulation(n,N):
    global nextRandom, P, N_R, allPaths
    dic = {}
    for path in allPaths:
        path_string = ""
        for c in path:
            c += 1
            path_string = path_string + str(c) + ","
        if (path_string not in dic.keys()):
            dic[path_string] = 0
    print(len(dic))
    print(len(allPaths))
    for i in range(n):
        N_R = randomizedN(N)
        P = []
        weight, nodeList = T(terminalNode)
        for z in P:
            if z[0]==weight:
                nodeList = z[1]
                nodeList.append(terminalNode+1)
                path_string = ""
                for c in nodeList:
                    path_string = path_string + str(c) + ","
                if (path_string not in dic.keys()):
                    dic[path_string] = 1
                else:
                    dic[path_string] = dic[path_string]+1
    write_output('resultsTest.txt', dic)
    print(dic)
    
def getRandom():
    global uniforms
    line = uniforms.readline()
    try:
        return float(line)
    except:
        print("Random Uniform was not found.")
        exit(1)

def runProgram(uniformFileName, repNum, txtFileName):
    global N,Beta,t_tab,terminalNode,n,uniforms, allPaths
    allPaths = []
    try:
        uniforms = open(uniformFileName,"r")
    except:
        print("Random File not found")
        exit(1)
    N = createMatrix(txtFileName)
    Beta = make_Beta()
    t_tab = [None for i in range(len(N))]
    t_tab[0] = 0.0
    terminalNode = len(N)-1

    find_paths(0, len(N)-1, [], [False]*len(N))
    # find_paths2(0,[])

    n = int(repNum)
    runSimulation(n,N)

def randomizedN(N):
    N_Random = [[e for e in s] for s in N]
    for col in range(len(N_Random[0])):
        x = getRandom()
        for row in range(len(N_Random)):
            N_Random[row][col] = N_Random[row][col] * x
    return N_Random

def find_paths(node, dest, path, visited):
    global allPaths
    visited[node] = True
    path.append(node)
    if node == dest:
        path.append(dest)
        allPaths.append(path)
    else:
        for i in range(len(N)):
            if node in Beta[i] and not visited[i]:
                find_paths(i, dest, [e for e in path], visited)
    path.pop()
    visited[node] = False

def find_paths2(j, pathList):
    global allPaths, terminalNode
    pathList.append(j+1)
    for col in range(len(N[j])):
        if N[j][col] > 0:
            for row in range(len(N)):
                if N[row][col] < 0:
                    if row==terminalNode:
                        pathList.append(row+1)
                        allPaths.append(pathList)
                        print("Path found, ",pathList)
                    else:
                        find_paths2(row, pathList)
