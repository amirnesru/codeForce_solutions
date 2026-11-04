for i in range(int(input())):
    n = int(input())
    s = input()
    left = 0
    right = n-1
    while left< right:
        if s[left]!= s[right]:
            left+=1
            right-=1
        else:
            break
    print(right-left+1)        