y,b,r = map(int, input().split())
x = min(y+2,b+1,r)
if x == r:
    print(r*3-3)
elif x == b+1:
    print(b*3)
else:
    print(y*3+3)    