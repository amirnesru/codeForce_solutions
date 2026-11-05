
from collections import Counter
for i in range(int(input())):
    n,m = map(int, input().split())
    s = input()
    ss= input()
    if n-m != 3 :
        print("NO")
    else:
        s = list(s)    
        d = Counter(s)
        for i in ss:
            if i in d and d[i]>=1:
                d[i]-=1
            else:
                print("NO")
                break
        else :
            if d['s'] == 1 and d['i'] == 1 and d['x'] == 1:
                print("YES")
            else:
                print("NO")