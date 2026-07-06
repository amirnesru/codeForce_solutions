n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0]*n
arr_sum_rev = [0]*n
sum1 = 0
sum2 = 0
for i in range(1,n):
    if arr[i-1] - arr[i] > 0 :
        sum1 += arr[i-1] - arr[i]
        arr_sum[i] = sum1
    else:
        arr_sum[i] = sum1
for i in range(n-2,-1,-1):
    if arr[i+1] - arr[i] > 0 :
        sum2 += arr[i+1] - arr[i]
        arr_sum_rev[i] = sum2 
    else :
        arr_sum_rev[i] = sum2    

for i in range (m):
    s, t = map(int, input().split())
    if s < t :
        print(arr_sum[t-1]-arr_sum[s-1])
    else:
        print(arr_sum_rev[t-1]-arr_sum_rev[s-1])