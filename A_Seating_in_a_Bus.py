for i in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = {a[0]}
    for i in range (1,n):
        if a[i]+1 not in ans and  a[i]-1 not in ans :
            print("NO")
            break
        ans.add(a[i])
    else:
        print("YES")    