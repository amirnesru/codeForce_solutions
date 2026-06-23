n = int(input())
arr = list (map (int, input().split()))
arr_1 = [0]*n
arr_2 = [0]*n
sum = 0
for i in range(n) :
    sum+=arr[i]
    arr_1[i]=sum
sum = 0
arr.sort()
for i in range(n) :
    sum+=arr[i]
    arr_2[i]=sum
    
for i in range (int(input())) :
    q,l,r = map(int, input().split())
    if q == 1:
        left = arr_1[l-2] if l > 1  else 0
        print (arr_1[r-1] - left)
    else:
        left = arr_2[l-2] if l > 1  else 0
        print (arr_2[r-1] - left )



