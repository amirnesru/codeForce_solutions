for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    even = 0
    odd = 0
    for i in range (n):
        if i%2 == 0:
            if arr[i]%2==1:
                even +=1
        else:
            if arr[i]%2==0:
                odd+=1
    if odd == even:
        print(even)
    else:
        print(-1)            