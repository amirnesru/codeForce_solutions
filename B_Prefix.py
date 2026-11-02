
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    low = high = arr[0]
    ans = arr[0]
    for i in range(1, n):
        orig = arr[i]
        ans = max(ans, orig + abs(low), orig + abs(high))
        low = orig + min(0, 2 * low)
        high = orig + max(0, 2 * high)
    print(ans)
