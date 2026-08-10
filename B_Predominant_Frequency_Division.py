for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    left = [0] * (n + 1)
    middle = [0] * (n + 1)
    for i in range(n):
        if arr[i] == 1:
            left[i + 1] = left[i] + 1
            middle[i + 1] = middle[i] + 1
        else:
            left[i + 1] = left[i] - 1
            if arr[i] == 2:
                middle[i + 1] = middle[i] + 1
            else:
                middle[i + 1] = middle[i] - 1

    for i in range(1, n - 1):
        if left[i] < 0:
            continue
        for j in range(i + 1, n):
            if middle[j] - middle[i] >= 0:
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")