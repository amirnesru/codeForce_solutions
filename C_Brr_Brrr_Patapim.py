for _ in range(int(input())):
    n = int(input())
    total_arr = []
    ans = [0] * (2 * n + 1)
    for i in range(n):
        arr = list(map(int, input().split()))
        total_arr += arr

    for i in range(len(total_arr)):
        x = i % n + 1          
        y = i // n + 1  

        if x + y <= 2 * n:
            ans[x + y] = total_arr[i]
    seen = set(ans)
    for i in range(1, 2 * n + 1):
        if i not in seen:
            ans[1] = i 
            break

    print(*ans[1:])