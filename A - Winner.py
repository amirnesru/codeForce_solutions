from collections import defaultdict

d = defaultdict(int)
arr = []

for i in range(int(input())):
    name, num = input().split()
    num = int(num)
    d[name] += num
    arr.append((name, num))

mx = max(d.values())
temp = defaultdict(int)
for name, num in arr:
    temp[name] += num
    if temp[name] >= mx and d[name] == mx:
        print(name)
        break
