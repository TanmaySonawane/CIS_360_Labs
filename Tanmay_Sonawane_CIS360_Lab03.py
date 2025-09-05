# Tanmay Sonawane CIS 360 Lab 03
# 09/25/24

from collections import deque

def Task_A(A):
    n = len(A)
    stack = deque()
    
    for i in range(n):
        stack.append(A[i])
    for i in range(n):
        A[i] = stack.pop()
    return A

def Task_B(A):
    n = len(A)
    queue = deque()
    
    for i in range(n):
        queue.append(A[i])
    for i in range(n-1, -1, -1): 
        A[i] = queue.popleft()
    return A

def Task_C(A):
    n = len(A)
    for i in range(n//2):
        temp = A[i]
        A[i] = A[n-i-1]
        A[n-i-1] = temp
    return A

# Test arrays
Arr1 = [1,2,3,4,5]
Arr2 = [1,2,3,4,5,6]

# Make copies to avoid modifying the original arrays
Arr1_copy1 = Arr1[:]  # Copy for Task_A
Arr2_copy1 = Arr2[:]  # Copy for Task_B
Arr1_copy2 = Arr1[:]  # Copy for Task_C on Arr1
Arr2_copy2 = Arr2[:]  # Copy for Task_C on Arr2

print("Task_A result (Arr1):", Task_A(Arr1_copy1))  # Stack-based reversal
print("Task_B result (Arr2):", Task_B(Arr2_copy1))  # Queue-based, no reversal (same order)
print("Task_C result (Arr1):", Task_C(Arr1_copy2))  # In-place reversal
print("Task_C result (Arr2):", Task_C(Arr2_copy2))  # In-place reversal