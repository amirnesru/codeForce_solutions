for i in range (int(input())):
    n, k = map(int, input().split())
    s=input()
    ans=0
    left = float("-inf")
    for i in range (n):
        if s[i] == '1':
            if i - left >=k :
                ans+=1
            left = i    
    print(ans)