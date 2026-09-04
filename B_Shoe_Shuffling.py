for _ in range (int(input())):
    n = int(input())
    stud = list(map(int,input().split()))
    ans = [0] * n
    i = 0
    while i < n:
        j = i
        while j < n and stud[j] == stud[i]:
            j += 1
        if j - i == 1:
            print(-1)
            break
        for k in range(i, j):
            ans[k] = k + 2 if k + 1 < j else i + 1

        i = j

    else:
        print(*ans)
