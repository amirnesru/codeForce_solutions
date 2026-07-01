for i in range (int(input())):
    n=int(input())
    arr = list(map(int, input().split()))
    sum = 0
    res = []
    for i in range(n):
        sum+=arr[i]
        average = sum // (i+1)
        if not res :
            res.append(average)
        else:
            res.append(min(res[-1],average))
    print(*res)    