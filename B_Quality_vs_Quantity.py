for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left = 1
    right = n-1
    sumB = arr[0]
    sumR = 0
    while left < right :
        sumR +=arr[right]
        sumB += arr[left]
        if sumR > sumB :
            print("YES")
            break
        
        left+=1
        right-=1
    else :
        print("NO")   