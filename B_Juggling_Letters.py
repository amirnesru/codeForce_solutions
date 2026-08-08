from collections import Counter
for i in range (int(input())):
    n = int(input())
    total_str = ""
    for i in range (n):
        s = input()
        total_str+=s
    d = Counter(total_str)
    for i in d :
        if d[i]%n != 0 :
            print("NO")
            break
    else:
        print("YES")        