for i in range (int(input())):
    a,b = (input().split())
    a,b = list(a), list(b)
    x = b[0]
    b[0] = a[0]
    a[0] = x
    print("".join(a),"".join(b),)