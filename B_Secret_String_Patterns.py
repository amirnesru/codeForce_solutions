import sys
 
for _ in range(int(input())):
    n = int(input())
    print("?", 1, n)
    sys.stdout.flush()
    ct = int(input())
    if ct == 0:
        print("! NO")
        continue
    print("?", 1, ct)
    sys.stdout.flush()
    x = int(input())
    if x == ct:
        print("! NO")
    else:
        print("! YES")