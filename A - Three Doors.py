t=int(input())
for i in range(t):
    x=int(input())
    arr=list(map(int , input().split()))
    b=0
    while True:
        if arr[x-1]==0:
            break
        x=arr[x-1]
        b+=1   
    if b>=2:
        print('YES')
    else:
        print("NO") 

