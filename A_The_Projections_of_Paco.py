for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = arr[0] * 2
    for i in range(1, n):
        ans = (arr[i] - ans) * 2 + ans

    if n % 2 == 1:
        print(ans // 2)
    else:
        print(-ans // 2)
