for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(n - 1, 0, -1):
        if a[i] > b[i]:
            diff = a[i] - b[i]
            a[i] -= diff
            a[i - 1] += diff  
            a[i] = b[i]       
            
    
    if a[0] <= b[0]:
        print("YES")
    else:
        print("NO")