# Tanmay Sonawane CIS 360 Lab 09
# 12/04/24
# floyd algorithm

import numpy as np

def floyd(low, high, W, D, P):
    for i in range(low, high+1):
        for j in range(low, high+1):
            P[i][j] = -1
            D[i][j] = W[i][j]
            
    for k in range(low, high+1):
        for i in range(low, high+1):
            for j in range(low, high+1):
                newpath = D[i][k] + D[k][j]
                if newpath < D[i][j]:
                    P[i][j] = k
                    D[i][j] = newpath

def getPath(P, first, last):
    w = int(P[first][last])
    if w > 0:
        getPath(P, first, w)
        print(w)
        getPath(P, w, last)
        
# G1
INF = 999
n = 6
W1 = [
    [0, 5, INF, 11, INF, INF],
    [7, 0, 3, INF, INF, INF],
    [INF, INF, 0, INF, 1, INF],
    [INF, INF, INF, 0, INF, 20],
    [INF, 1, 3, 1, 0, 6],
    [INF, INF, INF, INF, INF, 0]
]

P1 = np.zeros((6,6))
D1 = np.zeros((6,6))
floyd(0, 5, W1, D1, P1)
print("G1")
print(" ")
print("W")
for i in range(6):
    for j in range(6):
        print(W1[i][j], end=' ')
    print()
print(" ")
print("D")
for i in range(6):
    for j in range(6):
        print(D1[i][j], end=' ')
    print()
print(" ")
print("P")
for i in range(6):
    for j in range(6):
        print(P1[i][j], end=' ')
    print()
print(" ")
print("print results from getPath:")
getPath(P1, 0, 5)

print(" ")
print(" ")
print(" ")

#G2
W2 = [
    [0, 5, INF, 1, 3, INF],
    [5, 0, 11, 5, 7, INF],
    [INF, 11, 0, INF, 4, 13],
    [1, 5, INF, 0, INF, 4],
    [3, 7, 4, INF, 0, 4],
    [INF, INF, 13, 4, 4, 0]
]

P2 = np.zeros((6,6))
D2 = np.zeros((6,6))
floyd(0, 5, W2, D2, P2)
print("G2")
print(" ")
print("W")
for i in range(6):
    for j in range(6):
        print(W2[i][j], end=' ')
    print()
print(" ")
print("D")
for i in range(6):
    for j in range(6):
        print(D2[i][j], end=' ')
    print()
print(" ")
print("P")
for i in range(6):
    for j in range(6):
        print(P2[i][j], end=' ')
    print()
print(" ")
print("print results from getPath:")
getPath(P2, 0, 5)

