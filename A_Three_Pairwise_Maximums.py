for i in range (int(input())):
    x,y,z = list(map(int, input().split()))
    if x == y == z :
        print("YES")
        print(x,x,x)
    elif x+y+z == 2*max(x,y,z) + min(x,y,z):
        print("YES")
        print(max(x,y,z),min(x,y,z),min(x,y,z))
    else:
        print("NO")    