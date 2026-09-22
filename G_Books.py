n,t = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
maximum = 0
sum = 0
for i in range(n) :
    sum+=arr[i]
    while sum > t:
        sum-=arr[left]
        left+=1
    maximum = max(maximum, i - left+1)    
print(maximum)
 
