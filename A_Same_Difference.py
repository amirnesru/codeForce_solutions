for i in range (int(input())) :
    n = int(input())
    s = input()
    x = s.count(s[-1])
    print (len(s) - x)