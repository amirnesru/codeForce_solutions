for i in range (int(input())):
    k,q = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    for i in range (q):
        if arr2[i] >= arr1[0]:
            arr2[i] = arr1[0]-1
    print(*arr2)        