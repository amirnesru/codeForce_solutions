for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * n
    i = 0 
    while i < n and n > 1:
        if arr[i] != i+1:
            ans[i] = i+1
            i += 1
        elif i + 1 < n:
            ans[i] = i + 2
            ans[i+1] = i + 1
            i += 2 
        else:
            ans[i] = i + 1
            i += 1      
    if arr[-1] == ans[-1]:
        ans[-1],ans[-2] = ans[-2],ans[-1]
    
    if n == 1:
        print(-1)
    else:
        print(*ans)