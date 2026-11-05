
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    arr = []
    possible = True
    for i in range(1, n + 1):
        x = ((l + i - 1) // i) * i
        if x > r:
            possible = False
            break
        arr.append(x)
    if possible:
        print("YES")
        print(*arr)
    else:
        print("NO")
