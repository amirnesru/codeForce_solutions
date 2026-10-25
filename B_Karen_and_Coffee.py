n, k, q = map(int, input().split())
arr = [0]*200001
for i in range (n):
    l, r = map(int, input().split())
    arr[l-1]+=1
    arr[r]-=1
for i in range (1,len(arr)):
    arr[i]+=arr[i-1]
for i in range(len(arr)):
    if arr[i] >= k :
        arr[i] = 1
    else:
        arr[i] = 0
for i in range (1,len(arr)):
    arr[i]+=arr[i-1]     
arr = [0]+arr
for i in range(q):
    a,b = map(int, input().split())
    print (arr[b]- arr[a-1])
    