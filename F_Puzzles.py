
n,m=map(int,input().split())
arr=list( map(int, input().split()))
arr.sort()
counter=[]
for i in range((m-n)+1):
    counter.append(arr[i+(n-1)] - arr[i])
print(min(counter))