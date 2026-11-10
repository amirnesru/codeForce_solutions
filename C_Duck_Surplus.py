for _ in range(int(input())):
    n = int(input())
    arr =list(map(int, input().split())) 
    ans = arr[0]
    for i in range(1,n):
        if ans > arr[i]:
            ans+=arr[i]
        else:
            ans = arr[i]
    print(ans)        