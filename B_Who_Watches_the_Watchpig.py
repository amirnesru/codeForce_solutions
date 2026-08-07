for i in range (int(input())):
    n,k = map(int, input().split())
    s = input()
   
    if k > (len(s))//2:
        print(-1)
    else:
        x = s[:k].count("R")
        y = s[n-k :].count("L")
        print(2*k -(x+y))