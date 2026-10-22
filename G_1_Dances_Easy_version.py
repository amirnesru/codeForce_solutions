for i in range(int(input())):
    n,m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1 = [1]+arr1 
    arr1.sort()
    arr2.sort()
    slow = n-1
    fast = n-1
    count = 0
    while slow >=0 and fast >=0 :
        if arr1[fast] >= arr2[slow]:
            count+=1
            fast-=1
        else:
            fast-=1
            slow-=1
    print (count)      
            
            