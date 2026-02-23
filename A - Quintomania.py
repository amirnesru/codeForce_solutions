t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int ,input().split()))
    a=0
    for i in range (n-1):
        if abs(arr[i] - arr[i+1]) in (5, 7):
            a+=1
        else:
            print("NO")
            break
        if a==n-1:
            print("YES")
