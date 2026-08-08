for i in range (int(input())):
    a, b, c, d = map(int, input().split())
    if (min(a,b) + 1)*2 < max(a,b) or (min(c-a, d-b) + 1)*2 < max(c-a, d-b):
        print("NO")
    else:
        print("YES") 

1