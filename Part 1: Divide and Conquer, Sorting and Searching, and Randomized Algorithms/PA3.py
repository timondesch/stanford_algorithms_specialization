def QuickSort(A, l, r):
    if not (l < r):
        return
    m = Partition(A, l, r)
    QuickSort(A, l, m-1)
    QuickSort(A, m+1, r)
    return

def ChoosePivot(A, l, r):
    return l

def Partition(A, l, r):
    global comp
    comp += (r-l)
    p = ChoosePivot(A, l, r)
    pivot = A[p]
    A[p], A[l] = A[l], A[p]
    i = l+1
    for j in range(l+1, r+1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l] 
    return i-1

with open("QuickSort.txt", "r") as f:
    array = []
    for x in f:
        array.append(x)
comp = 0
QuickSort(array, 0, len(array)-1)
print(comp)
