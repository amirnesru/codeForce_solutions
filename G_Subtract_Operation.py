from collections import Counter
for i in range (int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    d = Counter(arr)
    for i in arr :
        val = i + k
        if val in d :
            if val != 0 or k != 0 :
                print("YES")
                break
    else:
        print("NO")