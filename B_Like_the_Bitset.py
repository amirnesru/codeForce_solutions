for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    cnt = 0
    ok = True

    for ch in s:
        if ch == '1':
            cnt += 1
            if cnt >= k:
                ok = False
                break
        else:
            cnt = 0
    if not ok:
        print("NO")
        continue
    print("YES")

    ones = []
    zeros = []

    for i in range(n):
        if s[i] == '1':
            ones.append(i)
        else:
            zeros.append(i)
    res = [0] * n
    val = 1
    for i in ones:
        res[i] = val
        val += 1
    for i in zeros:
        res[i] = val
        val += 1

    print(*res)