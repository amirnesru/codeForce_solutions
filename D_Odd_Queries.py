for i in range(int (input())):
    n, q = map(int,input().split())
    arr = list(map(int,input().split()))
    arr1 = [0]*(n+1)
    sum1 = 0
    for i in range (1,n+1):
        sum1 +=arr[i-1]
        arr1[i]=sum1     
    for i in range (q):
        l, r, k = map(int,input().split()) 
        remain = arr1[-1] - (arr1[r]-arr1[l-1])
        if ((remain+((r-l+1)*k )) ) % 2 == 1:
            print("YES")
        else:
            print("NO")