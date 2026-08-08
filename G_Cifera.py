k = int(input())
l = int(input())
count = -1
while l % k == 0:
    l //= k
    count += 1
if count >= 0 and l == 1:
    print("YES")
    print(count)
else:
    print("NO")
