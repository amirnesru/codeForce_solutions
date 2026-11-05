for i in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    slow = 0
    fast = k
    count = 0
    while fast <= n :
        if "0" not in set(s[slow:fast]) :
            count+=1
        fast+=k
        slow+=k
    print (count)        