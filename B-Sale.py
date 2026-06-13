n,m=map(int,input().split())
arr=list(map(int,input().split()))
count=0
arr.sort()
for i in arr:
    if i < 0 and m > 0 :
        count+=abs(i)
        m-=1
print(count)        

