for i in range (int(input())) :
    n = int(input())
    arr = list(map(int, input().split()))
    dif = (max(arr) - min(arr)) // 2
    print (( dif if (max(arr) - min(arr)) % 2==0 else dif + 1 ) )