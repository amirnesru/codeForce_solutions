for i in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    i = 0
    count = 0
    while i < n:
        if set(s[i:i+k]) == {"1"} and i+k <= n :
            count+=1
        i+=k
    print(count)

