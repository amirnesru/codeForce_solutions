for i in range (int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr.index(min(arr))
    arr[x]+=1
    pro = 1
    for i in arr :
        pro *= i
    print(pro)    