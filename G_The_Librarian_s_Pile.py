for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    d = {}
    pos = 0
    count = m
    for i in range(n):
        d[arr[i]] = i + 1

    for i in range(m):
        if d[brr[i]] > pos:
            count += 2 * (d[brr[i]] - i - 1)
            pos = d[brr[i]]

    print(count)