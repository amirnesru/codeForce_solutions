for i in range(int(input())):
    n =int( input())
    if n % 2 != 0 or n < 4 :
        print(-1)
    else:
        if n%6 == 0 :
            x = n//6 
        else:
            x = n//6+1
        print(x,n//4)
         