n,d = map(int,input().split())
arr = list(map(int,input().split()))
if sum(arr)+ (n-1)*10 > d :
    print(-1)
else :
    print((d-sum(arr))//5)