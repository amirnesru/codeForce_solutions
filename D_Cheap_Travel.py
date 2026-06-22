n, m, a, b = map(int, input().split())

if b < m * a:
    print(min((n // m * b) + (n % m * a), ((n + m - 1) // m) * b))
else:
    print(n * a)