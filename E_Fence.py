n, k = map (int , input(). split())
arr = list(map(int, input().split()))
sum = 0
max = float("inf")
left = 0
poi = 0
for i in range (n):
    sum+=arr[i]
    if i >= k-1 :
        if max > sum :
            max = sum
            poi = i+1-k
        sum-=arr[left]
        left+=1   
print(poi+1)            
