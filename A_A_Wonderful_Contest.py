for i in range (int(input())) :
    n = int(input())
    arr = list(map(int, input().split()))
    if 100 in arr :
        print("Yes")
    else:
        print("No")