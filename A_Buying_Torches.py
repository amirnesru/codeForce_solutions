for i in range(int(input())):
    x,y,k = map(int, input().split())
    need = k + y*k -1
    count = (need + x-2)//(x-1)
    print(count+k)    