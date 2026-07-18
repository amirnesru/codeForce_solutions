from collections import Counter
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = Counter(arr)
    arr1 = list(set(arr))
    arr1.sort()
    for i in range (n):
        if d[arr[i]] > 1 :
            while d[arr[i]] > 1 :
                arr1.append(arr[i])
                d[arr[i]] -= 1



    print(*arr1)