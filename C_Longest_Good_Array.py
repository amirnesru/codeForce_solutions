import math
for i in range (int(input())):
    l, r = map (int, input().split())
    print (int((-1 + math.sqrt(1 + 8 * (r-l))) // 2)+1)

