t=int(input())
for i in range(t):
    n,k=map(int , input().split())
    arr=list(map(int ,input().split()))
    arr.sort()
    abb=list(map(int ,input().split()))
    abb.sort(reverse=True)
    for i in range(n):
         a=max(abb)
         if k == 0:
              break
         if arr[i]<a:
              arr[i]=a
              k-=1
              abb.remove(abb[0])
    print(sum(arr))          

    
