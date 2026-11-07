for _ in range (int (input())):
    n,k = map(int, input().split())
    arr =list(map(int, input().split()))
    arr2 =list(map(int, input().split()))
    sum ,res,max_val = 0,0,0
    for i in range(min(n,k)):
        sum+=arr[i]
        max_val= max(max_val,arr2[i])
        res = max(res,sum+max_val*(k - i - 1))
    print(res)    
    