# Tanmay Sonawane Lab 01 CIS 360
import random

def sequential_search(Arr, x):
    i = 0
    while i <= len(Arr) - 1 and Arr[i] != x:
        i+=1
    if i == len(Arr):
        i = -1
    return i

def binary_search(Arr, x):
    low = 0
    high = len(Arr) - 1
    mid = 0
    count = 0
 
    while low <= high:
 
        count += 1
        mid = (high + low) // 2
        if Arr[mid] < x:
            low = mid + 1
        elif Arr[mid] > x:
            high = mid - 1
        else:
            return mid, count

    return -1 # element not found

Arr = sorted([random.randint(1, 1000) for _ in range(1000)])
Arr2 = sorted([random.randint(1, 100000) for _ in range(100000)])
Arr3 = sorted([random.randint(1, 1000000) for _ in range(1000000)])

x = random.randint(1,1000)
x2 = random.randint(1,100000)
x3 = random.randint(1,1000000)

print('For Array length 1000:')
index = sequential_search(Arr, x)
print(f'Element {x} found at index: {index} for Sequential search, it took {index} tries' if index != -1 else f'Element {x} not found\n')
if binary_search(Arr, x) == -1:
    print(f'Element {x} not found\n')
else: 
    index_B = binary_search(Arr, x)[0]
    count = binary_search(Arr, x)[1]
    print(f'Element {x} found at index: {index_B} for Binary Search, it took {count} tries\n')

print('For Array length 100,000:')
index = sequential_search(Arr2, x2)
print(f'Element {x2} found at index: {index} for Sequential search, it took {index} tries' if index != -1 else f'Element {x2} not found\n')
if binary_search(Arr2, x2) == -1:
    print(f'Element {x2} not found\n')
else: 
    index_B = binary_search(Arr2, x2)[0]
    count = binary_search(Arr2, x2)[1]
    print(f'Element {x2} found at index: {index_B} for Binary Search, it took {count} tries\n')
    
print('For Array length 1,000,000:')
index = sequential_search(Arr3, x3)
print(f'Element {x3} found at index: {index} for Sequential search, it took {index} tries' if index != -1 else f'Element {x3} not found\n')
if binary_search(Arr3, x3) == -1:
    print(f'Element {x3} not found\n')
else: 
    index_B = binary_search(Arr3, x3)[0]
    count = binary_search(Arr3, x3)[1]
    print(f'Element {x3} found at index: {index_B} for Binary Search, it took {count} tries\n')