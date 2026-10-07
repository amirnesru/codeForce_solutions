for i in range (int(input())):
    n = int(input())  
    arr = list(map(int, input().split()))
    print(sum(arr)- min(arr)*n)
