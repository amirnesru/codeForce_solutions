
for _ in range(int(input())):
    n = int(input())
    abb = []
    ans = 0
    for i in range(n):
        arr = input()
        abb.append(arr)
    for i in range((n+1) // 2):
        for j in range(n // 2):
            count_1 = 0
            count_0 = 0
            if abb[i][j] == "0":
                count_0 += 1
            else:
                count_1 += 1
            if abb[j][n-1-i] == "0":
                count_0 += 1
            else:
                count_1 += 1
            if abb[n-1-i][n-1-j] == "0":
                count_0 += 1
            else:
                count_1 += 1
            if abb[n-1-j][i] == "0":
                count_0 += 1
            else:
                count_1 += 1
            ans += min(count_1, count_0)

    print(ans)
