n , k  = map(int, input().split())
arr= list(map(int, input().split()))
count = 0 
for i in range (n):
    if arr[k-1]<= arr[i] and arr[i] !=0:
        count +=1
print(count)        

