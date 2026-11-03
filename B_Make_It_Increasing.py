
for i in range(int(input())):
    n =int(input())
    arr = list(map(int, input().split()))
    count = 0
    status = True
    for i in range(n-2,-1,-1):
        while arr[i+1] <= arr[i]:
            if arr[i+1] == 0:
                status = False 
                break
            count+=1
            arr[i]//=2
    if status:
        print(count)
    else:
        print(-1)