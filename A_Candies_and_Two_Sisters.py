for i in range (int(input())):
    n = int(input())
    if n > 1 and n%2 == 0 :
        print(n//2-1)
    elif n > 1 and n%2 != 0:
        print(n//2)
    else:
        print(0)
