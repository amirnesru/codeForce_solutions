for i in range (int(input())):
    n = int(input()) 
    arr = list(map(int,input().split()))
    d = {}
    count = 0
    for i in range (n-1, -1,-1):
        if arr[i] in d :
            break
        else :
            d[arr[i]]  = i
            
            count+=1
    print(n-count)