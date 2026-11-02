for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) == n:
        print(-1)
    elif sum(arr)-arr[-1]-arr[0] == n-2 :
        print(arr[-1]+arr[0]-1) 
    else:
        print(sum(arr)-1)    