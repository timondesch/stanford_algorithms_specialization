def karatsuba(x,y):
    if x/10 < 1 and y/10 < 1:
        return x*y
    
    n = max(len(str(x)),len(str(y)))
    mid = n // 2

    l1 = x // 10**(mid)
    r1 = x % 10**(mid)
    l2 = y // 10**(mid)
    r2 = y % 10**(mid)

    a = karatsuba(r1,r2)
    b = karatsuba((l1+r1),(l2+r2))
    c = karatsuba(l1,l2)

    return (c * 10**(2*mid)) + ((b - c - a) * 10**(mid)) + (a)

x = int(input())
y = int(input())
print(karatsuba(x, y))
