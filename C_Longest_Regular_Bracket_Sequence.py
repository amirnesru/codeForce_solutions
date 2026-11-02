from collections import Counter
s = input()
stack = [-1]
arr = []
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            count = i - stack[-1]
            arr.append(count)
if arr:
    d = Counter(arr)
    mx = max(arr)
    print(mx, d[mx])
else:
    print(0, 1)