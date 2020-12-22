
def merge(a, left, right):
        n = len(left)
        m = len(right)
        #merged = [None]*(n+m)
        i = 0
        j = 0
        k = 0 
        while i < len(left) and j < len(right):
            if left[i]< right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        
def mergesort(a):
    n = len(a)
    if n>1:
        mid = round(n/2)
        left = a[:mid]
        right = a[mid:]
        mergesort(left) 
        mergesort(right)
        merge(a, left, right)

def merge_sort (a):
    n = len(a)
    if n>1:
        mid = round(n/2)
        left = a[:mid]
        right = a[mid:]
        merge_sort(left) 
        merge_sort(right)
        i = 0
        j = 0
        k = 0 
        while i < len(left) and j < len(right):
            if left[i]< right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

def factorial(n):
    if n == 1:
        return 1
    else :
        return n*factorial(n-1)