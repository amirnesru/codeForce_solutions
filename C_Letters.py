from bisect import bisect_left
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total_arr = [0] * (n + 1)
total = 0
for i in range(1, n + 1):
    total += a[i - 1]
    total_arr[i] = total

for i in range(m):
    j = bisect_left(total_arr, b[i])

    print(j, b[i] - total_arr[j - 1])