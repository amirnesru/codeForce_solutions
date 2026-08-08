for _ in range(int(input())):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    start = max(l, L)
    end = min(r, R)
    if start > end:
        print(1)
    else:
        ans = end - start
        if l != L:
            ans += 1
        if r != R:
            ans += 1
        print(ans)
