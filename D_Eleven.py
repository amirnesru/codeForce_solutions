from collections import Counter
n = int(input())
arr =0
if n ==1:
    print("O")
elif n ==2:
    print("OO")
elif n==3:
    print("OOO")
else:
    arr = [0]*n
    arr[0] =1
    arr[1] =1
    for i in range(2,n):
        arr[i] = arr[i-1]+arr[i-2]
    s =""    
    arr = set(arr)
    for i in range(1,n+1):
        if i in arr:
            s+="O"
        else:
            s+="o"
    print(s)