total = 0
def quicksort(A, lo, hi):
    global total
    if lo < hi:
        total += len(A)-1
        n = hi+lo
        mid = int(n/2)
        if (A[mid] <= A[lo] < A[hi]) or (A[hi] <= A[lo] < A[mid]):
            p = partition_lo(A, lo, hi)

        if (A[mid] <= A[hi] < A[lo]) or (A[lo] <= A[hi] < A[mid]):
            p = partition_hi(A, lo, hi)
        else:
            p = partition_mid(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def quicksort_hi(A, lo, hi):
    global total
    if lo < hi :
        total += len(A)-1
        p = partition_hi(A, lo, hi)
        quicksort_hi(A, lo, p-1)
        quicksort_hi(A, p+1, hi)


def quicksort_lo(A, lo, hi):
    global total
    if lo < hi :
        p= partition_lo(A, lo, hi)
        quicksort_lo(A, lo, p-1)
        quicksort_lo(A, p+1, hi)
        total += len(A)-1

def quicksort_mid(A, lo, hi):
    global total
    if lo < hi :
        total += len(A)-1
        p = partition_mid(A, lo, hi)
        quicksort_mid(A, lo, p-1)
        quicksort_mid(A, p+1, hi)


def partition_hi(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        if A[j] < pivot:
            A[i],A[j] = A[j],A[i]
            i +=  1
    A[i],A[hi] = A[hi],A[i]
    return i

def partition_lo(A, lo, hi):
    pivot = A[lo]
    i = lo +1
    for j in range(lo+1,hi+1):
        if A[j] < pivot:
            A[i],A[j] = A[j],A[i]
            i +=  1
    A[i-1],A[lo] = A[lo],A[i-1]
    return i-1

def partition_mid(A, lo, hi):
    n = hi+lo
    mid = int(n/2)
    pivot = A[mid]
    i = lo
    j = hi
    while i<=j:
        while A[i] < pivot:
            i+=1
        while A[j] > pivot:
            j-=1
        if(i<=j):
            A[i],A[j] = A[j],A[i]
            i+=1
            j-=1
    return i-1

import os
import numpy as np
import pandas as pd
os.chdir('C:/Users/ituki/Documents/Classes/Coursera/Coursera_Algo')
li = np.array(pd.read_table('QuickSort.txt', header=None)[0])
total = 0
quicksort_hi(li, 0, len(li)-1)
print(len(li),total)
li = np.array(pd.read_table('QuickSort.txt', header=None)[0])
total = 0
quicksort_lo(li, 0, len(li)-1)
print(len(li),total)
li = np.array(pd.read_table('QuickSort.txt', header=None)[0])
total = 0
quicksort(li, 0, len(li)-1)
print(len(li),total)