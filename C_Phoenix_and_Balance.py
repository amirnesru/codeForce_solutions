for i in range(int(input())):
    n = int(input())
    a = (2**n) + (2**(n//2)-2)
    total = (2**(n+1))-2
    print(abs(a-(total-a)))