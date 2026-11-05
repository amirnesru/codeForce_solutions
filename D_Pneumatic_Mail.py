for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
  
    for i in range(n):
        x = i+1
        y = arr[i]
        while x%2 == 0 :
            x//=2
        while y%2 == 0:
            y //=2            
        if x != y :
            print("NO")    
            break
    else:
        print("YES")    