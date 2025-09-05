# Tanmay Sonawane CIS 360 Lab 07
# 11/20/24

import numpy as np

quicksort_calls = 0
partition_calls = 0
quicksort_with_median_calls = 0
partition_with_median_calls = 0
quicksort_with_cutoff_calls = 0
quicksort_with_cutoff_calls2 = 0
insertion_sort_calls = 0

def quicksort(arr, low, high):
    global quicksort_calls
    quicksort_calls += 1
    if low < high:
        pivotpoint = partition(arr, low, high)
        quicksort(arr, low, pivotpoint-1)
        quicksort(arr, pivotpoint+1, high)
        
def partition(arr, low, high):
    global partition_calls
    partition_calls += 1
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort_with_median(arr, low, high):
    global quicksort_with_median_calls 
    quicksort_with_median_calls += 1
    if low < high:
        pivotpoint = partition_with_median(arr, low, high)
        quicksort_with_median(arr, low, pivotpoint-1)
        quicksort_with_median(arr, pivotpoint+1, high)

def partition_with_median(arr, low, high):
    global partition_with_median_calls 
    partition_with_median_calls += 1
    
    mid = (low + high) // 2
    #sorted_median = [arr[low], arr[mid], arr[high]]
    #sorted_median.sort()
    #pivot = sorted_median[1]
    
    if arr[low]<arr[mid] and arr[mid]<arr[high]:
        arr[low],arr[mid] = arr[mid],arr[low]
    elif arr[high]<arr[mid] and arr[low]<arr[high]:
        arr[high],arr[low] = arr[low],arr[high]
    elif arr[low]>arr[mid] and arr[low]<arr[high]:
        arr[low],arr[mid] = arr[mid],arr[low]

    pivotpoint = low
    pivot = arr[pivotpoint]
    i = low + 1
    j = high
    
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
        
def quicksort_with_cutoff(arr, low, high):
    global quicksort_with_cutoff_calls
    quicksort_with_cutoff_calls += 1
    cutoff = 10
    
    if low < high:
        pivotpoint = partition(arr, low, high) 
        left_len = pivotpoint - low
        right_len = high - pivotpoint
        if left_len <= cutoff:
            insertion_sort(arr, low, pivotpoint - 1)
        else:
            quicksort_with_cutoff(arr, low, pivotpoint - 1)
        if right_len <= cutoff:
            insertion_sort(arr, pivotpoint + 1, high)
        else:
            quicksort_with_cutoff(arr, pivotpoint + 1, high) 
                   
def insertion_sort(arr, low, high):
    global insertion_sort_calls
    insertion_sort_calls += 1
    
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort_with_cutoff2(arr, low, high):
    global quicksort_with_cutoff_calls2
    quicksort_with_cutoff_calls2 += 1
    cutoff = 10
    
    if low < high:
        pivotpoint = partition_with_median(arr, low, high) 
        left_len = pivotpoint - low
        right_len = high - pivotpoint
        if left_len <= cutoff:
            insertion_sort(arr, low, pivotpoint - 1)
        else:
            quicksort_with_cutoff2(arr, low, pivotpoint - 1)
        if right_len <= cutoff:
            insertion_sort(arr, pivotpoint + 1, high)
        else:
            quicksort_with_cutoff2(arr, pivotpoint + 1, high) 
            
test_arrs = [
    np.random.randint(100, size=100),
    np.random.randint(5000, size=5000),
    np.random.randint(50000, size=50000),
    np.random.randint(100000, size=100000)
]

for arr in test_arrs:
    arr_copy = arr.copy()
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    print(f"Sorted array (quicksort): {arr_copy[:10]} ...")
    print(f"Quicksort calls: {quicksort_calls}")
    print(f"Partition calls: {partition_calls}")
    print("\n")
    partition_calls = 0

    arr_copy = arr.copy()
    quicksort_with_median(arr_copy, 0, len(arr_copy) - 1)
    print(f"Sorted array (quicksort_with_median): {arr_copy[:10]} ...")
    print(f"Quicksort_with_median_calls: {quicksort_with_median_calls}")
    print(f"partition_with_median_calls: {partition_with_median_calls}")
    print("\n")
    partition_calls = 0

    arr_copy = arr.copy()
    quicksort_with_cutoff(arr_copy, 0, len(arr_copy) - 1)
    print(f"Sorted array (quicksort_with_cutoff): {arr_copy[:10]} ...")
    print(f"quicksort_with_cutoff_calls: {quicksort_with_cutoff_calls}")
    print(f"partition_calls: {partition_calls}")
    print(f"insertion_sort_calls: {insertion_sort_calls}")
    print("\n")
    partition_with_median_calls = 0
    insertion_sort_calls = 0
    
    arr_copy = arr.copy()
    quicksort_with_cutoff2(arr_copy, 0, len(arr_copy) - 1)
    print(f"Sorted array (quicksort_with_cutoff2): {arr_copy[:10]} ...")
    print(f"quicksort_with_cutoff_calls2: {quicksort_with_cutoff_calls2}")
    print(f"partition_with_median_calls: {partition_with_median_calls}")
    print(f"insertion_sort_calls: {insertion_sort_calls}")
    print("\n")
    print("\n")