from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    count = defaultdict(int)

    for i in range(n):
        val = arr[i] - i
        count[val] += 1

    x = 0

    for f in count.values():
        x += f * (f - 1) // 2

    print(x)
