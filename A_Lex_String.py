for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = sorted(input())
    b = sorted(input())
    i = 0
    j = 0
    cntA = 0
    cntB = 0
    ans = []

    while i < n and j < m:
        if (a[i] < b[j] and cntA < k) or cntB == k:
            ans.append(a[i])
            i += 1
            cntA += 1
            cntB = 0
        else:
            ans.append(b[j])
            j += 1
            cntB += 1
            cntA = 0

    print("".join(ans))