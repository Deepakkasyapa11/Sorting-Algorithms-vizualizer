import random

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, j, j + 1  # Yield state for the visualizer

def quick_sort(data, start, end):
    if start >= end:
        return
    
    pivot = data[end]
    pivot_idx = start
    
    for i in range(start, end):
        if data[i] < pivot:
            data[i], data[pivot_idx] = data[pivot_idx], data[i]
            pivot_idx += 1
            yield data, i, pivot_idx
            
    data[pivot_idx], data[end] = data[end], data[pivot_idx]
    yield data, pivot_idx, end
    
    yield from quick_sort(data, start, pivot_idx - 1)
    yield from quick_sort(data, pivot_idx + 1, end)