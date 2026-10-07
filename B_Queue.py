n = int(input())

arr = list(map(int, input().split()))

stack = []
answer = [-1] * n

for i in range(n):
    if not stack or arr[i] < arr[stack[-1]]:
        stack.append(i)

for i in range(n):
    left = 0
    right = len(stack) - 1
    pos = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[stack[mid]] < arr[i]:
            pos = stack[mid]
            left = mid + 1
        else:
            right = mid - 1

    if pos != -1:
        answer[i] = pos - i - 1

print(*answer)