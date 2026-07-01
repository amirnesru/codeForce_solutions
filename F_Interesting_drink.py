n= int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range (int(input())):
    m = int(input())
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if arr[mid] <= m :
            left = mid +1
        elif arr[mid] > m:
            right = mid
    print (left)
            
                
