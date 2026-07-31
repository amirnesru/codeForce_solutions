n,q = map(int , input().split())
arr =list(map(int , input().split()))
arr.sort()
sum_arr = [0]*(n+1)
sum1 = 0
for i in range (1,n+1):
    sum1+=arr[i-1]
    sum_arr[i] = sum1
for i in range (q):
    x,y = map(int , input().split())
    print(sum_arr[n-x+y] - sum_arr[n-x])
    

#   1 2 3 5 5 
# 0 1 3 6 11 16 