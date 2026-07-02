t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    left = 0
    right = n - 1
    ok = True
    for x in range(1, n + 1):
        if p[left] == x:
            left += 1
        elif p[right] == x:
            right -= 1
        else:
            ok = False
            break
    print("YES" if ok else "NO")