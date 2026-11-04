for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    total = 0
    i = 0
    while i < n:
        if arr[i] < 0:
            count += 1
            while i < n and arr[i] <= 0:
                total += abs(arr[i])
                i += 1
        else:
            total += arr[i]
            i += 1
    print(total, count)