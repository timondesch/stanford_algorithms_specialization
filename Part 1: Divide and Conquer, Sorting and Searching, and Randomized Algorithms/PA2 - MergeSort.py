def mergesort(a):
    length = len(a)
    if length == 1:
        return a
    m = length//2

    l = mergesort(a[:m])
    r = mergesort(a[m:])

    return Merge(l, r)

def Merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while a:
        c.append(a[0])
        a.pop(0)
    while b:
        c.append(b[0])
        b.pop(0)
    return c

print(mergesort([3,2,1]))
