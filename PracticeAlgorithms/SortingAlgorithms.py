from .DataStructures.MinHeap import MinHeap

import math

def insertion_sort(Arr):
    n = len(Arr)
    for j in range(1, n):
        key = Arr[j]
        i = j - 1

        while i >= 0 and Arr[i] > key:
            Arr[i + 1] = Arr[i]
            i -= 1
        
        Arr[i + 1] = key

    return Arr

def selection_sort(Arr):
    n = len(Arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if Arr[j] < Arr[min_index]:
                min_index = j
        
        tmp = Arr[i]
        Arr[i] = Arr[min_index]
        Arr[min_index] = tmp
    
    return Arr

def bubble_sort(Arr):
    n = len(Arr)
    for i in range(n - 1):
        for j in reversed(range(i + 1, n)):
            if Arr[j] < Arr[j - 1]:
                tmp = Arr[j]
                Arr[j] = Arr[j - 1]
                Arr[j - 1] = tmp

    return Arr

def heap_sort(Arr):
    min_heap = MinHeap(Arr)
    return (min_heap.pop() for _ in Arr)

def merge_sort(Arr):
    n = len(Arr)
    if n == 1: return Arr

    split_point = math.floor(n / 2)

    left_divide = Arr[:split_point]
    right_divide = Arr[split_point:]

    left_conquered = merge_sort(left_divide)
    right_conquered = merge_sort(right_divide)

    i = 0
    j = 0
    left_len = len(left_conquered)
    right_len = len(right_conquered)
    new_array = []

    while i < left_len and j < right_len:
        if left_conquered[i] < right_conquered[j]:
            new_array.append(left_conquered[i])
            i += 1

        else:
            new_array.append(right_conquered[j])
            j += 1

    return new_array

def quick_sort(Arr):
    return _quick_sort(Arr, 0, len(Arr) - 1)

def _quick_sort(Arr, l, r):
    if l < r:
        pivot = _partition(Arr, l, r)
        _quick_sort(Arr, l, pivot - 1)
        _quick_sort(Arr, pivot + 1, r)

    return Arr

def _partition(Arr, l, r):
    x = Arr[r]
    i = l - 1
    for j in range(l, r - 1):
        if Arr[j] < x:
            i += 1
            tmp = Arr[i]
            Arr[i] = Arr[j]
            Arr[j] = tmp
    
    tmp = Arr[i + 1]
    Arr[i + 1] = Arr[r]
    Arr[r] = tmp

    return i + 1