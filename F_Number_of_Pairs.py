for i in range (int(input())):
    n,l,r = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    couner = 0
    left = 0
    right = n-1
    right_l = n-1
    while left < right :
        if arr[left]+arr[right] < l :
            left +=1
        elif arr[left]+arr[right] > r:
            right-=1 
        else :
            if right_l < left:
                right_l = left
            while right_l > left and arr[left]+arr[right_l] >=l:
                right_l-=1    
            couner+=(right-right_l)
            left+=1
    print(couner) 
