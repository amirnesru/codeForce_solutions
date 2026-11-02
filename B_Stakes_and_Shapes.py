for i in range(int(input())):
    x, y, z = map(int, input().split())
    val = max(x,y,z)
    if val == z:
        print((x+y+z)*"S")
    elif val == x:
        print((x+y+z)*"P")
    else:
        print((x+y+z)*"R")
        