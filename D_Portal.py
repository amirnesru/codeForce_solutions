for _ in range(int(input())):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    left = arr[:x]
    inside = arr[x:y]
    right = arr[y:]
    outside = left + right
    if inside:
        m = inside.index(min(inside))
        inside = inside[m:] + inside[:m]
    pos = len(outside)
    for i in range(len(outside)):
        if outside[i] > inside[0]:
            pos = i
            break
    ans = outside[:pos] + inside + outside[pos:]
    print(*ans)