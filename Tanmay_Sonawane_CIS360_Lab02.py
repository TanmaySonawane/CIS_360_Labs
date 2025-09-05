# Tanmay Sonawane CIS 360 Lab 02
# 09/18/24
import random

def MaxsubSlow(A):
    m = float('-inf') # 1 operation
    n = len(A) # 1 operation
    count = 3
    for j in range(n): # n operations
        for k in range(j,n): # n - j operations
            s = 0
            for i in range(j, k+1): # k+1 - j operations
                s += A[i] 
                count += 1
            if s > m:
                m = s
    return m, count

def MaxsubFaster(A):
    n = len(A)
    S = [0] * n
    S[0] = A[0]
    count = 4
    for i in range(1, n):
        S[i] = S[i-1] + A[i]
        count += 1
    m = float('-inf')
    for j in range(n):
        for k in range(j,n):
            count += 1
            if j == 0:
                s = S[k]
            else:
                s = S[k] - S[j-1]
            if s > m:
                m = s
    return m, count

def MaxsubFastest(A):
    n = len(A)
    if n == 0:
        return 0
    M = [0] * n
    M[0] = A[0]
    count = 5
    for t in range(1, n):
        M[t] = max(0, M[t-1] + A[t])
        count += 1
    m = float('-inf')
    for t in range(n):
        m = max(m, M[t])
        count += 1
    return m, count

for a in range(100, 1001, 100):
    A = [random.randint(-a,a) for _ in range(a)]
    return_values1 = MaxsubSlow(A)
    return_values2 = MaxsubFaster(A)
    return_values3 = MaxsubFastest(A)
    print(f'For array of length: {a}')
    print("MaxsubSlow: count = ", return_values1[1], "Max sum = ", return_values1[0], "Table Values:", return_values1[1]/a, return_values1[1]/(a ** 2), return_values1[1]/(a ** 3))  
    print("MaxsubFaster: count = ", return_values2[1], "Max sum = ", return_values2[0], "Table Values:", return_values2[1]/a, return_values2[1]/(a ** 2), return_values2[1]/(a ** 3))  
    print("MaxsubFastest: count = ", return_values3[1], "Max sum = ", return_values3[0], "Table Values:", return_values3[1]/a, return_values3[1]/(a ** 2), return_values3[1]/(a ** 3))  
    print('-' * 50)